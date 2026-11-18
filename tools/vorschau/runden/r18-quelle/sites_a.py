"""Runde 18 · Teil A: Sartorius Lastrup, Nowatzke Melle, Ofenhaus Colnrade, Ofen Schulte Bawinkel."""
from common import *
SITES = {}

# ───────────── 1. Sartorius GmbH, Lastrup ─────────────
def b_sartorius(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 50%', 'h2.jpg': '50% 50%', 'h3.jpg': '60% 50%'},
        ey='Sartorius · Kachelöfen und Kamine · Lastrup und Oldenburg',
        h1='Wir gestalten <em>Wärme.</em>',
        sub='Über 140 Öfen und Kamine in unseren Ausstellungen, vom Herd über den Kachelofen bis zum Kamin. Meisterbetrieb seit 1981, mit eigenem Team für Beratung, Lieferung und Montage.',
        ubar=[('Seit 1981', 'Fachbetrieb für Feuerstätten'), ('Über 140 Modelle', 'in zwei Kaminstudios'), ('30 Mitarbeiter', 'eingetragener Meisterbetrieb')]))
        + spot('feuer', 'Live in unserer Ausstellung', 'Feuer muss man <em>sehen.</em>', 'In Lastrup und Oldenburg brennen unsere Kamine für Sie. Kommen Sie vorbei, setzen Sie sich davor und spüren Sie den Unterschied.', 'feuer.mp4', 'feuer.jpg', 'nos')
        + marquee(['Kaminöfen', 'Kachelöfen', 'Kamine', 'Gaskamine', 'Pelletöfen', 'Specksteinöfen', 'Herde', 'Elektrokamine', 'Warmluftkassetten nach Maß', 'Wasserführende Kaminöfen'], 'wm')
        + panels('produkte', 'Unsere Feuerstätten', 'Für jede Aufstellsituation <em>das passende Feuer.</em>', 'Eine Auswahl aus unseren Ausstellungen. Alles Weitere zeigen wir Ihnen gerne persönlich.', [
            ('Kaminöfen', 'p1.jpg', 'Schnelle Wärme, wenig Einsatz. Mit moderner Stahlverkleidung, Naturstein oder Kachel, passend zu Ihrem Einrichtungsstil.', '50% 50%'),
            ('Kamine', 'p2.jpg', 'Front-, Eck- oder Panoramakamin, individuell geplant für Ihren Wohnstil. Mit Natursteinbank oder großzügiger Kachelverkleidung.', '50% 50%'),
            ('Kachelöfen', 'p3.jpg', 'Der traditionelle Wärmespeicher: nimmt viel Wärme auf und gibt sie über Stunden in Ihre Räume ab.', '50% 50%'),
            ('Gaskamine', 'p4.jpg', 'Wohlige Wärme auf Knopfdruck. Das Feuer zünden Sie per Fernbedienung, die Optik wählen Sie frei.', '50% 50%'),
            ('Pelletöfen', 'p5.jpg', 'Heizen automatisch mit Holzpellets und sehen aus wie klassische Kaminöfen.', '50% 50%')])
        + promo('kassette', 'kas.jpg', 'Warmluftkassetten nach Maß', 'Ihr offener Kamin heizt <em>endlich richtig.</em>',
                'Bei einem offenen Kamin geht der Großteil der Wärme verloren. Eine Kaminkassette löst dieses Problem, bietet mehr Heizleistung und reguliert den Abbrand. Wir fertigen sie passend für Ihren Kamin.',
                ['Mehr Heizleistung aus dem vorhandenen Kamin', 'Nach Maß gefertigt', 'Beratung zur Bundes-Immissionsschutzverordnung inklusive'], 'Kassette anfragen', 'alt')
        + svc('leistungen', 'Unsere Leistungen', 'Alles aus <em>einer Hand.</em>', 'Sartorius ist Fachbetrieb für Feuerstätten und eingetragener Meisterbetrieb.', [
            ('Beratung nach Maß', 'Individuell und umfassend, in unseren Ausstellungen in Lastrup und Oldenburg.'),
            ('Lieferung und Montage', 'Unser eigenes Team liefert, baut auf und schließt an.'),
            ('Service und Betreuung', 'Wir sind auch nach dem ersten Feuer für Sie da.'),
            ('Kaminarchitektur', 'Kachelöfen und Kamine mit und ohne Steuerungs- und Regelungstechnik, Pelletsysteme, Wassertechnik.')])
        + story('ueber', 'Moderner Traditionsbetrieb', 'Familie Dreckmann und <em>30 Mitarbeiter.</em>', [
            '1981 von Horst Sartorius gegründet, wird die Sartorius GmbH seit 1997 von Dieter Dreckmann geführt. Gemeinsam mit seinem Sohn Kevin und 30 Mitarbeitern bildet er ein Team, das Wert auf Teamgeist, ständige Weiterbildung und die Förderung junger Menschen in der Ausbildung legt.',
            'In unseren Kaminstudios an der Molberger Straße in Lastrup und Am Patentbusch in Oldenburg finden Sie Kachelöfen, Specksteinöfen, Kamine und Kaminöfen aller führenden Hersteller.'], 'bau.jpg', 'Kachelofenbau in Handarbeit', cls='dk',
            tl=[('1981', 'gegründet'), ('1997', 'Dieter Dreckmann übernimmt'), ('2 Studios', 'Lastrup und Oldenburg')])
        + gallery('galerie', 'Einblicke', 'So kann Ihr Wohnzimmer <em>aussehen.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', 'w2', '50% 50%')])
        + reviews(s, ['Die Idee kam von Instagram, Sartorius hat sie perfekt umgesetzt. Nichts von der Stange. Saubere Arbeit, freundliche Mitarbeiter.',
                      'Von der Planung über die Beratung bis zum Einbau lief alles perfekt. Der Inhaber hat sich persönlich Zeit für alle Fragen genommen.',
                      'Die Monteure waren sehr kompetent, haben sauber und zügig gearbeitet. Das Ergebnis ist einfach perfekt.',
                      'Liefer- und Montagetermin wurden eingehalten. Die Monteure haben gut und sauber gearbeitet.'])
        + contact(s) + footer(s))

