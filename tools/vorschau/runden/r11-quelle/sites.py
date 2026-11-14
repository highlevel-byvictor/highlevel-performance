"""Runde 11 – 10 Fitness-/Gesundheitsbetriebe rund um Werlte. Nur echtes Material und belegte Fakten der Originalseiten."""
from lib import *
SITES = {}

# ───────────────────────── 1. Werlter Fitness Studio & Physiotherapie ─────────────────────────
def b_werlter(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h-studio.jpg', 'h-cycling.jpg', 'h-kurs.jpg'], big='1987',
        ey='Fitness & Physiotherapie · Werlte · seit 1987',
        h1='Training mit <em>Therapie&shy;wissen.</em>',
        sub='Über 1000 m², ein Team aus Trainern und Physiotherapeuten und ein familiäres Studio: Hier trainieren Sie mit Plan – und wenn es zwickt, ist die Physio direkt nebenan.',
        pos={'h-studio.jpg': '50% 60%'},
        ubar=[('Kostenloses Probetraining', 'Termin vereinbaren, Studio kennenlernen'), ('Auch ohne Vertrag', 'Von der Tageskarte bis zum Abo'), ('Physio ohne Rezept', 'Erstkontakt als Heilpraktiker für Physiotherapie')]))
        + marquee(['Zumba', 'Bauch-Beine-Po', 'Pilates', 'Rückenfit', 'Indoor Cycling', 'Fit im Alter', 'Funktionstraining', 'Rundum Fit', 'E-Gym', 'Sauna'])
        + tabs('leistungen', 'Von Therapie bis Training', 'Alles unter <em>einem Dach.</em>', 'Training, Behandlung und Erholung greifen bei uns ineinander – so kommen Sie schneller ans Ziel und bleiben dran.', [
            ('Physiotherapie', 'physio.jpg', 'Als Heilpraktiker für Physiotherapie dürfen wir Sie auch ohne ärztliche Verordnung untersuchen und behandeln – bei Beschwerden, nach Verletzungen und bei chronischen Leiden.', ['Krankengymnastik', 'Manuelle Therapie', 'Lymphdrainage', 'Sportphysiotherapie', 'Kinesiotape', 'Massage']),
            ('Leistungsdiagnostik', 'diagnostik.jpg', 'Wissen statt raten: Mit der Leistungsdiagnostik per Aeroman finden wir Ihren optimalen Trainingsbereich – für Ausdauer, Lauftraining und Abnehmen.', ['Aeroman', 'Lauftraining', 'Athletiktraining']),
            ('E-Gym', 'egym.jpg', 'Der elektronische Gerätezirkel stellt sich automatisch auf Sie ein und zeigt Ihnen auf dem Bildschirm, wie Sie optimal trainieren.', ['Automatische Einstellung', 'Für Einsteiger ideal']),
            ('Sauna', 'sauna.jpg', 'Nach dem Training einfach abschalten: Die Sauna gehört zu Ihrem Studio dazu.', ['Entspannung', 'Regeneration']),
            ('Solarium', 'solarium.jpg', 'Ein bisschen Sonne für zwischendurch – direkt im Studio.', []),
            ('Firmenfitness', 'gebaeude.jpg', 'Individuelle Firmenfitness-Programme für Betriebe aus Werlte und Umgebung. Dazu von Krankenkassen geförderte Präventionskurse.', ['Firmenprogramme', 'Präventionskurse'])])
        + scroller('kurse', 'Neue Trends und Altbewährtes', 'Kurse, die <em>Spaß</em> machen.', 'Mit Musik, in der Gruppe, für jedes Level – vom Indoor Cycling bis zum Rückenkurs.', [
            ('Indoor Cycling', 'k-cycling.jpg', 'Ausdauer mit Licht und Musik – Herz-Kreislauf-Training, das richtig Laune macht.', '50% 50%'),
            ('Bauch-Beine-Po', 'k-bbp.jpg', 'Kraftausdauer mit aktueller Musik: Straffung und Kräftigung von Bauch, Beinen und Po.', '50% 40%'),
            ('Rückenfit', 'k-ruecken.jpg', 'Gezielt die Rumpfmuskulatur stärken – für einen Rücken, der den Alltag mitmacht.', '30% 50%'),
            ('Pilates', 'k-pilates.jpg', 'Kraft aus der Körpermitte, Haltung und Beweglichkeit.', '50% 50%'),
            ('Funktionstraining', 'k-funktion.jpg', 'Übungen, die Sie im Alltag wirklich brauchen: heben, tragen, stabil bleiben.', '50% 50%'),
            ('Zumba', 'k-zumba.jpg', 'Tanzen, schwitzen, lachen – Fitness, die sich nicht nach Training anfühlt.', '50% 50%')])
        + story('studio', 'Seit über 30 Jahren in Werlte', 'Training … <em>so viel Zeit muss sein.</em>', [
            'Unsere langjährige Bindung zu den Menschen und Sportlern in Werlte und Umgebung macht uns zu einem verlässlichen Partner. Über 300 m² Trainingsfläche mit Cardio- und Kraftgeräten, Kursräume, Physiotherapie und Sauna – an 7 Tagen in der Woche.',
            'Sie bekommen eine individuelle Einweisung, einen persönlichen Trainingsplan und stetige Betreuung. Und das ohne komplizierte Vertragsbedingungen – wenn Sie mögen, auch ganz ohne Vertrag.'],
            'gebaeude.jpg', cap='Ihr Studio am Raddeweg in Werlte', extra='<div class="op"><span>Tageskarte</span><span>10er-Karte</span><span>Monatskarte</span><span>6-Monatsabo</span><span>12-Monatsabo</span><span>24-Monatsabo</span></div><p style="margin-top:14px;font-size:14.5px;color:var(--mute)">Spezielle Angebote für Familien, Partner, Schüler, Azubis und Studenten.</p>')
        + '<section class="sec dk" style="padding-top:0;background:var(--dk)"><div class="w">' + numbers([('1987', 'gegründet in Werlte'), ('1000 m²', 'Gesamtfläche'), ('300 m²', 'Trainingsbereich'), ('7 Tage', 'pro Woche geöffnet')]) + '</div></section>'
        + reviews(s, ['Seit Jahren treuer Kunde: Das Team ist außergewöhnlich freundlich und kompetent, die Geräte modern und top in Schuss.',
                      'Sehr freundliches Personal und ein toller Chef. Alles ist sehr sauber, Duschen und Umkleiden top – und es gibt eine Sauna.',
                      'Kompetentes Personal, moderne Geräte und eine Inhaberin, die selbst Physiotherapeutin ist. Man nimmt sich viel Zeit für jeden.',
                      'Die Mitarbeiter kennen sogar deinen Namen. Dazu Physiotherapie im selben Haus – genau deshalb habe ich mich dafür entschieden.',
                      'Freundlich, kompetent, sauber, tolle Geräte und eine super Atmosphäre. Besser geht es kaum.'], 'alt')
        + steps('So starten Sie', 'In drei Schritten <em>zum Probetraining.</em>', [('Termin vereinbaren', 'Anrufen unter 05951 3233 oder das Formular ausfüllen.'), ('Kostenlos probetrainieren', 'Wir zeigen Ihnen das Studio und trainieren gemeinsam.'), ('Ihr Plan, Ihr Tempo', 'Sie wählen frei – mit oder ohne Vertrag.')])
        + contact(s, 'dk') + footer(s) + pop(dict(img='h-cycling.jpg', ey='Kostenloses Probetraining', h='Einmal reinschnuppern?', p='Lernen Sie Studio, Kurse und Team in Ruhe kennen – unverbindlich.', btn='Termin vereinbaren')))

SITES['werlter'] = dict(
    slug='werlter-fitness-studio', firma='Werlter Fitness Studio & Physiotherapie', web='werlter-fitness-studio.de', fonts='r11werlter',
    title='Werlter Fitness Studio & Physiotherapie – Fitnessstudio in Werlte', desc='Fitnessstudio und Physiotherapie in Werlte seit 1987: Training, Kurse, Sauna, E-Gym, Physio ohne Rezept. Kostenloses Probetraining.',
    tel='05951 3233', tel_i='+4959513233', mail='info@werlter-fitness-studio.de', adresse='Raddeweg 4, 49757 Werlte', google=('4,7', 67),
    cta='Probetraining vereinbaren', nav=[('Leistungen', 'leistungen'), ('Kurse', 'kurse'), ('Studio', 'studio'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '08:00 – 21:30'), ('Fr', '08:00 – 20:00'), ('Sa', '10:00 – 16:00'), ('So', '09:30 – 12:00')],
    form_opts=['Kostenloses Probetraining', 'Physiotherapie-Termin', 'Kurse', 'Firmenfitness', 'Sonstiges'], form_h3='Probetraining anfragen', form_p='Wir rufen Sie zurück und finden einen passenden Termin.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ihr erster Schritt: <em>ein Probetraining.</em>', kt_p='Rufen Sie an oder hinterlassen Sie Ihre Nummer – wir melden uns persönlich.',
    social=[('Instagram', 'https://www.instagram.com/werlterfitnessstudio/'), ('Facebook', 'https://www.facebook.com/p/Werlter-Fitness-Studio-100063505755762/')],
    bot=dict(name='Willi', tag='Ihr Studio-Guide', hello='Hallo! Ich bin Willi. Soll ich Ihnen kurz zeigen, was Sie im Werlter Fitness Studio erwartet?', hi='Hallo! Ich bin Willi vom Werlter Fitness Studio. Wobei darf ich helfen?',
             qa=[['Probetraining?', 'Das Probetraining ist kostenlos. Einfach anrufen: 05951 3233 – oder unten das Formular nutzen.'], ['Physio ohne Rezept?', 'Ja – als Heilpraktiker für Physiotherapie sind Erstkontakt und Behandlung auch ohne ärztliche Verordnung möglich.'], ['Muss ich einen Vertrag machen?', 'Nein. Von Tageskarte und 10er-Karte bis zum 24-Monatsabo – Sie wählen frei.'], ['Öffnungszeiten', 'Mo–Do 8–21:30, Fr 8–20, Sa 10–16 und So 9:30–12 Uhr.']],
             tour=[['#leistungen'], ['#kurse'], ['#studio'], ['#kontakt']]),
    vars='--bg:#fff;--ink:#141414;--mute:#5a5a5a;--p:#D7262E;--a:#E8352B;--a-ink:#fff;--dk:#121212;--s2:#f5f3f1;--fh:"Anton",Impact,sans-serif;--fb:"Archivo",system-ui,sans-serif;--r:6px;--r2:10px;--br:6px;--hero-ov:linear-gradient(100deg,rgba(10,10,10,.9) 0%,rgba(10,10,10,.55) 48%,rgba(140,10,10,.15) 100%);--mq-bg:linear-gradient(90deg,#D7262E,#F0652A);--hd-bg:rgba(18,18,18,.92);--hd-ink:#fff;--logo-h:62px',
    css='''.hs h1,.h2{text-transform:uppercase;letter-spacing:.005em;font-weight:400}.hs h1{font-size:clamp(50px,6.6vw,104px)}
.hd .logo img{border-radius:50%;background:#fff;padding:3px}
.hs .big{-webkit-text-stroke:2px rgba(232,53,43,.45)}
.hs::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:60px;background:#fff;clip-path:polygon(0 100%,100% 30%,100% 100%);z-index:2}
.hs .w{padding-bottom:90px}.ft img{border-radius:50%;background:#fff;padding:3px;height:64px}
.tb .lst button{font-family:var(--fb);font-weight:800;text-transform:uppercase;letter-spacing:.02em}
.sc .cd{border-radius:8px}.sc .cd h3{text-transform:uppercase;font-weight:400;font-size:26px}
.rv .sum b,.nb b,.sp .row div::before{font-weight:400}
.kt .bx{border-top:6px solid var(--p)}''',
    img={'logo.png': ('werlter/img/i010.jpg', 300, 'trim'), 'h-studio.jpg': ('werlter/img/i003.jpg', 2000), 'h-cycling.jpg': ('werlter/img/i011.jpg', 2000), 'h-kurs.jpg': ('werlter/img/i008.jpg', 2000),
         'physio.jpg': ('werlter/img/i019.jpg', 900), 'diagnostik.jpg': ('werlter/img/i018.jpg', 1000), 'egym.jpg': ('werlter/img/i001.jpg', 1100, (0, .1, 1, .85)), 'sauna.jpg': ('werlter/img/i020.jpg', 1000),
         'solarium.jpg': ('werlter/img/i012.jpg', 1000, (0, .2, 1, .8)), 'gebaeude.jpg': ('werlter/img/i002.jpg', 1400), 'team.jpg': ('werlter/img/i019.jpg', 900),
         'k-cycling.jpg': ('werlter/img/i011.jpg', 900), 'k-bbp.jpg': ('werlter/img/i014.jpg', 900), 'k-ruecken.jpg': ('werlter/img/i009.jpg', 900), 'k-pilates.jpg': ('werlter/img/i015.jpg', 900),
         'k-funktion.jpg': ('werlter/img/i007.jpg', 900), 'k-zumba.jpg': ('werlter/img/i013.jpg', 900)},
    adresse_map='Raddeweg 4, 49757 Werlte', body=b_werlter)

