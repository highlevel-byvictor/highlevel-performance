"""Runde 18 · Teil B: Dänisches Ofenstudio Vogt Lübbecke, Ralf Recker Saerbeck, Kachel + Kamin Anten Lohne, Evers Eggermühlen."""
from common import *
SITES = {}

# ───────────── 5. Dänisches Ofenstudio Vogt, Lübbecke ─────────────
def b_vogt(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], badge=('Hygge', 'dänisch für gemütlich'),
        ey='Dänisches Ofenstudio Vogt · Lübbecke',
        h1='Hyggelige Öfen <em>aus Dänemark.</em>',
        sub='Größter Anbieter vollautomatischer Öfen Norddeutschlands. In unserer Ausstellung finden Sie klassische Kaminöfen, Pelletöfen, Specksteinöfen und Öfen aus Steinbausätzen.'))
        + marquee(['Kaminöfen', 'Pelletöfen', 'Gaskamine', 'Specksteinöfen', 'Steinbausätze', 'Outdooröfen', 'Gasfeuerstellen', 'Schornsteine', 'Strandkörbe'], 'wm')
        + panels('oefen', 'Öfen für drinnen', 'Schlicht und klassisch <em>oder extravagant?</em>', 'Viele Modelle unterschiedlichster Hersteller, alle in Lübbecke zu sehen.', [
            ('Kaminöfen', 'p1.jpg', 'Seit jeher ein Garant für wohlige Wärme. Heute oft der Blickfang der ganzen Wohnung.', '50% 50%'),
            ('Pelletöfen', 'p2.jpg', 'Gemütlichkeit und Wärme auf Knopfdruck, mit hohem Wirkungsgrad und sehr niedrigen Emissionswerten.', '50% 50%'),
            ('Specksteinöfen', 'p3.jpg', 'Naturverbundene Optik und ein Stein, der die Wärme lange speichert.', '50% 50%'),
            ('Gaskamine', 'p4.jpg', 'Sicher, sauber und sehr komfortabel. Ohne Sorge um den Brennholznachschub.', '50% 50%'),
            ('Steinbausätze', 'p5.jpg', 'Die elegante und preiswerte Alternative zum gemauerten Kamin.', '50% 50%')])
        + promo('outdoor', 'out.jpg', 'Outdoor', 'Kulinarik <em>unter freiem Himmel.</em>',
                'Ein hochwertiger Ofen für Garten, Terrasse oder Balkon gehört zu jeder Outdoorküche. Dazu Gasfeuerstellen, Gas-Terrassenfeuer und Strandkörbe für das Küstengefühl zu Hause.',
                ['Outdooröfen für die Außenküche', 'Gasfeuerstellen und Gas-Terrassenfeuer', 'Strandkörbe aus eigener Ausstellung'], 'Outdoor-Beratung anfragen', 'alt')
        + story('ausstellung', 'Ausstellung in Lübbecke', 'Bei uns finden Sie garantiert <em>den passenden Ofen.</em>', [
            'Hyggelig, das dänische Wort für gemütlich. Kaum ein anderes Wort beschreibt die skandinavische Lebensfreude besser. Genießen Sie dieses Gefühl in den eigenen vier Wänden.',
            'Vereinbaren Sie bitte einen Termin, da die Ausstellung aktuell nicht dauerhaft besetzt ist. Wir nehmen uns dann in Ruhe Zeit für Sie.'], 'haus.jpg', 'Das Ofenstudio an der Steubenstraße in Lübbecke', cls='dk',
            tl=[('Steubenstraße 12', '32312 Lübbecke'), ('Schornsteine', 'Edelstahlsysteme für jeden Aufstellort')])
        + gallery('galerie', 'Einblicke', 'So sieht <em>Hygge aus.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', 'w2', '50% 50%')])
        + reviews(s, ['Vom ersten Kontakt bis zur Montage waren wir äußerst zufrieden. Hervorragende Beratung und immer ehrlich. Hier wird einem nichts Unnötiges aufgeschwatzt.',
                      'Nach über 30 Jahren Heizen mit Holz haben wir uns für einen Pelletofen entschieden. Von der Planung bis zum Einbau war alles perfekt.',
                      'Eigentlich wollten wir nur schauen und haben dann spontan gekauft. Kurze Lieferzeit, saubere Montage, gute Einweisung.',
                      'Wir haben schon den zweiten Ofen gekauft, weil wir mit dem ersten sehr zufrieden waren. Wieder lief alles reibungslos.'])
        + contact(s) + footer(s))

