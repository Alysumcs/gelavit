# -*- coding: utf-8 -*-
"""Články, právne stránky, SVG ilustrácie a SEO súbory."""
import re, pathlib, html
from i18n import T

# ============================================================== O NÁS ========
T["sk"]["about_story"] = """
<h4>Nech je tvoja strava tvojím liekom</h4>
<p>Plné čakárne ortopedických ordinácií a problémy, ktoré pri chôdzi, zohýbaní či pohybe pociťujú
už mladí ľudia, sú znamením, že niečo s našou výživou a životným štýlom nie je v poriadku.
Aj na začiatku produktu <strong>GelaVit</strong> bol príbeh „takmer strateného zdravia“.</p>
<p>Vždy som bola aktívna športovkyňa a bez pohybu som si život nevedela predstaviť. Moje problémy
s chrbticou sa objavili, keď som nastúpila do náročného zamestnania, kde telo nemalo možnosť
primeraného odpočinku. Šľachy a kĺby trpeli nadmernou námahou, napokon si to „odniesla“ platnička
v chrbtici. Silná a vytrvalá bolesť mi bránila nielen chodiť, ale aj šoférovať.</p>
<p>Našťastie, múdry lekár, ktorého som navštívila, zvolil namiesto operácie cestu liečby výživou.
A tak som po niekoľkonásobnom užívaní želatíny spoznala dôležitosť tejto súčasti našej stravy
a opäť som sa postavila na nohy. Keďže konzumácia samotnej želatíny nebola práve príjemná, hľadala
som spôsob, ako pripraviť chutnú a prirodzenú potravinu, ktorá by mala vysoko pozitívny vplyv na
pohybový aparát, a pritom obsahovala aj dôležité vitamíny a minerály.</p>
<p>Výsledkom môjho niekoľkoročného štúdia, testovania a skúšania je rada produktov
<strong>GelaVit</strong> — chutných, zdravých potravín.</p>
<p>Ideálne je, keď ich do svojej dennej stravy zaradíte skôr, ako sa objavia problémy súvisiace
s opotrebením kĺbov. Ak však už s podobnými problémami bojujete, stanú sa výbornou podporou liečby
a pravidelné užívanie kolagénu vo vhodnej kombinácii s vitamínmi vám pomôže predísť mnohým
zdravotným problémom.</p>
"""

T["en"]["about_story"] = """
<h4>Let food be thy medicine</h4>
<p>The full waiting rooms of orthopaedists and the problems the young have at walking, bending or
moving at all are signs that something is wrong with our diet and lifestyle. The <strong>GelaVit</strong>
story begins with a similar “story of health lost”.</p>
<p>I have been an active athlete for all my life. I could not imagine my life without moving actively.
My back issues appeared when I started in a demanding job. My body did not have enough time to rest.
The tendons and joints were under enormous pressure and a vertebral disc “gave up”. The intense and
persistent pain hindered me from walking, driving, or any more complex physical activity.</p>
<p>Luckily for me, a good physician I saw decided to treat me with food instead of an operation.
After eating gelatine for some time, I learnt how important it is in our diet and got back on my feet.
As eating gelatine on its own was not very pleasant, I searched for ways how to prepare tasty and
natural food with positive effects on our movement apparatus, containing the important vitamins and
minerals we need.</p>
<p>The result of my years of studying, testing and trying is the <strong>GelaVit</strong> product line —
tasty and healthy food products.</p>
<p>It is best to start taking them daily before any problems with joint wear appear. However, also when
fighting these issues, they are a great supplement to your treatment. Regular use of collagen combined
with vitamins can prevent many health issues.</p>
"""

T["de"]["about_story"] = """
<h4>Nahrung soll deine Medizin sein</h4>
<p>Volle Wartezimmer der Orthopäden und Probleme beim Gehen, Bücken oder jeder Bewegung schon bei jungen
Leuten sind ein Zeichen dessen, dass etwas mit unserer Ernährung und unserem Lebensstil nicht in Ordnung
ist. Auch am Anfang der Geschichte des Produkts <strong>GelaVit</strong> war eine „fast verlorene
Gesundheit“.</p>
<p>Ich habe immer aktiv Sport getrieben und ohne Sport konnte ich mir mein Leben nicht vorstellen. Meine
Rückenprobleme fingen an, als ich in einer anstrengenden Arbeit begonnen habe. Mein Körper hatte dort
nicht genug Zeit zu regenerieren. Meine Sehnen und Gelenke litten unter Anstrengung und am Ende hat eine
Bandscheibe „den Dienst quittiert“. Wegen starker und andauernder Schmerzen konnte ich nicht gehen und
nicht Auto fahren.</p>
<p>Glücklicherweise hat ein kluger Arzt, den ich besucht habe, eine Diät anstatt einer Operation gewählt.
Nach längerer Aufnahme von Gelatine habe ich die Wichtigkeit ihrer Präsenz in unserer Ernährung erkannt
und kam wieder auf die Beine. Da Gelatine selbst nicht gerade köstlich ist, suchte ich nach Möglichkeiten,
ein geschmackvolles und natürliches Nahrungsmittel mit positiven Auswirkungen auf unseren Bewegungsapparat
vorzubereiten, das auch wichtige Vitamine und Mineralstoffe enthalten würde.</p>
<p>Das Ergebnis meines mehrjährigen Suchens, Testens und Probierens ist die Reihe der
<strong>GelaVit</strong>-Produkte — köstliche und natürliche Lebensmittel.</p>
<p>Am besten integrieren Sie sie noch vor dem Auftreten der Gelenkprobleme in Ihr tägliches Menü. Wenn Sie
aber schon solche Probleme haben, dienen sie als hervorragende Unterstützung Ihrer Kur. Regelmäßige
Einnahme von Kollagen in geeigneter Kombination mit Vitaminen kann vielen Gesundheitsproblemen vorbeugen.</p>
"""

# ============================================================== ČLÁNKY ======
POSTS = {}

