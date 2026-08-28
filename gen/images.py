# -*- coding: utf-8 -*-
"""
Spracovanie obrázkov: orezanie okrajov, jednotné štvorcové packshoty,
zmenšenie a export do WebP + PNG/JPG fallbacku.

Zdroj:  gen/src-images/
Výstup: site/assets/img/
"""
import pathlib, re
from PIL import Image, ImageChops, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "gen" / "src-images"
OUT = ROOT / "site" / "assets" / "img"

CREAM = (241, 242, 242)      # --bg-alt = #F1F2F2, svetlá šedá z loga
WHITE = (255, 255, 255)


# --------------------------------------------------------------- pomocné ----
def to_rgba(im):
    if im.mode == "P":
        im = im.convert("RGBA")
    elif im.mode != "RGBA":
        im = im.convert("RGBA")
    return im


def trim(im, bg_tol=14):
    """Odreže jednofarebný okraj (biely/šedý/priehľadný)."""
    im = to_rgba(im)
    alpha = im.getchannel("A")
    if alpha.getextrema()[0] < 250:                      # má priehľadnosť
        box = alpha.point(lambda a: 255 if a > 8 else 0).getbbox()
    else:                                                 # jednofarebné pozadie
        rgb = im.convert("RGB")
        bg = Image.new("RGB", rgb.size, rgb.getpixel((0, 0)))
        diff = ImageChops.difference(rgb, bg).convert("L")
        box = diff.point(lambda v: 255 if v > bg_tol else 0).getbbox()
    return im.crop(box) if box else im



def square(im, size, bg, pad=0.075):
    """Vloží obrázok doprostred štvorca s okrajom a daným pozadím."""
    im = to_rgba(im)
    inner = int(size * (1 - 2 * pad))
    im.thumbnail((inner, inner), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), bg + (255,))
    canvas.alpha_composite(im, ((size - im.size[0]) // 2, (size - im.size[1]) // 2))
    return canvas


def shadow(im, blur=18, offset=14, opacity=54):
    """Pridá jemný tieň pod objekt (len ak má alfa kanál)."""
    im = to_rgba(im)
    a = im.getchannel("A")
    if a.getextrema()[0] >= 250:
        return im
    sh = Image.new("RGBA", im.size, (22, 40, 58, 0))
    mask = a.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * opacity / 255))
    sh.putalpha(mask)
    base = Image.new("RGBA", im.size, (0, 0, 0, 0))
    base.alpha_composite(sh, (0, offset))
    base.alpha_composite(im)
    return base


def save(im, stem, widths, fmt="png", quality=82, bg=None):
    """Uloží WebP + fallback v každej šírke. Vráti zoznam šírok."""
    stem.parent.mkdir(parents=True, exist_ok=True)
    for w in widths:
        h = round(im.size[1] * w / im.size[0])
        r = im.resize((w, h), Image.LANCZOS)
        r.save(f"{stem}-{w}.webp", "WEBP", quality=quality, method=6)
        if fmt == "png":
            r.save(f"{stem}-{w}.png", "PNG", optimize=True)
        else:
            flat = Image.new("RGB", r.size, bg or WHITE)
            flat.paste(r, mask=r.getchannel("A") if r.mode == "RGBA" else None)
            flat.save(f"{stem}-{w}.jpg", "JPEG", quality=quality, optimize=True, progressive=True)
    return widths


# ---------------------------------------------------------------- kroky -----
PRODUCT_WIDTHS = [400, 800]
LIFESTYLE_WIDTHS = [800, 1600]
BADGE_WIDTHS = [160, 320]


