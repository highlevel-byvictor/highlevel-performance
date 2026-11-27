"""Akquise-Agent 27.11.2026 (Freitag, Restaurants/Cafés): 5 Betriebe mit Instagram-Link und veralteter Website.
Texte, Gerichte, Bilder und Logos stammen von den Originalseiten. Keine erfundenen Preise, Stimmen oder Gerichtsnamen.
Google-Sterne werden nicht gezeigt (nicht geprüft)."""
from common import *
SITES = {}

# ─────────────── 1 · Restaurant Kavala, Wildeshausen (Du-Form wie im Original) ───────────────
def b_kavala(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Aus unserer Küche', 'Gyros mit Souvlaki'), True),
                                       ('m2.jpg', ('Vom Grill', 'Apollo-Teller'), True),
                                       ('m3.jpg', ('Aus dem Ofen', 'Gyros überbacken'), True)],
        steam={'m1.jpg': '50%', 'm2.jpg': '50%', 'm3.jpg': '50%'},
        ubar=[('Seit 2017', 'familiengeführt'), ('35 Jahre', 'Erfahrung in der Küche'), ('Mo', 'Ruhetag')],
        ey='Restaurant Kavala · Griechisch · Wildeshausen',
        h1='Der richtige Grieche <em>in Wildeshausen.</em>',
        sub='Gemütlich-rustikal und herzlich: Bei uns wirst du von Griechen bekocht und bedient. Traditionell gekocht, mit hochwertigen Zutaten, viel Erfahrung und Liebe.'))
        + marquee(['Gyros Metaxa', 'Hühnchen Souvlaki', 'Apollo-Teller', 'Paidakia', 'Kalamaris', 'Sardellen', 'Knoblauchbrot', 'Gefülltes Schweinefilet'], 'wm')
        + cards('kueche', 'Unsere Küche', 'Frisch, authentisch, <em>hochwertig.</em>', 'Schau dich um und finde dein nächstes Lieblingsgericht. Alle Fotos zeigen Gerichte aus unserer Küche.', [
            ('k1.jpg', 'Gyrosspezialitäten', 'Gyros Original, Metaxa, überbacken oder mit Kalamaris. Dazu Reis, Tsatsiki und gemischter Krautsalat.', '50% 50%'),
            ('k2.jpg', 'Souvlaki vom Grill', 'Chefkoch Souvlaki mit gebratenem Gemüse, Horiatiko Souvlaki mit Bratkartoffeln oder Hühnchen Souvlaki.', '50% 50%'),
            ('k3.jpg', 'Vorspeisen', 'Frittierte Peperoni, Knoblauchbrot, überbackene Champignons oder die Ouzomezze mit warmen und kalten Vorspeisen.', '50% 50%'),
            ('k4.jpg', 'Aus dem Meer', 'Kalamaris, Sardellen und frittierte Muscheln, klassisch mehliert, dazu Tsatsiki.', '50% 50%')])
        + moment('mo.jpg', 'Ob Jung oder Alt, allein, zu zweit oder mit der ganzen Familie: <em>Bei uns soll sich jeder willkommen fühlen.</em>', 'Restaurant Kavala · Am Krandel 4', '50% 50%')
        + gallery('eindruecke', 'Dein Ideenfinder', 'Hunger auf <em>etwas Neues?</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + story('ueber', 'Über uns', 'Ein Stück <em>Griechenland.</em>', [
            'Wir sind ein familiengeführtes, griechisches Lokal im Herzen Wildeshausens. Seit unserer Eröffnung am 1. Mai 2017 stehen wir für griechische Gastfreundschaft, Herzlichkeit und authentische Küche.',
            'Unser Name stammt aus der historischen Hafenstadt Kavala im Norden Griechenlands. Die Inhaberin und unser Küchenchef bringen jeweils mehr als 35 Jahre Erfahrung in der traditionellen griechischen Küche mit.'],
            'st.jpg', 'Unser Gastraum in Wildeshausen', tl=[('Gastfreundschaft', 'Geselligkeit und ein Ort zum Wohlfühlen'), ('Lage', 'gegenüber vom Krandel, Parkplätze am Haus')])
        + contact(s) + footer(s))

