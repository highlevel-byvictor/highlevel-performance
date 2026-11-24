"""Akquise DM 24.11.2026 · Teil A: Kerber Küchenforum (Osnabrück), Robertus Küchen (Ibbenbüren), Küchenstudio Köse (Oer-Erkenschwick)."""
from common import *
SITES = {}
V = '--bg:#fff;--ink:{ink};--mute:{mute};--p:{p};--p-ink:{pi};--a:{p};--a-ink:{pi};--dk:{dk};--s:#fff;--s2:{s2};--fh:{fh};--fb:{fb};--r:0px;--r2:0px;--br:2px;--mq-bg:{dk};--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:{ink};--logo-h:{lh}px;--ft-bg:{ft};--hp-bg:{s2}'
DKHD = ';--hd-bg:{c};--hd-ink:#fff'
# kantig, aber runde Akzente: Buttons, Chips, Play-Knöpfe rund
RUND = '.btn{border-radius:999px}.chip{border-radius:999px}.play span{border-radius:50%}.tag{border-radius:999px}.mcall a{border-radius:999px}'

# ───────────── 1. Kerber Küchenforum, Osnabrück ─────────────
def b_kerber(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg'], big='400 m²',
        ubar=[('400 m²', 'Ausstellung an der Hannoverschen Straße'), ('Über 40 Jahre', 'Kompetenz rund um Küche und Haushalt'), ('Eigener Kundendienst', 'auch nach dem Kauf')],
        ey='Kerber Küchenforum · Miele-Haus in Osnabrück',
        h1='Ihr Küchen-Experte <em>in Osnabrück.</em>',
        sub='Von der Beratung über die Planung bis zur Montage entsteht bei uns Ihre Wunschküche. Spezialist für Miele-Hausgeräte und Küchen der Marken Rempp und Häcker.'))
        + ytvideo('film', 'Unser Film', 'Design ist <em>unsere Leidenschaft.</em>', 'Thomas Richter zeigt Ihnen das Kerber Küchenforum. Danach wissen Sie, was Sie bei uns erwartet.', 'bVCS7wKjYoU', 'film.jpg', 'dk')
        + story('ueber', 'Seit 2008 inhabergeführt', 'Wir hören zu. Denken weiter. <em>Planen persönlich.</em>', [
            'Seit 2008 führen Christiane und Thomas Richter das KERBER Küchenforum, mit Freude an guter Gestaltung und persönlicher Beratung. Gemeinsam mit unserem Team planen wir Küchen und Einrichtungslösungen, die zu Ihrem Alltag und Ihrem Stil passen.',
            'Bei KERBER sprechen Sie mit uns als Inhabern. Wir beraten Sie, kümmern uns um die Umsetzung und bleiben auch nach dem Kauf Ihre Ansprechpartner.'], 'christiane.jpg', 'Christiane Richter, Küchenplanung und Beratung',
            tl=[('Seit 2008', 'Familie Richter'), ('Mo – Sa', 'geöffnet'), ('Auch abends', 'Termine nach Vereinbarung')])
        + panels('kuechen', 'Premium-Küchen', 'Ihr Stil. Unser Handwerk. <em>Ihre Küche.</em>', 'Charaktervolles Holz, fein lackierte Fronten, ausdrucksstarke Keramik: Gemeinsam wählen wir, was Ihren Stil trifft und Ihren Alltag mitmacht.', [
            ('Rempp und Häcker', 'k1.jpg', 'Exklusives Küchenmöbelprogramm für offene Wohnarchitektur, Mattlack in der Farbe Ihrer Wahl. Dazu unsere Hausmarke inpura by Häcker mit hervorragendem Preis-Leistungs-Verhältnis.', '50% 50%'),
            ('Miele-Geräte', 'k3.jpg', 'Als langjähriger, zertifizierter Miele-Partner helfen wir Ihnen, das passende Gerät zu finden, vom Staubsauger bis zum Dampfgarer.', '50% 50%'),
            ('Planung mit Zeit', 'k4.jpg', 'Für Ihre Küchenplanung gibt es einen eigenen Beratungsbereich. Für Kinder: Spielbereich und eigenes Kinderkino.', '50% 30%')], 'alt')
        + promo('abverkauf', 'abverkauf.jpg', 'Räumungsverkauf', 'Ausstellungsküchen <em>radikal reduziert.</em>',
                'Sonderpreise und Artikel nur so lange verfügbar: Unsere Musterküchen und Ausstellungsgeräte suchen ein liebevolles Zuhause.',
                ['Waschmaschinen, Trockner, Geschirrspüler', 'Kaffeemaschinen, Mikrowellen, Backöfen', 'Ausstellungsküchen aus 400 m² Ausstellung'], 'Jetzt Beratungstermin vereinbaren')
        + svc('service', 'Kerber-Plus-Service', 'Gut. Besser. <em>Kerber.</em>', 'Beim Kauf eines neuen Miele-Gerätes liefern wir nicht nur Technik, sondern auch Komfort.', [
            ('Persönliche Beratung', 'Vor Ort, zu Hause und auch außerhalb der Geschäftszeiten, abgestimmt auf Ihre Bedürfnisse.'),
            ('Lieferung und Montage', 'Aufstellung und Anschluss durch unsere hauseigene Fachkraft, Probelauf und Einweisung.'),
            ('Entsorgung', 'Wir nehmen Verpackung und Altgerät mit.'),
            ('Eigener Kundendienst', 'Ein offenes Ohr für alle Fragen zu Geräten, die Sie bei uns gekauft haben.')], 'dk')
        + story('genusswelt', 'Genusswelt', 'Probieren Sie Ihre Küche <em>vorher aus.</em>', [
            'Bevor Sie sich für Ihren neuen Küchenhelfer entscheiden, können Sie bei uns alle Geräte intensiv ausprobieren. Unser Team zeigt regelmäßig, wie die Küchengeräte funktionieren.',
            'Auch ein Blick zurück lohnt sich: Historische Miele-Geräte erzählen von den Anfängen der Haushaltstechnik. Gleich daneben sehen Sie, was moderne Geräte heute können.'], 'thomas.jpg', 'Thomas Richter, Küchenplanung und Beratung', rev=True)
        + contact(s) + footer(s))

