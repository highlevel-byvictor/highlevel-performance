"""Akquise DM 26.11.2026 (Do, Handwerk) · Teil A: A. Pähler Bedachungen (Gütersloh), Joswieg Malerbetrieb (Bielefeld), Kohnen & Meyer (Cloppenburg).
Texte, Leistungen, Bilder, Logos und Videos stammen von den Originalseiten. Keine erfundenen Preise, Zahlen oder Stimmen."""
from common import *
SITES = {}

# ───────────── 1 · A. Pähler Bedachungen GmbH, Gütersloh ─────────────
def b_paehler(s):
    return (hd(s, False) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 45%', 'h2.jpg': '50% 40%', 'h3.jpg': '60% 40%'}, big='',
        ubar=[('Seit 70 Jahren', 'Dachdecker in Gütersloh'), ('30', 'Mitarbeiter im Einsatz'), ('VELUX', 'Premium Partner')],
        ey='A. Pähler Bedachungen GmbH · Gütersloh',
        h1='Ihr Experte <em>für Flachdächer.</em>',
        sub='Im industriellen und privaten Bereich stehen wir Ihnen als „Komplettdienstleister“ rund um sämtliche Dacharbeiten kompetent zur Seite. Kein Dach ist uns zu groß oder zu steil.'))
        + spot('film', 'Unser Film', 'Mit Bedacht <em>bei der Arbeit.</em>',
               'Ein kurzer Einblick, wie wir arbeiten: auf den Dächern von Gütersloh, mit modernem Fuhrpark und einem Team, auf das man sich verlassen kann.', 'film.mp4', 'film.jpg')
        + promo('flachdach', 'fd.jpg', 'Unsere Spezialität', 'Flachdach: Neubau, Sanierung, <em>Wartung.</em>',
                'Unsere besondere Expertise liegt im Bereich der Flachdächer. Egal, ob es um eine Neukonstruktion, eine Reparatur oder die Wartung geht: Wir sind spezialisiert und auf dem neuesten Stand der Technik. Ob mit Begrünung oder ohne, wir fertigen Ihr Flachdach genau nach Ihren Wünschen an.',
                ['Großdächer für Industrie und Gewerbe', 'Sanieren und dämmen, fachmännisch', 'Flachdach mit oder ohne Begrünung'], 'Flachdach anfragen', 'alt')
        + panels('leistungen', 'Leistungen', 'Alles rund ums Dach <em>aus einer Hand.</em>', 'Ob Industrie, Unternehmen oder Privathaus: Wir beraten Sie umfangreich und setzen Ihr Bauvorhaben zuverlässig um.', [
            ('Flachdach', 'l1.jpg', 'Neukonstruktion, Reparatur und Wartung, mit oder ohne Begrünung.', '50% 50%'),
            ('Steildach, Pultdach, Satteldach', 'l2.jpg', 'Bauvorschriften, Formen und Eindeckmaterialien kennen wir in- und auswendig.', '50% 40%'),
            ('Gauben und Dachfenster', 'l3.jpg', 'Als VELUX Premium Partner beraten wir Sie zum neuen Dachfenster und bauen es ein.', '50% 30%'),
            ('Moderner Fuhrpark', 'l4.jpg', 'Wir arbeiten mit modernsten Maschinen und Arbeitsgeräten, bis hin zum eigenen Kran.', '50% 50%')])
        + facts([('70 Jahre', 'Firmengeschichte und Bedachungserfahrung'), ('30', 'Mitarbeiter auf den Dächern rund um Gütersloh'), ('46 Jahre', 'arbeiten unsere zwei längsten Kollegen schon bei uns')], 'nx')
        + gallery('team', 'Unser Team', 'Gewissenhaft unterwegs <em>auf den Dächern von Gütersloh.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 45%'), ('g2.jpg', 'h2r', '50% 35%'), ('g3.jpg', 'h2r', '50% 35%'), ('g4.jpg', '', '50% 40%'), ('g5.jpg', '', '50% 40%'), ('g6.jpg', 'w2', '50% 45%')])
        + ablauf('weg', 'Zu Ihrem neuen Dach', 'In 3 einfachen <em>Schritten.</em>', 'Lehnen Sie sich zurück, wir übernehmen alle anfallenden Dacharbeiten.', [
            ('Kontaktieren Sie uns unverbindlich', 'Sie melden sich über das Formular oder per Telefon und wir beraten Sie ausführlich.'),
            ('Planen Sie mit uns Ihr Projekt', 'Nach eingehender Analyse der örtlichen Gegebenheiten lassen wir beim Planen Ihre Wünsche Wirklichkeit werden.'),
            ('Sie entspannen, wir legen los', 'Während Sie uns im Garten- oder Bürostuhl zusehen, setzen wir Ihr Bauvorhaben nachhaltig und zuverlässig um.')])
        + story('ueber', 'Über uns', 'Was ich verspreche, <em>halte ich ein.</em>', [
            '„Im Jahr 1995 habe ich den Dachdeckerbetrieb von meinem Vater übernommen. Meine Kindertage habe ich viel im Unternehmen meines Vaters verbracht.“',
            '„Wenn ich Ihnen etwas verspreche, dann können Sie sich darauf verlassen, dass ich es auch einhalte. Für meine Mitarbeiter habe ich immer ein offenes Ohr oder einen lustigen Spruch in petto.“'],
            'ab.jpg', 'A. Pähler Bedachungen, Stadtring Kattenstroth 96', cls='dk',
            tl=[('Andreas Pähler', 'Dachdeckermeister, Geschäftsführer'), ('Seit 1995', 'in zweiter Generation')])
        + promo('karriere', 'ka.jpg', 'Karriere', 'Werde zum <em>Flachdachexperten.</em>',
                'Du möchtest dich in einem vertrauensvollen Team konstant zum Profi weiterentwickeln? Dann steig bei uns ein und hoch hinaus auf die Steil-, Sattel- und Flachdächer von Gütersloh und Umgebung.',
                ['Familiäres Team', 'Keine auswärtigen Baustellen', 'Unbefristeter Vertrag'], 'Jetzt bewerben')
        + contact(s) + footer(s))