P1, D1 = '#1f5fa8', '#0f2238'
S = SITES['kavala'] = site(
    slug='kavala-wildeshausen', firma='Restaurant Kavala', web='restaurant-kavala-wildeshausen.de', fonts='mykonos', branche='Griechisches Restaurant', du=True,
    logo_txt='Kavala<small>Griechisches Restaurant</small>',
    title='Restaurant Kavala – der richtige Grieche in Wildeshausen', desc='Restaurant Kavala in Wildeshausen: familiengeführt, griechische Küche seit 2017. Gyros, Souvlaki vom Grill, Vorspeisen und Fisch.',
    tel='04431 955 7155', tel_i='+4944319557155', mail='', adresse='Am Krandel 4, 27793 Wildeshausen', google=None,
    nav=[('Küche', 'kueche'), ('Gerichte', 'eindruecke'), ('Über uns', 'ueber'), ('Reservieren', 'kontakt')],
    hours=[('Di – So', '17:00 – 22:00 Uhr'), ('Feiertage', '17:00 – 22:00 Uhr'), ('Montag', 'Ruhetag')],
    form_h3='Tisch anfragen', form_p='Schreib uns Wunschtag, Uhrzeit und Personenzahl. Wir rufen dich zurück und bestätigen deine Reservierung.',
    kt_ey='Reservieren', kt_h2='Wir freuen uns <em>auf dich.</em>', kt_p='Reservierungen am liebsten telefonisch oder persönlich. Die Küche schließt immer eine Stunde vor Ende.',
    vars=V.format(bg='#f8fafc', ink='#0f2238', mute='#4d5d70', p=P1, dk=D1, s2='#eaf1f8', fh='"Marcellus",Georgia,serif', fb='"Manrope",system-ui,sans-serif', lh=46),
    css=css_g(P1, D1))
S['css2'] = hz('#eaf1f8', '#0f2238')
S['bot'] = dict(name='Eleni', tag='Deine Gastgeberin', hello='Hallo! Ich bin <b>Eleni</b>. Soll ich dir kurz zeigen, was dich im Kavala erwartet?',
    hi='Hallo, ich bin Eleni vom Restaurant Kavala. Wobei kann ich helfen?', qa=[
    ['Wann habt ihr geöffnet?', 'Dienstag bis Sonntag und an Feiertagen von 17 bis 22 Uhr. Montag ist Ruhetag. Die Küche schließt eine Stunde vorher.'],
    ['Wie reserviere ich?', 'Am besten telefonisch unter 04431 955 7155 oder persönlich bei uns. Per Mail nehmen wir keine Reservierungen an.'],
    ['Wo parke ich?', 'Direkt am Restaurant und gegenüber. Wir liegen am Krandel, nah am Wohnmobilstellplatz und am Krandelbad.']],
    tour=[['#kueche'], ['#eindruecke'], ['#ueber'], ['#kontakt']])
K = R + 'kavala/i/'
S['img'] = {'m1.jpg': (K + '13.jpg', 1600), 'm2.jpg': (K + '26.jpg', 1600), 'm3.jpg': (K + '22.jpg', 1600),
    'k1.jpg': (K + '10.jpg', 900), 'k2.jpg': (K + '11.jpg', 900), 'k3.jpg': (K + '12.jpg', 900), 'k4.jpg': (K + '31.jpg', 900),
    'mo.jpg': (K + '01.png', 1600), 'g1.jpg': (K + '20.jpg', 1200), 'g2.jpg': (K + '29.jpg', 900), 'g3.jpg': (K + '21.jpg', 900), 'g4.jpg': (K + '08.jpg', 900), 'g5.jpg': (K + '35.jpg', 1200),
    'st.jpg': (K + '01.png', 1200)}
S['body'] = b_kavala
S['social'] = [('Instagram', 'https://www.instagram.com/kavalawildeshausen/')]