S = SITES['sartorius'] = site(
    slug='sartorius-kamine-lastrup', firma='Sartorius GmbH', web='sartorius-kamine.de', fonts='r10liekam',
    title='Sartorius Kachelöfen und Kamine – Lastrup und Oldenburg', desc='Sartorius in Lastrup: Kaminöfen, Kachelöfen, Kamine, Gaskamine und Pelletöfen. Über 140 Modelle in der Ausstellung, Meisterbetrieb seit 1981.',
    tel='04472 1324', tel_i='+4944721324', mail='info@sartorius-kamine.de', adresse='Molberger Straße 4, 49688 Lastrup', google=('4,8', 133),
    cta='Beratungstermin anfragen', nav=[('Feuerstätten', 'produkte'), ('Kassetten', 'kassette'), ('Leistungen', 'leistungen'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '10:00 – 12:00, 14:00 – 18:00'), ('Sa', '9:00 – 13:00')],
    form_opts=['Kaminofen', 'Kamin / Kachelofen', 'Gaskamin', 'Pelletofen', 'Warmluftkassette', 'Alten Ofen tauschen', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Kommen Sie <em>ans Feuer.</em>', kt_p='Besuchen Sie unsere Ausstellung in Lastrup oder schreiben Sie uns.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#2b3136', mute='#5a5f66', p='#9B2929', pi='#fff', dk='#2E0E0E', s2='#fcfaf8', fh='"Roboto",system-ui,sans-serif', fb='"Roboto",system-ui,sans-serif', lh=78, ft='#2E0E0E'),
    css='''.hs h1,.h2{font-weight:900;letter-spacing:-.02em;line-height:1.02}.hs h1{font-size:clamp(46px,7vw,116px)}.hs h1 em,.h2 em{font-style:normal;color:#e0563f}.h2 em{color:#9B2929}.dk .h2 em{color:#f08a6c}
.mq.wm span{font-weight:700;letter-spacing:.04em;font-size:15px}.alt{background:var(--s2)}.sv .row div{border-top:4px solid #9B2929}.hs .ubar b{color:#fff}
.st.dk{background:#2E0E0E;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.sp16.nos .snd{display:none}.hs .ey{color:#ffd9cc!important}.sp16.nos{background:#2E0E0E;color:#fff}.sp16.nos .lead{color:rgba(255,255,255,.85)}.sp16.nos .h2 em{color:#f08a6c}
.ft img{background:#fff;padding:8px 12px;height:86px}''')
S['bot'] = BOT('Flamme', 'Ihr Ofen-Lotse', 'Sartorius', S, [
    ['Öffnungszeiten', 'Mo–Fr 10:00–12:00 und 14:00–18:00 Uhr, Sa 9:00–13:00 Uhr oder nach Vereinbarung.'],
    ['Wo ist die Ausstellung?', 'Molberger Straße 4 in Lastrup, ein zweites Kaminstudio finden Sie Am Patentbusch in Oldenburg.'],
    ['Muss mein alter Ofen raus?', 'Das hängt vom Baujahr ab. Wir beraten Sie zur Bundes-Immissionsschutzverordnung. Telefon: 04472 1324.']],
    ['#produkte', '#kassette', '#leistungen', '#kontakt'])
S['img'] = {'logo.png': ('/home/claude/r18raw/sartorius/logo.png', 0), 'h1.jpg': I('sartorius', 5, 0), 'h2.jpg': I('sartorius', 7, 0), 'h3.jpg': I('sartorius', 48, 0),
    'feuer.mp4': ('/home/claude/r18raw/sartorius/feuer_web.mp4', 0), 'feuer.jpg': ('/home/claude/r18raw/sartorius/feuer.jpg', 0),
    'p1.jpg': I('sartorius', 28), 'p2.jpg': I('sartorius', 139), 'p3.jpg': I('sartorius', 136), 'p4.jpg': I('sartorius', 132), 'p5.jpg': I('sartorius', 138),
    'kas.jpg': I('sartorius', 123), 'bau.jpg': I('sartorius', 143), 'g1.jpg': I('sartorius', 30), 'g2.jpg': I('sartorius', 31), 'g3.jpg': I('sartorius', 137), 'g4.jpg': I('sartorius', 95)}
S['body'] = b_sartorius

# ───────────── 2. Kamin- und Kachelofenbau Siegbert Nowatzke, Melle ─────────────
def b_nowatzke(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='130',
        ubar=[('Etwa 130', 'Kamine und Öfen im Jahr'), ('Über 30 Jahre', 'Erfahrung als Meisterbetrieb'), ('Ausstellung', 'in Melle, Euer Heide')],
        ey='Kamin- und Kachelofenbau Nowatzke · Melle',
        h1='Kamine und Kachelöfen <em>aus Meisterhand.</em>',
        sub='Bei uns ist jeder Heizkamin und jeder Kachelofen ein Unikat. Wir beraten, planen und bauen für die Region Osnabrück-Bielefeld.'))
        + marquee(['Melle', 'Osnabrück', 'Bielefeld', 'Bünde', 'Bissendorf', 'Bad Oeynhausen', 'Grundöfen', 'Heizkamine', 'Kachelöfen', 'Gaskamine', 'Kaminöfen'], 'wm')
        + scroller('galerie', 'Aus unserer Galerie', 'Gebaut von uns, <em>bei Kunden zu Hause.</em>', 'Keine Prospektbilder: Diese Kamine und Kachelöfen stehen in Wohnzimmern in der Region.', [
            ('Kachelofen mit Sitzbank', 'g1.jpg', 'Über Eck gebaut, mit Holzfach und warmer Bank.', '50% 50%'),
            ('Heizkamin, dreiseitig', 'g2.jpg', 'Freie Sicht aufs Feuer von drei Seiten.', '50% 50%'),
            ('Klassischer Kachelofen', 'g3.jpg', 'Mit Keramik verkleidet, passend zum Landhausstil.', '50% 50%'),
            ('Moderner Eckkamin', 'g4.jpg', 'Geradlinig, verputzt, mit Natursteinbank.', '50% 50%'),
            ('Kamin als Raumteiler', 'g5.jpg', 'Wohnen und Essen, verbunden durch das Feuer.', '50% 50%'),
            ('Kachelofen im Fachwerkhaus', 'g6.jpg', 'Neu gebaut, als wäre er schon immer da gewesen.', '50% 50%')])
        + ablauf('weg', 'So entsteht Ihr Ofen', 'Beratung, Planung, <em>Ofenbau.</em>', 'Drei Schritte, ein Ansprechpartner.', [
            ('Beratung', 'In unserer Ausstellung und bei Ihnen zu Hause: Welcher Ofentyp passt zu Ihren Wünschen und Ihren Räumen?'),
            ('Planung', 'Dank CAD-Software sehen Sie Ihren Ofen maßstabsgetreu in Ihren eigenen Räumen, bevor wir bauen.'),
            ('Ofenbau', 'Unsere Fachleute verarbeiten ausschließlich hochwertige Materialien. Wir decken großflächig ab und halten den Staub gering.')])
        + promo('ausstellung', 'aus.jpg', 'Kaminausstellung Melle', 'Nehmen Sie Platz auf der <em>warmen Ofenbank.</em>',
                'In unserer gemütlichen Ausstellung im Meller Gewerbegebiet Euer Heide zeigen wir Ihnen von Grund auf gemauerte Kachelöfen, Heizkamine, eine Gaskaminanlage sowie Kamin- und Speicheröfen unserer Partner.',
                ['Grundöfen mit hochwertiger Schamotte', 'Heizkamine im modernen Design', 'Kaminöfen von Spartherm und Leda, Speicheröfen von Tonwerk'], 'Besuch vereinbaren', 'alt')
        + story('ueber', 'Ihr Fachbetrieb', 'Etwa 130 Kamine und Öfen <em>im Jahr.</em>', [
            'Als Meisterbetrieb mit mehr als 30-jähriger Erfahrung stehen wir für ausgeklügelte Heiztechnik und höchste Qualität. Jeder einzelne Ofen ist eine individuelle Anfertigung, die zu Ihrem Stil und Ihren Bedürfnissen passt.',
            'Ob Neubau oder nachträglicher Einbau: Die Sorge vor einer lauten und staubigen Baustelle ist unbegründet.'], 'haus.jpg', 'Unsere Ausstellung am Ochsenweg in Melle', cls='dk',
            tl=[('Inhaber', 'Arne Funke'), ('Meisterbetrieb', 'für Kachelöfen und Kamine')])
        + reviews(s, ['Von der ersten Beratung bis zur Montage äußerst professionell und zuverlässig. Er hat sich viel Zeit genommen und kreative Lösungen gefunden.',
                      'Uns war wichtig, das Aussehen unseres alten Ofens zu erhalten. Herr Funke und sein Team haben das perfekt gelöst. Viel mehr Wärme mit weniger Holz.',
                      'Der Kamin wurde pünktlich fertig und genau so, wie ich ihn mir vorgestellt hatte.',
                      'Beratung ausgezeichnet, alle sehr freundlich. Lieferung und Einbau gingen schnell und reibungslos.'])
        + contact(s) + footer(s))

