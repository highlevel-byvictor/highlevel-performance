"""Runde 19 · Schornsteinfeger 60 km um Bersenbrück: 9 weitere Betriebe. Texte und Logos der Betriebe, große Bilder von Pixabay (neutral beschriftet)."""
from common import *
SITES = {}
P = PIX19
R19 = '/home/claude/r19raw/'
D = {
 'Schornsteinfegerarbeiten': 'Reinigen, Messen und Überprüfen. Seit vielen Jahrhunderten sorgen Schornsteinfeger mit ihrer Arbeit für Sicherheit.',
 'Energieberatung': 'Wo lässt sich bei Ihnen Energie sparen, und mit welchem Aufwand? Wir zeigen es Ihnen neutral.',
 'Energieausweis': 'Die verbriefte Verbrauchsangabe Ihres Gebäudes. Jeder kennt den Verbrauch seines Pkw, kaum jemand den seines Eigenheims.',
 'Rauchwarnmelder': 'Rauchwarnmelder retten Leben. Wir beraten, installieren und prüfen Ihre Melder.',
 'Gashausschau': 'Wir sehen uns Ihre Gasleitung und die Geräte an und geben Ihnen ein sicheres Gefühl.',
 'Holzfeuchtemessung': 'Nur trockenes Holz brennt sauber. Wir messen die Feuchte Ihres Brennholzes.',
 'Feuerungstechnische Beratung': 'Moderne Feuerungsanlagen stellen hohe Ansprüche an Messtechnik und Know-how. Wir beraten vor dem Kauf.',
 'Brandschutz': 'Vorbeugen ist besser als löschen. Wir beraten Sie rund um den Brandschutz im Haus.',
 'Lüftungsanlagen': 'Wir prüfen und reinigen Lüftungsanlagen, damit die Luft im Haus sauber bleibt.',
 'Professionelle Solarreinigung': 'Saubere Module bringen mehr Ertrag. Wir reinigen Ihre Solaranlage fachgerecht.',
 'Blowerdoor': 'Mit dem Blower-Door-Test finden wir undichte Stellen in der Gebäudehülle.',
 'Thermografie': 'Die Wärmebildkamera zeigt, wo Ihr Haus Wärme verliert.',
 'Sanierungsfahrplan (iSfP)': 'Schritt für Schritt zum sparsamen Haus: Ihr individueller Sanierungsfahrplan.',
 'Gasleitungsprüfung': 'Wir prüfen Ihre Gasleitung auf Dichtheit und Gebrauchsfähigkeit.',
 'Hydraulischer Abgleich': 'Damit jeder Heizkörper genau die Wärme bekommt, die er braucht.',
 'Kaminofen- und Ofenrohrreinigung': 'Wir reinigen Kaminofen und Ofenrohr, damit Ihr Feuer sauber brennt.',
 'Bauberatung': 'Wir beraten Sie schon in der Planung zu Schornstein, Feuerstätte und Lüftung.',
 'Holz und Pelletofen': 'Beratung rund um Holz- und Pelletöfen, vom Aufstellort bis zum Schornstein.',
}

