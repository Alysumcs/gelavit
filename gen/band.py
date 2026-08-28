# -*- coding: utf-8 -*-
"""
Oprava ateliérovej fotky celej rady.

Pôvodná fotka mala šesť produktov, z toho DVE rovnaké vrecká Ananás,
a chýbal Ananás Box. Fotku neprekresľujeme — je to reálny ateliérový záber.
Opravíme len to, čo je na nej zle:

1. šieste (duplicitné) vrecko vygumujeme klonovaním čistého pozadia
   (stena aj podlaha sú vodorovne takmer rovnaké, takže je to neviditeľné),
2. na jeho miesto položíme reálny packshot Ananás Boxu — vyrezaný,
   zladený so svetlom fotky a s vlastným mäkkým tieňom.

Vstup:  gen/src-images/_raw/rada-siroka.jpg   (nedotknutý originál)
Výstup: gen/src-images/lifestyle/rada-siroka.jpg
"""
import pathlib
import numpy as np
from scipy import ndimage
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "gen" / "src-images"
PRODUCTS = SRC / "products"

DUP = (1318, 1584)     # vodorovný rozsah duplicitného vrecka (aj s tieňom)
CLEAN = (1292, 1316)   # overene čistý pás pozadia medzi vreckami


def erase(im, x0, x1, src_x0, src_x1):
    """Vyplní pás [x0,x1) hladkým pozadím.

    Pozadie je vodorovne takmer rovnaké, preto z čistého pásu spravíme
    jeden priemerný stĺpec a ten roztiahneme — nevzniknú žiadne švy
    ani opakujúci sa vzor.
    """
    strip = np.asarray(im.crop((src_x0, 0, src_x1, im.size[1])), dtype=np.float32)
    col = strip.mean(axis=1, keepdims=True)                 # (H, 1, 3)
    fill = np.repeat(col, x1 - x0, axis=1)

    # trochu zrna, aby plocha nebola nápadne hladká
    rng = np.random.default_rng(7)
    fill = fill + rng.normal(0, 1.6, fill.shape)
    patch = Image.fromarray(np.clip(fill, 0, 255).astype(np.uint8), "RGB")
    im.paste(patch, (x0, 0))

    # ľavý prechod do pôvodnej fotky
    blend = 26
    left = im.crop((x0 - blend, 0, x0 + blend, im.size[1])).filter(ImageFilter.GaussianBlur(1.4))
    im.paste(left, (x0 - blend, 0))
    return im


def packshot(name, tol=16, hull=True):
    """Vyreže matný packshot z bieleho pozadia.

    Kartón je rovná doska, takže bielu hranu na bielom pozadí nedokáže prah
    trafiť presne — vznikajú schodíky. Preto z masky spravíme konvexný obal:
    výsledok má rovné hrany presne tam, kde ich má aj krabička.
    """
    im = Image.open(PRODUCTS / f"{name}.png").convert("RGBA")
    rgb = np.asarray(im.convert("RGB"), dtype=np.int16)
    mask = (255 - rgb).max(axis=2) > tol
    mask = ndimage.binary_closing(mask, structure=np.ones((7, 7)))
    lab, n = ndimage.label(mask)
    if n:
        sizes = ndimage.sum(mask, lab, range(1, n + 1))
        mask = ndimage.binary_fill_holes(lab == (int(np.argmax(sizes)) + 1))

    m = Image.new("L", im.size, 0)
    if hull:
        from scipy.spatial import ConvexHull
        ys, xs = np.nonzero(mask)
        pts = np.column_stack([xs, ys])
        h = ConvexHull(pts)
        poly = [tuple(map(float, pts[i])) for i in h.vertices]
        ImageDraw.Draw(m).polygon(poly, fill=255)
    else:
        m = Image.fromarray(np.where(mask, 255, 0).astype(np.uint8), "L")

    m = m.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    im.putalpha(m)
    return im.crop(m.point(lambda v: 255 if v > 8 else 0).getbbox())


def drop_shadow(canvas, obj, x, y, spread=34, opacity=64, dx=26, dy=6):
    """Mäkký tieň v smere svetla fotky (zľava zhora)."""
    a = obj.getchannel("A")
    sh = Image.new("L", canvas.size, 0)
    sh.paste(a, (x + dx, y + dy))
    sh = sh.filter(ImageFilter.GaussianBlur(spread)).point(lambda v: int(v * opacity / 255))
    dark = Image.new("RGB", canvas.size, (137, 136, 134))
    canvas.paste(Image.composite(dark, canvas, sh))


def contact(canvas, x, w, y, opacity=74):
    """Jemný kontaktný tieň tesne pod hranou, aby produkt nelietal."""
    lay = Image.new("L", canvas.size, 0)
    d = ImageDraw.Draw(lay)
    d.rectangle((x + w * .02, y - 5, x + w * 1.02, y + 5), fill=opacity)
    lay = lay.filter(ImageFilter.GaussianBlur(7))
    dark = Image.new("RGB", canvas.size, (128, 127, 126))
    canvas.paste(Image.composite(dark, canvas, lay))


def build():
    im = Image.open(SRC / "_raw" / "rada-siroka.jpg").convert("RGB")
    erase(im, DUP[0], DUP[1], CLEAN[0], CLEAN[1])

    box = packshot("gelavit-pure-ananas-box")
    BW = 344
    box = box.resize((BW, round(box.size[1] * BW / box.size[0])), Image.LANCZOS)

    # zladenie so svetlom fotky: mierne stlmiť a oteplíť
    box = ImageEnhance.Brightness(box).enhance(0.985)
    box = ImageEnhance.Contrast(box).enhance(0.97)
    r, g, b, a = box.split()
    box = Image.merge("RGBA", (r.point(lambda v: min(255, int(v * 1.012))), g,
                               b.point(lambda v: int(v * 0.985)), a))

    BASE = 596                       # kde stojí — o kúsok bližšie ku kamere
    x = 1232
    y = BASE - box.size[1]

    drop_shadow(im, box, x, y)
    contact(im, x, box.size[0], BASE - 2)
    im.paste(box, (x, y), box)

    out = SRC / "lifestyle" / "rada-siroka.jpg"
    im.save(out, "JPEG", quality=93, optimize=True, progressive=True)
    return out


if __name__ == "__main__":
    print(build())
