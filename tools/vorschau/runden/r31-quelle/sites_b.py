"""Akquise DM 26.11.2026 (Do, Handwerk) · Teil B: Noethen Bedachungen (Rheda-Wiedenbrück / Münster-Hiltrup), Gartemann Bedachungen (Bielefeld).
Texte, Leistungen, Bilder und Logos stammen von den Originalseiten. Keine erfundenen Preise, Zahlen oder Stimmen."""
from common import *
SITES = {}

# ───────────── 4 · Noethen Bedachungen, Rheda-Wiedenbrück + Münster-Hiltrup ─────────────
def b_noethen(s):
    return (hd(s) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 40%', 'h2.jpg': '55% 40%', 'h3.jpg': '50% 50%'}, big='', side='l',
        ubar=[('Meister', 'Dachdecker-Innung'), ('2 Orte', 'Rheda und Hiltrup'), ('24h', 'Notdienst')],
        ey='Noethen Bedachungen · Kreis Gütersloh und Münster',
        h1='Qualität <em>ganz oben.</em>',
        sub='Unser junger, hoch motivierter Dachdecker-Meisterbetrieb zeigt noch echtes Herzblut und handwerkliches Geschick. Steildach oder Flachdach: Wir sind Ihr Experte.'))
        + facts([('24h', 'Notdienst bei Sturmschaden: 0170 167 43 97'), ('Eigene', 'Bauklempnerei, unabhängig von Drittanbietern'), ('Geschult', 'Roto Profipartner und VELUX-Fachbetrieb')], 'nx')
        + panels('leistungen', 'Leistungen', 'Dächer sind unser <em>Spezialgebiet.</em>', 'Und je höher die Anforderungen sind, umso wohler fühlen wir uns.', [
            ('Dachdecker-Profis', 'l1.jpg', 'Steildach oder Flachdach, Neubau oder Sanierung: fachgerecht vom Meisterbetrieb.', '50% 40%'),
            ('Bauklempnerei', 'l2.jpg', 'Eigene Bauklempnerei: Wir sind unabhängig und arbeiten schneller und termingerecht.', '50% 50%'),
            ('Reparatur', 'l3.jpg', 'Bei einem Sturmschaden ist schnelles Handeln gefragt. Nach der Beratung beginnen wir schnellstmöglich.', '50% 50%'),
            ('Fassadenbau', 'l4.jpg', 'Mit der energetischen Sanierung Ihrer Fassade senken Sie den Energieverbrauch und sparen langfristig.', '50% 50%')])
        + promo('notdienst', 'nd.jpg', '24h Notdienst', 'Sturmschaden? <em>Wir sind schnell da.</em>',
                'Bei einem Sturmschaden ist schnelles Handeln erforderlich. Deshalb beginnen wir nach einer Beratung schnellstmöglich mit den Reparaturarbeiten, in Rheda-Wiedenbrück, Gütersloh, Münster und Umgebung.',
                ['Notdienst rund um die Uhr: 0170 167 43 97', 'Rheda-Wiedenbrück: 05242 9860665', 'Münster-Hiltrup: 02501 9783111'], 'Jetzt anfragen', 'alt')
        + svc('mehr', 'Gewerkeübergreifend', 'Mehr als <em>nur Dach.</em>', 'Gewerkeübergreifende Arbeiten werden immer wichtiger. Deshalb machen wir auch das:', [
            ('Balkone und Terrassen', 'Sanierung von Balkonen und Terrassen.'),
            ('Innenausbau und Trockenbau', 'Schnelle, flexible Gestaltung von Wohnräumen, Büros und Gewerbeflächen.'),
            ('Dachstühle in Holzbau', 'Fachgerecht ausgeführte Holzbauten für Ihren Dachstuhl.'),
            ('Dachfenster', 'Als geschulter Betrieb finden wir mit Ihnen die passende Fensterlösung.'),
            ('Energieberatung', 'Björn Noethen ist Gebäude- und Energieberater im Handwerk.'),
            ('Dachbelüftung', 'Fachgerechte Belüftung schützt Ihr Dach vor Feuchtigkeit und Schäden.')], 'dk')
        + story('ueber', 'Über uns', 'Jeden Tag mit einem <em>guten Gefühl beenden.</em>', [
            'Besonders stolz sind wir auf unsere Bandbreite an Leistungen. Unsere eigene Bauklempnerei macht uns unabhängig und garantiert eine termingerechte Ausführung.',
            'Nutzen Sie unsere kleine Schwäche, jeden Tag mit einem guten Gefühl beenden zu wollen, zu Ihrem Vorteil und fordern Sie ein unverbindliches Angebot an. Ihr Björn Noethen'],
            'ab.jpg', 'Noethen Bedachungen bei der Arbeit',
            tl=[('Björn Noethen', 'Dachdeckermeister, Gebäude- und Energieberater im Handwerk'), ('Wir bilden aus', 'Komm in unser Team')])
        + orte('gebiet', 'Einzugsgebiet', 'Für Sie unterwegs <em>zwischen Gütersloh und Münster.</em>', 'Zwei Standorte, kurze Wege.', [
            ('Rheda-Wiedenbrück', 'Siechenstraße 39b', '05242 9860665'), ('Münster-Hiltrup', 'Bernhard-Poether-Str. 38', '02501 9783111'),
            ('Kreis Gütersloh', 'Gütersloh, Herzebrock-Clarholz, Harsewinkel, Rietberg, Langenberg', ''), ('Münsterland', 'Wolbeck, Handorf, Roxel, Gievenbeck, Warendorf, Ahlen, Beckum', '')])
        + contact(s) + footer(s))