POSTS["sk"] = [
  {
    "slug": "kolagen-nenahraditelna-bielkovina", "date": "2017-05-30",
    "title": "Kolagén — nenahraditeľná bielkovina",
    "excerpt": "Kolagén tvorí až tretinu všetkých bielkovín v tele. Ako vzniká, prečo sa natívny kolagén nevstrebáva a čo s tým robí hydrolyzát.",
    "html": """
<p><strong>Kolagén</strong> je základnou stavebnou hmotou podporných tkanív a hlavnou organickou zložkou
podporného systému — kostí a chrupaviek, šliach, väzív a kože. Je hlavným pilierom spojivového tkaniva
a najdôležitejšou bielkovinou ľudského tela. Tvorí až jednu tretinu všetkých bielkovín.</p>
<p>Kolagén podporuje a zvyšuje výživu i rast kĺbovej chrupavky, zlepšuje pohyblivosť svalov, kĺbov
i chrbtice, zmierňuje bolesť a pôsobí proti vzniku degeneratívnych a zápalových ochorení pohybového
aparátu. Jeho účinok je skutočne komplexný.</p>
<h2>Kolagén a pokožka</h2>
<p>Ako väzivový glykoproteín dodáva pokožke pružnosť a elasticitu. Spája a „lepí“ bunkové prvky, formuje
z nich tkanivá a orgány. Medzi jeho účinky patrí aj intenzívna hydratácia pokožky, zvýšenie jej
elasticity, spomalenie procesu starnutia, urýchlenie hojenia rán — úrazových i pooperačných —
a regenerácia vlasovej pokožky, vlasov a nechtov.</p>
<h2>Prečo sa natívny kolagén nevstrebáva</h2>
<p>Kolagén je vo vode nerozpustná bielkovina a v natívnom stave sa nevstrebáva. Avšak
<strong>kolagénny hydrolyzát</strong>, ktorý obsahuje vo vode rozpustné kolagénne peptidy, je
vstrebateľný. Krvou a lymfou je transportovaný a následne využívaný na výživu kolagénových spojivových
tkanív. Iba spojivové tkanivo nasýtené kolagénom sa môže správne vyvíjať a následne lepšie odolávať
náhlemu aj dlhodobému preťažovaniu.</p>
<h2>Ako kolagén v tele vzniká</h2>
<p>Kolagén produkujú najmä väzivové bunky — fibroblasty, bunky chrupavky — chondroblasty, kostné bunky —
osteoblasty, ale aj epitelové bunky. Syntéza sčasti prebieha vo vnútri bunky a sčasti mimo nej.
Kľúčovú úlohu v nej zohráva <strong>vitamín C</strong>: bez neho telo z prijatých aminokyselín vlastný
kolagén jednoducho nevytvorí.</p>
<p>Produkty rozkladu kolagénu — voľné aminokyseliny — sprostredkúvajú výživu bunkám a majú pre
organizmus obnovujúcu a regeneračnú funkciu. Po úraze alebo ochorení sú to práve bielkoviny spojivového
tkaniva, ktoré ako prvé pomáhajú „opraviť“ poškodenú časť tela.</p>
<blockquote>Ani kolagén nie je trvalý. V tele stále prebieha jeho výmena — zaniká a súčasne sa obnovuje.
Preto je pri kúre rozhodujúca pravidelnosť, nie jednorazová vysoká dávka.</blockquote>
"""
  },
  {
    "slug": "kolagen-pre-vsetkych-a-jeho-vyznam", "date": "2018-02-08",
    "title": "Kolagén pre všetkých a jeho význam",
    "excerpt": "Čo sa deje s kolagénom po prehltnutí, prečo je vitamín C nevyhnutný a ako si vybrať správnu formu.",
    "html": """
<p>Kolagén je bielkovina. Je to <strong>hlavná stavebná bielkovina</strong> ľudského tela — tvorí takmer
tretinu všetkých bielkovín. Jeho najväčší podiel obsahujú podporné tkanivá: kosti, kĺby, šľachy a koža.</p>
<p>Kolagén má pre ľudské telo obrovský a nenahraditeľný význam. Je to hlavne preto, že jeho štruktúra
vytvára <strong>trojitú skrutkovicu</strong> podobnú spletenému lanu. Toto usporiadanie mu dáva vysokú
pevnosť v ťahu a predurčuje ho na tvorbu väzivových a nosných tkanív.</p>
<h2>Čo sa deje po užití kolagénu cez tráviaci trakt?</h2>
<p>Keďže kolagén nemôže byť priamo vstrebaný cez stenu čreva, rozloží sa najskôr na základné stavebné
jednotky — aminokyseliny. Najviac sú zastúpené glycín, prolín a lyzín. Tie sú následne transportované
krvou tam, kde sú potrebné.</p>
<p>Výsledok konzumácie kolagénu je taký, že dodá telu aminokyseliny na stavbu vlastného kolagénu.
Obrovskú úlohu tu hrá <strong>vitamín C</strong>, vďaka ktorému prebieha efektívna tvorba kolagénu
v organizme. Bez neho nemá užívanie doplnkov prakticky žiadny vplyv.</p>
<p>Ideálna kombinácia rybieho hydrolyzovaného kolagénu s vitamínom C je to, na čom staviame celú radu
Gelavit Pure®. K dispozícii v príchutiach ananás, lieskový orech a kokosové mlieko.</p>
"""
  },
  {
    "slug": "tekuta-krasa-existuje", "date": "2017-11-25",
    "title": "Tekutá krása existuje: čo hovoria dermatológovia o kolagéne v strave",
    "excerpt": "Kedy začať s kolagénom, kde ho nájdete prirodzene a čomu sa vyhnúť, ak chcete udržať pokožku pružnú.",
    "html": """
<p><strong>Dá sa krása vypiť?</strong> Do istej miery áno — a navyše vám bude chutiť. Kolagénový prášok
si primiešate do obľúbeného smoothie alebo do rannej ovsenej kaše. Nielenže pleť viditeľne osviežite,
ale dodáte jej aj chýbajúci jas a potrebnú hydratáciu.</p>
<h2>Prečo práve kolagén?</h2>
<p>Newyorská dermatologička Anne Chapas vysvetľuje, že kolagén je nesmierne cenná bielkovina, ktorá je
stavebným prvkom našej pokožky. Vďaka kolagénu je pokožka pružná a vie sa rýchlo zregenerovať z rán
a podráždenia.</p>
<h2>Kedy začať?</h2>
<p>Okolo tridsiateho roku života sa okrem mimických vrások objavujú aj prvé príznaky starnutia pokožky.
Ak už máte tridsať a viac, kolagén by sa mal stať každodennou súčasťou vášho jedálnička. Majiteľky
suchej pokožky môžu začať skôr.</p>
<h2>Kde sa kolagén nachádza prirodzene?</h2>
<p>Podporiť účinky kolagénového prášku môžete aj stravou. Patrí sem losos, vajíčka, quinoa, slepačí
vývar, morčacie mäso, orechy, olejnaté semená, šošovica a fazuľa.</p>
<blockquote>„Ak jete vyváženú stravu bohatú na bielkoviny, vaše telo premení tieto živiny na esenciálne
aminokyseliny potrebné na udržanie zdravej pokožky a zdravých kostí,“ hovorí dermatológ Craig Austin.</blockquote>
<h2>Čomu sa vyvarovať?</h2>
<p>Rovnako ako môžete tvorbu kolagénu vedome zvýšiť, viete spraviť aj presný opak. K strate kolagénu
dochádza pri nadmernom slnení bez ochrany, pri fajčení, nedostatku spánku a strave s vysokým obsahom
jednoduchých cukrov.</p>
"""
  },
  {
    "slug": "sukraloza-a-jej-pozitiva", "date": "2017-11-09",
    "title": "Sukralóza a jej pozitíva",
    "excerpt": "Prečo sme ako sladidlo zvolili sukralózu, ako sa správa v tele a prečo je vhodná aj pre diabetikov.",
    "html": """
<h2>Čo je vlastne sukralóza?</h2>
<ul>
<li>Je umelé sladidlo, ktorého názov evokuje príbuznosť s cukrom.</li>
<li>Je mnohonásobne sladšia ako cukor, ale má iba pätinu kalórií.</li>
<li>Má nízky glykemický index.</li>
<li>Nemá vplyv na glykémiu, nezvyšuje hladinu krvného cukru.</li>
</ul>
<h2>Ako vplýva na ľudské zdravie?</h2>
<p>Sukralóza sa v ľudskom tele nerozkladá a nie je metabolizovaná. V rovnakom stave sa vylučuje stolicou
alebo močom. Neukladá sa v tuku. Je vhodnou náhradou pre ľudí trpiacich cukrovkou.</p>
<p>Keďže neobsahuje žiadnu energiu, jej hlavnou úlohou je spríjemniť chuť potraviny. Práve preto ju
používame v našich práškových produktoch — bez sladidla by bola kúra pre väčšinu ľudí ťažko dodržateľná
a nepravidelné užívanie nemá zmysel.</p>
"""
  },
  {
    "slug": "samostatne-balenia-na-cesty", "date": "2017-12-20",
    "title": "Ideálne samostatné balenia na výlety či dovolenku",
    "excerpt": "Prečo je pri kolagéne rozhodujúca kontinuita a ako ju udržať aj mimo domova.",
    "html": """
<blockquote>„Starostlivosť o svoje kĺby nemusíte vynechať ani na výlete či dovolenke.“</blockquote>
<p>Plnohodnotná starostlivosť o kĺby by mala byť kontinuálna — stále a súvislé dopĺňanie výživy by malo
byť samozrejmosťou pre namáhané kosti a kĺby. Obdobie pracovného pokoja, výletov a dovoleniek však
prináša prerušovanie zabehnutých rituálov. Platí to aj pri pravidelnom užívaní doplnkov stravy.</p>
<p>Ak chceme dosiahnuť pozitívny účinok po ukončení celej kúry, musíme dodržať striktnú pravidelnosť
užívania. Je to základný pilier pri liečení kúrami.</p>
<h2>Riešenie: 28 samostatných vrecúšok</h2>
<p>Zobrať si na dovolenku k moru alebo do hôr obrovské balenie nie je praktické. Vďaka
<strong>GelaVit Pure® Ananás Boxu</strong> — kolagénovej kúre v 28 praktických sáčkoch obsahujúcich
dennú dávku kolagénu a vitamínu C — to už nie je problém.</p>
<p>Stačí si pribaliť do kufra potrebný počet sáčkov a svoju výživu tak máte stále nablízku aj mimo
domova. Či už ide o víkendovú chatu, lyžovačku alebo pracovnú cestu, o vaše kĺby je postarané.</p>
"""
  },
  {
    "slug": "intenzivna-kolagenova-kura", "date": "2017-11-09",
    "title": "Intenzívna kolagénová kúra GelaVit Pure®",
    "excerpt": "Pre koho je intenzívna kúra určená, ako sa užíva a čo od nej môžete čakať.",
    "html": """
<ul>
<li>Kĺbová výživa na zmiernenie bolesti s vysokým obsahom morského kolagénu.</li>
<li>Podporná liečba po úrazoch a operáciách kĺbov či chrbtice — urýchľuje hojenie rán a regeneráciu.</li>
<li>Prevencia pred opotrebením kĺbov a kostí.</li>
<li>Hydratácia pleti, vlasov a nechtov.</li>
<li>Vhodná aj pre diabetikov vďaka sukralóze.</li>
</ul>
<p>Jedno vrecúško s obsahom 5 g stačí primiešať do vody, vločiek alebo šejku, užívať každý deň a čakať
na pozitívne účinky. Telo si kolagén privedie práve tam, kde ho najviac potrebuje, a vy sa nemusíte
zaoberať jeho priebehom.</p>
<p>Choďte radšej do fitka alebo si zabehať s dobrým pocitom, že ste práve urobili niečo pre svoje telo.
V blízkej dobe to oceníte vy sami aj vaše okolie.</p>
"""
  },
  {
    "slug": "kolagenova-cokolada", "date": "2017-11-02",
    "title": "Kolagénová čokoláda: sladká chvíľa, ktorá niečo dá",
    "excerpt": "Tmavá čokoláda, flavonoly a morský kolagén — prečo je toto spojenie lepšie, než znie.",
    "html": """
<ul>
<li>Tmavá čokoláda obsahuje flavonoly, ktoré patria do skupiny flavonoidov a sú známe svojimi
antioxidačnými vlastnosťami.</li>
<li>Pomáha znižovať vysoký krvný tlak.</li>
<li>Vyplavuje endorfíny — tzv. hormóny šťastia.</li>
<li>Zvyšuje hladinu sérotonínu.</li>
<li>Zlepšuje lipidový profil a cholesterol.</li>
</ul>
<p>Navyše čokoláda <strong>Gelavit Pure®</strong> obsahuje kokosové mlieko a morský kolagén, vďaka čomu
budete mať zdravšie kĺby a krajšiu pleť. Nie je to náhrada za kúru — je to spôsob, ako mať v slabej
chvíli po ruke niečo, čo neublíži.</p>
"""
  },
]