# ─────────────── 2 · Schloßmühle Bad Iburg ───────────────
def b_schlossm(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Seeterrasse', 'Direkt am Charlottensee'), False),
                                       ('m2.jpg', ('Mittag- & Abendessen', 'Frische, regionale Küche'), True),
                                       ('m3.jpg', ('Beach Bad Iburg', 'Burger, Cocktails & more'), False)],
        pos={'m1.jpg': '50% 60%', 'm2.jpg': '50% 55%'}, steam={'m2.jpg': '50%'},
        ubar=[('Sonntag', 'Genießer-Frühstücksbuffet'), ('bis 120', 'Gäste im Eventraum'), ('Am See', 'Seeterrasse & Beachbar')],
        ey='Café · Restaurant · Eventlocation · Bad Iburg',
        h1='Genießen, <em>direkt am See.</em>',
        sub='Frühstück, Mittagstisch, Kaffee und Kuchen oder ein Abend mit Blick auf den Charlottensee. Wir arbeiten möglichst mit frischen, regionalen Produkten.'))
        + marquee(['Genießer-Frühstücksbuffet', 'Mittagstisch', 'Kaffee & Kuchen', 'Kuchenbuffet', 'Seeterrasse', 'Beach Bad Iburg', 'Hochzeiten am See', 'Silvesterbuffet'], 'wm')
        + svc('angebot', 'Bei uns', 'Vom Frühstück <em>bis zum Fest.</em>', 'Samstag und Sonntag durchgehend geöffnet, für Veranstaltungen ab 20 Personen öffnen wir gern auch unter der Woche.', [
            ('Genießer-Frühstücksbuffet', 'Jeden Sonntag und an ausgewählten Feiertagen von 9:00 bis 11:30 Uhr. Für Veranstaltungen ab 40 Personen auch exklusiv buchbar.'),
            ('Mittag- & Abendessen', 'Warme Küche am Samstag von 12 bis 20 Uhr, am Sonntag von 12 bis 17 Uhr. Ab 10 Personen bitte die Auswahl vorab mitteilen.'),
            ('Kaffee & Kuchen', 'Erlesene Kaffee- und Teespezialitäten, Kuchen und Torten. Sonn- und feiertags mit großem Kuchenbuffet. Konditionen für Gruppen und Busse.'),
            ('Silvesterbuffet', 'Genussvoll ins neue Jahr: Silvesterbuffet von 18 bis 21 Uhr mit Begrüßungsaperitif. Karten im Restaurant erhältlich.')])
        + moment('mo.jpg', 'Lust auf Sommer, Sonne und kühle Cocktails? <em>Dann ab an den Beach Bad Iburg.</em>', 'Beach Bad Iburg · April/Mai bis Oktober', '50% 50%')
        + cards('feiern', 'Eventlocation', 'Traumhaft feiern, <em>direkt am See.</em>', 'Eventraum mit Glashaus, großen Glasschiebetüren und Blick auf den Charlottensee.', [
            ('f1.jpg', 'Hochzeiten', 'Platz für bis zu 100, maximal 120 Personen. Gern senden wir Ihnen unsere Bankettmappe unverbindlich zu.', '50% 50%'),
            ('f2.jpg', 'Exklusiv feiern', 'Für größere Gesellschaften nach Absprache die gesamte Schloßmühle mit Seeterrasse oder dem Beach-Bereich.', '50% 50%'),
            ('f3.jpg', 'Beach-Events', 'Burger, Cocktails und Sand unter den Füßen. Reservierung und Infos per WhatsApp.', '50% 50%')], 'alt')
        + gallery('eindruecke', 'Eindrücke', 'Die Schloßmühle <em>am Charlottensee.</em>', [
            ('g1.jpg', 'h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', 'h2r', '50% 50%')])
        + contact(s) + footer(s))

P2, D2 = '#9b2c2c', '#2a1d1a'
S = SITES['schlossm'] = site(
    slug='schlossmuehle-bad-iburg', firma='Schloßmühle Bad Iburg', web='schlossmuehle-bad-iburg.de', fonts='droste', branche='Café, Restaurant & Eventlocation',
    logo_txt='Schloßmühle<small>Bad Iburg · am Charlottensee</small>',
    title='Schloßmühle Bad Iburg – Café, Restaurant & Beachbar am See', desc='Schloßmühle Bad Iburg: Genießer-Frühstücksbuffet, Mittagstisch, Kaffee & Kuchen, Hochzeiten am Charlottensee und Beach Bad Iburg.',
    tel='05403 9610', tel_i='+4954039610', mail='info@schlossmuehle-bad-iburg.de', adresse='Charlottenburger Ring 27, 49186 Bad Iburg', google=None,
    nav=[('Angebot', 'angebot'), ('Feiern', 'feiern'), ('Eindrücke', 'eindruecke'), ('Reservieren', 'kontakt')],
    hours=[('Samstag', '12:00 – 21:00 Uhr'), ('Sonntag', '09:00 – 18:00 Uhr'), ('Mo – Fr', 'für Gruppen ab 20 nach Absprache'), ('WhatsApp', '0152 56836668')],
    kt_ey='Reservieren', kt_h2='Wir freuen uns <em>auf Ihren Besuch.</em>', kt_p='Ihre Reservierung ist erst mit unserer Rückbestätigung verbindlich. Reservierungen auch per WhatsApp oder SMS an 0152 56836668.',
    vars=V.format(bg='#fbf8f4', ink='#2a1d1a', mute='#665953', p=P2, dk=D2, s2='#f3ece3', fh='"Lora",Georgia,serif', fb='"Source Sans 3",system-ui,sans-serif', lh=46),
    css=css_g(P2, D2))
S['css2'] = hz('#f3ece3')
S['bot'] = BOT('Charlotte', 'Ihre Gastgeberin', 'der Schloßmühle', [
    ['Wann haben Sie geöffnet?', 'Samstag 12 bis 21 Uhr, Sonntag 9 bis 18 Uhr. Montag bis Freitag öffnen wir für Veranstaltungen ab 20 Personen nach Absprache.'],
    ['Wann gibt es Frühstück?', 'Unser Genießer-Frühstücksbuffet gibt es sonntags und an ausgewählten Feiertagen von 9:00 bis 11:30 Uhr.'],
    ['Sind Hunde erlaubt?', 'Im gefliesten Bereich und auf der Seeterrasse herzlich willkommen. Im Teppichbereich und im Sand leider nicht.']],
    ['#angebot', '#feiern', '#eindruecke', '#kontakt'])