def mk(k, name, ort, strasse, plz, tel, tel_i, mail, web, quals, svcs, p, dk, s2, fam, fonts, hero, imgs, h1, sub, region, logo, lh, own=None, own_cap='', slugbase='', firma=None, mobil=None, extra_about=None, bot='Ruß'):
    firma = firma or f'Schornsteinfeger-Meisterbetrieb {name}'
    nach = name.split()[-1]
    ubar = [(q.split('|')[0], q.split('|')[1]) for q in quals[:3]]
    ey = f'Schornsteinfeger {name} · {ort}'
    def body(s):
        if hero == 'slides':
            top = hd(s) + hero_slides(s, dict(slides=['h1.jpg', 'h2.jpg'], pos={'h1.jpg': '50% 50%', 'h2.jpg': '50% 50%'}, ey=ey, h1=h1, sub=sub, ubar=ubar))
        elif hero == 'comp':
            top = hd(s, False) + hero_comp(s, dict(imgs=['h1.jpg', 'h2.jpg'], badge=('Meisterbetrieb', f'in {ort}'), ey=ey, h1=h1, sub=sub))
        else:
            top = hd(s, False) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg'], side=('l' if hero == 'splitl' else 'r'), big='', ubar=ubar, ey=ey, h1=h1, sub=sub))
        about = ['Als Schornsteinfeger-Betrieb sind wir der richtige Ansprechpartner für Sie, wenn es um Brandschutz, Umweltschutz, Energieeinsparung oder neutrale Beratung geht.',
                 extra_about or 'Qualität sorgt für Sicherheit. Wir messen uns an höchsten Ansprüchen und stehen Ihnen mit jahrelanger Erfahrung und Fachkenntnis zur Verfügung.']
        return (top + marquee(svcs + [region], 'wm')
            + svc('leistungen', 'Dienstleistungen', 'Weit mehr als <em>Schornsteinreinigung.</em>', 'Das Berufsbild des Schornsteinfegers hat sich gewandelt. Wir sind heute auch neutraler und unabhängiger Berater.', [(t, D[t]) for t in svcs[:6]])
            + promo('fokus', 'pr.jpg', svcs[1], 'Sicherheit, Umwelt und <em>Energie.</em>', D[svcs[1]] + ' Sprechen Sie uns einfach an.',
                    ['Vom Meisterbetrieb', 'Neutral und unabhängig', 'Termin direkt bei Ihnen zu Hause'], f'{svcs[1]} anfragen', 'alt')
            + ablauf('weg', 'So einfach geht es', 'Anfragen, Termin, <em>erledigt.</em>', 'Sie müssen sich um nichts kümmern.', [
                ('Anliegen schicken', 'Über das Formular oder direkt per Telefon. Sagen Sie kurz, worum es geht.'),
                ('Termin abstimmen', 'Wir melden uns bei Ihnen und finden einen Termin, der passt.'),
                ('Arbeit vor Ort', 'Wir kommen pünktlich, arbeiten sauber und erklären Ihnen das Ergebnis.')])
            + story('ueber', 'Über uns', 'Zum Glück gibt es <em>den Schornsteinfeger.</em>', about, 'ab.jpg', own_cap or f'Unterwegs in {region}', cls='dk',
                    tl=[(name, quals[0].split('|')[1]), (ort, 'und Umgebung')])
            + contact(s) + footer(s))
    hours = [('Termine', 'nach Vereinbarung')] + ([('Mobil', mobil)] if mobil else [])
    S = SITES[k] = site(
        slug=slugbase, firma=firma, web=web, fonts=fonts,
        title=f'Schornsteinfeger {name} – Meisterbetrieb in {ort}', desc=f'Schornsteinfeger {name} in {ort}: ' + ', '.join(svcs[:5]) + '.',
        tel=tel, tel_i=tel_i, mail=mail, adresse=f'{strasse}, {plz} {ort}', google=None,
        cta='Termin anfragen', nav=[('Leistungen', 'leistungen'), (svcs[1], 'fokus'), ('Ablauf', 'weg'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
        hours=hours, form_opts=svcs[:7] + ['Sonstiges'],
        form_h3='Termin anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
        kt_ey='Kontakt', kt_h2='Wir sind <em>für Sie da.</em>', kt_p='Rufen Sie an oder schreiben Sie uns. Wir kümmern uns.',
        vars=V.format(ink='#1c1c1c', mute='#575757', p=p, pi='#fff', dk=dk, s2=s2, fh=fam[0], fb=fam[1], lh=lh, ft=dk),
        css=f'''.h2,.hz h1,.hs h1,.hp h1{{font-weight:800;letter-spacing:-.02em}}.h2 em,.hz h1 em,.hp h1 em{{font-style:normal;color:{p}}}.hs h1 em{{font-style:normal;color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}.dk .h2 em{{color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}
.mq.wm span{{font-weight:700;font-size:15px}}.alt{{background:var(--s2)}}.sv .row div{{border-top:4px solid {p}}}.st.dk{{background:{dk};color:#fff}}.st.dk .lead{{color:rgba(255,255,255,.86)}}.st.dk .tl b{{color:#fff}}.rd .road div h3{{color:{p}}}
.hs .ubar b{{color:#fff}}.hs .ey{{color:#fff!important}}.hp .badge{{background:{p};color:#fff}}.hp .badge b{{color:#fff}}.ft img{{background:#fff;padding:8px 12px;height:66px}}{'#ueber figure{max-width:400px;justify-self:center}' if own else ''}
@media(max-width:820px){{.hz h1,.hs h1,.hp h1{{font-size:30px!important;hyphens:none!important;overflow-wrap:normal!important;word-break:normal!important}}}}''')
    S['css2'] = f'.hz{{--hz-bg:{s2};--hz-ink:#1c1c1c;--hz-mute:#575757;--hz-stroke:rgba(0,0,0,.07);--hz-cols:46fr 54fr}}.hz h1{{font-size:clamp(34px,4.2vw,66px)}}.hz .ey{{color:{p}}}'
    S['bot'] = BOT(bot, 'Ihr Schornsteinfeger-Lotse', nach, S, [
        ['Was machen Sie alles?', ', '.join(svcs[:6]) + '.'],
        ['Wie bekomme ich einen Termin?', f'Am schnellsten per Telefon: {tel}. Oder Sie nutzen das Formular.'],
        ['Wo sind Sie unterwegs?', f'In {ort} und Umgebung.']],
        ['#leistungen', '#fokus', '#ueber', '#kontakt'])
    S['img'] = {'logo.png': logo, 'h1.jpg': (P + imgs[0], 0), 'h2.jpg': (P + imgs[1], 0), 'pr.jpg': (P + imgs[2], 0), 'ab.jpg': (own, 0) if own else (P + imgs[3], 0)}
    S['body'] = body

NOTO = ('"Noto Sans",system-ui,sans-serif',) * 2; LATO = ('"Lato",system-ui,sans-serif',) * 2; RH = ('"Red Hat Display",system-ui,sans-serif', '"Red Hat Text",system-ui,sans-serif')
RAL = ('"Raleway",system-ui,sans-serif',) * 2; ROB = ('"Roboto",system-ui,sans-serif',) * 2; GUD = ('"Gudea",system-ui,sans-serif',) * 2

mk('bergmann', 'Jörg Bergmann', 'Bramsche', 'Luisenstraße 12', '49565', '05461 7039424', '+4954617039424', 'info@schornsteinfeger-bramsche.de', 'schornsteinfeger-bramsche.de',
   ['Meister|Schornsteinfegermeister', 'Energieberater|für Gebäude, HWK', 'Persönlich|und regional'],
   ['Schornsteinfegerarbeiten', 'Professionelle Solarreinigung', 'Rauchwarnmelder', 'Gashausschau'], '#4E8006', '#1f2a12', '#f4f6ef', LATO, 'r10vagts', 'slides',
   ['b2939551.jpg', '8114188.jpg', 'b1477987.jpg', 'b2853047.jpg'], 'Persönlich und regional. <em>Ihr Schornsteinfeger in Bramsche.</em>',
   'Schornsteinfegerarbeiten, Rauchwarnmelder, Gashausschau und professionelle Solarreinigung aus einer Hand.', 'Bramsche und Umgebung', I('bergmann', 4, 0), 64, slugbase='schornsteinfeger-bergmann-bramsche', bot='Kehr')
mk('rechtien', 'Gerd Rechtien', 'Nortrup', 'Am Poggenkamp 12', '49638', '05436 8833', '+4954368833', 'Rechtien-Schornsteinfeger@outlook.de', 'schornsteinfeger-rechtien.de',
   ['Meister|Schornsteinfegermeister und Heizungsbaumeister', 'Energieberater|HWK, KfW-Energie-Effizienz-Experte', 'TRGS 519|Sachkundiger Asbest'],
   ['Schornsteinfegerarbeiten', 'Energieberatung', 'Energieausweis', 'Blowerdoor', 'Thermografie', 'Hydraulischer Abgleich', 'Brandschutz', 'Lüftungsanlagen', 'Rauchwarnmelder', 'Gashausschau', 'Holzfeuchtemessung'],
   '#C8102E', '#22262b', '#f5f4f1', RH, 'r13feh', 'comp', ['b4800424.jpg', 'b5060927.jpg', 'b250556.jpg', 'b2776791.jpg'], 'Schornsteinfeger und <em>Energie-Effizienz-Experte.</em>',
   'Vom Kehren bis zum Blower-Door-Test: Gerd Rechtien ist Schornsteinfegermeister, Heizungsbaumeister und Gebäudeenergieberater in einer Person.', 'Nortrup und Umgebung', I('rechtien', 8, 0), 76, slugbase='schornsteinfeger-rechtien-nortrup', bot='Funke')
mk('kohlbrecher', 'Björn Kohlbrecher', 'Wallenhorst', 'Zu den Maschwiesen 4', '49134', '05407 8986633', '+4954078986633', 'info@kohlbrecher-schornsteinfeger.de', 'kohlbrecher-schornsteinfeger.de',
   ['Meister|Schornsteinfegermeister', 'Energieberater|für Gebäude, HWK', 'TÜV|Brandschutzbeauftragter'],
   ['Schornsteinfegerarbeiten', 'Energieausweis', 'Rauchwarnmelder', 'Gashausschau', 'Holzfeuchtemessung'], '#7A9A01', '#2f3336', '#f5f6f0', NOTO, 'r18rec', 'splitl',
   ['b3378773.jpg', '2792895.jpg', '315874.jpg', 'b4572410.jpg'], 'Meister Kohlbrecher. <em>Schornsteinfeger und Energieberater.</em>',
   'Ihr Ansprechpartner in Wallenhorst für Sicherheit, Umwelt und Energie. Auch als Brandschutzbeauftragter (TÜV) für Sie da.', 'Wallenhorst und Umgebung', I('kohlbrecher', 0, 0), 84, slugbase='schornsteinfeger-kohlbrecher-wallenhorst', firma='Schornsteinfeger & Energieberater Björn Kohlbrecher', bot='Zylinder')
mk('tepe', 'Oliver Tepe', 'Vechta', 'Meinard-Fortmann-Straße 44', '49377', '04441 9738930', '+4944419738930', 'info@schornsteinfeger-tepe.de', 'schornsteinfeger-tepe.de',
   ['Meister|Schornsteinfegermeister', 'Energieberater|für Gebäude, HWK', 'Vechta|und Umgebung'],
   ['Schornsteinfegerarbeiten', 'Energieberatung', 'Energieausweis', 'Brandschutz', 'Lüftungsanlagen', 'Rauchwarnmelder', 'Gashausschau', 'Holzfeuchtemessung', 'Feuerungstechnische Beratung', 'Bauberatung'],
   '#b3261e', '#141414', '#f3f3f3', ROB, 'r10liekam', 'slides', ['b7405160.jpg', 'b4515924.jpg', 'b78445.jpg', 'b1784455.jpg'], 'Ihr Schornsteinfeger <em>in Vechta.</em>',
   'Oliver Tepe ist Schornsteinfegermeister und Gebäudeenergieberater HWK. Für Brandschutz, Energieberatung und alles rund um Ihre Feuerstätte.', 'Vechta und Umgebung', (R19 + 'tepe/textlogo.png', 0), 56,
   own=R19 + 'tepe/portrait.jpg', own_cap='Oliver Tepe', slugbase='schornsteinfeger-tepe-vechta', bot='Besen')
mk('gall', 'Siegfried Gall', 'Diepholz', 'Lohneufer 8', '49356', '05441 9925209', '+4954419925209', 'info@siegfried-gall.de', 'siegfried-gall.de',
   ['Meister|Schornsteinfegermeister und Heizungsbaumeister', 'Energieberater|für Gebäude', 'iSfP|Sanierungsfahrplan'],
   ['Schornsteinfegerarbeiten', 'Energieausweis', 'Sanierungsfahrplan (iSfP)', 'Energieberatung', 'Gasleitungsprüfung', 'Hydraulischer Abgleich', 'Kaminofen- und Ofenrohrreinigung', 'Rauchwarnmelder'],
   '#D67800', '#2b2420', '#faf5ee', GUD, 'r18now', 'comp', ['b2776791.jpg', 'b949081.jpg', 'b7349347.jpg', 'b3591632.jpg'], 'Schornsteinfeger, Heizungsbaumeister, <em>Energieberater.</em>',
   'Siegfried Gall begleitet Sie vom Energieausweis über den Sanierungsfahrplan bis zum hydraulischen Abgleich.', 'Diepholz und Umgebung', (R19 + 'gall/textlogo.png', 0), 56, slugbase='schornsteinfeger-gall-diepholz', bot='Glut')
mk('telkmann', 'Thomas Telkmann', 'Lingen', 'Am Mühlenbach 8', '49809', '0591 61077129', '+4959161077129', 'thomas.telkmann@web.de', 'schornsteinfeger-telkmann.de',
   ['Meister|Schornsteinfegermeister und Heizungsbaumeister', 'Brandschutz|Beauftragter und Techniker (ZIV)', 'DIN 14676|Fachkraft Rauchwarnmelder'],
   ['Schornsteinfegerarbeiten', 'Energieberatung', 'Energieausweis', 'Brandschutz', 'Lüftungsanlagen', 'Rauchwarnmelder', 'Gashausschau', 'Holzfeuchtemessung', 'Holz und Pelletofen'],
   '#1f4e79', '#16212e', '#f1f4f7', RAL, 'r18ant', 'split', ['2792895.jpg', 'b4572410.jpg', 'b3792951.jpg', 'b1784455.jpg'], 'Schornsteinfeger und <em>Brandschutz-Fachmann.</em>',
   'In der Grafschaft Bentheim und im Emsland Ihr Ansprechpartner für Brandschutz, Umweltschutz, Energieeinsparung und neutrale Beratung.', 'Grafschaft Bentheim und Emsland', I('telkmann', 4, 0), 84, slugbase='schornsteinfeger-telkmann-lingen', bot='Leiter')
mk('huckriede', 'Bernd Huckriede', 'Ibbenbüren', 'Wilhelm-Busch-Straße 72', '49479', '05451 84875', '+49545184875', 'info@schornsteinfeger-tecklenburgerland.de', 'schornsteinfeger-tecklenburgerland.de',
   ['Meister|Schornsteinfegermeister', 'Energieberater|für Gebäude, HWK', 'Schimmel|Schimmelpilzberater'],
   ['Schornsteinfegerarbeiten', 'Energieberatung', 'Energieausweis', 'Rauchwarnmelder', 'Gashausschau', 'Holzfeuchtemessung', 'Feuerungstechnische Beratung'],
   '#3f7d20', '#20261c', '#f3f6ef', LATO, 'r10vagts', 'splitl', ['b2853047.jpg', 'b1784455.jpg', 'b250558.jpg', 'b3591632.jpg'], 'Ihr Schornsteinfeger im <em>Tecklenburger Land.</em>',
   'Bernd Huckriede ist Schornsteinfegermeister, Gebäudeenergieberater HWK und Schimmelpilzberater.', 'Tecklenburger Land', (R19 + 'huckriede/textlogo.png', 0), 56, slugbase='schornsteinfeger-huckriede-ibbenbueren', bot='Glück')
mk('brockmann', 'Frank Brockmann', 'Bad Iburg', 'Mühlenstraße 56', '49186', '05403 795363', '+495403795363', '', 'schornsteinfeger-brockmann.de',
   ['Meister|Schornsteinfegermeister', 'Energieberater|für Gebäude, HWK', 'Bad Iburg|und Umgebung'],
   ['Schornsteinfegerarbeiten', 'Energieberatung', 'Energieausweis', 'Rauchwarnmelder', 'Feuerungstechnische Beratung'], '#005A9F', '#0f2a44', '#f0f5fa', NOTO, 'r18rec', 'split',
   ['b4800424.jpg', '8193787.jpg', 'b227291.jpg', 'b3378773.jpg'], 'Sicherheits-, Umwelt- und <em>Energieexperte.</em>',
   'Frank Brockmann ist Schornsteinfegermeister und Gebäudeenergieberater HWK in Bad Iburg.', 'Bad Iburg und Umgebung', (R19 + 'brockmann/textlogo.png', 0), 56,
   own=R19 + 'brockmann/p2x.jpg', own_cap='Frank Brockmann', slugbase='schornsteinfeger-brockmann-bad-iburg', mobil='0160 7425866', bot='Kamin')
mk('peters', 'Torsten Peters', 'Bad Iburg', 'Hohenbrink 33a', '49186', '05403 795995', '+495403795995', '', 'peters-schornsteinfeger.de',
   ['Meister|Schornsteinfegermeister', 'Energieberater|für Gebäude', 'Bad Iburg|und Umgebung'],
   ['Schornsteinfegerarbeiten', 'Energieberatung', 'Energieausweis', 'Rauchwarnmelder', 'Feuerungstechnische Beratung'], '#0B6FB8', '#102536', '#eef4f9', RH, 'r13feh', 'slides',
   ['b3378773.jpg', 'b9877220.jpg', 'b2939560.jpg', 'b7405160.jpg'], 'Ihr Schornsteinfeger <em>in Bad Iburg.</em>',
   'Torsten Peters ist Schornsteinfegermeister und Gebäudeenergieberater. Ihr Sicherheits-, Umwelt- und Energieexperte.', 'Bad Iburg und Umgebung', (R19 + 'peters/textlogo.png', 0), 56,
   own=R19 + 'peters/p2x.jpg', own_cap='Torsten Peters', slugbase='schornsteinfeger-peters-bad-iburg', mobil='0160 90601322', bot='Schlot')