S = SITES['nowatzke'] = site(
    slug='kaminbau-nowatzke-melle', firma='Kamin- und Kachelofenbau Siegbert Nowatzke e.K.', web='nowatzke.de', fonts='r18now',
    title='Nowatzke – Kamine und Kachelöfen aus Meisterhand, Melle', desc='Kamin- und Kachelofenbau Nowatzke in Melle: Grundöfen, Heizkamine, Kachelöfen und Kaminöfen. Etwa 130 Unikate im Jahr, Ausstellung in Melle.',
    tel='05422 44659', tel_i='+49542244659', mail='kontakt@nowatzke.de', adresse='Ochsenweg 9, 49324 Melle', google=('4,9', 27),
    cta='Beratung vereinbaren', nav=[('Galerie', 'galerie'), ('Ablauf', 'weg'), ('Ausstellung', 'ausstellung'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '8:00 – 12:00'), ('Fr', '15:00 – 17:00'), ('Sa', 'nach Terminvereinbarung')],
    form_opts=['Kachelofen / Grundofen', 'Heizkamin', 'Gaskamin', 'Kaminofen', 'Alten Ofen modernisieren', 'Sonstiges'],
    form_h3='Beratung vereinbaren', form_p='Sagen Sie uns kurz, was Sie sich vorstellen. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Welcher Ofen <em>passt zu Ihnen?</em>', kt_p='Besuchen Sie unsere Ausstellung in Melle oder schicken Sie uns eine Nachricht.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#333', mute='#555', p='#860000', pi='#fff', dk='#3a0a0a', s2='#f7f3ee', fh='"Gudea",system-ui,sans-serif', fb='"Gudea",system-ui,sans-serif', lh=84, ft='#2a0808'),
    css='''.h2,.hz h1{font-weight:700;letter-spacing:-.015em}.h2 em,.hz h1 em{font-style:normal;color:#860000}.dk .h2 em{color:#ffb38a}.mq.wm span{font-weight:700;font-size:16px}
.alt{background:var(--s2)}.st.dk{background:#3a0a0a;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.rd .road div h3{color:#860000}.ft img{height:96px}''')
S['css2'] = '.hz{--hz-bg:#f7f3ee;--hz-ink:#2b2b2b;--hz-mute:#5a5a5a;--hz-stroke:rgba(134,0,0,.16);--hz-cols:45fr 55fr}.hz h1{font-size:clamp(36px,4.4vw,70px)}.hz .ey{color:#860000}.hz .hz-big{font-weight:700}'
S['bot'] = BOT('Glut', 'Ihr Ofen-Lotse', 'Nowatzke', S, [
    ['Öffnungszeiten', 'Mo–Fr 8:00–12:00 Uhr, Fr zusätzlich 15:00–17:00 Uhr, Sa nach Terminvereinbarung.'],
    ['Wo ist die Ausstellung?', 'Ochsenweg 9 in Melle, im Gewerbegebiet Euer Heide. Gut erreichbar von Osnabrück, Bünde und Bielefeld.'],
    ['Geht ein Ofen auch nachträglich?', 'Ja, auch ein nachträglicher Einbau eines Grundofens oder Kamins ist möglich. Telefon: 05422 44659.']],
    ['#galerie', '#weg', '#ausstellung', '#kontakt'])
