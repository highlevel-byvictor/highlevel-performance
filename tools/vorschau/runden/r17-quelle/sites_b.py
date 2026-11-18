"""Runde 17 · Teil B: KS Küchenservice Suty, Prima-Küchen, Küchen-Schilling, Hartwig & Timphus, Tischlerei Meyknecht."""
from common import *
from sites_a import V
SITES = {}
DKHD = ';--hd-bg:{c};--hd-ink:#fff'

# ───────────── 5. KS Küchenservice Suty, Preußisch Oldendorf ─────────────
def b_suty(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], side='l', pos={'h1.jpg': '22% 40%'}, alt='Krzysztof und Izabela Suty',
        ubar=[('Chefsache', 'Beratung durch den Inhaber'), ('3 Jahrzehnte', 'in der Möbelbranche'), ('Familienbetrieb', 'Krzysztof und Izabela Suty')],
        ey='KS Küchenservice Suty · Preußisch Oldendorf',
        h1='Bei uns ist die Beratung <em>Chefsache.</em>',
        sub='Krzysztof Suty ist gelernter Ingenieur für Holztechnologie und seit drei Jahrzehnten in der Möbelbranche. Zusammen mit seiner Frau Izabela berät er Sie persönlich, rund um Küchen, Einrichtung und Möbel.'))
        + vgrid('videos', 'Aus unserem Studio', 'Sehen Sie <em>selbst.</em>', 'Unsere Videos zeigen, was Sie bei uns erwartet.', [
            ('Video 1 ansehen', 'yt', '2f5oxOT5_0I', 'v1.jpg'), ('Video 2 ansehen', 'yt', 'DHNflo1iuTw', 'v2.jpg'), ('Video 3 ansehen', 'yt', 'KM1XmFxW6Es', 'v3.jpg')], 'dk')
        + svc('leistungen', 'Unsere Leistungen', 'Das können Sie <em>von uns erwarten.</em>', 'Viel Herzblut und Engagement für jeden kleinen oder großen Küchentraum.', [
            ('Termine nach Ihrem Zeitplan', 'Individuelle Beratungstermine, die zu Ihrem Zeitplan passen.'),
            ('Beratung vor Ort', 'Persönliche Beratung und Ausmessen bei Ihnen zu Hause.'),
            ('Günstige Einkaufspreise', 'Unsere Einkaufspreise kommen Ihnen zugute.'),
            ('Handwerker-Rundum-Service', 'Wir koordinieren Elektriker, Fliesenleger, Installateure und Schreiner.')])
        + scroller('ausstellung', 'Unsere Ausstellung', 'Küchen sind <em>Orte zum Leben.</em>', 'Ob puristisch-moderne Wohnküche, romantische Landhausküche oder preiswerte kleine Singleküche: Unsere Ausstellung zeigt verschiedene Stile und Trends.', [
            ('Ausstellung', 'k1.jpg', 'Unweit von Minden, Osnabrück und Bünde.', '50% 50%'),
            ('Dunkel und edel', 'k2.jpg', 'Schwarz mit Holz kombiniert.', '50% 50%'),
            ('Mit Kochinsel', 'k3.jpg', 'Der Treffpunkt der Familie.', '50% 50%'),
            ('Hell und wohnlich', 'k4.jpg', 'Viel Stauraum, ruhige Fronten.', '50% 50%'),
            ('Farbe wagen', 'k5.jpg', 'Akzente, die gute Laune machen.', '50% 50%')], 'alt')
        + reviews(s, ['Herr Suty hat sich bei der Beratung sehr viel Zeit genommen und hatte ein gutes Auge fürs Detail. Die Küche passt perfekt, bis in die letzte Ecke.',
                      'Ein guter Freund hat uns KS Küchenservice empfohlen. Es war die richtige Entscheidung, die Kommunikation war freundlich und unkompliziert.',
                      'Auch bei unseren vielen Sonderwünschen hatte Herr Suty immer gute Ideen für die Umsetzung.',
                      'Schon das zweite Mal bei KS, und das Ergebnis ist genauso gut wie beim ersten Mal. Termintreue und Liebe zum Detail.'])
        + contact(s) + footer(s))