P1, D1 = '#e63e0c', '#21383f'
S = SITES['paehler'] = site(
    slug='paehler-bedachungen-guetersloh', firma='A. Pähler Bedachungen GmbH', web='dachdecker-guetersloh.de', fonts='r31pa', branche='Dachdecker',
    title='A. Pähler Bedachungen – Dachdecker in Gütersloh', desc='A. Pähler Bedachungen GmbH in Gütersloh: Flachdach-Experten, Steildach, Gauben, Dachfenster, VELUX Premium Partner. Seit 70 Jahren.',
    tel='05241 211 75 0', tel_i='+495241211750', mail='info@paehler-dach.de', adresse='Stadtring Kattenstroth 96, 33332 Gütersloh', google=None,
    cta='Kostenlos beraten lassen', nav=[('Film', 'film'), ('Flachdach', 'flachdach'), ('Leistungen', 'leistungen'), ('Team', 'team'), ('Karriere', 'karriere'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung')],
    form_opts=['Flachdach', 'Steildach / Satteldach', 'Gaube / Dachfenster', 'Reparatur / Wartung', 'Großprojekt / Gewerbe', 'Bewerbung', 'Sonstiges'],
    form_h3='Kostenlos beraten lassen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ihr Dach soll wieder <em>in frischem Glanz erstrahlen?</em>', kt_p='Diese Herausforderung nehmen wir gerne an. Rufen Sie an oder schreiben Sie uns.',
    social=[('Instagram', 'https://www.instagram.com/paehler_bedachungen/')],
    vars=V.format(ink='#1d2a2e', mute='#3f4d52', p=P1, pi='#fff', dk=D1, s2='#f2f4f4', fh='"Montserrat",system-ui,sans-serif', fb='"Montserrat",system-ui,sans-serif', lh=50, ft=D1) + DKHD.format(c=D1),
    css=css_hw(P1, D1, '.h2,.hz h1{text-transform:uppercase;font-weight:800;letter-spacing:-.01em}.hd .nav a{color:#fff}.promo .tag{background:#e63e0c;color:#fff}'))
S['css2'] = hz(D1, P1, '#fff', 'rgba(255,255,255,.86)') + '.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hz .hz-ub b{color:#fff}.hz h1 em{color:#ff6a3d}'
S['bot'] = BOT('Ziegel', 'Ihr Dach-Lotse', 'A. Pähler Bedachungen', S, [
    ['Was ist Ihre Spezialität?', 'Flachdächer: Neukonstruktion, Reparatur und Wartung, auch für Großdächer in Industrie und Gewerbe.'],
    ['Bauen Sie Dachfenster ein?', 'Ja. Als VELUX Premium Partner beraten wir Sie und bauen Ihr neues Dachfenster ein.'],
    ['Wie erreiche ich Sie?', 'Telefon 05241 211 75 0 oder per Mail an info@paehler-dach.de.']],
    ['#film', '#flachdach', '#leistungen', '#kontakt'])
S['logo'] = 'logo.png'
S['img'] = {'logo.png': (I('paehler', 0)[0], 520), 'h1.jpg': I('paehler', 19), 'h2.jpg': I('paehler', 5), 'h3.jpg': I('paehler', 4),
    'film.mp4': ('/home/claude/r31raw/paehler/film.mp4', 0), 'film.jpg': ('/home/claude/r31raw/paehler/poster.jpg', 0),
    'fd.jpg': I('paehler', 3, 1400), 'l1.jpg': I('paehler', 20, 1200), 'l2.jpg': I('paehler', 22, 1200), 'l3.jpg': I('paehler', 23, 1200), 'l4.jpg': I('paehler', 2, 1200),
    'g1.jpg': I('paehler', 14, 1400), 'g2.jpg': I('paehler', 9, 900), 'g3.jpg': I('paehler', 34, 900), 'g4.jpg': I('paehler', 25, 900), 'g5.jpg': I('paehler', 12, 900), 'g6.jpg': ('/home/claude/r31raw/paehler/img/i042.png', 1000),
    'ab.jpg': I('paehler', 26, 1200), 'ka.jpg': I('paehler', 28, 1200)}
S['body'] = b_paehler

# ───────────── 2 · Joswieg Malerbetrieb GmbH, Bielefeld ─────────────
def b_joswieg(s):
    return (hd(s) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 50%', 'h2.jpg': '50% 60%', 'h3.jpg': '40% 40%'}, big='1966', side='l',
        ubar=[('Seit 1966', 'Familienbetrieb in Bielefeld'), ('3. Preis', 'Deutscher Fassadenpreis 2014 und 2016'), ('Hanf', 'zertifizierte Dämmung')],
        ey='Joswieg Malerbetrieb · Bielefeld',
        h1='Fassaden, die <em>Preise gewinnen.</em>',
        sub='Malerarbeiten jeglicher Art, spezialisiert auf Wärmedämmverbundsysteme. Tradition und jahrzehntelange Erfahrung, kombiniert mit den neuesten Techniken und viel Geschick.'))
        + marquee(['Malerarbeiten', 'Fassadenanstriche', 'Wärmedämmverbundsysteme', 'Industrieanstriche', 'Denkmalschutz', 'Keramische Beläge', 'Hanf-Fassadendämmung', 'Energieausweise', 'KfW-Förderung'], 'wm')
        + promo('wdvs', 'wd.jpg', 'Unsere Spezialität', 'Im Sommer kühl, <em>im Winter warm.</em>',
                'Wer sein Haus heute dämmen lässt, erhält ein ausgereiftes System aus vielen Komponenten, die alle zusammen funktionieren müssen. Wir verarbeiten Dämmstoffe aus Mineralwolle, PUR und mittlerweile auch aus Hanf. Ob Neu- oder Altbau: Der Untergrund wird geprüft, dann folgen Dämmung, Armierung, Oberputz und hochwertige Fassadenfarbe.',
                ['Heizkosten sparen, Bausubstanz schützen', 'Gesundes Raumklima, weniger Schimmel', 'Abnahmen mit dem Systemhersteller, schriftlich protokolliert'], 'Beratung anfragen', 'alt')
        + tabs('leistungen', 'Leistungen', 'Farbe kann <em>sehr viel.</em>', 'Sie bedeutet Verwirklichung, Frische, Umgestaltung oder einfach Altes wieder in neuem Glanz.', [
            ('Fassadenanstriche', 'l1.jpg', 'Ein frischer Außenanstrich verschönert Ihr Haus und schützt es langfristig vor Witterung. Unsere Arbeit beginnt mit der Analyse des Untergrunds, erst dann bestimmen wir Maßnahmen und Materialien.', ['Silikonharz-, Silikat- und Acrylfarben', 'Nur Qualitätsprodukte']),
            ('Malerarbeiten innen', 'l2.jpg', 'Die Gestaltung von Flächen schafft im besten Fall eine besondere Atmosphäre oder erweckt Architektur zu neuem Leben. Wir finden das Passende für Sie.', ['Vielzahl an Gestaltungsmöglichkeiten']),
            ('Industrieanstriche', 'l3.jpg', 'Schutz, Instandhaltung und ein repräsentatives Erscheinungsbild. Wo sinnvoll, setzen wir Hubsteiger statt Gerüst ein, damit Ihr Betrieb weiterläuft.', ['Hubsteiger statt Einrüsten']),
            ('Denkmalschutz', 'l4.jpg', 'Altes erhalten und neu zur Geltung bringen, mit den richtigen Materialien für historische Fassaden.', []),
            ('Keramische Beläge', 'l5.jpg', 'Naturstein, Klinkerriemchen oder Verblender auf dem Dämmsystem, auch um bei Altbauten die ursprüngliche Fassadenoptik wiederherzustellen.', [])])
        + gallery('referenzen', 'Referenzen', 'Ein Blick auf <em>unsere Fassaden.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%')])
        + story('preise', 'Auszeichnungen', 'Ausgezeichnet <em>für schönere Fassaden.</em>', [
            'Beim Deutschen Fassadenpreis von Brillux wurden wir 2014 und 2016 jeweils mit dem 3. Preis ausgezeichnet: für den Wohnpark Bathildis in Bad Pyrmont und das Klinikum in Lemgo.',
            'Beim Bielefelder Fassadenwettbewerb 2010 waren wir gleich dreifach Preisträger: Bestes Mehrfamilienhaus, Beste energetische Sanierung und Bürgerpreis.'],
            'aw.jpg', 'Urkunde Deutscher Fassadenpreis 2016', cls='alt',
            tl=[('2016', 'Ehrenurkunde der Handwerkskammer zum 50-jährigen Bestehen'), ('Alsecco', 'zertifiziert für Hanf-Fassadendämmung')])
        + story('ueber', 'Über uns', 'Ein Ansprechpartner, <em>vom ersten Gespräch bis zur Abnahme.</em>', [
            'Joswieg ist ein modernes Dienstleistungsunternehmen. Auf einen optimierten Ablauf und sorgfältige Planung können Sie sich verlassen. Schnell, sauber, innovativ und zuverlässig schafft das Joswieg-Team Lösungen für jede Auftragssituation.',
            'Damit alles reibungslos läuft, haben Sie immer einen festen Ansprechpartner. Überzeugen Sie sich und nehmen Sie uns beim Wort. Ihre Familie Joswieg'],
            'ab.jpg', 'Beratung bei Joswieg an der Ravensberger Bleiche', rev=True, cls='dk',
            tl=[('Daniel Joswieg', 'Malermeister, Geschäftsführer'), ('Förderung', 'Netzwerkpartner für KfW und Energieausweise')])
        + contact(s) + footer(s))