# ───────────────────────── 2. FC Fitnessclub Hümmling ─────────────────────────
def b_huemmling(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h-arena.jpg'], big='WERLTE', pos={'h-arena.jpg': '60% 50%'},
        ey='Fitnessclub Hümmling · Werlte · 365 Tage geöffnet',
        h1='Dein Training. <em>Deine Arena.</em>',
        sub='Kraft, Ausdauer, Kickboxen und Personal Training – betreut von Hans und Andrea van de Merbel, mehrfach ausgezeichnet bei Deutschen Meisterschaften.',
        ubar=[('365 Tage für euch da', 'Mo–Fr 7–22 Uhr, Wochenende & Feiertage 9–21 Uhr'), ('Profis an deiner Seite', 'Individueller Trainings- und Ernährungsplan'), ('Probetraining fair', 'Wird bei Vertragsabschluss erstattet')]))
        + marquee(['Krafttraining', 'Ausdauer', 'Kickboxen', 'Personal Training', 'Körperanalyse', 'IR-Sauna', 'Solarium', 'Hansefit'])
        + panels('studio', 'Das Studio', 'Trainieren, wo <em>Champions</em> trainieren.', 'Kraftgeräte, Freihantelbereich, Gerätezirkel und Cardio – fahr mit der Maus über die Bereiche.', [
            ('Kraftbereich', 'p-kraft.jpg', 'Plate-Loaded-Geräte, Kabelzüge und Hantelscheiben vor der Kolosseum-Wand – hier wird ehrlich trainiert.', '40% 50%'),
            ('Gerätezirkel', 'p-zirkel.jpg', 'Geführte Geräte auf Parkett: ideal zum Einstieg und für gesundes, gelenkschonendes Training.', '50% 50%'),
            ('Cardio', 'p-cardio.jpg', 'StairMaster & Co.: Ausdauer, die dich wirklich fordert.', '50% 40%'),
            ('Freihantel', 'p-frei.jpg', 'Bänke, Racks und Gewichte für alle, die Muskeln aufbauen wollen.', '50% 60%'),
            ('Palmen-Lounge', 'p-palmen.jpg', 'Trainieren mit Urlaubsblick – der ruhige Gerätebereich mit blauem Licht.', '50% 50%')], 'dk')
        + story('team', 'Hans & Andrea van de Merbel', 'Unsere Leidenschaft <em>geben wir weiter.</em>', [
            'Seit August 2010 betreiben wir schon ein Studio in Meppen/Apeldorn – wir haben unser Hobby zum Beruf gemacht. Im Haus Möbel Wilken in Werlte haben wir dann ein weiteres Studio eröffnet.',
            'Bei uns herrscht eine entspannte, familiäre Atmosphäre. Ihr werdet kompetent beraten, angeleitet und begleitet und bekommt einen individuellen Trainingsplan – auf Wunsch auch einen persönlichen Ernährungsplan.'],
            'p-frei.jpg', cap='Freihantelbereich im Fitnessclub Hümmling', tl=[('2009', '1. Platz Paare bei der Deutschen Meisterschaft'), ('2010', 'Eigenes Studio in Meppen/Apeldorn'), ('2012', 'Andrea: Miss Fitness Platz 1 – Internationale Deutsche Meisterschaft'), ('2020', 'Andrea: Ms Figure Platz 1 – Deutsche Meisterschaft')], rev=True)
        + tabs('extras', 'Mehr als Geräte', 'Alles für <em>deinen Fortschritt.</em>', 'Messen, kämpfen, entspannen – das gehört bei uns dazu.', [
            ('Körperanalyse', 'p-zirkel.jpg', 'Der cardioscan Checkpoint erstellt in rund 10 Minuten dein Vitalitätsprofil: Herz und Stress, Blutdruck, Stoffwechsel und Körperzusammensetzung per BIA – die Grundlage für deinen Plan.', ['EKG-genauer Herzcheck', 'Stress-Index', 'Körperfett & Muskelmasse']),
            ('Kickboxen', 'p-kraft.jpg', 'Kickboxen für alle ab 8 Jahren montags und mittwochs, dazu eine eigene Gruppe für Mädels von 8 bis 12 Jahren am Freitag. Fürs erste Mal einfach vorher anrufen.', ['Ab 8 Jahren', 'Mädels-Gruppe', 'Probe nach Anruf']),
            ('IR-Sauna', 'p-palmen.jpg', 'Nach jedem Training kostenlos: moderne Infrarot-Kabinen mit Musikanlage – im Damen- und im Herrenbereich.', ['Kostenlos', 'Damen & Herren']),
            ('Solarium', 'p-cardio.jpg', 'Der Sonnenengel steht für gute Bräunungsergebnisse mit variablem UV-Spektrum – nur auf Termin.', ['Nur auf Termin']),
            ('Hansefit', 'p-zirkel.jpg', 'Wir sind Partner von Hansefit – trainiere über deinen Arbeitgeber.', ['Firmenfitness'])])
        + '<section class="sec dk" style="padding-top:0"><div class="w">' + numbers([('365', 'Tage im Jahr geöffnet'), ('7–22', 'Uhr unter der Woche'), ('2010', 'erstes eigenes Studio'), ('10 Min', 'für dein Vitalprofil')]) + '</div></section>'
        + reviews(s, ['Andrea setzt die Messlatte richtig hoch – bei Qualität, Standards, Ausstattung und Service.', 'Super, sehr zu empfehlen! Der Inhaber ist sehr freundlich und hilfsbereit.', 'Ein sehr gutes Studio mit netten Trainern.', 'Die Hansefit-Onlinekurse von Andrea sind ideal und sehr zu empfehlen – die Besten!'])
        + steps('So startest du', 'Erst testen, <em>dann entscheiden.</em>', [('Anrufen', 'Melde dich unter 05951 8949200 – wir sind 365 Tage für euch da.'), ('Probetraining', 'Du trainierst einen Tag lang wie mit einer Tageskarte und lernst alles kennen.'), ('Zurück bei Vertrag', 'Zeig den Beleg beim Vertragsabschluss – du bekommst den Betrag erstattet.')], 'dk')
        + contact(s) + footer(s) + pop(dict(img='h-arena.jpg', ey='Kickboxen ab 8 Jahren', h='Erstes Training? Einfach anrufen.', p='Montags und mittwochs, dazu die Mädels-Gruppe am Freitag.', btn='Probe vereinbaren')))

SITES['huemmling'] = dict(
    slug='fitnessclub-huemmling-werlte', firma='FC Fitnessclub Hümmling GmbH', web='fitnessclub-huemmling.de', fonts='r11huemmling', du=True,
    title='Fitnessclub Hümmling – Fitnessstudio in Werlte', desc='Fitnessclub Hümmling in Werlte: Krafttraining, Kickboxen, Körperanalyse, IR-Sauna. 365 Tage geöffnet. Betreut von Hans und Andrea van de Merbel.',
    tel='05951 8949200', tel_i='+4959518949200', mail='fitnessclub-huemmling@hotmail.com', adresse='Unfriedstraße 4, 49757 Werlte', google=('4,6', 60),
    cta='Probetraining sichern', nav=[('Studio', 'studio'), ('Team', 'team'), ('Extras', 'extras'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '07:00 – 22:00'), ('Wochenende', '09:00 – 21:00'), ('Feiertage', '09:00 – 21:00')],
    form_opts=['Probetraining', 'Kickboxen', 'Körperanalyse', 'Personal Training', 'Solarium-Termin'], form_h3='Probetraining anfragen', form_p='Hinterlass deine Nummer – wir rufen dich zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Bereit für deine <em>erste Runde?</em>', kt_p='Ruf uns an oder hinterlass deine Nummer. Wir sind 365 Tage für euch da.',
    social=[('Facebook', 'https://www.facebook.com/fitnessclubhuemmling/')],
    rv_h2='Das sagen unsere <em>Mitglieder.</em>',
    bot=dict(name='Max', tag='Dein Studio-Guide', hello='Hey! Ich bin Max. Soll ich dir kurz zeigen, was dich im Fitnessclub Hümmling erwartet?', hi='Hey! Ich bin Max vom Fitnessclub Hümmling. Was möchtest du wissen?',
             qa=[['Probetraining?', 'Das Probetraining läuft wie eine Tageskarte. Zeigst du den Beleg beim Vertragsabschluss, bekommst du den Betrag zurück.'], ['Kickboxen?', 'Mo und Mi für alle ab 8 Jahren, freitags die Mädels-Gruppe (8–12). Fürs erste Mal bitte kurz anrufen: 05951 8949200.'], ['Öffnungszeiten', 'Mo–Fr 7–22 Uhr, Wochenende und Feiertage 9–21 Uhr – 365 Tage im Jahr.'], ['Ernährungsplan?', 'Ja, auf Wunsch erstellen Hans und Andrea dir einen individuellen Ernährungsplan.']],
             tour=[['#studio'], ['#team'], ['#extras'], ['#kontakt']]),
    vars='--bg:#141619;--ink:#f1f3f4;--mute:#a9b1b8;--p:#21A6CC;--a:#2BB8DD;--a-ink:#061317;--dk:#0d0f11;--s:#1d2024;--s2:#191c1f;--line:rgba(255,255,255,.1);--fh:"Big Shoulders Display",Impact,sans-serif;--fb:"Figtree",system-ui,sans-serif;--r:4px;--r2:6px;--br:4px;--hd-bg:rgba(14,16,18,.9);--hd-ink:#fff;--mq-bg:#e9eef0;--mq-ink:#141619;--logo-h:52px;--ft-bg:#0a0b0c',
    css='''.hs h1,.h2{text-transform:uppercase;font-weight:900;letter-spacing:.01em}.hs h1{font-size:clamp(54px,7.6vw,124px)}
.hd .logo img{background:#fff;border-radius:6px;padding:4px 8px}.ft img{background:#fff;border-radius:6px;padding:4px 8px}
.hs .ov{background:linear-gradient(90deg,rgba(13,15,17,.95) 0%,rgba(13,15,17,.6) 50%,rgba(13,15,17,.2) 100%),linear-gradient(0deg,rgba(13,15,17,.9),transparent 45%)}
.hs .big{font-weight:900;-webkit-text-stroke:2px rgba(43,184,221,.35)}
.mq{font-weight:800;text-transform:uppercase;letter-spacing:.06em}
.ap .pn{border:1px solid rgba(255,255,255,.08)}.ap .pn h3{text-transform:uppercase;font-weight:800}
.tb .lst button{text-transform:uppercase;letter-spacing:.03em;font-weight:800}
.st figure{border:1px solid rgba(255,255,255,.1)}
.st .tl b{font-size:22px}
.rv .cd,.kt .bx{color:var(--ink)}.kt .fm input,.kt .fm select,.kt .fm textarea{background:#0f1113;color:#fff;border-color:rgba(255,255,255,.15)}
.chip b{background:var(--a)}''',
    img={'logo.png': ('huemmling/img/logo.jpg', 320, 'trim'), 'h-arena.jpg': ('huemmling/img/gym-kolosseum.jpg', 0), 'h-zirkel.jpg': ('huemmling/img/zirkel.jpg', 0),
         'p-kraft.jpg': ('huemmling/img/gym-kolosseum.jpg', 0), 'p-zirkel.jpg': ('huemmling/img/zirkel.jpg', 0), 'p-cardio.jpg': ('huemmling/img/stairmaster.jpg', 0),
         'p-frei.jpg': ('huemmling/img/kolosseum-hoch.jpg', 0), 'p-palmen.jpg': ('huemmling/img/geraete-palmen.jpg', 0)},
    body=b_huemmling)