G = '/home/claude/r18raw/nowatzke/gal/'
S['img'] = {'logo.png': I('nowatzke', 4, 0), 'h1.jpg': (G + 'g02.jpg', 1700), 'h2.jpg': (G + 'g03.jpg', 1700), 'h3.jpg': (G + 'g01.jpg', 1700),
    'g1.jpg': (G + 'g10.jpg', 1300), 'g2.jpg': (G + 'g11.jpg', 1300), 'g3.jpg': (G + 'g04.jpg', 1300), 'g4.jpg': (G + 'g13.jpg', 1300), 'g5.jpg': (G + 'g09.jpg', 1300), 'g6.jpg': (G + 'g12.jpg', 1300),
    'aus.jpg': (G + 'g15.jpg', 1400), 'haus.jpg': I('nowatzke', 12, 0)}
S['body'] = b_nowatzke

# ───────────── 3. Ofenhaus Colnrade ─────────────
def b_colnrade(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 60%', 'h2.jpg': '50% 40%', 'h3.jpg': '50% 50%'},
        ey='Ofenhaus Colnrade · Ofenerlebniswelt seit 1981',
        h1='Wir machen Öfen <em>zum Erlebnis.</em>',
        sub='Umfangreiche Ofenausstellung, eigene Manufaktur zum Anfassen und ein Café unter einem Dach. Wir beraten, liefern an und bauen auf.',
        ubar=[('Seit 1981', 'Familie Dauskardt, zwei Generationen'), ('Eigene Manufaktur', 'Heimat des Bremer Grundofens'), ('Auch sonntags', 'Café von 14 bis 18 Uhr')]))
        + marquee(['Grundofen', 'Kaminofen', 'Specksteinofen', 'Dauerbrandofen', 'Heizkamin', 'Kachelofen', 'Holzherde und Küchenöfen', 'Pelletofen', 'Edelstahlschornstein'], 'wm')
        + panels('oefen', 'Unsere Öfen', 'Welches Feuer <em>passt zu Ihnen?</em>', 'Ein Auszug aus unserer Ausstellung in Colnrade.', [
            ('Grundofen', 'p1.jpg', 'Unsere Expertise für Speicheröfen: lange, gleichmäßige Wärme aus eigener Fertigung.', '50% 50%'),
            ('Kaminofen', 'p2.jpg', 'Schnell warm, schön anzusehen und in vielen Formen zu haben.', '50% 50%'),
            ('Specksteinofen', 'p3.jpg', 'Speichert die Wärme im Stein und gibt sie über Stunden ab.', '50% 50%'),
            ('Heizkamin', 'p4.jpg', 'Individuell gefertigt, passend zu Ihrem Zuhause.', '50% 50%'),
            ('Küchenofen', 'p5.jpg', 'Kochen und heizen mit Holz, mitten in der Küche.', '50% 50%')])
        + promo('ofentausch', 'tausch.jpg', 'Ofentausch', 'Der beste Zeitpunkt für <em>einen neuen Ofen.</em>',
                'Die Bundes-Immissionsschutzverordnung zwingt viele Ofenbesitzer zu einer Entscheidung: nachrüsten oder gleich neu kaufen? Wir schauen uns Ihren Ofen an, beraten ehrlich und setzen um.',
                ['Beratung zu Nachrüstung oder Austausch', 'Abbau des alten und Aufbau des neuen Ofens', 'Jederzeit telefonisch erreichbar'], 'Ofentausch anfragen', 'alt')
        + story('manufaktur', 'Eine Manufaktur zum Anfassen', 'Individuelle Ofenfertigung <em>bei uns im Haus.</em>', [
            'Mit der Ofenmanufaktur und dem Bremer Grundofen sind wir neue Wege gegangen. In Colnrade sehen Sie, wie unsere Speicheröfen entstehen.',
            'Kreative Ideen und viel Erfahrung helfen uns dabei, Ihre neue Feuerstelle zusammen mit Ihnen zu planen.'], 'manu.jpg', 'Aus unserer Ofenmanufaktur', rev=True,
            tl=[('CO2-neutral', 'Holzfeueröfen'), ('Speicheröfen', 'unsere Expertise')])
        + story('ueber', 'Unsere Leidenschaft seit 1981', 'Zwei Generationen, <em>ein Ofenhaus.</em>', [
            'Die Geschichte des Ofenhauses Colnrade ist mittlerweile mehrere Jahrzehnte und zwei Generationen lang. Im hektischen Alltag sind die eigenen vier Wände der schönste Rückzugsort. Wir haben es zu unserer Aufgabe gemacht, ihm mit der Wärme eines Ofens noch mehr Gemütlichkeit zu verleihen.',
            'Inhaber sind Björn Dauskardt (Leitung Ofenhaus) und Ole Dauskardt (Leitung Ofenmanufaktur).'], 'haus.jpg', 'Das Ofenhaus an der Dorfstraße in Colnrade', cls='dk',
            tl=[('Mo – Fr', '9 bis 18 Uhr durchgehend'), ('Sa', '9 bis 16 Uhr'), ('So', 'Café 14 bis 18 Uhr')])
        + gallery('galerie', 'Einblicke', 'Wärme und Gemütlichkeit <em>in jedem Haus.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', 'w2', '50% 50%')])
        + reviews(s, ['Die Auswahl ist riesig und schön präsentiert, sonntags gibt es sogar Kuchen. Man kann in Ruhe schauen, ohne gleich zum Kauf gedrängt zu werden.',
                      'Vom ersten Gespräch an fühlten wir uns in besten Händen. Die Beratung war kompetent, ehrlich und auf uns zugeschnitten.',
                      'Abbau des alten und Aufbau des neuen Ofens liefen absolut reibungslos, termingerecht und in bester Qualität.',
                      'Wir sind sehr glücklich mit dem Bremer Grundofen. Nach dem Anheizen genießen wir viele Stunden angenehme Wärme.'])
        + contact(s) + footer(s))

