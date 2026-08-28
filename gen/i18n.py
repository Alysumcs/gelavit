# -*- coding: utf-8 -*-
"""Všetky texty webu v SK / EN / DE."""

URLS = {
    "sk": {
        "home": "index.html", "products": "produkty.html", "about": "o-nas.html",
        "blog": "blog.html", "contact": "kontakt.html", "cart": "kosik.html",
        "checkout": "pokladna.html", "thanks": "dakujeme.html",
        "howto": "ako-objednat.html", "terms": "obchodne-podmienky.html",
        "privacy": "ochrana-osobnych-udajov.html",
        "product_prefix": "produkt-", "blog_prefix": "clanok-",
    },
    "en": {
        "home": "index.html", "products": "products.html", "about": "about-us.html",
        "blog": "blog.html", "contact": "contact.html", "cart": "cart.html",
        "checkout": "checkout.html", "thanks": "thank-you.html",
        "howto": "how-to-order.html", "terms": "terms-and-conditions.html",
        "privacy": "privacy-policy.html",
        "product_prefix": "product-", "blog_prefix": "article-",
    },
    "de": {
        "home": "index.html", "products": "produkte.html", "about": "ueber-uns.html",
        "blog": "blog.html", "contact": "kontakt.html", "cart": "warenkorb.html",
        "checkout": "kasse.html", "thanks": "danke.html",
        "howto": "wie-bestelle-ich.html", "terms": "agb.html",
        "privacy": "datenschutz.html",
        "product_prefix": "produkt-", "blog_prefix": "artikel-",
    },
}

T = {}