# ───────────────────────── 3. optiMumm Esterwegen ─────────────────────────
def b_optimumm(s):
    return (hd(s, light=False) + hero_comp(s, dict(imgs=['h-studio.jpg', 'haus.jpg', 'schlinge.jpg'], pos0='40% 50%',
        ey='Physiotherapie & Fitness-Studio · Esterwegen', h1='Vorbeugen. Fitness. <em>Gesundheit.</em>',
        sub='Unten die Physiotherapie, oben das Fitness-Studio – unter einem Dach in Esterwegen. Betreut von Physiotherapeuten, die wissen, was Ihr Körper braucht.',
        badge=('2005', 'gegründet in Esterwegen'), alt='Trainingsfläche im optiMumm'))
        + marquee(['Krankengymnastik', 'Manuelle Lymphdrainage', 'Massage', 'Fango', 'Schlingentisch', 'Rücken-Erfolgs-Training', 'Gerätetraining', 'Hausbesuche'])
        + duo('angebot', 'Zwei Etagen, ein Ziel', 'Therapie unten. <em>Training oben.</em>', 'Durch die Verbindung von Physiotherapie und modernem Gesundheitstraining schaffen wir die besten Voraussetzungen für Ihre Problemlösung.', [
            ('Erdgeschoss', 'Physiotherapie', 'physio.jpg', 'Bleibende Gesundheit, Wohlbefinden und Vorbeugung: In Zusammenarbeit mit Ihrem Arzt finden wir die passende Behandlung. Auch Hausbesuche gehören dazu.', ['Krankengymnastik', 'KG nach Bobath', 'Schlingentisch', 'Lymphdrainage', 'Fango', 'Massage', 'Fußreflexzonen', 'Elektrotherapie'], 'Behandlung anfragen'),
            ('Obergeschoss', 'Fitness-Studio', 'fitness.jpg', 'Ausdauer- und Krafttraining an computergesteuerten Geräten – mit ausgiebiger Einweisung durch geschulte Physiotherapeuten und Ihrem persönlichen Trainingsschlüssel.', ['Laufbänder', 'Crosstrainer', 'Kraftgeräte', 'Kurzhanteln', 'Rücken-Erfolgs-Training'], 'Probetraining anfragen')])
        + scroller('anwendungen', 'Unsere Anwendungen', 'Behandlung, die <em>wirkt.</em>', 'Von der Krankengymnastik bis zur Massage – individuell auf Sie abgestimmt.', [
            ('Krankengymnastik', 'a-kg.jpg', 'Bewegungstherapie zur Wiederherstellung von Bewegungs- und Funktionsfähigkeit.', '50% 30%'),
            ('Schlingentisch', 'a-schlinge.jpg', 'Körperteile werden entlastet – so sind Bewegungen möglich, die sonst kaum gehen.', '50% 50%'),
            ('Manuelle Lymphdrainage', 'a-lymph.jpg', 'Sanfte Grifftechnik, die Schwellungen reduziert und entstaut.', '50% 50%'),
            ('Medizinische Massage', 'a-massage.jpg', 'Löst Verspannungen und fördert die Durchblutung.', '50% 40%'),
            ('Fußreflexzonen', 'a-fuss.jpg', 'Gezielte Druckpunkte an den Füßen für mehr Wohlbefinden.', '50% 50%'),
            ('Elektrotherapie', 'a-elektro.jpg', 'Reizstrom zur Schmerzlinderung und Muskelaktivierung.', '50% 40%')], 'alt')
        + story('ueber', 'Über optiMumm', 'Seit 2005 Ihr Partner <em>für Gesundheit.</em>', [
            '„Mens sana in corpore sano“ – ein gesunder Geist in einem gesunden Körper. Regelmäßiger Sport und gesunde Ernährung steigern Ihr körperliches und seelisches Wohlbefinden.',
            'Inhaber Holger Otten und sein Team betreuen Sie individuell – egal ob jung oder alt. Und wer nicht zu uns kommen kann, den besuchen wir: Täglich fährt unsere Mitarbeiterin zu Patienten nach Hause.'],
            'haus.jpg', cap='optiMumm am Erlenweg 2 in Esterwegen', tl=[('2005', 'Gründung des Fitness-Studios in Esterwegen'), ('Heute', 'Physiotherapie und Fitness unter einem Dach'), ('Täglich', 'Hausbesuche für Patienten zu Hause')])
        + story('ruecken', 'Das Rücken-Erfolgs-Training', 'Raus aus dem <em>Nacken-Schmerz.</em>', [
            'Viel Sitzen und wenig Bewegung belasten die Rückenmuskulatur einseitig. Unser eigenes Konzept verbindet Gruppenkurse, gezieltes Training und wichtiges Hintergrundwissen – begleitet von unseren Physiotherapeuten.',
            'Mit dem tragbaren TGS-Schlüssel speichert jedes Gerät Ihr individuelles Programm. So trainieren Sie immer richtig eingestellt.'],
            'tgs.jpg', cap='Trainingsterminal im Studio', rev=True, cls='alt')
        + reviews(s, ['Fitness, Massagen, Physiotherapie in vielen Varianten – lockere Atmosphäre, kompetente Leitung und viele neue Geräte. Das Programm wird individuell erklärt.', 'Hervorragende Beratung und Service, toll geholfen bei meinem Bandscheibenvorfall.', 'Physiotherapie und Rehasport sind ausgezeichnet, die Therapeuten kompetent und freundlich.', 'Ich bin im Rehasport angemeldet: Die Übungsleiterin ist sehr nett und motiviert.'], 'alt')
        + steps('So geht es los', 'Ihr Weg zu <em>mehr Wohlbefinden.</em>', [('Anrufen', 'Unter 05955 2762 – wir beraten Sie gern.'), ('Einweisung', 'Unsere Physiotherapeuten zeigen Ihnen jedes Gerät.'), ('Ihr Programm', 'Gespeichert auf Ihrem Trainingsschlüssel.')])
        + contact(s) + footer(s))

SITES['optimumm'] = dict(
    slug='optimumm-esterwegen', firma='optiMumm Physiotherapie & Fitness-Studio', web='optimumm-fitness.de', fonts='r11optimumm',
    title='optiMumm – Physiotherapie & Fitness-Studio in Esterwegen', desc='optiMumm in Esterwegen: Physiotherapie, Hausbesuche und Fitness-Studio unter einem Dach. Seit 2005.',
    tel='05955 2762', tel_i='+4959552762', mail='info@optimumm-fitness.de', adresse='Erlenweg 2, 26897 Esterwegen', google=('4,6', 32),
    cta='Termin anfragen', nav=[('Angebot', 'angebot'), ('Anwendungen', 'anwendungen'), ('Über uns', 'ueber'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '07:00 – 21:00'), ('Fr', '07:00 – 20:00'), ('Sa', '11:00 – 15:00')],
    form_opts=['Physiotherapie-Termin', 'Probetraining Fitness', 'Rücken-Erfolgs-Training', 'Hausbesuch', 'Sonstiges'], form_h3='Termin anfragen', form_p='Wir melden uns persönlich bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir sind <em>für Sie da.</em>', kt_p='Ob Behandlung, Probetraining oder Hausbesuch – rufen Sie an oder schreiben Sie uns.',
    bot=dict(name='Otto', tag='Ihr Gesundheits-Guide', hello='Hallo! Ich bin Otto. Soll ich Ihnen zeigen, was optiMumm für Sie tun kann?', hi='Hallo! Ich bin Otto von optiMumm. Wobei darf ich helfen?',
             qa=[['Physio oder Fitness?', 'Beides: Physiotherapie im Erdgeschoss, Fitness-Studio im Obergeschoss – unter einem Dach.'], ['Hausbesuche?', 'Ja, unsere Mitarbeiterin fährt täglich zu Patienten nach Hause.'], ['Öffnungszeiten', 'Mo–Do 7–21, Fr 7–20 und Sa 11–15 Uhr.'], ['Termin', 'Rufen Sie an: 05955 2762 – oder nutzen Sie das Formular.']],
             tour=[['#angebot'], ['#anwendungen'], ['#ueber'], ['#kontakt']]),
    vars='--bg:#FBFCF8;--ink:#1B2A1A;--mute:#55634F;--p:#6FA82B;--a:#C8322B;--a-ink:#fff;--s2:#EEF4E4;--fh:"Outfit",system-ui,sans-serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:22px;--r2:34px;--mq-bg:#1B2A1A;--mq-ink:#D6F0B0;--logo-h:44px;--ft-bg:#152014;--hp-bg:linear-gradient(180deg,#F2F8E9,#FBFCF8)',
    css='''.hp h1{font-weight:800}.h2{font-weight:800}
.comp .c1{border-radius:40px 40px 140px 40px}.comp .c2{border-radius:999px;width:38%;height:46%}
.duo .wd small{color:#C9F08F}
.ft img{background:#fff;padding:6px 10px;border-radius:10px}''',
    img={'logo.png': ('optimumm/img/i010.png', 500), 'h-studio.jpg': ('optimumm/img/i014.jpg', 1800), 'haus.jpg': ('optimumm/img/i009.jpg', 1600, (.15, 0, .85, 1)),
         'schlinge.jpg': ('optimumm/img/i022.jpg', 800), 'physio.jpg': ('optimumm/img/i004.jpg', 900), 'fitness.jpg': ('optimumm/img/i014.jpg', 1400, (.42, 0, 1, 1)),
         'a-kg.jpg': ('optimumm/img/i004.jpg', 900), 'a-schlinge.jpg': ('optimumm/img/i022.jpg', 900), 'a-lymph.jpg': ('optimumm/img/i005.jpg', 900), 'a-massage.jpg': ('optimumm/img/i003.jpg', 900),
         'a-fuss.jpg': ('optimumm/img/i001.jpg', 900), 'a-elektro.jpg': ('optimumm/img/i002.jpg', 900), 'tgs.jpg': ('optimumm/img/i012.jpg', 900)},
    body=b_optimumm)

