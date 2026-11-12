"""Handgebaute Runde-10-Seiten zusammensetzen: Bilder vorbereiten, Kit + Schriften einbetten.
Aufruf: python3 assemble.py <key> [...]   (key = pinke|kicker|siefker|vagts|liekam)"""
import sys, glob
from pathlib import Path
from PIL import Image, ImageOps

H = Path(__file__).parent
ROOT = Path('/home/claude/highlevel-performance')
FONTS = ROOT / 'tools/vorschau/fonts'
RAW = Path('/home/claude/r10raw')
R10 = Path('/home/claude/r10')

def slugdir(prefix):
    return sorted(ROOT.glob(f'vorschau/{prefix}-*'))[0]

SITES = {
 'pinke': dict(dir='pinke-neuenkirchen', fonts='r10pinke', img={
   'hero.jpg': (R10/'pinke_big/hero.jpg', 2200),
   't-heizung.jpg': (R10/'pinke_big/Heizung-Sanitaer-Energie-Maschinenbau-Georg-Pinke-GmbH-Co.-KG-3-3.jpg', 1000),
   't-sanitaer.jpg': (R10/'pinke_big/HEIZUNG-PINKE-Neuenkirchen-Start.jpg', 1000),
   't-kwk.jpg': (R10/'pinke_big/Kraft-Waerme-Kopplun-KWK-PINKE-Neuenkirchen-Start.jpg', 1000),
   't-maschinenbau.jpg': (R10/'pinke_big/MASCHINENBAU-PINKE-Neuenkirchen.jpg', 1000),
   'monteur.jpg': (RAW/'pinke/img/i027.jpg', 1100), 'monteur2.jpg': (RAW/'pinke/img/i026.jpg', 1100),
   'fbh.jpg': (RAW/'pinke/img/i024.jpg', 1100), 'bad.jpg': (RAW/'pinke/img/i036.jpg', 1400), 'ausstellung.jpg': (RAW/'pinke/img/i033.jpg', 1400),
   'werkstatt.jpg': (RAW/'pinke/img/i055.jpg', 1400), 'schweissen.jpg': (RAW/'pinke/img/i058.jpg', 1200), 'anschluss.jpg': (RAW/'pinke/img/i029.jpg', 1200),
   'logo.png': (R10/'pinke_big/logo.png', 0),
   **{f'ig{k}.jpg': (R10/f'pinke_ig/p{n}.webp', 700) for k, n in enumerate([1, 2, 7, 5, 4], 1)},
   **{f'tm{k:02d}.jpg': (RAW/f'pinke/img/i{86+k:03d}.jpg', 520) for k in range(14)},
 }),
 'kicker': dict(dir='peter-kicker-wallenhorst', fonts='r10kicker', img={
   'h-van.jpg': (R10/'kick/header-kicker-02b.png', 2000), 'h-wp.jpg': (RAW/'kicker/img/i016.jpg', 1400), 'h-bad.jpg': (R10/'kick/slider-start-07.jpg', 2000),
   'team.jpg': (R10/'kick/header-kicker-03.jpg', 1800), 'einsatz.jpg': (R10/'kick/einsatz.jpg', 900),
   'simon.jpg': (R10/'kick/simon-ueberuns.jpg', 700), 'peter.jpg': (R10/'kick/peter-ueberuns.jpg', 700),
   'wp.jpg': (RAW/'kicker/img/i016.jpg', 1200), 'bio.jpg': (RAW/'kicker/img/i027.jpg', 900), 'brw.jpg': (RAW/'kicker/img/i017.jpg', 900),
   'wart.jpg': (RAW/'kicker/img/i019.jpg', 900), 'wp-aussen.jpg': (RAW/'kicker/img/i028.jpg', 900), 'bad-bf.jpg': (RAW/'kicker/img/i024.jpg', 1200),
   'bad-plan.jpg': (R10/'kick/AdobeStock_313238299__msi___jpg.jpg', 900), 'plan.jpg': (R10/'kick/AdobeStock_241837234__msi___jpg.jpg', 1000),
   'l-eut.png': (R10/'kick/EUT_Logo-ff61025e-1920w.png', 0), 'l-buderus.jpg': (R10/'kick/BUDERUS-Logo__msi___png.jpg', 320),
   'l-rwh.png': (R10/'kick/avatarimage.png', 0), 'l-elements.png': (R10/'kick/elements-logo_63__msi___png.png', 0),
   'logo.png': (R10/'kick/imgi_2_9g1HdiN01ZnatxByVJH1oT6egkewnG6AXBFHv2CW__msi___png.png', 0),
 }),
 'liekam': dict(dir='liekam-osnabrueck', fonts='r10liekam', img={
   'hero.mp4': (R10/'vid/o_Startseite.mp4', 0), 'hero.jpg': (R10/'vid/p_Startseite.jpg', 1600),
   'guten.mp4': (R10/'vid/o_Ueber.mp4', 0), 'guten.jpg': (R10/'vid/p_Ueber.jpg', 1280),
   'karriere.mp4': (R10/'vid/o_Karriere.mp4', 0), 'karriere-p.jpg': (R10/'vid/p_Karriere.jpg', 1280),
   **{f'm-{n}.jpg': (RAW/f'liekamhaustech/img/i{i:03d}.jpg', 1000) for n, i in [('heizung',4),('sanitaer',5),('erneuerbar',6),('elektro',7),('baeder',8),('klempner',9),('fliesen',10),('klima',11),('rohr',12)]},
   'pv.jpg': (RAW/'liekamhaustech/img/i013.jpg', 1600), 'wp.jpg': (RAW/'liekamhaustech/img/i014.jpg', 1600),
   'sven.jpg': (RAW/'liekamhaustech/img/i019.jpg', 700), 'team.jpg': (RAW/'liekamhaustech/img/i002.jpg', 1000),
   'jacken.jpg': (RAW/'liekamhaustech/img/i058.jpg', 1600), 'ausstellung.jpg': (RAW/'liekamhaustech/img/i055.jpg', 1000),
   'beratung.jpg': (RAW/'liekamhaustech/img/i059.jpg', 1000), 'eroeffnung.jpg': (RAW/'liekamhaustech/img/i049.jpg', 1400),
   'ref1.jpg': (RAW/'liekamhaustech/img/i016.jpg', 1400), 'ref2.jpg': (RAW/'liekamhaustech/img/i018.jpg', 1400), 'ref3.jpg': (RAW/'liekamhaustech/img/i017.jpg', 1000), 'ref4.jpg': (RAW/'liekamhaustech/img/i015.jpg', 1000),
   'logo.png': (R10/'logos/liekam.png', 0),
   **{f'tm{k:02d}.jpg': (RAW/f'liekamhaustech/img/i{19+k:03d}.jpg', 500) for k in range(15)},
 }),
 'vagts': dict(dir='vagts-haustechnik-ahlhorn', fonts='r10vagts', img={
   'hero.jpg': (RAW/'vagtshaustechn/img/i004.jpg', 1920), 'team.jpg': (RAW/'vagtshaustechn/img/i008.jpg', 1800), 'flotte.jpg': (RAW/'vagtshaustechn/img/i009.jpg', 1600),
   'logo.png': (R10/'vagts/logo-vagts-haustechnik-1920w.png', 0), 'logo-dark.png': (R10/'logos/vagts_dark.png', 0),
   'badge.png': (R10/'vagts/image-asset-1920w.png', 0), 'jannik.png': (R10/'vagts/jannik-vagts-intro-1920w.png', 0),
   'i-heizung.png': (R10/'vagts/icon-heizung-1920w.png', 0), 'i-sanitaer.png': (R10/'vagts/icon-sanitaer-1920w.png', 0), 'i-klima.png': (R10/'vagts/icon-klima-1920w.png', 0),
   'handwerk.jpg': (RAW/'vagtshaustechn/img/i003.jpg', 0),
   **{f'tm{k:02d}.jpg': (RAW/f'vagtshaustechn/img/i{13+k:03d}.jpg', 520) for k in range(16)},
 }),
 'siefker': dict(dir='siefker-bad-essen', fonts='r10siefker', img={
   'hero.jpg': (RAW/'siefker/img/i002.jpg', 2212), 'bad.jpg': (RAW/'siefker/img/i010.jpg', 1100), 'elektro.jpg': (RAW/'siefker/img/i012.jpg', 1100),
   'oel.jpg': (RAW/'siefker/img/i016.jpg', 1100), 'gas.jpg': (RAW/'siefker/img/i014.jpg', 1100), 'lueftung.jpg': (RAW/'siefker/img/i007.jpg', 1100),
   'bus.jpg': (RAW/'siefker/img/i020.jpg', 1100), 'team.jpg': (RAW/'siefker/img/i018.jpg', 1100), 'zaehler.jpg': (RAW/'siefker/orig/i017.jpg', 520),
   'telefon.jpg': (RAW/'siefker/img/i005.jpg', 520), 'logo.png': (R10/'logos/siefker.png', 0),
 }),
}