P2, D2 = '#e2001a', '#1d1d1b'
S = SITES['joswieg'] = site(
    slug='joswieg-malerbetrieb-bielefeld', firma='Joswieg Malerbetrieb GmbH', web='joswieg.de', fonts='r31jo', branche='Malerbetrieb',
    title='Joswieg Malerbetrieb – Maler und Fassaden in Bielefeld', desc='Joswieg Malerbetrieb in Bielefeld seit 1966: Malerarbeiten, Fassadenanstriche, Wärmedämmverbundsysteme, Hanf-Dämmung, Denkmalschutz. Deutscher Fassadenpreis 2014 und 2016.',
    tel='0521 48333', tel_i='+4952148333', mail='info@joswieg.de', adresse='Ravensberger Bleiche 14, 33649 Bielefeld', google=None,
    cta='Beratung anfragen', nav=[('Dämmung', 'wdvs'), ('Leistungen', 'leistungen'), ('Referenzen', 'referenzen'), ('Preise', 'preise'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung')],
    form_opts=['Wärmedämmung / WDVS', 'Fassadenanstrich', 'Malerarbeiten innen', 'Industrieanstrich', 'Denkmalschutz', 'Energieausweis / Förderung', 'Sonstiges'],
    form_h3='Beratung anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Was auch immer Sie sich wünschen: <em>Wir unterstützen Sie.</em>', kt_p='Rufen Sie an oder schreiben Sie uns.',
    social=[('Instagram', 'https://www.instagram.com/joswieg_malerbetrieb/')],
    vars=V.format(ink='#1d1d1b', mute='#45454a', p=P2, pi='#fff', dk=D2, s2='#f5f5f4', fh='"Archivo",system-ui,sans-serif', fb='"Inter",system-ui,sans-serif', lh=60, ft=D2),
    css=css_hw(P2, D2, '.hz .hz-big{color:rgba(226,0,26,.07)}.promo .tag{background:#e2001a;color:#fff}.ft img{background:#fff;padding:8px 12px;height:66px}'))
S['css2'] = hz('#fff', P2)
S['logo'] = 'logo.png'
S['bot'] = BOT('Rolle', 'Ihr Maler-Lotse', 'Joswieg', S, [
    ['Was ist Ihre Spezialität?', 'Wärmedämmverbundsysteme und Fassaden. Wir dämmen auch mit Hanf, zertifiziert von Alsecco.'],
    ['Helfen Sie bei Fördermitteln?', 'Ja. Unsere Netzwerkpartner beraten zu KfW-Programmen, wir erstellen Energieausweise mit Gutachtern.'],
    ['Wie erreiche ich Sie?', 'Telefon 0521 48333 oder info@joswieg.de.']],
    ['#wdvs', '#leistungen', '#referenzen', '#kontakt'])
S['img'] = {'logo.png': (I('joswieg', 0)[0], 300, 'alphacrop'), 'h1.jpg': I('joswieg', 41), 'h2.jpg': I('joswieg', 1), 'h3.jpg': I('joswieg', 55),
    'wd.jpg': I('joswieg', 45, 1400), 'l1.jpg': I('joswieg', 43, 1200), 'l2.jpg': I('joswieg', 99, 1200), 'l3.jpg': I('joswieg', 77, 800), 'l4.jpg': I('joswieg', 69, 1000), 'l5.jpg': I('joswieg', 104, 1200),
    'g1.jpg': I('joswieg', 10, 1400), 'g2.jpg': I('joswieg', 91, 750), 'g3.jpg': I('joswieg', 83, 750), 'g4.jpg': I('joswieg', 89, 750), 'g5.jpg': I('joswieg', 102, 750), 'g6.jpg': I('joswieg', 42, 1400),
    'aw.jpg': I('joswieg', 111, 750), 'ab.jpg': I('joswieg', 20, 1200)}
S['body'] = b_joswieg

# ───────────── 3 · Kohnen & Meyer Malerbetriebs GmbH, Cloppenburg ─────────────
def b_kohnen(s):
    return (hd(s) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 50%', 'h2.jpg': '50% 50%', 'h3.jpg': '50% 50%'}, big='',
        ubar=[('Seit 1980', 'in Cloppenburg'), ('Vor Ort', 'Ausstellung mit Beratung'), ('Böden', 'aus einer Hand')],
        ey='Kohnen & Meyer · Ihr Maler & Lackierer aus Cloppenburg',
        h1='Wände mit <em>Charakter.</em>',
        sub='Farbliche Neugestaltung, dekorative Wandgestaltung, Tapezierarbeiten und neue Böden: Wir stehen Ihnen mit Kreativität, handwerklichem Geschick und Erfahrung zur Seite.'))
        + duo('angebote', 'Unsere Angebote', 'Von der Wand <em>bis zum Boden.</em>', 'Neben klassischen Malerarbeiten bieten wir Ihnen Raumgestaltungen und Raumaufteilungen nach Ihren Wünschen.', [
            ('Maler & Lackierer', 'Wände, Tapeten, Lack', 'w1.jpg', 'Streich-, Tapezier- und Lackierarbeiten innen und außen. Wir lackieren oder lasieren Vertäfelungen, Verkleidungen, Zäune und Treppengeländer.', ['Dekorative Wandgestaltung', 'Designtapeten', 'Renovierung ganzer Wohnungen'], 'Beratung anfragen'),
            ('Bodenleger', 'Parkett, Design, Teppich', 'w2.jpg', 'Wir verlegen Teppichböden, Parkett, Design-Beläge, PVC und Linoleum und bereiten alte Böden wieder auf.', ['Parkett schleifen und ölen', 'Vinyl- und Linoleum-Sanierung', 'Leistenmontage'], 'Boden anfragen')])
        + gallery('referenzen', 'Referenzen', 'Lassen Sie sich <em>inspirieren.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 40%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%')])
        + promo('ausstellung', 'au.jpg', 'Ausstellung', 'Sehen und fühlen, <em>bevor es an die Wand geht.</em>',
                'In unserer Ausstellung am Lankumer Ring 6 können Sie sich einen Eindruck von hochwertigen Tapeten, Bodenbelägen und Techniken verschaffen und sich von unserem Fachpersonal ausführlich beraten lassen.',
                ['Tapeten, Böden und Techniken zum Anfassen', 'Persönliche Beratung vor Ort'], 'Termin vereinbaren', 'alt')
        + svc('leistungen', 'Leistungen', 'Wir erfüllen <em>vielfältige Kundenwünsche.</em>', 'Für Kunden im privaten, öffentlichen und gewerblichen Bereich.', [
            ('Streichen, Tapezieren, Lackieren', 'Sämtliche Arbeiten innen und außen, sauber und termintreu.'),
            ('Bodenbeläge', 'Teppichböden, Parkett, Design-Beläge, PVC, Linoleum und mehr fachgerecht verlegt.'),
            ('Bodensanierung', 'Alte Parkettböden, Linoleum oder Vinyl aufbereiten.'),
            ('Reinigung', 'Von Fassaden, Dachflächen und Gehwegen.'),
            ('Wärmedämmverbundsystem', 'Planung und Ausführung aus einer Hand.'),
            ('Gerüstbau', 'Eigene Gerüstbauarbeiten, damit es zügig vorangeht.')])
        + marquee(['Brillux', 'Herbol', 'KEIM', 'Sigma Coatings', 'Storch', 'Metylan', 'Marburg', 'Omexco', 'Jordan', 'Weigel'], 'wm')
        + story('ueber', 'Über uns', 'Ein Cloppenburger <em>Traditionsunternehmen.</em>', [
            'Als Cloppenburger Traditionsunternehmen betreuen wir seit 1980 unsere Kunden. Ob Sie im nicht mehr genutzten Kinderzimmer Ihr Homeoffice einrichten oder die gesamte Wohnung neu gestalten möchten: Wir sind der Partner an Ihrer Seite.',
            'Wir verstehen uns als moderner Malerbetrieb, der sich regelmäßig weiterbildet, um am Puls der Zeit zu bleiben. Wir suchen Maler und Lackierer sowie Bodenleger (m/w/d).'],
            'ab.jpg', 'Unterwegs für Kohnen & Meyer', cls='dk',
            tl=[('Thomas Meyer', 'Geschäftsführer'), ('Yvonne Klänelschen-Meyer', 'Geschäftsführerin')])
        + contact(s) + footer(s))

