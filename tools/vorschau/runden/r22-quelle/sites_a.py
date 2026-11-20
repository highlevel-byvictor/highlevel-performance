"""Akquise-Agent 20.11.2026 (Freitag, Restaurants/Cafés): 5 Betriebe mit Instagram und schwacher Website.
Texte, Gerichte, Bilder und Logos stammen von den Originalseiten. Keine erfundenen Preise, Stimmen oder Gerichtsnamen.
Google-Sterne werden nicht gezeigt (nicht geprüft)."""
from common import *
SITES = {}

# ─────────────── 1 · Mühlencafé & Restaurant Borgerding, Vechta-Langförden ───────────────
def b_borgerding(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Aus unserer Küche', 'Frisch serviert im Mühlencafé'), True),
                                       ('m2.jpg', ('Feiern bis 250 Gäste', 'Saalbetrieb Borgerdings Mühle'), False),
                                       ('m3.jpg', ('Zwei Etagen', 'Gruppen von 20 bis ca. 100 Personen'), False)],
        steam={'m1.jpg': '42%'},
        ubar=[('Seit 1878', 'in Familienhand'), ('2 Etagen', '+ 150 Plätze draußen'), ('bis 250', 'Gäste im Saal')],
        ey='Mühlencafé & Restaurant · Langförden bei Vechta',
        h1='Kaffee und Kuchen <em>an der Mühle.</em>',
        sub='Selbstgebackener Kuchen, Stuten, Schwarzbrot und Eisbecher in idyllischer Atmosphäre an unserem Mühlenteich. Für Gruppen kochen wir auch zum Abendessen.'))
        + marquee(['Selbstgebackener Kuchen', 'Frühstücksbuffet', 'Eisbecher', 'Spargelessen', 'Grünkohlessen', 'Karpfenessen', 'Feiern bis 250 Gäste', 'Spielplatz'], 'wm')
        + cards('angebot', 'Bei uns', 'Was Sie an der Mühle <em>erwartet.</em>', 'Ob zum Frühstück, Kaffee oder Abendessen: Ein Besuch bei uns ist immer ein Erlebnis.', [
            ('k1.jpg', 'Kaffee & Kuchen', 'Kaffee, Latte macchiato und unsere reichhaltige Auswahl an selbstgebackenem Kuchen, dazu Stuten, Schwarzbrot und Eisbecher.', '50% 50%'),
            ('k2.jpg', 'Gruppen & Abendessen', 'Gruppen ab 20 bis ca. 100 Personen bewirten wir auf zwei Etagen. Abendessen nach vorheriger Menüabsprache.', '50% 50%'),
            ('k3.jpg', 'Saisonale Essen', 'Spargelessen, Grünkohlessen oder Karpfenessen à la Borgerdings Mühle.', '50% 50%'),
            ('k4.jpg', 'Feiern im Saal', 'Hochzeiten, Geburtstage, Betriebsfeste, Bälle oder Weihnachtsfeiern. Buffet oder Menü, runde Tische oder lange Tafel.', '50% 50%')])
        + moment('mo.jpg', 'Ihr Kaffee auf der Terrasse, <em>die Kleinen auf dem Spielplatz</em> – immer im Blickfeld.', 'Mühlencafé Borgerding · Langförden', '50% 45%')
        + gallery('eindruecke', 'Eindrücke', 'Ein Blick <em>ins Mühlencafé.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + story('geschichte', 'Unsere Geschichte', 'Eine Familie, <em>eine Mühle.</em>', [
            '1878 erwarb Franz Borgerding das Anwesen mit der Wassermühle. Der Mühlenbetrieb blieb bis heute ein reines Familienunternehmen, mit Gaststätte und später einem Saalbetrieb.',
            'Lange war es der Traum der Familie, wieder eine Mühle zu errichten. Am 14. Oktober 2007 öffnete das Mühlencafé seine Pforten, mit über 1000 Besuchern am ersten Tag.'],
            'st.jpg', 'Die Mühle am Mühlenteich', tl=[('Franz-Josef & Gabi Borgerding', 'Gastgeber'), ('Seit 1993', 'Saalbetrieb für bis zu 250 Personen')])
        + ablauf('weg', 'So einfach geht es', 'Ihr Besuch <em>bei uns.</em>', 'Für Gruppen und Feiern sprechen Sie uns einfach an.', ABL)
        + contact(s) + footer(s))