SM = R + 'schlossm/i/'
S['img'] = {'m1.jpg': (SM + '14.jpg', 1400), 'm2.jpg': (SM + '21.jpg', 1400), 'm3.jpg': (SM + '11.jpeg', 1600),
    'mo.jpg': (SM + '12.jpg', 1440), 'f1.jpg': (SM + '10.jpeg', 900), 'f2.jpg': (SM + '14.jpg', 900), 'f3.jpg': (SM + '11.jpeg', 900),
    'g1.jpg': (SM + '10.jpeg', 900), 'g2.jpg': (SM + '12.jpg', 900), 'g3.jpg': (SM + '21.jpg', 900), 'g4.jpg': (SM + '14.jpg', 900)}
S['body'] = b_schlossm
S['social'] = [('Instagram', 'https://www.instagram.com/schlossmuehle.bad.iburg/')]

# ─────────────── 3 · Heidehof Jansen-Olliges, Friesoythe-Gehlenberg ───────────────
def b_heidehof(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Festsaal', 'Feiern bis 250 Personen'), False),
                                       ('m2.jpg', ('Bauerndiele & Kneipe', 'Gemütlich-rustikal'), False),
                                       ('m3.jpg', ('Campingplatz', 'Mit eigenem Quellsee'), False)],
        ubar=[('bis 250', 'Gäste im Festsaal'), ('2 Bahnen', 'Bundes- & Scherenbahn'), ('6 ha', 'Campingplatz mit See')],
        ey='Gastronomie · Festsaal · Kegelbahn · Campingplatz',
        h1='Gastlichkeit <em>im Grünen.</em>',
        sub='Abseits von Hast und Lärm, direkt am Waldrand: regionale und saisonale Küche, hübsch gedeckte Tische und Räume für Feste aller Art.'))
        + marquee(['Regionale Küche', 'Spare Ribs & Steaks vom Grill', 'Festsaal', 'Deele', 'Kaminfeuer', 'Kegelbahnen', 'Freie Trauung', 'Campingplatz'], 'wm')
        + cards('angebot', 'Bei uns', 'Für jeden Anlass <em>der passende Rahmen.</em>', 'Ob Familienfeier, Vereinsausflug, Urlaub oder geselliger Abend.', [
            ('k1.jpg', 'Bauerndiele & Kneipe', 'Saisonale Küche für Gruppen bis 30 Personen. Jeden Donnerstag Spare Ribs und Steaks vom Grill, bitte reservieren.', '50% 50%'),
            ('k2.jpg', 'Deele', 'Für 25 bis 80 Personen: gemütlicher kleiner Saal mit separater Theke, Kaminfeuer und Vorraum für das Büffet.', '50% 50%'),
            ('k3.jpg', 'Kegelbahnen', 'Bundeskegelbahn und Scherenbahn, gefüllte Getränkekühlschränke zur Selbstbedienung und eine eigene kleine Speisekarte.', '50% 50%'),
            ('k4.jpg', 'Campingplatz', 'Rund 6 ha im Grünen mit Quellsee zum Baden. Für Tagescamper und Kurzurlauber, mit Zelt, Wohnwagen oder Wohnmobil.', '50% 50%')])
        + moment('mo.jpg', 'Wanderungen in den Eleonorenwald, <em>danach gemütlich auf der Terrasse sitzen.</em>', 'Heidehof · Neulorup 22', '50% 55%')
        + cards('feiern', 'Festsaal', 'Hochzeit, Geburtstag, <em>Weihnachtsfeier.</em>', 'Von rustikaler Gemütlichkeit im Kaminzimmer bis zur gediegenen Eleganz: Wir richten den Saal passend für Sie her.', [
            ('f1.jpg', 'Festsaal für ca. 250', 'Tanzfläche aus Parkett, Bühne für Band oder DJ, eigene große Theke. Modern, rustikal und klimatisiert.', '50% 50%'),
            ('f2.jpg', 'Feste Tafel', 'Runde Tische oder lange Tafel, festlich gedeckt für Ihre Gesellschaft.', '50% 50%'),
            ('f3.jpg', 'Sommerterrasse', 'Mit Weinlaube und Hochzeitsgarten am See. Freie Trauung möglich.', '50% 50%')], 'alt')
        + gallery('eindruecke', 'Eindrücke', 'Ein Blick <em>in den Heidehof.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + story('historie', 'Historie', 'Eine Familie, <em>seit Generationen.</em>', [
            'Hermann Jansen-Olliges und seine Frau Maria Gertrud kauften sich in Neulorup ein: die Gaststätte und Landwirtschaft Jansen-Olliges, genannt Hütten-Harm.',
            'Heute empfiehlt sich der gemütlich eingerichtete Heidehof mit Übernachtungsmöglichkeit und diversen Nebenräumen für Tagungen und Festlichkeiten aller Art.'],
            'st.jpg', 'Der Heidehof am Waldrand', tl=[('Hütten-Harm', 'so heißt der Hof bis heute'), ('Ausflüge', 'Eleonorenwald und Tatemeer')])
        + contact(s) + footer(s))

