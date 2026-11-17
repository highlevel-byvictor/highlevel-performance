"""Runde 16 · Teil B: Meppens Küchenstudio, Ihre Küche & Mehr, Die Zwei Küchen / Möbelbau Maic Niemann."""
from common import *
SITES = {}

# ───────────── 5. Meppens Küchenstudio, Meppen ─────────────
def b_meppens(s):
    T = [('t01.jpg', 'Lothar Hempel', 'Geschäftsführer, Küchenfachberater'), ('t02.jpg', 'Andreas Nieters', 'Küchenfachberater (DE · NL)'),
         ('t03.jpg', 'Benjamin Baudendistel', 'Küchenfachberater (DE · NL)'), ('t04.jpg', 'Christian Wester', 'Küchenfachberater (DE · NL)'),
         ('t05.jpg', 'Gela Reinink', 'Angehende Küchenfachberaterin (DE · NL)'), ('t06.jpg', 'Sonja Korte', 'Auftrags- und Sachbearbeitung'),
         ('t07.jpg', 'Manuela Heymann', 'Sachbearbeitung'), ('t08.jpg', 'Gaby Blasczyk', 'Mitarbeiterin'), ('t09.jpg', 'Frank Düttmann', 'Küchen-Fachmonteur'),
         ('t10.jpg', 'Patrick Sommer', 'Küchen-Fachmonteur'), ('t11.jpg', 'Christoph Sandmann', 'Küchen-Fachmonteur'), ('t12.jpg', 'Christoph Budde', 'Küchen-Fachmonteur'),
         ('t13.jpg', 'Björn Mink', 'Küchen-Fachmonteur'), ('t14.jpg', 'Marek Fehrmann', 'Küchen-Fachmonteur'), ('t15.jpg', 'Philipp Kreutzmann', 'Lager &amp; Logistik')]
    return (hd(s, False) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg', 'h4.jpg'], pos={'h1.jpg': '60% 50%', 'h2.jpg': '60% 50%', 'h3.jpg': '60% 50%', 'h4.jpg': '60% 50%'},
        big='40', ey='Meppens Küchenstudio · das Original seit über 40 Jahren',
        h1='Küche mit Herz. <em>Ihr Rezept zur Traumküche.</em>',
        sub='Professionelle und individuelle Beratung, 3D-Planung, Lieferung und Montage aus einer Hand. Beratung auf Deutsch und Niederländisch, auf Wunsch auch nach 18 Uhr.',
        ubar=[('40+ Jahre', 'Ihr Experte in Sachen Küche'), ('15 Profis', 'Beratung, Büro, Montage, Lager'), ('Platz 4', '„Das Goldene Dreieck“ 2016')]))
        + spot('quooker', 'Quooker im Meppens Küchenstudio', 'Der Hahn, der alles kann. <em>Live bei uns im Studio.</em>', 'Kochend, gekühlt, sprudelnd: Den Quooker zeigen wir Ihnen in unserer Ausstellung in Meppen am laufenden Hahn. Den TV-Spot gibt es hier schon mal vorab.', 'quooker.mp4', 'quooker.jpg', 'mpq')
        + marquee(['Häcker', 'Schüller', 'neola', 'Laminam', 'Stoneworks', 'Siemens', 'Miele', 'Berbel', 'Franke', 'Naber'], 'mp')
        + promo('angebote', 'p-ausstellung.jpg', 'Aktion 2026', 'Ausstellungsküchen <em>zum Hammerpreis.</em>',
                'Unsere Ausstellungsküchen geben wir zu besonders günstigen Preisen ab, inklusive Markengeräten. Dazu gibt es das neue Küchenmagazin 2026 gratis, im Studio oder per Post zu Ihnen nach Hause.',
                ['Ausstellungsküchen mit Markengeräten', 'Küchenmagazin 2026 gratis', 'Wij spreken Nederlands'], 'Ausstellungsküche anfragen', 'alt')
        + tabs('leistungen', 'Alles aus einer Hand', 'Einzigartig, individuell, <em>ein Meisterwerk.</em>', 'Professionelle und individuelle Beratung ist unsere Maxime, um Ihre Traumküche mit Ihnen zu konzipieren.', [
            ('Individuelle Beratung', 'l1.jpg', 'Persönlich und bedarfsgerecht, auch zur idealen Arbeitshöhe für Ihren Rücken. Beratungen nach 18 Uhr mit Terminabsprache.', ['Ergonomie', 'Auch nach 18 Uhr']),
            ('3D-Computerplanung', 'l2.jpg', 'Virtuell und doch real: Sie sehen Ihre Küche, bevor sie gebaut wird. Dazu nehmen wir bei Ihnen zu Hause Maß.', ['3D-Planung', 'Aufmaß vor Ort']),
            ('Glas, Granit, Edelstahl', 'l3.jpg', 'Unsere Spezialität: Arbeitsplatten und Flächen aus Glas, Granit, Edelstahl und Keramik.', ['Laminam', 'Stoneworks']),
            ('Lieferung & Montage', 'l4.jpg', 'Fachgerecht und pünktlich durch unsere eigenen Küchen-Fachmonteure, inklusive Strom- und Sanitäranschlüssen.', ['Eigene Monteure', 'Strom und Wasser']),
            ('Kundendienst & Finanzierung', 'l5.jpg', 'Haben Sie Fragen? Wir helfen gern. Clever finanzieren zu günstigen Konditionen bei unserer Hausbank.', ['Kundendienst', 'Finanzierung'])])
        + gallery('kundenkuechen', 'Küchen unserer Kunden', 'Echte Küchen, <em>echte Zuhause.</em>', [
            ('k1.jpg', 'w2', '50% 50%'), ('k2.jpg', '', '50% 50%'), ('k3.jpg', '', '50% 50%'), ('k4.jpg', '', '50% 50%'), ('k5.jpg', '', '50% 50%'), ('k6.jpg', 'w2', '50% 50%'), ('k7.jpg', '', '50% 50%'), ('k8.jpg', '', '50% 50%')])
        + story('auszeichnung', 'Küche des Jahres', 'Platz 4 beim <em>„Goldenen Dreieck“.</em>', [
            'Mit dem Küchen-Award „Das Goldene Dreieck“ werden die schönsten Küchen Deutschlands ausgezeichnet. 2016 hat Meppens Küchenstudio den 4. Platz nach Meppen geholt, mit einer Küche in Friesland.',
            'Auch 2026 läuft die Aktion wieder: Wir planen Ihre Traumküche, und Sie können gewinnen.'],
            'award.jpg', cap='Eindrücke aus unserem Studio am Schützenhof 19', rev=True, cls='dk')
        + team('team', 'Das Team vom Küchenstudio Meppen', 'Küchen sind <em>Lebensräume.</em>', 'Im Mittelpunkt unserer Arbeit steht immer der Mensch. Hier sind Ihre Ansprechpartner.', T)
        + reviews(s, ['Herr Hempel hat uns hochkompetent beraten und fachkundig geplant. Dank seiner tollen Ideen ist unsere Küche ein echter Traum geworden. Lieferung und Montage waren erstklassig.',
                      'Lothar hat uns hervorragend und angenehm beraten. Die Monteure waren freundlich, genau und haben super zusammengearbeitet.',
                      'Absolut empfehlenswert: Von der ersten Beratung bis zur Montage lief alles reibungslos. Die Auswahl an Fronten, Platten und Geräten ist beeindruckend.',
                      'Ein fantastisches Unternehmen mit großartiger Beratung und mehr als exzellentem Service.'], 'alt')
        + contact(s) + footer(s) + pop(dict(img='p-ausstellung.jpg', ey='Aktion 2026', h='Ausstellungsküchen zum Hammerpreis', p='Inklusive Markengeräten. Dazu das Küchenmagazin 2026 gratis.', btn='Jetzt anfragen')))