P4, D4 = '#e30613', '#2b2b2e'
S = SITES['noethen'] = site(
    slug='noethen-bedachungen-rheda-wiedenbrueck', firma='Noethen Bedachungen', web='noethen-dachdecker.de', fonts='r31no', branche='Dachdecker',
    title='Noethen Bedachungen – Dachdecker in Rheda-Wiedenbrück und Münster', desc='Noethen Bedachungen: Dachdecker-Meisterbetrieb in Rheda-Wiedenbrück und Münster-Hiltrup. Steildach, Flachdach, Bauklempnerei, Reparatur, Fassadenbau, 24h Notdienst.',
    tel='05242 9860665', tel_i='+4952429860665', mail='kontakt@noethen-dachdecker.de', adresse='Siechenstraße 39b, 33378 Rheda-Wiedenbrück', google=None,
    cta='Kostenlos beraten lassen', nav=[('Leistungen', 'leistungen'), ('Notdienst', 'notdienst'), ('Mehr', 'mehr'), ('Über uns', 'ueber'), ('Gebiet', 'gebiet'), ('Kontakt', 'kontakt')],
    hours=[('Notdienst', '24 Stunden'), ('Münster', '02501 9783111')],
    form_opts=['Steildach', 'Flachdach', 'Reparatur / Sturmschaden', 'Bauklempnerei', 'Fassade', 'Dachfenster', 'Sonstiges'], form_orte=['Rheda-Wiedenbrück', 'Münster-Hiltrup'],
    form_h3='Unverbindlich anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns umgehend.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='So erreichen <em>Sie uns.</em>', kt_p='Schreiben Sie uns oder rufen Sie direkt an. Wir melden uns gerne und umgehend bei Ihnen zurück.',
    social=[('Instagram', 'https://www.instagram.com/noethen.dachdecker/')],
    vars=V.format(ink='#1f1f22', mute='#47474d', p=P4, pi='#fff', dk=D4, s2='#f4f4f5', fh='"Oswald",system-ui,sans-serif', fb='"Source Sans 3",system-ui,sans-serif', lh=40, ft=D4),
    css=css_hw(P4, D4, '.h2,.hz h1{text-transform:uppercase;font-weight:600;letter-spacing:.005em}.promo .tag{background:#e30613;color:#fff}.sv.dk{background:#2b2b2e;color:#fff}.sv.dk .lead{color:rgba(255,255,255,.85)}.ft img{background:#fff;padding:8px 12px;height:56px}'))