P3, D3 = '#1f6b3a', '#15261b'
S = SITES['heidehof'] = site(
    slug='heidehof-friesoythe', firma='Heidehof Jansen-Olliges', web='heidehof-jo.de', fonts='artland', branche='Gasthof, Festsaal & Camping',
    logo_txt='Heidehof<small>Die Note des Besonderen</small>', cta='Anfrage stellen',
    title='Heidehof Jansen-Olliges – Gastronomie, Festsaal, Kegelbahn, Camping', desc='Heidehof Jansen-Olliges in Friesoythe-Gehlenberg: regionale Küche, Festsaal für 250 Gäste, Kegelbahnen und Campingplatz mit Quellsee.',
    tel='04493 921303', tel_i='+494493921303', mail='info@heidehof-jo.de', adresse='Neulorup 22, 26169 Friesoythe', google=None,
    nav=[('Angebot', 'angebot'), ('Festsaal', 'feiern'), ('Historie', 'historie'), ('Kontakt', 'kontakt')],
    hours=[('Do – So', '18:00 – 23:00 Uhr'), ('Küche', '18:00 – 20:30 Uhr'), ('Donnerstag', 'Spare Ribs & Steaks vom Grill')],
    form_opts=['Tisch im Restaurant', 'Feier im Saal', 'Kegelbahn', 'Campingplatz'], form_lbl='Anliegen', form_h3='Anfrage stellen', form_btn='Anfrage senden',
    form_p='Schreiben Sie uns Datum, Personenzahl und Anlass. Wir rufen Sie zurück.',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Sie.</em>', kt_p='Persönlich erreichen Sie uns mindestens während unserer Öffnungszeiten.',
    vars=V.format(bg='#f8faf6', ink='#15261b', mute='#56645a', p=P3, dk=D3, s2='#ebf2ea', fh='"DM Serif Display",Georgia,serif', fb='"Libre Franklin",system-ui,sans-serif', lh=46),
    css=css_g(P3, D3))
S['css2'] = hz('#ebf2ea')
S['bot'] = BOT('Maria', 'Ihre Gastgeberin', 'dem Heidehof', [
    ['Wann haben Sie geöffnet?', 'Donnerstag bis Sonntag von 18 bis 23 Uhr, die Küche bis 20:30 Uhr. Donnerstags gibt es Spare Ribs und Steaks vom Grill.'],
    ['Wie viele Gäste passen in den Saal?', 'Der Festsaal fasst ca. 250 Personen, die Deele 25 bis 80. Rufen Sie an: 04493 921303.'],
    ['Kann ich bei Ihnen campen?', 'Ja, als Tagescamper oder Kurzurlauber mit Zelt, Wohnwagen oder Wohnmobil. Mit Quellsee, Strom und Sanitäranlagen.']],
    ['#angebot', '#feiern', '#historie', '#kontakt'])
HH = R + 'heidehof/i/'
S['img'] = {'m1.jpg': (HH + '31.jpg', 1000), 'm2.jpg': (HH + '18.jpg', 1600), 'm3.jpg': (HH + '42.jpg', 1600),
    'k1.jpg': (HH + '17.jpg', 900), 'k2.jpg': (HH + '35.jpg', 900), 'k3.jpg': (HH + '38.jpg', 900), 'k4.jpg': (HH + '43.jpg', 900),
    'mo.jpg': (HH + '42.jpg', 1800), 'f1.jpg': (HH + '33.png', 900), 'f2.jpg': (HH + '26.jpg', 900), 'f3.jpg': (HH + '32.png', 900),
    'g1.jpg': (HH + '24.jpg', 900), 'g2.jpg': (HH + '29.jpg', 900), 'g3.jpg': (HH + '27.jpg', 900), 'g4.jpg': (HH + '40.jpg', 900), 'g5.jpg': (HH + '30.jpg', 1000),
    'st.jpg': (HH + '05.jpg', 1000)}
S['body'] = b_heidehof
S['social'] = [('Instagram', 'https://www.instagram.com/heidehof.jansenolliges/')]