POSTS["en"] = [
  {"slug": p["slug"], "date": p["date"], "title": t_, "excerpt": e_, "html": h_}
  for p, t_, e_, h_ in zip(POSTS["sk"],
    ["Collagen — an irreplaceable protein",
     "Collagen for everyone and why it matters",
     "Liquid beauty exists: what dermatologists say about collagen in your diet",
     "Sucralose and its upsides",
     "Individual sachets for trips and holidays",
     "The GelaVit Pure® intense collagen course",
     "Collagen chocolate: a sweet moment that gives something back"],
    ["Collagen makes up a third of all proteins in the body. How it is formed, why native collagen is not absorbed, and what a hydrolysate changes.",
     "What happens to collagen after you swallow it, why vitamin C is essential, and how to pick the right form.",
     "When to start with collagen, where to find it naturally, and what to avoid if you want to keep your skin elastic.",
     "Why we chose sucralose as the sweetener, how it behaves in the body, and why it suits diabetics.",
     "Why continuity is decisive with collagen — and how to keep it up away from home.",
     "Who the intense course is for, how to take it, and what to expect.",
     "Dark chocolate, flavanols and marine collagen — why this combination is better than it sounds."],
    ["""
<p><strong>Collagen</strong> is the basic building material of supporting tissues and the main organic
component of the supporting system — bones and cartilage, tendons, ligaments and skin. It is the main
pillar of connective tissue and the most important protein of the human body, making up one third of
all proteins.</p>
<p>Collagen supports and increases the nutrition and growth of joint cartilage, improves the mobility of
muscles, joints and the spine, relieves pain and acts against degenerative and inflammatory diseases of
the movement apparatus.</p>
<h2>Collagen and skin</h2>
<p>As a connective glycoprotein it gives the skin flexibility and elasticity. It joins and “glues”
cellular elements and forms tissues and organs from them. Its effects include intense skin hydration,
increased elasticity, slowing of skin ageing, faster healing of wounds — both injury and post-operative —
and regeneration of the scalp, hair and nails.</p>
<h2>Why native collagen is not absorbed</h2>
<p>Collagen is a water-insoluble protein and in its native state it is not absorbed. However, a
<strong>collagen hydrolysate</strong> containing water-soluble collagen peptides is absorbable. It is
transported by blood and lymph and then used to nourish collagenous connective tissues. Only connective
tissue saturated with collagen can develop properly and withstand sudden and long-term overload.</p>
<h2>How collagen is formed in the body</h2>
<p>Collagen is produced mainly by connective cells (fibroblasts), cartilage cells (chondroblasts), bone
cells (osteoblasts) and epithelial cells. <strong>Vitamin C</strong> plays a key role: without it the
body simply cannot build its own collagen from the amino acids you consume.</p>
<blockquote>Collagen is not permanent. It is continuously exchanged in the body — it degrades and is
renewed at the same time. That is why consistency, not a single large dose, decides the outcome.</blockquote>
""",
     """
<p>Collagen is a protein — the <strong>main structural protein</strong> of the human body, making up
almost a third of all proteins. Supporting tissues contain the most of it: bones, joints, tendons and
skin.</p>
<p>Its structure forms a <strong>triple helix</strong> similar to a braided rope. This arrangement gives
it high tensile strength and predisposes it to build connective and load-bearing tissues.</p>
<h2>What happens after you take collagen?</h2>
<p>Since collagen cannot be absorbed directly through the intestinal wall, it is first broken down into
its basic building blocks — amino acids, mostly glycine, proline and lysine. These are then transported
by the blood to where they are needed.</p>
<p>The result is that collagen supplies the body with the amino acids to build its own collagen.
<strong>Vitamin C</strong> plays a huge role here — without it, taking supplements has virtually no
effect.</p>
""",
     """
<p><strong>Can beauty be drunk?</strong> To a degree, yes — and it will taste good too. You can mix
collagen powder into a smoothie or your morning porridge, refreshing your skin and giving it the
hydration it lacks.</p>
<h2>Why collagen?</h2>
<p>New York dermatologist Anne Chapas explains that collagen is an extremely valuable protein and the
building block of our skin. Thanks to collagen, skin is elastic and can regenerate quickly from wounds
and irritation.</p>
<h2>When to start?</h2>
<p>Around the age of thirty, the first signs of skin ageing appear alongside expression lines. If you are
thirty or over, collagen should become a daily part of your diet. Those with dry skin can start earlier.</p>
<h2>Where is collagen found naturally?</h2>
<p>You can support the effects of collagen powder through diet too: salmon, eggs, quinoa, chicken broth,
turkey, nuts, oilseeds, lentils and beans.</p>
<h2>What to avoid</h2>
<p>Just as you can consciously increase collagen production, you can do the exact opposite. Collagen is
lost through excessive unprotected sun exposure, smoking, lack of sleep and a diet high in simple sugars.</p>
""",
     """
<h2>What is sucralose?</h2>
<ul>
<li>An artificial sweetener whose name suggests its relation to sugar.</li>
<li>Many times sweeter than sugar, with only a fifth of the calories.</li>
<li>Low glycaemic index.</li>
<li>No effect on glycaemia; it does not raise blood sugar levels.</li>
</ul>
<h2>How does it affect health?</h2>
<p>Sucralose is not broken down or metabolised in the human body. It is excreted in the same state and is
not stored in fat. It is a suitable substitute for people with diabetes.</p>
<p>Since it contains no energy, its main role is to make the food taste pleasant. That is exactly why we
use it — without a sweetener, most people would find the course hard to keep up, and irregular use makes
no sense.</p>
""",
     """
<blockquote>“You do not have to skip caring for your joints on a trip or a holiday.”</blockquote>
<p>Full joint care should be continuous. Periods of rest, trips and holidays, however, interrupt
established rituals — including the regular use of food supplements.</p>
<p>To achieve a positive effect after completing a course, strict regularity is required. It is the basic
pillar of treatment by courses.</p>
<h2>The solution: 28 individual sachets</h2>
<p>Taking a huge package to the seaside or the mountains is not practical. With the
<strong>GelaVit Pure® Pineapple Box</strong> — a collagen course in 28 practical sachets, each with a
daily dose of collagen and vitamin C — that is no longer a problem.</p>
""",
     """
<ul>
<li>Joint nutrition to relieve pain, with a high content of marine collagen.</li>
<li>Supportive treatment after injuries and joint or spine surgery — it speeds up wound healing and
regeneration.</li>
<li>Prevention of joint and bone wear.</li>
<li>Hydration of skin, hair and nails.</li>
<li>Suitable for diabetics thanks to sucralose.</li>
</ul>
<p>Just mix one 5 g sachet into water, oats or a shake, take it every day and wait for the effects. Your
body will bring the collagen exactly where it is needed most.</p>
""",
     """
<ul>
<li>Dark chocolate contains flavanols from the flavonoid group, known for their antioxidant properties.</li>
<li>It helps lower high blood pressure.</li>
<li>It releases endorphins — the so-called happiness hormones.</li>
<li>It raises serotonin levels.</li>
<li>It improves the lipid profile and cholesterol.</li>
</ul>
<p>On top of that, <strong>Gelavit Pure®</strong> chocolate contains coconut milk and marine collagen, so
your joints and skin benefit too. It is not a replacement for a course — it is a way to have something on
hand in a weak moment that does no harm.</p>
"""])
]