P1, D1 = '#8a5a2b', '#3b2a1c'
S = SITES['borgerding'] = site(
    slug='muehlencafe-borgerding-langfoerden', firma='Mühlencafé & Restaurant Borgerding', web='muehlencafe-borgerding.de', fonts='droste', branche='Café & Restaurant',
    logo_txt='Mühlencafé<small>& Restaurant Borgerding</small>',
    title='Mühlencafé & Restaurant Borgerding – Langförden', desc='Mühlencafé & Restaurant Borgerding in Langförden: selbstgebackener Kuchen am Mühlenteich, Frühstück, Gruppen und Feiern bis 250 Personen.',
    tel='04447 560', tel_i='+494447560', mail='kontakt@muehlencafe-borgerding.de', adresse='Zur Spredaer Mühle 19b, 49377 Vechta-Langförden', google=None,
    cta='Tisch anfragen', nav=[('Angebot', 'angebot'), ('Eindrücke', 'eindruecke'), ('Geschichte', 'geschichte'), ('Kontakt', 'kontakt')],
    hours=[('Do – So', '14:00 – 18:00 Uhr'), ('Mo – Mi', 'nach Vereinbarung'), ('Saal', '04447 505')],
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Sie.</em>', kt_p='Rufen Sie an oder schreiben Sie uns. Für Gruppen und Feiern beraten wir Sie gern persönlich.',
    vars=V.format(bg='#fbf7f1', ink='#2a1f17', mute='#6b5c4f', p=P1, dk=D1, s2='#f3ebdf', fh='"Lora",Georgia,serif', fb='"Source Sans 3",system-ui,sans-serif', lh=46),
    css=css_g(P1, D1))
S['css2'] = hz('#f3ebdf')
S['bot'] = BOT('Greta', 'Ihre Gastgeberin', 'Borgerding', [
    ['Wann haben Sie geöffnet?', 'Donnerstag bis Sonntag von 14 bis 18 Uhr. Montag bis Mittwoch nach Vereinbarung.'],
    ['Kann ich bei Ihnen feiern?', 'Ja. Im Mühlencafé für 20 bis ca. 100 Personen, im Saal Borgerdings Mühle für bis zu 250 Gäste. Tel. 04447 505.'],
    ['Gibt es Abendessen?', 'Für Gruppen mit vorheriger Menüabsprache. Sprechen Sie uns einfach an: 04447 560.']],
    ['#angebot', '#eindruecke', '#geschichte', '#kontakt'])
B = R + 'borgerding/'
S['img'] = {'m1.jpg': (B + '14.jpg', 1600), 'm2.jpg': (B + '23.jpg', 1600), 'm3.jpg': (B + '12.jpg', 1600),
    'k1.jpg': (B + '13.jpg', 900), 'k2.jpg': (B + '24.jpg', 900), 'k3.jpg': (B + '15.jpg', 900), 'k4.jpg': (B + '23.jpg', 900),
    'mo.jpg': (B + '22.jpg', 1920), 'g1.jpg': (B + '09.jpg', 1200), 'g2.jpg': (B + '06.jpg', 900), 'g3.jpg': (B + '07.jpg', 900), 'g4.jpg': (B + '26.jpg', 900), 'g5.jpg': (B + '10.jpg', 1200),
    'st.jpg': (B + '30.jpg', 1200)}
S['body'] = b_borgerding
S['social'] = [('Instagram', 'https://www.instagram.com/muehlencafe_borgerding/'), ('Facebook', 'https://www.facebook.com/MuehlencafeBorgerding')]

