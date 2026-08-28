# GelaVit — nový statický e-shop

Kompletná náhrada za WordPress. Žiadna databáza, žiadny PHP, žiadne pluginy na aktualizáciu.
Nahráte priečinok `site/` na hosting a web beží.

---

## 1. Čo je v balíku

```
site/                  ← TOTO nahráte na hosting (je to hotový web)
  index.html           domovská stránka (SK)
  produkty.html        výpis produktov
  produkt-*.html       8 detailov produktov
  kosik.html           košík
  pokladna.html        pokladňa
  dakujeme.html        potvrdenie objednávky
  o-nas.html           o nás
  blog.html + clanok-*.html   7 článkov
  kontakt.html         kontakt a predajné miesta
  ako-objednat.html    návod na objednanie
  obchodne-podmienky.html
  ochrana-osobnych-udajov.html
  404.html
  en/                  celá anglická mutácia
  de/                  celá nemecká mutácia
  assets/css/style.css design systém
  assets/css/motion.css animácie
  assets/js/shop.js    košík a pokladňa
  assets/js/motion.js  animácie a interakcie
  assets/img/          fotky (WebP + fallback), odznaky, logo
  sitemap.xml, robots.txt, .htaccess, _redirects

gen/                   ← generátor (nemusí byť na hostingu)
  products.json        CENY, SKLADOM, popisy produktov  ← tu upravujete
  i18n.py              všetky texty webu (SK/EN/DE)
  content.py           články a právne stránky
  images.py            spracovanie fotiek do WebP/PNG
  src-images/          zdrojové fotky (vaše originály)
  templates/           HTML šablóny
  build.py             spúšťač
```

---

## 2. Ako web spustiť naživo

1. Cez FTP/File manager nahrajte **obsah priečinka `site/`** do koreňa webu (`public_html`).
2. Súbor `.htaccess` musí ísť tiež (je skrytý — v FTP klientovi zapnite zobrazenie skrytých súborov).
   Obsahuje 301 presmerovania zo starých WordPress adries, takže SEO sa neztratí.
3. Na Netlify/Vercel použite namiesto `.htaccess` súbor `_redirects` (je tam tiež).

**Dôležité:** starý WordPress najprv zálohujte, potom zmažte `wp-*` súbory. `.htaccess` v balíku
posiela staré `/wp-content/...` adresy na `410 Gone`, aby ich Google vyhodil z indexu.

---

## 3. Ako meniť ceny a skladovú dostupnosť

Otvorte `gen/products.json`. Pri každom produkte:

```json
"price": 16.90,      ← cena v EUR s DPH
"stock": true,       ← true = skladom, false = vypredané
"featured": true,    ← true = zobrazí sa na domovskej stránke a dostane odznak Bestseller
```

Potom spustite (potrebný Python 3 a knižnica Jinja2):

```bash
pip install jinja2
python3 gen/build.py
```

Web sa prebuduje v priečinku `site/`. Nahráte znova na hosting.

> **Ceny sú zatiaľ odhad.** Vo WordPress exporte neboli uvedené žiadne ceny (WooCommerce mal prázdne
> `_regular_price`). Nastavil som ich podľa konkurencie na slovenskom trhu — Inca Collagen,
> KolagenDrink, Skin Collagen. Prepíšte ich na skutočné.

---

## 4. Kam chodia objednávky

Objednávka sa odosiela e-mailom cez službu **FormSubmit** (zadarmo, bez registrácie).
V `gen/build.py` hore nájdete:

```python
ORDER_ACTION   = "https://formsubmit.co/info@gelavit.sk"
CONTACT_ACTION = "https://formsubmit.co/info@gelavit.sk"
```

**Prvá objednávka:** FormSubmit vám pošle na `info@gelavit.sk` aktivačný e-mail — kliknete na odkaz
a od tej chvíle chodia objednávky rovno do schránky.

Alternatívy, ak chcete krajšie e-maily alebo Zapier/Make napojenie:

| Služba | Zadarmo | Poznámka |
|---|---|---|
| FormSubmit | áno, neobmedzene | nastavené, netreba účet |
| Formspree | 50 správ/mesiac | pekné notifikácie, štatistiky |
| Netlify Forms | 100/mesiac | ak hostujete na Netlify |
| Web3Forms | 250/mesiac | jednoduché API |