# ─────────────── 4 · Restaurant Kalimera, Bad Zwischenahn ───────────────
def b_kalimera(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Kalimera', 'heißt „Guten Tag“'), False),
                                       ('m2.jpg', ('Unser Restaurant', 'Modern und zwanglos'), False),
                                       ('m3.jpg', ('Unsere Theke', 'Weine & griechische Liköre'), False)],
        ubar=[('110', 'Plätze auf der Terrasse'), ('Lieferservice', 'auch mit EC-Karte'), ('Barrierefrei', 'Sanitäranlagen')],
        ey='Restaurant Kalimera · Griechisch-mediterran · Bad Zwischenahn',
        h1='Ein bisschen Griechenland <em>in Bad Zwischenahn.</em>',
        sub='Griechische Spezialitäten und mediterrane Speisen in einem modernen, zwanglosen Ambiente. Von der Vorspeise mit Aperitif bis zum griechischen Likör danach.'))
        + marquee(['Griechische Spezialitäten', 'Mediterran-vegetarisch', 'Feine Weine', 'Griechische Liköre', 'Desserts', 'Terrasse mit 110 Plätzen', 'Lieferservice', 'Freies WLAN'], 'wm')
        + cards('kueche', 'Unsere Küche', 'Alles, was <em>das Herz begehrt.</em>', 'Von leckeren Vorspeisen bis zur vielfältigen Auswahl an Hauptgerichten ist für jeden Geschmack das Passende dabei.', [
            ('k1.jpg', 'Griechische Spezialitäten', 'Hervorragende Fleischgerichte, wie man sie aus Griechenland kennt, und köstliche mediterran-vegetarische Gerichte.', '50% 50%'),
            ('k2.jpg', 'Weine & Liköre', 'Eine feine Auswahl an Weinen, die ideal zu unseren Gerichten passt. Danach gern einer unserer griechischen Liköre.', '50% 50%'),
            ('k3.jpg', 'Lieferservice', 'Lieber zu Hause genießen? Bestellen Sie telefonisch unter 04403 9841480. Bezahlung auch mit EC-Karte.', '50% 50%')])
        + moment('mo.jpg', 'Entspannte Stunden, ein gutes Glas Wein <em>und das Treiben des Kurortes beobachten.</em>', 'Restaurant Kalimera · In der Horst 23', '50% 50%')
        + gallery('eindruecke', 'Eindrücke', 'Ein Blick <em>ins Kalimera.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + story('ueber', 'Unser Name', 'Kalimera heißt <em>„Guten Morgen“.</em>', [
            'Καλημέρα meint auf Deutsch so viel wie „Guten Tag“ oder „Guten Morgen“. Diesen Ausruf haben wir uns zu Herzen genommen: Unser Logo symbolisiert die aufgehende Sonne Griechenlands.',
            'Der sonnig-goldene Schriftzug, die gedeckten Farben und das Dekor holen ein bisschen Griechenland nach Bad Zwischenahn. Wir leben Gastfreundschaft und freuen uns auf Ihren Besuch.'],
            'st.jpg', 'Unser Gastraum', tl=[('Mo', 'Ruhetag'), ('So', 'ab 12 Uhr geöffnet')])
        + contact(s) + footer(s))

P4, D4 = '#d9822b', '#1e1a17'
S = SITES['kalimera'] = site(
    slug='kalimera-bad-zwischenahn', firma='Restaurant Kalimera', web='kalimera-zwischenahn.de', fonts='elia', branche='Griechisches Restaurant',
    logo_txt='Kalimera<small>Restaurant · Bad Zwischenahn</small>',
    title='Restaurant Kalimera – griechisch-mediterran in Bad Zwischenahn', desc='Restaurant Kalimera in Bad Zwischenahn: original griechisch-mediterrane Küche, feine Weine, Terrasse mit 110 Plätzen und Lieferservice.',
    tel='04403 9841480', tel_i='+4944039841480', mail='info@kalimera-zwischenahn.de', adresse='In der Horst 23, 26160 Bad Zwischenahn', google=None,
    nav=[('Küche', 'kueche'), ('Eindrücke', 'eindruecke'), ('Über uns', 'ueber'), ('Reservieren', 'kontakt')],
    hours=[('Di – Sa', '15:00 – 22:00 Uhr'), ('Sonntag', '12:00 – 21:00 Uhr'), ('Montag', 'Ruhetag')],
    kt_ey='Reservieren', kt_h2='Wir freuen uns <em>auf Ihren Besuch.</em>', kt_p='Reservieren oder bestellen Sie telefonisch, oder hinterlassen Sie hier Ihren Wunschtermin.',
    vars=V.format(bg='#fbf8f4', ink='#1e1a17', mute='#62584f', p=P4, dk=D4, s2='#f5ece1', fh='"Gilda Display",Georgia,serif', fb='"Mulish",system-ui,sans-serif', lh=46),
    css=css_g(P4, D4))
S['css2'] = hz('#f5ece1')
S['bot'] = BOT('Sofia', 'Ihre Gastgeberin', 'Kalimera', [
    ['Wann haben Sie geöffnet?', 'Dienstag bis Samstag 15 bis 22 Uhr, Sonntag 12 bis 21 Uhr. Montag ist Ruhetag.'],
    ['Liefern Sie auch?', 'Ja. Bestellen Sie telefonisch unter 04403 9841480. Bezahlung auch beim Lieferservice mit EC-Karte.'],
    ['Gibt es vegetarische Gerichte?', 'Ja, neben unseren Fleischgerichten bieten wir köstliche mediterran-vegetarische Gerichte an.']],
    ['#kueche', '#eindruecke', '#ueber', '#kontakt'])