# ─────────────── 2 · GastWerk, Melle-Buer ───────────────
def b_gastwerk(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Besonders beliebt', 'Unsere GastWerk Burger'), False),
                                       ('m2.jpg', ('Am Kirchplatz', 'Fachwerk unter alten Linden'), False),
                                       ('m3.jpg', ('Happy Hour Mi – Fr', 'Cocktails & Mocktails'), False),
                                       ('m4.jpg', ('Klassiker', 'Knuspriges Schnitzel'), True)],
        pos={'m2.jpg': '50% 60%'}, steam={'m4.jpg': '45%'},
        ubar=[('Junge Küche', 'in altem Fachwerk'), ('Saisonal', 'wechselnde Karte'), ('Gegenüber', 'der Martinikirche')],
        ey='GastWerk Restaurant | Bar · Melle-Buer',
        h1='Junge Küche <em>in altem Fachwerk.</em>',
        sub='Frische Zutaten, kreative Gerichte, fast alles hausgemacht. Dazu Cocktails, ein frisch gezapftes Pils und ein ganz besonderes Flair in der historischen Kirchhofsburg von Buer.'))
        + marquee(['GastWerk Burger', 'Cocktails', 'Happy Hour', 'Terrasse unter der Linde', 'Außer-Haus-Service', 'Feiern bis 80 Gäste', 'Frühstück für Gruppen', 'Kneipenkrimi'], 'wm')
        + cards('kueche', 'Restaurant | Bar', 'Worauf haben <em>Sie Lust?</em>', 'Die kleine, aber feine Speisekarte wechselt saisonal. Fast alles wird im Haus selbst hergestellt.', [
            ('k1.jpg', 'GastWerk Burger', 'Ihr Lieblingsburger in uriger Atmosphäre, dazu ein Glas Wein oder ein frisch gezapftes Pils.', '50% 50%'),
            ('k2.jpg', 'Cocktails & Bar', 'Mittwochs bis freitags Happy Hour von 18 bis 19 Uhr für alle Cocktails und Mocktails.', '50% 40%'),
            ('k3.jpg', 'Saisonale Küche', 'Kreative Gerichte aus frischen Zutaten, abgestimmt auf die Jahreszeit.', '50% 50%'),
            ('k4.jpg', 'Frühstück für Gruppen', 'Ab 20 Personen, mindestens zwei Tage vorher reservieren und entspannt verwöhnen lassen.', '50% 50%')])
        + moment('mo.jpg', 'Unter der prächtigen alten Linde, <em>mit Blick auf die Martinikirche.</em>', 'Unsere Terrasse · Kirchplatz 2', '50% 55%')
        + cards('feiern', 'Feiern Sie mit uns', 'Ihr Fest <em>in kleinem Rahmen.</em>', 'Restaurant mit urigen Fachwerk-Nischen für 30 Personen, Clubraum für weitere 20, das „Alte Café“ für 30 Gäste und bei schönem Wetter die Terrasse.', [
            ('f1.jpg', 'Familienfeiern', 'Geburtstag, Taufe, Kommunion, Konfirmation, Silber- und Goldhochzeit.', '50% 50%'),
            ('f2.jpg', 'Firma & Verein', 'Weihnachtsfeier, Firmenevent, Jubiläum, Tagung oder Vereinsfeier.', '50% 50%'),
            ('f3.jpg', 'Kneipenkrimi & Quiz', 'Kneipenkrimi „Das tödliche Rezept“ am 26. Februar 2027, Kneipenquiz am 19. März 2027.', '50% 50%')], 'alt')
        + gallery('eindruecke', 'Eindrücke', 'Ein Abend <em>im GastWerk.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + story('ueber', 'Über uns', 'Alt und Neu, <em>perfekt vereint.</em>', [
            'Mit sanfter Hand und viel Herzblut wurde das denkmalgeschützte Fachwerkgebäude am alten Torbogen, dem „Osnabrücker Tor“, aufwändig restauriert und modernisiert.',
            'Ein Ort zum Wohlfühlen, für gemütliche Stunden mit Freunden, ein Ort zum Genießen. An Konzertabenden in der Martinikirche und im B22 sind wir oft ausgebucht, reservieren Sie frühzeitig.'],
            'st.jpg', 'Das GastWerk am Kirchplatz in Buer', tl=[('Nadin Weber', 'Inhaberin'), ('Außer-Haus', 'Mi – Sa ab 18 Uhr, So ab 17 Uhr')])
        + contact(s) + footer(s))

P2, D2 = '#5b7a3a', '#1f2a18'
S = SITES['gastwerk'] = site(
    slug='gastwerk-melle-buer', firma='GastWerk Restaurant | Bar', web='gastwerk-melle.com', fonts='karbarosa', branche='Restaurant & Bar',
    logo_txt='GastWerk<small>Restaurant | Bar · Buer</small>',
    title='GastWerk Restaurant | Bar – Melle-Buer', desc='GastWerk in Melle-Buer: junge Küche in altem Fachwerk, GastWerk Burger, Cocktails, Terrasse mit Blick auf die Martinikirche.',
    tel='05427 80195-90', tel_i='+4954278019590', mail='', adresse='Kirchplatz 2, 49328 Melle-Buer', google=None,
    nav=[('Küche', 'kueche'), ('Feiern', 'feiern'), ('Eindrücke', 'eindruecke'), ('Über uns', 'ueber'), ('Reservieren', 'kontakt')],
    hours=[('Mi – Sa', 'ab 18:00 Uhr'), ('Sonntag', 'ab 17:00 Uhr'), ('Montag', 'Ruhetag')],
    kt_ey='Reservieren', kt_h2='Reservieren Sie <em>Ihren Tisch.</em>', kt_p='Wir garantieren die Öffnungszeiten bei vorheriger Reservierung. Gruppen ab 20 Personen gern auch außerhalb der Öffnungszeiten.',
    vars=V.format(bg='#faf8f3', ink='#1d2318', mute='#5b6253', p=P2, dk=D2, s2='#eef1e6', fh='"Fraunces",Georgia,serif', fb='"Nunito",system-ui,sans-serif', lh=46),
    css=css_g(P2, D2))