S['css2'] = hz('#fff', P4)
S['logo'] = 'logo.png'
S['bot'] = BOT('Firstl', 'Ihr Dach-Lotse', 'Noethen Bedachungen', S, [
    ['Ich habe einen Sturmschaden.', 'Rufen Sie unseren 24h Notdienst an: 0170 167 43 97. Wir beginnen schnellstmöglich mit der Reparatur.'],
    ['Wo sind Sie?', 'In Rheda-Wiedenbrück (Siechenstraße 39b) und Münster-Hiltrup (Bernhard-Poether-Str. 38).'],
    ['Was machen Sie außer Dächern?', 'Bauklempnerei, Fassadenbau, Balkone und Terrassen, Trocken- und Innenausbau, Dachstühle in Holzbau.']],
    ['#leistungen', '#notdienst', '#gebiet', '#kontakt'])
S['img'] = {'logo.png': (I('noethen', 12)[0], 600), 'h1.jpg': I('noethen', 17, 1200), 'h2.jpg': I('noethen', 15, 1200), 'h3.jpg': I('noethen', 29, 1592),
    'l1.jpg': I('noethen', 46, 1400), 'l2.jpg': I('noethen', 22, 1200), 'l3.jpg': I('noethen', 21, 1200), 'l4.jpg': I('noethen', 18, 1200),
    'nd.jpg': I('noethen', 33, 1400), 'ab.jpg': I('noethen', 48, 1200)}
S['body'] = b_noethen

# ───────────── 5 · Gartemann GmbH Bedachungen, Bielefeld ─────────────
def b_gartemann(s):
    return (hd(s) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 45%', 'h2.jpg': '50% 50%', 'h3.jpg': '50% 50%'}, big='',
        ubar=[('4.', 'Generation'), ('10', 'Mitarbeiter'), ('Neu', 'Drohnen-Check')],
        ey='Gartemann Bedachungen · Bielefeld',
        h1='GeDacht … <em>Getan.</em>',
        sub='Traditionelles Handwerk verbindet moderne Technik: vom Gerüstbau über den kompletten Dachstuhl und Ihre Fassade bis zur Verlegung des letzten Dachziegels.'))
        + tabs('leistungen', 'Leistungen', 'Ihr Dach ist bei uns <em>in besten Händen.</em>', 'Nach umfassender Beratung setzen wir Ihre Vorstellungen um.', [
            ('Steildachsanierung', 'l1.jpg', 'Alte Ziegel und Latten runter, Unterspannbahn mit Nageldichtband und Konterlatten drauf: So ist Ihr Haus auch nach Feierabend gegen die Witterung geschützt.', ['Hochwertige Baustoffe', 'Geschultes Fachpersonal']),
            ('Flachdach', 'l2.jpg', 'Industrie- oder Wohngebäude: Ein modernes Flachdach bietet maximale Gestaltungsfreiheit, auch als Dachterrasse oder Gründach.', ['Planung, Ausführung, Wartung']),
            ('Kranservice', 'l3.jpg', 'Effizient. Zuverlässig. Außergewöhnlich. Wir heben das Material dorthin, wo es gebraucht wird, auch für Kollegen anderer Gewerke.', []),
            ('Drohnen-Inspektion', 'l4.jpg', 'Mit hochauflösender 4K-Kamera erkennen wir bei der Dachinspektion auch die kleinsten Mängel, ohne dass jemand aufs Dach steigen muss.', ['DJI Mini 5 Pro für kleine Baustellen', 'DJI Phantom 4 für große Industriedächer']),
            ('Fassade', 'l5.jpg', 'Von der Unterkonstruktion bis zum fertigen Fassadenbild, echte Handwerksarbeit mit Liebe zum Detail.', [])])
        + gallery('projekte', 'Projekte', 'Hier sehen Sie <em>unsere Arbeit.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%')])
        + promo('kirche', 'ki.jpg', 'Referenz', 'Umdeckung <em>einer Kirche.</em>',
                'Tradition bewahren, Qualität neu gedacht: Dieses Kirchendach erstrahlt mit neuen Ziegeln und hochwertigen Kupferdetails in neuem Glanz.',
                ['Asbestsanierung', 'Gauben richten', 'Carport aufbereiten'], 'Projekt anfragen', 'alt')
        + story('ueber', 'Über uns', 'Professionell <em>und zuverlässig.</em>', [
            'Hochwertige Baustoffe, ständig geschultes Personal und die Erfahrung aus nunmehr vier Generationen sind Garanten für die optimale Umsetzung Ihrer Wünsche rund ums Dach.',
            'Unser Anspruch ist nicht nur ein Dach über Ihrem Kopf, das den heutigen Anforderungen gerecht wird, sondern ein nachhaltiges Dach, das Ihnen noch lange Freude bereitet.'],
            'ab.jpg', 'Unser Betriebshof an der Grafenheider Straße', cls='dk',
            tl=[('Dirk Gartemann', 'Geschäftsführer'), ('Karriere', 'Dachdecker oder Zimmermann gesucht')])
        + contact(s) + footer(s))