S = SITES['colnrade'] = site(
    slug='ofenhaus-colnrade', firma='Ofenhaus Colnrade', web='ofenhaus.de', fonts='r18col',
    title='Ofenhaus Colnrade – Ofenausstellung, Manufaktur und Café', desc='Ofenhaus Colnrade: Grundöfen, Kaminöfen, Specksteinöfen, Heizkamine und Kachelöfen. Große Ausstellung, eigene Ofenmanufaktur, seit 1981.',
    tel='04434 94840', tel_i='+494434948400', mail='info@ofenhaus.de', adresse='Dorfstraße 21, 27243 Colnrade', google=('4,7', 458),
    cta='Beratung anfragen', nav=[('Öfen', 'oefen'), ('Ofentausch', 'ofentausch'), ('Manufaktur', 'manufaktur'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 18:00'), ('Sa', '9:00 – 16:00'), ('So', '14:00 – 18:00 (Café, außer feiertags)')],
    form_opts=['Grundofen', 'Kaminofen', 'Specksteinofen', 'Heizkamin / Kachelofen', 'Pelletofen', 'Ofentausch', 'Sonstiges'],
    form_h3='Beratung anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Besuchen Sie unsere <em>Ofenerlebniswelt.</em>', kt_p='Wir brennen darauf, Ihre neue Feuerstelle mit Ihnen zusammen zu planen.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#303030', mute='#5a5552', p='#D41737', pi='#fff', dk='#3d2b25', s2='#f6f1ee', fh='"Noticia Text",Georgia,serif', fb='"Josefin Sans",system-ui,sans-serif', lh=66, ft='#2e211c'),
    css='''body{font-size:18px}.hs h1,.h2{font-weight:700;line-height:1.08}.hs h1{font-size:clamp(42px,6vw,96px)}.hs h1 em,.h2 em{font-style:italic;font-weight:400;color:#D41737}.hs h1 em{color:#ffb9a6}.dk .h2 em{color:#e8b9a6}
.mq.wm span{font-family:"Josefin Sans";font-weight:600;letter-spacing:.1em;text-transform:uppercase;font-size:14px}.alt{background:var(--s2)}.st.dk{background:#3d2b25;color:#fff}.st.dk .lead{color:rgba(255,255,255,.88)}.st.dk .tl b{color:#fff}
.ey{color:#7D584B}.hs .ey{color:#f1d8cd!important}.hs .ubar b{color:#fff}.btn{font-family:"Josefin Sans";font-weight:600;letter-spacing:.04em}''')
S['bot'] = BOT('Fuchs', 'Ihr Ofen-Lotse', 'Ofenhaus Colnrade', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–18 Uhr, Sa 9–16 Uhr, sonntags hat das Café von 14–18 Uhr geöffnet (außer feiertags).'],
    ['Muss mein alter Ofen raus?', 'Das kommt auf das Prüfjahr an. Wir beraten Sie zu Nachrüstung oder Austausch. Telefon: 04434 94840.'],
    ['Bauen Sie auch auf?', 'Ja. Wenn Sie Ihren Ofen gefunden haben, liefern wir an und bauen auf.']],
    ['#oefen', '#ofentausch', '#manufaktur', '#kontakt'])
