"""Runde 14 · Teil C: Simon, Loheide + Kraft, Carsten Ludwig, Napierski, Witte."""
from common import *
SITES = {}

# ───────────── 11. Fahrschule Simon, Bissendorf-Schledehausen · Venne ─────────────
def b_simon(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 60%', quick=['auto', 'moto', 'roller', 'anh'],
        ey='Fahrschule Simon · Schledehausen &amp; Venne',
        h1='Ihr Führerschein <em>vor der Haustür.</em>',
        sub='Seit Beginn in Bissendorf-Schledehausen zu Hause, dazu eine Filiale in Venne: damit Ihre Wege zu uns kurz bleiben. Auto, Anhänger, Motorrad und Roller, persönlich ausgebildet von Jörn Simon.',
        badge=('5,0 ★', 'bei Google')))
        + marquee(['Klasse B', 'BF17', 'BE · B96', 'B196', 'A · A2 · A1', 'AM', 'Mofa'], 'sm')
        + orte('filialen', 'Zwei Filialen', 'Kurze Wege, <em>feste Abende.</em>', 'Unterricht jeweils 19:00 bis 20:30 Uhr. Geöffnet ist in der Regel kurz vorher, Zeit genug zur Anmeldung.', [
            ('Schledehausen', 'Am Langenkamp 2, 49143 Bissendorf', 'Mo &amp; Mi 19:00'), ('Venne', 'Hauptstraße 28, 49179 Ostercappeln', 'Di &amp; Do 19:00')])
        + story('team', 'Das Team', 'Ein Fahrlehrer, <em>der alle Klassen kann.</em>', [
            'Jörn Simon bildet die Klassen B, BE, AM, A1, A2, A und Mofa aus und ist verantwortlicher Leiter der Führerscheinausbildung. Sie lernen also vom ersten Roller bis zum großen Motorrad bei demselben Menschen.',
            'Im Büro kümmert sich Christian Lohmeyer um Verwaltung und Organisation, damit Sie sich aufs Fahren konzentrieren können.'],
            'st-buero.jpg', cap='Unser Büro in Schledehausen', tl=[('B · BE', 'Auto &amp; Anhänger mit Ford'), ('A · A2 · A1', 'alle Zweiradklassen'), ('2', 'Filialen')], cls='alt')
        + gallery('fahrzeuge', 'Unsere Schulungsfahrzeuge', 'Ford, KTM, Honda <em>und unser Anhänger.</em>', [
            ('g1.jpg', 'w2', '50% 60%'), ('g2.jpg', '', '50% 55%'), ('g3.jpg', '', '50% 55%'), ('g4.jpg', '', '50% 55%'), ('g5.jpg', '', '50% 55%'), ('g6.jpg', 'w2', '50% 55%')])
        + klassen('klassen', 'Ausbildungsklassen', 'Welche Klasse <em>brauchen Sie?</em>', '', [
            ('B · BF17', 'Auto', 'Ab 17 mit Begleitung, ausgebildet auf Ford.', 'ab 17', 'auto'),
            ('BE · B96', 'Anhänger', 'Für schwere Anhänger und Gespanne.', 'ab 18', 'anh'),
            ('B196', '125er', 'Mit dem Autoführerschein aufs Leichtkraftrad.', 'ab 25', 'roller'),
            ('A · A2 · A1', 'Motorrad', 'Alle Stufen, eine Fahrschule.', 'ab 16', 'moto'),
            ('AM · Mofa', 'Roller', 'Der erste eigene Motor.', 'ab 15', 'roller')], 'dk')
        + ablauf('ablauf', 'Gut zu wissen', 'So starten <em>Sie bei uns.</em>', '', [
            ('Anmelden', 'Montags oder mittwochs in Schledehausen, dienstags oder donnerstags in Venne, kurz vor 19 Uhr.'),
            ('Unterlagen', 'Sehtest, Erste-Hilfe-Kurs und Passbild für den Antrag. Bei BF17 die Begleitperson.'),
            ('Theorie &amp; App', 'Unterricht an zwei Abenden pro Woche, dazu die Lern-App für zu Hause.'),
            ('Fahren', 'Fahrstunden mit Jörn Simon, dann die Prüfung.')])
        + contact(s) + footer(s))