POSTS["de"] = [
  {"slug": p["slug"], "date": p["date"], "title": t_, "excerpt": e_, "html": h_}
  for p, t_, e_, h_ in zip(POSTS["sk"],
    ["Kollagen — ein unersetzliches Protein",
     "Kollagen für alle und seine Bedeutung",
     "Flüssige Schönheit gibt es: Was Dermatologen über Kollagen in der Ernährung sagen",
     "Sucralose und ihre Vorteile",
     "Ideale Einzelportionen für Ausflüge und Urlaub",
     "Die GelaVit Pure® Intensiv-Kollagenkur",
     "Kollagen-Schokolade: ein süßer Moment, der etwas zurückgibt"],
    ["Kollagen macht ein Drittel aller Proteine im Körper aus. Wie es entsteht, warum natives Kollagen nicht aufgenommen wird und was ein Hydrolysat ändert.",
     "Was mit Kollagen nach dem Schlucken passiert, warum Vitamin C unentbehrlich ist und wie man die richtige Form wählt.",
     "Wann man mit Kollagen beginnen sollte, wo es natürlich vorkommt und was man meiden sollte.",
     "Warum wir Sucralose als Süßungsmittel gewählt haben und warum sie auch für Diabetiker geeignet ist.",
     "Warum Kontinuität bei Kollagen entscheidend ist — und wie man sie auch unterwegs hält.",
     "Für wen die Intensivkur gedacht ist, wie sie eingenommen wird und was Sie erwarten können.",
     "Zartbitterschokolade, Flavanole und Meereskollagen — warum diese Kombination besser ist, als sie klingt."],
    ["""
<p><strong>Kollagen</strong> ist das grundlegende Baumaterial der Stützgewebe und der wichtigste
organische Bestandteil des Stützsystems — Knochen und Knorpel, Sehnen, Bänder und Haut. Es ist die
Hauptsäule des Bindegewebes und das wichtigste Protein des menschlichen Körpers und macht ein Drittel
aller Proteine aus.</p>
<p>Kollagen fördert die Ernährung und das Wachstum des Gelenkknorpels, verbessert die Beweglichkeit von
Muskeln, Gelenken und Wirbelsäule, lindert Schmerzen und wirkt degenerativen und entzündlichen
Erkrankungen des Bewegungsapparats entgegen.</p>
<h2>Kollagen und Haut</h2>
<p>Als Bindegewebs-Glykoprotein verleiht es der Haut Spannkraft und Elastizität. Zu seinen Wirkungen
zählen intensive Hautfeuchtigkeit, erhöhte Elastizität, verlangsamte Hautalterung, schnellere Heilung von
Wunden sowie die Regeneration von Kopfhaut, Haaren und Nägeln.</p>
<h2>Warum natives Kollagen nicht aufgenommen wird</h2>
<p>Kollagen ist ein wasserunlösliches Protein und wird in nativem Zustand nicht aufgenommen. Ein
<strong>Kollagenhydrolysat</strong> mit wasserlöslichen Kollagenpeptiden ist jedoch resorbierbar. Es wird
über Blut und Lymphe transportiert und zur Ernährung der kollagenen Bindegewebe genutzt.</p>
<h2>Wie Kollagen im Körper entsteht</h2>
<p>Kollagen wird vor allem von Bindegewebszellen (Fibroblasten), Knorpelzellen (Chondroblasten),
Knochenzellen (Osteoblasten) und Epithelzellen gebildet. Eine Schlüsselrolle spielt dabei
<strong>Vitamin C</strong>: Ohne es kann der Körper aus den aufgenommenen Aminosäuren kein eigenes
Kollagen bilden.</p>
<blockquote>Kollagen ist nicht dauerhaft. Es wird im Körper ständig ausgetauscht — deshalb entscheidet
die Regelmäßigkeit, nicht eine einzelne hohe Dosis.</blockquote>
""",
     """
<p>Kollagen ist ein Protein — das <strong>wichtigste Strukturprotein</strong> des menschlichen Körpers
und macht fast ein Drittel aller Proteine aus. Am meisten enthalten die Stützgewebe: Knochen, Gelenke,
Sehnen und Haut.</p>
<p>Seine Struktur bildet eine <strong>Tripelhelix</strong>, ähnlich einem geflochtenen Seil. Diese
Anordnung verleiht ihm hohe Zugfestigkeit.</p>
<h2>Was passiert nach der Einnahme?</h2>
<p>Da Kollagen nicht direkt durch die Darmwand aufgenommen werden kann, wird es zuerst in seine
Grundbausteine zerlegt — Aminosäuren, vor allem Glycin, Prolin und Lysin. Diese werden dann über das Blut
dorthin transportiert, wo sie gebraucht werden.</p>
<p>Eine große Rolle spielt dabei <strong>Vitamin C</strong>, ohne das die Einnahme von
Nahrungsergänzungsmitteln praktisch keine Wirkung hat.</p>
""",
     """
<p><strong>Kann man Schönheit trinken?</strong> Bis zu einem gewissen Grad ja — und es schmeckt auch noch.
Kollagenpulver lässt sich in einen Smoothie oder ins Morgen-Porridge einrühren.</p>
<h2>Warum Kollagen?</h2>
<p>Die New Yorker Dermatologin Anne Chapas erklärt, dass Kollagen ein äußerst wertvolles Protein und der
Baustein unserer Haut ist. Dank Kollagen ist die Haut elastisch und regeneriert sich schnell.</p>
<h2>Wann anfangen?</h2>
<p>Um das dreißigste Lebensjahr treten neben Mimikfalten die ersten Zeichen der Hautalterung auf. Ab
dreißig sollte Kollagen ein täglicher Teil der Ernährung sein. Bei trockener Haut auch früher.</p>
<h2>Wo kommt Kollagen natürlich vor?</h2>
<p>Lachs, Eier, Quinoa, Hühnerbrühe, Putenfleisch, Nüsse, Ölsaaten, Linsen und Bohnen.</p>
<h2>Was man meiden sollte</h2>
<p>Kollagenverlust entsteht durch übermäßiges ungeschütztes Sonnenbaden, Rauchen, Schlafmangel und eine
Ernährung mit vielen einfachen Zuckern.</p>
""",
     """
<h2>Was ist Sucralose?</h2>
<ul>
<li>Ein Süßungsmittel, dessen Name auf die Verwandtschaft mit Zucker hinweist.</li>
<li>Vielfach süßer als Zucker, aber nur ein Fünftel der Kalorien.</li>
<li>Niedriger glykämischer Index.</li>
<li>Kein Einfluss auf die Glykämie; erhöht den Blutzuckerspiegel nicht.</li>
</ul>
<h2>Wie wirkt sie auf die Gesundheit?</h2>
<p>Sucralose wird im menschlichen Körper nicht abgebaut und nicht metabolisiert. Sie wird unverändert
ausgeschieden und nicht im Fett gespeichert. Für Diabetiker ist sie ein geeigneter Ersatz.</p>
<p>Ihre Hauptaufgabe ist es, den Geschmack angenehm zu machen — ohne Süßungsmittel würden die meisten
Menschen die Kur nicht durchhalten, und unregelmäßige Einnahme ist sinnlos.</p>
""",
     """
<blockquote>„Die Pflege Ihrer Gelenke müssen Sie auch auf einem Ausflug oder im Urlaub nicht auslassen.“</blockquote>
<p>Vollwertige Gelenkpflege sollte kontinuierlich sein. Ruhephasen, Ausflüge und Urlaube unterbrechen
jedoch eingespielte Rituale — auch die regelmäßige Einnahme von Nahrungsergänzungsmitteln.</p>
<h2>Die Lösung: 28 Einzelsäckchen</h2>
<p>Eine große Packung ans Meer oder in die Berge mitzunehmen ist unpraktisch. Mit der
<strong>GelaVit Pure® Ananas Box</strong> — einer Kollagenkur in 28 praktischen Säckchen mit je einer
Tagesportion Kollagen und Vitamin C — ist das kein Problem mehr.</p>
""",
     """
<ul>
<li>Gelenknahrung zur Schmerzlinderung mit hohem Anteil an Meereskollagen.</li>
<li>Unterstützende Behandlung nach Verletzungen und Gelenk- oder Wirbelsäulenoperationen.</li>
<li>Vorbeugung gegen Gelenk- und Knochenverschleiß.</li>
<li>Feuchtigkeit für Haut, Haare und Nägel.</li>
<li>Dank Sucralose auch für Diabetiker geeignet.</li>
</ul>
<p>Ein Säckchen mit 5 g in Wasser, Haferflocken oder einen Shake einrühren, täglich einnehmen — der
Körper bringt das Kollagen genau dorthin, wo es am nötigsten ist.</p>
""",
     """
<ul>
<li>Zartbitterschokolade enthält Flavanole aus der Gruppe der Flavonoide mit antioxidativen
Eigenschaften.</li>
<li>Sie hilft, hohen Blutdruck zu senken.</li>
<li>Sie setzt Endorphine frei — die sogenannten Glückshormone.</li>
<li>Sie erhöht den Serotoninspiegel.</li>
<li>Sie verbessert das Lipidprofil und den Cholesterinwert.</li>
</ul>
<p>Zusätzlich enthält die <strong>Gelavit Pure®</strong> Schokolade Kokosmilch und Meereskollagen — so
profitieren auch Gelenke und Haut.</p>
"""])
]


PHOTOS = {'kolagen-nenahraditelna-bielkovina': 'prasok', 'kolagen-pre-vsetkych-a-jeho-vyznam': 'rollup', 'tekuta-krasa-existuje': 'rada-produktov', 'sukraloza-a-jej-pozitiva': 'prasok', 'samostatne-balenia-na-cesty': 'cestovne-balenie', 'intenzivna-kolagenova-kura': 'box-detail', 'kolagenova-cokolada': 'cokolada-mlieko'}


def posts_for(lang):
    out = []
    for p in POSTS[lang]:
        d = dict(p)
        d["photo"] = PHOTOS.get(d["slug"], "rada-produktov")
        out.append(d)
    return out


# ========================================================= PRÁVNE STRÁNKY ====
def strip_notice(html_text):
    """Vyhodí odsek s triedou notice (interné upozornenie)."""
    return re.sub(r'<p class="notice">.*?</p>', "", html_text, flags=re.S)


def legal(key, lang, T, URLS, DIR):
    t = T[lang]
    u = URLS[lang]
    if key == "howto":
        body = HOWTO[lang].replace("{products}", u["products"]).replace("{terms}", u["terms"])
        return body, t["nav_howto"]
    body = TERMS[lang] if key == "terms" else PRIVACY[lang]
    if not SHOW_LEGAL_NOTICE:
        body = strip_notice(body)
    return body, (t["nav_terms"] if key == "terms" else t["nav_privacy"])