S['css2'] = hz('#eef1e6')
S['bot'] = BOT('Linda', 'Ihre Gastgeberin', 'GastWerk', [
    ['Wann haben Sie geöffnet?', 'Mittwoch bis Samstag ab 18 Uhr, Sonntag ab 17 Uhr. Montag ist Ruhetag. Warme Küche in der Regel bis 21 Uhr.'],
    ['Gibt es Happy Hour?', 'Ja, mittwochs bis freitags von 18 bis 19 Uhr für alle Cocktails und Mocktails.'],
    ['Kann ich bei Ihnen feiern?', 'Gern. Restaurant 30 Personen, Clubraum 20, „Altes Café“ 30, dazu die Terrasse. Rufen Sie an: 05427 80195-90.']],
    ['#kueche', '#feiern', '#eindruecke', '#kontakt'])
G = R + 'gastwerk/'
S['img'] = {'m1.jpg': (G + '10.jpg', 1600), 'm2.jpg': (G + '48.jpg', 1600), 'm3.jpg': (G + '40.jpg', 1600), 'm4.jpg': (G + '08.jpg', 1600),
    'k1.jpg': (G + '32.jpg', 900), 'k2.jpg': (G + '18.jpg', 900), 'k3.jpg': (G + '07.jpg', 900), 'k4.jpg': (G + '74.jpg', 900),
    'mo.jpg': (G + '44.jpg', 1800), 'f1.jpg': (G + '65.jpg', 900), 'f2.jpg': (G + '58.jpg', 900), 'f3.jpg': (G + '02.jpg', 900),
    'g1.jpg': (G + '34.jpg', 1400), 'g2.jpg': (G + '81.jpg', 900), 'g3.jpg': (G + '63.jpg', 900), 'g4.jpg': (G + '68.jpg', 900), 'g5.jpg': (G + '30.jpg', 1400),
    'st.jpg': (G + '52.jpg', 1200)}
S['body'] = b_gastwerk
S['social'] = [('Instagram', 'https://www.instagram.com/gastwerk.buer')]

# ─────────────── 3 · Restaurant Olympia, Papenburg ───────────────
def b_olympia(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Am Hauptkanal', 'Restaurant Olympia Papenburg'), False),
                                       ('m2.jpg', ('Griechisch-mediterran', 'Gedeckt für Ihren Abend'), False),
                                       ('m3.jpg', ('90 Plätze innen', 'Platz für die ganze Familie'), False)],
        pos={'m1.jpg': '50% 55%'}, steam={'m2.jpg': '48%'},
        ubar=[('Täglich', 'ab 17:30 Uhr'), ('90 + 80', 'Plätze innen und außen'), ('Barrierefrei', 'stufenloser Zugang')],
        ey='Restaurant Olympia · Griechisch-mediterran · Papenburg',
        h1='Griechenland, <em>am Hauptkanal.</em>',
        sub='Griechische Klassiker und mediterrane Spezialitäten, frisch zubereitet und mit viel Wert auf Qualität und Geschmack. Dazu Weine aus Griechenland, Deutschland, Italien und Spanien.'))
        + marquee(['Saganaki', 'Fetakäse Sfoliata', 'Melitsanes Tigani', 'Garides', 'Baby-Calamaris', 'Vom Grill', 'Aus dem Meer', 'Griechische Weine'], 'wm')
        + svc('karte', 'Aus unserer Karte', 'Vorspeisen, <em>wie in Griechenland.</em>', 'Eine kleine Auswahl unserer Empfehlungen und Klassiker.', [
            ('Korfu – Überbackener Feta', 'Griechischer Fetakäse aus dem Ofen mit Paprika, Peperoni und Tomaten, veredelt mit Grana Padano.'),
            ('Fetakäse Sfoliata', 'Fetakäse im knusprigen Blätterteigmantel mit Honig, weißem und schwarzem Sesam und Granatapfelkernen.'),
            ('Saganaki', 'Goldbraun gebratener Fetakäse, serviert auf marinierten Tomaten.'),
            ('Melitsanes Tigani', 'Knusprig gebratene Auberginen mit Tomatensoße, Grana Padano und Zaziki.'),
            ('Garides', 'Knusprige Garnelen im Kartoffelmantel, serviert mit Aioli.'),
            ('Baby-Calamaris', 'Zarte Baby-Calamaris vom Grill, mit Aioli serviert.')])
        + moment('mo.jpg', 'Ankommen, Platz nehmen, <em>den Abend genießen.</em>', 'Restaurant Olympia · Hauptkanal rechts 37', '50% 50%')
        + gallery('eindruecke', 'Eindrücke', 'Unser <em>Restaurant.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + story('ueber', 'Genuss & Gastfreundschaft', 'Unser Team ist <em>gern für Sie da.</em>', [
            'Freuen Sie sich auf frisch zubereitete griechisch-mediterrane Gerichte und eine gemütliche Atmosphäre. Individuelle Wünsche berücksichtigen wir nach Möglichkeit gern.',
            'Mit 90 Sitzplätzen innen und 80 Plätzen draußen haben wir auch für größere Gruppen ausreichend Platz. Unser Restaurant ist stufenlos über den Parkplatz erreichbar.'],
            'st.jpg', 'Restaurant Olympia am Hauptkanal', tl=[('Küche', 'täglich bis 21:00 Uhr'), ('Gruppen', 'bis zu 90 Plätze innen')])
        + ablauf('weg', 'So einfach geht es', 'Ihr Abend <em>bei uns.</em>', 'Reservieren Sie telefonisch oder über das Formular.', ABL)
        + contact(s) + footer(s))