S = SITES['meppens'] = site(
    slug='meppens-kuechenstudio', firma='Meppens Küchenstudio', web='kuechenstudio-meppen.de', fonts='r16meppens',
    title='Meppens Küchenstudio – das Original seit über 40 Jahren', desc='Meppens Küchenstudio am Schützenhof 19: Küchen mit Herz seit über 40 Jahren. Beratung auf Deutsch und Niederländisch, 3D-Planung, eigene Monteure, Ausstellungsküchen.',
    tel='05931 6686', tel_i='+4959316686', mail='info@kuechenstudio-meppen.de', adresse='Schützenhof 19, 49716 Meppen', google=('4,7', 75),
    cta='Beratungstermin vereinbaren', nav=[('Angebote', 'angebote'), ('Leistungen', 'leistungen'), ('Kundenküchen', 'kundenkuechen'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '09:00 – 12:30, 13:30 – 18:00'), ('Sa', '09:00 – 13:00'), ('', 'Beratung nach 18 Uhr mit Termin')],
    form_opts=['Neue Küche', 'Ausstellungsküche', 'Küchenmagazin 2026 gratis', 'Beratung auf Niederländisch', 'Kundendienst', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Wir rufen Sie zurück und finden einen Termin, gern auch nach 18 Uhr.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Ihren Besuch.</em>', kt_p='Rufen Sie uns an unter 05931 6686. Wij spreken ook Nederlands.',
    social=[('Facebook', 'https://www.facebook.com/MeppensKuechenstudio')], rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars='--bg:#fff;--ink:#151417;--mute:#56545b;--p:#DC092F;--p-ink:#fff;--a:#DC092F;--a-ink:#fff;--dk:#15141A;--s:#fff;--s2:#f4f3f3;--fh:"Open Sans",system-ui,sans-serif;--fb:"Open Sans",system-ui,sans-serif;--r:2px;--r2:4px;--br:2px;--hero-ov:linear-gradient(95deg,rgba(21,20,26,.9) 0%,rgba(21,20,26,.55) 52%,rgba(21,20,26,.05) 100%);--mq-bg:#15141A;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#151417;--logo-h:40px;--ft-bg:#15141A',
    css='''.hs h1,.h2{font-weight:800;letter-spacing:-.015em;line-height:1.04;text-transform:uppercase}.hs h1{font-size:clamp(36px,4.6vw,70px)}.hs h1 em,.h2 em{font-style:italic;color:#ff3a59}.h2 em{color:#DC092F}.dk .h2 em{color:#ff3a59}
.h2{font-size:clamp(30px,3.6vw,50px)}.hs .big{font-style:italic;-webkit-text-stroke:2px rgba(220,9,47,.5)}
.hd{border-bottom:3px solid #DC092F;background:rgba(255,255,255,.97)!important}.hd .nav a{color:#151417}.hs .ey{color:#ff8a9c!important}.hs h1{hyphens:manual}.mq.mp span{font-weight:800;font-style:italic;text-transform:uppercase}.alt{background:var(--s2)}
.tm .grid{grid-template-columns:repeat(5,1fr);gap:22px}.tm .grid figure div{aspect-ratio:3/4}.tm .grid figure div img{object-position:50% 20%}
@media(max-width:900px){.tm .grid{grid-template-columns:repeat(2,1fr)}}
.ft img{background:#fff;padding:8px 12px;height:52px}''')
S['css2'] = '.sp16{--sp-bg:#15141A}.sp16 .h2{text-transform:uppercase}.sp16 .h2 em{color:#ff3a59}'
S['bot'] = BOT('Mia', 'Ihre Küchen-Lotsin', 'Meppens Küchenstudio', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–12:30 und 13:30–18 Uhr, Sa 9–13 Uhr. Beratungen nach 18 Uhr mit Terminabsprache.'],
    ['Ausstellungsküchen?', 'Aktuell gibt es Ausstellungsküchen zum Hammerpreis. Rufen Sie an: 05931 6686.'],
    ['Nederlands?', 'Ja, onze adviseurs spreken Nederlands. Bel ons: +49 5931 6686.']],
    ['#angebote', '#leistungen', '#kundenkuechen', '#kontakt'])