S = SITES['simon'] = site(
    slug='fahrschule-simon-schledehausen', firma='Fahrschule Simon', web='fahrschule-simon-schledehausen.de', fonts='r14sim', du=False,
    title='Fahrschule Simon – Führerschein in Bissendorf-Schledehausen und Venne', desc='Fahrschule Simon in Bissendorf-Schledehausen und Venne: Klassen B, BE, B96, B196, A, A2, A1, AM und Mofa.',
    tel='05402 98070', tel_i='+49540298070', mail='', adresse='Am Langenkamp 2, 49143 Bissendorf', google=('5,0', 3),
    cta='Anmeldung anfragen', nav=[('Filialen', 'filialen'), ('Team', 'team'), ('Fahrzeuge', 'fahrzeuge'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Schledehausen', 'Mo &amp; Mi 19:00 – 20:30'), ('Venne', 'Di &amp; Do 19:00 – 20:30'), ('Jörn Simon', '0174 9666031')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17', 'Anhänger · BE / B96', '125er · B196', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa'],
    form_orte=['Schledehausen', 'Venne'],
    form_h3='Anmeldung anfragen', form_p='Hinterlassen Sie Ihre Nummer, wir rufen zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Sie.</em>', kt_p='Büro 05402 98070, Jörn Simon mobil 0174 9666031.',
    vars='--bg:#f4f7fc;--ink:#0f1d3a;--mute:#53607a;--p:#1f3fa6;--p-ink:#fff;--a:#2fae3d;--a-ink:#fff;--dk:#0f1d3a;--s:#fff;--s2:#e5ecf8;--fh:"Kanit",system-ui,sans-serif;--fb:"Open Sans",system-ui,sans-serif;--r:14px;--r2:22px;--br:10px;--mq-bg:#1f3fa6;--hd-bg:rgba(244,247,252,.95);--hd-ink:#0f1d3a;--logo-h:52px;--ft-bg:#0b1630;--hp-bg:linear-gradient(120deg,#f4f7fc 50%,#dfe8fb)',
    css='''.hp h1,.h2{font-weight:800;font-style:italic;letter-spacing:-.01em;line-height:1.12;padding-top:6px}.hp .ey{margin-bottom:14px}.hp h1 em,.h2 em{color:var(--a)}.dk .h2 em{color:#7fe08a}
.comp{height:470px}.comp figure{border-radius:20px;transform:skewX(-3deg)}.comp figure img{transform:skewX(3deg) scale(1.06)}.ft img{background:#fff;padding:8px;border-radius:8px}''')
S['bot'] = BOT('Sim', 'Ihr Fahrschul-Lotse', 'der Fahrschule Simon', S, ['B', 'BE', 'B96', 'B196', 'A', 'A2', 'A1', 'AM', 'Mofa'],
    {'schnell': 'Unterricht an vier Abenden pro Woche in zwei Filialen. Je öfter Sie kommen, desto schneller.', 'ruhe': 'Bei uns lernen Sie persönlich bei Jörn Simon, vom ersten bis zum letzten Tag.', 'flex': 'Montags und mittwochs in Schledehausen, dienstags und donnerstags in Venne.', 'angst': 'Sprechen Sie es einfach an. Wir starten in Ihrem Tempo.'},
    qa=[('venne|ostercappeln', 'Unsere Filiale in Venne: Hauptstraße 28, Unterricht dienstags und donnerstags ab 19 Uhr.'), ('bf17|17', 'Mit BF17 fahren Sie ab 17 mit Begleitperson. Infos auch unter bf17.de.')],
    tour=[('#filialen', 'Zwei Filialen, feste Abende.'), ('#team', 'Wer Sie ausbildet.'), ('#klassen', 'Alle Klassen.'), ('#kontakt', 'Hier fragen Sie die Anmeldung an.')], du=False)
S['img'] = {'logo.png': ('simon/img/i002.jpg', 0, 'trimalpha'), 'h1.jpg': ('simon/img/i004.jpg', 0), 'h2.jpg': ('simon/img/i008.jpg', 900), 'h3.jpg': ('simon/img/i022.jpg', 0),
    'st-buero.jpg': ('simon/img/i003.jpg', 0),
    'g1.jpg': ('simon/img/i007.jpg', 1400), 'g2.jpg': ('simon/img/i009.jpg', 900), 'g3.jpg': ('simon/img/i014.jpg', 900), 'g4.jpg': ('simon/img/i021.jpg', 0), 'g5.jpg': ('simon/img/i005.jpg', 0), 'g6.jpg': ('simon/img/i029.jpg', 0)}
S['body'] = b_simon

# ───────────── 12. Loheide + Kraft Fahrschulen, Ostercappeln · Osnabrück · Bad Essen · Borgloh · Schledehausen ─────────────
def b_loheide(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h2.jpg', pos='50% 50%', bg='h3.jpg', quick=['auto', 'moto', 'lkw', 'trak'],
        ey='Loheide + Kraft Fahrschulen · seit 2005',
        h1='Sicher fahren. <em>Mit Freude.</em>',
        sub='Aus den Fahrschulen von Christoph Loheide und Wladimir Kraft ist ein Team für alle Klassen geworden. Moderne Flotte, neue Unterrichtsräume und Theorie-Termine, die du online buchst.',
        g1=('6 Standorte', 'rund um Osnabrück'), g2=('AZAV', 'Bildungsgutschein möglich')))
        + svc('vorteile', 'Warum wir', 'Weniger Wege, <em>mehr Zeit zum Fahren.</em>', 'Digitale Anmelde- und Buchungstools sparen Zeit und Wege.', [
            ('Theorie online buchen', 'Im Buchungskalender siehst du die Termine aller Standorte für die nächsten Wochen und buchst deine Stunden.'),
            ('Automatik oder Schaltung', 'Stunden und Prüfung auch auf Automatik, mit Schlüsselzahl 197.'),
            ('Alle Klassen', 'Auto, Motorrad, Lkw und Traktor, plus Berufskraftfahrer-Ausbildung.'),
            ('Bildungsgutschein', 'Nach AZAV zertifiziert: Weiterbildungen können gefördert werden.')])
        + faces('team', 'Unser Team', 'Gesichter, <em>die du kennenlernst.</em>', 'Christoph Loheide, Wladimir Kraft und ihr Team aus Fahrlehrern und Büro.', [
            ('t-wladimir.jpg', 'Wladimir Kraft'), ('t-thomas.jpg', 'Thomas'), ('t-andreas.jpg', 'Andreas'), ('t-fred.jpg', 'Fred'), ('t-tanja.jpg', 'Tanja'),
            ('t-6.jpg', 'Team Loheide + Kraft'), ('t-7.jpg', 'Team Loheide + Kraft'), ('t-8.jpg', 'Team Loheide + Kraft')], 'alt')
        + gallery('halloffame', 'Hall of Fame', 'Bestanden! <em>Herzlichen Glückwunsch.</em>', [
            ('hf1.jpg', '', '50% 30%'), ('hf2.jpg', '', '50% 30%'), ('hf3.jpg', '', '50% 30%'), ('hf4.jpg', '', '50% 30%'), ('hf6.jpg', '', '50% 30%')], 'dk')
        + flotte('fahrzeuge', 'Unsere Fahrzeuge', 'Modern, sportlich, <em>vielseitig.</em>', 'Pkw mit Schalt- und Automatikgetriebe, Motorräder und Lkw.', [
            ('f-auto.jpg', 'Pkw', 'Klasse B · Schalter &amp; Automatik', '50% 55%'), ('f-auto2.jpg', 'Pkw', 'Klasse B / B197', '50% 55%'), ('f-moto.jpg', 'Motorrad', 'Klasse A', '50% 55%'),
            ('f-moto2.jpg', 'Motorrad', 'Klasse A2 / A1', '50% 55%'), ('f-lkw.jpg', 'Lkw', 'Klasse C / CE', '50% 55%'), ('f-anh.jpg', 'Anhänger', 'Klasse BE', '50% 55%')])
        + duo('beruf', 'Für Profis', 'Berufskraftfahrer <em>werden oder bleiben.</em>', '', [
            ('Ausbildung', 'Neu einsteigen', 'd-lkw.jpg', 'Sie möchten beruflich umsatteln? Wir bilden regelmäßig Lkw- und Busfahrer aus, auch mit Bildungsgutschein.', ['Grundqualifikation', 'AZAV-zertifiziert'], 'Beraten lassen'),
            ('Weiterbildung', '95er-Module', 'd-raum.jpg', 'Sie brauchen noch 95er-Weiterbildungen? Termine buchen Sie direkt online.', ['Lkw &amp; Bus', 'Online-Termine'], 'Termin anfragen')], 'alt')
        + orte('standorte', 'Standorte', 'Sechsmal <em>rund um Osnabrück.</em>', 'Anmeldung vor Ort in Ostercappeln: Mo – Fr 8 bis 12 Uhr, Mo – Do auch 15 bis 18 Uhr.', [
            ('Ostercappeln', 'Kronenbrink 4 · Hauptsitz', ''), ('Osnabrück', 'Möserstraße', ''), ('Osnabrück', '', ''), ('Bad Essen', '', ''), ('Borgloh', '', ''), ('Schledehausen', '', '')])
        + reviews(s, ['Tolle Fahrschule! Ein großes Dankeschön an meinen Fahrlehrer Marcus, immer geduldig, freundlich und entspannt. Ich bin viel sicherer geworden.',
                      'Bei mir ging es um die Neuerteilung. Ich wurde zu nichts gedrängt, und alles lief schnell und effizient. Kiki hat einen super Job gemacht.',
                      'Alles lief reibungslos, und die Fahrlehrer sind klasse.',
                      'Sehr gute Fahrschule und ein freundlicher Chef.'], 'dk')
        + contact(s) + footer(s))