P3, D3 = '#9a7b3c', '#1d2a36'
S = SITES['olympia'] = site(
    slug='olympia-papenburg', firma='Restaurant Olympia', web='olympia-papenburg.de', fonts='elia', branche='Griechisches Restaurant',
    title='Restaurant Olympia – griechisch-mediterran in Papenburg', desc='Restaurant Olympia in Papenburg: griechische Klassiker und mediterrane Spezialitäten am Hauptkanal, täglich ab 17:30 Uhr.',
    tel='04961 1219', tel_i='+4949611219', mail='info@olympia-papenburg.de', adresse='Hauptkanal rechts 37, 26871 Papenburg', google=None,
    nav=[('Karte', 'karte'), ('Eindrücke', 'eindruecke'), ('Über uns', 'ueber'), ('Reservieren', 'kontakt')],
    hours=[('Täglich', '17:30 – 21:00 Uhr Küche'), ('Danach', 'gern noch gemütlich ausklingen')],
    kt_ey='Reservieren', kt_h2='Reservieren Sie <em>Ihren Tisch.</em>', kt_p='Rufen Sie uns an oder hinterlassen Sie Ihren Wunschtermin. Wir melden uns persönlich zur Bestätigung.',
    vars=V.format(bg='#fbfaf6', ink='#1d2a36', mute='#56606a', p=P3, dk=D3, s2='#f2efe6', fh='"Gilda Display",Georgia,serif', fb='"Mulish",system-ui,sans-serif', lh=58),
    css=css_g(P3, D3, '.hd .logo img{height:58px}'))
S['css2'] = hz('#f2efe6', '#1d2a36')
S['bot'] = BOT('Eleni', 'Ihre Gastgeberin', 'Olympia', [
    ['Wann haben Sie geöffnet?', 'Täglich ab 17:30 Uhr. Unsere Küche ist bis 21 Uhr für Sie da.'],
    ['Haben Sie Platz für Gruppen?', 'Ja, 90 Plätze innen und 80 draußen. Rufen Sie an: 04961 1219.'],
    ['Darf mein Hund mit?', 'Leider nein. Wir lieben Hunde, haben aber keinen separaten Bereich für sie.']],
    ['#karte', '#eindruecke', '#ueber', '#kontakt'])
O = R + 'olympia/'
S['img'] = {'logo.png': (O + '07.jpg', 500, 'trimalpha'), 'm1.jpg': (O + '12.jpg', 1800), 'm2.jpg': (O + '20.jpg', 1700), 'm3.jpg': (O + '16.jpg', 1800),
    'mo.jpg': (O + '18.jpg', 1800), 'g1.jpg': (O + '24.jpg', 1400), 'g2.jpg': (O + '20.jpg', 1000), 'g3.jpg': (O + '10.jpg', 1000), 'g4.jpg': (O + '11.jpg', 900), 'g5.jpg': (O + '31.jpg', 1400),
    'st.jpg': (O + '22.jpg', 1200)}
S['body'] = b_olympia
S['social'] = [('Instagram', 'https://www.instagram.com/restaurantolympiapapenburg'), ('Facebook', 'https://www.facebook.com/OlympiaPapenburg')]