# ───────────────────────── 4. reaktiv Sprenkel Sögel ─────────────────────────
def b_sprenkel(s):
    return (hd(s, light=False) + hero_comp(s, dict(imgs=['mtt.jpg'], pos0='62% 30%',
        ey='Physiotherapie & Medizinische Trainingstherapie · Sögel', h1='Wieder Freude an <em>Bewegung</em> haben.',
        sub='Physiotherapie, medizinische Fitness, Funktionstraining und Präventionskurse – ein ganzheitliches Gesundheitskonzept aus einer Hand. Auch ohne Rezept.',
        badge=('seit 2005', 'Ihre Praxis in Sögel'), alt='Das Team von reaktiv Sprenkel'))
        + video('film', 'Imagefilm', 'Ein Blick in <em>unsere Praxis.</em>', 'Große MTT, manuelle Therapie, Behandlung neurologischer Patienten – sehen Sie selbst.', 'film.mp4', 'film.jpg', 'alt')
        + tabs('leistungen', 'Unser Gesundheitskonzept', 'Aktiv <em>statt passiv.</em>', 'Wir behandeln Ihre Schmerzen und gehen den Ursachen auf den Grund – mit Therapie und Training.', [
            ('Physiotherapie', 'physio.jpg', 'Manuelle Therapie, Muskeltechniken und aktive Übungen: Wir stellen die Funktion Ihres Körpers wieder her – bei Rücken-, Knie-, Hüft- und Schulterproblemen, nach Operationen und bei Kindern.', ['Manuelle Therapie', 'Lymphdrainage', 'Bobath', 'Orthopädie', 'Chirurgie', 'Kinder']),
            ('Medizinische Trainingstherapie', 'mtt.jpg', 'Die intelligente Chipkartensteuerung stimmt jedes Gerät auf Sie ab. Prävention, Trainingskontrolle und schnelle Erfolge – so persönlich wie möglich.', ['Chipkarte', 'Prävention', 'Kostenloses Probetraining']),
            ('Firmenfitness', 'praxis.jpg', 'Als EGYM-Wellpass- und Epassi-Partner trainieren Sie mit Unterstützung Ihres Arbeitgebers – günstig statt teurer Mitgliedschaft.', ['EGYM Wellpass', 'Epassi']),
            ('Kurse', 'kurs.jpg', 'Funktionstraining und Präventionskurse für Herz-Kreislauf, Atmung, Bewegung, Stoffwechsel und Psyche.', ['Funktionstraining', 'Prävention']),
            ('Ohne Rezept', 'empfang.jpg', 'Auch ohne Rezept ist eine Privatbehandlung inklusive Nutzung aller Trainingsgeräte möglich.', ['Privatbehandlung', 'Alle Geräte'])])
        + story('praxis', 'Ihr starker Partner für Gesundheit', 'Aus Sögel. <em>Für Sögel.</em>', [
            '1996 legten Thomas Sprenkel und seine Frau das Examen als Physiotherapeuten ab. Nach vielen Jahren in auswärtigen Praxen zog es sie zurück in die Heimat.',
            'Jeder Patient wird persönlich untersucht und bekommt einen eigenen Therapieplan. Unsere Therapeuten haben mindestens eine anerkannte Weiterbildung in Manueller Therapie, Lymphdrainage und Bobath.'],
            'gebaeude.jpg', cap='Die Praxis in der Wahner Straße 10', tl=[('1996', 'Examen als Physiotherapeuten'), ('2005', 'Erste eigene Praxis in der Sigiltrastraße'), ('2008', 'Umzug in den Neubau Wahner Straße 10'), ('Heute', 'Neuer MTT-Bereich mit Chipkartensteuerung')])
        + reviews(s, ['Eine tolle Praxis mit sehr freundlichem Personal. Beim Bandscheibenvorfall bekam ich noch am selben Tag Termine angeboten.', 'Nach der dritten manuellen Therapie endlich Besserung – nach über einem Jahr Schmerzen.', 'Ein fantastisches, freundliches und bestens ausgebildetes Team. Hier wird Physiotherapie mit Freude gemacht.', 'Freundlich, respektvoll und eine angenehme Atmosphäre. Die Praxis ist modern ausgestattet.'], 'alt')
        + steps('So starten Sie', 'Drei Schritte zu <em>mehr Bewegung.</em>', [('Termin anfragen', 'Telefon 05952 2936 oder das Formular.'), ('Persönliche Untersuchung', 'Wir hören zu und erstellen Ihren Therapieplan.'), ('Therapie & Training', 'Behandlung und MTT greifen ineinander.')])
        + contact(s) + footer(s) + pop(dict(img='mtt.jpg', ey='Neue MTT in Sögel', h='Kostenloses Probetraining', p='Testen Sie die medizinische Trainingstherapie mit Chipkarte.', btn='Probetraining anfragen')))