S['img'] = {'logo.png': ('/home/claude/r18raw/colnrade/logo_big.png', 0, 'alphacrop'), 'h1.jpg': I('colnrade', 50, 0), 'h2.jpg': I('colnrade', 58, 0), 'h3.jpg': I('colnrade', 149, 0),
    'p1.jpg': I('colnrade', 103), 'p2.jpg': I('colnrade', 67), 'p3.jpg': I('colnrade', 105), 'p4.jpg': I('colnrade', 148), 'p5.jpg': I('colnrade', 94),
    'tausch.jpg': I('colnrade', 136), 'manu.jpg': I('colnrade', 68), 'haus.jpg': I('colnrade', 60),
    'g1.jpg': I('colnrade', 126), 'g2.jpg': I('colnrade', 115), 'g3.jpg': I('colnrade', 137), 'g4.jpg': I('colnrade', 154)}
S['body'] = b_colnrade

# ───────────── 4. Ofen Schulte GmbH, Bawinkel ─────────────
def b_schulte(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg'], side='l', big='1979',
        ubar=[('Seit 1979', 'Familienbetrieb im Emsland'), ('800 qm', 'Ausstellung in Bawinkel'), ('Rund 130', 'Feuerstätten zum Anfassen')],
        ey='Ofen Schulte · die Ofenmanufaktur im Emsland',
        h1='Feuer liefert einfach <em>die schönere Wärme.</em>',
        sub='Seit mehr als 40 Jahren Ihr Ansprechpartner für individuellen Kamin- und Ofenbau. Von der Beratung über den Einbau bis zu Service und Wartung.'))
        + marquee(['Kaminbau', 'Ofenbau', 'Gaskamine', 'Kaminöfen', 'Pelletöfen', 'Tulikivi-Specksteinöfen', 'Kachelöfen', 'Service und Wartung'], 'wm')
        + scroller('feuer', 'Unsere Feuerstätten', 'Modernes Design oder <em>zeitlose Ästhetik.</em>', 'Kamine und Öfen führender Hersteller aus Skandinavien, Österreich und Deutschland, dazu Kamine aus unserer eigenen Manufaktur.', [
            ('Kamin- und Ofenbau', 'f1.jpg', 'Individuell geplant und gefertigt, für Neubau, Renovierung oder Bestand.', '50% 50%'),
            ('Gaskamine', 'f2.jpg', 'Feuer auf Knopfdruck, sauber und komfortabel.', '50% 50%'),
            ('Kaminöfen', 'f3.jpg', 'Große Auswahl, direkt in der Ausstellung zu sehen.', '50% 50%'),
            ('Pelletöfen', 'f4.jpg', 'Automatisch heizen mit Holzpellets.', '50% 50%'),
            ('Tulikivi-Specksteinöfen', 'f5.jpg', 'Speichern die Wärme über viele Stunden.', '50% 50%'),
            ('Kachelöfen', 'f6.jpg', 'Stilvoll gefertigt, ganz nach Ihren Wünschen.', '50% 50%')])
        + promo('ausstellung', 'aus.jpg', '800 qm Ausstellung', 'Rund 130 Feuerstätten <em>live erleben.</em>',
                'In unserer Ausstellung in Bawinkel finden Sie Kamin- und Pelletöfen, Tulikivi-Specksteinöfen sowie stilvoll gefertigte Kamine, Gaskamine und Kachelöfen.',
                ['Mo – Fr 10:00 – 12:30 und 14:00 – 18:00 Uhr', 'Sa 9:00 – 13:00 Uhr', 'Schautag an einem Sonntag im Monat, 14 – 17 Uhr (ohne Beratung und Verkauf)'], 'Beratungstermin sichern', 'alt')
        + svc('service', 'Rundum-Service', 'Der komplette Kaminbau <em>aus einer Hand.</em>', 'Uns ist an einer langjährigen Partnerschaft mit unseren Kunden gelegen.', [
            ('Persönliche Beratung', 'Wir nehmen uns Zeit für Ihre Vorstellungen von Design und Einbau.'),
            ('Planung', 'Jede Feuerstätte planen wir individuell nach Ihren Wünschen.'),
            ('Einbau und Inbetriebnahme', 'Unser Meisterbetrieb übernimmt den kompletten Vorgang.'),
            ('Service und Wartung', 'Auch nach dem Einbau bleiben wir Ihr Ansprechpartner.')])
        + story('ueber', 'Seit Generationen geschätzt', 'In die Wiege gelegt: <em>Ofenbau seit 1979.</em>', [
            '1979 gründeten Edeltraud und Ewald Schulte den Handwerksbetrieb als eines der ersten Unternehmen für Kachelofen- und Kaminbau in Nordwest-Deutschland. Angefangen hat alles mit einem winzigen Ausstellungsraum und dem Lager in der häuslichen Garage.',
            'Heute führt Ofenbau-Meister Patrick Schulte den eingetragenen Meisterbetrieb für Ofen-, Kamin- und Luftheizungsbau.'], 'alt.jpg', 'Aus den Anfangsjahren von Ofen Schulte', cls='dk',
            tl=[('1979', 'Gründung in Bawinkel'), ('Heute', 'Patrick Schulte, Ofenbau-Meister')])
        + gallery('referenzen', 'Referenzen', 'Kamine und Öfen <em>unserer Kunden.</em>', [
            ('r1.jpg', 'w2 h2r', '50% 50%'), ('r2.jpg', '', '50% 50%'), ('r3.jpg', '', '50% 50%'), ('r4.jpg', 'w2', '50% 50%')])
        + reviews(s, ['Äußerst professionelle und kompetente Beratung. Man merkt sofort, dass Qualität an erster Stelle steht. Wir haben schon den zweiten Ofen dort gekauft.',
                      'Keine Wartezeit, freundlicher Empfang. Vor- und Nachteile jedes Ofens wurden für unsere Situation erklärt. Und der Kaffee war auch gut.',
                      'Das Montageteam war sehr freundlich und kompetent. Aufbau und Anschluss des Ofens waren perfekt.',
                      'Nach 25 Jahren wieder einen Ofen bei Schulte gekauft. Und wieder war alles wunderbar.'])
        + contact(s) + footer(s))