S = SITES['suty'] = site(
    slug='ks-kuechenservice-suty-preussisch-oldendorf', firma='KS Küchenservice Suty', web='ks-kuechenservice.de', fonts='r9goodlife',
    title='KS Küchenservice Suty – Küchenstudio in Preußisch Oldendorf', desc='KS Küchenservice Suty in Preußisch Oldendorf: Beratung durch den Inhaber, Ausmessen vor Ort, Handwerker-Rundum-Service.',
    tel='05742 5039029', tel_i='+4957425039029', mail='info@suty.de', adresse='Berliner Str. 15, 32361 Preußisch Oldendorf', google=('5,0', 13),
    cta='Termin vereinbaren', nav=[('Videos', 'videos'), ('Leistungen', 'leistungen'), ('Ausstellung', 'ausstellung'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '11:00 – 17:00'), ('Außerhalb', 'Termine nach Vereinbarung')],
    form_opts=['Neue Küche', 'Beratung bei mir zu Hause', 'Küchenmodernisierung', 'Sonstiges'],
    form_h3='Termin vereinbaren', form_p='Terminwünsche sind Montag bis Freitag zwischen 10 und 17 Uhr möglich. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Besuchen Sie uns <em>in Preußisch Oldendorf.</em>', kt_p='Lassen Sie sich gern von uns überzeugen. Wir freuen uns auf Ihren Besuch.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#1c1c2a', mute='#56566a', p='#E3312A', pi='#fff', dk='#2A2A3D', s2='#f2f2f6', fh='"Outfit",system-ui,sans-serif', fb='"Open Sans",system-ui,sans-serif', lh=46, ft='#1c1c2a') + DKHD.format(c='#2A2A3D'),
    css='''.h2{font-weight:700;letter-spacing:-.02em;line-height:1.06}.h2 em{font-style:normal;color:#E3312A}.alt{background:var(--s2)}.vg.dk{background:#2A2A3D;color:#fff}.vg.dk .lead,.vg.dk small{color:rgba(255,255,255,.8)}
.sv .row div{border-top:4px solid #E3312A}.hd .nav a{color:#fff}''')
S['css2'] = '.hz{--hz-bg:#fff;--hz-cols:50fr 50fr}.hz h1{font-weight:700;font-size:clamp(36px,4.4vw,70px)}.hz h1 em{color:#E3312A}.hz .ey{color:#E3312A}'
S['bot'] = BOT('Iza', 'Ihre Küchen-Lotsin', 'KS Küchenservice Suty', S, [
    ['Öffnungszeiten', 'Mo–Fr 11–17 Uhr. Weitere Termine gerne nach Vereinbarung.'],
    ['Kommen Sie zu mir nach Hause?', 'Ja, wir beraten und messen persönlich bei Ihnen vor Ort aus.'],
    ['Wer koordiniert die Handwerker?', 'Wir. Elektriker, Fliesenleger, Installateure und Schreiner stimmen wir für Sie ab.']],
    ['#videos', '#leistungen', '#ausstellung', '#kontakt'])
S['img'] = {'logo.png': ('suty/img/i000.png', 0), 'h1.jpg': ('suty/img/i001.jpg', 0), 'h2.jpg': ('suty/img/i032.jpg', 2000), 'h3.jpg': ('suty/img/i035.jpg', 0),
    'v1.jpg': ('suty/img/i037.jpg', 1200), 'v2.jpg': ('suty/img/i034.jpg', 1200), 'v3.jpg': ('suty/img/i041.jpg', 1200),
    'k1.jpg': ('suty/img/i038.jpg', 1300), 'k2.jpg': ('suty/img/i036.jpg', 1300), 'k3.jpg': ('suty/img/i039.jpg', 1300), 'k4.jpg': ('suty/img/i031.jpg', 1300), 'k5.jpg': ('suty/img/i008.jpg', 1300)}
S['body'] = b_suty