M = 'meppens/img/'
S['img'] = {'quooker.mp4': ('/home/claude/r16raw/vid/meppens_quooker_web.mp4', 0), 'quooker.jpg': ('/home/claude/r16raw/vid/meppens_poster.jpg', 0), 'logo.png': (M + 'i002.png', 0), 'h1.jpg': (M + 'i017.jpg', 0), 'h2.jpg': (M + 'i008.jpg', 0), 'h3.jpg': (M + 'i018.jpg', 0), 'h4.jpg': (M + 'i019.jpg', 0),
    'p-ausstellung.jpg': (M + 'i010.jpg', 1200), 'award.jpg': (M + 'i020.jpg', 0),
    'l1.jpg': (M + 'i011.jpg', 1400), 'l2.jpg': (M + 'i012.jpg', 1400), 'l3.jpg': (M + 'i021.jpg', 0), 'l4.jpg': (M + 'i009.webp', 1400), 'l5.jpg': (M + 'i022.jpg', 0),
    'k1.jpg': (M + 'i087.jpg', 0), 'k2.jpg': (M + 'i070.jpg', 0), 'k3.jpg': (M + 'i080.jpg', 0), 'k4.jpg': (M + 'i072.jpg', 0), 'k5.jpg': (M + 'i081.jpg', 0),
    'k6.jpg': (M + 'i091.jpg', 0), 'k7.jpg': (M + 'i079.jpg', 0), 'k8.jpg': (M + 'i071.jpg', 0)}