S = SITES['vogt'] = site(
    slug='daenisches-ofenstudio-vogt-luebbecke', firma='Dänisches Ofenstudio Vogt', web='ofenstudio.net', fonts='r10vagts',
    title='Dänisches Ofenstudio Vogt – Kaminöfen und Pelletöfen in Lübbecke', desc='Dänisches Ofenstudio Vogt in Lübbecke: Kaminöfen, Pelletöfen, Specksteinöfen, Gaskamine, Outdooröfen und Schornsteine.',
    tel='05741 5540', tel_i='+4957415540', mail='info@ofenstudio.net', adresse='Steubenstraße 12, 32312 Lübbecke', google=('4,8', 79),
    cta='Termin in der Ausstellung', nav=[('Öfen', 'oefen'), ('Outdoor', 'outdoor'), ('Ausstellung', 'ausstellung'), ('Einblicke', 'galerie'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Sa', 'nach Terminvereinbarung')],
    form_opts=['Kaminofen', 'Pelletofen', 'Specksteinofen', 'Gaskamin', 'Outdoor / Gasfeuerstelle', 'Schornstein', 'Sonstiges'],
    form_h3='Termin in der Ausstellung', form_p='Sagen Sie uns, wann es Ihnen passt. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wann dürfen wir <em>Ihnen die Öfen zeigen?</em>', kt_p='Rufen Sie direkt an oder schreiben Sie uns.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#242424', mute='#585858', p='#C8102E', pi='#fff', dk='#242424', s2='#f6f4f1', fh='"Lato",system-ui,sans-serif', fb='"Lato",system-ui,sans-serif', lh=74, ft='#242424'),
    css='''.hp h1,.h2{font-weight:900;letter-spacing:-.02em}.hp h1 em,.h2 em{font-style:normal;color:#C8102E}.dk .h2 em{color:#ff7a8c}.mq.wm span{font-weight:900;letter-spacing:.06em;text-transform:uppercase;font-size:14px}
.alt{background:var(--s2)}.st.dk{background:#242424;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.hp .badge{background:#C8102E;color:#fff}.hp .badge b{color:#fff}.ft img{background:#fff;padding:8px 12px;height:88px}''')
S['bot'] = BOT('Hygge', 'Ihr Ofen-Lotse', 'Ofenstudio Vogt', S, [
    ['Wann ist geöffnet?', 'Die Ausstellung ist aktuell nicht dauerhaft besetzt. Bitte vereinbaren Sie einen Termin: 05741 5540.'],
    ['Was zeigen Sie?', 'Kaminöfen, Pelletöfen, Specksteinöfen, Gaskamine, Steinbausätze, Outdooröfen, Gasfeuerstellen und Strandkörbe.'],
    ['Ich habe keinen Schornstein', 'Mit einem Edelstahlschornstein sind Sie beim Aufstellort flexibel. Wir beraten Sie dazu.']],
    ['#oefen', '#outdoor', '#ausstellung', '#kontakt'])
S['img'] = {'logo.png': ('/home/claude/r18raw/vogt/Zeichenflaeche-2.png', 0, 'alphacrop'), 'h1.jpg': I('vogt', 36, 0), 'h2.jpg': I('vogt', 28, 0), 'h3.jpg': I('vogt', 35, 0),
    'p1.jpg': I('vogt', 41, 0), 'p2.jpg': I('vogt', 38, 0), 'p3.jpg': I('vogt', 45, 0), 'p4.jpg': I('vogt', 42, 0), 'p5.jpg': I('vogt', 48, 0),
    'out.jpg': I('vogt', 50, 0), 'haus.jpg': I('vogt', 24, 0), 'g1.jpg': I('vogt', 25, 0), 'g2.jpg': I('vogt', 44, 0), 'g3.jpg': I('vogt', 47, 0), 'g4.jpg': I('vogt', 51, 0)}
S['body'] = b_vogt

# ───────────── 6. Ralf Recker Ofenbaumeister, Saerbeck ─────────────
def b_recker(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='1996',
        ubar=[('Seit 1996', 'Meisterbetrieb in der Handwerksrolle'), ('Jeder Ofen', 'ein Unikat'), ('Ausstellung', 'Am Schulkamp in Saerbeck')],
        ey='Ralf Recker · Ofenbaumeister · Saerbeck',
        h1='So einzigartig <em>wie Ihr Zuhause.</em>',
        sub='Ihr Meisterbetrieb für individuellen Ofenbau im Münsterland. Vom Zeichenbrett bis zum fertigen Ofen, genau nach Ihren Wünschen.'))
        + marquee(['Kachelofenbau', 'Kaminbau', 'Individuelle Planung', 'Maßstabsgenaue Zeichnung', 'Münsterland', 'Saerbeck', 'Meisterbetrieb seit 1996'], 'wm')
        + scroller('projekte', 'Projekte', 'Bilder sagen mehr <em>als 1.000 Worte.</em>', 'Ein paar unserer Arbeiten. Bei Interesse erklären wir Ihnen gerne Bauweise und Besonderheiten.', [
            ('Kamin mit Sitzbank', 'g1.jpg', 'Feuer über Eck, die Bank gleich mitgeplant.', '50% 50%'),
            ('Dreiseitiger Kamin', 'g2.jpg', 'Als Raumteiler zwischen Wohnen und Essen.', '50% 50%'),
            ('Kachelofen, rund', 'g3.jpg', 'Klassisch gekachelt, neu gebaut.', '50% 50%'),
            ('Kamin mit Lichtfuge', 'g4.jpg', 'Schwebende Optik durch indirektes Licht.', '50% 50%'),
            ('Eckkamin auf Stein', 'g5.jpg', 'Schlicht, verputzt, mit Natursteinplatte.', '50% 50%'),
            ('Kamin im Wohnraum', 'g6.jpg', 'Geradlinig und ruhig, passend zum Raum.', '50% 50%')])
        + ablauf('weg', 'Vom Zeichenbrett bis zum fertigen Ofen', 'Sie sind von Anfang an <em>dabei.</em>', 'Planung ist aufwändiger, als man auf den ersten Blick vermutet. Darum machen wir sie gründlich.', [
            ('Beratungsgespräch', 'Wir sprechen über Ihre Vorstellungen, das Raumkonzept und die Zu- und Abluftsituation.'),
            ('Maßstabsgenaue Zeichnung', 'Ihre Wünsche bilden wir in einer Zeichnung ab und besprechen sie mit Ihnen.'),
            ('Umsetzung vor Ort', 'Wenn alle mit dem Zwischenergebnis zufrieden sind, bauen wir Ihren Ofen präzise bei Ihnen auf.')])
        + story('ueber', 'Qualität seit mehr als 20 Jahren', 'Kein Zimmer gleicht <em>dem anderen.</em>', [
            'Unser Betrieb ist seit 1996 als Meisterbetrieb in die Handwerksrolle eingetragen. 2006 haben wir Betriebsstätte und Ausstellung in das Gewerbegebiet „Am Schulkamp“ nach Saerbeck verlegt.',
            'Unsere Stärke ist der auf das jeweilige Objekt zugeschnittene Kachelofen- und Kaminbau. Ihre Vorstellungen und Wünsche beziehen wir 1:1 in die Planung mit ein.'], 'aus.jpg', 'Blick in unsere Ausstellung in Saerbeck', cls='dk',
            tl=[('1996', 'Eintragung als Meisterbetrieb'), ('2006', 'Umzug nach Saerbeck')])
        + reviews_ns(s, ['Der Ofen ist fantastisch. Ohne ihn hätten wir unser Steinhaus nach der Bauphase nie warm bekommen. Leicht zu bedienen und er sieht toll aus.',
                         'Ein toller Ofen, sehr guter Kundenservice. Wir würden uns immer wieder für Ralf Recker entscheiden.'])
        + contact(s) + footer(s))