# ───────────── 6. Prima-Küchen, Rahden ─────────────
def b_prima(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h3.jpg'], big='1999',
        ubar=[('Seit 1999', 'Einbauküchen und Geräte'), ('Fast alle', 'Preislagen'), ('2 auf 5 Jahre', 'Garantie auf Wunsch')],
        ey='Prima-Küchen · Rahden',
        h1='Das Küchenstudio <em>mit dem besonderen Service.</em>',
        sub='Seit 1999 verkaufen wir Einbauküchen und Einbauelektrogeräte in fast allen Preislagen. Mit umfassender Beratung, Aufmaß vor Ort und fairen Preisen.'))
        + marquee(['Burger-Küchen', 'Bauformat-Küchen', 'Küchenumbauten', 'Arbeitsplatten-Austausch', 'Elektrogeräte-Austausch', 'Finanzierung möglich'], 'pm')
        + svc('service', 'Bei uns erhalten Sie', 'Alles für <em>Ihre neue Küche.</em>', 'Ihr Partner des Vertrauens, seit 1999.', [
            ('Umfassende Beratung', 'Mit computerunterstützter Planung, bei uns im Studio.'),
            ('Aufmaß vor Ort', 'Wir ermitteln die Raummaße und Problembereiche bei Ihnen zu Hause.'),
            ('Anlieferung und Montage', 'Auf Wunsch liefern und montieren wir Ihre Küche.'),
            ('Finanzierung', 'Ratenzahlung ist möglich. Sprechen Sie uns an.')])
        + duo('marken', 'Unsere Küchen', 'Zwei Hersteller, <em>viele Möglichkeiten.</em>', 'Zu Fronten, Korpus, Griffen und Arbeitsplatten erhalten Sie bei uns alle Unterlagen, um sie in Ruhe anzuschauen.', [
            ('Hersteller', 'Burger-Küchen', 'd1.jpg', 'Fronten, Unterschränke, Hängeschränke und Griffe in großer Auswahl.', ['Fronten', 'Korpus', 'Arbeitsplatten'], 'Burger-Küche anfragen'),
            ('Hersteller', 'Bauformat-Küchen', 'd2.jpg', 'Unterschränke in zwei Höhen, dazu Ausstattung, Arbeitsplatten und Rückwände.', ['780 mm + 715 mm', 'Ausstattung', 'Rückwände'], 'Bauformat-Küche anfragen')], 'alt')
        + promo('umbau', 'umbau.jpg', 'Auch das machen wir', 'Küchenumbau statt <em>neuer Küche.</em>',
                'Sie ziehen um oder Ihre Küche braucht ein Update? Wir ergänzen und bauen bestehende Küchen um, zum Beispiel für eine neue Wohnung.',
                ['Küchenergänzungen und Küchenumbauten', 'Austausch von Arbeitsplatten', 'Austausch von Elektrogeräten'], 'Umbau anfragen')
        + reviews(s, ['Der gesamte Ablauf war perfekt. Großes Lob an den Monteur: unglaublich sauber, schnell und mit Blick fürs Detail.',
                      'Beratung und Planung waren sehr gut, per WhatsApp und im Studio. Ich hatte nie das Gefühl, dass mir etwas verkauft werden soll, das ich nicht brauche.',
                      'Sehr kompetente und freundliche Beratung durch Herrn Pieper. Ich bin begeistert von meiner neuen Küche.',
                      'Die Küche ist perfekt eingebaut, alles sauber und ordentlich. Freundlich und zuverlässig.'])
        + contact(s) + footer(s))

S = SITES['prima'] = site(
    slug='prima-kuechen-rahden', firma='Prima-Küchen', web='prima-kuechen.de', fonts='r16meppens',
    title='Prima-Küchen Rahden – das Küchenstudio mit dem besonderen Service', desc='Prima-Küchen in Rahden: Einbauküchen und Einbaugeräte seit 1999, Burger- und Bauformat-Küchen, Küchenumbauten, Finanzierung möglich.',
    tel='05771 608211', tel_i='+495771608211', adresse='Mindener Str. 62, 32369 Rahden', google=('4,8', 36),
    cta='Beratung anfragen', nav=[('Service', 'service'), ('Küchen', 'marken'), ('Umbau', 'umbau'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 18:00'), ('Sa', '9:00 – 12:30')],
    form_opts=['Neue Küche', 'Küchenumbau / Ergänzung', 'Arbeitsplatte tauschen', 'Elektrogerät tauschen', 'Finanzierung', 'Sonstiges'],
    form_h3='Beratung anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Rufen Sie uns <em>gerne an.</em>', kt_p='Sollten Sie Fragen haben, erreichen Sie uns unter 05771 608211. Öffnungszeiten laut Google.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#333', mute='#666', p='#D98F00', pi='#fff', dk='#3b3b3b', s2='#faf5ea', fh='"Open Sans",system-ui,sans-serif', fb='"Open Sans",system-ui,sans-serif', lh=42, ft='#2b2b2b') + DKHD.format(c='#3b3b3b'),
    css='''.h2{font-weight:800;letter-spacing:-.02em;line-height:1.08}.h2 em{font-style:normal;color:#D98F00}.alt{background:var(--s2)}.mq.pm span{font-weight:700;letter-spacing:.04em}
.sv .row div{border-top:4px solid #EDB059}.hd .nav a{color:#fff}''')
S['css2'] = '.hz{--hz-bg:#3b3b3b;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(237,176,89,.25);--hz-line:rgba(255,255,255,.2)}.hz h1{font-size:clamp(34px,4.2vw,66px)}.hz h1 em{color:#EDB059}.hz .ey{color:#EDB059}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hz .chip{background:rgba(255,255,255,.1);color:#fff}'
S['bot'] = BOT('Paula', 'Ihre Küchen-Lotsin', 'Prima-Küchen', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–18 Uhr, Sa 9–12:30 Uhr (Angaben laut Google).'],
    ['Ist Ratenzahlung möglich?', 'Ja, Finanzierung und Ratenzahlung sind möglich.'],
    ['Bauen Sie auch Küchen um?', 'Ja, wir ergänzen und bauen Küchen um und tauschen Arbeitsplatten und Elektrogeräte.']],
    ['#service', '#marken', '#umbau', '#kontakt'])