# ─────────────── 4 · Weberhaus, Melle ───────────────
def b_weberhaus(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Mitten im Wald', 'Das Weberhaus in Melle'), False),
                                       ('m2.jpg', ('Herbst-Saisonkarte', 'Grünkohl & Co.'), True),
                                       ('m3.jpg', ('Eventlocation', 'Feiern bis 185 Gäste'), False)],
        pos={'m1.jpg': '50% 60%'}, steam={'m2.jpg': '55%'},
        ubar=[('Wild', 'hausgemacht'), ('Kochschule', 'im eigenen Haus'), ('bis 185', 'Gäste bei Events')],
        ey='Weberhaus · Ausflugsrestaurant · Melle',
        h1='Regionale Küche <em>mit Charakter.</em>',
        sub='Wild, hausgemacht und modern interpretiert: ehrliche Gerichte aus besten Zutaten, ohne Fertigprodukte, inmitten einer zauberhaften Waldlandschaft.'))
        + marquee(['Wildragout', 'Wildspezialitäten', 'Rippchen mit BBQ-Soße', 'Flammkuchen', 'Hexenkartoffeln', 'Burger', 'Kochschule', 'Waldkapelle'], 'wm')
        + cards('kueche', 'Unsere Küche', 'Fisch, Fleisch, Wild, <em>Veggy und mehr.</em>', 'Bodenständige, aber erstklassige deutsche Küche mit regionalen Zutaten von höchster Qualität und Frische.', [
            ('k1.jpg', 'Wildspezialitäten', 'Unser berühmtes Wildragout überzeugt auch Nicht-Wildkenner.', '50% 50%'),
            ('k2.jpg', 'Saisonkarte', 'Der Herbst ist da: Grünkohl, Kürbis und Co. auf unserer neuen Saisonkarte.', '50% 50%'),
            ('k3.jpg', 'Für Genießer & Familien', 'Zarte Rippchen mit hausgemachter BBQ-Soße, knusprige Flammkuchen, Hexenkartoffeln und kreative Burger.', '50% 50%'),
            ('k4.jpg', 'Kochschule', 'Unsere Küchenprofis geben ihr Wissen weiter. Ideal als Team-Event, Junggesellenabschied oder Abend mit Freunden.', '50% 50%')])
        + moment('mo.jpg', 'Ein entspannter Abend im Grünen, <em>ein festlicher Anlass</em> oder ein kulinarisches Abenteuer.', 'Weberhaus 40 · Melle', '50% 50%')
        + cards('feiern', 'Eventlocation', 'Hochzeit, Betriebsfeier, <em>Weihnachten.</em>', 'Das besondere Ambiente unseres Restaurants inmitten des Waldes bietet Platz für Events mit bis zu 185 Gästen.', [
            ('f1.jpg', 'Heiraten', 'In unserer Waldkapelle führen wir auch individuelle Zeremonien durch.', '50% 50%'),
            ('f2.jpg', 'Firmenfeiern', 'Ob kleiner Kreis oder große Firmenweihnachtsfeier: Sichern Sie sich Ihren Wunschtermin.', '50% 50%'),
            ('f3.jpg', 'Feiern im Grünen', 'Geburtstag, Jubiläum oder Familienfest, drinnen oder draußen.', '50% 50%')], 'alt')
        + gallery('eindruecke', 'Eindrücke', 'Ein Blick <em>ins Weberhaus.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + ablauf('weg', 'So einfach geht es', 'Ihr Besuch <em>im Weberhaus.</em>', 'Die Straße Weberhaus ist komplett befestigt und Sommer wie Winter befahrbar, auch für Busse.', ABL)
        + contact(s) + footer(s))

P4, D4 = '#a0522d', '#2a2119'
S = SITES['weberhaus'] = site(
    slug='weberhaus-melle', firma='Weberhaus', web='das-weberhaus-melle.de', fonts='meyer', branche='Ausflugsrestaurant & Eventlocation',
    logo_txt='Weberhaus<small>Ausflugsrestaurant · Melle</small>',
    title='Weberhaus – Ausflugsrestaurant in Melle', desc='Weberhaus Melle: regionale Küche mit Charakter, Wildspezialitäten, Kochschule und Eventlocation für bis zu 185 Gäste.',
    tel='05422 9811088', tel_i='+4954229811088', mail='info@das-weberhaus-melle.de', adresse='Weberhaus 40, 49324 Melle', google=None,
    nav=[('Küche', 'kueche'), ('Feiern', 'feiern'), ('Eindrücke', 'eindruecke'), ('Reservieren', 'kontakt')],
    hours=[('Mi – Fr', '16:30 – 23:00 Uhr'), ('Samstag', '11:30 – 23:00 Uhr'), ('Sonntag', '09:00 – 23:00 Uhr')],
    kt_ey='Reservieren', kt_h2='Eine gemütliche Zeit <em>im Weberhaus.</em>', kt_p='Reservieren Sie telefonisch oder schreiben Sie uns Ihren Wunschtermin.',
    vars=V.format(bg='#faf6f0', ink='#2a2119', mute='#64574b', p=P4, dk=D4, s2='#f1e8dc', fh='"Bitter",Georgia,serif', fb='"Karla",system-ui,sans-serif', lh=46),
    css=css_g(P4, D4))