KA = R + 'kalimera/i/'
S['img'] = {'m1.jpg': (KA + '01.jpg', 1600), 'm2.jpg': (KA + '02.jpg', 1600), 'm3.jpg': (KA + '03.jpg', 1600),
    'k1.jpg': (KA + '05.jpg', 900), 'k2.jpg': (KA + '09.jpg', 900), 'k3.jpg': (KA + '07.jpg', 900),
    'mo.jpg': (KA + '15.jpg', 1280), 'g1.jpg': (KA + '10.jpg', 1280), 'g2.jpg': (KA + '12.jpg', 900), 'g3.jpg': (KA + '13.jpg', 900), 'g4.jpg': (KA + '08.jpg', 900), 'g5.jpg': (KA + '11.jpg', 1280),
    'st.jpg': (KA + '17.jpg', 1200)}
S['body'] = b_kalimera
S['social'] = [('Instagram', 'https://www.instagram.com/kalimera.badzwischenahn/')]

# ─────────────── 5 · Restaurant Schomaker, Damme-Dümmerlohausen ───────────────
def b_schomaker(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Ihre Hochzeitslocation', 'Freie Trauung in unserer Parkanlage'), False),
                                       ('m2.jpg', ('Genuss vom Feinsten', 'Aus unserer Küche'), True),
                                       ('m3.jpg', ('Biergarten', 'Idyllisch angelegt'), False),
                                       ('m4.jpg', ('Festsaal', 'Bis zu 300 Personen'), False)],
        steam={'m2.jpg': '40%'},
        ubar=[('5. Generation', 'Familienbetrieb'), ('120 Jahre', 'Gastronomie'), ('bis 300', 'Gäste im Festsaal')],
        ey='Restaurant Schomaker · Dümmerlohausen am Dümmer',
        h1='Gut essen, stilvoll feiern, <em>rundum wohlfühlen.</em>',
        sub='Die Atmosphäre eines südoldenburgischen Landgasthofes mit erstklassiger Küche, ausgesuchten Weinen und freundlichem Service. Seit Generationen in Familienbesitz.'))
        + marquee(['Hochzeiten', 'Freie Trauungen', 'Wildbuffet', 'Fischbuffet', 'Sektfrühstück', 'Biergarten', 'Kaminzimmer', 'Geschenkgutscheine'], 'wm')
        + svc('events', 'Termine & Buffets', 'Genuss <em>mit Termin.</em>', 'Alle Termine sind auch als Geschenkgutschein buchbar. Plätze begrenzt, reservieren Sie rechtzeitig unter 05491 7849.', [
            ('Gemütliches Sektfrühstück', 'Reichhaltiges Frühstücksbuffet in der Lounge mit Fisch, Käse und veganen Aufstrichen. So., 06.12.2026 als Nikolaus-Frühstück, 9 bis 11:30 Uhr.'),
            ('All-inclusive-Weihnachtsfeier', 'Für Firmen und Cliquen mit DJ, Buffet, Tanz und Drinks. 12.12.2026, 19 bis 3 Uhr.'),
            ('Weihnachten am Buffet', '1. und 2. Weihnachtstag großes Familienbuffet um 11:30 oder 13:30 Uhr. Abends am 1. Weihnachtstag à la carte.'),
            ('Silvester Gala-Buffet', 'Großes Silvester-Gala-Buffet, Beginn 19 Uhr.')])
        + cards('feiern', 'Stilvoll feiern', 'Ihre perfekte <em>Hochzeitslocation.</em>', 'Rustikaler Landhaus-Charme mit komfortabler Moderne, inmitten einer großen idyllischen Anlage.', [
            ('f1.jpg', 'Hochzeiten', 'Festsaal für bis zu 300 Personen, Sektempfang und Canapés. Wir vermitteln gern Musiker, Floristen und Fotografen.', '50% 50%'),
            ('f2.jpg', 'Freie Trauungen', 'Ja sagen unter freiem Himmel, mitten in unserer Parkanlage.', '50% 50%'),
            ('f3.jpg', 'Familien- & Firmenfeiern', 'Im urigen Kaminzimmer mit ca. 20 Personen, im edlen Clubzimmer mit ca. 50 oder im großen Saal.', '50% 50%')])
        + moment('mo.jpg', 'Ein kühles, frisch gezapftes Pils <em>in unserem idyllischen Biergarten.</em>', 'Restaurant Schomaker · Dümmerstraße 7', '50% 55%')
        + cards('kueche', 'Essen & Trinken', 'Genuss <em>vom Feinsten.</em>', 'Traditionelle Fisch- und Wildgerichte, gern auch verfeinert, und Buffets in elegant-rustikalem Ambiente.', [
            ('k1.jpg', 'Restaurant', 'Südoldenburgischer Landgasthof mit erstklassiger Küche und ausgesuchten Weinen.', '50% 50%'),
            ('k2.jpg', 'Kaminzimmer', 'Urig und gemütlich am offenen Feuer.', '50% 50%'),
            ('k3.jpg', 'Catering', 'Unser Essen auch bei Ihnen zu Hause. Rufen Sie an, wir beraten Sie gern.', '50% 50%')], 'alt')
        + story('ueber', 'Über uns', 'Mit Leidenschaft, <em>in fünfter Generation.</em>', [
            'Als Eigentümer und Betreiber blicken wir auf mehr als 120 Jahre Gastronomie mit unzähligen Hochzeiten und vielen tollen Feiern zurück.',
            'Wir verstehen uns nicht nur als Veranstalter, sondern als Teilnehmer unvergesslicher Lebensereignisse. Von Anfang bis Ende, mit Herz und Seele.'],
            'st.jpg', 'Familie Schomaker und Skrapic', tl=[('Sebastian & Sandra Skrapic', 'geb. Schomaker'), ('Bernd Schomaker', 'Familienbetrieb')])
        + gallery('eindruecke', 'Eindrücke', 'Feste <em>bei Schomaker.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + contact(s) + footer(s))

P5, D5 = '#a3201d', '#231a17'
S = SITES['schomaker'] = site(
    slug='schomaker-damme', firma='Restaurant Schomaker', web='restaurant-schomaker.de', fonts='meyer', branche='Restaurant & Hochzeitslocation',
    title='Restaurant Schomaker – Landgasthof & Hochzeitslocation am Dümmer', desc='Restaurant Schomaker in Damme-Dümmerlohausen: Familienbetrieb in 5. Generation, Hochzeiten bis 300 Gäste, freie Trauungen, Biergarten und Buffets.',
    tel='05491 7849', tel_i='+4954917849', mail='info@restaurant-schomaker.de', adresse='Dümmerstraße 7, 49401 Damme', google=None,
    nav=[('Termine', 'events'), ('Feiern', 'feiern'), ('Küche', 'kueche'), ('Über uns', 'ueber'), ('Reservieren', 'kontakt')],
    hours=[('Di – Do', '17:00 – 22:00 Uhr'), ('Freitag', '17:00 – 24:00 Uhr'), ('Samstag', '11:30 – 14:00, 17:00 – 24:00 Uhr'), ('Sonntag', '11:30 – 22:00 Uhr'), ('Montag', 'Ruhetag')],
    form_opts=['À la carte', 'Hochzeit', 'Familienfeier', 'Firmenfeier', 'Event'], form_lbl='Anlass',
    kt_ey='Reservieren', kt_h2='Wir freuen uns <em>auf Sie!</em>', kt_p='Tisch direkt hier anfragen oder unter 05491 7849 reservieren.',
    vars=V.format(bg='#fbf8f5', ink='#231a17', mute='#665a53', p=P5, dk=D5, s2='#f4ece6', fh='"Bitter",Georgia,serif', fb='"Karla",system-ui,sans-serif', lh=50),
    css=css_g(P5, D5, '.hd .logo img{height:50px}'))
S['css2'] = hz('#f4ece6')
S['bot'] = BOT('Sandra', 'Ihre Gastgeberin', 'Schomaker', [
    ['Wann haben Sie geöffnet?', 'Dienstag bis Donnerstag 17 bis 22 Uhr, Freitag bis 24 Uhr, Samstag 11:30 bis 14 und ab 17 Uhr, Sonntag 11:30 bis 22 Uhr. Montag Ruhetag.'],
    ['Kann ich bei Ihnen heiraten?', 'Ja. Festsaal bis zu 300 Personen und freie Trauungen in unserer Parkanlage. Tel. 05491 7849.'],
    ['Gibt es Gutscheine?', 'Ja, alle Termine sind auch als Geschenkgutschein buchbar. Einfach anrufen oder eine E-Mail schreiben.']],
    ['#events', '#feiern', '#kueche', '#kontakt'])
SO = R + 'schomaker/o/'
S['img'] = {'logo.png': (SO + '00.png', 400), 'm1.jpg': (SO + '19.jpg', 1500), 'm2.jpg': (SO + '13.jpg', 1000), 'm3.jpg': (SO + '14.jpg', 1000), 'm4.jpg': (SO + '27.jpg', 1000),
    'f1.jpg': (SO + '22.jpg', 900), 'f2.jpg': (SO + '24.jpg', 900), 'f3.jpg': (SO + '32.jpg', 900),
    'mo.jpg': (SO + '38.jpg', 1500), 'k1.jpg': (SO + '40.jpg', 900), 'k2.jpg': (SO + '43.jpg', 900), 'k3.jpg': (SO + '12.jpg', 900),
    'st.jpg': (SO + '05.jpg', 1500), 'g1.jpg': (SO + '02.jpg', 1500), 'g2.jpg': (SO + '16.jpg', 667), 'g3.jpg': (SO + '33.jpg', 900), 'g4.jpg': (SO + '28.jpg', 900), 'g5.jpg': (SO + '15.jpg', 1000)}
S['body'] = b_schomaker
S['social'] = [('Instagram', 'https://www.instagram.com/restaurantschomaker/')]