P3, D3 = '#005895', '#0b2f4f'
S = SITES['kohnen'] = site(
    slug='kohnen-meyer-maler-cloppenburg', firma='Kohnen & Meyer Malerbetriebs GmbH', web='maler-kohnen-meyer.de', fonts='r31km', branche='Malerbetrieb',
    title='Kohnen & Meyer – Maler & Lackierer in Cloppenburg', desc='Kohnen & Meyer Malerbetriebs GmbH in Cloppenburg seit 1980: Malerarbeiten, Wandgestaltung, Tapeten, Bodenbeläge, Parkett, Wärmedämmung. Ausstellung am Lankumer Ring 6.',
    tel='04471 947190', tel_i='+494471947190', mail='info@maler-kohnen-meyer.de', adresse='Lankumer Ring 6, 49661 Cloppenburg', google=None,
    cta='Angebot anfragen', nav=[('Angebote', 'angebote'), ('Referenzen', 'referenzen'), ('Ausstellung', 'ausstellung'), ('Leistungen', 'leistungen'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Beratung', 'nach Vereinbarung')],
    form_opts=['Malerarbeiten / Wandgestaltung', 'Tapezieren', 'Bodenbelag / Parkett', 'Bodensanierung', 'Fassade / Wärmedämmung', 'Bewerbung', 'Sonstiges'],
    form_h3='Unverbindliches Angebot', form_p='Sagen Sie uns kurz, was Sie vorhaben. Wir nehmen uns Zeit für Sie.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Sie möchten beraten werden? <em>Wir sind für Sie da.</em>', kt_p='Besuchen Sie uns in Cloppenburg, rufen Sie an oder schreiben Sie uns.',
    social=[('Instagram', 'https://www.instagram.com/kohnenundmeyer/')],
    vars=V.format(ink='#13283a', mute='#3d5060', p=P3, pi='#fff', dk=D3, s2='#f2f6fa', fh='"Josefin Sans",system-ui,sans-serif', fb='"Open Sans",system-ui,sans-serif', lh=62, ft=D3),
    css=css_hw(P3, D3, '.h2,.hz h1{font-weight:700;letter-spacing:-.01em}.hz h1 em,.h2 em{color:#005895;background:linear-gradient(transparent 62%,#ffe500 62%)}.dk .h2 em{background:none;color:#ffe500;text-decoration:none}.promo .tag{background:#ffe500;color:#0b2f4f}.duo .tx small{color:#005895}.st.dk .ey{color:#ffe500}.ft img{background:#fff;padding:8px 12px;height:70px}'))
S['css2'] = hz('#fff', P3)
S['logo'] = 'logo.png'
S['bot'] = BOT('Farbtupfer', 'Ihr Maler-Lotse', 'Kohnen & Meyer', S, [
    ['Verlegen Sie auch Böden?', 'Ja: Teppich, Parkett, Design-Beläge, PVC und Linoleum. Alte Böden bereiten wir auch wieder auf.'],
    ['Kann ich Tapeten ansehen?', 'Ja, in unserer Ausstellung am Lankumer Ring 6 in Cloppenburg, mit persönlicher Beratung.'],
    ['Wie erreiche ich Sie?', 'Telefon 04471 947190 oder info@maler-kohnen-meyer.de.']],
    ['#angebote', '#referenzen', '#ausstellung', '#kontakt'])
S['img'] = {'logo.png': (I('kohnen', 15)[0], 300), 'h1.jpg': I('kohnen', 23), 'h2.jpg': I('kohnen', 24, 1600), 'h3.jpg': I('kohnen', 18, 1080),
    'w1.jpg': I('kohnen', 21, 1200), 'w2.jpg': I('kohnen', 29, 1200),
    'g1.jpg': I('kohnen', 22, 1080), 'g2.jpg': I('kohnen', 20, 900), 'g3.jpg': I('kohnen', 17, 900), 'g4.jpg': I('kohnen', 24, 1200), 'g5.jpg': I('kohnen', 30, 1200), 'g6.jpg': I('kohnen', 28, 1080),
    'au.jpg': I('kohnen', 26, 1400), 'ab.jpg': I('kohnen', 16, 1400)}
S['body'] = b_kohnen