def prep(site):
    d = slugdir(site['dir']) / 'img'
    for dst, (src, w) in site['img'].items():
        out = d / dst
        if str(src).endswith('.mp4'):
            import shutil; shutil.copy(src, out); continue
        im = Image.open(src); im = ImageOps.exif_transpose(im)
        if dst.endswith('.png'):
            im = im.convert('RGBA')
            if im.width > 700: im = im.resize((700, round(im.height * 700 / im.width)), Image.LANCZOS)
            im.save(out, optimize=True); continue
        im = im.convert('RGB')
        if w and im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        if dst.startswith('tm') or dst.startswith('ig'):
            pass
        im.save(out, quality=84, optimize=True, progressive=True)
    return d.parent

def build(key):
    site = SITES[key]
    d = prep(site)
    html = (H / f'{key}.html').read_text()
    html = html.replace('<!--KIT_CSS-->', (H/'kit.css').read_text()).replace('<!--KIT_JS-->', (H/'kit.js').read_text())
    html = html.replace('<!--FONTS-->', (FONTS / f"{site['fonts']}.css").read_text())
    (d / 'index.html').write_text(html)
    out = H / f'{key}.built.html'; out.write_text(html)
    print('OK', key, '→', d.name)

if __name__ == '__main__':
    for k in sys.argv[1:]: build(k)
