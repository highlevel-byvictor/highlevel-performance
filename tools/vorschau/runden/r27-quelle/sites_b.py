"""Akquise DM 24.11.2026 · Teil B: Küchen Masmeier (Verl), Küchenhaus König (Wesseln)."""
from common import *
from sites_a import V, DKHD, RUND
SITES = {}

# ───────────── 4. Küchen Masmeier, Verl ─────────────
def b_masmeier(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='40',
        ubar=[('Über 40 Jahre', 'Küchen aus Verl'), ('2. Generation', 'Familie Masmeier'), ('Eigene Tischler', 'Montage durch geschultes Fachpersonal')],
        ey='Küchen Masmeier · Verl, zwischen Bielefeld und Gütersloh',
        h1='Wir machen <em>Küchenträume wahr.</em>',
        sub='Seit über 40 Jahren steht der Name Masmeier für gute Küchen, individuelle Planung und perfekten Service. Als Fachhändler mit Herz und Verstand nehmen wir uns Zeit und Ruhe für Sie.'))
        + story('geschichte', 'Wie alles begann', 'Die erste Küche <em>entstand im Wohnzimmer.</em>', [
            'Die erste Küche plante und verkaufte Manfred Masmeier noch in seinem Wohnzimmer. Der gelernte Tischler hatte bei nobilia als Monteur gearbeitet, bis er den Schritt in die Selbstständigkeit wagte.',
            'Schritt für Schritt kamen großzügige Ausstellungsräume, mehr Personal und digitale 3D-Planung dazu. Heute ist mit Tochter Lorena bereits die zweite Generation im Unternehmen.'], 'manfred.jpg', 'Manfred Masmeier, Geschäftsführer',
            tl=[('40 Jahre', 'mit Sternekoch Nelson Müller gefeiert'), ('Raum', 'Bielefeld & Gütersloh'), ('GARANT', 'Partner im Einkaufsverband')])
        + duo('marken', 'Unsere Küchenmarken', 'Ballerina und nobilia: <em>Küchen für Generationen.</em>', 'Als Partner der GARANT Gruppe bieten wir exklusive Kollektionen und große Marken zu Top-Konditionen.', [
            ('Landhausstil', 'Ihre neue Landhausküche', 'm1.jpg', 'Für Generationen gedacht, fürs Leben gemacht: Wir planen Ihre Küche im Landhausstil mit allem, was Sie im Alltag brauchen.', ['Fronten, Farben und Materialien zur Auswahl', 'Digitale 3D-Planung'], 'Landhausküche anfragen'),
            ('Modern', 'Design trifft Alltag', 'm2.jpg', 'Grifflose Fronten, Kochinsel, smarte Technik: Bei uns stellen Sie Ihre Traumküche aus verschiedensten Oberflächen und Materialien zusammen.', ['Geräte von Miele, Siemens, NEFF, BORA u. v. m.', 'Quooker, BLANCO, Franke'], 'Beratung anfragen')])
        + svc('service', 'Unser Motto: Service, Service, Service', 'Rundum-sorglos <em>zu fairen Preisen.</em>', 'Von ergonomischen Aspekten bis zur Farb- und Stilwelt haben wir sämtliche Details im Blick.', [
            ('Individuelle Küchenplanung', 'Die Planung richtet sich stets nach Ihren Bedürfnissen, Vorstellungen und den Gegebenheiten vor Ort.'),
            ('Fachgerechte Montage', 'Die Montage Ihrer neuen Küche übernimmt ausschließlich geschultes Fachpersonal.'),
            ('Finanzierung', 'Mit unserer Hausbank bieten wir Ihnen günstige Konditionen zur Finanzierung.'),
            ('Kennenlerngespräch', 'Sie wissen schon genau, was Sie wollen? Oder noch gar nicht? Beides ist ein guter Anfang.')], 'alt')
        + gallery('ausstellung', 'Unsere Ausstellung', 'Kommen Sie vorbei und <em>lassen Sie sich inspirieren.</em>', [
            ('a1.jpg', 'a', '50% 50%'), ('a2.jpg', 'b', '50% 50%'), ('a3.jpg', 'c', '50% 50%'), ('a4.jpg', 'd', '50% 50%')])
        + story('team', 'Das Team von Küchen Masmeier', 'Zertifizierte Küchenfachplaner <em>und eigene Monteure.</em>', [
            'Unser Team aus zertifizierten Küchenfachplanern und ausgebildeten Monteuren unterstützt Sie kompetent und zuverlässig. Viele Kundinnen und Kunden aus dem Raum Bielefeld und Gütersloh begleiten uns schon seit vielen Jahren.',
            'Vereinbaren Sie doch direkt ein Kennenlerngespräch!'], 'team.jpg', 'Das Team von Küchen Masmeier in Verl', rev=True, cls='dk')
        + contact(s) + footer(s))