S['img'] = {'logo.png': ('prima/img/i000.png', 0), 'h1.jpg': ('prima/img/i003.jpg', 0), 'h2.jpg': ('prima/img/i004.jpg', 0), 'h3.jpg': ('prima/img/i039.jpg', 0),
    'd1.jpg': ('prima/img/i004.jpg', 0), 'd2.jpg': ('prima/img/i039.jpg', 0), 'umbau.jpg': ('prima/img/i067.jpg', 0)}
S['body'] = b_prima

# ───────────── 7. Küchen-Schilling, Rödinghausen ─────────────
def b_schilling(s):
    return (hd(s, False) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'],
        ey='Küchen-Schilling · Ihr Küchenstudio in Rödinghausen',
        h1='Style, Komfort, <em>Qualität.</em>',
        sub='Hohe Qualität, vorbildlicher Kundenservice, freundliche Beratung und faire Preise. Bei Küchen-Schilling sind Sie in erfahrenen Händen.',
        ubar=[('3-D-Planung', 'am Computer'), ('Aufmaß', 'bei Ihnen zu Hause'), ('Handwerker', 'vermittelt und koordiniert')]))
        + marquee(['Ballerina', 'Häcker', 'Leicht', 'nobilia', 'Miele', 'Neff', 'Siemens', 'AEG', 'BORA', 'berbel'], 'sm')
        + svc('leistungen', 'Unsere Leistungen', 'Service von Anfang <em>bis Ende.</em>', 'Sie werden unsere Liebe zum Detail und unser Qualitätsbewusstsein spüren.', [
            ('Persönliche Beratung', 'Wir ermitteln gemeinsam Ihren Bedarf und beraten umfassend und fachmännisch.'),
            ('Aufmaß und 3-D-Planung', 'Aufmaß bei Ihnen, Planung am Computer.'),
            ('Handwerker-Koordination', 'Wir vermitteln und koordinieren Handwerker für alle Bereiche.'),
            ('Montage', 'Ausführung der handwerklichen Arbeiten und Montage aus einer Hand.')])
        + gallery('kuechen', 'Küchenstile', 'Eine Küche braucht <em>Charakter.</em>', [
            ('g1.jpg', 'a', '50% 50%'), ('g2.jpg', 'b', '50% 50%'), ('g3.jpg', 'c', '50% 50%')], 'alt')
        + faq('Warum Küchen-Schilling?', 'Vorteile, die nur ein <em>Fachhändler vor Ort</em> bietet.', [
            ('Top Marken, Top Service', 'Wir arbeiten ausschließlich mit marktführenden Herstellern zusammen und beraten Sie umfassend, zielgerichtet und fachmännisch.'),
            ('Regional und persönlich', 'Als Ihr regionaler Fachhändler schätzen wir das Vertrauen unserer Kunden. Lehnen Sie sich zurück und genießen Sie das Ergebnis.'),
            ('Hauswirtschaftsraum und mehr', 'Wir planen auch Hauswirtschaftsräume, Speisekammern und Möbel für weitere Räume.'),
            ('Finanzierung', 'Sprechen Sie uns auf Finanzierungsmöglichkeiten an.')])
        + reviews(s, ['Die Beratung war professionell, persönlich und voller guter Ideen. Von der 3D-Planung bis zur Montage lief alles stressfrei.',
                      'Nach dem ersten Termin bei uns zu Hause hatte Herr Schilling schon mehrere Ideen. Nichts wirkte aufgedrängt, es war einfach ehrlich.',
                      'Das war unsere dritte Küche von Schilling, und wir sind mehr als zufrieden. Zuverlässig und reibungslos.',
                      'Sehr gute Beratung, tolle Ideen, und die Monteure waren spitze. Wir haben schon die zweite Küche bestellt.'])
        + contact(s) + footer(s))