S = SITES['loheide'] = site(
    slug='loheide-kraft-fahrschulen', firma='Loheide + Kraft Fahrschulen GmbH', web='loheide-kraft.de', fonts='r14loh',
    title='Loheide + Kraft Fahrschulen – Ostercappeln, Osnabrück, Bad Essen, Borgloh, Schledehausen', desc='Loheide + Kraft Fahrschulen: alle Klassen, Berufskraftfahrer, AZAV-zertifiziert, Theorie-Termine online buchen. Sechs Standorte rund um Osnabrück.',
    tel='05473 911363', tel_i='+495473911363', mail='info@loheide-kraft.de', adresse='Kronenbrink 4, 49179 Ostercappeln', google=('4,9', 18),
    cta='Jetzt anmelden', nav=[('Vorteile', 'vorteile'), ('Team', 'team'), ('Hall of Fame', 'halloffame'), ('Fahrzeuge', 'fahrzeuge'), ('Beruf', 'beruf'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 12:00'), ('Mo – Do', '15:00 – 18:00')],
    form_lbl='Führerschein', form_opts=['Auto · B / B197', 'Anhänger · BE', 'Motorrad · A / A2 / A1', 'Lkw · C / CE', 'Traktor · L / T', 'Berufskraftfahrer / 95er-Weiterbildung', 'Bildungsgutschein'],
    form_orte=['Ostercappeln', 'Osnabrück', 'Bad Essen', 'Borgloh', 'Schledehausen'],
    form_h3='Neuanmeldung', form_p='Jetzt anmelden und schon bald den eigenen Führerschein in den Händen halten.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Bereit <em>für die Straße?</em>', kt_p='Hauptsitz Ostercappeln, Telefon 05473 911363.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--hx-op:.18;--bg:#f5f7fb;--ink:#101a33;--mute:#56627a;--p:#21409a;--p-ink:#fff;--a:#f28c18;--a-ink:#fff;--dk:#101a33;--s:#fff;--s2:#e7ecf6;--fh:"Exo 2",system-ui,sans-serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:12px;--r2:18px;--br:8px;--mq-bg:#21409a;--hd-bg:rgba(245,247,251,.95);--hd-ink:#101a33;--logo-h:46px;--ft-bg:#0b1226',
    css='''.hx h1,.h2{font-weight:800;font-style:italic;letter-spacing:-.01em;line-height:1.08}.hx h1 em,.h2 em{font-style:italic;color:var(--a)}.hx .pic{--hx-ar:1505/812}
.hd.lt:not(.scr) .logo img{background:#fff;padding:6px 10px;border-radius:8px}.ft img{background:#fff;padding:8px 10px;border-radius:8px}
.fc{--fc-ar:3/2}.fc .grid{grid-template-columns:repeat(4,1fr)}@media (max-width:820px){.fc .grid{grid-template-columns:repeat(2,1fr)}}
.gl .grid{grid-template-columns:repeat(5,1fr);grid-auto-rows:300px}.gl .grid figure{border-radius:16px}@media (max-width:820px){.gl .grid{grid-template-columns:repeat(2,1fr)}}''')
S['bot'] = BOT('Lukas', 'dein Loheide-+-Kraft-Lotse', 'Loheide + Kraft', S, ['B', 'B197', 'BE', 'A', 'A2', 'A1', 'C', 'CE', 'L', 'T'],
    {'schnell': 'Theorie-Termine buchst du online, an allen Standorten. So bekommst du schnell deine Stunden zusammen.', 'ruhe': 'Unsere Fahrschüler loben geduldige, entspannte Fahrlehrer.', 'flex': 'Sechs Standorte und ein Online-Buchungskalender für die Theorie.', 'angst': 'Du kannst auch auf Automatik lernen und die Prüfung machen.'},
    qa=[('gutschein|azav|arbeitsamt|jobcenter|förder', 'Wir sind nach AZAV zertifiziert, Ausbildungen können mit Bildungsgutschein gefördert werden.'), ('theorie|termin|buch', 'Theorie-Termine buchst du online im Buchungskalender, für alle Standorte.'), ('karriere|fahrlehrer|job', 'Wir bilden auch Fahrlehrer aus und suchen Verstärkung.')],
    tour=[('#vorteile', 'Was dir Zeit und Wege spart.'), ('#team', 'Unser Team.'), ('#halloffame', 'Unsere frisch Bestandenen.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('loheide/img/i001.png', 0, 'alphacrop'), 'h1.jpg': ('loheide/img/i007.jpg', 0), 'h2.jpg': ('loheide/img/i009.jpg', 0), 'h3.jpg': ('loheide/img/i002.jpg', 0),
    't-wladimir.jpg': ('loheide/img/i022.jpg', 0), 't-thomas.jpg': ('loheide/img/i013.jpg', 0), 't-andreas.jpg': ('loheide/img/i014.jpg', 0), 't-fred.jpg': ('loheide/img/i016.jpg', 0), 't-tanja.jpg': ('loheide/img/i018.jpg', 0),
    't-6.jpg': ('loheide/img/i019.jpg', 0), 't-7.jpg': ('loheide/img/i020.jpg', 0), 't-8.jpg': ('loheide/img/i021.jpg', 0),
    'hf1.jpg': ('loheide/img/i024.jpg', 0), 'hf2.jpg': ('loheide/img/i025.jpg', 0), 'hf3.jpg': ('loheide/img/i026.jpg', 0), 'hf4.jpg': ('loheide/img/i027.jpg', 0), 'hf5.jpg': ('loheide/img/i028.jpg', 700), 'hf6.jpg': ('loheide/img/i029.jpg', 0),
    'f-auto.jpg': ('loheide/img/i012.jpg', 0), 'f-auto2.jpg': ('loheide/img/i009.jpg', 0), 'f-moto.jpg': ('loheide/img/i010.jpg', 0), 'f-moto2.jpg': ('loheide/img/i011.jpg', 0), 'f-lkw.jpg': ('loheide/img/i006.jpg', 0), 'f-anh.jpg': ('loheide/img/i004.jpg', 0, (.25, 0, .85, 1)),
    'd-lkw.jpg': ('loheide/img/i006.jpg', 0), 'd-raum.jpg': ('loheide/img/i002.jpg', 0)}
S['body'] = b_loheide

# ───────────── 13. Fahrschule CL Carsten Ludwig, Bohmte ─────────────
def b_ludwig(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-team.jpg', pos='50% 40%', bg='h-cars.jpg', quick=['auto', 'moto', 'anh'],
        ey='Fahrschule CL · Bohmte',
        h1='Fahren lernen <em>ohne Druck.</em>',
        sub='Carsten Ludwig und Detlev bringen dich in Bohmte entspannt zum Führerschein. Mit Vogel-Simulator, DriversCam-Videosystem und Theorie, die tatsächlich Spaß macht.',
        g1=('4,7 ★', 'bei Google'), g2=('Di &amp; Do', 'Theorie 19:00 – 20:30')))
        + sorgen('stimmen', 'Was Fahrschüler über uns sagen', 'Locker, geduldig, <em>ohne Stress.</em>', 'So beschreiben uns unsere Fahrschüler auf Google, sinngemäß:', [
            ('Was, wenn ich was nicht verstehe?', 'Dann wird es <b>ruhig und klar erklärt</b>. Du kannst jederzeit fragen, ohne dich schlecht zu fühlen.'),
            ('Ist das nicht total stressig?', 'Die Stunden sind <b>nicht stressig oder unter Druck</b>, sondern locker und angenehm. Man fühlt sich sofort wohl.'),
            ('Wer hilft mir bei Problemen?', '<b>Carsten und Detlev</b> sind immer ansprechbar und finden gemeinsam eine Lösung.'),
            ('Ist Theorie nicht öde?', 'Unsere Fahrschüler schreiben: Der Theorieunterricht hat <b>sogar Spaß gemacht</b>.')], 'alt')
        + duo('technik', 'Unsere Extras', 'Mehr sehen, <em>mehr verstehen.</em>', 'Zwei Werkzeuge, die dir das Lernen leichter machen.', [
            ('Vogel-Simulator', 'Der perfekte Begleiter', 'd-sim.jpg', 'Erste Handgriffe, Schalten und Anfahren in Ruhe üben, bevor es in den Verkehr geht.', ['ohne Verkehr', 'ohne Zeitdruck'], 'Mehr erfahren'),
            ('DriversCam', 'Das Fahrschul-Videosystem', 'd-cam.jpg', 'Deine Fahrstunden auf Video: So siehst du hinterher genau, was gut lief und was du noch üben solltest.', ['Video der Fahrstunde', 'auf dem Handy ansehen'], 'Mehr erfahren')])
        + vgrid('video', 'Kurz erklärt', 'So funktioniert <em>DriversCam.</em>', '', [('DriversCam, das Fahrschul-Videosystem', 'mp4', 'v-cam.mp4', 'v-cam.jpg')], 'dk')
        + klassen('klassen', 'Führerscheine', 'Was willst <em>du fahren?</em>', '', [
            ('B · B197', 'Auto', 'B197: Ausbildung auf Schalter und Automatik, Prüfung auf Automatik.', 'ab 17', 'auto'),
            ('BE', 'Anhänger', 'Für schwere Anhänger und Wohnwagen.', 'ab 18', 'anh'),
            ('A', 'Motorrad', 'Zwei Räder, volle Freiheit.', 'ab 16', 'moto')])
        + gallery('einblicke', 'Einblicke', 'Unsere <em>Fahrschule.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 55%')], 'alt')
        + reviews(s, ['Alle sind freundlich, geduldig und entspannt. Die Stunden sind nicht stressig, sondern locker und angenehm. Man fühlt sich sofort wohl.',
                      'Theorie und Praxis waren super, freundlich und nett. Vielen Dank an Herrn Carsten und Herrn Detlev.',
                      'Bei Problemen sind Carsten und Detlev da und finden gemeinsam eine Lösung. Die Atmosphäre war immer angenehm.',
                      'Gute Tipps in den Fahrstunden, und der Theorieunterricht hat sogar Spaß gemacht.'], 'dk')
        + contact(s) + footer(s))