S = SITES['masmeier'] = site(
    slug='kuechen-masmeier-verl', firma='Küchen Masmeier GmbH & Co. KG', web='masmeier.de', fonts='r14bei',
    title='Küchen Masmeier – Ihr Küchenstudio in Verl', desc='Küchen Masmeier in Verl: seit über 40 Jahren Küchen, individuelle Planung und Service. Ballerina, nobilia und Markengeräte, Raum Bielefeld und Gütersloh.',
    tel='05246 4800', tel_i='+4952464800', mail='info@masmeier.de', adresse='Bergstraße 24, 33415 Verl',
    cta='Beratungstermin vereinbaren', nav=[('Geschichte', 'geschichte'), ('Küchen', 'marken'), ('Service', 'service'), ('Ausstellung', 'ausstellung'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 12:30, 14:30 – 18:00'), ('Sa', '10:00 – 13:00')],
    form_opts=['Neue Küche', 'Landhausküche', 'Elektrogeräte', 'Finanzierung', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Ihren Besuch.</em>', kt_p='Kontaktieren Sie uns einfach oder besuchen Sie uns in unserer Ausstellung an der Bergstraße in Verl.',
    social=[('Instagram', 'https://www.instagram.com/kuechen.masmeier/')],
    vars=V.format(ink='#1f2a33', mute='#55616b', p='#3A9AD9', pi='#fff', dk='#2f3b44', s2='#eef5fa', fh='"Sora",system-ui,sans-serif', fb='"Inter",system-ui,sans-serif', lh=58, ft='#1f2a33'),
    css='''.h2{font-weight:700;letter-spacing:-.025em;line-height:1.08}.h2 em{font-style:normal;color:#2b86c4}.st.dk .h2 em{color:#8fd0ff}.alt{background:var(--s2)}
.st.dk{background:#2f3b44;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk figcaption{color:rgba(255,255,255,.7)}.sv .row div{border-top:4px solid #3A9AD9}
.st figure img{object-position:50% 30%}.gl .grid{grid-template-columns:repeat(4,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:4/3}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr 1fr}}''' + RUND)
S['css2'] = '.hz{--hz-bg:#2f3b44;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.86);--hz-stroke:rgba(58,154,217,.35);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:700;font-size:clamp(36px,4.4vw,70px)}.hz h1 em{color:#8fd0ff;font-style:normal}.hz .ey{color:#8fd0ff}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}'
S['bot'] = BOT('Mia', 'Ihre Küchen-Lotsin', 'Küchen Masmeier', S, [
    ['Öffnungszeiten', 'Mo–Fr 9:00–12:30 und 14:30–18:00 Uhr, Sa 10:00–13:00 Uhr.'],
    ['Welche Küchenmarken?', 'Unter anderem Ballerina und nobilia, dazu Geräte von Miele, Siemens, NEFF, BORA und vielen mehr.'],
    ['Kann ich finanzieren?', 'Ja, mit unserer Hausbank bieten wir günstige Finanzierungskonditionen an.']],
    ['#geschichte', '#marken', '#ausstellung', '#kontakt'])
S['img'] = {'logo.png': ('masmeier/logo.png', 0), 'h1.jpg': ('masmeier/img/i007.jpg', 0, (0.08, 0, 0.92, 1)), 'h2.jpg': ('masmeier/img/i003.jpg', 0), 'h3.jpg': ('masmeier/img/ueb_i010.jpg', 0),
    'manfred.jpg': ('masmeier/img/tea_i006.jpg', 1400), 'team.jpg': ('masmeier/img/tea_i002.jpg', 1600),
    'm1.jpg': ('masmeier/img/ueb_i002.jpg', 1400), 'm2.jpg': ('masmeier/img/ueb_i009.jpg', 1400),
    'a1.jpg': ('masmeier/img/uns_i003.jpg', 0), 'a2.jpg': ('masmeier/img/uns_i007.jpg', 0), 'a3.jpg': ('masmeier/img/uns_i009.jpg', 0), 'a4.jpg': ('masmeier/img/uns_i011.jpg', 0)}
S['body'] = b_masmeier

# ───────────── 5. Küchenhaus König, Wesseln bei Heide ─────────────
def b_koenig(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='KÖNIG',
        ubar=[('Ausgezeichnet', 'von Architektur & Wohnen'), ('Ballerina', 'und weitere Küchenmarken'), ('Junges Team', 'Beratung bis Montage')],
        ey='Küchenhaus König · Ihr Küchenstudio in Wesseln und Heide',
        h1='So schön <em>kann Küche sein.</em>',
        sub='Maßgeschneiderte Küchen, von der modernen Wohnküche über die gemütliche Landhausküche bis zur Singleküche. Trotz idyllischer Lage im ländlichen Wesseln sind wir am Puls der Zeit.'))
        + story('auszeichnung', 'Ausgezeichneter Service', 'Eines der <em>besten Küchenstudios Deutschlands.</em>', [
            'Architektur & Wohnen hat das Küchenhaus König zu einem der 100 besten Küchenstudios Deutschlands erklärt. Diese Auszeichnung verdanken wir unserem Service und den Küchen, die wir mit unseren Kundinnen und Kunden geplant haben.',
            'Wenn auch Sie eine ausgezeichnete Küche möchten, machen Sie einen Termin mit uns. Wir finden Ihre Traumküche gemeinsam.'], 'aw.jpg', 'Auszeichnung von Architektur & Wohnen', cls='aw')
        + scroller('ausstellung', 'Einblicke in unsere Ausstellung', 'Küchen zum <em>Anfassen und Ausprobieren.</em>', 'Es lohnt sich, einfach mal in unserer Ausstellung in Wesseln vorbeizuschauen.', [
            ('Dunkel und edel', 'k1.jpg', 'Matte Fronten, Stein und Holz.', '50% 50%'),
            ('Petrol mit Holz', 'k2.jpg', 'Mut zur Farbe.', '50% 50%'),
            ('Landhaus', 'k3.jpg', 'Hell, mit Kochinsel.', '50% 50%'),
            ('Wohnküche', 'k4.jpg', 'Mit großem Esstisch.', '50% 50%'),
            ('Kochinsel', 'k5.jpg', 'Mittendrin statt an der Wand.', '50% 50%')])
        + panels('mehr', 'Küchen & Mehr', 'Nicht nur Küchen: <em>Räume, die funktionieren.</em>', 'Mit derselben Sorgfalt planen wir Bäder, Wohnräume und Hauswirtschaftsräume.', [
            ('Bäder', 'm1.jpg', 'Waschtisch, Stauraum und Licht aus einer Hand.', '50% 50%'),
            ('Wohnen', 'm2.jpg', 'Ankleide, Garderobe und Wohnmöbel nach Maß.', '50% 50%'),
            ('Hauswirtschaftsräume', 'm3.jpg', 'Waschmaschine und Trockner auf Arbeitshöhe.', '50% 50%'),
            ('Geräte & Ausstattung', 'm4.jpg', 'Gerätewelt, Spülen, Armaturen und Smart Home.', '50% 50%')], 'alt')
        + ablauf('ablauf', 'Wie wir beraten', 'Persönlich <em>und individuell.</em>', 'Von der ersten Beratung bis zur finalen Montage sind wir an Ihrer Seite.', [
            ('Individuelle Beratung', 'Wir nehmen uns Zeit, Ihre Wünsche zu verstehen, bei einem Termin in unserem Küchenhaus.'),
            ('Aufmaß', 'Damit Ihre Küche perfekt passt, kommen wir zu Ihnen und messen Ihren Raum millimetergenau aus.'),
            ('Planung', 'Mit Planungssoftware und Ihren Ideen entwickeln wir eine Küche, die zu Ihnen passt.'),
            ('Lieferung & Montage', 'Wir liefern Ihre Küche pünktlich und montieren sie für Sie.')])
        + story('team', 'Unser Team', 'Ein junges Team <em>mit frischen Ideen.</em>', [
            'Das Küchenhaus König steht für modernen Küchenbau mit einer kreativen und persönlichen Note. Unser Team setzt auf Innovation, um die Küche zum Mittelpunkt Ihres Zuhauses zu machen.',
            '„So schön kann Küche sein!“ – Daniel König, Geschäftsführer'], 'team.jpg', 'Aus dem Team vom Küchenhaus König', rev=True, cls='dk')
        + contact(s) + footer(s))

S = SITES['koenig'] = site(
    slug='kuechenhaus-koenig-wesseln', firma='Küchenhaus König GmbH', web='kuechenhaus-koenig.de', fonts='r16zwei',
    title='Küchenhaus König – Ihr Küchenstudio in Wesseln und Heide', desc='Küchenhaus König in Wesseln bei Heide: ausgezeichnet als eines der besten Küchenstudios Deutschlands. Küchen, Bäder, Wohnen, Hauswirtschaftsräume.',
    tel='0481 78775000', tel_i='+4948178775000', mail='info@kuechenhaus-koenig.de', adresse='Von-Humboldt-Str. 3, 25746 Wesseln',
    cta='Termin vereinbaren', nav=[('Auszeichnung', 'auszeichnung'), ('Ausstellung', 'ausstellung'), ('Küchen & Mehr', 'mehr'), ('Beratung', 'ablauf'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo, Di, Do, Fr', '9:00 – 12:00, 13:00 – 18:00'), ('Mi', 'nach Vereinbarung'), ('Sa', '9:00 – 12:00')],
    form_opts=['Neue Küche', 'Bad', 'Wohnen / Ankleide', 'Hauswirtschaftsraum', 'Geräte', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Besuchen Sie uns <em>in Wesseln.</em>', kt_p='Rufen Sie an oder vereinbaren Sie direkt einen Termin. Mittwochs beraten wir Sie nach Vereinbarung.',
    social=[('Instagram', 'https://www.instagram.com/kuechenhauskoenig/')],
    vars=V.format(ink='#1b1d1c', mute='#555a57', p='#76B82A', pi='#111', dk='#1f2321', s2='#f1f4ef', fh='"Montserrat",system-ui,sans-serif', fb='"Work Sans",system-ui,sans-serif', lh=60, ft='#151816') + DKHD.format(c='#1f2321'),
    css='''.h2{font-weight:700;letter-spacing:-.02em;line-height:1.08}.h2 em{font-style:normal;color:#5c9a17}.st.dk .h2 em,.dk .h2 em{color:#9be14a}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.st.dk{background:#1f2321;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk figcaption{color:rgba(255,255,255,.7)}.st.aw figure img{aspect-ratio:2048/1164;object-fit:cover;height:auto}
.rd .road div::before{background:#76B82A}.ft img{height:60px}#team figure img{aspect-ratio:1/1!important;height:auto!important;object-fit:cover;object-position:50% 40%}''' + RUND)
S['css2'] = '.hz{--hz-bg:#1f2321;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.85);--hz-stroke:rgba(118,184,42,.35);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:700;font-size:clamp(38px,4.6vw,74px)}.hz h1 em{color:#9be14a;font-style:normal}.hz .ey{color:#9be14a}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hz .hz-big{font-weight:800}'
S['bot'] = BOT('Kaja', 'Ihre Küchen-Lotsin', 'dem Küchenhaus König', S, [
    ['Öffnungszeiten', 'Mo, Di, Do, Fr 9–12 und 13–18 Uhr, Sa 9–12 Uhr. Mittwoch nach Vereinbarung.'],
    ['Planen Sie auch Bäder?', 'Ja, neben Küchen planen wir Bäder, Wohnräume und Hauswirtschaftsräume.'],
    ['Wie bekomme ich einen Termin?', 'Rufen Sie uns an unter 0481 78775000 oder nutzen Sie das Formular unten.']],
    ['#auszeichnung', '#ausstellung', '#mehr', '#kontakt'])
S['logo'] = 'logo.svg'
S['img'] = {'logo.svg': ('koenig/logo.svg', 0), 'h1.jpg': ('koenig/img/i005.jpg', 0), 'h2.jpg': ('koenig/img/i076.jpg', 0), 'h3.jpg': ('koenig/img/i184.jpg', 0),
    'aw.jpg': ('koenig/img/i011.jpg', 0),
    'k1.jpg': ('koenig/img/i067.jpg', 1300), 'k2.jpg': ('koenig/img/i076.jpg', 1300), 'k3.jpg': ('koenig/img/i085.jpg', 1300), 'k4.jpg': ('koenig/img/i103.jpg', 1300), 'k5.jpg': ('koenig/img/i112.jpg', 1300),
    'm1.jpg': ('koenig/img/i346.jpg', 0), 'm2.jpg': ('koenig/img/i374.jpg', 1300), 'm3.jpg': ('koenig/img/i406.jpg', 1300), 'm4.jpg': ('koenig/img/i175.jpg', 1300),
    'team.jpg': ('koenig/img/i274.jpg', 1400, (0, 0, 0.97, 1))}
S['body'] = b_koenig