S = SITES['schilling'] = site(
    slug='kuechen-schilling-roedinghausen', firma='Küchen-Schilling GmbH', web='kuechen-schilling.com', fonts='r13opel',
    title='Küchen-Schilling – Ihr Küchenstudio in Rödinghausen', desc='Küchen-Schilling in Rödinghausen: persönliche Beratung, Aufmaß, 3-D-Planung, Handwerker-Koordination und Montage.',
    tel='05226 592282', tel_i='+495226592282', mail='info@kuechen-schilling.com', adresse='Rennerskamp 16, 32289 Rödinghausen', google=('4,9', 36),
    cta='Beratungstermin vereinbaren', nav=[('Leistungen', 'leistungen'), ('Küchen', 'kuechen'), ('Warum wir', 'vorteile'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 13:00, 14:00 – 18:00'), ('Sa', 'nach Vereinbarung')],
    form_opts=['Neue Küche', 'Hauswirtschaftsraum', 'Kundendienst', 'Finanzierung', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Nennen Sie uns Ihren Wunschtermin. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Besuchen Sie <em>unser Küchenstudio.</em>', kt_p='Wenn Sie Fragen haben, stehen wir Ihnen gern Rede und Antwort. Öffnungszeiten laut Google.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#1b1b1b', mute='#555', p='#8C6B45', pi='#fff', dk='#222', s2='#f3f1ee', fh='"Outfit",system-ui,sans-serif', fb='"Inter",system-ui,sans-serif', lh=50, ft='#161616') + DKHD.format(c='#222'),
    css='''.hs h1,.h2{font-weight:600;letter-spacing:-.025em;line-height:1.04}.hs h1{font-size:clamp(44px,7vw,110px)}.hs h1 em,.h2 em{font-style:normal;color:#C9A57A}.h2 em{color:#8C6B45}
.mq.sm span{font-family:var(--fh);font-weight:600;letter-spacing:.06em;text-transform:uppercase;font-size:15px}.alt{background:var(--s2)}.sv .row div{border-top:2px solid #8C6B45}
.gl .grid{grid-template-columns:repeat(3,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:16/10}.hd .nav a{color:#fff}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr}}''')
S['bot'] = BOT('Selma', 'Ihre Küchen-Lotsin', 'Küchen-Schilling', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–13 und 14–18 Uhr (Angaben laut Google). Weitere Termine nach Vereinbarung.'],
    ['Messen Sie bei mir aus?', 'Ja, das Aufmaß machen wir bei Ihnen zu Hause, danach planen wir in 3-D am Computer.'],
    ['Koordinieren Sie Handwerker?', 'Ja, wir vermitteln und koordinieren Handwerker für alle Bereiche.']],
    ['#leistungen', '#kuechen', '#vorteile', '#kontakt'])
S['img'] = {'logo.png': ('schilling/img/i000.png', 0), 'h1.jpg': ('schilling/img/i002.jpg', 0), 'h2.jpg': ('schilling/img/i001.jpg', 0), 'h3.jpg': ('schilling/img/i003.jpg', 0),
    'g1.jpg': ('schilling/img/i053.jpg', 0), 'g2.jpg': ('schilling/img/i054.jpg', 0), 'g3.jpg': ('schilling/img/i055.jpg', 0)}
S['body'] = b_schilling

# ───────────── 8. Küchen Zentrum Hartwig & Timphus, Steinfeld ─────────────
def b_timphus(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='12',
        ubar=[('12 Mitarbeiter', 'qualifiziert und motiviert'), ('Aus Steinfeld', 'inhabergeführt'), ('3 Hersteller', 'Ballerina, Bauformat, Burger')],
        ey='Küchenzentrum Hartwig & Timphus · Steinfeld im Landkreis Vechta',
        h1='Küchen <em>aus dem Norden.</em>',
        sub='Unser inhabergeführtes Unternehmen aus Steinfeld beschäftigt derzeit 12 Mitarbeiter. Wir finden für Sie die perfekte Küche und den passenden Hauswirtschaftsraum.'))
        + spot('spot', 'Quooker im Küchenzentrum', 'Kochendes Wasser <em>direkt aus dem Hahn.</em>', 'Kein Wasserkocher, kein Warten. Den Quooker können Sie sich bei uns in Steinfeld vorführen lassen.', 'tv.mp4', 'tv.jpg', 'tq')
        + spot('neff', 'NEFF im Küchenzentrum', 'Kochen aus <em>Leidenschaft.</em>', 'Auch den Kampagnenfilm von NEFF zeigen wir auf unserer Seite. Die Geräte sehen Sie bei uns in der Ausstellung.', 'neff.mp4', 'neff.jpg', 'tn')
        + scroller('kuechen', 'Unsere Traumküchen', 'Große Auswahl, <em>Ihr Stil.</em>', 'Klassisch, Landhaus oder modern, farbig, Holz oder Weiß: Entdecken Sie unsere Küchen-Vielfalt.', [
            ('Modern', 'k1.jpg', 'Klare Linien, viel Licht.', '50% 50%'),
            ('Klassisch', 'k2.jpg', 'Zeitlos und hell.', '50% 50%'),
            ('Landhaus', 'k3.jpg', 'Gemütlich mit Rahmenfronten.', '50% 50%'),
            ('Holz', 'k4.jpg', 'Warme Töne, wohnlich.', '50% 50%'),
            ('Farbig', 'k5.jpg', 'Mut zur Farbe.', '50% 50%'),
            ('Weiß', 'k6.jpg', 'Hell und freundlich.', '50% 50%')])
        + panels('hwr', 'Hauswirtschaftsräume', 'Mit den Profis zum <em>Traum-Hauswirtschaftsraum.</em>', 'Einrichtungsideen für den Raum, der im Alltag am meisten leisten muss.', [
            ('Garderobe', 'w1.jpg', 'Jacken, Mäntel und Schuhe ordentlich verstaut.', '50% 50%'),
            ('Vorräte', 'w2.jpg', 'Getränke und Vorräte griffbereit.', '50% 50%'),
            ('Putzschrank', 'w3.jpg', 'Besen, Sauger und Reiniger haben ihren Platz.', '50% 50%'),
            ('Wäsche', 'w4.jpg', 'Waschmaschine und Trockner auf Arbeitshöhe.', '50% 50%')], 'alt')
        + reviews_ns(s, ['Wir haben hier unsere neue Ballerina-Küche gekauft und sind rundum zufrieden. Beratung und Montage waren zuverlässig, schnell und sauber.',
                         '2009 hat Herr Timphus eine tolle Küche für uns geplant, an der wir bis heute Freude haben. Jederzeit wieder.',
                         'Tolle Ideen in der Planung und zuverlässige Mitarbeiter. Saubere Arbeit.'])
        + contact(s) + footer(s))