S = SITES['kerber'] = site(
    slug='kerber-kuechenforum-osnabrueck', firma='Kerber GmbH & Co. KG', web='kerber-kuechen.de', fonts='r16hirnstein',
    title='Kerber Küchenforum – Ihr Küchen-Experte in Osnabrück', desc='Kerber Küchenforum in Osnabrück: 400 m² Küchenausstellung, Küchen von Rempp und Häcker, Miele-Hausgeräte, eigener Kundendienst.',
    tel='0541 24553', tel_i='+4954124553', mail='info@kerber-kuechen.de', adresse='Hannoversche Straße 99A, 49084 Osnabrück',
    cta='Beratungstermin anfragen', nav=[('Film', 'film'), ('Über uns', 'ueber'), ('Küchen', 'kuechen'), ('Abverkauf', 'abverkauf'), ('Service', 'service'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '10:00 – 18:00'), ('Fr', '10:00 – 17:00'), ('Sa', '10:00 – 13:00'), ('Küchenberatung', 'nach Vereinbarung')],
    form_opts=['Neue Küche', 'Miele-Hausgerät', 'Ausstellungsküche / Abverkauf', 'Kundendienst', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Gern auch außerhalb der Öffnungszeiten. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Schauen Sie vorbei. <em>Parkplätze direkt vor der Tür.</em>', kt_p='Sie finden uns an der Hannoverschen Straße 99A in Osnabrück. Vereinbaren Sie einen Termin für Ihre Küchenplanung.',
    social=[('Instagram', 'https://www.instagram.com/kerberkuechen/')],
    vars=V.format(ink='#1d1d1d', mute='#5b5754', p='#C8161D', pi='#fff', dk='#1d1d1d', s2='#f3f1ef', fh='"Roboto Slab",Georgia,serif', fb='"Source Sans 3",system-ui,sans-serif', lh=58, ft='#141414') + DKHD.format(c='#141414'),
    css='''.h2{font-weight:700;letter-spacing:-.01em;line-height:1.08}.h2 em{font-style:normal;color:#C8161D}.dk .h2 em{color:#ff6b70}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.sv.dk{background:#1d1d1d;color:#fff}.sv.dk .lead{color:rgba(255,255,255,.82)}.sv .row div{border-top:4px solid #8A7D72}.vd.dk{background:#141414;color:#fff}.vd.dk .lead,.vd.dk .note{color:rgba(255,255,255,.75)}
.promo .tag{background:#C8161D;color:#fff}.ft img{height:56px}''' + RUND)
S['css2'] = '.hz{--hz-bg:#1d1d1d;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(200,22,29,.35);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:700;font-size:clamp(36px,4.4vw,70px)}.hz h1 em{color:#ff5a60;font-style:normal}.hz .ey{color:#c9bcb1}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}'
S['bot'] = BOT('Kira', 'Ihre Küchen-Lotsin', 'dem Kerber Küchenforum', S, [
    ['Öffnungszeiten', 'Mo–Do 10–18 Uhr, Fr 10–17 Uhr, Sa 10–13 Uhr. Küchenberatung nach Vereinbarung, gern auch außerhalb der Öffnungszeiten.'],
    ['Welche Küchenmarken?', 'Rempp und Häcker, dazu unsere Hausmarke inpura by Häcker. Bei Geräten sind wir Miele-Spezialist.'],
    ['Gibt es Ausstellungsküchen?', 'Ja, im Räumungsverkauf sind Ausstellungsküchen und -geräte reduziert, solange verfügbar. Telefon: 0541 24553.']],
    ['#film', '#kuechen', '#abverkauf', '#kontakt'])
S['logo'] = 'logo.png'
S['img'] = {'logo.png': ('kerber/logo.png', 0), 'h1.jpg': ('kerber/img/i008.jpg', 0),
    'film.jpg': ('kerber/img/i002.png', 0), 'christiane.jpg': ('kerber/img/i025.jpg', 0), 'thomas.jpg': ('kerber/img/i056.png', 0),
    'k1.jpg': ('kerber/img/i053.png', 0), 'k3.jpg': ('kerber/img/i047.jpg', 1400), 'k4.jpg': ('kerber/img/i028.jpg', 0),
    'abverkauf.jpg': ('kerber/img/i052.jpg', 1400)}
S['body'] = b_kerber

# ───────────── 2. Robertus Küchen, Ibbenbüren ─────────────
def b_robertus(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='2003',
        ubar=[('Seit 2003', 'Familienunternehmen'), ('450 m²', 'Ausstellung an der Gildestraße'), ('1a-Fachhändler', 'ausgezeichnet von „markt intern“')],
        ey='Robertus Küchen · Ihr Küchenstudio in Ibbenbüren',
        h1='Beste Küche <em>genießen.</em>',
        sub='Individuelle Beratung, durchdachte Planung und professionelle Montage, alles aus einer Hand. Vom günstigen Einsteigermodell bis zur exklusiven Premiumküche.'))
        + spot('film', 'Einblick in die Ausstellung', 'Willkommen <em>an der Gildestraße.</em>', 'Klassisch, modern oder Landhaus: Sehen Sie sich in Ruhe um und kommen Sie dann zum Anfassen vorbei.', 'film.mp4', 'film.jpg', 'tr')
        + scroller('kuechen', 'Klassisch, modern oder Landhaus', 'Ihre Küche, <em>exakt nach Ihren Vorstellungen.</em>', 'Vom günstigen Einsteigermodell bis zur exklusiven Premiumküche. Ein Blick in unsere Ausstellung:', [
            ('Grün mit Ausblick', 'k1.jpg', 'Matte Fronten und viel Tageslicht.', '50% 50%'),
            ('Theke mit Barhockern', 'k2.jpg', 'Kochen und zusammensitzen.', '50% 50%'),
            ('Holz und Weiß', 'k3.jpg', 'Warm, wohnlich, mit Essplatz.', '50% 50%'),
            ('Offene Regale', 'k4.jpg', 'Leicht und luftig gestaltet.', '50% 50%'),
            ('Hochschränke', 'k5.jpg', 'Geräte auf bequemer Höhe.', '50% 50%'),
            ('Badmöbel von nobilia', 'k6.jpg', 'Auch fürs Bad planen wir passend.', '50% 50%')])
        + ablauf('ablauf', 'Bester Küchenservice', 'Schritt für Schritt <em>zu Ihrer Küche.</em>', 'Gemeinsam planen wir Ihre Küche. Aufmaß, Bestellung und Montage übernehmen wir für Sie.', [
            ('Beratung im Showroom', 'Wir sprechen darüber, wie Sie Ihre Küche nutzen möchten, und vergleichen gemeinsam Küchen, Materialien und Muster.'),
            ('3D-Küchenplanung', 'Sie sehen, wie Fronten, Materialien und Designelemente in Ihrem Raum zusammenwirken. Änderungen passen wir direkt an.'),
            ('Aufmaß vor Ort', 'Wir messen Ihren Raum präzise aus und gleichen die Maße mit der 3D-Planung ab.'),
            ('Bestellung', 'Die komplette Bestellung läuft über uns, von den Küchenmöbeln bis zu den Geräten.'),
            ('Finale Montage', 'Unser Team montiert und installiert Ihre Küche bis zur letzten Schraube und nimmt die Verpackung mit.')], 'alt')
        + facts([('Endpreisgarantie', 'fester Endpreis ohne versteckte Kosten'), ('5 Jahre', 'Garantie auf Ihre Küche'), ('Ohne Scheinrabatte', 'Küchen direkt ab Werk namhafter Hersteller')])
        + team('team', 'Familienunternehmen', 'Seit 2003 <em>Robertus Küchen.</em>', 'Gegründet von Dimitri Robertus. Mit seinen Töchtern Laura und Valerie ist inzwischen die nächste Generation dabei.', [
            ('t1.jpg', 'Dimitri Robertus', 'Inhaber und Geschäftsführer'), ('t2.jpg', 'Laura Robertus', 'Verkauf & Design'), ('t3.jpg', 'Valerie Robertus', 'Leitung im Backoffice')], 'dk')
        + story('auszeichnung', 'Ausgezeichneter Service', 'Mehrfach <em>1a-Küchen-Fachhändler.</em>', [
            'Zum wiederholten Mal wurden wir vom Brancheninformationsdienst „markt intern“ für unsere Fachkompetenz und unsere überdurchschnittlichen Serviceleistungen ausgezeichnet.',
            'Service beginnt bei uns bei der individuellen Beratung und geht weit über die Endmontage hinaus.'], 'team_gesamt.jpg', 'Das Team von Robertus Küchen an der Gildestraße 7')
        + contact(s) + footer(s))