S = SITES['schulte'] = site(
    slug='ofen-schulte-bawinkel', firma='Ofen Schulte GmbH', web='ofenschulte.de', fonts='r10vagts',
    title='Ofen Schulte – Ofenmanufaktur und Kaminstudio in Bawinkel', desc='Ofen Schulte in Bawinkel: individueller Kamin- und Ofenbau seit 1979, 800 qm Ausstellung mit rund 130 Feuerstätten.',
    tel='05963 283', tel_i='+495963283', mail='info@ofenschulte.de', adresse='Osterbrocker Straße 17, 49844 Bawinkel', google=('4,9', 145),
    cta='Beratungstermin sichern', nav=[('Feuerstätten', 'feuer'), ('Ausstellung', 'ausstellung'), ('Service', 'service'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '10:00 – 12:30, 14:00 – 18:00'), ('Sa', '9:00 – 13:00')],
    form_opts=['Kamin / Ofenbau', 'Gaskamin', 'Kaminofen', 'Pelletofen', 'Specksteinofen', 'Service / Wartung', 'Sonstiges'],
    form_h3='Beratungstermin sichern', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Sie möchten bald <em>auch dazugehören?</em>', kt_p='Dann freuen wir uns auf Sie. Schreiben Sie uns oder kommen Sie nach Bawinkel.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#141414', mute='#5c5c5c', p='#C20016', pi='#fff', dk='#141414', s2='#f4f4f4', fh='"Lato",system-ui,sans-serif', fb='"Lato",system-ui,sans-serif', lh=58, ft='#141414'),
    css='''.h2,.hz h1{font-weight:900;font-style:italic;letter-spacing:-.01em}.h2 em,.hz h1 em{color:#C20016}.dk .h2 em{color:#ff6b7a}.mq.wm span{font-weight:900;font-style:italic;font-size:16px}
.alt{background:var(--s2)}.sv .row div{border-top:4px solid #C20016}.st.dk{background:#141414;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.ft img{background:#fff;padding:8px 12px;height:74px}''')
S['css2'] = '.hz{--hz-bg:#141414;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(255,255,255,.12);--hz-line:rgba(255,255,255,.2);--hz-cols:46fr 54fr}.hz h1{font-size:clamp(36px,4.4vw,70px)}.hz h1 em{color:#ff5a6b}.hz .ey{color:#ff9aa5}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hz .chip{background:rgba(255,255,255,.12);color:#fff}'
S['bot'] = BOT('Funke', 'Ihr Ofen-Lotse', 'Ofen Schulte', S, [
    ['Öffnungszeiten', 'Mo–Fr 10:00–12:30 und 14:00–18:00 Uhr, Sa 9:00–13:00 Uhr.'],
    ['Was gibt es in der Ausstellung?', 'Rund 130 Feuerstätten auf 800 qm: Kamin- und Pelletöfen, Specksteinöfen, Kamine, Gaskamine und Kachelöfen.'],
    ['Machen Sie auch Wartung?', 'Ja, von der Beratung über den Einbau bis zu Service und Wartung. Telefon: 05963 283.']],
    ['#feuer', '#ausstellung', '#service', '#kontakt'])
S['img'] = {'logo.png': I('schulte', 0, 0), 'h1.jpg': I('schulte', 1, 0), 'h2.jpg': I('schulte', 11, 0),
    'f1.jpg': I('schulte', 16, 0), 'f2.jpg': I('schulte', 29, 0), 'f3.jpg': I('schulte', 44, 0), 'f4.jpg': I('schulte', 62, 0), 'f5.jpg': I('schulte', 83, 0), 'f6.jpg': I('schulte', 95, 0),
    'aus.jpg': I('schulte', 107, 0), 'alt.jpg': I('schulte', 110, 0), 'r1.jpg': I('schulte', 92, 0), 'r2.jpg': I('schulte', 98, 0), 'r3.jpg': I('schulte', 101, 0), 'r4.jpg': I('schulte', 104, 0)}
S['body'] = b_schulte