S = SITES['recker'] = site(
    slug='ofenbau-ralf-recker-saerbeck', firma='Ralf Recker Ofenbaumeister', web='gute-oefen.de', fonts='r18rec',
    title='Ralf Recker Ofenbaumeister – individueller Ofenbau in Saerbeck', desc='Ofenbaumeister Ralf Recker in Saerbeck: individueller Kachelofen- und Kaminbau im Münsterland, Meisterbetrieb seit 1996.',
    tel='02574 9397940', tel_i='+4925749397940', mail='info@gute-oefen.de', adresse='Am Schulkamp 85, 48369 Saerbeck', google=None,
    cta='Gesprächstermin vereinbaren', nav=[('Projekte', 'projekte'), ('Ablauf', 'weg'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung')],
    form_opts=['Kachelofen', 'Kamin', 'Ofen modernisieren', 'Beratung in der Ausstellung', 'Sonstiges'],
    form_h3='Gesprächstermin vereinbaren', form_p='Sagen Sie uns kurz, was Sie sich vorstellen. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Kommen Sie mit uns <em>ins Gespräch.</em>', kt_p='Sie haben eine Frage oder möchten einen persönlichen Termin? Schreiben Sie uns.',
    vars=V.format(ink='#2a2a2a', mute='#5c5c5c', p='#E5261E', pi='#fff', dk='#1e1e1e', s2='#f5f3f0', fh='"Noto Sans",system-ui,sans-serif', fb='"Noto Sans",system-ui,sans-serif', lh=44, ft='#1e1e1e'),
    css='''.h2,.hz h1{font-weight:800;letter-spacing:-.025em}.h2 em,.hz h1 em{font-style:normal;color:#E5261E}.dk .h2 em{color:#ff8a84}.mq.wm span{font-weight:700;font-size:15px}
.st.dk{background:#1e1e1e;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.rd .road div h3{color:#E5261E}.ft img{background:#fff;padding:8px 12px;height:60px}''')
S['css2'] = '.hz{--hz-bg:#fff;--hz-ink:#1e1e1e;--hz-mute:#5c5c5c;--hz-stroke:rgba(229,38,30,.14);--hz-cols:44fr 56fr}.hz h1{font-size:clamp(38px,4.6vw,74px)}.hz .ey{color:#E5261E}'
S['bot'] = BOT('Kachel', 'Ihr Ofen-Lotse', 'Ralf Recker', S, [
    ['Wie läuft die Planung ab?', 'Erst das Beratungsgespräch, dann eine maßstabsgenaue Zeichnung, dann die Umsetzung bei Ihnen vor Ort.'],
    ['Wo ist die Ausstellung?', 'Am Schulkamp 85 in Saerbeck. Termine bitte vorab vereinbaren: 02574 9397940.'],
    ['Bauen Sie auch Kachelöfen?', 'Ja. Unsere Stärke ist der auf Ihr Zuhause zugeschnittene Kachelofen- und Kaminbau.']],
    ['#projekte', '#weg', '#ueber', '#kontakt'])
S['img'] = {'logo.png': I('recker', 0, 0), 'h1.jpg': I('recker', 2, 0), 'h2.jpg': I('recker', 4, 0), 'h3.jpg': I('recker', 40, 0),
    'g1.jpg': I('recker', 7, 0), 'g2.jpg': I('recker', 18, 0), 'g3.jpg': I('recker', 20, 0), 'g4.jpg': I('recker', 10, 0), 'g5.jpg': I('recker', 12, 0), 'g6.jpg': I('recker', 8, 0),
    'aus.jpg': I('recker', 21, 0)}
S['body'] = b_recker

# ───────────── 7. Kachel + Kamin Anten GmbH, Lohne ─────────────
def b_anten(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '60% 50%', 'h2.jpg': '60% 50%', 'h3.jpg': '60% 50%'},
        ey='Kachel + Kamin Anten · Lohne',
        h1='Feuer <em>fasziniert.</em>',
        sub='Kamine, Gaskamine, Kachelöfen und Kaminöfen auf 1.000 m² Ausstellung. Eigene Planung, eigene Handwerker, zwei Ofenbaumeister an der Spitze.',
        ubar=[('1.000 m²', 'Kamin- und Ofenausstellung'), ('Schautag', 'jeden 2. Sonntag im Monat'), ('A1 Lohne / Dinklage', 'nur 1,5 km entfernt')]))
        + marquee(['Kamine', 'Gaskamine', 'Kachelöfen', 'Kaminöfen', 'Schornsteinbau', 'Reinigung und Reparatur', 'Spartherm', 'Brunner', 'Austroflamm', 'Hoxter', 'Drooff', 'Skantherm'], 'wm')
        + panels('produkte', 'Produkte und Technik', 'Ein Kamin ist ein Stück <em>Lebensart.</em>', 'Aber auch immer ein Stück Wohnkultur. Was zu Ihnen passt, zeigen wir Ihnen in Lohne.', [
            ('Kamine', 'p1.jpg', 'Das beruhigende Flackern der Flammen und eine Wärme, die durchdringt.', '50% 50%'),
            ('Gaskamine', 'p2.jpg', 'Unser Spezialgebiet: Flammenbild auf Knopfdruck, fachgerecht geplant und angeschlossen.', '50% 50%'),
            ('Kachelöfen', 'p3.jpg', 'Wärme zum Anlehnen, individuell gebaut.', '50% 50%'),
            ('Kaminöfen', 'p4.jpg', 'Freistehend, schnell warm und in vielen Formen.', '50% 50%')])
        + promo('ausstellung', 'aus.jpg', 'Schautag jeden 2. Sonntag', '1.000 m² Kamine und Öfen <em>zum Anfassen.</em>',
                'Gewinnen Sie einen ersten Eindruck in unserer großen Ausstellung in Lohne. Jeden 2. Sonntag im Monat öffnen wir zum Schautag von 13 bis 17 Uhr.',
                ['Sept. – März: Mo – Fr 9:00 – 18:30, Sa 10:00 – 15:00 Uhr', 'April – Aug.: Mo – Fr 9:00 – 18:00, Sa 10:00 – 14:00 Uhr', 'Termine außerhalb der Öffnungszeiten nach Vereinbarung'], 'Beratungstermin anfragen', 'alt')
        + gallery('referenzen', 'Einblicke', 'Kamine, die <em>Räume verändern.</em>', [
            ('r1.jpg', 'w2 h2r', '50% 50%'), ('r2.jpg', '', '50% 50%'), ('r3.jpg', '', '50% 50%'), ('r4.jpg', 'w2', '50% 50%')])
        + svc('wissen', 'Drei Schritte beim Kamin-Kauf', 'Billig kommt <em>schnell teuer.</em>', 'Wer länger Freude an seinem Kamin haben möchte, sollte sinnvoll investieren.', [
            ('Schornsteinfeger bestellen', 'Er prüft vor dem Kauf, welches Modell unter welchen Auflagen bei Ihnen betrieben werden kann.'),
            ('Nutzung klären', 'Ständig oder gelegentlich? Als Ergänzung zur Heizung oder für das Ambiente?'),
            ('Bei uns planen lassen', 'Durch unsere eigene Planung berücksichtigen wir Ihre Raumsituation und erfüllen „fast“ jeden Wunsch.'),
            ('Reinigung und Reparatur', 'Zu Beginn der Heizsaison sollte die Feuerstätte gereinigt werden. Auch das übernehmen wir.')])
        + story('team', 'Unser Team', 'Fachkompetenz und <em>Schnelligkeit.</em>', [
            'Dank eines breiten Fachwissens rund um Kamine und Öfen können wir fundiert beraten. Wir sind gut aufgestellt mit Fachkräften, die sich bestens auskennen, auch mit Spezialgebieten wie Gaskaminen oder Schornsteinbau.',
            'Geführt wird der Betrieb von den Ofen- und Luftheizungsbaumeistern Norbert Anten und Michael Anten.'], 'haus.jpg', 'Kachel + Kamin am Fladderweg in Lohne', cls='dk',
            tl=[('Norbert Anten', 'Geschäftsführer, Ofen- und Luftheizungsbaumeister'), ('Michael Anten', 'Geschäftsführung, Ofen- und Luftheizungsbaumeister')])
        + reviews_ns(s, ['Beratung hochkompetent, freundlich und sympathisch. Alles wurde bei uns zu Hause besichtigt und besprochen. Qualität erstklassig, auch beim Einbau.',
                         'Dank der ausgezeichneten Beratung und der sauberen, pünktlichen Ausführung genießen wir jetzt unseren Kamin. Es ist schon unser zweiter in 26 Jahren.',
                         'Beratung, Planung, Service und Einbau: Wir sind rundum zufrieden. Unsere Vorstellungen wurden perfekt umgesetzt.',
                         'Der Kamin sieht fantastisch aus, funktioniert einwandfrei und lässt sich gut regeln.'])
        + contact(s) + footer(s))