S = SITES['robertus'] = site(
    slug='robertus-kuechen-ibbenbueren', firma='Robertus Küchen GmbH', web='robertus-kuechen.de', fonts='r14egg',
    title='Robertus Küchen – Ihr Küchenstudio in Ibbenbüren', desc='Robertus Küchen in Ibbenbüren: Familienunternehmen seit 2003, 450 m² Ausstellung, 3D-Planung, Endpreisgarantie und 5 Jahre Garantie.',
    tel='05451 504945', tel_i='+495451504945', mail='info@robertus-kuechen.de', adresse='Gildestraße 7, 49477 Ibbenbüren',
    cta='Beratungstermin vereinbaren', nav=[('Ausstellung', 'film'), ('Küchen', 'kuechen'), ('Ablauf', 'ablauf'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:30 – 18:00'), ('Sa', '9:30 – 13:30')],
    form_opts=['Neue Küche', 'Ausstellungsküche', 'Badmöbel', 'Service / Montage', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Nennen Sie uns Ihre Nummer. Wir rufen Sie innerhalb unserer Öffnungszeiten zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ihre Küche <em>planen.</em>', kt_p='Besuchen Sie unser Küchenstudio an der Gildestraße 7 in Ibbenbüren oder rufen Sie uns an.',
    social=[('Instagram', 'https://www.instagram.com/robertuskuechen/')],
    vars=V.format(ink='#1c1c1c', mute='#585858', p='#E30613', pi='#fff', dk='#111', s2='#f4f4f2', fh='"Montserrat",system-ui,sans-serif', fb='"Montserrat",system-ui,sans-serif', lh=62, ft='#111') + DKHD.format(c='#111'),
    css='''.h2{font-weight:800;letter-spacing:-.02em;line-height:1.06}.h2 em{font-style:normal;color:#E30613}.tm.dk .h2 em{color:#ff5c63}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.tm.dk{background:#111;color:#fff}.tm.dk .lead{color:rgba(255,255,255,.82)}.tm .grid{grid-template-columns:repeat(3,minmax(0,300px));justify-content:center}.tm .grid figure div{aspect-ratio:4/5}.tm .grid figure div img{object-position:50% 20%}
.rd .road div::before{background:#5C8A2E}.ft16 .nb b{color:#E30613}@media(max-width:820px){.tm .grid{grid-template-columns:1fr 1fr}}''' + RUND)
S['css2'] = '.hz{--hz-bg:#111;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.85);--hz-stroke:rgba(227,6,19,.3);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:800;font-size:clamp(38px,4.6vw,74px)}.hz h1 em{color:#ff3b45;font-style:normal}.hz .ey{color:#9ccc65}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.sp16{--sp-bg:#f4f4f2;--sp-ink:#1c1c1c;--sp-ey:#E30613}.sp16 .h2 em{color:#E30613;font-style:normal}'
S['bot'] = BOT('Rieke', 'Ihre Küchen-Lotsin', 'Robertus Küchen', S, [
    ['Öffnungszeiten', 'Mo–Fr 9:30–18:00 Uhr, Sa 9:30–13:30 Uhr.'],
    ['Was kostet meine Küche am Ende?', 'Beim Kauf garantieren wir Ihnen einen festen Endpreis ohne versteckte Kosten. Dazu 5 Jahre Garantie.'],
    ['Gibt es günstige Ausstellungsküchen?', 'Ja, einige Ausstellungsküchen mit Top-Markengeräten geben wir günstig ab. Rufen Sie an: 05451 504945.']],
    ['#film', '#kuechen', '#ablauf', '#kontakt'])
S['img'] = {'logo.png': ('robertus/img/i001.png', 0), 'h1.jpg': ('robertus/img/i002.jpg', 0), 'h2.jpg': ('robertus/img/i051.jpg', 0), 'h3.jpg': ('robertus/img/i038.jpg', 0),
    'film.mp4': ('robertus/start_s.mp4', 0), 'film.jpg': ('robertus/poster.jpg', 0),
    'k1.jpg': ('robertus/img/i039.jpg', 1300), 'k2.jpg': ('robertus/img/i051.jpg', 0), 'k3.jpg': ('robertus/img/i064.jpg', 0), 'k4.jpg': ('robertus/img/i016.jpg', 1300), 'k5.jpg': ('robertus/img/i042.jpg', 0), 'k6.jpg': ('robertus/img/i009.jpg', 0),
    't1.jpg': ('robertus/img/i022.jpg', 0), 't2.jpg': ('robertus/img/i023.jpg', 0), 't3.jpg': ('robertus/img/i024.jpg', 0), 'team_gesamt.jpg': ('robertus/img/i021.jpg', 1600)}
S['body'] = b_robertus

# ───────────── 3. Küchenstudio Köse, Oer-Erkenschwick ─────────────
def b_koese(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='KÖSE',
        ubar=[('Alles aus einer Hand', 'mit eigenem Personal'), ('5 Jahre', 'Garantie auf neue Küchen'), ('Made in Germany', 'alle Küchen aus deutscher Produktion')],
        ey='Küchenstudio Köse · Oer-Erkenschwick, Kreis Recklinghausen',
        h1='Wenn es um Küchen geht, <em>sind Sie bei uns richtig.</em>',
        sub='Als Familienunternehmen setzen wir jedes Küchenprojekt mit Leidenschaft und Akribie um. Individuelle Wunschküchen zu fairen Preisen, von der Beratung bis zur Montage.'))
        + duo('stile', 'Unsere Küchen', 'Wir planen die Küchen <em>für Ihr Leben.</em>', 'Design, Farben und Materialien bestimmen Sie. Wir führen alles zu einer runden Gesamtlösung zusammen.', [
            ('Country-Stil', 'Landhausküchen', 's1.jpg', 'Kleine Inseln der Entspannung: warme, familiäre Atmosphäre mit neuer Technik und viel Komfort.', ['Skandinavisch, alpin oder mediterran', 'Gemütlich und natürlich'], 'Landhausküche anfragen'),
            ('Zeitlos', 'Klassische Küchen', 's2.jpg', 'Die Alltagshelden: klare Linien, zeitloses Design, perfekt für jede Haushaltsgröße.', ['Single, Paar oder große Familie', 'Optimum an Komfort'], 'Beratung anfragen'),
            ('Highlight', 'Design-Küchen', 's3.jpg', 'Puristische Optik, markante Farben und versteckt integrierte Technik.', ['Ganz in Schwarz oder mit Kontrasten', 'Innovative Geräte'], 'Design-Küche anfragen')])
        + ablauf('service', 'Das Komplettpaket muss stimmen', 'Vom Startschuss <em>bis zur fertigen Küche.</em>', 'Sie sollen sich zu jedem Zeitpunkt gut aufgehoben und bestens informiert fühlen.', [
            ('Beratung', 'Wir machen uns ein genaues Bild von Ihren Vorstellungen und zeigen an Beispielen, was möglich ist.'),
            ('Gratis-Aufmaß', 'Jede Nische, jeder Winkel: Mit moderner Messtechnik erfassen wir alle Daten bei Ihnen vor Ort.'),
            ('3D-Planung', 'Am Bildschirm sehen Sie Ihre Küche in 3D und bekommen ein erstes Raumgefühl.'),
            ('Montage', 'Aufmaß und Montage führen wir mit eigenem, geschultem Personal durch.')], 'alt')
        + story('studio', 'Die Begeisterung liegt in der Familie', 'Serif Ali Köse <em>berät Sie persönlich.</em>', [
            'Serif Ali Köse führt das Küchenstudio seit Herbst 2022. Übernommen hat er es von seinem Vater, der seit mehr als 22 Jahren in der Branche tätig war.',
            'In unserer Ausstellung stehen immer drei moderne Ausstellungsküchen. Denn Küchen muss man anfassen und ausprobieren können. Wir freuen uns auf Ihren Besuch!'], 'inhaber.jpg', 'Serif Ali Köse, Geschäftsführer',
            tl=[('Seit 2022', 'in zweiter Generation'), ('3 Küchen', 'in der Ausstellung'), ('3 Teams', 'Fußball-Sponsoring vor Ort')], cls='dk')
        + panels('geraete', 'Elektrogeräte', 'Erst die Technik <em>macht die Küche perfekt.</em>', 'Markenqualität von renommierten Herstellern, für jede Küchengröße und jedes Budget.', [
            ('Kochfelder', 'g1.jpg', 'Induktion oder Glaskeramik, in vielen Varianten.', '50% 50%'),
            ('Dunstabzüge', 'g2.jpg', 'Von der Inselhaube bis zur Technik im Kochfeld.', '50% 50%'),
            ('Backöfen', 'g3.jpg', 'Gern in Augenhöhe: ohne Stolperfalle durch die Ofentür.', '50% 50%'),
            ('Geschirrspüler', 'g4.jpg', 'Voll- oder teilintegriert, effizient und leise.', '50% 50%')])
        + contact(s) + footer(s))

S = SITES['koese'] = site(
    slug='kuechenstudio-koese-oer-erkenschwick', firma='Küchenstudio Köse', web='kuechen-koese.de', fonts='r14sch',
    title='Küchenstudio Köse – Küchen in Oer-Erkenschwick', desc='Küchenstudio Köse in Oer-Erkenschwick: Familienunternehmen, individuelle Küchen zu fairen Preisen, Gratis-Aufmaß, 3D-Planung, 5 Jahre Garantie.',
    tel='02368 890103', tel_i='+492368890103', mail='info@kuechen-koese.de', adresse='Klein-Erkenschwicker-Str. 137, 45739 Oer-Erkenschwick',
    cta='Beratung vereinbaren', nav=[('Küchen', 'stile'), ('Service', 'service'), ('Studio', 'studio'), ('Geräte', 'geraete'), ('Kontakt', 'kontakt')],
    hours=[('Mo', 'Ruhetag'), ('Di – Fr', '10:00 – 13:00, 15:00 – 17:00'), ('Sa', '10:00 – 14:00'), ('Weitere Termine', 'nach Vereinbarung')],
    form_opts=['Neue Küche', 'Landhausküche', 'Design-Küche', 'Elektrogeräte', 'Sonstiges'],
    form_h3='Beratung vereinbaren', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ihr Weg ins <em>Küchenstudio Köse.</em>', kt_p='Zentral in der Innenstadt, gut mit Bus und Bahn erreichbar. Parkplätze direkt vor der Tür.',
    social=[('Instagram', 'https://www.instagram.com/kuechenstudio_koese/')],
    vars=V.format(ink='#1d1d1b', mute='#575756', p='#E30613', pi='#fff', dk='#3c3c3b', s2='#f2f2f2', fh='"Poppins",system-ui,sans-serif', fb='"Poppins",system-ui,sans-serif', lh=56, ft='#1d1d1b') + DKHD.format(c='#1d1d1b'),
    css='''.h2{font-weight:700;letter-spacing:-.02em;line-height:1.08}.h2 em{font-style:normal;color:#E30613}.st.dk .h2 em{color:#ff5b63}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.st.dk{background:#3c3c3b;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.st figure img{object-position:50% 25%}.rd .road div::before{background:#E30613}.ft img{height:52px}''' + RUND)
S['css2'] = '.hz{--hz-bg:#1d1d1b;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(227,6,19,.3);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:700;font-size:clamp(34px,4vw,62px)}.hz h1 em{color:#ff3b45;font-style:normal}.hz .ey{color:#ff8a90}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hz .hz-big{font-weight:800}'
S['bot'] = BOT('Selin', 'Ihre Küchen-Lotsin', 'dem Küchenstudio Köse', S, [
    ['Öffnungszeiten', 'Montag Ruhetag. Di–Fr 10–13 und 15–17 Uhr, Sa 10–14 Uhr. Weitere Termine nach Vereinbarung.'],
    ['Kostet das Aufmaß etwas?', 'Nein, das Aufmaß bei Ihnen vor Ort ist kostenlos.'],
    ['Welche Garantie gibt es?', 'Auf neue, mit uns geplante Küchen geben wir 5 Jahre Garantie.']],
    ['#stile', '#service', '#studio', '#kontakt'])
S['logo'] = 'logo.svg'
S['img'] = {'logo.svg': ('koese/logo_inv.svg', 0), 'h1.jpg': ('koese/img/i103.jpg', 0), 'h2.jpg': ('koese/img/i148.jpg', 0), 'h3.jpg': ('koese/img/i094.jpg', 0),
    's1.jpg': ('koese/img/i121.jpg', 1400), 's2.jpg': ('koese/img/i130.jpg', 1400), 's3.jpg': ('koese/img/i202.jpg', 1400),
    'inhaber.jpg': ('koese/img/i074.jpg', 0),
    'g1.jpg': ('koese/img/i367.jpg', 1200), 'g2.jpg': ('koese/img/i349.jpg', 1200), 'g3.jpg': ('koese/img/i385.jpg', 1200), 'g4.jpg': ('koese/img/i394.jpg', 1200)}
S['body'] = b_koese