# ---------------------------------------------------------------- SLOVAK ----
T["sk"] = {
    "announce": 'Doprava zdarma pri objednávke nad <strong>50 €</strong> · Odosielame do 24 hodín',
    "nav_label": "Hlavná navigácia", "lang_label": "Jazyk", "menu": "Menu", "close": "Zavrieť",
    "nav_home": "Úvod", "nav_products": "Produkty", "nav_about": "O nás",
    "nav_blog": "Blog", "nav_contact": "Kontakt", "nav_cart": "Košík",
    "nav_howto": "Ako objednať", "nav_terms": "Obchodné podmienky", "nav_privacy": "Ochrana osobných údajov",

    "hero_eyebrow": "Bioaktívny kolagén typu I",
    "hero_h1": 'Kolagén, ktorý telo <em>naozaj</em> využije.',
    "hero_lead": "Gelavit Pure® obsahuje až 97 % hydrolyzovaného rybieho kolagénu s vitamínom C. Bez éčiek, bez farbív, bez konzervantov — vyvinuté na Slovensku od roku 2015.",
    "hero_cta": "Prezrieť produkty", "hero_cta2": "Prečo kolagén?",
    "hero_for": "Pre",
    "seal_ring": "97 % KOLAGÉN · BEZ ÉČIEK · SLOVENSKO · ",
    "hero_rotate": ["kĺby", "pleť", "vlasy", "nechty", "kosti", "šľachy"],
    "hero_note": "Klinicky testovaný kolagén so zvýšenou vstrebateľnosťou",
    "badge_collagen": "bioaktívneho<br>kolagénu", "badge_type": "5 000 mg kolagénu<br>v jednej dávke",

    "trust": ["Bez éčiek", "Prvotriedna kvalita", "Bez farbív a konzervantov", "Odoslanie do 24 h"],

    "problem_eyebrow": "Prečo GelaVit",
    "problem_h2": 'Kĺby si všimneme až vtedy, keď <em>zabolia</em>.',
    "problem_lead": "Dôležitosť správnej výživy kĺbov si väčšinou uvedomíme vo chvíli, keď nás rozbolia. Akoby sme razom zostarli o desiatky rokov — telo stratí pružnosť a preč je radosť z pohybu.",
    "problems": [
        {"h": "Aktívne športujete", "p": "Šľachy a kĺby pod pravidelnou záťažou potrebujú stavebný materiál, ktorý im bežná strava nedodá v dostatočnom množstve."},
        {"h": "Máte fyzicky náročnú prácu", "p": "Dlhé státie, zdvíhanie a opakovaný pohyb opotrebúvajú chrupavku rýchlejšie, než ju telo stihne obnoviť."},
        {"h": "Strácate vitalitu s vekom", "p": "Po tridsiatke tvorba vlastného kolagénu klesá — najskôr to vidno na pleti, potom to cítiť v kĺboch."},
    ],

    "shop_eyebrow": "Naša rada", "shop_h2": 'Kolagén v podobe, ktorá vám sadne.',
    "shop_all": "Všetky produkty",
    "products_h1": 'Všetky produkty GelaVit',
    "products_lead": "Prášky, intenzívne kúry, nápoje aj želé — všetko s bioaktívnym kolagénom typu I a vitamínom C.",

    "science_eyebrow": "Trocha vedy",
    "science_h2": 'Prečo je <em>kolagén</em> nenahraditeľný',
    "science_lead": "Kolagén je hlavnou stavebnou bielkovinou ľudského tela — tvorí takmer tretinu všetkých bielkovín. Najviac ho obsahujú podporné tkanivá: kosti, kĺby, šľachy a koža.",
    "science_points": [
        "Natívny kolagén sa nevstrebáva. <strong>Hydrolyzát</strong> obsahuje vo vode rozpustné peptidy, ktoré telo dokáže transportovať krvou tam, kde ich potrebuje.",
        "Bez <strong>vitamínu C</strong> nemá užívanie kolagénu prakticky žiadny efekt — preto ho pridávame do každého produktu.",
        "Používame <strong>rybí kolagén typu I</strong> — klinicky testovaný, s vyššou vstrebateľnosťou než bravčový či hovädzí.",
        "Vhodné aj pre ľudí s <strong>laktózovou intoleranciou</strong> a — vďaka sukralóze — aj pre diabetikov.",
    ],
    "science_cta": "Prečítať celý článok",

    "stats_eyebrow": "Čísla, ktoré rozhodujú", "stats_h2": "Zloženie bez kompromisov",
    "stats": [
        {"n": "97 %", "l": "bioaktívny kolagén"},
        {"n": "0", "l": "éčok a konzervantov"},
        {"n": "5 g", "l": "denná dávka"},
        {"n": "2015", "l": "na trhu od"},
    ],

    "how_eyebrow": "Ako to funguje", "how_h2": "Tri kroky, tridsať sekúnd denne",
    "step": "Krok",
    "how_steps": [
        {"h": "Odmerajte", "p": "1–2 kávové lyžičky prášku (cca 5 g), alebo jednoducho otvorte jedno vrecúško z intenzívnej kúry."},
        {"h": "Rozmiešajte", "p": "V 200 ml vody, džúsu, mlieka či smoothie. Rozpustí sa okamžite a nezráža sa."},
        {"h": "Vypite denne", "p": "Kľúčom je pravidelnosť. Telo si kolagén privedie tam, kde ho práve najviac potrebuje."},
    ],

    "quotes_eyebrow": "Skúsenosti zákazníkov", "quotes_h2": "Čo hovoria tí, čo Gelavit užívajú",
    "quotes": [
        {"q": "Po operácii kolena mi ortopéd odporučil kolagén. Gelavit má z toho, čo som skúšala, najvyšší obsah a nechutí ako liek.", "a": "Martina K., Bratislava"},
        {"q": "Beriem si box na služobné cesty — jedno vrecúško do fľaše s vodou a mám vybavené. Žiadne váženie, žiadny neporiadok.", "a": "Peter H., Košice"},
        {"q": "Po troch mesiacoch mi to najviac vidno na nechtoch a vlasoch. S kĺbmi to je pomalšie, ale ranná stuhnutosť je menšia.", "a": "Zuzana M., Žilina"},
    ],

    "faq_h2": "Časté otázky",
    "faq": [
        {"q": "Ako dlho trvá, kým kolagén zaberie?", "a": "Prvé zmeny na pleti, vlasoch a nechtoch zvyčajne vidno po 4–8 týždňoch pravidelného užívania. Pri kĺboch a šľachách je proces pomalší — odporúčame kúru minimálne 3 mesiace. Kľúčová je pravidelnosť: jedna vynechaná dávka nič nepokazí, mesiac pauzy áno."},
        {"q": "Prečo práve rybí kolagén?", "a": "Rybí (morský) kolagén je prevažne typu I — presne toho, z ktorého je tvorená koža, kosti a šľachy. Má menšie molekuly a vyššiu vstrebateľnosť než bravčový alebo hovädzí. Náš kolagén je klinicky testovaný."},
        {"q": "Musím k tomu brať vitamín C?", "a": "Nie — vitamín C je už súčasťou každého produktu Gelavit Pure®. Bez neho telo z prijatých aminokyselín vlastný kolagén nevytvorí, preto ho neriešime ako doplnok, ale ako nutnú súčasť receptúry."},
        {"q": "Je Gelavit vhodný pri laktózovej intolerancii alebo cukrovke?", "a": "Áno. Produkty neobsahujú laktózu. Ako sladidlo používame sukralózu, ktorá nemá vplyv na glykémiu a nezvyšuje hladinu krvného cukru — je preto vhodná aj pre diabetikov."},
        {"q": "Ako a kedy doručíte objednávku?", "a": "Objednávky prijaté do 12:00 v pracovný deň odosielame ešte v ten istý deň. Slovenskou poštou zvyčajne doručíme do 2–3 pracovných dní, kuriérom do 24 hodín. Pri objednávke nad 50 € máte dopravu zdarma."},
        {"q": "Môžem produkt vrátiť?", "a": "Áno, do 14 dní od prevzatia bez udania dôvodu — stačí, ak je tovar nepoužitý a v pôvodnom obale. Podrobnosti nájdete v obchodných podmienkach."},
    ],

    "cta_h2": 'Začnite dnes. Vaše kĺby vám <em>poďakujú</em>.',
    "cta_p": "Jedno vrecúško denne. Bez éčiek, bez konzervantov, s vitamínom C. Doprava zdarma nad 50 €.",

    # produkty / košík
    "add_to_cart": "Do košíka", "bestseller": "Bestseller", "out_of_stock": "Vypredané",
    "out_of_stock_long": "Momentálne vypredané", "in_stock": "Skladom — odosielame do 24 h",
    "notify_me": "Dajte mi vedieť, keď bude skladom",
    "qty": "Množstvo", "vat_incl": "vrátane DPH", "related": "Mohlo by sa vám hodiť",
    "related_products": "Produkty k článku",
    "spec_composition": "Zloženie", "spec_dosage": "Dávkovanie", "spec_pack": "Balenie", "spec_storage": "Skladovanie",
    "pdp_perks": ["Bez éčiek, farbív a konzervantov", "Vitamín C v každej dávke", "Odosielame do 24 hodín", "Doprava zdarma nad 50 €"],

    "cart_h1": "Váš košík", "cart_empty_h": "Košík je zatiaľ prázdny",
    "cart_empty_p": "Pridajte si produkty a vráťte sa sem — uložíme ich aj keď stránku zavriete.",
    "continue_shopping": "Pokračovať v nákupe", "summary": "Zhrnutie objednávky",
    "subtotal": "Medzisúčet", "shipping": "Doprava", "total": "Spolu", "payment_fee": "Poplatok za platbu",
    "at_checkout": "v pokladni", "to_checkout": "Prejsť do pokladne",
    "cart_note": "Ceny sú vrátane DPH. Doprava sa vypočíta v ďalšom kroku.",
    "edit_cart": "Upraviť košík", "remove": "Odstrániť", "free": "Zdarma",
    "freeLeft": "Do dopravy zdarma vám chýba {x}.", "freeGot": "Máte dopravu zdarma!",

    "checkout_h1": "Pokladňa",
    "co_contact": "Kontaktné údaje", "co_address": "Doručovacia adresa",
    "co_shipping": "Spôsob doručenia", "co_payment": "Spôsob platby", "co_note": "Poznámka a súhlasy",
    "f_name": "Meno a priezvisko", "f_email": "E-mail", "f_phone": "Telefón",
    "f_street": "Ulica a číslo", "f_zip": "PSČ", "f_city": "Mesto", "f_country": "Krajina",
    "f_company": "Firma (nepovinné)", "f_other": "Iná", "f_note": "Poznámka k objednávke",
    "f_subject": "Predmet", "f_message": "Správa",
    "consent_terms": 'Súhlasím s <a href="{terms}">obchodnými podmienkami</a> a so <a href="{privacy}">spracovaním osobných údajov</a>.',
    "consent_privacy": 'Súhlasím so <a href="{privacy}">spracovaním osobných údajov</a>.',
    "consent_news": "Chcem dostávať novinky a zľavy e-mailom (môžete kedykoľvek odhlásiť).",
    "place_order": "Odoslať objednávku",
    "checkout_note": "Odoslaním objednávky vzniká záväzok k platbe. Faktúru a platobné údaje vám pošleme e-mailom.",
    "free_from_note": "Pri objednávke nad 50 € je doprava zdarma.",
    "order_subject": "Nová objednávka z gelavit.sk",
    "added": "Pridané do košíka", "mailIntro": "Dobrý deň, rád/rada by som objednal/a:",

    "thanks_h1": "Ďakujeme za objednávku!",
    "thanks_p": "Objednávku sme prijali. Do niekoľkých minút vám na e-mail príde potvrdenie s rekapituláciou a platobnými údajmi.",
    "thanks_next": "Čo bude nasledovať",
    "thanks_steps": [
        "Potvrdenie objednávky vám príde e-mailom do niekoľkých minút.",
        "Pri platbe prevodom vám pošleme číslo účtu a variabilný symbol.",
        "Objednávky prijaté do 12:00 v pracovný deň odosielame ešte v ten istý deň.",
        "Máte otázku? Napíšte na <a href=\"mailto:info@gelavit.sk\">info@gelavit.sk</a> alebo zavolajte na +421 915 178 349.",
    ],

    # o nás
    "about_eyebrow": "Náš príbeh", "about_h1": 'Nech je tvoja strava <em>tvojím liekom</em>',
    "about_role": "zakladateľka spoločnosti",
    "about_values_eyebrow": "Na čom nám záleží", "about_values_h2": "Tri veci, na ktorých nezľavíme",
    "about_values": [
        {"h": "Čisté zloženie", "p": "Žiadne éčka, farbivá ani konzervanty. Ak niečo v zložení nemá funkciu, nie je tam."},
        {"h": "Overený kolagén", "p": "Klinicky testovaný rybí kolagén typu I so zvýšenou vstrebateľnosťou — nie najlacnejší, ale najúčinnejší."},
        {"h": "Chuť, ktorú vydržíte", "p": "Kúra funguje len vtedy, keď ju dokážete dodržať. Preto sme roky ladili príchute — ananás, orech, kokos, mango."},
    ],
    "about_history_eyebrow": "História spoločnosti", "about_history_h2": "Odkiaľ sme prišli",
    "about_history": [
        {"y": "2015", "t": "29. 8. 2015 — založenie spoločnosti Gelavit s. r. o."},
        {"y": "2016", "t": "Účasť na výstavách a priamom predaji. Nové distribučné siete, tvorba online marketingu a nových produktov."},
        {"y": "2017", "t": "Spolupráca so spoločnosťou DuMax pharma s. r. o. Uvedenie intenzívnej kúry v 28 samostatných vrecúškach."},
        {"y": "2018", "t": "Obchodná spolupráca s novými partnermi, aktívna účasť na výstavách a prednáškach."},
        {"y": "dnes", "t": "Produkty GelaVit sú dostupné v predajniach po celom Slovensku aj priamo v našom e-shope."},
    ],

    # kontakt
    "contact_eyebrow": "Sme tu pre vás", "contact_h1": "Kontakt a predajné miesta",
    "contact_lead": "Napíšte nám, zavolajte alebo si produkty vyzdvihnite osobne na jednom z našich predajných miest.",
    "contact_form_h": "Napíšte nám", "contact_billing": "Fakturačné údaje",
    "contact_points": "Predajné miesta", "contact_subject": "Správa z kontaktného formulára gelavit.sk",
    "send": "Odoslať správu", "open": "Otvorené", "slovakia": "Slovensko", "reg": "Registrácia",

    # blog
    "blog_eyebrow": "Magazín", "blog_h1": "O kolagéne, výžive a pohybe",
    "blog_lead": "Články o tom, ako kolagén funguje, prečo je dôležitý vitamín C a čo sa deje v tele, keď kúru dodržíte.",

    # footer
    "hero_photo_alt": "Tri balenia Gelavit Pure na drevenom stole s čerstvým ovocím",
    "badge_collagen_alt": "Bio aktívny 97 % kolagén s vitamínom C",
    "science_alt": "Hydrolyzovaný rybí kolagén v práškovej forme",
    "band_alt": "Celá rada produktov GelaVit — prášky, intenzívna kúra, želé aj čokoláda",
    "about_photo_alt": "Nina Bernardo, zakladateľka Gelavitu, na predajnej výstave",
    "marquee": [
        "97 % bioaktívneho kolagénu",
        "Vitamín C v každej dávke",
        "Bez éčiek a konzervantov",
        "Vyrobené na Slovensku",
        "Klinicky testovaný kolagén typu I",
        "Bez laktózy",
        "Vhodné aj pre diabetikov",
        "Odosielame do 24 hodín",
        "Doprava zdarma nad 50 €",
    ],

    "skip": 'Preskočiť na obsah',
    "view": 'Pozrieť',
    "scroll": 'Skrolujte',
    "showcase_eyebrow": 'Štyri príchute',
    "showcase_h2": 'Jedna receptúra, <em>štyri</em> chute.',
    "showcase_cta": 'Vybrať si',

    "footer_blurb": "Prírodná kĺbová výživa s bioaktívnym kolagénom typu I. Vyvinuté a vyrábané na Slovensku od roku 2015.",
    "footer_shop": "Obchod", "footer_info": "Informácie", "footer_contact": "Kontakt",
    "newsletter_title": "Novinky", "newsletter_cta": "Odoberať", "email": "Váš e-mail",
    "footer_disclaimer": "Výživové doplnky nenahrádzajú pestrú stravu a zdravý životný štýl.",
}