for i in range(15): S['img'][f't{i+1:02d}.jpg'] = (M + f'i{105+i:03d}.jpg', 0)
S['body'] = b_meppens

# ───────────── 6. Ihre Küche & Mehr, Meppen ─────────────
def b_ikum(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-team.jpg', pos='50% 32%', wide=True, alt='Das Team von Ihre Küche &amp; Mehr in der Ausstellung in Meppen',
        ey='Ihre Küche &amp; Mehr · der Küchenprofi im Emsland',
        h1='Wir nehmen Ihre Küche persönlich. <em>Herz drauf!</em>',
        sub='Ihr Küchenstudio in Meppen mit großer Ausstellung: individuelle Planung, Marken wie pronorm, NEFF, Quooker, Hollweg und brueder, dazu Lieferung und Montage durch unser Team.',
))
        + marquee(['pronorm', 'NEFF', 'Quooker', 'Hollweg', 'brueder', 'Miele', 'Siemens', 'Bosch', 'Blanco', 'Naber'], 'ik')
        + scroller('kuechenideen', 'Küchenideen', 'Lassen Sie sich <em>inspirieren.</em>', 'Musterküchen und Raumkonzepte live in unserer großzügigen Ausstellung in Meppen.', [
            ('Holz und Wärme', 'k1.jpg', 'Natürliche Fronten, gemütliche Atmosphäre.', '50% 50%'),
            ('Beton und Glas', 'k2.jpg', 'Moderne Materialien, klare Linien.', '50% 50%'),
            ('Mit Kochinsel', 'k3.jpg', 'Kochen mitten im Leben.', '50% 50%'),
            ('Farbe mit Mut', 'k4.jpg', 'Ein Statement in Rot.', '50% 50%'),
            ('Dunkel und edel', 'k5.jpg', 'Schwarz trifft Holz.', '50% 50%'),
            ('Wohnküche', 'k6.jpg', 'Küche und Wohnraum verschmelzen.', '50% 50%')])
        + duo('beratung', 'Beratung und Planung', 'Ihre maßgeschneiderte <em>Traumküche.</em>', 'Ob in unserem Küchenstudio mit zahlreichen Beispielküchen oder bei Ihnen zu Hause: Wir nehmen uns Zeit für Sie.', [
            ('Im Studio', 'Persönliche Beratung', 'd1.jpg', 'Nach Terminvereinbarung nimmt sich einer unserer Fachberater ausführlich Zeit für Sie. Tipp: Bringen Sie eine bemaßte Grundrisszeichnung mit.', ['Viele Beispielküchen', 'Donnerstags bis 20 Uhr'], 'Termin anfragen'),
            ('Bei Ihnen', 'Lieferung und Montage', 'd2.jpg', 'Unsere Küchenmonteure bauen Ihre Küche fachgerecht bei Ihnen zu Hause auf, von der Planung bis zum letzten Handgriff aus einer Hand.', ['Eigene Küchenmonteure', 'Alles aus einer Hand'], 'Beratung anfragen')])
        + story('ueber-uns', 'Über uns', 'Für Meppen und das Emsland: <em>nur das Beste.</em>', [
            'Unser Versprechen lautet: „Wir nehmen Ihre Küche persönlich.“ In unseren großzügigen Ausstellungsräumen erleben Sie Designs, Materialien und Verarbeitung hautnah.',
            'Geführt wird Ihre Küche &amp; Mehr von Wilfried Dulle und Markus Jürgens. Unsere Pflegeprodukte für Ihre Küche gibt es übrigens auch im Onlineshop.'],
            'u-herz.jpg', cap='„Wir nehmen Ihre Küche persönlich.“', rev=True, cls='alt')
        + reviews(s, ['Das beste Küchenstudio im Emsland. Herr Dulle hat uns ausgezeichnet beraten, das Angebot war absolut fair, und er kam vorher sogar zu uns nach Hause, um sich alles anzusehen.',
                      'Toller Service von der Planung bis zur Montage. Küche und Hauswirtschaftsraum wurden geplant und eingebaut, der Montagetermin stand früh fest und wurde eingehalten.',
                      'Wilfried hat uns auf Niederländisch durch den ganzen Prozess begleitet. Wir haben genau die Küche bekommen, die wir wollten.',
                      'Die Küche ist unglaublich praktisch und das Design ist perfekt aufgegangen. Die Monteure waren pünktlich und freundlich.'])
        + contact(s, 'dk') + footer(s) + pop(dict(img='d1.jpg', ey='Länger für Sie da', h='Donnerstags bis 20 Uhr geöffnet', p='Planen Sie Ihre Küche ganz entspannt nach Feierabend.', btn='Termin anfragen')))