S = SITES['timphus'] = site(
    slug='kuechenzentrum-hartwig-timphus-steinfeld', firma='Küchenzentrum Hartwig & Timphus', web='kuechenzentrum.net', fonts='r12bsb',
    title='Küchenzentrum Hartwig & Timphus – Küchen aus dem Norden, Steinfeld', desc='Küchenzentrum Hartwig & Timphus in Steinfeld: Küchen von Ballerina, Bauformat und Burger, Hauswirtschaftsräume, 12 Mitarbeiter.',
    tel='05492 962900', tel_i='+495492962900', adresse='Bergmannstraße 25, 49439 Steinfeld (Oldenburg)',
    cta='Termin vereinbaren', nav=[('Video', 'spot'), ('Küchen', 'kuechen'), ('Hauswirtschaftsräume', 'hwr'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '8:00 – 18:00'), ('Sa', '9:00 – 12:00'), ('So / Feiertage', 'geschlossen')],
    form_opts=['Neue Küche', 'Hauswirtschaftsraum', 'Quooker / Geräte', 'Sonstiges'],
    form_h3='Termin vereinbaren', form_p='Wir beraten Sie gerne. Nehmen Sie jetzt unverbindlich Kontakt auf.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ihr Interesse <em>ist geweckt?</em>', kt_p='Rufen Sie uns an oder kommen Sie in unserer Ausstellung in Steinfeld vorbei.',
    vars=V.format(ink='#111', mute='#4d4b4b', p='#E2001A', pi='#fff', dk='#111', s2='#f4f4f1', fh='"Sora",system-ui,sans-serif', fb='"Inter",system-ui,sans-serif', lh=70, ft='#000') + DKHD.format(c='#000'),
    css='''.h2{font-weight:700;letter-spacing:-.03em;line-height:1.06}.h2 em{font-style:normal;color:#E2001A}.alt{background:var(--s2)}.hd .nav a{color:#fff}.mcall a:last-child{background:#FFE600;color:#111}''')
S['css2'] = '.hz{--hz-bg:#111;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(255,230,0,.22);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:700}.hz h1 em{color:#FFE600}.hz .ey{color:#FFE600}.hz .btn-a{background:#FFE600;color:#111}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.sp16{--sp-bg:#FFE600;--sp-ink:#111;--sp-ey:#E2001A}.sp16.tn{--sp-bg:#111;--sp-ink:#fff;--sp-ey:#FFE600}.sp16 .h2 em{color:#E2001A;font-style:normal}'
S['bot'] = BOT('Tilda', 'Ihre Küchen-Lotsin', 'dem Küchenzentrum Hartwig & Timphus', S, [
    ['Öffnungszeiten', 'Mo–Fr 8–18 Uhr, Sa 9–12 Uhr. Sonn- und feiertags geschlossen.'],
    ['Welche Hersteller führen Sie?', 'Ballerina, Bauformat und Burger.'],
    ['Planen Sie auch Hauswirtschaftsräume?', 'Ja, wir beraten Sie gerne zu Ihrem Hauswirtschaftsraum.']],
    ['#spot', '#kuechen', '#hwr', '#kontakt'])