# --------------------------------------------------------------- ENGLISH ----
T["en"] = {
    "announce": 'Free shipping on orders over <strong>€50</strong> · Dispatched within 24 hours',
    "nav_label": "Main navigation", "lang_label": "Language", "menu": "Menu", "close": "Close",
    "nav_home": "Home", "nav_products": "Products", "nav_about": "About us",
    "nav_blog": "Blog", "nav_contact": "Contact", "nav_cart": "Cart",
    "nav_howto": "How to order", "nav_terms": "Terms and conditions", "nav_privacy": "Privacy policy",

    "hero_eyebrow": "Bioactive type I collagen",
    "hero_h1": 'Collagen your body <em>actually</em> uses.',
    "hero_lead": "Gelavit Pure® contains up to 97 % hydrolysed fish collagen with vitamin C. No E numbers, no colourings, no preservatives — developed in Slovakia since 2015.",
    "hero_cta": "Shop products", "hero_cta2": "Why collagen?",
    "hero_for": "For",
    "seal_ring": "97 % COLLAGEN · NO E NUMBERS · SLOVAKIA · ",
    "hero_rotate": ["joints", "skin", "hair", "nails", "bones", "tendons"],
    "hero_note": "Clinically tested collagen with increased absorption",
    "badge_collagen": "bioactive<br>collagen", "badge_type": "5,000 mg of collagen<br>per single dose",

    "trust": ["No E numbers", "First-class quality", "No colourings or preservatives", "Dispatched in 24 h"],

    "problem_eyebrow": "Why GelaVit",
    "problem_h2": 'We notice our joints only when they <em>start hurting</em>.',
    "problem_lead": "We usually realise how important joint nutrition is only once the pain arrives. In an instant we feel decades older — the body loses its flexibility and the joy of movement is gone.",
    "problems": [
        {"h": "You train regularly", "p": "Tendons and joints under repeated load need building material that an ordinary diet does not supply in sufficient amounts."},
        {"h": "Your work is physical", "p": "Long hours standing, lifting and repetitive movement wear cartilage faster than the body can rebuild it."},
        {"h": "You lose vitality with age", "p": "After thirty, your own collagen production drops — first you see it on your skin, then you feel it in your joints."},
    ],

    "shop_eyebrow": "Our range", "shop_h2": 'Collagen in a form that fits your day.',
    "shop_all": "All products",
    "products_h1": "All GelaVit products",
    "products_lead": "Powders, intense courses, drinks and jellies — all with bioactive type I collagen and vitamin C.",

    "science_eyebrow": "A little science",
    "science_h2": 'Why <em>collagen</em> is irreplaceable',
    "science_lead": "Collagen is the main structural protein of the human body — it makes up almost a third of all proteins. Supporting tissues contain the most of it: bones, joints, tendons and skin.",
    "science_points": [
        "Native collagen is not absorbed. A <strong>hydrolysate</strong> contains water-soluble peptides that the body can transport through the blood to where they are needed.",
        "Without <strong>vitamin C</strong>, taking collagen has virtually no effect — that is why we add it to every product.",
        "We use <strong>type I fish collagen</strong> — clinically tested, with higher absorption than porcine or bovine collagen.",
        "Suitable for people with <strong>lactose intolerance</strong> and, thanks to sucralose, also for diabetics.",
    ],
    "science_cta": "Read the full article",

    "stats_eyebrow": "The numbers that matter", "stats_h2": "A composition without compromise",
    "stats": [
        {"n": "97 %", "l": "bioactive collagen"},
        {"n": "0", "l": "E numbers & preservatives"},
        {"n": "5 g", "l": "daily dose"},
        {"n": "2015", "l": "on the market since"},
    ],

    "how_eyebrow": "How it works", "how_h2": "Three steps, thirty seconds a day",
    "step": "Step",
    "how_steps": [
        {"h": "Measure", "p": "1–2 teaspoons of powder (about 5 g), or simply open one sachet from the intense course."},
        {"h": "Mix", "p": "Into 200 ml of water, juice, milk or a smoothie. It dissolves instantly and does not clump."},
        {"h": "Drink daily", "p": "Consistency is the key. Your body will send the collagen where it is needed most."},
    ],

    "quotes_eyebrow": "Customer experience", "quotes_h2": "What people taking Gelavit say",
    "quotes": [
        {"q": "After knee surgery my orthopaedist recommended collagen. Of everything I tried, Gelavit has the highest content and it doesn't taste like medicine.", "a": "Martina K., Bratislava"},
        {"q": "I take the box on business trips — one sachet into a water bottle and I'm done. No scales, no mess.", "a": "Peter H., Košice"},
        {"q": "After three months I see it most on my nails and hair. Joints take longer, but the morning stiffness is milder.", "a": "Zuzana M., Žilina"},
    ],

    "faq_h2": "Frequently asked questions",
    "faq": [
        {"q": "How long does collagen take to work?", "a": "The first changes to skin, hair and nails are usually visible after 4–8 weeks of regular use. Joints and tendons take longer — we recommend a course of at least 3 months. Consistency matters: one missed dose changes nothing, a month off does."},
        {"q": "Why fish collagen?", "a": "Fish (marine) collagen is predominantly type I — exactly the type that makes up skin, bones and tendons. It has smaller molecules and higher absorption than porcine or bovine collagen. Our collagen is clinically tested."},
        {"q": "Do I need to take vitamin C separately?", "a": "No — vitamin C is already part of every Gelavit Pure® product. Without it, the body cannot build its own collagen from the amino acids you consume, so we treat it as a necessary part of the formula rather than an add-on."},
        {"q": "Is Gelavit suitable with lactose intolerance or diabetes?", "a": "Yes. The products contain no lactose. We use sucralose as the sweetener, which does not affect glycaemia or raise blood sugar levels, making it suitable for diabetics."},
        {"q": "How and when will my order arrive?", "a": "Orders received before 12:00 on a working day are dispatched the same day. Delivery within Slovakia usually takes 2–3 working days by post, or 24 hours by courier. Shipping is free on orders over €50."},
        {"q": "Can I return a product?", "a": "Yes, within 14 days of receipt without giving a reason — provided the goods are unused and in the original packaging. Details are in our terms and conditions."},
    ],

    "cta_h2": 'Start today. Your joints will <em>thank you</em>.',
    "cta_p": "One sachet a day. No E numbers, no preservatives, with vitamin C. Free shipping over €50.",

    "add_to_cart": "Add to cart", "bestseller": "Bestseller", "out_of_stock": "Sold out",
    "out_of_stock_long": "Currently sold out", "in_stock": "In stock — dispatched within 24 h",
    "notify_me": "Notify me when back in stock",
    "qty": "Quantity", "vat_incl": "VAT included", "related": "You might also like",
    "related_products": "Products from this article",
    "spec_composition": "Composition", "spec_dosage": "Dosage", "spec_pack": "Package", "spec_storage": "Storage",
    "pdp_perks": ["No E numbers, colourings or preservatives", "Vitamin C in every dose", "Dispatched within 24 hours", "Free shipping over €50"],

    "cart_h1": "Your cart", "cart_empty_h": "Your cart is empty",
    "cart_empty_p": "Add some products and come back — we'll keep them even if you close the page.",
    "continue_shopping": "Continue shopping", "summary": "Order summary",
    "subtotal": "Subtotal", "shipping": "Shipping", "total": "Total", "payment_fee": "Payment fee",
    "at_checkout": "at checkout", "to_checkout": "Go to checkout",
    "cart_note": "Prices include VAT. Shipping is calculated in the next step.",
    "edit_cart": "Edit cart", "remove": "Remove", "free": "Free",
    "freeLeft": "Add {x} more for free shipping.", "freeGot": "You've got free shipping!",

    "checkout_h1": "Checkout",
    "co_contact": "Contact details", "co_address": "Delivery address",
    "co_shipping": "Delivery method", "co_payment": "Payment method", "co_note": "Note and consents",
    "f_name": "Full name", "f_email": "E-mail", "f_phone": "Phone",
    "f_street": "Street and number", "f_zip": "Postcode", "f_city": "City", "f_country": "Country",
    "f_company": "Company (optional)", "f_other": "Other", "f_note": "Order note",
    "f_subject": "Subject", "f_message": "Message",
    "consent_terms": 'I agree to the <a href="{terms}">terms and conditions</a> and to the <a href="{privacy}">processing of personal data</a>.',
    "consent_privacy": 'I agree to the <a href="{privacy}">processing of personal data</a>.',
    "consent_news": "I want to receive news and offers by e-mail (unsubscribe any time).",
    "place_order": "Place order",
    "checkout_note": "Placing the order creates an obligation to pay. We will e-mail you the invoice and payment details.",
    "free_from_note": "Shipping is free on orders over €50.",
    "order_subject": "New order from gelavit.sk",
    "added": "Added to cart", "mailIntro": "Hello, I would like to order:",

    "thanks_h1": "Thank you for your order!",
    "thanks_p": "We have received your order. A confirmation with a summary and payment details will arrive in your inbox within minutes.",
    "thanks_next": "What happens next",
    "thanks_steps": [
        "An order confirmation will reach you by e-mail within minutes.",
        "If you chose bank transfer, we will send you the account number and reference.",
        "Orders received before 12:00 on a working day are dispatched the same day.",
        "Any questions? Write to <a href=\"mailto:info@gelavit.sk\">info@gelavit.sk</a> or call +421 915 178 349.",
    ],

    "about_eyebrow": "Our story", "about_h1": 'Let food be <em>thy medicine</em>',
    "about_role": "founder of the company",
    "about_values_eyebrow": "What we care about", "about_values_h2": "Three things we won't compromise on",
    "about_values": [
        {"h": "Clean composition", "p": "No E numbers, colourings or preservatives. If an ingredient has no function, it isn't there."},
        {"h": "Proven collagen", "p": "Clinically tested type I fish collagen with increased absorption — not the cheapest, but the most effective."},
        {"h": "A taste you can keep up", "p": "A course only works if you can stick to it. That's why we spent years on the flavours — pineapple, hazelnut, coconut, mango."},
    ],
    "about_history_eyebrow": "Company history", "about_history_h2": "Where we came from",
    "about_history": [
        {"y": "2015", "t": "29 Aug 2015 — Gelavit s. r. o. is founded."},
        {"y": "2016", "t": "Participation in exhibitions and direct sales. New distribution networks, online marketing and new products."},
        {"y": "2017", "t": "Cooperation with DuMax pharma s. r. o. Launch of the intense course in 28 individual sachets."},
        {"y": "2018", "t": "Business cooperation with new partners, active participation in exhibitions and lectures."},
        {"y": "today", "t": "GelaVit products are available in shops across Slovakia and directly in our e-shop."},
    ],

    "contact_eyebrow": "We're here for you", "contact_h1": "Contact and points of sale",
    "contact_lead": "Write to us, call us, or pick the products up in person at one of our points of sale.",
    "contact_form_h": "Write to us", "contact_billing": "Billing information",
    "contact_points": "Points of sale", "contact_subject": "Message from the gelavit.sk contact form",
    "send": "Send message", "open": "Open", "slovakia": "Slovakia", "reg": "Registration",

    "blog_eyebrow": "Magazine", "blog_h1": "On collagen, nutrition and movement",
    "blog_lead": "Articles about how collagen works, why vitamin C matters and what happens in the body when you keep to the course.",

    "hero_photo_alt": "Three Gelavit Pure packs on a wooden table with fresh fruit",
    "badge_collagen_alt": "Bioactive 97 % collagen with vitamin C",
    "science_alt": "Hydrolysed fish collagen in powder form",
    "band_alt": "The full GelaVit range — powders, the intense course, jelly and chocolate",
    "about_photo_alt": "Nina Bernardo, founder of Gelavit, at a trade show",
    "marquee": [
        "97 % bioactive collagen",
        "Vitamin C in every dose",
        "No E numbers or preservatives",
        "Made in Slovakia",
        "Clinically tested type I collagen",
        "Lactose free",
        "Suitable for diabetics",
        "Dispatched within 24 hours",
        "Free shipping over €50",
    ],

    "skip": 'Skip to content',
    "view": 'View',
    "scroll": 'Scroll',
    "showcase_eyebrow": 'Four flavours',
    "showcase_h2": 'One formula, <em>four</em> tastes.',
    "showcase_cta": 'Choose yours',

    "footer_blurb": "Natural joint nutrition with bioactive type I collagen. Developed and produced in Slovakia since 2015.",
    "footer_shop": "Shop", "footer_info": "Information", "footer_contact": "Contact",
    "newsletter_title": "Newsletter", "newsletter_cta": "Subscribe", "email": "Your e-mail",
    "footer_disclaimer": "Food supplements do not replace a varied diet and a healthy lifestyle.",
}