S = SITES['anten'] = site(
    slug='kachel-kamin-anten-lohne', firma='Kachel und Kamin Anten GmbH', web='kachelundkamin.de', fonts='r18ant',
    title='Kachel + Kamin Anten – Kamine und Öfen in Lohne', desc='Kachel + Kamin Anten in Lohne: Kamine, Gaskamine, Kachelöfen und Kaminöfen. 1.000 m² Ausstellung, Schautag jeden 2. Sonntag im Monat.',
    tel='04442 92600', tel_i='+49444292600', mail='info@kachelundkamin.de', adresse='Fladderweg 1, 49393 Lohne', google=None,
    cta='Beratungstermin anfragen', nav=[('Produkte', 'produkte'), ('Ausstellung', 'ausstellung'), ('Einblicke', 'referenzen'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 18:30 (Apr. – Aug. bis 18:00)'), ('Sa', '10:00 – 15:00 (Apr. – Aug. bis 14:00)'), ('Schautag', 'jeden 2. Sonntag im Monat, 13 – 17 Uhr')],
    form_opts=['Kamin', 'Gaskamin', 'Kachelofen', 'Kaminofen', 'Reinigung / Reparatur', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Schreiben Sie uns Ihr Anliegen. Wir melden uns schnellstmöglich bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Verkehrsgünstig <em>an der A1.</em>', kt_p='Nur 1,5 km von der Abfahrt Lohne / Dinklage. Besucher aus dem Diepholzer Raum kommen am besten über den Südring.',
    vars=V.format(ink='#262626', mute='#5b6163', p='#DA2F10', pi='#fff', dk='#3c4143', s2='#f3f3f2', fh='"Raleway",system-ui,sans-serif', fb='"Raleway",system-ui,sans-serif', lh=54, ft='#2b2f30') + DKHD.format(c='#3c4143'),
    css='''body{font-weight:400}.hs h1,.h2{font-weight:300;letter-spacing:-.02em;line-height:1.04}.hs h1{font-size:clamp(48px,7.4vw,124px)}.hs h1 em,.h2 em{font-style:normal;font-weight:800;color:#DA2F10}.hs h1 em{color:#ff8d73}.dk .h2 em{color:#ff9a82}
.mq.wm span{font-weight:600;letter-spacing:.12em;text-transform:uppercase;font-size:13px}.alt{background:var(--s2)}.sv .row div{border-top:4px solid #DA2F10}.hs .ubar b{color:#fff}.hs .ey{color:#ffd7cc!important}@media(max-width:820px){.hs h1{font-size:46px;hyphens:none}}
.st.dk{background:#3c4143;color:#fff}.st.dk .lead{color:rgba(255,255,255,.88)}.st.dk .tl b{color:#fff}''')
S['bot'] = BOT('Lohe', 'Ihr Kamin-Lotse', 'Kachel + Kamin Anten', S, [
    ['Öffnungszeiten', 'Sept.–März: Mo–Fr 9:00–18:30, Sa 10:00–15:00 Uhr. April–Aug.: Mo–Fr 9:00–18:00, Sa 10:00–14:00 Uhr.'],
    ['Wann ist Schautag?', 'Jeden 2. Sonntag im Monat von 13 bis 17 Uhr in unserer Ausstellung in Lohne.'],
    ['Was muss ich vor dem Kauf klären?', 'Am besten zuerst den Schornsteinfeger fragen, welches Modell bei Ihnen betrieben werden kann. Telefon: 04442 92600.']],
    ['#produkte', '#ausstellung', '#referenzen', '#kontakt'])
S['img'] = {'logo.png': I('anten', 0, 0), 'h1.jpg': I('anten', 1, 0), 'h2.jpg': I('anten', 2, 0), 'h3.jpg': I('anten', 3, 0),
    'p1.jpg': I('anten', 28), 'p2.jpg': I('anten', 80), 'p3.jpg': I('anten', 63), 'p4.jpg': I('anten', 76),
    'aus.jpg': I('anten', 35), 'haus.jpg': I('anten', 26, 0), 'r1.jpg': I('anten', 84), 'r2.jpg': I('anten', 24), 'r3.jpg': I('anten', 88), 'r4.jpg': I('anten', 39)}
S['body'] = b_anten

# ───────────── 8. Evers eGbR Kamine & Öfen, Eggermühlen ─────────────
def b_evers(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg'], badge=('Vor Ort', 'in Eggermühlen'),
        ey='Evers Kamine & Öfen · Eggermühlen',
        h1='Der Winter <em>kommt bestimmt.</em>',
        sub='Kaminöfen der neuesten Generation: als gemütlicher Wärmespender an langen Winterabenden oder als wirtschaftliche Zusatzheizung in der Übergangszeit.'))
        + marquee(['Kaminöfen', 'Pelletöfen', 'Schornsteintechnik', 'Planung', 'Installation', 'Wartung', 'Ersatzteile', 'Spartherm', 'Schmid', 'Olsberg', 'Lohberger', 'MCZ'], 'wm')
        + svc('service', 'Service', 'Planung, Beratung, <em>Installation.</em>', 'Beziehen Sie den Kamin von Beginn an in Ihre Planung ein. Am besten kommen Sie mit Grundriss oder Vorentwurf zu uns.', [
            ('Planung und Beratung', 'Bei Neubauten erleben wir oft, dass die Planung schon fast abgeschlossen ist. Früh geplant, lässt sich fast jede Vorstellung umsetzen.'),
            ('Wartung', 'Tür schließt nicht richtig? Probleme mit der Wärmeentwicklung? Wir finden die Ursache und beheben den Fehler.'),
            ('Ersatzteile', 'Oft erst nach Jahren gebraucht und dann schwer zu bekommen. Wir besorgen sie für Sie.'),
            ('Abnahme', 'Klären Sie vor dem Kauf mit Ihrem Bezirksschornsteinfeger, ob Schornstein und Anschlüsse in Ordnung sind. Wir helfen dabei.')])
        + promo('aktionen', 'akt.jpg', 'Aktionen', 'Ihr Traumofen <em>zu einem guten Preis.</em>',
                'Was gibt es Schöneres, als sich an kühlen Tagen bei flackerndem Feuer zu Hause einzukuscheln? Fragen Sie nach unseren aktuellen Aktionsmodellen.',
                ['Kaminöfen und Pelletöfen namhafter Hersteller', 'Termine nach telefonischer Vereinbarung', 'Direkt bei uns in Eggermühlen ansehen'], 'Nach Aktionen fragen', 'alt')
        + story('ueber', 'Ihr Kaminstudio in Eggermühlen', 'Design und Qualität <em>für Kaminliebhaber.</em>', [
            'Mit einer auf aktuelle Wohntrends abgestimmten Designvielfalt und modernster Verbrennungstechnik erfüllen Kaminöfen der neuesten Generation auch höchste Ansprüche.',
            'Ansprechpartner bei der Evers eGbR ist Manuel Evers. Rufen Sie einfach an, wir vereinbaren einen Termin.'], 'haus.jpg', 'Evers Kamine & Öfen, Im Mersch 1a in Eggermühlen', cls='dk',
            tl=[('Mo – Sa', 'Termine nach telefonischer Vereinbarung'), ('Schornsteintechnik', 'gleich mit dabei')])
        + gallery('stimmung', 'Wohlige Wärme', 'So fühlt sich <em>ein Kaminabend an.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', 'w2', '50% 50%')])
        + reviews(s, ['Ein wirklich tolles und motiviertes Team. Sehr nette und fleißige Handwerker, saubere und zuverlässige Arbeit.',
                      'Sehr freundliches und zuvorkommendes Personal. Schneller, guter und sauberer Service.',
                      'Ausgezeichnete Arbeit, zuverlässig und kompetent. Gerne wieder.',
                      'Herr Evers ist ein zuverlässiger Handwerker und Händler.'])
        + contact(s) + footer(s))