HOWTO = {"sk": """
<h2>1. Vyberte si produkt</h2>
<p>V sekcii <a href="{products}">Produkty</a> nájdete celú radu GelaVit. Pri každom produkte je uvedený
názov, obrázok, krátky popis, cena a dostupnosť. Kliknutím na názov alebo obrázok otvoríte detail
s kompletným zložením, dávkovaním a skladovaním.</p>

<h2>2. Vložte tovar do košíka</h2>
<p>Na stránke produktu zvoľte požadované množstvo a kliknite na <strong>Do košíka</strong>. Obsah košíka
sa ukladá vo vašom prehliadači — zostane vám aj keď stránku zavriete a vrátite sa neskôr.</p>

<h2>3. Skontrolujte košík</h2>
<p>Na ikonu košíka vpravo hore kliknite kedykoľvek. Zobrazí sa zoznam vybraných produktov, kde môžete
meniť počet kusov tlačidlami <strong>−</strong> a <strong>+</strong>, alebo položku odstrániť odkazom
<strong>Odstrániť</strong>. Medzisúčet sa prepočíta okamžite.</p>

<h2>4. Vyplňte objednávku</h2>
<p>Kliknite na <strong>Prejsť do pokladne</strong> a vyplňte kontaktné a doručovacie údaje. Vyberte
spôsob doručenia a platby — celková suma vrátane dopravy sa priebežne zobrazuje v pravom stĺpci.</p>

<h2>5. Odošlite a čakajte na potvrdenie</h2>
<p>Po odsúhlasení <a href="{terms}">obchodných podmienok</a> kliknite na <strong>Odoslať objednávku</strong>.
Do niekoľkých minút vám na e-mail príde potvrdenie s rekapituláciou objednávky a platobnými údajmi.</p>

<h2>Doprava a platba</h2>
<table>
<tr><th>Spôsob</th><th>Cena</th><th>Doručenie</th></tr>
<tr><td>Slovenská pošta — balík na adresu</td><td>3,90 €</td><td>2–3 pracovné dni</td></tr>
<tr><td>Kuriér</td><td>4,90 €</td><td>do 24 hodín</td></tr>
<tr><td>Osobný odber — Bratislava</td><td>zdarma</td><td>po telefonickej dohode</td></tr>
</table>
<p>Pri objednávke nad <strong>50 €</strong> je doprava zdarma. Platiť môžete prevodom na účet (bez
poplatku) alebo dobierkou (+1,20 €).</p>

<h2>Máte otázku?</h2>
<p>Napíšte na <a href="mailto:info@gelavit.sk">info@gelavit.sk</a> alebo zavolajte na
<a href="tel:+421915178349">+421 915 178 349</a>, Po–Pia 9:00–16:00.</p>
""", "en": """
<h2>1. Choose a product</h2>
<p>The <a href="{products}">Products</a> section lists the whole GelaVit range. Each product shows its
name, image, short description, price and availability. Click the name or image to open the detail page
with the full composition, dosage and storage information.</p>

<h2>2. Add it to the cart</h2>
<p>On the product page select the quantity and click <strong>Add to cart</strong>. The cart is stored in
your browser — it stays there even if you close the page and come back later.</p>

<h2>3. Review your cart</h2>
<p>Click the cart icon in the top right at any time. You will see the list of selected products, where
you can change quantities with the <strong>−</strong> and <strong>+</strong> buttons, or remove an item
using <strong>Remove</strong>. The subtotal recalculates instantly.</p>

<h2>4. Fill in your order</h2>
<p>Click <strong>Go to checkout</strong> and fill in your contact and delivery details. Select the
delivery and payment method — the total including shipping is shown live in the right-hand column.</p>

<h2>5. Submit and wait for confirmation</h2>
<p>After agreeing to the <a href="{terms}">terms and conditions</a>, click <strong>Place order</strong>.
A confirmation with a summary and payment details will arrive by e-mail within minutes.</p>

<h2>Shipping and payment</h2>
<table>
<tr><th>Method</th><th>Price</th><th>Delivery</th></tr>
<tr><td>Slovak Post — parcel to address</td><td>€3.90</td><td>2–3 working days</td></tr>
<tr><td>Courier</td><td>€4.90</td><td>within 24 hours</td></tr>
<tr><td>Personal pickup — Bratislava</td><td>free</td><td>by phone arrangement</td></tr>
</table>
<p>Shipping is free on orders over <strong>€50</strong>. You can pay by bank transfer (no fee) or cash on
delivery (+€1.20).</p>

<h2>Any questions?</h2>
<p>Write to <a href="mailto:info@gelavit.sk">info@gelavit.sk</a> or call
<a href="tel:+421915178349">+421 915 178 349</a>, Mon–Fri 9:00–16:00.</p>
""", "de": """
<h2>1. Produkt auswählen</h2>
<p>Im Bereich <a href="{products}">Produkte</a> finden Sie die gesamte GelaVit-Reihe. Bei jedem Produkt
sehen Sie Namen, Bild, Kurzbeschreibung, Preis und Verfügbarkeit. Ein Klick auf Namen oder Bild öffnet
die Detailseite mit vollständiger Zusammensetzung, Dosierung und Lagerung.</p>

<h2>2. In den Warenkorb legen</h2>
<p>Wählen Sie auf der Produktseite die gewünschte Menge und klicken Sie auf
<strong>In den Warenkorb</strong>. Der Warenkorb wird in Ihrem Browser gespeichert — er bleibt erhalten,
auch wenn Sie die Seite schließen.</p>

<h2>3. Warenkorb prüfen</h2>
<p>Klicken Sie jederzeit auf das Warenkorb-Symbol oben rechts. Dort können Sie die Stückzahl mit
<strong>−</strong> und <strong>+</strong> ändern oder eine Position mit <strong>Entfernen</strong>
löschen. Die Zwischensumme wird sofort neu berechnet.</p>

<h2>4. Bestellung ausfüllen</h2>
<p>Klicken Sie auf <strong>Zur Kasse</strong> und füllen Sie Kontakt- und Lieferdaten aus. Wählen Sie
Versand- und Zahlungsart — die Gesamtsumme inkl. Versand wird laufend in der rechten Spalte angezeigt.</p>

<h2>5. Absenden und auf die Bestätigung warten</h2>
<p>Nach Zustimmung zu den <a href="{terms}">AGB</a> klicken Sie auf <strong>Bestellung absenden</strong>.
Innerhalb weniger Minuten erhalten Sie eine Bestätigung mit Übersicht und Zahlungsdaten per E-Mail.</p>

<h2>Versand und Zahlung</h2>
<table>
<tr><th>Methode</th><th>Preis</th><th>Lieferung</th></tr>
<tr><td>Slowakische Post — Paket an die Adresse</td><td>3,90 €</td><td>2–3 Werktage</td></tr>
<tr><td>Kurier</td><td>4,90 €</td><td>innerhalb 24 Stunden</td></tr>
<tr><td>Persönliche Abholung — Bratislava</td><td>kostenlos</td><td>nach telefonischer Absprache</td></tr>
</table>
<p>Ab einem Bestellwert von <strong>50 €</strong> ist der Versand kostenlos. Sie können per Überweisung
(gebührenfrei) oder per Nachnahme (+1,20 €) zahlen.</p>

<h2>Fragen?</h2>
<p>Schreiben Sie an <a href="mailto:info@gelavit.sk">info@gelavit.sk</a> oder rufen Sie
<a href="tel:+421915178349">+421 915 178 349</a> an, Mo–Fr 9:00–16:00.</p>
"""}


# Upozornenie na vrchu právnych stránok. Je to odkaz pre teba, nie pre
# zákazníka — keď texty prejde právnik, prepni na False a upozornenie
# zmizne zo všetkých troch jazykov naraz.
SHOW_LEGAL_NOTICE = True

_TERMS_NOTE = {
    "sk": "<p class=\"notice\">Tento dokument je prevzatý z pôvodného webu gelavit.sk a skrátený do prehľadnejšej podoby. Pred spustením e-shopu ho dajte skontrolovať právnikovi — najmä články o odstúpení od zmluvy, reklamáciách a alternatívnom riešení sporov, ktoré sa od roku 2022 menili.</p>",
    "en": "<p class=\"notice\">This document is taken from the original gelavit.sk website and shortened. Have it reviewed by a lawyer before launching the shop — especially the sections on withdrawal, complaints and alternative dispute resolution, which have changed since 2022.</p>",
    "de": "<p class=\"notice\">Dieses Dokument stammt von der ursprünglichen Website gelavit.sk und wurde gekürzt. Lassen Sie es vor dem Start des Shops von einem Anwalt prüfen — insbesondere die Abschnitte zu Widerruf, Reklamationen und alternativer Streitbeilegung.</p>",
}