S['img'] = {'neff.mp4': ('/home/claude/r17raw/timphus/vid/neff_web.mp4', 0), 'neff.jpg': ('/home/claude/r17raw/timphus/vid/neff.jpg', 0), 'tv.mp4': ('/home/claude/r17raw/timphus/vid/tv_web.mp4', 0), 'tv.jpg': ('/home/claude/r17raw/timphus/vid/poster.jpg', 0),
    'logo.png': ('timphus/img/i004.png', 0), 'h1.jpg': ('timphus/img/i016.jpg', 0), 'h2.jpg': ('timphus/img/i017.jpg', 0), 'h3.jpg': ('timphus/img/i019.jpg', 0),
    'k1.jpg': ('timphus/img/i097.jpg', 1300), 'k2.jpg': ('timphus/img/i018.jpg', 1300), 'k3.jpg': ('timphus/img/i120.jpg', 1300), 'k4.jpg': ('timphus/img/i099.jpg', 1300), 'k5.jpg': ('timphus/img/i096.jpg', 1300), 'k6.jpg': ('timphus/img/i121.jpg', 1300),
    'w1.jpg': ('timphus/img/i104.jpg', 0), 'w2.jpg': ('timphus/img/i106.jpg', 0), 'w3.jpg': ('timphus/img/i109.jpg', 0), 'w4.jpg': ('timphus/img/i107.jpg', 0)}
S['body'] = b_timphus

# ───────────── 9. Küchen Tischlerei Jürgen Meyknecht, Hopsten ─────────────
def b_meyknecht(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='2005',
        ubar=[('Über 30 Jahre', 'Tischler-Erfahrung'), ('Seit 2005', 'Küchenplanung und Montage'), ('Chefsache', 'Beratung durch Jürgen Meyknecht')],
        ey='Küchen Tischlerei Jürgen Meyknecht · Hopsten',
        h1='Die erste Adresse für <em>individuelle Einbauküchen.</em>',
        sub='Jürgen Meyknecht ist seit über 30 Jahren gelernter Tischler. Seit 2005 planen, montieren und modernisieren wir Küchen und bauen Möbel nach Maß.'))
        + vgrid('videos', 'Videos von unserer Seite', 'Unsere Partner <em>im Film.</em>', 'Diese Videos zeigen wir auch auf unserer bisherigen Seite.', [
            ('systemceram: Feinsteinzeug aus dem Westerwald', 'yt', 'Zf6MKnwsgSc', 'yt1.jpg'), ('Franke: Box Center', 'yt', '986ScGDUqwo', 'yt2.jpg')], 'alt')
        + story('team', 'Über uns', 'Küche vom Tischler: <em>geplant und gebaut aus einer Hand.</em>', [
            'Wir sind Ihr professioneller Partner für Küchen und Möbel nach Maß. Als Partner von GK Gute Küchen ist die Beratung bei uns Chefsache, und erstklassiger Service selbstverständlich.',
            'Wir beweisen Ihnen, dass beste Qualität von Küchen und Möbeln zum gleichen Preis oder sogar günstiger zu haben ist, als Sie vermuten.'], 'team.jpg', 'Das Team der Tischlerei Meyknecht bei der Planung', cls='hb')
        + promo('modernisierung', 'mod.jpg', 'Küchenmodernisierung', 'Frischer Wind <em>für Ihre Küche.</em>',
                'Eine in die Jahre gekommene Küche kann durch den Austausch einzelner Teile wieder in neuem Glanz erscheinen. So erreichen Sie eine optische Aufwertung, ohne alles neu zu kaufen.',
                ['Neue Arbeitsplatte', 'Neue Fronten oder Auszüge', 'Neue Geräte passgenau eingebaut'], 'Modernisierung anfragen', 'alt')
        + svc('leistungen', 'Leistungen', 'Qualität <em>setzt sich durch.</em>', 'Vom ersten Planungstermin bis zum letzten Handgriff.', [
            ('Küchenplanung', 'Persönlicher, unverbindlicher Planungstermin in unserer Ausstellung.'),
            ('Küchenmontage', 'Sorgfältig und millimetergenau durch unser eigenes Team.'),
            ('Küchenmodernisierung', 'Einzelne Teile tauschen statt alles neu kaufen.'),
            ('Tischlerarbeiten', 'Möbel nach Maß aus der eigenen Werkstatt.')])
        + story('tischler', 'Tischlerarbeit im Kundenauftrag', 'Esstisch in <em>Eiche massiv.</em>', [
            'Durchgehende Lamellen, die Tischfüße sichtbar eingearbeitet, auf Wunsch der Kundin im Querverlauf zur Tischplatte. Ein schönes Möbelstück mit viel Platz für Abende mit Freunden.'], 'tisch.jpg', 'Esstisch Eiche massiv aus unserer Werkstatt', rev=True, cls='tw')
        + reviews(s, ['Von der ersten Planung bis zur Montage lief alles reibungslos. Der Einbau war sorgfältig, schnell und auf den Millimeter genau.',
                      'Projekt „Verjüngung einer 20 Jahre alten Küche“: Jürgen und Irene standen uns mit Rat und Tat zur Seite. Alles lief glatt, sogar schneller als geplant.',
                      'Es war die beste Entscheidung, diese Tischlerei zu nehmen. Sie denken voraus, planen verantwortungsbewusst und gehen auch an unkonventionelle Lösungen heran.',
                      'Die Tischlerarbeiten und unsere Einbauschränke nach Maß wurden pünktlich und zuverlässig fertig. Die Arbeit des Teams war tadellos.'])
        + contact(s) + footer(s))