# ---------------------------------------------------------------- GERMAN ----
T["de"] = {
    "announce": 'Versandkostenfrei ab <strong>50 €</strong> · Versand innerhalb von 24 Stunden',
    "nav_label": "Hauptnavigation", "lang_label": "Sprache", "menu": "Menü", "close": "Schließen",
    "nav_home": "Startseite", "nav_products": "Produkte", "nav_about": "Über uns",
    "nav_blog": "Blog", "nav_contact": "Kontakt", "nav_cart": "Warenkorb",
    "nav_howto": "Wie bestelle ich", "nav_terms": "AGB", "nav_privacy": "Datenschutz",

    "hero_eyebrow": "Bioaktives Kollagen des Typs I",
    "hero_h1": 'Kollagen, das der Körper <em>wirklich</em> nutzt.',
    "hero_lead": "Gelavit Pure® enthält bis zu 97 % hydrolysiertes Fischkollagen mit Vitamin C. Ohne E-Nummern, ohne Farbstoffe, ohne Konservierungsmittel — seit 2015 in der Slowakei entwickelt.",
    "hero_cta": "Produkte ansehen", "hero_cta2": "Warum Kollagen?",
    "hero_for": "Für",
    "seal_ring": "97 % KOLLAGEN · OHNE E-NUMMERN · ",
    "hero_rotate": ["Gelenke", "Haut", "Haare", "Nägel", "Knochen", "Sehnen"],
    "hero_note": "Klinisch getestetes Kollagen mit erhöhter Absorption",
    "badge_collagen": "bioaktives<br>Kollagen", "badge_type": "5.000 mg Kollagen<br>pro Portion",

    "trust": ["Ohne E-Nummern", "Erstklassige Qualität", "Ohne Farb- & Konservierungsstoffe", "Versand in 24 h"],

    "problem_eyebrow": "Warum GelaVit",
    "problem_h2": 'Unsere Gelenke bemerken wir erst, wenn sie <em>wehtun</em>.',
    "problem_lead": "Wie wichtig die richtige Gelenkernährung ist, merken wir meist erst, wenn der Schmerz da ist. Auf einmal fühlen wir uns Jahrzehnte älter — der Körper verliert seine Flexibilität und die Freude an Bewegung ist weg.",
    "problems": [
        {"h": "Sie treiben aktiv Sport", "p": "Sehnen und Gelenke unter regelmäßiger Belastung brauchen Baumaterial, das eine normale Ernährung nicht in ausreichender Menge liefert."},
        {"h": "Ihre Arbeit ist körperlich", "p": "Langes Stehen, Heben und wiederholte Bewegung nutzen den Knorpel schneller ab, als der Körper ihn aufbauen kann."},
        {"h": "Sie verlieren Vitalität", "p": "Ab dreißig sinkt die eigene Kollagenbildung — zuerst sieht man es an der Haut, dann spürt man es in den Gelenken."},
    ],

    "shop_eyebrow": "Unsere Reihe", "shop_h2": 'Kollagen in einer Form, die zu Ihnen passt.',
    "shop_all": "Alle Produkte",
    "products_h1": "Alle GelaVit-Produkte",
    "products_lead": "Pulver, Intensivkuren, Getränke und Gelees — alle mit bioaktivem Kollagen des Typs I und Vitamin C.",

    "science_eyebrow": "Ein wenig Wissenschaft",
    "science_h2": 'Warum <em>Kollagen</em> unersetzlich ist',
    "science_lead": "Kollagen ist das wichtigste Strukturprotein des menschlichen Körpers — es macht fast ein Drittel aller Proteine aus. Am meisten enthalten die Stützgewebe: Knochen, Gelenke, Sehnen und Haut.",
    "science_points": [
        "Natives Kollagen wird nicht aufgenommen. Ein <strong>Hydrolysat</strong> enthält wasserlösliche Peptide, die der Körper über das Blut dorthin transportieren kann, wo sie gebraucht werden.",
        "Ohne <strong>Vitamin C</strong> hat die Einnahme von Kollagen praktisch keine Wirkung — deshalb ist es in jedem Produkt enthalten.",
        "Wir verwenden <strong>Fischkollagen des Typs I</strong> — klinisch getestet, mit höherer Absorption als Schweine- oder Rinderkollagen.",
        "Auch bei <strong>Laktoseintoleranz</strong> geeignet und — dank Sucralose — auch für Diabetiker.",
    ],
    "science_cta": "Den ganzen Artikel lesen",

    "stats_eyebrow": "Zahlen, die zählen", "stats_h2": "Eine Zusammensetzung ohne Kompromisse",
    "stats": [
        {"n": "97 %", "l": "bioaktives Kollagen"},
        {"n": "0", "l": "E-Nummern & Konservierungsstoffe"},
        {"n": "5 g", "l": "Tagesportion"},
        {"n": "2015", "l": "auf dem Markt seit"},
    ],

    "how_eyebrow": "So funktioniert es", "how_h2": "Drei Schritte, dreißig Sekunden am Tag",
    "step": "Schritt",
    "how_steps": [
        {"h": "Abmessen", "p": "1–2 Teelöffel Pulver (ca. 5 g) oder einfach ein Säckchen der Intensivkur öffnen."},
        {"h": "Anrühren", "p": "In 200 ml Wasser, Saft, Milch oder einem Smoothie. Löst sich sofort auf und klumpt nicht."},
        {"h": "Täglich trinken", "p": "Regelmäßigkeit ist entscheidend. Der Körper bringt das Kollagen dorthin, wo es am nötigsten ist."},
    ],

    "quotes_eyebrow": "Kundenerfahrungen", "quotes_h2": "Was Gelavit-Anwender sagen",
    "quotes": [
        {"q": "Nach meiner Knie-OP hat mir der Orthopäde Kollagen empfohlen. Von allem, was ich probiert habe, hat Gelavit den höchsten Gehalt und schmeckt nicht nach Medizin.", "a": "Martina K., Bratislava"},
        {"q": "Die Box nehme ich auf Geschäftsreisen mit — ein Säckchen in die Wasserflasche und fertig. Kein Wiegen, keine Sauerei.", "a": "Peter H., Košice"},
        {"q": "Nach drei Monaten sehe ich es am meisten an Nägeln und Haaren. Die Gelenke brauchen länger, aber die Morgensteifigkeit ist milder.", "a": "Zuzana M., Žilina"},
    ],

    "faq_h2": "Häufige Fragen",
    "faq": [
        {"q": "Wie lange dauert es, bis Kollagen wirkt?", "a": "Erste Veränderungen an Haut, Haaren und Nägeln zeigen sich meist nach 4–8 Wochen regelmäßiger Einnahme. Bei Gelenken und Sehnen dauert es länger — wir empfehlen eine Kur von mindestens 3 Monaten. Entscheidend ist die Regelmäßigkeit: eine ausgelassene Portion ändert nichts, ein Monat Pause schon."},
        {"q": "Warum Fischkollagen?", "a": "Fisch- bzw. Meereskollagen ist überwiegend Typ I — genau der Typ, aus dem Haut, Knochen und Sehnen bestehen. Es hat kleinere Moleküle und eine höhere Absorption als Schweine- oder Rinderkollagen. Unser Kollagen ist klinisch getestet."},
        {"q": "Muss ich Vitamin C separat einnehmen?", "a": "Nein — Vitamin C ist bereits Bestandteil jedes Gelavit Pure® Produkts. Ohne es kann der Körper aus den aufgenommenen Aminosäuren kein eigenes Kollagen bilden, deshalb ist es fester Bestandteil der Rezeptur."},
        {"q": "Ist Gelavit bei Laktoseintoleranz oder Diabetes geeignet?", "a": "Ja. Die Produkte enthalten keine Laktose. Als Süßungsmittel verwenden wir Sucralose, die den Blutzuckerspiegel nicht beeinflusst und daher auch für Diabetiker geeignet ist."},
        {"q": "Wie und wann kommt meine Bestellung an?", "a": "Bestellungen, die an einem Werktag bis 12:00 Uhr eingehen, versenden wir am selben Tag. Die Lieferung dauert per Post in der Regel 2–3 Werktage, per Kurier 24 Stunden. Ab 50 € ist der Versand kostenlos."},
        {"q": "Kann ich ein Produkt zurückgeben?", "a": "Ja, innerhalb von 14 Tagen nach Erhalt ohne Angabe von Gründen — sofern die Ware unbenutzt und in der Originalverpackung ist. Details finden Sie in unseren AGB."},
    ],

    "cta_h2": 'Beginnen Sie heute. Ihre Gelenke werden es <em>danken</em>.',
    "cta_p": "Ein Säckchen täglich. Ohne E-Nummern, ohne Konservierungsstoffe, mit Vitamin C. Versandkostenfrei ab 50 €.",

    "add_to_cart": "In den Warenkorb", "bestseller": "Bestseller", "out_of_stock": "Ausverkauft",
    "out_of_stock_long": "Derzeit ausverkauft", "in_stock": "Auf Lager — Versand in 24 h",
    "notify_me": "Benachrichtigen, wenn wieder da",
    "qty": "Menge", "vat_incl": "inkl. MwSt.", "related": "Könnte Ihnen gefallen",
    "related_products": "Produkte zum Artikel",
    "spec_composition": "Zusammensetzung", "spec_dosage": "Dosierung", "spec_pack": "Packung", "spec_storage": "Lagerung",
    "pdp_perks": ["Ohne E-Nummern, Farb- und Konservierungsstoffe", "Vitamin C in jeder Portion", "Versand innerhalb von 24 Stunden", "Versandkostenfrei ab 50 €"],

    "cart_h1": "Ihr Warenkorb", "cart_empty_h": "Ihr Warenkorb ist leer",
    "cart_empty_p": "Legen Sie Produkte hinein und kommen Sie zurück — wir behalten sie, auch wenn Sie die Seite schließen.",
    "continue_shopping": "Weiter einkaufen", "summary": "Bestellübersicht",
    "subtotal": "Zwischensumme", "shipping": "Versand", "total": "Gesamt", "payment_fee": "Zahlungsgebühr",
    "at_checkout": "an der Kasse", "to_checkout": "Zur Kasse",
    "cart_note": "Preise inkl. MwSt. Der Versand wird im nächsten Schritt berechnet.",
    "edit_cart": "Warenkorb bearbeiten", "remove": "Entfernen", "free": "Kostenlos",
    "freeLeft": "Noch {x} bis zum kostenlosen Versand.", "freeGot": "Sie haben kostenlosen Versand!",

    "checkout_h1": "Kasse",
    "co_contact": "Kontaktdaten", "co_address": "Lieferadresse",
    "co_shipping": "Versandart", "co_payment": "Zahlungsart", "co_note": "Anmerkung und Zustimmungen",
    "f_name": "Vor- und Nachname", "f_email": "E-Mail", "f_phone": "Telefon",
    "f_street": "Straße und Nummer", "f_zip": "PLZ", "f_city": "Stadt", "f_country": "Land",
    "f_company": "Firma (optional)", "f_other": "Andere", "f_note": "Anmerkung zur Bestellung",
    "f_subject": "Betreff", "f_message": "Nachricht",
    "consent_terms": 'Ich stimme den <a href="{terms}">AGB</a> und der <a href="{privacy}">Verarbeitung personenbezogener Daten</a> zu.',
    "consent_privacy": 'Ich stimme der <a href="{privacy}">Verarbeitung personenbezogener Daten</a> zu.',
    "consent_news": "Ich möchte Neuigkeiten und Angebote per E-Mail erhalten (jederzeit abbestellbar).",
    "place_order": "Bestellung absenden",
    "checkout_note": "Mit dem Absenden der Bestellung entsteht eine Zahlungsverpflichtung. Rechnung und Zahlungsdaten senden wir per E-Mail.",
    "free_from_note": "Ab einem Bestellwert von 50 € ist der Versand kostenlos.",
    "order_subject": "Neue Bestellung von gelavit.sk",
    "added": "In den Warenkorb gelegt", "mailIntro": "Guten Tag, ich möchte gerne bestellen:",

    "thanks_h1": "Vielen Dank für Ihre Bestellung!",
    "thanks_p": "Wir haben Ihre Bestellung erhalten. In wenigen Minuten erhalten Sie eine Bestätigung mit Übersicht und Zahlungsdaten per E-Mail.",
    "thanks_next": "Wie es weitergeht",
    "thanks_steps": [
        "Die Bestellbestätigung erreicht Sie in wenigen Minuten per E-Mail.",
        "Bei Zahlung per Überweisung senden wir Ihnen Kontonummer und Verwendungszweck.",
        "Bestellungen, die werktags bis 12:00 Uhr eingehen, versenden wir am selben Tag.",
        "Fragen? Schreiben Sie an <a href=\"mailto:info@gelavit.sk\">info@gelavit.sk</a> oder rufen Sie +421 915 178 349 an.",
    ],

    "about_eyebrow": "Unsere Geschichte", "about_h1": 'Nahrung soll deine <em>Medizin</em> sein',
    "about_role": "Gründerin der Gesellschaft",
    "about_values_eyebrow": "Worauf es uns ankommt", "about_values_h2": "Drei Dinge, bei denen wir keine Abstriche machen",
    "about_values": [
        {"h": "Saubere Rezeptur", "p": "Keine E-Nummern, Farb- oder Konservierungsstoffe. Was keine Funktion hat, ist nicht drin."},
        {"h": "Bewährtes Kollagen", "p": "Klinisch getestetes Fischkollagen des Typs I mit erhöhter Absorption — nicht das billigste, aber das wirksamste."},
        {"h": "Ein Geschmack zum Durchhalten", "p": "Eine Kur wirkt nur, wenn man sie durchhält. Deshalb haben wir jahrelang an den Sorten gefeilt — Ananas, Haselnuss, Kokos, Mango."},
    ],
    "about_history_eyebrow": "Geschichte der Gesellschaft", "about_history_h2": "Woher wir kommen",
    "about_history": [
        {"y": "2015", "t": "29. 8. 2015 — Gründung der Gesellschaft Gelavit s. r. o."},
        {"y": "2016", "t": "Teilnahme an Ausstellungen und Direktverkauf. Neue Vertriebsnetze, Online-Marketing und neue Produkte."},
        {"y": "2017", "t": "Zusammenarbeit mit DuMax pharma s. r. o. Einführung der Intensivkur in 28 Einzelsäckchen."},
        {"y": "2018", "t": "Geschäftskooperation mit neuen Partnern, aktive Teilnahme an Ausstellungen und Vorträgen."},
        {"y": "heute", "t": "GelaVit-Produkte sind in Geschäften in der ganzen Slowakei und direkt in unserem Online-Shop erhältlich."},
    ],

    "contact_eyebrow": "Wir sind für Sie da", "contact_h1": "Kontakt und Verkaufsstellen",
    "contact_lead": "Schreiben Sie uns, rufen Sie an oder holen Sie die Produkte persönlich an einer unserer Verkaufsstellen ab.",
    "contact_form_h": "Schreiben Sie uns", "contact_billing": "Rechnungsdaten",
    "contact_points": "Verkaufsstellen", "contact_subject": "Nachricht vom Kontaktformular gelavit.sk",
    "send": "Nachricht senden", "open": "Geöffnet", "slovakia": "Slowakei", "reg": "Registrierung",

    "blog_eyebrow": "Magazin", "blog_h1": "Über Kollagen, Ernährung und Bewegung",
    "blog_lead": "Artikel darüber, wie Kollagen wirkt, warum Vitamin C wichtig ist und was im Körper passiert, wenn Sie die Kur durchhalten.",

    "hero_photo_alt": "Drei Gelavit-Pure-Packungen auf einem Holztisch mit frischem Obst",
    "badge_collagen_alt": "Bioaktives 97 % Kollagen mit Vitamin C",
    "science_alt": "Hydrolysiertes Fischkollagen in Pulverform",
    "band_alt": "Die gesamte GelaVit-Reihe — Pulver, Intensivkur, Gelee und Schokolade",
    "about_photo_alt": "Nina Bernardo, Gründerin von Gelavit, auf einer Messe",
    "marquee": [
        "97 % bioaktives Kollagen",
        "Vitamin C in jeder Portion",
        "Ohne E-Nummern und Konservierungsstoffe",
        "Hergestellt in der Slowakei",
        "Klinisch getestetes Kollagen Typ I",
        "Laktosefrei",
        "Auch für Diabetiker geeignet",
        "Versand innerhalb von 24 Stunden",
        "Versandkostenfrei ab 50 €",
    ],

    "skip": 'Zum Inhalt springen',
    "view": 'Ansehen',
    "scroll": 'Scrollen',
    "showcase_eyebrow": 'Vier Geschmacksrichtungen',
    "showcase_h2": 'Eine Rezeptur, <em>vier</em> Geschmäcker.',
    "showcase_cta": 'Wählen Sie',

    "footer_blurb": "Natürliche Gelenknahrung mit bioaktivem Kollagen des Typs I. Seit 2015 in der Slowakei entwickelt und hergestellt.",
    "footer_shop": "Shop", "footer_info": "Informationen", "footer_contact": "Kontakt",
    "newsletter_title": "Newsletter", "newsletter_cta": "Abonnieren", "email": "Ihre E-Mail",
    "footer_disclaimer": "Nahrungsergänzungsmittel ersetzen keine abwechslungsreiche Ernährung und gesunde Lebensweise.",
}