S['css2'] = hz('#f1e8dc')
S['bot'] = BOT('Hanna', 'Ihre Gastgeberin', 'Weberhaus', [
    ['Wann haben Sie geöffnet?', 'Mittwoch bis Freitag ab 16:30 Uhr, Samstag ab 11:30 Uhr, Sonntag ab 9 Uhr.'],
    ['Kann ich bei Ihnen heiraten?', 'Ja. Wir richten Hochzeiten mit bis zu 185 Gästen aus, Zeremonien auch in unserer Waldkapelle.'],
    ['Wie finde ich zu Ihnen?', 'Weberhaus 40 in Melle. Die Straße ist komplett befestigt, auch Busse können wenden.']],
    ['#kueche', '#feiern', '#eindruecke', '#kontakt'])
W = R + 'weberhaus/hq/'
S['img'] = {'m1.jpg': (W + '21.jpg', 1800), 'm2.jpg': (W + '05.jpg', 1600), 'm3.jpg': (W + '24.jpg', 1800),
    'k1.jpg': (W + '24.jpg', 900), 'k2.jpg': (W + '05.jpg', 900), 'k3.jpg': (W + '06.jpg', 900), 'k4.jpg': (W + '17.jpg', 900),
    'mo.jpg': (W + '16.jpg', 1800), 'f1.jpg': (W + '12.jpg', 900), 'f2.jpg': (W + '22.jpg', 900), 'f3.jpg': (W + '18.jpg', 900),
    'g1.jpg': (W + '19.jpg', 1400), 'g2.jpg': (W + '13.jpg', 900), 'g3.jpg': (W + '20.jpg', 900), 'g4.jpg': (W + '25.jpg', 900), 'g5.jpg': (W + '26.jpg', 1400)}
S['body'] = b_weberhaus
S['social'] = []

# ─────────────── 5 · Gasthof Schrage, Melle-Wellingholzhausen ───────────────
def b_schrage(s):
    return (hd(s) + hero_g(s, dict(imgs=[('m1.jpg', ('Unser LandWerk', 'Für Feiern und Hochzeiten'), False),
                                       ('m2.jpg', ('Seit 1846', 'Gedeckt für Ihren Abend'), False),
                                       ('m3.jpg', ('Feste Tafel', 'Für Ihre Gesellschaft'), False)],
        pos={'m2.jpg': '50% 55%'},
        ubar=[('Seit 1846', 'in Familienbesitz'), ('6. Generation', 'Mira & Hendrick Schrage'), ('70', 'Sitzplätze im Restaurant')],
        ey='Gasthof Schrage · Restaurant & Biergarten · Melle',
        h1='Regional genießen, <em>seit 1846.</em>',
        sub='Saisonale und regionale Gerichte aus sorgfältig ausgewählten, frischen Zutaten. Mit unseren weithin bekannten Schnitzelgerichten und einem idyllischen Biergarten am Haseradweg.'))
        + marquee(['Schnitzelgerichte', 'Saisonkarte', 'Vegetarisch & vegan', 'Biergarten', 'Kegelbahn', 'Hochzeiten', 'Freie Trauungen', 'Familienfeiern'], 'wm')
        + svc('kueche', 'Unser kulinarisches Angebot', 'Echtes <em>Küchenhandwerk.</em>', 'Unter der Leitung von Mira Schrage und Dennis Hellermann verwöhnt Sie unser Küchenteam mit regionalen Spezialitäten.', [
            ('Saisonkarte', 'Stets aktuelle Produkte aus unserer Region, frisch angerichtet.'),
            ('Schnitzelklassiker', 'Unsere weithin bekannten Schnitzelgerichte finden sich immer auf der Karte.'),
            ('Vegetarisch & vegan', 'Wechselnde Gerichte für Vegetarier und Veganer. Auf Unverträglichkeiten gehen wir gern ein.'),
            ('Ohne Zusatzstoffe', 'Natürliche Speisen und gewachsene Qualität, sorgsam eingekauft und zubereitet.')])
        + moment('mo.jpg', 'Für Genießer ein Ort für gute Küche, <em>für Brautpaare ein Ort für fantastische Feste.</em>', 'Gasthof Schrage · Dissener Straße 15', '50% 45%')
        + cards('feiern', 'Ihre Veranstaltungslocation', 'Hochzeiten, Familienfeste, <em>Firmenevents.</em>', 'Das LandWerk, das Haus des Gastes und der Quellengarten bieten einzigartiges Flair für unvergessliche Momente.', [
            ('f1.jpg', 'LandWerk', 'Unser Saal für Hochzeiten, Familienfeiern und Firmenevents.', '50% 50%'),
            ('f2.jpg', 'Freie Trauung im Quellengarten', 'Unser prämierter Garten mit dem Mondtor als Traubogen.', '50% 50%'),
            ('f3.jpg', 'Persönliche Planung', 'Veranstaltungsplanerin Franziska Buckentin begleitet Ihre Feier von der Idee bis zum Fest.', '50% 30%')], 'alt')
        + gallery('eindruecke', 'Eindrücke', 'Ein Blick <em>ins LandWerk.</em>', [
            ('g1.jpg', 'h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', 'h2r', '50% 50%')])
        + story('ueber', 'Familie Schrage', 'Seit 1846 <em>in Familienhand.</em>', [
            'Der Gasthof Schrage wird von Mira und Hendrick Schrage in sechster Generation geführt. Wir leben frische, junge Gastronomie und stehen für abwechslungsreiche, regionale Küche.',
            'Für Genießer hervorragende Küche, für Einheimische ein Ort der Begegnung und für Jubilare und Brautpaare fantastische Feste. In unserem Haus ist jeder willkommen.'],
            'st.jpg', 'Der Gasthof Schrage in früheren Zeiten', tl=[('Hendrick Schrage', 'Gastgeber und Inhaber'), ('Mira Schrage', 'Küche, mit Dennis Hellermann')])
        + contact(s) + footer(s))