S = SITES['ludwig'] = site(
    slug='fahrschule-cl-bohmte', firma='Fahrschule CL Carsten Ludwig', web='fahrschule.cl', fonts='r14lud',
    title='Fahrschule CL Carsten Ludwig – Führerschein in Bohmte', desc='Fahrschule CL in Bohmte: B, B197, BE und A. Vogel-Simulator, DriversCam-Videosystem, Theorie dienstags und donnerstags.',
    tel='0151 56002121', tel_i='+4915156002121', mail='info@fahrschule.cl', adresse='Bremer Straße 16, 49163 Bohmte', google=('4,7', 30),
    cta='Jetzt anmelden', nav=[('Stimmen', 'stimmen'), ('Technik', 'technik'), ('Klassen', 'klassen'), ('Einblicke', 'einblicke'), ('Kontakt', 'kontakt')],
    hours=[('Anmeldung Di &amp; Do', '18:00 – 19:00'), ('Theorie Di &amp; Do', '19:00 – 20:30'), ('', 'oder nach Vereinbarung')],
    form_lbl='Führerschein', form_opts=['Auto · B / B197', 'Anhänger · BE', 'Motorrad · A'],
    form_h3='Anmeldung', form_p='Trag dich ein, wir melden uns und machen einen Termin mit dir.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Komm vorbei, <em>Di oder Do.</em>', kt_p='Anmeldung dienstags und donnerstags von 18 bis 19 Uhr oder nach Vereinbarung.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#f6f5f3;--ink:#161616;--mute:#5b5956;--p:#d31b23;--p-ink:#fff;--a:#d31b23;--a-ink:#fff;--dk:#161616;--s:#fff;--s2:#ebe8e3;--fh:"Oswald",Impact,sans-serif;--fb:"Lato",system-ui,sans-serif;--r:10px;--r2:16px;--br:6px;--hd-bg:rgba(246,245,243,.95);--hd-ink:#161616;--logo-h:44px;--ft-bg:#0e0e0e;--hx-op:.2;--hx-bg:#f6f5f3',
    css='''.hx h1,.h2{font-weight:700;text-transform:uppercase;letter-spacing:.005em;line-height:1.05}.hx h1 em,.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#ff5b62}
.hx .pic{--hx-ar:4/3;transform:rotate(-1.2deg);border:10px solid #fff}.ft img{background:#fff;padding:8px;border-radius:8px}''')
S['bot'] = BOT('Lu', 'dein CL-Lotse', 'der Fahrschule CL', S, ['B', 'B197', 'BE', 'A'],
    {'schnell': 'Theorie dienstags und donnerstags. Mit DriversCam siehst du nach jeder Stunde, woran du arbeiten musst.', 'ruhe': 'Unsere Fahrschüler sagen: nicht stressig, nicht unter Druck, sondern locker und angenehm.', 'flex': 'Anmeldung dienstags und donnerstags oder nach Vereinbarung.', 'angst': 'Starte am Vogel-Simulator, ganz ohne Verkehr.'},
    qa=[('drivers|cam|video', 'Mit DriversCam werden deine Fahrstunden aufgezeichnet, so kannst du sie dir hinterher ansehen.'), ('simulator|vogel', 'Am Vogel-Simulator übst du die ersten Schritte ohne Verkehr.'), ('english|englisch', 'Unsere Seite gibt es auch auf Englisch, sprich uns einfach an.')],
    tour=[('#stimmen', 'Was unsere Fahrschüler sagen.'), ('#technik', 'Simulator und DriversCam.'), ('#klassen', 'Unsere Klassen.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('ludwig/img/i025.png', 0, 'alphacrop'), 'h-team.jpg': ('ludwig/img/i014.jpg', 0), 'h-cars.jpg': ('ludwig/img/i021.jpg', 0),
    'd-sim.jpg': ('ludwig/img/i011.jpg', 0), 'd-cam.jpg': ('ludwig/img/i009.jpg', 0), 'v-cam.mp4': ('ludwig/vid/v.mp4', 0), 'v-cam.jpg': ('ludwig/vid/poster.jpg', 0),
    'g1.jpg': ('ludwig/img/i023.jpg', 0), 'g2.jpg': ('ludwig/img/i006.jpg', 0), 'g3.jpg': ('ludwig/img/i018.jpg', 0), 'g4.jpg': ('ludwig/img/i015.jpg', 0), 'g5.jpg': ('ludwig/img/i020.jpg', 0), 'g6.jpg': ('ludwig/img/i022.jpg', 0)}
S['body'] = b_ludwig

# ───────────── 14. Fahrschule Napierski, Löningen · Lastrup · Essen (Oldb.) ─────────────
def b_napierski(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-team.jpg', pos='50% 45%', wide=True, quick=['auto', 'moto', 'roller', 'anh', 'lkw', 'trak'],
        ey='Fahrschule Napierski · Löningen · Lastrup · Essen',
        h1='Dein Weg zum Führerschein <em>beginnt jetzt.</em>',
        sub='Sicher, kompetent und mit einem guten Gefühl auf die Straße: in nahezu allen Klassen außer Bus, mit einem Team, das sich die Zeit nimmt, die du brauchst.',
        g1=('3 Standorte', 'Löningen, Lastrup, Essen'), g2=('Alle Klassen', 'außer Bus')))
        + svc('warum', 'Willkommen bei uns', 'Du stehst <em>im Mittelpunkt.</em>', 'Bei uns geht es nicht nur ums Bestehen. Du sollst dich die ganze Ausbildung über sicher und wohl fühlen.', [
            ('Erfahrung, die weiterbringt', 'Gut ausgebildete Fahrlehrerinnen und Fahrlehrer, die wissen: Jeder lernt anders.'),
            ('Dein Lerntempo', 'Deine Bedürfnisse und dein Tempo bestimmen die Ausbildung.'),
            ('Modern unterwegs', 'Fahrzeuge mit aktueller Sicherheitstechnik und modernem Komfort.'),
            ('Nicht an einen Ort gebunden', 'Kurs oder einzelne Tage einfach am anderen Theorie-Standort besuchen.')])
        + team('team', 'Unser Team', 'Unser erfahrenes Team <em>freut sich auf dich.</em>', '', [
            ('t-aaron.jpg', 'Aaron Napierski', 'Geschäftsführer'), ('t-klaus.jpg', 'Klaus Napierski', 'Geschäftsführer'), ('t-beate.jpg', 'Beate Napierski', 'Team'), ('t-jonas.jpg', 'Jonas Tiemann', 'Team'),
            ('t-annalena.jpg', 'Anna-Lena Mehmann', 'Team'), ('t-walter.jpg', 'Walter Hartke', 'Team'), ('t-juergen.jpg', 'Jürgen Bernert', 'Team'), ('t-josephine.jpg', 'Josephine Brockhage', 'Team'), ('t-hermann.jpg', 'Hermann Albers', 'Team')], 'alt')
        + orte('standorte', 'Standorte &amp; Öffnungszeiten', 'Komm vorbei, <em>wir sind für dich da.</em>', 'Theorieunterricht in Löningen und Lastrup monatlich abwechselnd in Kursform. Telefonische Anmeldung für alle drei Fahrschulen: Mo – Do 9 bis 18 Uhr, Fr 9 bis 13 Uhr.', [
            ('Löningen', 'Poststraße 12 · Hauptstandort', 'Kurs 07.12. – 16.12.2026'), ('Lastrup', 'Theorie im Wechsel mit Löningen', ''), ('Essen (Oldb.)', 'Fahrschule vor Ort', '')], 'dk')
        + klassen('klassen', 'Führerscheine', 'Fast alles, <em>außer Bus.</em>', '', [
            ('B · BE', 'Auto &amp; Anhänger', 'Der Klassiker, auch mit 17 begleitet.', 'ab 17', 'auto'),
            ('A · A2 · A1', 'Motorrad', 'Stufenweise oder direkt.', 'ab 16', 'moto'),
            ('AM · Mofa', 'Roller', 'Ab 15 unterwegs.', 'ab 15', 'roller'),
            ('C1 · C · CE', 'Lkw', 'Für den Beruf.', 'ab 18', 'lkw'),
            ('L · T', 'Traktor', 'Für die Landwirtschaft.', 'ab 16', 'trak')])
        + gallery('vorort', 'Vor Ort', 'Unsere Fahrschulen <em>und Fahrzeuge.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 40%'), ('g3.jpg', '', '50% 40%')], 'alt')
        + contact(s) + footer(s))