TERMS = {"sk": _TERMS_NOTE["sk"] + """
<h2>I. Všeobecné ustanovenia</h2>
<p>Prevádzkovateľom internetového obchodu gelavit.sk je <strong>Gelavit s. r. o.</strong>, Kopčianska 8,
851 01 Bratislava, IČO 48 288 691, DIČ 2120117241, IČ DPH SK2120117241, zapísaná v OR OS Bratislava I,
odd. Sro, vl. č. 106031/B (ďalej „predávajúci“).</p>
<p>Tieto obchodné podmienky upravujú práva a povinnosti zmluvných strán vyplývajúce z kúpnej zmluvy
uzatvorenej medzi predávajúcim a kupujúcim prostredníctvom internetového obchodu gelavit.sk.</p>

<h2>II. Objednávka a uzavretie zmluvy</h2>
<p>Kupujúci objednáva tovar vyplnením a odoslaním objednávkového formulára. Odoslaná objednávka je
návrhom na uzavretie kúpnej zmluvy. Kúpna zmluva je uzavretá momentom doručenia potvrdenia objednávky
predávajúcim na e-mail kupujúceho.</p>
<p>Kupujúci je povinný uviesť pravdivé a úplné údaje. Predávajúci si vyhradzuje právo objednávku
nepotvrdiť, ak je tovar vypredaný, ak sú údaje zjavne nesprávne alebo ak nie je možné objednávku overiť.</p>

<h2>III. Ceny</h2>
<p>Všetky ceny uvedené v e-shope sú konečné, vrátane DPH. Cena dopravy je uvedená osobitne v pokladni.
Pri objednávke nad 50 € je doprava po Slovensku zdarma.</p>

<h2>IV. Dodacie podmienky</h2>
<p>Objednávky prijaté do 12:00 v pracovný deň sú spravidla expedované v ten istý deň. Dodacia lehota je
2–3 pracovné dni pri doručení Slovenskou poštou a spravidla do 24 hodín pri doručení kuriérom. Ak tovar
nie je skladom, predávajúci o tom kupujúceho bezodkladne informuje.</p>

<h2>V. Platobné podmienky</h2>
<p>Kupujúci môže za tovar zaplatiť prevodom na účet predávajúceho (bez poplatku) alebo dobierkou pri
prevzatí (+1,20 €). Faktúra je zasielaná elektronicky na e-mail kupujúceho.</p>

<h2>VI. Odstúpenie od zmluvy</h2>
<p>Kupujúci, ktorý je spotrebiteľom, má právo odstúpiť od zmluvy bez uvedenia dôvodu do
<strong>14 dní</strong> odo dňa prevzatia tovaru. Odstúpenie je potrebné oznámiť písomne na
<a href="mailto:info@gelavit.sk">info@gelavit.sk</a>.</p>
<p>Tovar musí byť vrátený nepoužitý, nepoškodený a v pôvodnom obale. Náklady na vrátenie tovaru znáša
kupujúci. Predávajúci vráti kupujúcemu všetky prijaté platby do 14 dní od doručenia oznámenia
o odstúpení.</p>
<p>Právo na odstúpenie sa nevzťahuje na tovar uzavretý v ochrannom obale, ktorý nie je vhodné vrátiť
z dôvodu ochrany zdravia alebo z hygienických dôvodov a ktorého ochranný obal bol po dodaní porušený.</p>

<h2>VII. Reklamácie a záruka</h2>
<p>Na predávaný tovar sa vzťahuje záručná doba podľa platných právnych predpisov, minimálne však doba
minimálnej trvanlivosti vyznačená na obale. Reklamáciu je potrebné uplatniť bez zbytočného odkladu
e-mailom na <a href="mailto:info@gelavit.sk">info@gelavit.sk</a> spolu s dokladom o kúpe a popisom vady.</p>
<p>Predávajúci vybaví reklamáciu najneskôr do 30 dní od jej uplatnenia.</p>

<h2>VIII. Alternatívne riešenie sporov</h2>
<p>Kupujúci má právo obrátiť sa na predávajúceho so žiadosťou o nápravu, ak nie je spokojný so spôsobom
vybavenia reklamácie. Ak predávajúci odpovie zamietavo alebo neodpovie do 30 dní, kupujúci má právo
podať návrh na začatie alternatívneho riešenia sporu subjektu ARS podľa zákona č. 391/2015 Z. z.
Zoznam subjektov ARS vedie Ministerstvo hospodárstva SR. Návrh je možné podať aj online cez platformu
<a href="https://ec.europa.eu/consumers/odr" rel="noopener" target="_blank">ec.europa.eu/consumers/odr</a>.</p>

<h2>IX. Záverečné ustanovenia</h2>
<p>Vzťahy neupravené týmito podmienkami sa riadia príslušnými ustanoveniami Občianskeho zákonníka,
zákona č. 102/2014 Z. z. o ochrane spotrebiteľa pri predaji na diaľku a zákona č. 22/2004 Z. z.
o elektronickom obchode.</p>
<p>Tieto obchodné podmienky nadobúdajú platnosť dňom ich zverejnenia na gelavit.sk.</p>
""", "en": _TERMS_NOTE["en"] + """
<h2>I. General provisions</h2>
<p>The operator of the gelavit.sk online shop is <strong>Gelavit s. r. o.</strong>, Kopčianska 8,
851 01 Bratislava, Slovakia, Company ID 48 288 691, Tax ID 2120117241, VAT ID SK2120117241, registered
with the Commercial Register of the District Court Bratislava I, section Sro, file no. 106031/B
(the “seller”).</p>

<h2>II. Order and conclusion of contract</h2>
<p>The buyer orders goods by completing and submitting the order form. A submitted order is a proposal to
conclude a purchase contract. The contract is concluded when the seller delivers an order confirmation to
the buyer's e-mail address.</p>

<h2>III. Prices</h2>
<p>All prices shown in the shop are final and include VAT. Shipping is shown separately at checkout.
Shipping within Slovakia is free on orders over €50.</p>

<h2>IV. Delivery terms</h2>
<p>Orders received before 12:00 on a working day are usually dispatched the same day. Delivery takes 2–3
working days by post and usually 24 hours by courier. If an item is out of stock, the seller informs the
buyer without delay.</p>

<h2>V. Payment terms</h2>
<p>The buyer may pay by bank transfer (no fee) or cash on delivery (+€1.20). The invoice is sent
electronically to the buyer's e-mail.</p>

<h2>VI. Withdrawal from the contract</h2>
<p>A buyer who is a consumer has the right to withdraw from the contract without giving a reason within
<strong>14 days</strong> of receiving the goods. Withdrawal must be announced in writing to
<a href="mailto:info@gelavit.sk">info@gelavit.sk</a>.</p>
<p>The goods must be returned unused, undamaged and in the original packaging. The cost of return is
borne by the buyer. The seller refunds all payments received within 14 days of receiving the withdrawal
notice.</p>
<p>The right of withdrawal does not apply to goods sealed in protective packaging which are unsuitable for
return for health-protection or hygiene reasons and whose seal was broken after delivery.</p>

<h2>VII. Complaints and warranty</h2>
<p>The goods are covered by the statutory warranty period, at minimum the best-before date marked on the
packaging. Complaints must be raised without undue delay by e-mail at
<a href="mailto:info@gelavit.sk">info@gelavit.sk</a>, together with proof of purchase and a description
of the defect. The seller settles complaints within 30 days.</p>

<h2>VIII. Alternative dispute resolution</h2>
<p>If the buyer is not satisfied with the handling of a complaint, they may ask the seller for redress. If
the seller responds negatively or does not respond within 30 days, the buyer may file a proposal for
alternative dispute resolution under Act No. 391/2015 Coll. A proposal may also be filed online via
<a href="https://ec.europa.eu/consumers/odr" rel="noopener" target="_blank">ec.europa.eu/consumers/odr</a>.</p>

<h2>IX. Final provisions</h2>
<p>Matters not covered by these terms are governed by the Slovak Civil Code, Act No. 102/2014 Coll. on
consumer protection in distance selling, and Act No. 22/2004 Coll. on electronic commerce.</p>
""", "de": _TERMS_NOTE["de"] + """
<h2>I. Allgemeine Bestimmungen</h2>
<p>Betreiber des Online-Shops gelavit.sk ist <strong>Gelavit s. r. o.</strong>, Kopčianska 8,
851 01 Bratislava, Slowakei, Firmen-ID 48 288 691, Steuer-ID 2120117241, USt-IdNr. SK2120117241,
eingetragen im Handelsregister des Bezirksgerichts Bratislava I, Abt. Sro, Einlage Nr. 106031/B
(der „Verkäufer“).</p>

<h2>II. Bestellung und Vertragsabschluss</h2>
<p>Der Käufer bestellt Ware durch Ausfüllen und Absenden des Bestellformulars. Eine abgesendete Bestellung
ist ein Antrag auf Abschluss eines Kaufvertrags. Der Vertrag kommt zustande, sobald der Verkäufer eine
Bestellbestätigung an die E-Mail-Adresse des Käufers sendet.</p>

<h2>III. Preise</h2>
<p>Alle im Shop angegebenen Preise sind Endpreise inkl. MwSt. Die Versandkosten werden an der Kasse
gesondert ausgewiesen. Ab einem Bestellwert von 50 € ist der Versand innerhalb der Slowakei kostenlos.</p>

<h2>IV. Lieferbedingungen</h2>
<p>Bestellungen, die werktags bis 12:00 Uhr eingehen, werden in der Regel am selben Tag versandt. Die
Lieferung dauert per Post 2–3 Werktage, per Kurier in der Regel 24 Stunden.</p>

<h2>V. Zahlungsbedingungen</h2>
<p>Der Käufer kann per Banküberweisung (gebührenfrei) oder per Nachnahme (+1,20 €) zahlen. Die Rechnung
wird elektronisch an die E-Mail-Adresse des Käufers gesendet.</p>

<h2>VI. Widerruf</h2>
<p>Ein Käufer, der Verbraucher ist, hat das Recht, innerhalb von <strong>14 Tagen</strong> nach Erhalt der
Ware ohne Angabe von Gründen vom Vertrag zurückzutreten. Der Widerruf ist schriftlich an
<a href="mailto:info@gelavit.sk">info@gelavit.sk</a> zu richten.</p>
<p>Die Ware muss unbenutzt, unbeschädigt und in der Originalverpackung zurückgesandt werden. Die Kosten
der Rücksendung trägt der Käufer. Der Verkäufer erstattet alle erhaltenen Zahlungen innerhalb von
14 Tagen nach Zugang der Widerrufserklärung.</p>
<p>Das Widerrufsrecht gilt nicht für versiegelte Waren, die aus Gründen des Gesundheitsschutzes oder der
Hygiene nicht zur Rückgabe geeignet sind, wenn ihre Versiegelung nach der Lieferung entfernt wurde.</p>

<h2>VII. Reklamationen und Gewährleistung</h2>
<p>Für die Ware gilt die gesetzliche Gewährleistungsfrist, mindestens jedoch das auf der Verpackung
angegebene Mindesthaltbarkeitsdatum. Reklamationen sind unverzüglich per E-Mail an
<a href="mailto:info@gelavit.sk">info@gelavit.sk</a> mit Kaufbeleg und Mängelbeschreibung zu melden.
Der Verkäufer bearbeitet Reklamationen innerhalb von 30 Tagen.</p>

<h2>VIII. Alternative Streitbeilegung</h2>
<p>Ist der Käufer mit der Bearbeitung einer Reklamation nicht zufrieden, kann er den Verkäufer um Abhilfe
bitten. Antwortet der Verkäufer ablehnend oder nicht innerhalb von 30 Tagen, kann der Käufer ein
Verfahren zur alternativen Streitbeilegung nach dem Gesetz Nr. 391/2015 Slg. einleiten. Ein Antrag kann
auch online über
<a href="https://ec.europa.eu/consumers/odr" rel="noopener" target="_blank">ec.europa.eu/consumers/odr</a>
gestellt werden.</p>

<h2>IX. Schlussbestimmungen</h2>
<p>Nicht geregelte Fragen richten sich nach dem slowakischen Bürgerlichen Gesetzbuch, dem Gesetz
Nr. 102/2014 Slg. über den Verbraucherschutz im Fernabsatz und dem Gesetz Nr. 22/2004 Slg. über den
elektronischen Geschäftsverkehr.</p>
"""}