Stačí prepísať URL v `build.py` a znova spustiť build.

---

## 5. Fotky

Na webe sú **vaše skutočné fotky** z priečinka `pictures/`. Nie sú tam nahodené — prešli
spracovaním v `gen/images.py`:

- packshoty sa orežú, vycentrujú do štvorca na krémovom pozadí a dostanú jemný tieň,
- všetko sa exportuje do **WebP + PNG/JPG fallbacku** v dvoch šírkach (`srcset`),
- lifestyle fotky sa zmenšia na max. 1600 px a skomprimujú,
- odznaky (97 %, BIO, hydrolyzovaný kolagén, Vyrobené na Slovensku) sa orežú na priehľadné pozadie,
- z fotky `hero-trio` sa vygeneruje Open Graph obrázok 1200 × 630 px pre zdieľanie na sieťach.

Zdrojové súbory sú v `gen/src-images/`. Ak chcete niektorú fotku vymeniť, prepíšte súbor
v tomto priečinku (rovnaký názov) a spustite `python3 gen/build.py`.

**Logo** je vaše originálne vektorové `gelavit_logo_dark.svg` — v hlavičke tmavá verzia,
v pätičke automaticky vygenerovaná svetlá.

### Čo som upratal v priečinku `pictures/`

Bolo tam **4 226 súborov / 368 MB**, z toho presne polovica boli WordPressom generované
miniatúry (`nazov-300x300.png`, `nazov-570x570.bk.png` …) — každý obrázok existoval
v 15–20 kópiách.

Nová štruktúra:

```
pictures/
  _originaly/          179 skutočných originálov, roztriedených
    produkty/    48    packshoty a balenia
    odznaky/     35    97 %, BIO, Made in Slovakia, ikony
    blog/        36    fotky z výstav, ochutnávok, článkov
    logo-a-znacka/ 9   logá vo všetkých verziách + favicon
    fotky/        7    široké produktové fotky pre bannery
    ostatne/      6
  _zmazat/       4 047 duplikátov (344 MB) — po kontrole zmažte celý priečinok
```

Priečinok `_zmazat/` som **nezmazal** — nechal som to na vás. Keď si overíte, že nič
nechýba, môžete ho vymazať a ušetríte 344 MB.

---

## 6. Čo som z pôvodného webu nepreniesol (zámerne)

**Váš blog bol hacknutý.** V exporte je 42 spamových článkov o online kasínach
(„Golden Tiger Casino 50 Free Spins“, „Hracie Automaty Betsoft Casino“ …), pridaných
4. 12. 2025. Zničili vám SEO a Google vás pravdepodobne kvôli nim penalizuje.

Do nového webu som ich nevzal. Odporúčam navyše:

1. V Google Search Console skontrolovať **Bezpečnostné problémy** a **Manuálne opatrenia**.
2. Cez `.htaccess` v balíku sa staré spam URL vrátia ako `410 Gone` → Google ich vyhodí z indexu.
3. Zmeniť všetky heslá (WordPress admin, FTP, databáza, hosting).

Ďalej som nepreniesol: WooCommerce účty zákazníkov (nový web ich nepotrebuje),
prázdne testimonials a duplicitné produkty označené „(Kópia)“.

---

## 7. Právne texty

`obchodne-podmienky.html` a `ochrana-osobnych-udajov.html` som prevzal z pôvodného webu
a sprehľadnil. **Dajte ich skontrolovať právnikovi** — pravidlá o odstúpení od zmluvy,
reklamáciách a alternatívnom riešení sporov sa od roku 2022 menili. Text upravíte
v `gen/content.py` (premenné `TERMS` a `PRIVACY`).

Cookie lišta zatiaľ nie je potrebná — web používa iba technicky nevyhnutné úložisko prehliadača
pre košík, žiadne analytické ani reklamné cookies. Ak pridáte Google Analytics alebo Meta Pixel,
cookie lištu doplniť treba.

---

## 8. Animácie a motion