S = SITES['napierski'] = site(
    slug='fahrschule-napierski-loeningen', firma='Fahrschule Napierski GmbH', web='fahrschule-napierski.de', fonts='r14nap',
    title='Fahrschule Napierski – Löningen, Lastrup & Essen', desc='Fahrschule Napierski GmbH in Löningen, Lastrup und Essen (Oldb.): Ausbildung in nahezu allen Klassen außer Bus.',
    tel='05432 58014', tel_i='+49543258014', mail='info@fahrschule-napierski.de', adresse='Poststraße 12, 49624 Löningen', google=None,
    cta='Jetzt anmelden', tbar='Nächster Theoriekurs in Löningen: <b>07.12. – 16.12.2026</b> · <a href="#kontakt">Platz sichern</a>',
    nav=[('Warum wir', 'warum'), ('Team', 'team'), ('Standorte', 'standorte'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '09:00 – 18:00 (Telefon)'), ('Fr', '09:00 – 13:00 (Telefon)'), ('Löningen Mo &amp; Mi', '09:00 – 12:00 Anmeldung')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17', 'Anhänger · BE', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', 'Lkw · C1 / C / CE', 'Traktor · L / T', 'Theoriekurs 07.12.–16.12.'],
    form_orte=['Löningen', 'Lastrup', 'Essen (Oldb.)'],
    form_h3='Persönlicher Kostenvoranschlag', form_p='Sag uns, was du vorhast. Wir melden uns mit deinem persönlichen Angebot.', form_btn='Anfrage senden',
    kt_ey='Kontakt', kt_h2='Du hast noch Fragen? <em>Wir helfen dir.</em>', kt_p='Telefon, WhatsApp oder E-Mail, wie es dir am liebsten ist.',
    vars='--bg:#f4f7fd;--ink:#0b1630;--mute:#55607a;--p:#1846c8;--p-ink:#fff;--a:#1846c8;--a-ink:#fff;--dk:#0b1630;--s:#fff;--s2:#e3eafb;--fh:"Red Hat Display",system-ui,sans-serif;--fb:"Open Sans",system-ui,sans-serif;--r:16px;--r2:24px;--br:999px;--mq-bg:#1846c8;--hd-bg:rgba(244,247,253,.95);--hd-ink:#0b1630;--logo-h:40px;--ft-bg:#081129;--tbar-bg:#0b1630;--hxw-ar:1600/755;--hx-bg:linear-gradient(180deg,#f4f7fd,#dfe7fb)',
    css='''.hx h1,.h2{font-weight:900;letter-spacing:-.02em;line-height:1.04}.hx h1 em{font-style:normal;color:var(--p)}.hx .pic{--hx-r:40px 40px 0 40px}.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#8fb0ff}
.hd .logo img{filter:brightness(0)}.ft img{filter:brightness(0) invert(1)}.tm .grid{grid-template-columns:repeat(5,1fr)}.tm figure img{aspect-ratio:4/5;object-position:50% 25%;background:#fff}@media (max-width:900px){.tm .grid{grid-template-columns:repeat(2,1fr)}}''')
S['bot'] = BOT('Nele', 'deine Napierski-Lotsin', 'der Fahrschule Napierski', S, ['B', 'BE', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE', 'L', 'T'],
    {'schnell': 'Theorie läuft in Kursform. Der nächste Kurs in Löningen startet am 07.12.2026.', 'ruhe': 'Wir nehmen uns die Zeit, die du brauchst. Jeder Mensch lernt anders.', 'flex': 'Du bist nicht an einen Standort gebunden und kannst Kurstage auch am anderen Ort besuchen.', 'angst': 'Wir möchten, dass du dich die ganze Ausbildung über sicher und wohl fühlst.'},
    qa=[('kurs|theorie|termin', 'Theorie läuft monatlich abwechselnd in Löningen und Lastrup in Kursform. Nächster Kurs in Löningen: 07.12. bis 16.12.2026.'), ('kost|preis|angebot', 'Über das Formular bekommst du einen persönlichen Kostenvoranschlag.'), ('bus', 'Bus bilden wir nicht aus, sonst nahezu alle Klassen.')],
    tour=[('#warum', 'Warum Napierski.'), ('#team', 'Unser Team.'), ('#standorte', 'Drei Standorte.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('napierski/img/i001.webp', 0, 'alphacrop'), 'h-team.jpg': ('napierski/img/i004.webp', 0), 'h-moto.jpg': ('napierski/img/i006.webp', 0),
    't-aaron.jpg': ('napierski/img/i010.webp', 0), 't-klaus.jpg': ('napierski/img/i017.webp', 0), 't-beate.jpg': ('napierski/img/i012.webp', 0), 't-jonas.jpg': ('napierski/img/i014.webp', 0),
    't-annalena.jpg': ('napierski/img/i011.webp', 0), 't-walter.jpg': ('napierski/img/i018.webp', 0), 't-juergen.jpg': ('napierski/img/i016.webp', 0), 't-josephine.jpg': ('napierski/img/i015.webp', 0), 't-hermann.jpg': ('napierski/img/i013.webp', 0),
    'g1.jpg': ('napierski/img/i005.webp', 0), 'g2.jpg': ('napierski/img/i009.webp', 0), 'g3.jpg': ('napierski/img/i008.webp', 0), 'g4.jpg': ('napierski/img/i007.webp', 0), 'g5.jpg': ('napierski/img/i006.webp', 0)}
S['body'] = b_napierski

# ───────────── 15. Fahrschule Burkard Witte & Sohn, Cloppenburg · Cappeln ─────────────
def b_witte(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 50%', quick=['auto', 'moto', 'roller', 'lkw', 'trak'],
        ey='Burkard Witte &amp; Sohn · Cloppenburg &amp; Cappeln',
        h1='Familiär. Modern. <em>Alle Klassen.</em>',
        sub='Eine Fahrschule, in der schon Eltern und Kinder ihren Führerschein gemacht haben. Wir begleiten dich Schritt für Schritt, mit neuen Fahrzeugen, flexiblen Stundenplänen und einem Unterrichtsraum, den man nicht vergisst.',
        badge=('4,7 ★', '66 Google-Bewertungen')))
        + marquee(['Auto', 'Motorrad', 'Lkw', 'Bus', 'Traktor', 'Mofa', 'Erste-Hilfe-Kurs', 'Seminare'], 'wm')
        + story('raum', 'Unser Unterrichtsraum', 'Theorie, <em>die man nicht vergisst.</em>', [
            'Wer bei uns Theorie macht, sitzt mitten in einem Wandbild aus Verkehrszeichen und Fahrschulautos. Moderne Unterrichtsmethoden, flexible Stundenpläne und faire Preise machen den Rest.',
            'Ob du als Fahranfänger startest, dein Wissen auffrischen oder eine neue Klasse erwerben willst: Bei uns bist du richtig.'],
            'st-raum.jpg', cap='Theorieraum der Fahrschule Witte', tl=[('Cloppenburg', 'Eisenbahnweg 1'), ('Cappeln', 'zweiter Standort'), ('Alle Klassen', '&amp; Seminare')], cls='alt')
        + flotte('fahrzeuge', 'Moderne Fahrzeuge', 'Neu, gepflegt <em>und sauber.</em>', 'Alle unsere Fahrzeuge, egal ob Auto, Motorrad oder Lkw, sind neu und modern ausgestattet.', [
            ('f1.jpg', 'Pkw', 'Klasse B', '50% 60%'), ('f2.jpg', 'Pkw', 'Klasse B', '50% 60%'), ('f3.jpg', 'Pkw', 'Klasse B', '50% 55%'), ('f4.jpg', 'Pkw', 'Klasse B / BE', '50% 55%'), ('f5.jpg', 'Flotte', 'Cloppenburg', '50% 55%')], 'dk')
        + klassen('klassen', 'Alle Fahrschulklassen', 'Von zwei Rädern <em>bis zum Bus.</em>', '', [
            ('B · BF17 · B197', 'Autoführerschein', 'Die Klasse B beinhaltet AM und L.', 'ab 17', 'auto'),
            ('A · A2 · A1', 'Motorrad', 'Stufenweise mit AM, A1 und A2.', 'ab 16', 'moto'),
            ('AM · Mofa', 'Moped &amp; Mofa', 'Der Einstieg auf zwei Rädern.', 'ab 15', 'roller'),
            ('C · CE · C1', 'Lkw', 'Für Beruf und Landwirtschaft.', 'ab 18', 'lkw'),
            ('D · DE · D1', 'Bus', 'Personenbeförderung.', 'ab 21', 'lkw'),
            ('L · T', 'Traktor', 'Für Hof und Feld.', 'ab 16', 'trak')])
        + promo('erstehilfe', 'p-eh.jpg', 'Gleich mit erledigen', 'Erste-Hilfe-Kurs <em>bei uns.</em>', 'Für den Führerscheinantrag brauchst du einen Erste-Hilfe-Kurs. Den bieten wir dir direkt an, damit du keine Extra-Wege hast.', ['Pflicht für den Antrag', 'Direkt über uns buchbar'], 'Kurs anfragen', 'alt')
        + reviews(s, ['Ein familiengeführter Betrieb mit Herz und Fachwissen. Ich habe dort meinen Führerschein gemacht, und auch meine Kinder.',
                      'Egal wie nervös man am Anfang ist, die ruhige und herzliche Art beruhigt sofort. Alles wird verständlich erklärt, auch mehrmals.',
                      'Ich wurde herzlich empfangen und habe mich sofort wohlgefühlt. Ohne euch hätte ich die Prüfung nicht so schnell geschafft.',
                      'Die Fahrzeuge sind immer modern, gepflegt und sauber. Die Fahrlehrer gehen auf jeden Schüler einzeln ein.'], 'dk')
        + contact(s) + footer(s))

S = SITES['witte'] = site(
    slug='fahrschule-witte-cloppenburg', firma='Fahrschule Burkard Witte & Sohn', web='fahrschule-bwitte.de', fonts='r14wit',
    title='Fahrschule Burkard Witte & Sohn – alle Klassen in Cloppenburg & Cappeln', desc='Fahrschule Burkard Witte & Sohn in Cloppenburg und Cappeln: alle Führerscheinklassen, Seminare, Erste-Hilfe-Kurs, moderne Fahrzeuge.',
    tel='04471 3408', tel_i='+4944713408', mail='info@fahrschule-bwitte.de', adresse='Eisenbahnweg 1, 49661 Cloppenburg', google=('4,7', 66),
    cta='Online anmelden', nav=[('Theorieraum', 'raum'), ('Fahrzeuge', 'fahrzeuge'), ('Klassen', 'klassen'), ('Erste Hilfe', 'erstehilfe'), ('Kontakt', 'kontakt')],
    hours=[('Telefon', '04471 3408'), ('Mobil', '0172 4368211')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17 / B197', 'Motorrad · A / A2 / A1', 'Moped · AM / Mofa', 'Lkw · C / CE / C1', 'Bus · D / DE / D1', 'Traktor · L / T', 'Erste-Hilfe-Kurs', 'Seminar'],
    form_orte=['Cloppenburg', 'Cappeln'],
    form_h3='Online-Anmeldung', form_p='Wir melden uns bei dir und besprechen den Start.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Deine erste <em>Anlaufstelle.</em>', kt_p='Ruf uns gern direkt an oder schreib uns eine E-Mail.',
    rv_h2='Was ehemalige Fahrschüler <em>über uns sagen.</em>',
    vars='--bg:#faf8f4;--ink:#1a1a1a;--mute:#5e5a54;--p:#284b59;--p-ink:#fff;--a:#284b59;--a-ink:#fff;--dk:#1a1a1a;--s:#fff;--s2:#efeae1;--fh:"Gupter",Georgia,serif;--fb:"Signika",system-ui,sans-serif;--r:14px;--r2:22px;--br:8px;--mq-bg:#1a1a1a;--mq-ink:#fff;--hd-bg:rgba(250,248,244,.95);--hd-ink:#1a1a1a;--logo-h:48px;--ft-bg:#111',
    css='''.hp h1,.h2{font-weight:700;line-height:1.08}.hp h1 em,.h2 em{color:#284b59}.dk .h2 em{color:#7fb2c6}.comp{height:480px}
.st figure img{aspect-ratio:4/3}.ft img{background:#fff;padding:8px 10px;border-radius:6px}.mq span{font-family:var(--fh);font-style:italic}''')
S['bot'] = BOT('Willi', 'dein Witte-Lotse', 'der Fahrschule Witte', S, ['B', 'B197', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE', 'D', 'L', 'T'],
    {'schnell': 'Flexible Stundenpläne helfen dir, zügig voranzukommen.', 'ruhe': 'Unsere Fahrschüler schreiben: Egal wie nervös man ist, die ruhige Art beruhigt sofort.', 'flex': 'Zwei Standorte, Cloppenburg und Cappeln, und flexible Stundenpläne.', 'angst': 'Alles wird verständlich erklärt, wenn nötig auch mehrmals.'},
    qa=[('erste hilfe', 'Den Erste-Hilfe-Kurs kannst du direkt bei uns machen.'), ('bus|lkw', 'Wir bilden alle Klassen aus, auch Lkw und Bus.')],
    tour=[('#raum', 'Unser besonderer Theorieraum.'), ('#fahrzeuge', 'Unsere Fahrzeuge.'), ('#klassen', 'Alle Klassen.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('witte/img/i008.png', 0, 'trimalpha'), 'h1.jpg': ('witte/img/i014.jpg', 0), 'h2.jpg': ('witte/img/i027.jpg', 0), 'h3.jpg': ('witte/img/i030.jpg', 0),
    'st-raum.jpg': ('witte/img/i015.jpg', 0), 'p-eh.jpg': ('witte/img/i020.jpg', 0),
    'f1.jpg': ('witte/img/i028.jpg', 0), 'f2.jpg': ('witte/img/i032.jpg', 0), 'f3.jpg': ('witte/img/i029.jpg', 0), 'f4.jpg': ('witte/img/i033.jpg', 0), 'f5.jpg': ('witte/img/i026.jpg', 0)}
S['body'] = b_witte