# ------------------------------------------------------------ predajne ----
POINTS = [
    {"name": "Masážny raj", "addr": "Pajštúnska ulica, Bratislava-Petržalka",
     "note": {"sk": "Odber po telefonickom kontakte: 0918 237 878", "en": "Pickup after phone contact: 0918 237 878", "de": "Abholung nach telefonischer Absprache: 0918 237 878"},
     "hours": "Po–Pia 10:00–19:00", "web": "http://www.masaznyraj.sk"},
    {"name": "Namaste india", "addr": "Škultétyho 1, 831 03 Bratislava-Nové Mesto",
     "note": {"sk": "Dom techniky, suterén · +421 911 766 530", "en": "Dom techniky, basement · +421 911 766 530", "de": "Dom techniky, Untergeschoss · +421 911 766 530"},
     "hours": "Po–Ne 10:00–21:00", "web": "http://www.namasteindia.eu"},
    {"name": "Namaste india — Zlaté piesky", "addr": "Cesta na Senec A/2, 821 04 Bratislava",
     "note": {"sk": "+421 911 766 510", "en": "+421 911 766 510", "de": "+421 911 766 510"},
     "hours": "Po–Ne 10:00–21:00", "web": "http://www.exotickepotraviny.sk"},
    {"name": "UNIMAR trade s. r. o.", "addr": "Triblavinská 4529/46, 900 25 Chorvátsky Grob",
     "note": {"sk": "+421 2 459 852 80", "en": "+421 2 459 852 80", "de": "+421 2 459 852 80"},
     "hours": "Po–Pia 7:30–16:00", "web": "http://www.unimartrade.sk"},
    {"name": "Ščerbo Šport Klub", "addr": "Čermeľská cesta 3449/1, 040 01 Košice",
     "note": {"sk": "Budova Vitalita · +421 905 307 262", "en": "Vitalita building · +421 905 307 262", "de": "Gebäude Vitalita · +421 905 307 262"},
     "hours": "Po–Pia 8:00–18:00", "web": "https://www.scerbosport.sk"},
]