S = SITES['evers'] = site(
    slug='evers-kamine-oefen-eggermuehlen', firma='Evers eGbR Kamine & Öfen', web='evers-kamine.de', fonts='r13feh',
    title='Evers Kamine & Öfen – Kaminstudio in Eggermühlen', desc='Evers Kamine & Öfen in Eggermühlen: Kaminöfen, Pelletöfen, Schornsteintechnik, Planung, Wartung und Ersatzteile.',
    tel='0171 6512957', tel_i='+491716512957', mail='info@evers-kamine.de', adresse='Im Mersch 1a, 49577 Eggermühlen', google=('4,8', 17),
    cta='Termin vereinbaren', nav=[('Service', 'service'), ('Aktionen', 'aktionen'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Sa', 'Termine nach telefonischer Vereinbarung')],
    form_opts=['Kaminofen', 'Pelletofen', 'Schornstein', 'Wartung / Reparatur', 'Ersatzteile', 'Sonstiges'],
    form_h3='Termin vereinbaren', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Nehmen Sie mit uns <em>Kontakt auf.</em>', kt_p='Am schnellsten erreichen Sie uns telefonisch.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#252525', mute='#5a5a5a', p='#D12323', pi='#fff', dk='#232529', s2='#f5f4f2', fh='"Red Hat Display",system-ui,sans-serif', fb='"Red Hat Text",system-ui,sans-serif', lh=48, ft='#232529'),
    css='''.hp h1,.h2{font-weight:800;letter-spacing:-.025em}.hp h1 em,.h2 em{font-style:normal;color:#D12323}.dk .h2 em{color:#ff7d7d}.mq.wm span{font-weight:700;font-size:15px}
.alt{background:var(--s2)}.sv .row div{border-top:4px solid #D12323}.st.dk{background:#232529;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.hp .badge{background:#D12323;color:#fff}.hp .badge b{color:#fff}
.ft img{background:#fff;padding:8px 12px;height:62px}''')
S['bot'] = BOT('Glimm', 'Ihr Ofen-Lotse', 'Evers Kamine & Öfen', S, [
    ['Wann haben Sie geöffnet?', 'Montag bis Samstag nach telefonischer Vereinbarung: 0171 6512957.'],
    ['Mein Ofen macht Probleme', 'Wir finden die Ursache, besorgen Ersatzteile und beheben den Fehler.'],
    ['Was kläre ich vor dem Kauf?', 'Sprechen Sie vorher mit Ihrem Bezirksschornsteinfeger, ob Schornstein und Anschlüsse in Ordnung sind.']],
    ['#service', '#aktionen', '#ueber', '#kontakt'])
S['img'] = {'logo.png': I('evers', 0, 0), 'h1.jpg': I('evers', 8, 0), 'h2.jpg': I('evers', 10, 0),
    'akt.jpg': (PIX18 + '10510216.jpg', 0), 'haus.jpg': I('evers', 7, 0),
    'g1.jpg': (PIX18 + '8352436.jpg', 0), 'g2.jpg': (PIX18 + '9750451.jpg', 0), 'g3.jpg': (PIX18 + '4621891.jpg', 0), 'g4.jpg': (PIX18 + '2237147.jpg', 0)}
S['body'] = b_evers