PRIVACY = {"sk": _TERMS_NOTE["sk"] + """
<h2>1. Prevádzkovateľ</h2>
<p><strong>Gelavit s. r. o.</strong>, Kopčianska 8, 851 01 Bratislava, IČO 48 288 691,
e-mail <a href="mailto:info@gelavit.sk">info@gelavit.sk</a>, tel. +421 915 178 349.</p>

<h2>2. Aké údaje spracúvame</h2>
<ul>
<li><strong>Objednávka:</strong> meno a priezvisko, e-mail, telefón, doručovacia adresa, prípadne
fakturačné údaje firmy a poznámka k objednávke.</li>
<li><strong>Kontaktný formulár:</strong> meno, e-mail, obsah správy.</li>
<li><strong>Newsletter:</strong> e-mailová adresa (len s vaším súhlasom).</li>
<li><strong>Technické údaje:</strong> obsah nákupného košíka uložený vo vašom prehliadači
(localStorage). Tieto údaje neopúšťajú vaše zariadenie, kým neodošlete objednávku.</li>
</ul>

<h2>3. Právny základ a účel</h2>
<table>
<tr><th>Účel</th><th>Právny základ</th><th>Doba uchovávania</th></tr>
<tr><td>Vybavenie objednávky</td><td>plnenie zmluvy (čl. 6 ods. 1 písm. b GDPR)</td><td>10 rokov (účtovné doklady)</td></tr>
<tr><td>Odpoveď na správu</td><td>oprávnený záujem (čl. 6 ods. 1 písm. f)</td><td>1 rok</td></tr>
<tr><td>Newsletter</td><td>súhlas (čl. 6 ods. 1 písm. a)</td><td>do odvolania súhlasu</td></tr>
</table>

<h2>4. Komu údaje odovzdávame</h2>
<p>Vaše údaje odovzdávame len v rozsahu nevyhnutnom na doručenie a účtovníctvo: prepravcovi (Slovenská
pošta, kuriérska spoločnosť), účtovnej firme a poskytovateľovi hostingu a e-mailových služieb. So všetkými
máme uzatvorené zmluvy o spracúvaní osobných údajov. Údaje neprenášame mimo EÚ a nepredávame ich tretím
stranám.</p>

<h2>5. Vaše práva</h2>
<p>Máte právo na prístup k svojim údajom, ich opravu, vymazanie, obmedzenie spracúvania, prenosnosť
a právo namietať proti spracúvaniu. Súhlas so spracúvaním (napr. newsletter) môžete kedykoľvek odvolať
e-mailom na <a href="mailto:info@gelavit.sk">info@gelavit.sk</a>.</p>
<p>Ak sa domnievate, že vaše údaje spracúvame v rozpore s predpismi, máte právo podať sťažnosť
Úradu na ochranu osobných údajov SR, Hraničná 12, 820 07 Bratislava.</p>

<h2>6. Cookies</h2>
<p>Web gelavit.sk používa iba <strong>technicky nevyhnutné úložisko prehliadača</strong> na uchovanie
obsahu košíka. Nepoužívame reklamné ani analytické cookies tretích strán. Ak v budúcnosti pridáme
napríklad Google Analytics alebo Meta Pixel, vyžiadame si na to váš súhlas cez cookie lištu.</p>
""", "en": _TERMS_NOTE["en"] + """
<h2>1. Controller</h2>
<p><strong>Gelavit s. r. o.</strong>, Kopčianska 8, 851 01 Bratislava, Slovakia, Company ID 48 288 691,
e-mail <a href="mailto:info@gelavit.sk">info@gelavit.sk</a>, tel. +421 915 178 349.</p>

<h2>2. What data we process</h2>
<ul>
<li><strong>Order:</strong> name, e-mail, phone, delivery address, company billing details and order note.</li>
<li><strong>Contact form:</strong> name, e-mail, message content.</li>
<li><strong>Newsletter:</strong> e-mail address (only with your consent).</li>
<li><strong>Technical data:</strong> the contents of your shopping cart stored in your browser
(localStorage). This data never leaves your device until you submit an order.</li>
</ul>

<h2>3. Legal basis and purpose</h2>
<table>
<tr><th>Purpose</th><th>Legal basis</th><th>Retention</th></tr>
<tr><td>Order fulfilment</td><td>performance of a contract (Art. 6(1)(b) GDPR)</td><td>10 years (accounting)</td></tr>
<tr><td>Replying to a message</td><td>legitimate interest (Art. 6(1)(f))</td><td>1 year</td></tr>
<tr><td>Newsletter</td><td>consent (Art. 6(1)(a))</td><td>until consent is withdrawn</td></tr>
</table>

<h2>4. Who we share data with</h2>
<p>We pass your data on only to the extent necessary for delivery and accounting: the carrier (Slovak
Post, courier company), our accounting firm and our hosting and e-mail providers. We have data processing
agreements with all of them. We do not transfer data outside the EU and never sell it.</p>

<h2>5. Your rights</h2>
<p>You have the right to access, rectify, erase, restrict processing of and port your data, and to object
to processing. You may withdraw consent (e.g. for the newsletter) at any time at
<a href="mailto:info@gelavit.sk">info@gelavit.sk</a>.</p>
<p>You also have the right to lodge a complaint with the Office for Personal Data Protection of the Slovak
Republic, Hraničná 12, 820 07 Bratislava.</p>

<h2>6. Cookies</h2>
<p>gelavit.sk uses only <strong>strictly necessary browser storage</strong> to keep the cart contents.
We use no third-party advertising or analytics cookies. If we ever add tools such as Google Analytics or
the Meta Pixel, we will ask for your consent via a cookie banner.</p>
""", "de": _TERMS_NOTE["de"] + """
<h2>1. Verantwortlicher</h2>
<p><strong>Gelavit s. r. o.</strong>, Kopčianska 8, 851 01 Bratislava, Slowakei, Firmen-ID 48 288 691,
E-Mail <a href="mailto:info@gelavit.sk">info@gelavit.sk</a>, Tel. +421 915 178 349.</p>

<h2>2. Welche Daten wir verarbeiten</h2>
<ul>
<li><strong>Bestellung:</strong> Name, E-Mail, Telefon, Lieferadresse, ggf. Firmen-Rechnungsdaten und
Anmerkung zur Bestellung.</li>
<li><strong>Kontaktformular:</strong> Name, E-Mail, Nachrichteninhalt.</li>
<li><strong>Newsletter:</strong> E-Mail-Adresse (nur mit Ihrer Einwilligung).</li>
<li><strong>Technische Daten:</strong> der Inhalt Ihres Warenkorbs, gespeichert in Ihrem Browser
(localStorage). Diese Daten verlassen Ihr Gerät erst, wenn Sie eine Bestellung absenden.</li>
</ul>

<h2>3. Rechtsgrundlage und Zweck</h2>
<table>
<tr><th>Zweck</th><th>Rechtsgrundlage</th><th>Speicherdauer</th></tr>
<tr><td>Abwicklung der Bestellung</td><td>Vertragserfüllung (Art. 6 Abs. 1 lit. b DSGVO)</td><td>10 Jahre (Buchhaltung)</td></tr>
<tr><td>Beantwortung einer Nachricht</td><td>berechtigtes Interesse (Art. 6 Abs. 1 lit. f)</td><td>1 Jahr</td></tr>
<tr><td>Newsletter</td><td>Einwilligung (Art. 6 Abs. 1 lit. a)</td><td>bis zum Widerruf</td></tr>
</table>

<h2>4. An wen wir Daten weitergeben</h2>
<p>Wir geben Ihre Daten nur im für Lieferung und Buchhaltung notwendigen Umfang weiter: an den
Transporteur (Slowakische Post, Kurierdienst), unser Buchhaltungsbüro sowie Hosting- und E-Mail-Anbieter.
Mit allen bestehen Auftragsverarbeitungsverträge. Eine Übermittlung außerhalb der EU findet nicht statt.</p>

<h2>5. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung,
Datenübertragbarkeit und Widerspruch. Eine Einwilligung (z. B. Newsletter) können Sie jederzeit unter
<a href="mailto:info@gelavit.sk">info@gelavit.sk</a> widerrufen.</p>
<p>Zudem haben Sie das Recht, sich beim Amt für den Schutz personenbezogener Daten der Slowakischen
Republik, Hraničná 12, 820 07 Bratislava, zu beschweren.</p>

<h2>6. Cookies</h2>
<p>gelavit.sk verwendet ausschließlich <strong>technisch notwendigen Browser-Speicher</strong> für den
Warenkorb. Wir setzen keine Werbe- oder Analyse-Cookies Dritter ein. Sollten wir künftig Werkzeuge wie
Google Analytics oder das Meta-Pixel einsetzen, holen wir Ihre Einwilligung über ein Cookie-Banner ein.</p>
"""}


# ================================================== STATICKÉ SVG A SEO ======
FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#16283A"/>
<text x="32" y="43" text-anchor="middle" font-family="Georgia, serif" font-size="34" font-weight="700" fill="#FBF8F3">G<tspan fill="#E2573C">a</tspan></text>
</svg>"""

COLLAGEN_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 420" width="520" height="420" role="img" aria-label="Trojitá skrutkovica kolagénu">
<defs>
  <linearGradient id="s1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#E2573C"/><stop offset="100%" stop-color="#F2B23E"/></linearGradient>
  <linearGradient id="s2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#6F8F73"/><stop offset="100%" stop-color="#A8C0A5"/></linearGradient>
  <linearGradient id="s3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#16283A"/><stop offset="100%" stop-color="#4A6579"/></linearGradient>
</defs>
<g fill="none" stroke-width="7" stroke-linecap="round">
  <path d="M60,210 C110,90 160,330 210,210 C260,90 310,330 360,210 C410,90 440,300 470,220" stroke="url(#s1)" opacity=".95"/>
  <path d="M60,240 C110,120 160,360 210,240 C260,120 310,360 360,240 C410,120 440,330 470,250" stroke="url(#s2)" opacity=".9"/>
  <path d="M60,180 C110,60 160,300 210,180 C260,60 310,300 360,180 C410,60 440,270 470,190" stroke="url(#s3)" opacity=".85"/>
</g>
<g stroke="#16283A" stroke-opacity=".16" stroke-width="1.6">
  <path d="M85,150 L85,255"/><path d="M150,175 L150,275"/><path d="M215,150 L215,255"/>
  <path d="M285,175 L285,275"/><path d="M350,150 L350,255"/><path d="M420,145 L420,250"/>
</g>
<g fill="#16283A" font-family="Helvetica, Arial, sans-serif" font-size="11" letter-spacing="2" opacity=".55">
  <text x="60" y="360">GLYCÍN</text><text x="200" y="360">PROLÍN</text><text x="350" y="360">LYZÍN</text>
</g>
<text x="60" y="392" font-family="Georgia, serif" font-size="15" fill="#E2573C">Typ I · trojitá skrutkovica</text>
</svg>"""

