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
 'bergmann': dict(dir='tischlerei-bergmann-bissendorf', fonts='r10bergmann', img={
   'hero.jpg': (RAW/'bergmann/img/i036.jpg', 2200), 'kubus.jpg': (RAW/'bergmann/img/i019.jpg', 900), 'kueche.jpg': (RAW/'bergmann/img/i005.jpg', 700),
   'g-tisch.jpg': (RAW/'bergmann/img/i018.jpg', 1000), 'g-kueche2.jpg': (RAW/'bergmann/img/i007.jpg', 700), 'g-schrank.jpg': (RAW/'bergmann/img/i010.jpg', 700),
   'g-gebeizt.jpg': (RAW/'bergmann/img/i012.jpg', 1000), 'g-wiege.jpg': (RAW/'bergmann/img/i009.jpg', 700), 'g-zinken.jpg': (RAW/'bergmann/img/i024.jpg', 700),
   'g-tv.jpg': (RAW/'bergmann/img/i017.jpg', 700), 'g-sideboard.jpg': (RAW/'bergmann/img/i014.jpg', 1000), 'g-staffelei.jpg': (RAW/'bergmann/img/i003.jpg', 700),
   'g-regal.jpg': (RAW/'bergmann/img/i016.jpg', 1000), 'h-kiefer.jpg': (RAW/'bergmann/img/i020.jpg', 600), 'h-birke.jpg': (RAW/'bergmann/img/i021.jpg', 600),
   'h-buche.jpg': (RAW/'bergmann/img/i022.jpg', 600), 't-alt.jpg': (RAW/'bergmann/img/i034.jpg', 900), 't-neu.jpg': (RAW/'bergmann/img/i035.jpg', 900),
   'aussen.jpg': (RAW/'bergmann/img/i030.jpg', 900), 'hobel2.jpg': (RAW/'bergmann/img/i001.jpg', 1100), 'leidenschaft.jpg': (RAW/'bergmann/img/i004.jpg', 1600),
 }),
 'tepe': dict(dir='tepe-massmann-wallenhorst', fonts='r10tepe', img={
   'hero.jpg': (RAW/'tepe/img/i002.jpg', 2000), 'logo.png': (R10/'logos2/tepe.png', 0), 'zert.png': (RAW/'tepe/img/i012.jpg', 0),
   'p-wintergarten.jpg': (RAW/'tepe/img/i003.jpg', 900), 'p-terrasse.jpg': (RAW/'tepe/img/i002.jpg', 900), 'p-vordach.jpg': (RAW/'tepe/img/i011.jpg', 900),
   'p-balkon.jpg': (RAW/'tepe/img/i004.jpg', 900), 'p-fassade.jpg': (RAW/'tepe/img/i006.jpg', 900), 'p-wintergarten2.jpg': (RAW/'tepe/img/i008.jpg', 900),
   'p-garage.jpg': (RAW/'tepe/img/i001.jpg', 900), 'p-tor.jpg': (RAW/'tepe/img/i010.jpg', 900), 'p-gelaender.jpg': (RAW/'tepe/img/i007.jpg', 900),
   'p-balkone.jpg': (RAW/'tepe/img/i005.jpg', 900), 's1.jpg': (RAW/'tepe/img/i007.jpg', 700), 's2.jpg': (RAW/'tepe/img/i003.jpg', 700),
   's3.jpg': (RAW/'tepe/img/i006.jpg', 700), 's4.jpg': (RAW/'tepe/img/i008.jpg', 700), 's5.jpg': (RAW/'tepe/img/i009.jpg', 700),
   'betrieb.jpg': (RAW/'tepe/img/i016.jpg', 1400),
 }),
 'borggreve': dict(dir='borggreve-osnabrueck', fonts='r10borggreve', img={
   'hero.jpg': (RAW/'borggreve/img/i001.jpg', 2000), 'logo.png': (R10/'logos2/borggreve.png', 0),
   'l-maler.jpg': (RAW/'borggreve/img/i029.jpg', 800), 'l-tapete.jpg': (RAW/'borggreve/img/i014.jpg', 800), 'l-boden.jpg': (RAW/'borggreve/img/i035.jpg', 800), 'l-fenster.jpg': (RAW/'borggreve/img/i004.jpg', 800),
   **{f'f{k}.jpg': (RAW/f'borggreve/img/i{n:03d}.jpg', 900) for k, n in [(1,29),(2,27),(3,28),(4,30),(5,31),(6,26)]},
   'farbfaecher.jpg': (RAW/'borggreve/img/i005.jpg', 700), 'service.jpg': (RAW/'borggreve/img/i006.jpg', 1100),
   **{f't{k}.jpg': (RAW/f'borggreve/img/i{n:03d}.jpg', 700) for k, n in [(1,14),(2,16),(3,18),(4,19),(5,21),(6,22)]},
   **{f'b{k}.jpg': (RAW/f'borggreve/img/i{n:03d}.jpg', 700) for k, n in [(1,35),(2,43),(3,47),(4,36),(5,48),(6,50)]},
 }),
 'abeling': dict(dir='abeling-essen-oldb', fonts='r10abeling', img={
   'logo.png': (R10/'logos2/abeling.png', 0),
   's1.jpg': (RAW/'abref/img/tankst_16.jpg', 1800), 's2.jpg': (RAW/'abref/img/landwi_08.jpg', 1800), 's3.jpg': (RAW/'abref/img/gewerb_05.jpg', 1800), 's4.jpg': (RAW/'abref/img/vordae_23.jpg', 1800),
   't-tank.jpg': (RAW/'abeling/img/i004.jpg', 900), 't-land.jpg': (RAW/'abeling/img/i005.jpg', 900), 't-gewerbe.jpg': (RAW/'abeling/img/i006.jpg', 900),
   't-vordach.jpg': (RAW/'abeling/img/i007.jpg', 900), 't-sonder.jpg': (RAW/'abeling/img/i008.jpg', 900),
   'z1.jpg': (RAW/'abref/img/tankst_19.jpg', 1200), 'z2.jpg': (RAW/'abref/img/tankst_17.jpg', 800), 'z3.jpg': (RAW/'abref/img/tankst_20.jpg', 800),
   'r-tank1.jpg': (RAW/'abref/img/tankst_16.jpg', 700), 'r-tank2.jpg': (RAW/'abref/img/tankst_17.jpg', 700), 'r-tank3.jpg': (RAW/'abref/img/tankst_18.jpg', 700),
   'r-land1.jpg': (RAW/'abref/img/landwi_13.jpg', 700), 'r-land2.jpg': (RAW/'abref/img/landwi_10.jpg', 700), 'r-land3.jpg': (RAW/'abref/img/landwi_11.jpg', 700),
   'r-gew1.jpg': (RAW/'abref/img/gewerb_02.jpg', 700), 'r-gew2.jpg': (RAW/'abref/img/gewerb_04.jpg', 700), 'r-gew3.jpg': (RAW/'abref/img/gewerb_06.jpg', 700),
   'r-vor1.jpg': (RAW/'abref/img/vordae_21.jpg', 700), 'r-vor2.jpg': (RAW/'abref/img/vordae_23.jpg', 700), 'r-vor3.jpg': (RAW/'abref/img/vordae_24.jpg', 700),
   'team.jpg': (RAW/'abeling/img/i010.jpg', 0),
 }),
 'daelken': dict(dir='dach-daelken-bad-laer', fonts='r10daelken', img={
   'logo.png': (R10/'logos2/daelken.png', 0), 'zettel.png': (R10/'logos2/daelken-zettel.png', 0),
   'h1.jpg': (RAW/'daelken/img/i003.jpg', 2200), 'h2.jpg': (RAW/'daelken/img/i000.jpg', 2200), 'h3.jpg': (RAW/'daelken/img/i004.jpg', 2200),
   'wohnbau.jpg': (RAW/'daelken/img/i005.jpg', 1400), 'w1.jpg': (RAW/'daelken/img/i006.jpg', 0), 'w2.jpg': (RAW/'daelken/img/i007.jpg', 0),
   'metall.jpg': (RAW/'daelken/img/i008.jpg', 1400), 'm1.jpg': (RAW/'daelken/img/i002.jpg', 900), 'm2.jpg': (RAW/'daelken/img/i013.jpg', 900),
   'industrie.jpg': (RAW/'daelken/img/i009.jpg', 1400), 'i1.jpg': (RAW/'daelken/img/i012.jpg', 900), 'fassade.jpg': (RAW/'daelken/img/i020.jpg', 0),
   'k1.jpg': (RAW/'daelken/img/i015.jpg', 0), 'k2.jpg': (RAW/'daelken/img/i016.jpg', 0), 'k3.jpg': (RAW/'daelken/img/i017.jpg', 0), 'k4.jpg': (RAW/'daelken/img/i019.jpg', 900),
   'd1.jpg': (RAW/'daelken/img/i023.jpg', 0), 'd2.jpg': (RAW/'daelken/img/i024.jpg', 0), 'd3.jpg': (RAW/'daelken/img/i025.jpg', 0), 'd4.jpg': (RAW/'daelken/img/i028.jpg', 0),
   'pv1.jpg': (RAW/'daelken/img/i031.jpg', 0), 'pv2.jpg': (RAW/'daelken/img/i032.jpg', 0), 'merlo.jpg': (RAW/'daelken/img/i043.jpg', 1400), 'flyer.jpg': (RAW/'daelken/img/i044.jpg', 0),
 }),
}

for _k, _a in {'bergmann':'Wulftener Str. 4, 49143 Bissendorf','tepe':'Fürstenauer Weg 1a, 49134 Wallenhorst','borggreve':'Bremer Straße 52, 49084 Osnabrück',
               'abeling':'Dinklager Straße 12, 49632 Essen (Oldenburg)','daelken':'Warendorfer Straße 36, 49196 Bad Laer'}.items():
    SITES[_k]['adresse'] = _a

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
    if site.get('adresse'):
        sys.path.insert(0, str(ROOT/'tools/vorschau')); import beauty; beauty.karte(site['adresse'], d)
    html = (H / f'{key}.html').read_text()
    html = html.replace('<!--KIT_CSS-->', (H/'kit.css').read_text()).replace('<!--KIT_JS-->', (H/'kit.js').read_text())
    html = html.replace('<!--FONTS-->', (FONTS / f"{site['fonts']}.css").read_text())
    (d / 'index.html').write_text(html)
    out = H / f'{key}.built.html'; out.write_text(html)
    print('OK', key, '→', d.name)

if __name__ == '__main__':
    for k in sys.argv[1:]: build(k)