Web je postavený tak, aby obstál na [awwwards.com](https://www.awwwards.com/) — ale nie na úkor
predaja. Všetko beží na `transform` a `opacity` (teda na GPU), celá vrstva má ~14 kB
(`assets/js/motion.js` + `assets/css/motion.css`) a nepoužíva žiadnu knižnicu.

### Podpis stránky — tri momenty

1. **Intro** — logo sa nadýchne, počítadlo dobehne do 100, tmavá clona odíde hore.
   Zobrazí sa raz za reláciu (`sessionStorage`), nie pri každom kliknutí.
2. **Pripnutá scéna príchutí** — sekcia sa „zamkne" na obrazovke a ako scrollujete,
   produkt sa mení, pozadie sa preleje do farby danej príchute, text sa prepíše
   a bočný indikátor ukazuje postup. Na mobile sa mení klikom na bodky.
3. **Horizontálny rail** — vertikálny scroll posúva produkty do strany. Na mobile
   sa z toho stane carousel so snapovaním.

### Ostatné

| Efekt | Kde |
|---|---|
| Inertia scroll (tlmené rolovanie s dojazdom) | celý web, desktop |
| Vlastný kurzor — mení sa na odkazoch, nad kartou ukáže „Pozrieť" | desktop |
| Filmové zrno cez celú stránku | všade |
| Nadpisy vystupujú po slovách spod masky | h1 a nadpisy sekcií |
| Plávajúce farebné aury, Ken Burns na fotke, paralax | hero |
| Pečať 97 % dopadne a otáča sa so scrollom | hero |
| Obrázky sa odhalia clip-path stierkou zdola | fotky, packshoty, banner |
| Nekonečný pás s claimami | pod hero |
| Počítadlá 0 → 97 % | sekcia „Zloženie bez kompromisov" |
| 3D náklon karty za kurzorom + lesk | produktové karty |
| Magnetické tlačidlá | primárne a tmavé CTA |
| Produkt priletí do košíka, košík poskočí | „Do košíka" |
| Prechod medzi stránkami (fade + posun) | všetky odkazy |
| Kruhové otvorenie mobilného menu | mobil |
| Ukazovateľ prečítania, hlavička sa skryje pri scrolle nadol | všade |

### Prístupnosť a výkon

- `prefers-reduced-motion` vypne **úplne všetko** — žiadne intro, žiadny kurzor,
  žiadny inertia scroll, obsah je okamžite viditeľný a statický.
- Kurzorové efekty a inertia scroll sa zapnú len na `(hover: hover) and (pointer: fine)` —
  na mobile a tablete vôbec nebežia.
- Jediná `requestAnimationFrame` slučka pre celý web (nie desať samostatných).
- Preskočiť na obsah, viditeľný focus, `aria-current`, `aria-live` na počte v košíku.

Ak chcete niektorý efekt vypnúť, zakomentujte jeho blok v `assets/css/motion.css` —
JavaScript sa nerozbije.

---

## 9. Technické parametre

- **Bez závislostí** — žiadny React, jQuery ani build krok pre prehliadač. Iba HTML, CSS a ~18 kB JS.
- **Košík** v `localStorage` — prežije zatvorenie okna, nič neodchádza na server až do odoslania.
- **SEO:** hreflang pre SK/EN/DE, canonical, Open Graph s obrázkom, JSON-LD
  (Organization, Product, FAQPage), `sitemap.xml`, `robots.txt`.
- **Obrázky:** WebP s PNG/JPG fallbackom, `srcset` + `sizes`, lazy loading,
  pevné `width`/`height` proti poskakovaniu rozloženia.
- **Prístupnosť:** viditeľný focus, `aria-current`, `aria-live` na počte v košíku, kontrast textu
  ≥ 4.5:1, rešpektuje `prefers-reduced-motion`.
- **Responzívne** od 320 px, hamburger menu pod 860 px.
- Funguje aj **bez JavaScriptu** (obsah je viditeľný, len košík nefunguje).

---

## 10. Design systém

| Token | Hodnota | Použitie |
|---|---|---|
| `--bg-base` | `#FBF8F3` | teplá krémová — hlavné pozadie (60 %) |
| `--bg-sand-soft` | `#F6F0E7` | striedavé sekcie |
| `--bg-ink` | `#14283A` | tmavé sekcie a pätička |
| `--fg-primary` | `#16283A` | text (30 %) |
| `--fg-secondary` | `#5E7183` | sekundárny text |
| `--brand` | `#E2573C` | koralová — iba CTA a akcenty (10 %) |
| `--sage` | `#6F8F73` | zelené „organické“ signály |

Písma: **Fraunces** (nadpisy, organický serif) + **Inter** (text). Obe z Google Fonts.
Pôvodné firemné farby (`#2a4163` navy, `#f15d47` koralová) som zachoval, len zladil.

Krivky animácií: `cubic-bezier(.22, 1, .36, 1)` pre príchody, `cubic-bezier(.33, .9, .3, 1)`
pre stavy. Hover 150–250 ms, odhalenia 550–950 ms.


## Farebná vrstva a idle animácie (verzia 3)

Päť farieb kvapky z loga je teraz systém, nie ozdoba. Tokeny sú v `style.css`:

| Token | Hex | Text-varianta (kontrast na bielej) |
|---|---|---|
| `--c1` | `#C9DC50` limetková | `--ct1` `#7E9612` |
| `--c2` | `#F04E4A` koralová | `--ct2` `#E03430` |
| `--c3` | `#84B939` zelená | `--ct3` `#5F8A26` |
| `--c4` | `#5FBEEC` obloha | `--ct4` `#1B8FC8` |
| `--c5` | `#0086B5` modrá | `--ct5` `#006C92` |

`--cN` sa používa na **plochy** (kvapky, disky, prúžky, bodky), `--ctN` na **text a ikony**,
aby všetko prešlo kontrastom. Každý produkt má v `gen/products.json` pole `hue` — z neho
vychádza farba karty, kategórie, štítku, disku v showcase a plochy na detaile produktu.

### Čo sa hýbe bez skrolovania

| Prvok | Animácia | Trvanie |
|---|---|---|
| Kvapky v hero | plynutie + rotácia + zmena mierky | 14 / 17 / 21 s |
| Bodky v hero | pulz | 5,5 s |
| Zvislé prúžky | zmena výšky | 6,5 s |
| Farebná doska za fotkou | cyklus piatich farieb loga | 24 s |
| Pečať 97 % | rotácia kruhového textu | 26 s |
| Ticker „Pre kĺby / pleť / vlasy…" | zvislé prepínanie šiestich slov | 13,2 s |
| Farebný pás pod hlavičkou | nádych piatich políčok | 4,4 s |
| Disk za balením v showcase | dýchanie + mierna rotácia | 9 s |
| Kvapka v hlavičke podstránok | plynutie | 20 s |
| Bodky v marquee | pulz | 6 s |

Všetko je v `motion.css` v bloku **14. Idle motion** a celé sa vypína
pri `prefers-reduced-motion: reduce` (ticker vtedy zobrazí len prvé slovo).

Texty tickera sa menia v `gen/i18n.py` v kľúči `hero_rotate` (musí ich byť **presne šesť**,
inak sa rozbije časovanie keyframu `tick`). Text v pečati je `seal_ring` — maximálne
~46 znakov, inak sa v kruhu prekryje.


## Hero: kruhová produktová scéna (verzia 4)

Hero už nie je fotka, ale **pripnutá scéna** — funguje rovnako ako sekcia 03:

- `.hero` je vysoká `100vh + (počet produktov − 1) × 24vh`, vnútro `.hero-pin` je `position: sticky`
- ako roluješ, prepína sa produkt v kruhu; text vľavo (H1, ticker, lead, tlačidlá) zostáva stáť
- farebný disk za balením a linka postupu dole preberajú `hue` práve aktívneho produktu
- bodky po obvode kruhu sú klikacie — skočia na príslušnú výšku scény
- pod 980 px šírky a pri `prefers-reduced-motion` sa pripnutie vypne, hero je bežná sekcia
  a bodky prepínajú produkt klikom

Riadi to `heroScene()` v `motion.js`. Dĺžku scény zmeníš hodnotou `24vh`
v `.hero { height: calc(...) }` v `style.css`.

### Organický tvar namiesto kruhu

Za produktom v hero scéne, v showcase aj na detaile produktu je **nepravidelný
tvar odvodený od farebných polí na obale** — nie kruh. Je to jedna SVG cesta
(`.blob`) použitá trikrát: raz ako výplň (16 % krytie) a dvakrát ako obrys,
zakaždým inak otočený. Tým vzniká vrstvenie kriviek ako na obale.

Farbu berie z premennej `--shape`, ktorú nastavuje:

- `.hero-stage` — z `--stage-hue`, ktorú prepína JavaScript pri rolovaní,
- `.showcase-slide` a `.pdp-stage` — z `--hue` daného produktu.

Tvar sa pomaly otáča a mierne mení mierku (26 / 34 / 41 s, každá vrstva inak),
pri `prefers-reduced-motion` stojí.

### Vyrezanie packshotov

Farebný tvar je **za** produktom, takže produkt musí mať skutočnú alfu.
Robí to `cutout()` v `gen/images.py`. Samotný prah na to nestačí: biele plochy
na obale (etiketa fľaše, predná stena krabičky) sú rovnako svetlé ako pozadie
a miestami doň prechádzajú bez viditeľnej hrany. Postup je preto trojkrokový:

1. maska svetlých nefarebných pixelov spojených s okrajom obrázka — pred
   hľadaním sa maska zeroduje a späť dilatuje, čím sa prerežú úzke krčky,
   ktorými pozadie „presakuje" do bielej etikety,
2. z objektu sa odstránia drobné škvrny,
3. každý riadok sa vyplní medzi krajnými bodmi objektu. Všetky obaly sú
   vodorovne súvislé, takže sa tým doplní aj biela plocha, ktorá s pozadím
   splýva.

Tá istá silueta sa použije pre obe verzie: na karte sedí produkt na krémovej
ploche bunky, v scénach má priehľadné pozadie.

### Pásová fotka celej rady

`gen/band.py` **neprekresľuje** fotku — opravuje na nej len to, čo je zle.
Originál (`gen/src-images/_raw/rada-siroka.jpg`) mal šesť produktov, z toho
**dve rovnaké vrecká Ananás**, a chýbal **Ananás Box**. Skript preto:

1. vygumuje šieste (duplicitné) vrecko — pozadie je vodorovne takmer rovnaké,
   takže sa vyplní priemerným stĺpcom z overene čistého pásu medzi vreckami,
2. na uvoľnené miesto položí reálny packshot Ananás Boxu; jeho silueta sa
   berie ako **konvexný obal** masky, aby mal kartón rovné hrany bez schodíkov,
3. doladí jas a teplotu na svetlo fotky a pridá mäkký tieň v smere svetla.

Zvyšok fotky zostáva presne taký, aký bol.

Spustenie po zmene sortimentu: `python3 gen/band.py && python3 gen/build.py`


## Responzivita a kompatibilita

Overené na 320 / 360 / 390 / 412 / 430 / 744 / 820 / 1024 / 1180 / 1280 / 1440
a 1920 px, plus na nízkych oknách (720 px výšky). **Žiadna stránka nikde
vodorovne nepreteká.**

### Hlavička na mobile

Pod 860 px sa hlavička prestavia tak, aby logo dostalo priestor:

- logo `clamp(132px, 38vw, 168px)` — na telefóne je viac než dvojnásobné oproti
  pôvodnému stavu,
- prepínač jazyka z hlavičky zmizne (je v mobilnom menu),
- košík je len ikona 44 × 44 px s červenou bublinkou počtu; pri prázdnom košíku
  sa bublinka nezobrazuje,
- burger 44 × 44 px.

### Čo sa ešte opravilo

| Problém | Riešenie |
|---|---|
| Na 320 px pretekala hlavička o 25 px | kompaktná hlavička + `clamp` na logo |
| Pätička rozšírila stránku o 21 px | `.social` sa zalamuje, položky mriežok majú `min-width: 0` |
| Preloader pretekal na úzkych telefónoch | `max-width: 100vw; overflow: hidden` |
| Malé dotykové ciele (jazyk, pätička, odkazy) | pod 860 px a pri `hover: none` majú aspoň 44 px |
| Zaškrtávacie polia 13 × 13 px | 20 × 20 px, riadok 44 px |
| iOS zoomoval pri kliknutí do formulára | polia majú na mobile `font-size: 16px` |
| `100vh` na mobilnom Safari skáče | `100svh` cez `@supports` |
| Pripnuté scény sa na dotyku ovládali ťažko | pri `hover: none` sú scény statické a prepínajú sa klikom |
| Hero sa nezmestil do nízkeho okna (1280 × 720) | `@media (max-height: 860px)` zmenší typografiu aj scénu |
| Výrez na iPhone | `env(safe-area-inset-*)` v `.wrap` a v mobilnom menu |
| Počet v bublinke splynul s pozadím | po „pop" animácii ostáva na mobile biely |

### Kompatibilita prehliadačov

Bez experimentálnych vlastností. Kde by mohol byť problém, je záložka:

- `100svh` je v `@supports`, inak `100vh`
- jednotky kontajnera (`cqi`) sú v `@supports`, inak pevná hodnota v px
- `:has()` má záložku cez triedu `.is-chosen`, ktorú nastaví JavaScript
- `-webkit-line-clamp` doplnené o štandardné `line-clamp`
- `textPath` má aj `xlink:href` pre staršie Safari
- `localStorage` je celý v `try/catch` (súkromné okno Safari)
- obrázky idú cez `<picture>`: WebP s JPG/PNG záložkou


## Hero na veľkých obrazovkách a bočné nadpisy

### Väčší nadpis a produkt

Meta riadok (97 % / 5 g / 2015) a linka postupu scény sú od tejto verzie
v samostatnom `.hero-foot`, ktorý je nad 980 px **ukotvený na spodok
pripnutia** (`position: absolute`). Mriežka tak dostala celú výšku okna
a nadpis aj produkt mohli narásť:

| | predtým | teraz |
|---|---|---|
| Nadpis pri 1440 × 900 | 63 px / riadok | **75 px / riadok** |
| Tvar s produktom pri 1440 × 900 | 414 px | **504 px** |
| Nadpis pri 1280 × 720 | 34 px | **43 px** |
| Tvar pri 1280 × 720 | 274 px | **324 px** |

Veľkosti sú viazané na šírku **aj** výšku okna:
`clamp(2.4rem, min(5.4vw, 8.6vh), 6.4rem)` pre nadpis a
`min(580px, 56vh)` pre tvar. Na nízkych oknách ich blok 22.7 zmenší tak,
aby sa scéna vždy zmestila na jednu obrazovku — overené na
1024 × 700, 1280 × 720, 1440 × 900, 1680 × 1050 a 1920 × 1080.

`.hero-foot` musí byť **mimo** `.hero-grid` — tá má `position: relative`,
takže by inak bola kotvou pre absolútne umiestnenie namiesto `.hero-pin`.

### Bočné nadpisy sa už neorezávajú

Sekcie 02, 07, 09 a 10 mali stĺpce nastavené priamo v HTML
(`style="grid-column:6/13"`), čo médiá dotazy nevedeli prebiť — na telefóne
zostal nadpis v úzkom stĺpci a orezal sa uprostred písmena. Inline štýly
nahradili triedy `.col-main` a `.col-aside`, ktoré sa pod 900 px roztiahnu
na celú šírku. Doplnené je aj `overflow-wrap: break-word` na všetky nadpisy,
takže sa dlhé slovo radšej zalomí, než by prečnievalo.


## Nasadenie na Vercel

Web beží na Vercel, kde **neplatí `.htaccess` ani `_redirects`** — tie sú pre
Apache a Netlify. Presmerovania starých WordPress adries sa preto generujú aj
do **`site/vercel.json`** (34 presmerovaní 301 plus bezpečnostné hlavičky
a ročná cache na `/assets/`). Bez tohto súboru by staré odkazy z Googlu
končili na 404 a web by prišiel o doteraz nazbieranú SEO hodnotu.

Súbor musí byť v **koreni nasadenia** — teda tam, kde je `index.html`.

## Rýchlosť generovania

Vyrezávanie packshotov je morfologicky drahé (asi 15 s na obrázok), preto sa
výsledok cachuje do `gen/.cache/` s časovou pečiatkou zdroja. Prvý beh trvá
niekoľko minút, ďalšie asi minútu. Po výmene zdrojového packshotu sa jeho
cache prepočíta sama; celú vieš zahodiť cez `rm -rf gen/.cache`.