P5, D5 = '#4f7a3b', '#1e2b1a'
S = SITES['schrage'] = site(
    slug='gasthof-schrage-melle', firma='Gasthof Schrage', web='gasthof-schrage.de', fonts='artland', branche='Restaurant & Gasthof',
    title='Gasthof Schrage – Restaurant & Biergarten in Melle', desc='Gasthof Schrage in Melle: regionale Küche seit 1846, Schnitzelklassiker, Biergarten am Haseradweg, Hochzeiten und Feiern im LandWerk.',
    tel='05429 306', tel_i='+495429306', mail='', adresse='Dissener Straße 15, 49326 Melle', google=None,
    nav=[('Küche', 'kueche'), ('Feiern', 'feiern'), ('Über uns', 'ueber'), ('Reservieren', 'kontakt')],
    hours=[('Mi – So', 'ab 17:00 Uhr'), ('Mo & Di', 'Ruhetag')],
    kt_ey='Reservieren', kt_h2='Das ganze Team <em>freut sich auf Sie.</em>', kt_p='Reservierungen und Bestellungen nehmen wir gern unter 05429 306 entgegen.',
    vars=V.format(bg='#fafaf6', ink='#1e2b1a', mute='#5a6455', p=P5, dk=D5, s2='#eef2e8', fh='"DM Serif Display",Georgia,serif', fb='"Libre Franklin",system-ui,sans-serif', lh=58),
    css=css_g(P5, D5, '.hd .logo img{height:58px}'))
S['css2'] = hz('#eef2e8')
S['bot'] = BOT('Mira', 'Ihre Gastgeberin', 'Gasthof Schrage', [
    ['Wann haben Sie geöffnet?', 'Mittwoch bis Sonntag ab 17 Uhr.'],
    ['Gibt es vegetarische Gerichte?', 'Ja, wir bieten wechselnde vegetarische und vegane Gerichte an. Unverträglichkeiten bitte bei der Reservierung nennen.'],
    ['Kann ich bei Ihnen heiraten?', 'Ja. LandWerk, Haus des Gastes und Quellengarten mit Mondtor für freie Trauungen. Tel. 05429 306.']],
    ['#kueche', '#feiern', '#ueber', '#kontakt'])
SC = R + 'schrage/'
S['img'] = {'logo.png': (SC + '00.jpg', 500, 'trimalpha'), 'm1.jpg': (SC + '02.jpg', 1800), 'm2.jpg': (SC + '06.jpg', 1400), 'm3.jpg': (SC + '04.jpg', 1400),
    'mo.jpg': (SC + '07.jpg', 1400), 'f1.jpg': (SC + '08.jpg', 900), 'f2.jpg': (SC + '12.jpg', 900), 'f3.jpg': (SC + '05.jpg', 900),
    'g1.jpg': (SC + '07.jpg', 900), 'g2.jpg': (SC + '05.jpg', 900), 'g3.jpg': (SC + '04.jpg', 900), 'g4.jpg': (SC + '08.jpg', 900),
    'st.jpg': (SC + '10.jpg', 1000)}
S['body'] = b_schrage
S['social'] = [('Instagram', 'https://www.instagram.com/gasthof_schrage/')]