SITES['sprenkel'] = dict(
    slug='reaktiv-sprenkel-soegel', firma='reaktiv Sprenkel – Praxis für Physiotherapie und Rehabilitation', web='physiotherapie-sprenkel.de', fonts='r11sprenkel',
    title='reaktiv Sprenkel – Physiotherapie & MTT in Sögel', desc='reaktiv Sprenkel in Sögel: Physiotherapie, Medizinische Trainingstherapie, Firmenfitness und Kurse. Auch ohne Rezept.',
    tel='05952 2936', tel_i='+4959522936', mail='info@physiotherapie-sprenkel.de', adresse='Wahner Straße 10, 49751 Sögel', google=('4,8', 10),
    cta='Termin anfragen', nav=[('Leistungen', 'leistungen'), ('Film', 'film'), ('Praxis', 'praxis'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo, Mi', '08:00 – 20:30'), ('Di, Do', '08:00 – 20:00'), ('Fr', '08:00 – 15:00')],
    form_opts=['Physiotherapie-Termin', 'Probetraining MTT', 'Firmenfitness', 'Kurse', 'Bewerbung'], form_h3='Termin anfragen', form_p='Wir melden uns zeitnah bei Ihnen.', form_btn='Anfrage senden',
    kt_ey='Kontakt', kt_h2='Wie können wir <em>helfen?</em>', kt_p='Termine ändern oder absagen bitte telefonisch – Anfragen gern auch über das Formular.',
    social=[('Instagram', 'https://www.instagram.com/physiotherapie_reaktivsprenkel/'), ('Facebook', 'https://www.facebook.com/PhysiotherapieSprenkel/')],
    rv_h2='Das sagen unsere <em>Patienten.</em>',
    bot=dict(name='Rex', tag='Ihr Praxis-Guide', hello='Hallo! Ich bin Rex. Soll ich Ihnen kurz zeigen, wie reaktiv Sprenkel Ihnen hilft?', hi='Hallo! Ich bin Rex von reaktiv Sprenkel. Wobei darf ich helfen?',
             qa=[['Ohne Rezept?', 'Ja – auch ohne Rezept ist eine Privatbehandlung inklusive Nutzung aller Trainingsgeräte möglich.'], ['Probetraining MTT', 'Das Probetraining für die medizinische Trainingstherapie ist kostenlos. Einfach anfragen!'], ['Firmenfitness', 'Wir sind Partner von EGYM Wellpass und Epassi.'], ['Telefon', '05952 2936']],
             tour=[['#film'], ['#leistungen'], ['#praxis'], ['#kontakt']]),
    vars='--bg:#F7F9FC;--ink:#0E2240;--mute:#4D5E78;--p:#1F57A5;--a:#F5C400;--a-ink:#0E2240;--s2:#EAF0F8;--fh:"Barlow Condensed",system-ui,sans-serif;--fb:"Barlow",system-ui,sans-serif;--r:10px;--r2:16px;--br:10px;--mq-bg:#1F57A5;--logo-h:44px;--ft-bg:#0B1A33;--hp-bg:linear-gradient(160deg,#EAF0F8,#F7F9FC 55%)',
    css='''.hp h1,.h2{text-transform:uppercase;font-weight:800;letter-spacing:.005em}.hp h1{font-size:clamp(50px,6.2vw,96px)}
.comp .c1{clip-path:polygon(0 0,100% 0,100% 88%,88% 100%,0 100%)}
.tb .lst button{text-transform:uppercase;font-weight:700}
.ey{color:#1F57A5}.ft img{background:#fff;padding:8px 10px;border-radius:8px}''',
    img={'logo.png': ('logos/sprenkel.png', 400), 'team.jpg': ('sprenkel/img/i064.jpg', 0), 'mtt.jpg': ('sprenkel/img/i040.jpg', 0), 'wirbel.jpg': ('sprenkel/img/i056.jpg', 0),
         'physio.jpg': ('sprenkel/img/i007.jpg', 0), 'praxis.jpg': ('sprenkel/img/i030.jpg', 1400), 'kurs.jpg': ('sprenkel/img/i018.jpg', 1000), 'empfang.jpg': ('sprenkel/img/i005.jpg', 0),
         'gebaeude.jpg': ('sprenkel/img/i034.jpg', 0), 'film.mp4': ('vid/sprenkel-film.mp4', 0), 'film.jpg': ('vid/sprenkel-poster.jpg', 0)},
    body=b_sprenkel)

# ───────────────────────── 5. Physio Vital & Physio Fit Sögel ─────────────────────────
def b_physiovital(s):
    return (hd(s, light=False) + hero_comp(s, dict(imgs=['h-kurs.jpg', 'h-cycling.jpg', 'h-gravity.jpg'], pos0='50% 40%',
        ey='Physiotherapie · Medizinische Fitness · Ernährung · Sögel', h1='Therapie und Bewegung für ein <em>aktives Leben.</em>',
        sub='Physio Vital behandelt, Physio Fit trainiert, PEP begleitet beim Abnehmen. Drei Wege, ein Team – damit Sie schmerzfrei und gesund leben.',
        badge=('seit 2002', 'Ihre Praxis in Sögel'), alt='Kurs im Physio Fit'))
        + duo('angebot', 'Physio Vital & Physio Fit', 'Behandeln. Trainieren. <em>Wohlfühlen.</em>', 'Die Praxis im Erdgeschoss ist barrierefrei, das Fitness-Studio liegt im oberen Stockwerk.', [
            ('Physio Vital', 'Physiotherapie', 'physio.jpg', 'Bei akuten oder chronischen Schmerzen, nach Unfall oder Operation – und als Vorsorge, bevor der Schmerz chronisch wird. Vier Behandlungsräume, barrierefrei.', ['Krankengymnastik', 'FOI', 'Bobath', 'Lymphdrainage', 'Kiefergelenk', 'Beckenboden', 'Liebscher & Bracht'], 'Behandlung vereinbaren'),
            ('Physio Fit', 'Medizinische Fitness', 'fit.jpg', 'Gerätezirkel Vitality Circuit von Ergofit, Sensopro, Gravity Group, Indoor Cycling und viele Kurse – Sport für jedes Alter.', ['Vitality Circuit', 'Sensopro', 'Gravity Group', 'Indoor Cycling', 'Mama Fit'], 'Beratung buchen')])
        + panels('training', 'Unsere Trainingsangebote', 'Finden Sie <em>Ihr Training.</em>', 'Fahren Sie über die Bilder.', [
            ('Vitality Circuit', 'p-zirkel.jpg', 'Computergestützter medizinischer Gerätezirkel „Ergofit Vector“ – gesund, sicher und effizient.', '50% 50%'),
            ('Gravity Group', 'p-gravity.jpg', 'Körpergewicht gegen Schwerkraft: zeitsparendes, hochintensives Kraftausdauertraining auf der schiefen Ebene.', '50% 50%'),
            ('Indoor Cycling', 'p-cycling.jpg', 'Mit fetziger Musik durch Berge und Täler – Ihr Leistungslevel bestimmen Sie selbst.', '50% 50%'),
            ('Kurse', 'p-kurs.jpg', 'Wochenstarter, Pilates, Zumba, Step Aerobic, BOP, Faszien-Fit und Wirbelsäulengymnastik.', '50% 40%'),
            ('Mama Fit', 'p-mama.jpg', 'Ganzkörpertraining in netter Gesellschaft – Ihr Baby darf mit.', '50% 50%')])
        + story('pep', 'Ernährungsprogramm PEP', 'Abnehmen <em>ohne Jojo-Effekt.</em>', [
            'Eine Stoffwechsel-Ernährungsanalyse zeigt, warum Sie nicht abnehmen oder keine Muskeln aufbauen. Daraus entsteht Ihr individueller Ernährungsplan.',
            'In drei Phasen – Stoffwechsel-Aktivierung, Gewichtsreduktion, Erhaltung – erreichen Sie Ihr Wunschgewicht, kombiniert mit einem regelmäßigen Bewegungsprogramm.'],
            'pep.jpg', cap='Beratung im Physio Fit', tl=[('Phase 1', 'Stoffwechsel-Aktivierung'), ('Phase 2', 'Gewichtsreduktion'), ('Phase 3', 'Erhaltungsphase')], cls='alt', extra='<a class="btn btn-a" style="margin-top:26px" href="#kontakt">Kostenloses Beratungsgespräch</a>')
        + story('praxis', 'Wie alles begann', 'Peter und Katja Moritz <em>kamen zurück nach Sögel.</em>', [
            '2002 wurde der Gedanke einer eigenen Praxis Realität. Aus den ersten Räumen in der General-Clay-Straße wurde später die heutige Praxis im umgebauten Kasernengebäude – und mit Physio Fit kam das Fitness-Studio dazu.',
            'Heute arbeitet hier ein Team aus erfahrenen Physiotherapeuten und Trainern mit vielen Zusatzqualifikationen – und bildet sich regelmäßig weiter.'],
            'gebaeude.jpg', cap='Physio Vital & Physio Fit in Sögel', rev=True)
        + gallery('einblicke', 'Einblicke', 'So sieht es <em>bei uns aus.</em>', [('g1.jpg', 'w2', '50% 10%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 45%')])
        + reviews(s, ['Fachliche Kompetenz und eine herzliche, familiäre Atmosphäre. Tolle Kurse, ein neuer Fitnessraum und ein fantastisches Team.', 'Super nett, man fühlt sich wohl. Tolle Atmosphäre – absolut zu empfehlen!', 'Hervorragend! Ein sehr kompetentes und freundliches Team.', 'Danke, Katja und Peter, für die Leidenschaft, die ihr in dieses Studio steckt.'], 'alt')
        + contact(s) + footer(s) + pop(dict(img='pep.jpg', ey='Ernährungsprogramm PEP', h='Kostenloses Beratungsgespräch', p='Finden Sie heraus, warum die Pfunde bisher nicht purzeln.', btn='Gespräch anfragen')))

SITES['physiovital'] = dict(
    slug='physio-vital-soegel', firma='Physio Vital & Physio Fit', web='physio-vital.net', fonts='r11physiovital',
    title='Physio Vital & Physio Fit – Physiotherapie und Fitness in Sögel', desc='Physio Vital & Physio Fit in Sögel: Physiotherapie, medizinische Fitness, Kurse und Ernährungsprogramm PEP.',
    tel='05952 990826', tel_i='+495952990826', adresse='Von-Stauffenberg-Straße 6, 49751 Sögel', google=('4,6', 7),
    cta='Beratung vereinbaren', nav=[('Angebot', 'angebot'), ('Training', 'training'), ('PEP', 'pep'), ('Praxis', 'praxis'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '08:00 – 12:00, 14:00 – 20:00'), ('Fr', '08:00 – 12:00')],
    form_opts=['Physiotherapie-Termin', 'Beratung Fitness', 'Ernährungsprogramm PEP', 'Kurse', 'Bewerbung'], form_h3='Beratung anfragen', form_p='Wir rufen Sie zurück und finden einen Termin.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Sie.</em>', kt_p='Physiotherapie-Termine am besten telefonisch, Fitness-Beratung gern auch über das Formular.',
    social=[('Instagram', 'https://www.instagram.com/physiovital_soegel/'), ('Facebook', 'https://www.facebook.com/physio76/')],
    rv_h2='Das sagen unsere <em>Patienten & Mitglieder.</em>',
    bot=dict(name='Vita', tag='Ihre Praxis-Begleiterin', hello='Hallo! Ich bin Vita. Soll ich Ihnen zeigen, was Physio Vital und Physio Fit bieten?', hi='Hallo! Ich bin Vita. Wobei darf ich helfen?',
             qa=[['Physio oder Fitness?', 'Beides: Physiotherapie im Erdgeschoss (barrierefrei), das Fitness-Studio Physio Fit oben.'], ['Abnehmen?', 'Mit dem Ernährungsprogramm PEP – das Beratungsgespräch ist kostenlos.'], ['Kurse', 'Wochenstarter, Pilates, Zumba, Step Aerobic, BOP, Faszien-Fit, Indoor Cycling und Mama Fit.'], ['Telefon', '05952 990826']],
             tour=[['#angebot'], ['#training'], ['#pep'], ['#kontakt']]),
    vars='--bg:#FFFCF7;--ink:#2A1018;--mute:#6B5359;--p:#8E1F3C;--a:#F4B41A;--a-ink:#2A1018;--s2:#F8EFE6;--fh:"Sora",system-ui,sans-serif;--fb:"Nunito Sans",system-ui,sans-serif;--r:20px;--r2:30px;--mq-bg:#8E1F3C;--logo-h:40px;--ft-bg:#2A1018;--hp-bg:radial-gradient(circle at 80% 10%,#FCE7B8,transparent 40%),#FFFCF7',
    css='''.hp h1,.h2{font-weight:800;letter-spacing:-.03em}
.comp .c1{inset:0 0 34% 0;border-radius:30px}.comp .c2{width:49%;height:31%;left:0;right:auto;bottom:0;border:0;border-radius:30px}.comp .c3{width:49%;height:31%;right:0;left:auto;top:auto;bottom:0;border:0;border-radius:30px}
.comp .badge{left:auto;right:-16px;top:40%;bottom:auto}
.ft img{background:#fff;padding:6px 10px;border-radius:10px}''',
    img={'logo.png': ('logos/physiovital.jpg', 700), 'h-kurs.jpg': ('physiovital/img/i050.jpg', 0), 'h-cycling.jpg': ('physiovital/img/i044.jpg', 0), 'h-gravity.jpg': ('physiovital/img/i038.jpg', 0),
         'physio.jpg': ('physiovital/img/i025.jpg', 0), 'fit.jpg': ('physiovital/img/i037.jpg', 0), 'p-zirkel.jpg': ('physiovital/img/i066.jpg', 0), 'p-gravity.jpg': ('physiovital/img/i035.jpg', 0),
         'p-cycling.jpg': ('physiovital/img/i042.jpg', 0), 'p-kurs.jpg': ('physiovital/img/i048.jpg', 0), 'p-mama.jpg': ('physiovital/img/i058.jpg', 0), 'pep.jpg': ('physiovital/img/i060.jpg', 0),
         'gebaeude.jpg': ('physiovital/img/i016.jpg', 0), 'g1.jpg': ('physiovital/img/i051.jpg', 0), 'g2.jpg': ('physiovital/img/i046.jpg', 0), 'g3.jpg': ('physiovital/img/i049.jpg', 0), 'g4.jpg': ('physiovital/img/i043.jpg', 0), 'g5.jpg': ('physiovital/img/i052.jpg', 0)},
    body=b_physiovital)

# ───────────────────────── 6. Reha-Zentrum Meiners Werlte ─────────────────────────
def b_meiners(s):
    return (hd(s) + hero_slides(s, dict(slides=['loop.mp4', 'h-pool.jpg', 'h-therapie.jpg'], poster='h-pool.jpg',
        ey='Reha-Zentrum Meiners · Werlte · Familienbetrieb seit 1977', h1='Gesund werden. <em>In 32 °C warmem Wasser.</em>',
        sub='Physiotherapie, Trainingsraum und ein hauseigenes Schwimmbad: Vom Babyschwimmen bis zur Reha – wir begleiten die ganze Familie.',
        ubar=[('Akutsprechstunde', 'Für Säuglinge, Kinder, Jugendliche und Erwachsene'), ('Eigenes Schwimmbad', 'Wassertemperatur 32 °C'), ('Seit 1977', 'In zweiter Generation geführt')]))
        + marquee(['Krankengymnastik', 'Manuelle Therapie', 'Vojta', 'Bobath', 'KG-Gerät', 'Bewegungsbad', 'Fango', 'Lymphdrainage', 'Kinesiotape', 'CMD'])
        + scroller('kurse', 'Kurse im Wasser und an Land', 'Für jedes Alter <em>das Richtige.</em>', 'Buchen Sie bequem Ihren Kurs-Warteplatz – Eltern-Kind-Kurse, Kinderkurse und mehr.', [
            ('Babyschwimmen', 'k-baby.jpg', 'Erste Schwimmerfahrungen gemeinsam mit Mama oder Papa – in angenehm warmem Wasser.', '50% 50%'),
            ('Schwimmkurs Seepferdchen', 'k-seepferd.jpg', 'Sicher schwimmen lernen – mit Spaß und Geduld.', '50% 40%'),
            ('Schwimmkurs Bronze', 'k-bronze.jpg', 'Der nächste Schritt für junge Schwimmerinnen und Schwimmer.', '50% 50%'),
            ('Aquafitness', 'k-aqua.jpg', 'Gelenkschonend fit werden – das Wasser trägt mit.', '50% 50%'),
            ('Funktionstraining', 'k-funktion.jpg', 'Im Wasser und trocken: Beweglichkeit erhalten, Beschwerden lindern.', '50% 50%'),
            ('T-RENA & RV Fit', 'k-trena.jpg', 'Gerätegestütztes Training mit Verordnung.', '50% 50%')], 'wide')
        + video('film', 'Reha-Zentrum Meiners in Bewegung', 'Kommen Sie mit <em>auf einen Rundgang.</em>', 'Schwimmbad, Behandlungsräume und Trainingsraum – 800 Quadratmeter für Ihre Gesundheit.', 'film.mp4', 'film.jpg', 'alt')
        + story('ueber', 'Über uns', 'Ein Familienbetrieb <em>in zweiter Generation.</em>', [
            '1977 eröffnete Wilhelm Meiners mit seiner Frau Ruth als Erster eine private Massagepraxis in der Region. Ende 1998 folgte das Reha-Zentrum mit über 800 m² an der Loruper Straße.',
            'Seit 2017 führt Tochter Alexandra Meiners den Betrieb – mit Unterstützung ihres Mannes Günther Stammermann-Meiners, im Sinne der Familientradition und mit Blick nach vorn.'],
            'familie.jpg', cap='Familie Meiners', tl=[('1975', 'Staatsexamen von Wilhelm Meiners'), ('1977', 'Eröffnung der ersten privaten Massagepraxis'), ('1998', 'Bezug des Reha-Zentrums an der Loruper Straße'), ('2017', 'Übergabe an Alexandra Meiners')])
        + story('akut', 'Akutsprechstunde', 'Wenn es <em>schnell gehen muss.</em>', [
            'Eingeklemmter Nerv, Ischias, Hexenschuss? Unsere Akutsprechstunde ist für Säuglinge, Kinder, Jugendliche und Erwachsene da – wir sind zeitnah für Sie da.'],
            'akut.jpg', cap='', rev=True, cls='alt', extra='<a class="btn btn-a" style="margin-top:26px" href="tel:+4959511266">Jetzt anrufen: 05951 1266</a>')
        + reviews(s, ['Wir kamen mit unserem drei Wochen alten Baby – beruhigend, sanft und hochprofessionell. Ohne jeden Druck.', 'Ob Babyschwimmen, Physiotherapie oder Wasserfrösche – wir fühlen uns immer bestens betreut.', 'Am selben Tag einen Termin bekommen – und schon während der Behandlung Schmerzlinderung gespürt.', 'Seit fast 8 Jahren regelmäßig hier: schnelle Terminvergabe und Fachwissen mit Herzlichkeit.'])
        + contact(s, 'alt') + footer(s) + pop(dict(img='k-baby.jpg', ey='Kurs-Warteplatz', h='Babyschwimmen & Seepferdchen', p='Sichern Sie sich jetzt einen Platz auf der Warteliste.', btn='Platz anfragen')))

SITES['meiners'] = dict(
    slug='reha-zentrum-meiners-werlte', firma='Reha-Zentrum Meiners', web='reha-zentrum-meiners.de', fonts='r11meiners',
    title='Reha-Zentrum Meiners – Physiotherapie & Schwimmbad in Werlte', desc='Reha-Zentrum Meiners in Werlte: Physiotherapie, Akutsprechstunde, hauseigenes Schwimmbad mit Babyschwimmen und Schwimmkursen. Familienbetrieb seit 1977.',
    tel='05951 1266', tel_i='+4959511266', mail='mail@reha-zentrum-meiners.de', adresse='Loruper Straße 21, 49757 Werlte', google=('4,7', 143),
    cta='Termin vereinbaren', nav=[('Kurse', 'kurse'), ('Rundgang', 'film'), ('Über uns', 'ueber'), ('Akut', 'akut'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '07:30 – 20:00'), ('Fr', '07:30 – 14:00')],
    form_opts=['Physiotherapie-Termin', 'Akutsprechstunde', 'Babyschwimmen', 'Schwimmkurs', 'Aquafitness / Funktionstraining', 'Bewerbung'], form_h3='Termin anfragen', form_p='Wir melden uns schnellstmöglich bei Ihnen.', form_btn='Anfrage senden',
    kt_ey='Kontakt', kt_h2='Wir sind <em>für Sie da.</em>', kt_p='Rufen Sie an oder schicken Sie uns Ihre Anfrage – auch für Kurs-Warteplätze.',
    social=[('Instagram', 'https://www.instagram.com/reha_zentrum_meiners')], rv_h2='Das sagen <em>unsere Patienten.</em>',
    bot=dict(name='Mia', tag='Ihre Reha-Begleiterin', hello='Hallo! Ich bin Mia. Soll ich Ihnen das Reha-Zentrum Meiners kurz zeigen?', hi='Hallo! Ich bin Mia vom Reha-Zentrum Meiners. Wobei darf ich helfen?',
             qa=[['Akutsprechstunde?', 'Ja – für Säuglinge, Kinder, Jugendliche und Erwachsene. Rufen Sie an: 05951 1266.'], ['Schwimmbad', 'Unser hauseigenes Schwimmbad hat 32 °C Wassertemperatur.'], ['Kurse', 'Babyschwimmen, Seepferdchen, Bronze, Aquafitness, Funktionstraining und T-RENA.'], ['Öffnungszeiten', 'Mo–Do 7:30–20 Uhr, Fr 7:30–14 Uhr.']],
             tour=[['#kurse'], ['#film'], ['#ueber'], ['#kontakt']]),
    vars='--bg:#F6FBFB;--ink:#0B2D3B;--mute:#4A6670;--p:#0E8FA0;--a:#0E8FA0;--a-ink:#fff;--s2:#E5F3F4;--fh:"Fraunces",Georgia,serif;--fb:"DM Sans",system-ui,sans-serif;--r:22px;--r2:32px;--mq-bg:#0B2D3B;--mq-ink:#9EE3EA;--logo-h:60px;--ft-bg:#082430;--hero-ov:linear-gradient(100deg,rgba(6,38,50,.85) 0%,rgba(6,38,50,.45) 50%,rgba(6,38,50,.05) 100%)',
    css='''.hs h1,.h2{font-weight:600;letter-spacing:-.02em}.hs h1 em,.h2 em{font-style:italic;color:#7FE0E8}.h2 em{color:var(--p)}
.hd .logo img{background:#fff;border-radius:50%;padding:3px}.ft img{background:#fff;border-radius:50%;padding:3px;height:64px}
.hs::after{content:"";position:absolute;left:0;right:0;bottom:-2px;height:70px;z-index:2;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 70' preserveAspectRatio='none'%3E%3Cpath d='M0 40 C240 0 480 70 720 40 S1200 10 1440 40 V70 H0Z' fill='%230B2D3B'/%3E%3C/svg%3E") center/100% 100%}
.hs .w{padding-bottom:100px}''',
    img={'logo.png': ('logos/meiners.png', 140), 'loop.mp4': ('vid/meiners-loop.mp4', 0), 'h-pool.jpg': ('meiners/img/i075.webp', 0), 'h-therapie.jpg': ('meiners/img/i073.webp', 0),
         'k-baby.jpg': ('meiners/img/i043.webp', 0), 'k-seepferd.jpg': ('meiners/img/i068.webp', 0), 'k-bronze.jpg': ('meiners/img/i069.webp', 900), 'k-aqua.jpg': ('meiners/img/i063.webp', 900),
         'k-funktion.jpg': ('meiners/img/i062.webp', 900), 'k-trena.jpg': ('meiners/img/i064.webp', 900), 'film.mp4': ('vid/meiners-film.mp4', 0), 'film.jpg': ('vid/meiners-poster.jpg', 0),
         'familie.jpg': ('meiners/img/i057.webp', 0), 'akut.jpg': ('meiners/img/i058.webp', 0)},
    body=b_meiners)

# ───────────────────────── 7. Happiness Studio Werlte ─────────────────────────
def b_happiness(s):
    return (hd(s, light=False) + hero_comp(s, dict(imgs=['jana.jpg', 'raum.jpg', 'schalen.jpg'], pos0='50% 25%',
        ey='Yoga · Rückbildung · Entspannung · im Herzen von Werlte', h1='Dein Glück <em>beginnt in dir.</em>',
        sub='Ein Ort für Tiefe, Erdung und Leichtigkeit: Yoga für Frauen, Mama und Baby und alle, die zur Ruhe kommen wollen – ohne Leistungsdruck.',
        badge=('5,0 ★', '13 Google-Bewertungen'), alt='Jana im Happiness Studio'))
        + marquee(['FemVitalYoga®', 'Mamasté', 'Sanfte Tiefe', 'Weekend Yoga', 'Pränatal', 'Postnatal', 'Workshops', 'Einzelcoaching'])
        + scroller('kurse', 'Kurse', 'Finde deinen <em>Lieblingskurs.</em>', 'Kleine Gruppen, 70 Minuten nur für dich – Vorkenntnisse brauchst du nicht.', [
            ('FemVitalYoga®', 'k-fem.jpg', 'Yoga, Kraftübungen und Entspannung: stärkt Muskeln, fördert Beweglichkeit und schenkt neue Energie.', '50% 30%'),
            ('Mamasté', 'k-mama.jpg', 'Liebevolle Begleitung für Mama und Baby – Beckenboden und Körpermitte stärken. Das Baby darf mit.', '50% 0%'),
            ('Sanfte Tiefe', 'k-tiefe.jpg', 'Yin Yoga, myofasziales Yoga und Hatha: entschleunigen, erden, loslassen – in deinem Tempo.', '50% 50%'),
            ('Weekend Yoga', 'k-weekend.jpg', 'Kleine Auszeit am Wochenende – anfängerfreundlich und für jeden geeignet.', '50% 40%')], 'alt')
        + story('ueber', 'Über mich', 'Hey, ich bin <em>Jana.</em>', [
            'Mama einer kleinen Tochter, Ehefrau, Naturmensch – und eine Seele, die in der Stille aufblüht. Ich liebe es, Momente zu schaffen, in denen Menschen wieder ganz bei sich ankommen.',
            'Ich verbinde die Weisheiten aus Ayurveda, TCM und Yoga mit dem Fortschritt der Schulmedizin. Ganzheitlichkeit heißt für mich, verschiedene Welten zusammenzuführen.'],
            'jana2.jpg', cap='Jana, Happiness Studio Werlte')
        + gallery('studio', 'Das Studio', 'Ankommen. <em>Durchatmen.</em>', [('g1.jpg', 'h2r', '50% 50%'), ('g2.jpg', 'w2', '50% 60%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 5%'), ('g5.jpg', 'h2r', '50% 30%'), ('g6.jpg', 'w2', '50% 50%')], 'alt')
        + reviews(s, ['Wir haben einen Mädelstag gebucht: schnelle, hilfreiche Antworten – und Jana hat besondere Rituale und Überraschungen rund um die Yogastunde geplant.', 'Eine schöne, entspannte Atmosphäre. Janas Kurse machen einfach Spaß – sie ist herzlich und gibt jedem ein gutes Gefühl.', 'Prä- und Postnatal-Yoga bei Jana: Ich habe mich immer rundum wohlgefühlt und nie als Störung.', 'Mein erstes Yoga überhaupt – sie erklärt alles verständlich und schaut, dass jeder die Übungen richtig macht.'])
        + steps('So einfach geht’s', 'Deine Matte <em>wartet schon.</em>', [('Kurs aussuchen', 'FemVitalYoga, Mamasté, Sanfte Tiefe oder Weekend Yoga.'), ('Platz buchen', 'Online oder einfach anrufen: 01515 3528628.'), ('Ankommen', 'Matte ausrollen, durchatmen – alles andere ist schon da.')], 'alt')
        + contact(s) + footer(s))

SITES['happiness'] = dict(
    slug='happiness-studio-werlte', firma='Happiness Studio Werlte', web='happiness-studio-werlte.de', fonts='r11happiness', du=True,
    title='Happiness Studio Werlte – Yoga, Mamasté & Entspannung', desc='Happiness Studio im Herzen von Werlte: FemVitalYoga, Mamasté für Mama und Baby, Sanfte Tiefe und Weekend Yoga. Dein Glück beginnt in dir.',
    tel='01515 3528628', tel_i='+4915153528628', mail='info@happiness-studio.de', adresse='Marktstraße 2, 49757 Werlte', google=('5,0', 13),
    cta='Platz buchen', nav=[('Kurse', 'kurse'), ('Über mich', 'ueber'), ('Studio', 'studio'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Erreichbar Mo – Fr', '08:00 – 20:00'), ('Sa', '09:00 – 14:00'), ('Studio', 'zu den Kurszeiten geöffnet')],
    form_opts=['FemVitalYoga®', 'Mamasté', 'Sanfte Tiefe', 'Weekend Yoga', 'Workshop / Mädelstag', 'Einzelcoaching'], form_h3='Platz anfragen', form_p='Schreib mir, ich melde mich persönlich bei dir.', form_btn='Anfrage senden',
    kt_ey='Kontakt', kt_h2='Kontaktiere <em>mich gerne.</em>', kt_p='Ob Kursplatz, Mädelstag oder Einzelcoaching – ich freue mich auf deine Nachricht.',
    rv_h2='Das sagen <em>meine Teilnehmerinnen.</em>',
    bot=dict(name='Lotta', tag='Deine Studio-Begleiterin', hello='Hallo! Ich bin Lotta. Soll ich dir zeigen, welcher Kurs zu dir passt?', hi='Hallo! Ich bin Lotta vom Happiness Studio. Was möchtest du wissen?',
             qa=[['Welcher Kurs passt?', 'FemVitalYoga für Kraft und Entspannung, Mamasté nach der Geburt, Sanfte Tiefe zum Entschleunigen, Weekend Yoga als Auszeit.'], ['Vorkenntnisse?', 'Brauchst du nicht – die Kurse sind Level 1 und bauen aufeinander auf.'], ['Mit Baby?', 'Ja, im Mamasté-Kurs darf dein Baby dabei sein.'], ['Kontakt', 'Telefon 01515 3528628 oder info@happiness-studio.de']],
             tour=[['#kurse'], ['#ueber'], ['#studio'], ['#kontakt']]),
    vars='--bg:#FAF6F1;--ink:#3A2E27;--mute:#7A6A5F;--p:#B0704F;--a:#3A2E27;--a-ink:#FAF6F1;--s:#fff;--s2:#F1E8DE;--fh:"Cormorant",Georgia,serif;--fb:"Mulish",system-ui,sans-serif;--r:24px;--r2:200px 200px 24px 24px;--mq-bg:#EADBCB;--mq-ink:#3A2E27;--logo-h:58px;--ft-bg:#2E241E;--hp-bg:#FAF6F1',
    css='''.hp h1,.h2{font-weight:500;letter-spacing:-.01em;line-height:1.02}.hp h1{font-size:clamp(54px,6.6vw,104px)}.hp h1 em,.h2 em{font-style:italic;color:var(--p)}
.comp .c1{inset:0 22% 0 6%;border-radius:999px 999px 30px 30px}.comp .c2{width:40%;height:40%;border-radius:50%;right:0;bottom:4%}.comp .c3{width:30%;height:30%;border-radius:50%;left:-2%;right:auto;top:auto;bottom:10%}
.comp .badge{left:auto;right:4%;top:4%;bottom:auto}
.mq{font-family:var(--fh);font-style:italic;font-weight:500;font-size:clamp(22px,2.4vw,32px)}
.sc .cd{border-radius:24px}.sc .cd figure{aspect-ratio:3/3.6}.st figure{border-radius:300px 300px 30px 30px}
.gl .grid figure{border-radius:24px}.btn{font-weight:600;letter-spacing:.02em}
.ft img{filter:invert(1)}''',
    img={'logo.png': ('logos/happiness-logo.png', 360), 'jana.jpg': ('happiness/img/i012.webp', 0), 'raum.jpg': ('happiness/img/i015.webp', 900), 'schalen.jpg': ('happiness/img/i008.jpeg', 800),
         'k-fem.jpg': ('happiness/img/i006.jpeg', 0), 'k-mama.jpg': ('happiness/img/i019.webp', 0, (0, 0, .6, 1)), 'k-tiefe.jpg': ('happiness/img/i021.webp', 0), 'k-weekend.jpg': ('happiness/img/i024.webp', 0),
         'jana2.jpg': ('happiness/img/i017.webp', 0), 'g1.jpg': ('happiness/img/i004.jpeg', 900), 'g2.jpg': ('happiness/img/i015.webp', 1200), 'g3.jpg': ('happiness/img/i013.webp', 700),
         'g4.jpg': ('happiness/img/i016.webp', 700), 'g5.jpg': ('happiness/img/i022.webp', 700), 'g6.jpg': ('happiness/img/i008.jpeg', 1000)},
    body=b_happiness)

# ───────────────────────── 8. INBalance Aktiv & Gesund Lastrup ─────────────────────────
def b_inbalance(s):
    return (hd(s) + hero_slides(s, dict(slides=['h-team.jpg', 'h-messung.jpg', 'h-training.jpg'], pos={'h-team.jpg': '55% 40%'},
        ey='INBalance Aktiv & Gesund · Lastrup', h1='Schmerzfrei. Beweglich. <em>In Balance.</em>',
        sub='Wir helfen Menschen, Schmerzen loszuwerden, beweglicher zu werden, nachhaltig Gewicht zu verlieren und sich ausgeglichener zu fühlen – mit der INBalance METHODE®.',
        ubar=[('Persönliche Betreuung', 'Immer mindestens ein Sporttherapeut vor Ort'), ('Milon-Zirkel', 'Geräte speichern Ihre Einstellung auf Chipkarte'), ('Kostenfreier Infotermin', 'Analyse statt Ratespiel')]))
        + panels('konzepte', 'Unsere Konzepte', 'Lösungen für <em>Volkskrankheiten.</em>', 'Bluthochdruck, Arthrose, Osteoporose, Diabetes II und mehr – für jedes Ziel ein eigenes Programm.', [
            ('Rücken & Gelenke', 'c-ruecken.jpg', 'Beweglich & Stark®: Wir suchen die Ursache, damit Sie sich endlich wieder schmerzfrei bewegen – bei Bandscheibe, Hüfte und Knie.', '50% 40%'),
            ('Energie & Kraft', 'c-kraft.jpg', 'Ab dem 30. Lebensjahr verlieren wir Muskelkraft. Bei uns tanken Sie wieder Kraft und Energie.', '50% 40%'),
            ('Abnehmen & Ernährung', 'c-abnehmen.jpg', 'Stoffwechsel in Balance®: gezielt abnehmen mit kontrolliertem Stoffwechseltraining und Ernährungsberatung.', '50% 40%'),
            ('Herz & Kreislauf', 'c-herz.jpg', 'Herz-Kreislauf Balance®: sicher und aktiv – mit professioneller Anamnese und Stoffwechselanalyse.', '50% 40%'),
            ('Beckenboden', 'c-becken.jpg', 'BeckenbodenStärke® mit dem EMP Chair – das Beckenbodenkonzept für Frauen und Männer.', '50% 30%')], 'dk')
        + video('methode', 'Die INBalance METHODE®', 'So funktioniert <em>Ihr Weg zu uns.</em>', 'Persönliche Betreuung, individuelle Analyse, gezieltes Training und bewusste Regeneration – im Film erklärt.', 'film.mp4', 'film.jpg')
        + story('ueber', 'Das INBalance', 'Persönlich und <em>familiär.</em>', [
            'Wenn es um Sport und Gesundheit geht, wollen wir der persönliche Ansprechpartner in Ihrer Nähe sein: Gesundheitstraining, Schmerzbehandlungen, Fitness- und Faszientraining.',
            'Inhaber Stefan Backhaus und Studioleiterin Sandra führen ein Team aus Trainern, Sportwissenschaftlern und Fitness-Betriebswirten – mit Herz und Leidenschaft.'],
            'team.jpg', cap='Das Team des INBalance', cls='alt')
        + '<section class="sec dk" style="padding:70px 0"><div class="w">' + numbers([('4,9', 'Sterne bei Google'), ('93', 'Google-Bewertungen'), ('5', 'eigene Gesundheitskonzepte'), ('1', 'Ansprechpartner für alles')]) + '</div></section>'
        + reviews(s, ['Mit 77 könnte ich mich ohne das regelmäßige Training hier nicht so gut bewegen – dafür fahre ich extra aus Cloppenburg.', 'Mit starken Rückenschmerzen gekommen, mit persönlichem Trainingsplan im Milon-Zirkel geblieben. Heute fühle ich mich fantastisch.', 'Hier steht die Gesundheit wirklich an erster Stelle. Jedes Gerät ist individuell eingestellt.', 'Liebevoll eingerichtet – und so viel Herzlichkeit beim Empfang. Man fühlt sich sofort gut aufgehoben.'])
        + steps('Ihr Start', 'Erst verstehen, <em>dann trainieren.</em>', [('Kostenfreier Infotermin', 'Wir lernen uns kennen und klären Ihr Ziel.'), ('Anamnese & Analyse', 'Gründliche Gesundheits- und Stoffwechselanalyse.'), ('Ihr Programm', 'Training, Ernährung und Regeneration – betreut.')], 'dk')
        + contact(s) + footer(s) + pop(dict(img='h-messung.jpg', ey='Kostenfreier Infotermin', h='Was braucht Ihr Körper?', p='Lassen Sie sich unverbindlich beraten – mit Analyse.', btn='Infotermin vereinbaren')))

SITES['inbalance'] = dict(
    slug='inbalance-aktiv-gesund-lastrup', firma='INBalance Aktiv & Gesund', web='in-balance-aktiv.de', fonts='r11inbalance',
    title='INBalance Aktiv & Gesund – Gesundheitsstudio in Lastrup', desc='INBalance Aktiv & Gesund in Lastrup: Rücken & Gelenke, Abnehmen, Herz-Kreislauf, Beckenboden. Kostenfreier Infotermin.',
    tel='04472 947978', tel_i='+494472947978', mail='backhaus@in-balance-aktiv.de', adresse='Pegasusstraße 2a, 49688 Lastrup', google=('4,9', 93),
    cta='Infotermin vereinbaren', nav=[('Konzepte', 'konzepte'), ('Methode', 'methode'), ('Über uns', 'ueber'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo, Mi', '07:00 – 11:30, 14:30 – 21:00'), ('Di', '08:00 – 11:30, 14:30 – 21:00'), ('Do', '14:30 – 21:00'), ('Fr', '07:00 – 11:30, 14:30 – 20:30'), ('Sa', '08:00 – 11:30')],
    form_opts=['Kostenfreier Infotermin', 'Rücken & Gelenke', 'Abnehmen & Ernährung', 'Herz & Kreislauf', 'Beckenboden', 'Firmenfitness'], form_h3='Infotermin vereinbaren', form_p='Kostenfrei und unverbindlich – wir melden uns.', form_btn='Termin anfragen',
    kt_ey='Kontakt', kt_h2='Herzlich willkommen <em>in Lastrup.</em>', kt_p='Interesse? Dann freut sich das ganze Team auf Sie.',
    social=[('Instagram', 'https://www.instagram.com/inbalancelastrup/'), ('Facebook', 'https://www.facebook.com/in.balance.lastrup/')],
    bot=dict(name='Balu', tag='Ihr Gesundheits-Guide', hello='Hallo! Ich bin Balu. Soll ich Ihnen zeigen, welches INBalance-Konzept zu Ihnen passt?', hi='Hallo! Ich bin Balu vom INBalance. Wobei darf ich helfen?',
             qa=[['Rückenschmerzen?', 'Dafür gibt es Beweglich & Stark® – unser Rücken- und Gelenkkonzept.'], ['Abnehmen?', 'Stoffwechsel in Balance®: Stoffwechseltraining plus Ernährungsberatung.'], ['Infotermin', 'Der Infotermin ist kostenfrei. Rufen Sie an: 04472 947978.'], ['Firmenfitness', 'Ja – mit individueller Beratung vor Ort und Gesundheitsnetzwerk.']],
             tour=[['#konzepte'], ['#methode'], ['#ueber'], ['#kontakt']]),
    vars='--bg:#fff;--ink:#16211B;--mute:#55625A;--p:#E8730C;--a:#F07F12;--a-ink:#fff;--dk:#16211B;--s2:#F4F2EC;--fh:"Unbounded",system-ui,sans-serif;--fb:"Manrope",system-ui,sans-serif;--r:16px;--r2:24px;--hd-bg:rgba(22,33,27,.92);--hd-ink:#fff;--logo-h:48px;--ft-bg:#101813;--hero-ov:linear-gradient(100deg,rgba(16,24,19,.9) 0%,rgba(16,24,19,.55) 50%,rgba(16,24,19,.1) 100%)',
    css='''.hs h1{font-size:clamp(40px,5.6vw,86px);font-weight:700}.h2{font-weight:700;font-size:clamp(30px,3.6vw,52px)}
.hs h1 em{color:#B9D24A}.dk .h2 em{color:#B9D24A}
.hd .logo img,.ft img{background:#fff;border-radius:10px;padding:4px 8px}
.ap .pn h3{font-size:clamp(17px,1.4vw,22px)}''',
    img={'logo.png': ('logos/inbalance.webp', 300), 'h-team.jpg': ('inbalance/img/i041.jpg', 2200), 'h-messung.jpg': ('inbalance/img/i042.jpg', 2200), 'h-training.jpg': ('inbalance/img/i043.jpg', 2200),
         'c-ruecken.jpg': ('inbalance/img/i026.jpeg', 0), 'c-kraft.jpg': ('inbalance/img/i025.jpeg', 0), 'c-abnehmen.jpg': ('inbalance/img/i028.jpeg', 0), 'c-herz.jpg': ('inbalance/img/i046.jpg', 0),
         'c-becken.jpg': ('inbalance/img/i038.webp', 0), 'film.mp4': ('vid/inbalance-film.mp4', 0), 'film.jpg': ('vid/inbalance-poster.jpg', 0), 'team.jpg': ('inbalance/img/i048.jpg', 0)},
    body=b_inbalance)

# ───────────────────────── 9. Prime Sportclub Löningen ─────────────────────────
def b_prime(s):
    return (hd(s) + hero_slides(s, dict(slides=['h-hantel.jpg', 'h-kettle.jpg', 'h-kurs.jpg'], big='PRIME', pos={'h-hantel.jpg': '70% 40%'},
        ey='Prime Sportclub · Löningen · Roevenkamp 12', h1='Lass dich <em>inspirieren.</em>',
        sub='EGYM-Zirkel, Kraft und Cardio, Reha-Sport, Kindersport, Sauna – und in Löningen 300 m² nur für HYROX. Willkommen im Club.',
        ubar=[('HYROX Löningen', '300 m² wettkampforientierter Trainingsbereich'), ('EGYM', 'Nur 2 × 30 Minuten pro Woche'), ('Reha & Prävention', 'In Kooperation mit allen gesetzlichen Krankenkassen')]))
        + marquee(['HYROX', 'EGYM', 'Krafttraining', 'Cardio', 'Funktionales Training', 'Reha-Sport', 'Kindersport', 'Sauna', 'Solarium', 'Hansefit'], 'gold')
        + story('hyrox', 'HYROX Trainingsraum Löningen', '300 m² für deinen <em>nächsten Wettkampf.</em>', [
            'Ein speziell für HYROX konzipierter Trainingsbereich mit wettkampforientierter Ausstattung – egal, ob du deine ersten HYROX-Erfahrungen sammelst oder dich gezielt vorbereitest.'],
            'hyrox.jpg', cap='Prime Sportclub', extra='<div class="op"><span>HYROX-Gruppenkurse</span><span>Einzelstunden</span><span>Wettkampfvorbereitung</span><span>Freies Training</span></div>', cls='dk')
        + panels('leistungen', 'Leistungen', 'Alles für <em>deinen Körper.</em>', 'Fahr über die Bereiche.', [
            ('EGYM', 'p-egym.jpg', 'Elektronischer Zirkel mit automatischer Einstellung und regelmäßiger Kraftmessung – nur 2 × 30 Minuten sorgen für wahre Wunder.', '50% 40%'),
            ('Krafttraining', 'p-kraft.jpg', 'Körper definieren – wir wissen, wie es geht.', '60% 40%'),
            ('Reha-Sport', 'p-reha.jpg', 'Zurück in ein bewegliches Leben – zugeschnitten auf dein Beschwerdebild. Neue Reha-Sport-Gruppen in Löningen.', '50% 40%'),
            ('Kindersport', 'p-kinder.jpg', 'Spaß und Freude an der Bewegung durch vielfältige Kursinhalte.', '50% 40%'),
            ('Kurse', 'p-kurs.jpg', 'Funktionales Training, World Jumping und mehr – such dir deinen Prime-Kursplan aus.', '50% 40%'),
            ('Sauna', 'p-sauna.jpg', 'Damen-, Herren- und gemischte Saunatage – auch für geschlossene Gesellschaften buchbar.', '50% 50%')], 'dk')
        + reviews(s, ['Ich bin LKW-Fahrer und zum ersten Mal in einem Studio, in dem alles auf den ersten Blick klar ist: tolle Atmosphäre, sauber, echte Profis.', 'Seit Januar 2024 Mitglied: Nach einer Pause wurden wir mit „Schön, dass ihr wieder da seid“ begrüßt. Immer sauber und ordentlich.', 'Die Geräte sind gut und decken alles ab, was ich brauche.', 'Top!'], 'dk')
        + steps('So startest du', 'Dein Weg in den <em>Club.</em>', [('Probetraining vereinbaren', 'Ruf an unter 05432 9054158 oder nutz das Formular.'), ('Kennenlernen', 'Wir zeigen dir Geräte, Kurse und den HYROX-Bereich.'), ('Durchstarten', 'Mit Plan, Team und Club-Atmosphäre.')], 'dk')
        + contact(s, 'dk') + footer(s) + pop(dict(img='hyrox.jpg', ey='HYROX Löningen', h='Bereit für deinen ersten Wettkampf?', p='Gruppenkurse, Einzelstunden und Wettkampfvorbereitung.', btn='Probetraining sichern')))

SITES['prime'] = dict(
    slug='prime-sportclub-loeningen', firma='Prime Sportclub Löningen', web='prime-sportclub.de', fonts='r11prime', du=True,
    title='Prime Sportclub Löningen – Fitness, EGYM & HYROX', desc='Prime Sportclub in Löningen: HYROX-Trainingsraum, EGYM, Krafttraining, Reha-Sport, Kindersport und Sauna.',
    tel='05432 9054158', tel_i='+4954329054158', adresse='Roevenkamp 12, 49624 Löningen', google=('4,7', 89),
    cta='Probetraining sichern', nav=[('HYROX', 'hyrox'), ('Leistungen', 'leistungen'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 22:00'), ('Sa + So', '08:00 – 16:00'), ('Feiertage', '09:00 – 13:00')],
    form_opts=['Probetraining', 'HYROX', 'EGYM', 'Reha-Sport', 'Kindersport', 'Sauna'], form_h3='Probetraining sichern', form_p='Hinterlass deine Nummer, wir melden uns.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Werde Teil <em>des Clubs.</em>', kt_p='Ruf an oder schreib uns – wir finden einen Termin für dein Probetraining.',
    social=[('Instagram', 'https://www.instagram.com/prime.sportclub')],
    bot=dict(name='Leo', tag='Dein Club-Guide', hello='Hey! Ich bin Leo. Soll ich dir kurz den Prime Sportclub zeigen?', hi='Hey! Ich bin Leo vom Prime Sportclub. Was möchtest du wissen?',
             qa=[['HYROX?', 'In Löningen gibt es 300 m² nur für HYROX – mit Gruppenkursen, Einzelstunden und Wettkampfvorbereitung.'], ['EGYM?', 'Der elektronische Zirkel stellt sich automatisch ein – nur 2 × 30 Minuten pro Woche.'], ['Öffnungszeiten', 'Mo–Fr 8–22 Uhr, Sa + So 8–16 Uhr, Feiertage 9–13 Uhr.'], ['Probetraining', 'Ruf an unter 05432 9054158.']],
             tour=[['#hyrox'], ['#leistungen'], ['#kontakt']]),
    vars='--bg:#0B0B0C;--ink:#F3EFE6;--mute:#ABA596;--p:#C9A34E;--a:#D4AF5A;--a-ink:#141108;--dk:#0B0B0C;--s:#17171A;--s2:#121214;--line:rgba(255,255,255,.1);--fh:"Cinzel",Georgia,serif;--fb:"Rubik",system-ui,sans-serif;--r:2px;--r2:2px;--br:2px;--hd-bg:rgba(11,11,12,.92);--hd-ink:#fff;--mq-bg:#C9A34E;--mq-ink:#0B0B0C;--logo-h:64px;--ft-bg:#060606',
    css='''.hs h1,.h2{font-weight:700;letter-spacing:.02em;text-transform:uppercase}.hs h1{font-size:clamp(48px,6.4vw,100px)}
.hs .big{font-family:var(--fh);-webkit-text-stroke:1.5px rgba(212,175,90,.35)}
.btn{text-transform:uppercase;letter-spacing:.08em;font-size:14px}
.ap .pn{border:1px solid rgba(212,175,90,.25)}.ap .pn h3{text-transform:uppercase;letter-spacing:.06em}
.kt .fm input,.kt .fm select,.kt .fm textarea{background:#0e0e10;color:#fff;border-color:rgba(255,255,255,.15)}
.rv .cd{border:1px solid rgba(212,175,90,.2)}''',
    img={'logo.png': ('prime/img/i043.png', 260, (0, .3, 1, .7)), 'h-hantel.jpg': ('prime/img/i030.jpg', 2000), 'h-kettle.jpg': ('prime/img/i027.jpg', 2000), 'h-kurs.jpg': ('prime/img/i031.jpg', 2000),
         'hyrox.jpg': ('prime/img/i042.jpg', 1400), 'p-egym.jpg': ('prime/img/i040.jpg', 1200), 'p-kraft.jpg': ('prime/img/i026.jpg', 1200), 'p-reha.jpg': ('prime/img/i028.jpg', 1200),
         'p-kinder.jpg': ('prime/img/i014.jpg', 0), 'p-kurs.jpg': ('prime/img/i031.jpg', 1200), 'p-sauna.jpg': ('prime/img/i039.jpg', 1200)},
    body=b_prime)

# ───────────────────────── 10. Fitness Freunde Lindern ─────────────────────────
def b_freunde(s):
    return (hd(s) + hero_slides(s, dict(slides=['h-lauf.jpg', 'h-hantel.jpg'], big='24/7', pos={'h-hantel.jpg': '50% 25%'},
        ey='Fitness Freunde · Lindern · rund um die Uhr', h1='Dein Studio. <em>Deine Zeit.</em>',
        sub='Trainiere 24 Stunden am Tag, 7 Tage die Woche – mit modernen Matrix-Geräten, Trainings-App und Getränken inklusive. Erst 14 Tage testen, dann entscheiden.',
        ubar=[('24/7 geöffnet', 'Check-in per App – Licht und Sound schalten automatisch'), ('14 Tage testen', 'Widerruf in der Testphase kostet nichts'), ('Matrix-Geräte', 'Vom Marktführer für Studiogeräte')]))
        + marquee(['Kraft', 'Cardio', 'Functional', 'Calisthenics', 'Dehnen', 'Gesundheitssport', 'Geräte', '24/7'], 'neon')
        + scroller('angebot', 'Unser Angebot', 'Training für <em>jedes Ziel.</em>', 'Muskeln, Ausdauer, Abnehmen, Alltagsfitness, Gesundheit im Alter und Beweglichkeit.', [
            ('Kraft', 'a-kraft.jpg', 'Freihanteln und Geräte für Muskelaufbau und Kraftausdauer.', '50% 30%'),
            ('Cardio', 'a-cardio.jpg', 'Laufbänder & Co. – Ausdauer, wann immer du Zeit hast.', '50% 0%'),
            ('Functional', 'a-functional.jpg', 'Ropes, Ganzkörper, Athletik – Training, das im Alltag zählt.', '50% 30%'),
            ('Calisthenics', 'a-cali.jpg', 'Das eigene Körpergewicht als Trainingsgerät.', '50% 20%'),
            ('Gesundheitssport', 'a-gesund.jpg', 'Sanft, gelenkschonend und für jedes Alter.', '50% 20%')])
        + faq('Deine Vorteile', 'Fitness, <em>ganz ohne Haken.</em>', [
            ('24/7 Öffnungszeiten', 'Unser Studio ist personallos gesteuert: Über ein innovatives Check-in-System werden Licht, Sound und Videoüberwachung gesteuert – du trainierst, wann du willst.'),
            ('Ausstattung des Studios', 'Moderne, voll automatisierte Fläche mit den neuesten Geräten der Marke Matrix – für jede Zielgruppe angepasst.'),
            ('Betreuung trotz 24/7', 'Kein Personal heißt nicht keine Beratung: Über die App und viele Kontaktwege reagieren wir schnell und zuverlässig. Einweisungen buchst du einfach in der App.'),
            ('Transparente Verträge', 'Keine versteckten Nebenbedingungen. Alle Verträge außer der Tageskarte haben eine 14-tägige Testphase – widerrufst du darin, entstehen keine Kosten.'),
            ('Nie im Studio gewesen?', 'Super Entscheidung! Für deine Einweisung steht qualifiziertes Personal bereit – Termin unkompliziert per App buchen.')], 'dk')
        + reviews(s, ['Modern und rund um die Uhr geöffnet. Besonders die Sauberkeit: Egal ob früh morgens oder spät abends – immer ordentlich.', 'So ein sauberes und aufgeräumtes Studio habe ich noch nie gesehen. Tolle Atmosphäre und kompetente Trainer.', 'Wasser jederzeit kalt nachfüllen – mit oder ohne Geschmack und Kohlensäure.', 'Super Studio!'])
        + steps('So startest du', 'In drei Schritten <em>Mitglied.</em>', [('Mitgliedschaft wählen', 'Online in wenigen Minuten.'), ('14 Tage testen', 'In Ruhe ausprobieren – ohne Risiko.'), ('Einweisung buchen', 'Per App – und dann rund um die Uhr trainieren.')])
        + contact(s, 'dk') + footer(s) + pop(dict(img='h-lauf.jpg', ey='14 Tage unverbindlich', h='Erst testen, dann entscheiden.', p='Widerrufst du in der Testphase, entstehen dir keine Kosten.', btn='Jetzt testen')))

SITES['freunde'] = dict(
    slug='fitness-freunde-lindern', firma='Fitness Freunde Lindern', web='fitnessfreunde.club', fonts='r11freunde', du=True,
    title='Fitness Freunde Lindern – 24/7 Fitnessstudio', desc='Fitness Freunde in Lindern: 24/7 geöffnet, moderne Matrix-Geräte, Trainings-App, Getränke inklusive. 14 Tage unverbindlich testen.',
    tel='info@fitnessfreunde.club', tel_i='mailto:info@fitnessfreunde.club', mail='Kontakt per App und E-Mail', adresse='Lastruper Straße 29, 49699 Lindern (Oldenburg)', google=('4,8', 47),
    cta='Jetzt Mitglied werden', nav=[('Angebot', 'angebot'), ('Vorteile', 'vorteile'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Täglich', '24 Stunden'), ('365 Tage', 'im Jahr')],
    form_opts=['Mitgliedschaft', 'Einweisung', 'Tageskarte', 'Frage zum Vertrag'], form_h3='Mitglied werden', form_p='Hinterlass deine Daten – wir melden uns bei dir.', form_btn='Anfrage senden',
    kt_ey='Kontakt', kt_h2='Bereit, <em>loszulegen?</em>', kt_p='Schreib uns – wir reagieren schnell. Oder komm einfach vorbei: Lastruper Straße 29.',
    bot=dict(name='Finn', tag='Dein 24/7-Guide', hello='Hey! Ich bin Finn. Soll ich dir zeigen, wie Fitness Freunde funktioniert?', hi='Hey! Ich bin Finn von Fitness Freunde. Was willst du wissen?',
             qa=[['Wirklich 24/7?', 'Ja – Check-in per System, Licht und Sound gehen automatisch an. Rund um die Uhr, 365 Tage.'], ['Probetraining?', 'Alle Verträge außer der Tageskarte haben 14 Tage Testphase – Widerruf darin kostet nichts.'], ['Einweisung?', 'Klar! Einfach über die App buchen.'], ['Getränke?', 'Inklusive: Wasser mit oder ohne Geschmack und Kohlensäure.']],
             tour=[['#angebot'], ['#vorteile'], ['#kontakt']]),
    vars='--bg:#F4F6F2;--ink:#0D100C;--mute:#4D554A;--p:#3DAA2B;--a:#7CE04A;--a-ink:#0D100C;--dk:#0D100C;--s2:#E7ECE3;--fh:"Space Grotesk",system-ui,sans-serif;--fb:"Inter Tight",system-ui,sans-serif;--r:14px;--r2:20px;--br:12px;--hd-bg:rgba(13,16,12,.92);--hd-ink:#fff;--mq-bg:#7CE04A;--mq-ink:#0D100C;--logo-h:44px;--ft-bg:#070907',
    css='''.hs h1,.h2{font-weight:700;letter-spacing:-.035em}.hs h1{font-size:clamp(52px,7vw,112px)}
.hs .big{font-family:var(--fh);-webkit-text-stroke:2px rgba(124,224,74,.35)}
.hs h1 em{color:#7CE04A}.dk .h2 em{color:#7CE04A}
.fq .it button::after{color:#7CE04A}''',
    img={'logo.png': ('freunde/img/i003.png', 400), 'h-lauf.jpg': ('freunde/img/i008.jpg', 0), 'h-hantel.jpg': ('freunde/img/i011.jpg', 1400),
         'a-kraft.jpg': ('freunde/img/i011.jpg', 800), 'a-cardio.jpg': ('freunde/img/i009.jpg', 0), 'a-functional.jpg': ('freunde/img/i005.jpg', 0), 'a-cali.jpg': ('freunde/img/i002.jpg', 0), 'a-gesund.jpg': ('freunde/img/i006.jpg', 0)},
    body=b_freunde)