P5, D5 = '#151883', '#0e1052'
S = SITES['gartemann'] = site(
    slug='gartemann-bedachungen-bielefeld', firma='Gartemann GmbH', web='bedachungen-gartemann.de', fonts='r31ga', branche='Dachdecker',
    title='Gartemann Bedachungen – Dachdecker in Bielefeld', desc='Gartemann Bedachungen in Bielefeld, Traditionsbetrieb in vierter Generation: Steildach, Flachdach, Fassade, Kranservice und Drohnen-Inspektion.',
    tel='0521 771919', tel_i='+49521771919', mail='gartemanngmbh@bitel.net', adresse='Grafenheider Straße 88a, 33729 Bielefeld', google=None,
    cta='Kostenlos beraten lassen', nav=[('Leistungen', 'leistungen'), ('Projekte', 'projekte'), ('Referenz', 'kirche'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung')],
    form_opts=['Steildach', 'Flachdach', 'Fassade', 'Kranservice', 'Drohnen-Inspektion', 'Bewerbung', 'Sonstiges'],
    form_h3='Kostenlos beraten lassen', form_p='Sagen Sie uns kurz, worum es geht. Wir freuen uns auf Sie.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Kontaktieren Sie uns gerne. <em>Wir freuen uns auf Sie.</em>', kt_p='Rufen Sie an oder schreiben Sie uns.',
    social=[('Instagram', 'https://www.instagram.com/gartemannbedachungen/')],
    vars=V.format(ink='#10123a', mute='#3e4062', p=P5, pi='#fff', dk=D5, s2='#f1f2f9', fh='"Poppins",system-ui,sans-serif', fb='"Poppins",system-ui,sans-serif', lh=64, ft=D5),
    css=css_hw(P5, D5, '.h2,.hz h1{font-weight:700}.h2 em,.hz h1 em{color:#3a3fd1}.promo .tag{background:#151883;color:#fff}.ft img{background:#fff;padding:6px 10px;height:70px}body{font-weight:400}.st.dk .ey{color:#aab0ff}'))
S['css2'] = hz('#fff', P5)
S['logo'] = 'logo.png'
S['bot'] = BOT('Dachs', 'Ihr Dach-Lotse', 'Gartemann', S, [
    ['Was ist die Drohnen-Inspektion?', 'Mit 4K-Drohnen prüfen wir Ihr Dach von oben und erkennen auch kleine Mängel, ohne Gerüst.'],
    ['Haben Sie einen Kran?', 'Ja, unser Kranservice hebt Material auch für Kollegen anderer Gewerke.'],
    ['Wie erreiche ich Sie?', 'Telefon 0521 771919 oder gartemanngmbh@bitel.net.']],
    ['#leistungen', '#projekte', '#kirche', '#kontakt'])
S['img'] = {'logo.png': ('/home/claude/r31raw/gartemann/logo.jpg', 420, 'trimalpha'), 'h1.jpg': I('gartemann', 3), 'h2.jpg': I('gartemann', 1), 'h3.jpg': I('gartemann', 22),
    'l1.jpg': I('gartemann', 24, 1400), 'l2.jpg': I('gartemann', 32, 1400), 'l3.jpg': I('gartemann', 5, 1400), 'l4.jpg': I('gartemann', 8, 1400), 'l5.jpg': I('gartemann', 4, 1400),
    'g1.jpg': I('gartemann', 13, 1400), 'g2.jpg': I('gartemann', 18, 900), 'g3.jpg': I('gartemann', 19, 900), 'g4.jpg': I('gartemann', 26, 1000), 'g5.jpg': I('gartemann', 27, 1000), 'g6.jpg': I('gartemann', 14, 1400),
    'ki.jpg': I('gartemann', 11, 1400), 'ab.jpg': I('gartemann', 2, 1400)}
S['body'] = b_gartemann