S = SITES['meyknecht'] = site(
    slug='kuechen-tischlerei-meyknecht-hopsten', firma='Küchen Tischlerei Jürgen Meyknecht', web='kuechen-meyknecht.de', fonts='r9medifit',
    title='Küchen Tischlerei Meyknecht – individuelle Einbauküchen aus Hopsten', desc='Tischlerei Jürgen Meyknecht in Hopsten: Küchenplanung, Montage, Küchenmodernisierung und Möbel nach Maß.',
    tel='05458 933806', tel_i='+495458933806', adresse='Gärtnereistraße 1, 48496 Hopsten', google=('4,9', 14),
    cta='Planungstermin anfragen', nav=[('Videos', 'videos'), ('Über uns', 'team'), ('Modernisierung', 'modernisierung'), ('Leistungen', 'leistungen'), ('Tischlerei', 'tischler'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '7:30 – 12:00, 14:00 – 17:00'), ('Sa', 'nach Vereinbarung')],
    form_opts=['Neue Küche', 'Küchenmodernisierung', 'Möbel nach Maß', 'Sonstiges'],
    form_h3='Planungstermin anfragen', form_p='Persönlich und unverbindlich. Wir melden uns so schnell wie möglich, um Ihren Termin zu bestätigen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Nur einen Klick von Ihrer <em>neuen Küche entfernt.</em>', kt_p='Starten Sie Ihre unverbindliche Planungsterminanfrage. Öffnungszeiten laut Google.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#181716', mute='#58585a', p='#0C4093', pi='#fff', dk='#0C4093', s2='#eef4fb', fh='"Poppins",system-ui,sans-serif', fb='"Inter",system-ui,sans-serif', lh=58, ft='#0a2f6e'),
    css='''.h2{font-weight:700;letter-spacing:-.02em;line-height:1.08}.h2 em{font-style:normal;color:#0C4093}.alt{background:var(--s2)}.sv .row div{border-top:4px solid #00A4E3}.promo .tag{background:#00A4E3;color:#fff}
.st.hb figure img{aspect-ratio:3637/2424;object-fit:cover;height:auto}.st.hb .w{grid-template-columns:1.15fr 1fr}.st.tw figure{max-width:420px;justify-self:center}.ft img{background:#fff;padding:8px 12px;height:60px}
@media(max-width:820px){.st.hb .w{grid-template-columns:1fr}}''')
S['css2'] = '.hz{--hz-bg:#0C4093;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.86);--hz-stroke:rgba(0,164,227,.35);--hz-line:rgba(255,255,255,.22)}.hz h1{font-weight:700;font-size:clamp(34px,4.1vw,64px)}.hz h1 em{color:#7fd6f7}.hz .ey{color:#7fd6f7}.hz .btn-a{background:#00A4E3}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hz .chip{background:rgba(255,255,255,.12);color:#fff}'
S['bot'] = BOT('Marta', 'Ihre Küchen-Lotsin', 'der Tischlerei Meyknecht', S, [
    ['Öffnungszeiten', 'Mo–Fr 7:30–12 und 14–17 Uhr (Angaben laut Google). Planungstermine nach Vereinbarung.'],
    ['Modernisieren Sie auch alte Küchen?', 'Ja, durch den Austausch einzelner Teile erscheint Ihre Küche wieder in neuem Glanz.'],
    ['Bauen Sie Möbel nach Maß?', 'Ja, in unserer Tischlerei fertigen wir Möbel im Kundenauftrag.']],
    ['#team', '#modernisierung', '#leistungen', '#kontakt'])
S['img'] = {'logo.png': ('/home/claude/r17raw/meyknecht/logo.png', 0), 'h1.jpg': ('meyknecht/img/i001.jpg', 2200), 'h2.jpg': ('meyknecht/img/i101.jpg', 2200), 'h3.jpg': ('meyknecht/img/i102.jpg', 2200),
    'yt1.jpg': ('/home/claude/r17raw/meyknecht/yt_Zf6MKnwsgSc.jpg', 0), 'yt2.jpg': ('/home/claude/r17raw/meyknecht/yt_986ScGDUqwo.jpg', 0), 'team.jpg': ('meyknecht/img/i106.jpg', 1800), 'mod.jpg': ('meyknecht/img/i100.jpg', 1500), 'tisch.jpg': ('meyknecht/img/i107.jpg', 1000)}
S['body'] = b_meyknecht
