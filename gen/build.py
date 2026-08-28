# -*- coding: utf-8 -*-
"""
GelaVit — statický generátor e-shopu.
Spustenie:  python3 gen/build.py
Výstup:     site/
"""
import json, os, re, shutil, pathlib, datetime, html
from jinja2 import Environment, FileSystemLoader, select_autoescape
from i18n import T, URLS, POINTS
import images, content

ROOT = pathlib.Path(__file__).resolve().parent.parent
GEN = ROOT / "gen"
SITE = ROOT / "site"
SITE_URL = "https://gelavit.sk"
YEAR = 2026
LANGS = ["sk", "en", "de"]
DIR = {"sk": "", "en": "en/", "de": "de/"}

# Kam sa odosielajú formuláre. Zmeň na svoj Formspree / FormSubmit endpoint.
ORDER_ACTION = "https://formsubmit.co/info@gelavit.sk"
CONTACT_ACTION = "https://formsubmit.co/info@gelavit.sk"
NEWSLETTER_ACTION = "https://formsubmit.co/info@gelavit.sk"

data = json.loads((GEN / "products.json").read_text())
SHIPPING = data["shipping"]
PAYMENT = data["payment"]

env = Environment(
    loader=FileSystemLoader(str(GEN / "templates")),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True, lstrip_blocks=True,
)

MONTHS = {
    "sk": ["januára", "februára", "marca", "apríla", "mája", "júna", "júla", "augusta", "septembra", "októbra", "novembra", "decembra"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
}


# text-bezpečné varianty farieb kvapky (kontrast na bielej)
HUE_TEXT = {
    "#C9DC50": "#7E9612",
    "#F04E4A": "#E03430",
    "#84B939": "#5F8A26",
    "#5FBEEC": "#1B8FC8",
    "#0086B5": "#006C92",
}


def money(v, lang):
    s = f"{v:,.2f}"
    if lang == "sk" or lang == "de":
        s = s.replace(",", " ").replace(".", ",")
        return f"{s} €"
    return f"€{s}"


def fmt_date(iso, lang):
    y, m, d = [int(x) for x in iso.split("-")]
    if lang == "en":
        return f"{d} {MONTHS['en'][m-1]} {y}"
    return f"{d}. {MONTHS[lang][m-1]} {y}"


def products_for(lang):
    out = []
    for p in data["products"]:
        loc = p[lang]
        out.append({
            "slug": p["slug"], "sku": p["sku"], "price": p["price"], "stock": p["stock"],
            "featured": p["featured"], "img": p["img"], "size_g": p["size_g"],
            "hue": p.get("hue", "#F04E4A"), "hue_t": HUE_TEXT.get(p.get("hue", "#F04E4A"), "#E03430"),
            "price_fmt": money(p["price"], lang), **loc,
        })
    return out


def catalog_json(lang, prods):
    return json.dumps({p["slug"]: {
        "name": p["name"], "price": p["price"], "img": p["img"], "pack": p["pack"], "sku": p["sku"],
    } for p in prods}, ensure_ascii=False)


def i18n_json(lang):
    t = T[lang]
    keys = ["added", "remove", "qty", "free", "freeLeft", "freeGot", "subtotal", "shipping",
            "payment_fee", "total", "mailIntro"]
    d = {k: t.get(k, k) for k in keys}
    d["payment"] = t["co_payment"]
    d["orderSubject"] = t["order_subject"]
    return json.dumps(d, ensure_ascii=False)


def alternates_for(key, slug=None):
    """Vráti { lang: '/cesta.html' } pre hreflang a prepínač jazykov."""
    out = {}
    for l in LANGS:
        u = URLS[l]
        if key == "product":
            path = f"{u['product_prefix']}{slug}.html"
        elif key == "post":
            path = f"{u['blog_prefix']}{slug}.html"
        else:
            path = u[key]
        out[l] = "/" + DIR[l] + ("" if path == "index.html" and DIR[l] == "" else path)
        if path == "index.html":
            out[l] = "/" + DIR[l]
    return out


def render(lang, tpl, outpath, **ctx):
    prods = products_for(lang)
    t = dict(T[lang])
    u = URLS[lang]
    base = "../" if DIR[lang] else ""
    # doplniť odkazy do súhlasov
    for k in ("consent_terms", "consent_privacy"):
        t[k] = t[k].replace("{terms}", u["terms"]).replace("{privacy}", u["privacy"])

    cfg = {
        "freeFrom": SHIPPING["free_from"],
        "cartUrl": u["cart"], "thanksUrl": u["thanks"],
        "orderEndpoint": ORDER_ACTION, "orderEmail": "info@gelavit.sk",
    }
    full = dict(
        lang=lang, t=t, u=u, base=base, products=prods,
        featured=[p for p in prods if p["featured"]][:4],
        site_url=SITE_URL, site_root=("../" if DIR[lang] else "") or "",
        year=YEAR, config_json=json.dumps(cfg, ensure_ascii=False),
        catalog_json=catalog_json(lang, prods), i18n_json=i18n_json(lang),
        order_action=ORDER_ACTION, contact_action=CONTACT_ACTION,
        newsletter_action=NEWSLETTER_ACTION, schema=None, page="", intro=None,
    )
    full.update(ctx)
    # relatívne odkazy pre prepínač jazykov (funguje aj z file:// a z podpriečinka)
    import posixpath
    curdir = DIR[lang] or "."
    sw = {}
    for l, href in full["alternates"].items():
        target = href.lstrip("/") or "index.html"
        if target.endswith("/"):
            target += "index.html"
        sw[l] = posixpath.relpath(target, curdir if curdir != "." else ".")
    full["switch"] = sw
    full["site_root"] = ""
    out = SITE / DIR[lang] / outpath
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(env.get_template(tpl).render(**full), encoding="utf-8")
    return "/" + DIR[lang] + ("" if outpath == "index.html" else outpath)


# ------------------------------------------------------------------ schema --
def org_schema():
    return json.dumps({
        "@context": "https://schema.org", "@type": "Organization",
        "name": "Gelavit s. r. o.", "url": SITE_URL,
        "logo": SITE_URL + "/assets/img/logo.svg",
        "email": "info@gelavit.sk", "telephone": "+421915178349",
        "address": {"@type": "PostalAddress", "streetAddress": "Kopčianska 8",
                    "postalCode": "851 01", "addressLocality": "Bratislava", "addressCountry": "SK"},
        "vatID": "SK2120117241", "taxID": "2120117241",
        "sameAs": ["https://www.facebook.com/gelavit", "https://www.instagram.com/gelavit"],
    }, ensure_ascii=False)


def product_schema(p, lang, url):
    return json.dumps({
        "@context": "https://schema.org", "@type": "Product",
        "name": p["name"], "description": p["short"], "sku": p["sku"], "gtin13": p["sku"],
        "brand": {"@type": "Brand", "name": "GelaVit"},
        "image": SITE_URL + "/assets/img/products/" + p["img"] + "-800.png",
        "offers": {
            "@type": "Offer", "url": SITE_URL + url, "priceCurrency": "EUR",
            "price": f'{p["price"]:.2f}',
            "availability": "https://schema.org/InStock" if p["stock"] else "https://schema.org/OutOfStock",
            "seller": {"@type": "Organization", "name": "Gelavit s. r. o."},
        },
    }, ensure_ascii=False)


def faq_schema(lang):
    return json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": f["q"],
                        "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", f["a"])}}
                       for f in T[lang]["faq"]],
    }, ensure_ascii=False)