S = SITES['ikum'] = site(
    slug='ihre-kueche-und-mehr-meppen', firma='Ihre Küche und Mehr GmbH', web='ihre-kueche-und-mehr.de', fonts='r16ikum',
    title='Ihre Küche & Mehr – der Küchenprofi im Emsland | Meppen', desc='Ihre Küche & Mehr am Sophienplatz in Meppen: Wir nehmen Ihre Küche persönlich. Große Ausstellung, pronorm, NEFF, Quooker, eigene Monteure, donnerstags bis 20 Uhr.',
    tel='05931 8338', tel_i='+4959318338', mail='kueche_u._mehr@t-online.de', adresse='Sophienplatz 1–7, 49716 Meppen', google=('4,9', 76),
    cta='Beratungstermin anfragen', nav=[('Küchenideen', 'kuechenideen'), ('Beratung', 'beratung'), ('Über uns', 'ueber-uns'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '09:00 – 13:00, 14:00 – 18:30'), ('Do', 'bis 20:00'), ('Sa', '09:00 – 13:00')],
    form_opts=['Neue Küche', 'Beratung im Studio', 'Beratung zu Hause', 'Hauswirtschaftsraum / Wohnbereich', 'Pflegeprodukte', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Ein Fachberater nimmt sich Zeit für Sie. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Sie.</em>', kt_p='Rufen Sie an unter 05931 8338 oder kommen Sie vorbei, donnerstags sogar bis 20 Uhr.',
    rv_h2='Herz drauf: <em>Das sagen unsere Kunden.</em>',
    vars='--bg:#fff;--ink:#1d1e3a;--mute:#555872;--p:#16A6A6;--p-ink:#fff;--a:#1a9e9e;--a-ink:#fff;--dk:#343565;--s:#fff;--s2:#eef8f8;--fh:"Asap",system-ui,sans-serif;--fb:"Asap",system-ui,sans-serif;--r:10px;--r2:18px;--br:999px;--mq-bg:#343565;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#1d1e3a;--logo-h:58px;--ft-bg:#24254a;--hx-bg:linear-gradient(170deg,#fff 0%,#eef8f8 60%,#e3f3f3 100%);--hxw-ar:21/9;--hx-r:22px',
    css='''.hx h1,.h2{font-weight:700;letter-spacing:-.02em;line-height:1.05}.hx h1 em{display:inline-block;color:#e2001a;font-style:italic}.h2 em{font-style:normal;color:#16A6A6}.dk .h2 em{color:#7fe0e0}
.hx{padding-top:130px}.hx h1{hyphens:manual}@media(max-width:820px){.hx .gl{display:none}.hx.wide .pic{--hxw-ar:4/3}}.mq.ik span{font-weight:700}.alt{background:var(--s2)}.st figure img{object-position:50% 50%}
.ft img{background:#fff;padding:8px 12px;border-radius:10px;height:60px}''')
S['css2'] = '.hx{padding-top:92px!important;min-height:0!important}.hx.wide .w{gap:26px}.hx.wide .pic{margin-inline:calc(50% - 50vw);aspect-ratio:auto!important;height:min(54vh,520px);box-shadow:none}.hx h1{font-size:clamp(38px,4.3vw,66px)!important}@media(max-width:820px){.hx.wide .pic{height:38vh;margin-inline:-20px}}'
S['bot'] = BOT('Lena', 'Ihre Küchen-Lotsin', 'Ihre Küche &amp; Mehr', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–13 und 14–18:30 Uhr, donnerstags bis 20 Uhr, Sa 9–13 Uhr.'],
    ['Beratung zu Hause?', 'Ja, wir beraten Sie im Studio oder bei Ihnen zu Hause. Rufen Sie an: 05931 8338.'],
    ['Welche Marken?', 'Unter anderem pronorm, NEFF, Hollweg, Quooker und brueder.']],
    ['#kuechenideen', '#beratung', '#ueber-uns', '#kontakt'])