def products():
    """Dve sady: na krémovom pozadí (karty) a s priehľadným pozadím (scroll scéna)."""
    d = OUT / "products"
    n = 0
    for f in sorted((SRC / "products").glob("*.png")):
        base = trim(Image.open(f))
        # Swiss Grid: ploché, bez tieňa, orezané do bunky mriežky
        save(square(base, 1000, CREAM, pad=0.06), d / f.stem, PRODUCT_WIDTHS, fmt="png")
        # priehľadná verzia pre hero scénu a showcase.
        # Packshoty sú na bielom ateliérovom pozadí; automatické vyrezanie
        # skla fľaše a hrdla vrecka nedávalo čistý výsledok, preto ich
        # nevyrezávame a v scénach ich staviame na bielu plochu — farbu nesie
        # prstenec okolo produktu, nie plný disk pod ním.
        t = to_rgba(base)
        w = max(t.size)
        canvas = Image.new("RGBA", (w, w), (0, 0, 0, 0))
        canvas.alpha_composite(t, ((w - t.size[0]) // 2, (w - t.size[1]) // 2))
        save(canvas, d / (f.stem + "-tr"), [500, 1000], fmt="png")
        n += 1
    return n


def lifestyle():
    d = OUT / "photo"
    n = 0
    for f in sorted((SRC / "lifestyle").glob("*.*")):
        im = Image.open(f).convert("RGB")
        if im.size[0] > 1600:
            im = im.resize((1600, round(im.size[1] * 1600 / im.size[0])), Image.LANCZOS)
        widths = [800] + ([1600] if im.size[0] >= 1200 else [])
        save(im.convert("RGBA"), d / f.stem, widths, fmt="jpg", quality=80)
        n += 1
    return n


def badges():
    d = OUT / "badge"
    n = 0
    for f in sorted((SRC / "badges").glob("*.png")):
        im = square(trim(Image.open(f)), 640, WHITE, pad=0.01)
        # priehľadné pozadie namiesto bieleho
        im = to_rgba(trim(Image.open(f)))
        w = max(im.size)
        canvas = Image.new("RGBA", (w, w), (0, 0, 0, 0))
        canvas.alpha_composite(im, ((w - im.size[0]) // 2, (w - im.size[1]) // 2))
        save(canvas, d / f.stem, BADGE_WIDTHS, fmt="png")
        n += 1
    return n


NAVY = "rgb(16.078431%,25.490196%,38.823529%)"


def brand():
    OUT.mkdir(parents=True, exist_ok=True)
    svg = (SRC / "brand" / "logo.svg").read_text()
    (OUT / "logo.svg").write_text(svg)
    # svetlá verzia pre tmavú pätičku: navy -> krémová
    (OUT / "logo-light.svg").write_text(svg.replace(NAVY, "rgb(98%,97.2%,95.3%)"))

    # favicon z farebnej kvapky v logu (orežeme ľavú časť loga)
    im = trim(Image.open(SRC / "brand" / "favicon-src.png"))
    im = square(im, 256, WHITE, pad=0.08)
    im.save(OUT / "favicon.png", "PNG", optimize=True)

    # darčekový poukaz
    dp = square(trim(Image.open(SRC / "brand" / "darcekovy-poukaz.png")), 1000, CREAM, pad=0.06)
    save(dp, OUT / "products" / "darcekovy-poukaz", PRODUCT_WIDTHS, fmt="png")


def og_image():
    """Open Graph 1200x630 z hero fotky + logo."""
    photo = Image.open(SRC / "lifestyle" / "hero-trio.jpg").convert("RGB")
    w, h = photo.size
    target = 1200 / 630
    if w / h > target:
        nw = int(h * target); photo = photo.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
    else:
        nh = int(w / target); photo = photo.crop((0, (h - nh) // 2, w, (h + nh) // 2))
    photo = photo.resize((1200, 630), Image.LANCZOS).convert("RGB")
    photo.save(OUT / "og.jpg", "JPEG", quality=86, optimize=True)


def build():
    brand()
    p, l, b = products(), lifestyle(), badges()
    og_image()
    print(f"obrázky: {p} produktov, {l} fotiek, {b} odznakov")


if __name__ == "__main__":
    build()