# -------------------------------------------------------------------- build --
def build():
    # assets
    images.build()
    content.write_static_assets(SITE)

    urls = []

    for lang in LANGS:
        t = T[lang]
        u = URLS[lang]
        prods = products_for(lang)
        posts = content.posts_for(lang)
        for po in posts:
            po["date_fmt"] = fmt_date(po["date"], lang)

        brand = "GelaVit"
        TINT = {"gelavit-pure-ananas": "#FBEBD2", "gelavit-pure-vitamin-c": "#FBE3D3",
                "gelavit-pure-ananas-box": "#E4EFE2", "gelavit-pure-lieskovy-orech": "#EFE4D6",
                "gelavit-pure-kokosove-mlieko": "#F3ECE2", "gelavit-napoj-mango": "#FCEBD0",
                "gelavit-zele-mango": "#FBE9CF", "kolagenova-cokolada-kokos": "#EDE3DA"}
        show_slugs = ["gelavit-pure-ananas", "gelavit-pure-vitamin-c",
                      "gelavit-pure-ananas-box", "gelavit-pure-lieskovy-orech"]
        by_slug = {p["slug"]: p for p in prods}
        showcase = []
        for sl in show_slugs:
            it = dict(by_slug[sl])
            raw = next(x for x in data["products"] if x["slug"] == sl)
            it["tint"] = TINT.get(sl, "#F1E9DC")
            it["badge"] = (f'{raw["collagen"]:g} % {t["stats"][0]["l"]}'
                           if raw["collagen"] else t["hero_eyebrow"])
            showcase.append(it)
        # --- home
        urls.append((render(lang, "index.html", u["home"],
            page="home", canonical=alternates_for("home")[lang],
            alternates=alternates_for("home"),
            title=f'{brand} — {t["hero_eyebrow"]} | {t["nav_products"]}' if lang != "sk"
                  else "GelaVit Pure® — bioaktívny kolagén typu I s vitamínom C",
            description=t["hero_lead"][:158],
            hero_product=prods[0], showcase=showcase,
            schema=org_schema() + "</script><script type=\"application/ld+json\">" + faq_schema(lang),
        ), 1.0))

        # --- produkty
        urls.append((render(lang, "products.html", u["products"],
            page="products", canonical=alternates_for("products")[lang],
            alternates=alternates_for("products"),
            title=f'{t["products_h1"]} | {brand}', description=t["products_lead"][:158],
            schema=faq_schema(lang),
        ), 0.9))

        # --- detail produktov
        for p in prods:
            url = "/" + DIR[lang] + u["product_prefix"] + p["slug"] + ".html"
            rel = [x for x in prods if x["slug"] != p["slug"] and x["stock"]][:3]
            urls.append((render(lang, "product.html", f'{u["product_prefix"]}{p["slug"]}.html',
                page="products", canonical=url, alternates=alternates_for("product", p["slug"]),
                title=f'{p["name"]} | {brand}', description=p["short"][:158],
                p=p, related=rel, og_type="product",
                schema=product_schema(p, lang, url),
            ), 0.8))

        # --- košík / pokladňa / ďakujeme
        ship = [{"id": s["id"], "price": s["price"], "price_fmt": money(s["price"], lang) if s["price"] else t["free"],
                 "label": s[lang], "note": ""} for s in SHIPPING["methods"]]
        pay = [{"id": m["id"], "fee": m["fee"], "fee_fmt": money(m["fee"], lang) if m["fee"] else t["free"],
                "label": m[lang], "note": ""} for m in PAYMENT]

        render(lang, "cart.html", u["cart"], page="cart", canonical=alternates_for("cart")[lang],
               alternates=alternates_for("cart"), title=f'{t["cart_h1"]} | {brand}',
               description=t["cart_note"])
        render(lang, "checkout.html", u["checkout"], page="cart", canonical=alternates_for("checkout")[lang],
               alternates=alternates_for("checkout"), title=f'{t["checkout_h1"]} | {brand}',
               description=t["checkout_note"], shipping={"methods": ship}, payment=pay)
        render(lang, "thanks.html", u["thanks"], page="", canonical=alternates_for("thanks")[lang],
               alternates=alternates_for("thanks"), title=f'{t["thanks_h1"]} | {brand}',
               description=t["thanks_p"])

        # --- o nás
        urls.append((render(lang, "about.html", u["about"], page="about",
            canonical=alternates_for("about")[lang], alternates=alternates_for("about"),
            title=f'{t["nav_about"]} | {brand}', description=re.sub("<[^>]+>", "", t["about_story"])[:158],
        ), 0.7))

        # --- kontakt
        pts = [{"name": p["name"], "addr": p["addr"], "note": p["note"][lang],
                "hours": p["hours"], "web": p["web"]} for p in POINTS]
        urls.append((render(lang, "contact.html", u["contact"], page="contact",
            canonical=alternates_for("contact")[lang], alternates=alternates_for("contact"),
            title=f'{t["contact_h1"]} | {brand}', description=t["contact_lead"][:158], points=pts,
        ), 0.7))

        # --- blog
        urls.append((render(lang, "blog.html", u["blog"], page="blog",
            canonical=alternates_for("blog")[lang], alternates=alternates_for("blog"),
            title=f'{t["blog_h1"]} | {brand}', description=t["blog_lead"][:158], posts=posts,
        ), 0.7))
        for po in posts:
            urls.append((render(lang, "post.html", f'{u["blog_prefix"]}{po["slug"]}.html',
                page="blog", canonical="/" + DIR[lang] + u["blog_prefix"] + po["slug"] + ".html",
                alternates=alternates_for("post", po["slug"]),
                title=f'{po["title"]} | {brand}', description=po["excerpt"][:158],
                post=po, og_type="article",
            ), 0.6))

        # --- statické stránky
        for key, src in (("howto", "howto"), ("terms", "terms"), ("privacy", "privacy")):
            body, heading = content.legal(key, lang, T, URLS, DIR)
            urls.append((render(lang, "page.html", u[key], page="",
                canonical=alternates_for(key)[lang], alternates=alternates_for(key),
                title=f'{heading} | {brand}', description=heading + " — GelaVit",
                heading=heading, body=body,
            ), 0.3))

    # 404
    for lang in LANGS:
        render(lang, "page.html", "404.html", page="",
               canonical="/404.html", alternates=alternates_for("home"),
               title={"sk": "Stránka sa nenašla", "en": "Page not found", "de": "Seite nicht gefunden"}[lang] + " | GelaVit",
               description="404",
               heading={"sk": "Stránka sa nenašla", "en": "Page not found", "de": "Seite nicht gefunden"}[lang],
               body={"sk": '<p>Táto stránka neexistuje alebo bola presunutá. Skúste <a href="produkty.html">produkty</a>, <a href="blog.html">blog</a> alebo <a href="kontakt.html">kontakt</a>.</p>',
                     "en": '<p>This page does not exist or has moved. Try <a href="products.html">products</a>, the <a href="blog.html">blog</a> or <a href="contact.html">contact</a>.</p>',
                     "de": '<p>Diese Seite existiert nicht oder wurde verschoben. Versuchen Sie <a href="produkte.html">Produkte</a>, den <a href="blog.html">Blog</a> oder <a href="kontakt.html">Kontakt</a>.</p>'}[lang])

    content.write_seo(SITE, SITE_URL, urls)
    print(f"✓ hotovo — {len(list(SITE.rglob('*.html')))} HTML súborov")


if __name__ == "__main__":
    build()