I = 'ikum/img/'
S['img'] = {'logo.png': ('ikum/hi/i000.png', 900), 'h-team.jpg': ('ikum/hi/i033.jpg', 0),
    'k1.jpg': (I + 'i018.jpg', 1100), 'k2.jpg': (I + 'i019.jpg', 1100), 'k3.jpg': (I + 'i020.jpg', 1100), 'k4.jpg': (I + 'i021.jpg', 1100), 'k5.jpg': (I + 'i024.jpg', 1100), 'k6.jpg': (I + 'i022.jpg', 1100),
    'd1.jpg': ('ikum/hi/i039.jpg', 1400, (.18, 0, .82, 1)), 'd2.jpg': ('ikum/hi/i038.jpg', 1400, (.18, 0, .82, 1)), 'u-herz.jpg': ('ikum/hi/i032.jpg', 1400)}
S['body'] = b_ikum

# ───────────── 7. Die Zwei Küchen & Möbelbau Maic Niemann, Lastrup ─────────────
def b_zwei(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['emo.jpg', 'h-pic.jpg', 'h-moebel.jpg'], pos={'emo.jpg': '55% 35%', 'h-moebel.jpg': '50% 40%'}, side='l', big='2',
        ubar=[('Meisterbetrieb', 'eigene Werkstatt'), ('3D-Planung', 'Aufmaß vor Ort'), ('Deutschlandweit', 'Montage')],
        ey='Die Zwei Küchen &amp; Möbelbau Maic Niemann · Lastrup',
        h1='Ihre Küche nach Maß. <em>Geplant und gebaut in Lastrup.</em>',
        sub='Einbauküchen in allen Variationen und Möbel nach Maß aus der eigenen Meisterwerkstatt, unter einem Dach in Lastrup. Montage deutschlandweit.',
))
        + marquee(['Häcker', 'nobilia', 'berbel', 'Miele', 'Bosch', 'NOVY', 'Quooker', 'Constructa', 'Möbel nach Maß'], 'zw')
        + duo('welten', 'Zwei Partner, ein Standort', 'Küche und Möbel <em>aus einer Hand.</em>', 'Ihre Küche plant Die Zwei Küchen, passende Möbel fertigt Möbelbau Maic Niemann.', [
            ('Küchenstudio', 'Die Zwei Küchen', 'w-kueche.jpg', 'Küchen für jede Raumgröße, hochwertige Materialien und Elektrogeräte namhafter Hersteller. Auch Sonderwünsche sind kein Problem.', ['Computergestützte 3D-Planung', 'Aufmaß vor Ort', 'Montage deutschlandweit'], 'Küche anfragen'),
            ('Möbelbau', 'Möbel nach Maß', 'w-moebel.jpg', 'Wohnzimmer, Esszimmer, Schlafzimmer, Küche oder Bad: Wir fertigen ganz individuell, in der eigenen Werkstatt mit modernem Maschinenpark.', ['Meisterbetrieb', 'Eigene Produktion', 'Einzelmöbel bis Komplettraum'], 'Möbel anfragen')])
        + gallery('eindruecke', 'Eindrücke aus unseren Projekten', 'Geplant, gefertigt, <em>eingebaut.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 60%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%'), ('g7.jpg', '', '50% 50%'), ('g8.jpg', '', '50% 50%')], 'alt')
        + svc('leistungen', 'Unsere Leistungen', 'Das ganze Spektrum <em>des Küchenkaufs.</em>', 'Mit unserer Planungssoftware sind wir professionell, schnell und effizient.', [
            ('Beratung', 'Nicht nur aus Sicht des Küchenfachberaters, sondern auch aus Sicht der Menschen, die täglich in der Küche stehen.'),
            ('Mobile Küchenplanung', 'Wir beraten und messen bei Ihnen vor Ort, für die optimale Raumaufteilung.'),
            ('Montage', 'Durch erfahrene Küchenmonteure, sauber und staubarm. Die Übergabe nach Abnahme macht der Inhaber persönlich.'),
            ('Umbau und Entsorgung', 'Renovierung, Erweiterung, Umbau bei Umzug, dazu die Entsorgung der alten Küche und Geräte.')])
        + story('inhaber', 'Ihr Ansprechpartner', 'Maic Niemann, <em>Inhaber.</em>', [
            'Als Meisterbetrieb verstehen wir unser Handwerk. Möbelbau Maic Niemann und Die Zwei Küchen arbeiten unter einem Dach an der Adam-Opel-Straße 5 in Lastrup zusammen.',
            'Gegen eine Planungsgebühr erhalten Sie alle Pläne. Kaufen Sie die Küche bei uns, wird die Gebühr zu 100 % angerechnet.'],
            'inhaber.jpg', cap='Maic Niemann', rev=True, cls='dk')
        + reviews_ns(s, ['Wir haben heute unsere Küche ausgesucht, die Beratung war hervorragend. Der Inhaber hat bei uns zu Hause selbst ausgemessen, kurz darauf hatten wir die Entwürfe im Postfach. Unsere Wünsche wurden zu 100 % erfüllt.',
                         'Ausgezeichnete Beratung und Montage. Wir haben Büro, Ankleide und Hauswirtschaftsraum einrichten lassen und sind mehr als begeistert.',
                         'Super freundliche Mitarbeiter, die sich auskennen, haben mich bei meiner Küchenplanung sehr gut beraten.',
                         'Hervorragende Beratung, super Qualität, immer auf dem neuesten Stand und Unterstützung auch nach dem Kauf.'])
        + contact(s) + footer(s) + pop(dict(img='g1.jpg', ey='Mobile Küchenplanung', h='Wir planen bei Ihnen vor Ort.', p='Aufmaß und Beratung zu Hause, für die optimale Raumaufteilung.', btn='Termin anfragen')))