FOUNDER_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 560" width="520" height="560" role="img" aria-label="">
<defs><linearGradient id="fg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#F6F0E7"/><stop offset="100%" stop-color="#E9DFCE"/></linearGradient></defs>
<rect width="520" height="560" fill="url(#fg)"/>
<circle cx="260" cy="200" r="86" fill="#D8C9B2"/>
<path d="M120,560 C120,420 176,344 260,344 C344,344 400,420 400,560 Z" fill="#C9B79C"/>
<g stroke="#16283A" stroke-opacity=".14" stroke-width="1.5" fill="none">
  <path d="M40,470 C110,430 150,500 220,462"/><path d="M300,500 C370,462 410,530 480,492"/>
</g>
<g opacity=".5">
  <path d="M418,96 c22,-26 62,-22 62,14 c0,32 -38,52 -62,74 c-24,-22 -62,-42 -62,-74 c0,-36 40,-40 62,-14z" fill="#6F8F73" opacity=".35"/>
</g>
<text x="46" y="60" font-family="Georgia, serif" font-size="26" fill="#16283A" opacity=".8">Nina Bernardo</text>
<text x="47" y="84" font-family="Helvetica, Arial, sans-serif" font-size="11" letter-spacing="3.5" fill="#5E7183">GELAVIT · 2015</text>
</svg>"""

OG_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
<rect width="1200" height="630" fill="#FBF8F3"/>
<circle cx="980" cy="300" r="300" fill="#F1E9DC"/>
<text x="90" y="250" font-family="Georgia, serif" font-size="82" font-weight="600" fill="#16283A">Gel<tspan fill="#E2573C">a</tspan>Vit Pure®</text>
<text x="94" y="300" font-family="Helvetica, Arial, sans-serif" font-size="20" letter-spacing="7" fill="#5E7183">BIOAKTÍVNY KOLAGÉN TYPU I</text>
<text x="90" y="380" font-family="Georgia, serif" font-size="40" fill="#16283A">Kolagén, ktorý telo naozaj využije.</text>
<text x="90" y="450" font-family="Helvetica, Arial, sans-serif" font-size="22" fill="#5E7183">97 % kolagénu · vitamín C · bez éčiek a konzervantov</text>
<rect x="90" y="500" width="230" height="58" rx="29" fill="#E2573C"/>
<text x="205" y="537" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="19" font-weight="700" fill="#fff">gelavit.sk</text>
</svg>"""


def write_static_assets(SITE):
    img = SITE / "assets" / "img"
    img.mkdir(parents=True, exist_ok=True)
    pass  # obrázky rieši gen/images.py


REDIRECTS = """# 301 presmerovania zo starých WordPress URL na nový statický web.
# Skopírujte obsah do .htaccess v koreni webu (Apache).
"""


def write_seo(SITE, SITE_URL, urls):
    today = "2026-08-17"
    body = "\n".join(
        f'  <url><loc>{SITE_URL}{u}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>'
        for u, pr in urls)
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + '\n</urlset>\n')

    (SITE / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n"
        "Disallow: /kosik.html\nDisallow: /pokladna.html\nDisallow: /dakujeme.html\n"
        "Disallow: /en/cart.html\nDisallow: /en/checkout.html\nDisallow: /en/thank-you.html\n"
        "Disallow: /de/warenkorb.html\nDisallow: /de/kasse.html\nDisallow: /de/danke.html\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n")

    # 301 mapa starých WP URL
    old_new = [
        ("/produkty/", "/produkty.html"),
        ("/produkt/gelavit-pure-ananas/", "/produkt-gelavit-pure-ananas.html"),
        ("/produkt/gelavit-pure-vitamin-c/", "/produkt-gelavit-pure-vitamin-c.html"),
        ("/produkt/gelavit-pure-ananas-box/", "/produkt-gelavit-pure-ananas-box.html"),
        ("/produkt/gelavit-pure-lieskovy-orech/", "/produkt-gelavit-pure-lieskovy-orech.html"),
        ("/produkt/gelavit-pure-kokosove-mlieko/", "/produkt-gelavit-pure-kokosove-mlieko.html"),
        ("/produkt/gelavit-pure-kolagenovy-napoj-mango/", "/produkt-gelavit-napoj-mango.html"),
        ("/produkt/gelavit-zele-mango/", "/produkt-gelavit-zele-mango.html"),
        ("/produkt/kolagenova-cokolada-s-kokosovym-mliekom/", "/produkt-kolagenova-cokolada-kokos.html"),
        ("/o-nas/", "/o-nas.html"),
        ("/kontakt/", "/kontakt.html"),
        ("/blog/", "/blog.html"),
        ("/ako-objednat/", "/ako-objednat.html"),
        ("/obchodne-podmienky/", "/obchodne-podmienky.html"),
        ("/informacie/", "/ako-objednat.html"),
        ("/kosik/", "/kosik.html"),
        ("/pokladna/", "/pokladna.html"),
        ("/moj-ucet/", "/kontakt.html"),
        ("/products/", "/en/products.html"),
        ("/about-us/", "/en/about-us.html"),
        ("/contact/", "/en/contact.html"),
        ("/how-to-order/", "/en/how-to-order.html"),
        ("/terms-and-conditions/", "/en/terms-and-conditions.html"),
        ("/produkte/", "/de/produkte.html"),
        ("/uber-uns/", "/de/ueber-uns.html"),
        ("/wie-bestelle-ich/", "/de/wie-bestelle-ich.html"),
        ("/agb-geschaftsbedingungen/", "/de/agb.html"),
        ("/kolagen-nenahraditelna-bielkovina/", "/clanok-kolagen-nenahraditelna-bielkovina.html"),
        ("/sukraloza-a-jej-pozitiva/", "/clanok-sukraloza-a-jej-pozitiva.html"),
        ("/intenzivna-kolagenova-kura-gelavit-pure/", "/clanok-intenzivna-kolagenova-kura.html"),
        ("/kolagen-pre-vsetkych-od-gelavitu-a-jeho-vyznam/", "/clanok-kolagen-pre-vsetkych-a-jeho-vyznam.html"),
        ("/idealne-samostatne-balenia-na-vylety-ci-dovolenku/", "/clanok-samostatne-balenia-na-cesty.html"),
        ("/vyhlasenie-o-zasadach-ochrany-osobnych-udajov%ef%bf%bc/", "/ochrana-osobnych-udajov.html"),
        ("/personal-data-protection/", "/en/privacy-policy.html"),
    ]
    ht = ["# ---- GelaVit statický web: Apache konfigurácia ----",
          "Options -Indexes",
          "DirectoryIndex index.html", "",
          "<IfModule mod_rewrite.c>",
          "  RewriteEngine On", "",
          "  # www -> non-www + HTTPS",
          "  RewriteCond %{HTTPS} off [OR]",
          "  RewriteCond %{HTTP_HOST} ^www\\. [NC]",
          "  RewriteRule ^(.*)$ https://gelavit.sk/$1 [R=301,L]", ""]
    ht.append("  # ---- 301 zo starých WordPress URL ----")
    for o, n in old_new:
        ht.append(f'  RewriteRule "^{o.lstrip("/").rstrip("/")}/?$" "{n}" [R=301,L]')
    ht += ["",
           "  # WordPress spam a zvyšky -> 410 Gone (nech ich Google vyhodí z indexu)",
           '  RewriteRule "^(wp-content|wp-includes|wp-admin|wp-json|xmlrpc\\.php)" - [G,L]',
           "</IfModule>", "",
           "# ---- Chybové stránky ----",
           "ErrorDocument 404 /404.html", "",
           "# ---- Kompresia ----",
           "<IfModule mod_deflate.c>",
           "  AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml application/javascript application/json image/svg+xml",
           "</IfModule>", "",
           "# ---- Cache ----",
           "<IfModule mod_expires.c>",
           "  ExpiresActive On",
           '  ExpiresByType text/css "access plus 1 year"',
           '  ExpiresByType application/javascript "access plus 1 year"',
           '  ExpiresByType image/svg+xml "access plus 1 year"',
           '  ExpiresByType image/png "access plus 1 year"',
           '  ExpiresByType text/html "access plus 1 hour"',
           "</IfModule>", "",
           "# ---- Bezpečnostné hlavičky ----",
           "<IfModule mod_headers.c>",
           '  Header set X-Content-Type-Options "nosniff"',
           '  Header set Referrer-Policy "strict-origin-when-cross-origin"',
           '  Header set X-Frame-Options "SAMEORIGIN"',
           "</IfModule>", ""]
    (SITE / ".htaccess").write_text("\n".join(ht))

    # Netlify
    (SITE / "_redirects").write_text(
        "\n".join(f"{o}  {n}  301" for o, n in old_new) + "\n")

    # Vercel — _redirects ani .htaccess tam neplatia, presmerovania sa
    # zapisujú do vercel.json v koreni nasadenia.
    import json as _json
    (SITE / "vercel.json").write_text(_json.dumps({
        "cleanUrls": False,
        "trailingSlash": False,
        "redirects": [{"source": o.rstrip("/") or "/", "destination": n,
                       "permanent": True} for o, n in old_new],
        "headers": [{
            "source": "/(.*)",
            "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
            ],
        }, {
            "source": "/assets/(.*)",
            "headers": [{"key": "Cache-Control",
                         "value": "public, max-age=31536000, immutable"}],
        }],
    }, ensure_ascii=False, indent=2) + "\n")