S = SITES['zwei'] = site(
    slug='die-zwei-kuechen-lastrup', firma='Die Zwei Einbauküchen & Möbel nach Maß', web='die-zwei-kuechen.de', fonts='r16zwei',
    title='Die Zwei Küchen & Möbelbau Maic Niemann – Lastrup', desc='Die Zwei Küchen und Möbelbau Maic Niemann in Lastrup: Einbauküchen in allen Variationen, Möbel nach Maß aus der eigenen Meisterwerkstatt, Montage deutschlandweit.',
    tel='04472 947120', tel_i='+494472947120', mail='info@die-zwei-kuechen.de', adresse='Adam-Opel-Straße 5, 49688 Lastrup', google=None,
    cta='Beratungstermin anfragen', nav=[('Küche &amp; Möbel', 'welten'), ('Eindrücke', 'eindruecke'), ('Leistungen', 'leistungen'), ('Inhaber', 'inhaber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '10:00 – 16:00'), ('Sa', 'nach Vereinbarung'), ('Mobil', '0173 2368947')],
    form_opts=['Neue Küche', 'Möbel nach Maß', 'Aufmaß vor Ort', 'Umbau / Erweiterung', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Wir melden uns persönlich, gern auch für einen Termin bei Ihnen vor Ort.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Sprechen Sie <em>mit uns.</em>', kt_p='Küchenstudio: 04472 947120 · Möbelbau: 04472 947121 · mobil 0173 2368947.',
    vars='--bg:#fff;--ink:#22262a;--mute:#51585F;--p:#E8711A;--p-ink:#fff;--a:#E8711A;--a-ink:#fff;--dk:#3a2416;--s:#fff;--s2:#fbf6ef;--fh:"Montserrat",system-ui,sans-serif;--fb:"Work Sans",system-ui,sans-serif;--r:6px;--r2:10px;--br:6px;--mq-bg:#854F2C;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#22262a;--logo-h:52px;--ft-bg:#2b1b10;--hx-ar:4/3;--hx-r:10px',
    css='''
.hx h1,.h2{font-weight:800;letter-spacing:-.02em;line-height:1.05}.hx h1 em{display:block;color:#E8711A;font-style:normal}.h2 em{font-style:normal;color:#E8711A}.dk .h2 em{color:#F2A224}
.hx .pic{border:6px solid #fff;box-shadow:0 30px 60px rgba(0,0,0,.25)}.hx .gl{border-left:5px solid #F2A224}
.mq.zw span{font-family:var(--fh);font-weight:700}.alt{background:var(--s2)}.sv .row div{border-top:4px solid #F2A224}
#inhaber figure{max-width:150px;justify-self:center;border-radius:50%;overflow:hidden}#inhaber figcaption{display:none}#inhaber figure img{object-position:50% 20%}
.ft img{background:#fff;padding:8px 12px;border-radius:8px;height:56px}''')
S['css2'] = '.hz{--hz-bg:#fbf6ef;--hz-cols:55fr 45fr;--hz-stroke:rgba(232,113,26,.18)}.hz .hz-img{clip-path:polygon(0 0,100% 0,88% 100%,0 100%)}.hz h1 em{display:block;color:#E8711A}#inhaber figure{border-radius:0!important;max-width:220px!important}@media(max-width:900px){.hz .hz-img{clip-path:polygon(0 0,100% 0,100% 88%,0 100%)}}'
S['bot'] = BOT('Nele', 'Ihre Küchen-Lotsin', 'Die Zwei Küchen', S, [
    ['Öffnungszeiten', 'Mo–Fr 10–16 Uhr, samstags nach Vereinbarung.'],
    ['Möbel nach Maß?', 'Ja, Möbelbau Maic Niemann fertigt im eigenen Meisterbetrieb in Lastrup.'],
    ['Aufmaß vor Ort?', 'Ja, wir beraten und messen bei Ihnen zu Hause. Rufen Sie an: 04472 947120.']],
    ['#welten', '#eindruecke', '#leistungen', '#kontakt'])
Z = 'zwei/hi/'
S['img'] = {'logo.png': ('zwei/img/i000.png', 0), 'emo.jpg': (PIX + '9998456.jpg', 0), 'h-pic.jpg': (Z + 'IMG_1128.jpg', 0), 'h-moebel.jpg': (Z + 'PHOTO-2023-03-15-14-06-46.jpg', 1400),
    'w-kueche.jpg': (Z + 'IMG_6975.jpg', 0), 'w-moebel.jpg': (Z + 'IMG_5893.jpg', 0),
    'g1.jpg': (Z + '2018-03-01-PHOTO-00000609.jpg', 0), 'g2.jpg': (Z + 'IMG_1994.jpg', 0), 'g3.jpg': (Z + 'PHOTO-2023-03-15-14-06-46.jpg', 900), 'g4.jpg': (Z + 'IMG_7085.jpg', 0),
    'g5.jpg': (Z + 'IMG_4939.jpg', 0), 'g6.jpg': (Z + 'IMG_7326.jpg', 0), 'g7.jpg': (Z + 'IMG_7249.jpg', 0), 'g8.jpg': (Z + 'IMG_3150.jpg', 0),
    'inhaber.jpg': (Z + 'mn.jpg', 0)}
S['body'] = b_zwei
