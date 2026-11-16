"""Runde 14 · Teil D: Mammen, Schulz, Moss, Christians, Kaiser."""
from common import *
SITES = {}

# ───────────── 16. Fahrschule Mammen, Cloppenburg & Umgebung ─────────────
def b_mammen(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 50%', quick=['auto', 'moto', 'anh', 'lkw'],
        ey='Fahrschule · Verkehrsakademie · MPU-Beratung · Cloppenburg',
        h1='Erst fahren. <em>Später zahlen.</em>',
        sub='Die Fahrschule Mammen bildet in Cloppenburg und sieben Orten drumherum aus. Mit Ratenzahlung, damit der Führerschein nicht am Geld scheitert, und mit MPU-Beratung, wenn es mal schiefgelaufen ist.',
        badge=('7 Orte', 'rund um Cloppenburg')))
        + marquee(['Klasse B', 'BE', 'A', 'CE', 'Ratenzahlung', 'Verkehrsakademie', 'MPU-Beratung', 'Aufbauseminare'], 'mm')
        + svc('angebot', 'Drei Bereiche', 'Fahrschule. Akademie. <em>Neustart.</em>', '', [
            ('Fahrschule', 'Auto, Anhänger, Motorrad und Lkw, mit Theorie in mehreren Orten rund um Cloppenburg.'),
            ('Verkehrsakademie', 'Seminare und Weiterbildung rund ums Fahren.'),
            ('MPU Hilfe &amp; Beratung', 'Führerschein weg? Wir beraten Sie zur MPU und begleiten Sie auf dem Weg zurück ans Steuer.'),
            ('Ratenzahlung', 'Flexibel und unkompliziert. Die Details klären wir persönlich.')])
        + promo('finanzierung', 'p-raten.jpg', 'Finanzierung', 'Der Führerschein darf <em>nicht am Geld scheitern.</em>', 'Bei uns ist Ratenzahlung möglich: flexibel und unkompliziert. Sie fangen an zu fahren und zahlen in Raten. Die Details klären wir persönlich mit Ihnen.', ['Ratenzahlung möglich', 'Flexibel &amp; unkompliziert', 'Persönliche Beratung'], 'Finanzierung anfragen', 'dk')
        + orte('standorte', 'Unsere Standorte', 'Finde jetzt <em>deine Fahrschule.</em>', 'Theorie in Cloppenburg mittwochs von 17:00 bis 18:30 und von 18:30 bis 20:00 Uhr, zwei Unterrichte an einem Tag.', [
            ('Cloppenburg', 'Eschstraße 1', 'Mi · 2 Unterrichte'), ('Altenoythe', '', ''), ('Bösel', '', ''), ('Garrel', '', ''), ('Markhausen', '', ''), ('Molbergen', '', ''), ('Sedelsberg', '', '')])
        + gallery('einblicke', 'Einblicke', 'Unsere Räume <em>in Cloppenburg.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', '', '50% 50%')], 'alt')
        + contact(s) + footer(s))

S = SITES['mammen'] = site(
    slug='fahrschule-mammen-cloppenburg', firma='Fahrschule Dirk Mammen', web='fahrschulemammen.de', fonts='r14mam', du=False,
    title='Fahrschule Mammen – Fahrschule, Verkehrsakademie & MPU-Beratung in Cloppenburg', desc='Fahrschule Mammen in Cloppenburg und Umgebung: Führerschein mit Ratenzahlung, Verkehrsakademie und MPU-Beratung. Sieben Standorte.',
    tel='04471 1767963', tel_i='+4944711767963', mail='info@fahrschule-mammen.de', adresse='Eschstraße 1, 49661 Cloppenburg', google=None,
    cta='Jetzt anmelden', nav=[('Angebot', 'angebot'), ('Finanzierung', 'finanzierung'), ('Standorte', 'standorte'), ('Einblicke', 'einblicke'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 16:00'), ('Theorie Mi', '17:00 – 20:00')],
    form_lbl='Interesse an', form_opts=['Auto · B', 'Anhänger · BE', 'Motorrad · A', 'Lkw · CE', 'Ratenzahlung', 'MPU-Beratung', 'Seminar'],
    form_orte=['Cloppenburg', 'Altenoythe', 'Bösel', 'Garrel', 'Markhausen', 'Molbergen', 'Sedelsberg'],
    form_h3='Anmeldung &amp; Beratung', form_p='Sagen Sie uns, was Sie brauchen. Wir melden uns persönlich.', form_btn='Anfrage senden',
    kt_ey='Kontakt', kt_h2='Wir sind <em>für Sie da.</em>', kt_p='Telefon 04471 1767963 oder 04494 922822.',
    vars='--bg:#f7f5f2;--ink:#121212;--mute:#5b5853;--p:#d0142c;--p-ink:#fff;--a:#d0142c;--a-ink:#fff;--dk:#121212;--s:#fff;--s2:#ece8e2;--fh:"Anton",Impact,sans-serif;--fb:"Karla",system-ui,sans-serif;--r:8px;--r2:12px;--br:4px;--mq-bg:#121212;--mq-ink:#fff;--hd-bg:rgba(247,245,242,.95);--hd-ink:#121212;--logo-h:42px;--ft-bg:#0b0b0b',
    css='''.hp h1,.h2{font-weight:400;text-transform:uppercase;letter-spacing:.01em;line-height:1.04;padding-top:4px}.hp h1 em,.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#ff5267}
.comp{height:360px}.comp .c1{width:62%}.promo figure{max-width:380px;justify-self:center}.gl .grid{grid-template-columns:repeat(4,1fr);grid-auto-rows:200px}.gl .grid .w2{grid-column:span 1}.hd .logo img{filter:none}.ft img{filter:invert(1)}.mq span{font-weight:400}''')
S['bot'] = BOT('Max', 'Ihr Mammen-Lotse', 'der Fahrschule Mammen', S, ['B', 'BE', 'A', 'A2', 'A1', 'CE', 'C'],
    {'schnell': 'Zwei Theorie-Unterrichte an einem Mittwoch: So kommen Sie zügig durch.', 'ruhe': 'Unsere Fahrschüler loben Fahrlehrer, die ruhig und ohne Stress erklären.', 'flex': 'Sieben Orte rund um Cloppenburg, da ist einer in Ihrer Nähe.', 'angst': 'Sprechen Sie es an. Wir erklären alles in Ruhe.'},
    qa=[('rate|finanz|bezahl|zahl', 'Bei uns ist Ratenzahlung möglich. Die Details klären wir persönlich mit Ihnen.'), ('mpu', 'Wir bieten MPU-Hilfe und Beratung an, sprechen Sie uns einfach an.')],
    tour=[('#angebot', 'Fahrschule und MPU-Beratung.'), ('#finanzierung', 'Ratenzahlung möglich.'), ('#standorte', 'Sieben Orte.'), ('#kontakt', 'Hier melden Sie sich an.')], du=False)
S['img'] = {'logo.png': ('mammen/img/i022.png', 0, 'alphacrop'), 'h1.jpg': ('mammen/img/i024.png', 0), 'h2.jpg': ('mammen/img/i021.webp', 0), 'h3.jpg': ('mammen/img/i010.png', 0),
    'd-fs.jpg': ('mammen/img/i003.png', 0), 'd-mpu.jpg': ('mammen/img/i004.png', 0), 'p-raten.jpg': ('mammen/img/i008.png', 0),
    'g1.jpg': ('mammen/img/i009.png', 0), 'g2.jpg': ('mammen/img/i005.png', 0), 'g3.jpg': ('mammen/img/i006.png', 0), 'g4.jpg': ('mammen/img/i007.png', 0), 'g5.jpg': ('mammen/img/i020.webp', 0), 'g6.jpg': ('mammen/img/i023.png', 0)}
S['body'] = b_mammen

# ───────────── 17. Fahrschule Schulz, Lohne & Vechta ─────────────
def b_schulz(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h-team.jpg'], pos={'h-team.jpg': '50% 60%'}, quick=['auto', 'moto', 'roller', 'anh', 'trak'],
        ey='Fahrschule Schulz · Inh. Björn Stratemann · Lohne &amp; Vechta',
        h1='Hier macht das Lernen <em>Spaß!</em>',
        sub='Theorie in gemütlicher Atmosphäre mit kostenlosen Snacks und Getränken, ein motiviertes Team, Fahrsimulator und App. In Lohne und Vechta, schnell und unkompliziert anmelden.',
        ubar=[('4,9 Sterne', 'bei Google in Lohne'), ('Snacks &amp; Getränke', 'gratis im Unterricht'), ('2 Standorte', 'Lohne und Vechta')]))
        + svc('vorteile', 'Darum Schulz', 'Bei uns fühlst du dich <em>wie zu Hause.</em>', 'Ein motiviertes Team, das dir alle Inhalte mit viel Spaß und anschaulichen Beispielen näherbringt.', [
            ('Gemütliche Theorie', 'Unterricht in unseren Schulungsräumen, inklusive kostenloser Snacks und Getränke.'),
            ('Fahrsimulator', 'Erst im Cockpit üben, dann auf die Straße.'),
            ('App fürs Handy', 'Lernen, wann und wo du willst.'),
            ('Schnell angemeldet', 'Einfach mit Ausweis vorbeikommen, fertig.')])
        + flotte('fuhrpark', 'Unser Fuhrpark', 'BMW, Honda, KTM <em>und mehr.</em>', 'Auf diesen Fahrzeugen lernst du bei uns.', [
            ('f-x1.jpg', 'BMW X1', 'Klasse B', '50% 55%'), ('f-flotte.jpg', 'Auto-Fuhrpark', 'Klasse B · BE', '50% 55%'), ('f-flotte2.jpg', 'Auto-Fuhrpark', 'Lohne &amp; Vechta', '50% 55%'),
            ('f-cb500.jpg', 'Honda CB 500', 'Klasse A2', '50% 55%'), ('f-duke.jpg', 'KTM 125 Duke', 'Klasse A1', '50% 55%'), ('f-bikes.jpg', 'Motorrad-Fuhrpark', 'Klasse A · A2 · A1', '50% 55%')], 'dk')
        + duo('standorte', 'Zwei Standorte', 'Lohne <em>und Vechta.</em>', 'Unterricht in gemütlicher Atmosphäre. Anmelden kannst du dich schnell und unkompliziert, bring bitte deinen Ausweis mit.', [
            ('Lohne', 'Deichstraße 14', 'd-lohne.jpg', 'Bürozeiten für Anmeldungen und Papierkram: Dienstag, Mittwoch und Donnerstag von 16:00 bis 18:30 Uhr. Weitere Termine nach Vereinbarung.', ['Di – Do 16:00 – 18:30'], 'In Lohne anmelden'),
            ('Vechta', 'Falkenrotterstraße 54', 'd-vechta.jpg', 'Bürozeiten für Anmeldungen und Papierkram: Montag und Mittwoch von 16:00 bis 18:30 Uhr. Weitere Termine nach Vereinbarung.', ['Mo &amp; Mi 16:00 – 18:30'], 'In Vechta anmelden')], 'alt')
        + promo('jobs', 'p-team.jpg', 'Hier ist noch Platz …', '… vielleicht <em>für dich!</em>', 'Wir suchen weitere Fahrlehrerinnen und Fahrlehrer. Bewirb dich jetzt bei einem Team, in dem das Arbeiten genauso Spaß macht wie das Lernen.', ['Fahrlehrer/innen gesucht', 'Lohne und Vechta'], 'Jetzt bewerben')
        + reviews(s, ['Ich kann die Fahrschule nur empfehlen! Freundlich, kompetent und geduldig. Besonders der Inhaber hat mich mit seiner ruhigen Art perfekt auf die Prüfung vorbereitet.',
                      'Die Fahrlehrer sind entspannt, erklären alles verständlich und man fühlt keinen Druck. Hat richtig Spaß gemacht.',
                      'Vor langer Zeit Auto hier gemacht, jetzt mit 50 noch den Motorradführerschein. Damals wie heute: Geduld und Verständnis.',
                      'Schnelle Rückmeldungen, freundliche Fahrlehrer, praktische Prüfung innerhalb eines Monats bestanden.'], 'dk')
        + contact(s) + footer(s))

S = SITES['schulz'] = site(
    slug='fahrschule-schulz-lohne', firma='Fahrschule Schulz Inh. Björn Stratemann', web='schulz-fahrschule.de', fonts='r14sch',
    title='Fahrschule Schulz – Hier macht das Lernen Spaß | Lohne & Vechta', desc='Fahrschule Schulz, Inh. Björn Stratemann, in Lohne und Vechta: Theorie mit kostenlosen Snacks, Fahrsimulator, App, BMW und Motorräder.',
    tel='0171 7805040', tel_i='+491717805040', mail='info@schulz-fahrschule.de', adresse='Deichstraße 14, 49393 Lohne', google=('4,9', 37),
    cta='Jetzt anmelden', nav=[('Vorteile', 'vorteile'), ('Fuhrpark', 'fuhrpark'), ('Standorte', 'standorte'), ('Jobs', 'jobs'), ('Kontakt', 'kontakt')],
    hours=[('Lohne Di – Do', '16:00 – 18:30'), ('Vechta Mo &amp; Mi', '16:00 – 18:30')],
    form_lbl='Führerschein', form_opts=['Auto · B', 'Anhänger · BE', 'Motorrad · A / A2 / A1', 'Roller · AM', 'Traktor · T', 'Bewerbung Fahrlehrer/in'],
    form_orte=['Lohne', 'Vechta'],
    form_h3='Anmelden', form_p='Wir melden uns bei dir. Ausweis bitte zur Anmeldung mitbringen.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf dich!</em>', kt_p='Björn Stratemann, Telefon 0171 7805040.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>', logo_txt='Fahrschule <b style="color:#e5007d">SCHULZ</b>',
    vars='--bg:#fff7fb;--ink:#141014;--mute:#5f5560;--p:#e5007d;--p-ink:#fff;--a:#e5007d;--a-ink:#fff;--dk:#141014;--s:#fff;--s2:#fbe6f1;--fh:"Poppins",system-ui,sans-serif;--fb:"Poppins",system-ui,sans-serif;--r:22px;--r2:30px;--br:999px;--mq-bg:#e5007d;--hd-bg:rgba(255,247,251,.95);--hd-ink:#141014;--ft-bg:#0d0a0d;--hero-ov:linear-gradient(90deg,rgba(20,16,20,.86) 0%,rgba(20,16,20,.45) 55%,rgba(20,16,20,.1) 90%)',
    css='''.hs h1,.h2{font-weight:800;letter-spacing:-.02em;line-height:1.05}.hs h1 em{font-style:normal;color:#ff5fb0}.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#ff5fb0}
.hd.lt .lt-logo{color:#fff}.hd.scr .lt-logo{color:var(--ink)}.lt-logo{font-weight:600;font-size:20px}''')
S['bot'] = BOT('Sunny', 'deine Schulz-Lotsin', 'der Fahrschule Schulz', S, ['B', 'BE', 'A', 'A2', 'A1', 'AM', 'T'],
    {'schnell': 'Schnell anmelden, Ausweis mitbringen, los. Unsere Fahrschüler haben die Praxisprüfung teils innerhalb eines Monats bestanden.', 'ruhe': 'Entspannte Fahrlehrer, kein Druck, und in der Theorie gibt es Snacks und Getränke.', 'flex': 'Zwei Standorte, Lohne und Vechta, weitere Termine nach Vereinbarung.', 'angst': 'Starte im Fahrsimulator, ganz ohne Verkehr.'},
    qa=[('snack|getränk|essen', 'Ja, im Unterricht gibt es kostenlose Snacks und Getränke.'), ('job|fahrlehrer|bewerb', 'Wir suchen Fahrlehrer/innen, bewirb dich gern.'), ('simulator', 'Im Fahrsimulator übst du vor der ersten Fahrstunde.')],
    tour=[('#vorteile', 'Darum Schulz.'), ('#fuhrpark', 'Unser Fuhrpark.'), ('#standorte', 'Lohne und Vechta.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'h-team.jpg': ('schulzv/img/i103.webp', 0), 'h-cars.jpg': ('schulzv/img/i042.webp', 0), 'h-bikes.jpg': ('schulzv/img/i015.webp', 0),
    'f-x1.jpg': ('schulzv/img/i041.webp', 0), 'f-flotte.jpg': ('schulzv/img/i042.webp', 0), 'f-flotte2.jpg': ('schulzv/img/i043.webp', 0),
    'f-cb500.jpg': ('schulzv/img/i014.webp', 0), 'f-duke.jpg': ('schulzv/img/i016.webp', 0), 'f-bikes.jpg': ('schulzv/img/i015.webp', 0),
    'd-lohne.jpg': ('schulzv/img/i025.webp', 0), 'd-vechta.jpg': ('schulzv/img/i024.webp', 0), 'p-team.jpg': ('schulzv/img/i106.webp', 0)}
S['body'] = b_schulz

# ───────────── 18. Fahrschule Moss, Vechta & Lohne ─────────────
def b_moss(s):
    return (hd(s) + hero_x(s, dict(
        img='h-hof.jpg', pos='50% 30%', bg='h-car.jpg', quick=['auto', 'moto', 'roller', 'anh'],
        ey='Fahrschule Moss · Vechta &amp; Lohne · ehrlich und fair',
        h1='Bestanden. <em>Prüfling der Woche.</em>',
        sub='Jede Woche feiern wir unsere frischen Führerschein-Besitzer. Damit du der Nächste bist: Termine online reservieren, direkt online anmelden und viermal pro Woche Unterricht in Vechta und Lohne.',
        g1=('4,8 ★', '50 Google-Bewertungen'), g2=('4× pro Woche', 'Unterricht, 2× Vechta, 2× Lohne')))
        + gallery('halloffame', 'Hall of Fame', 'Gut gemacht! <em>Unsere Prüflinge.</em>', [
            ('hf1.jpg', '', '50% 30%'), ('hf2.jpg', '', '50% 30%'), ('hf3.jpg', '', '50% 30%'), ('hf4.jpg', '', '50% 30%'), ('hf5.jpg', '', '50% 30%'), ('hf6.jpg', '', '50% 30%'), ('hf7.jpg', '', '50% 30%'), ('hf8.jpg', '', '50% 30%')], 'dk')
        + ablauf('weg', 'Der schnellste Weg', 'Online in drei Klicks, <em>dann fährst du.</em>', '', [
            ('Termin aussuchen', 'Unsere Unterrichte der nächsten Wochen siehst du online und reservierst direkt.'),
            ('Online anmelden', 'Der schnellste und einfachste Weg zum Führerschein.'),
            ('Theorie in 2 Orten', 'Viermal pro Woche: zweimal Vechta, zweimal Lohne. Du kannst beide besuchen.'),
            ('Fahren &amp; feiern', 'Fahrstunden mit Phillip, Robert oder Tobias. Danach: Hall of Fame.')])
        + team('team', 'Bestes Team', 'Phillip, Robert, <em>Tobias.</em>', 'Freundlich, humorvoll und geduldig, so beschreiben uns unsere Fahrschüler.', [
            ('t-phillip.jpg', 'Phillip', 'Fahrlehrer'), ('t-robert.jpg', 'Robert Moss', 'Leiter der Fahrschule'), ('t-tobias.jpg', 'Tobias', 'Fahrlehrer')], 'alt')
        + klassen('klassen', 'Führerschein', 'Was willst <em>du fahren?</em>', '', [
            ('B · B197 · BF17', 'Auto', 'Mit Schaltung oder Automatik, ab 17 begleitet.', 'ab 17', 'auto'),
            ('BE · B96', 'Anhänger', 'Wohnwagen-Urlaub gerettet: Wir helfen auch kurzfristig.', 'ab 18', 'anh'),
            ('A · A2 · A1 · AM', 'Motorrad &amp; Roller', 'Bike to Bike: vom Roller bis zur großen Maschine.', 'ab 15', 'moto'),
            ('B196', '125er', 'Mit dem Autoführerschein aufs Motorrad.', 'ab 25', 'roller')], 'dk')
        + reviews(s, ['Klasse B hier gemacht und kann die Fahrschule nur empfehlen. Die Stimmung war immer super, und ich ging völlig entspannt in die Prüfung. Danke, Phillip!',
                      'Von der Anmeldung bis zum letzten Schritt habe ich mich nie allein gefühlt: Unterstützung, Geduld, Motivation und Ehrlichkeit.',
                      'Phillip für B und Robert für BE, beide geduldig mit hilfreichen Tipps. Alle Prüfungen beim ersten Versuch bestanden.',
                      'Eine andere Fahrschule hat schlecht gearbeitet, fast wäre unser Urlaub geplatzt. Moss hat sofort geholfen, damit wir mit dem Wohnwagen fahren konnten.'], 'alt')
        + contact(s) + footer(s))

S = SITES['moss'] = site(
    slug='fahrschule-moss-vechta', firma='Fahrschule Moss', web='fahrschule-moss.de', fonts='r14mss',
    title='Fahrschule Moss – Deine Fahrschule in Vechta und Lohne', desc='Fahrschule Moss in Vechta und Lohne: online anmelden, Termine reservieren, viermal pro Woche Unterricht. Ehrlich und fair.',
    tel='04441 859745', tel_i='+494441859745', mail='info@fahrschule-moss.de', adresse='Allensteiner Straße 1, 49377 Vechta', google=('4,8', 50),
    cta='Online anmelden', nav=[('Hall of Fame', 'halloffame'), ('So geht’s', 'weg'), ('Team', 'team'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Vechta Mo &amp; Mi', '18:15 – 20:00'), ('Mobil', '0170 2914695')],
    form_lbl='Führerschein', form_opts=['Auto · B / B197 / BF17', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', '125er · B196'],
    form_orte=['Vechta', 'Lohne'],
    form_h3='Direkt online anmelden', form_p='Der schnellste und einfachste Weg. Wir melden uns bei dir.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Ehrlich <em>und fair.</em>', kt_p='Vechta und Lohne. Telefon 04441 859745.',
    rv_h2='Stimmen <em>unserer Fahrschüler.</em>', logo_txt='FAHRSCHULE <span style="color:#5ec8ff">MOSS</span>',
    vars='--bg:#f2f6fa;--ink:#0b1424;--mute:#556175;--p:#2aa9ef;--p-ink:#06121f;--a:#2aa9ef;--a-ink:#06121f;--dk:#0b1424;--s:#fff;--s2:#e2ebf4;--fh:"Unbounded",system-ui,sans-serif;--fb:"Plus Jakarta Sans",system-ui,sans-serif;--r:20px;--r2:28px;--br:999px;--hd-bg:rgba(11,20,36,.9);--hd-ink:#fff;--ft-bg:#060c17;--hx-bg:#0b1424;--hx-op:.35;--hx-blur:3px',
    css='''.hx{color:#fff}.hx .sub{color:rgba(255,255,255,.75)}.hx .btn-o{color:#fff}.hx .chip{background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2);color:#fff}
.hx h1{font-weight:800;font-size:clamp(38px,4.6vw,70px);line-height:1.08}.hx h1 em,.h2 em{font-style:normal;color:var(--p)}.h2{font-weight:700;letter-spacing:-.02em;font-size:clamp(32px,3.6vw,56px)}
.hx .pic{--hx-ar:4/5;max-width:440px;justify-self:end}.hd .lt-logo{color:#fff;font-size:18px}.gl .grid{grid-template-columns:repeat(4,1fr);grid-auto-rows:320px}@media (max-width:820px){.gl .grid{grid-template-columns:repeat(2,1fr);grid-auto-rows:240px}}
.tm .grid{grid-template-columns:repeat(3,1fr)}.tm figure img{aspect-ratio:1/1;object-position:50% 25%}''')
S['bot'] = BOT('Milo', 'dein Moss-Lotse', 'der Fahrschule Moss', S, ['B', 'B197', 'BE', 'B96', 'B196', 'A', 'A2', 'A1', 'AM', 'Mofa'],
    {'schnell': 'Termine reservierst du online, Unterricht gibt es viermal pro Woche.', 'ruhe': 'Unsere Fahrschüler gehen völlig entspannt in die Prüfung, sagen sie.', 'flex': 'Unterricht zweimal in Vechta und zweimal in Lohne, du kannst beide besuchen.', 'angst': 'Phillip, Robert und Tobias gelten als geduldig und humorvoll.'},
    qa=[('lohne', 'In Lohne findet zweimal pro Woche Unterricht statt.'), ('wohnwagen|anhänger|be|b96', 'Anhänger-Führerschein BE und B96: Wir helfen auch, wenn es schnell gehen muss.'), ('termin|reserv', 'Unsere Unterrichtstermine der nächsten Wochen kannst du online reservieren.')],
    tour=[('#halloffame', 'Unsere Prüflinge der Woche.'), ('#weg', 'Der schnellste Weg zum Führerschein.'), ('#team', 'Das Team.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'h-hof.jpg': ('moss/img/i067.webp', 0), 'h-car.jpg': ('moss/img/i002.png', 1600),
    't-phillip.jpg': ('moss/img/i019.webp', 800), 't-robert.jpg': ('moss/img/i020.webp', 800), 't-tobias.jpg': ('moss/img/i021.webp', 800)}
for i, n in enumerate([64, 65, 66, 68, 70, 89, 76, 85], 1): S['img'][f'hf{i}.jpg'] = (f'moss/img/i{n:03d}.webp', 0)
S['body'] = b_moss

# ───────────── 19. Christians Fahrschul-Team, Lohne & Dinklage ─────────────
def b_christians(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 60%', 'h2.jpg': '50% 55%', 'h3.jpg': '50% 50%'}, quick=['auto', 'moto', 'roller', 'anh', 'trak'],
        ey='Christians Fahrschul-Team · Lohne &amp; Dinklage',
        h1='Come in <em>&amp; drive out.</em>',
        sub='Seit über 30 Jahren steht unsere Fahrschule für Kompetenz, Qualität und Herzlichkeit. Pkw, Motorrad, Anhänger oder Traktor: Wir bringen dich erfolgreich ans Ziel.',
        ubar=[('5,0 Sterne', '47 Google-Bewertungen'), ('30+ Jahre', 'Erfahrung'), ('Simulator', 'Ängste abbauen')]))
        + svc('vorteile', 'Kompetent · Flexibel · Erfolgreich', 'Anmelden <em>und durchstarten.</em>', 'Unser Service-Team ist von der Beratung bis zur Prüfung an deiner Seite.', [
            ('Trainings-App', 'Mit dem Online-Führerscheintraining lernst du, wann und wo du willst.'),
            ('Fahrsimulator', 'Für die Grundausbildung, zur Schulung des Reaktionsvermögens oder um Ängste abzubauen.'),
            ('Aufbauseminare', 'Nächstes ASF voraussichtlich am 27.11.2026. Platz sichern!'),
            ('Herzliche Betreuung', 'Fahrlehrer, die fachlich und menschlich überzeugen.')])
        + team('team', 'Wir stehen dir zur Seite', 'Unser <em>Fahrschul-Team.</em>', '', [
            ('t-christian.jpg', 'Christian', 'Inhaber'), ('t-olaf.jpg', 'Olaf', 'Fahrlehrer'), ('t-stefan.jpg', 'Stefan', 'Fahrlehrer'),
            ('t-holger.jpg', 'Holger', 'Fahrlehrer'), ('t-rene.jpg', 'Rene', 'Fahrlehrer'), ('t-erika.jpg', 'Erika', 'Team')], 'dk')
        + duo('standorte', 'Zwei Standorte', 'Lohne <em>und Dinklage.</em>', '', [
            ('Lohne', 'Lindenstraße 18', 'd-lohne.jpg', 'Unterricht montags, dienstags und donnerstags von 18 bis 20 Uhr.', ['Mo · Di · Do 18 – 20 Uhr'], 'In Lohne starten'),
            ('Dinklage', 'Fahrschule Dinklage', 'd-dinklage.jpg', 'Unser zweiter Standort, ganz in deiner Nähe.', ['Dinklage'], 'In Dinklage starten')], 'alt')
        + klassen('klassen', 'Führerscheinklassen', 'Hier ist für jeden <em>etwas dabei.</em>', '', [
            ('B · B197 · BE · B96', 'Pkw &amp; Anhänger', 'Mit Schaltung oder Automatik, mit oder ohne Anhänger.', 'ab 17', 'auto'),
            ('A · A2 · A1 · AM · B196', 'Krafträder &amp; Mofa', 'Vom Mofa bis zur großen Maschine.', 'ab 15', 'moto'),
            ('L · T', 'Landwirtschaftliche Zugmaschinen', 'Für Hof und Lohnunternehmen.', 'ab 16', 'trak')])
        + reviews(s, ['Nach drei Versuchen in Leipzig bin ich nach Lohne gezogen und habe hier bestanden. Christian hat mir unglaublich geholfen. Bester Moment meines Lebens!',
                      'Sehr gute Fahrschule mit sehr entspannten Fahrlehrern, super nett und freundlich.',
                      'Die Fahrlehrer sind motiviert und tun alles, damit man Theorie und Praxis besteht. Auch Familie und Freunde waren hier und begeistert.',
                      'Professionell, freundlich und sehr geduldig. Beim ersten Versuch bestanden!'], 'dk')
        + contact(s) + footer(s))

S = SITES['christians'] = site(
    slug='christians-fahrschul-team-lohne', firma='Christians Fahrschul-Team', web='christians-fahrschul-team.de', fonts='r14chr',
    title='Christians Fahrschul-Team – Come in & drive out | Lohne & Dinklage', desc='Christians Fahrschul-Team in Lohne und Dinklage: Pkw, Motorrad, Anhänger, Traktor, Fahrsimulator, Trainings-App und Aufbauseminare.',
    tel='04442 707666', tel_i='+494442707666', mail='info@christians-fahrschul-team.de', adresse='Lindenstraße 18, 49393 Lohne', google=('5,0', 47),
    cta='Online anmelden', tbar='Nächstes Aufbauseminar voraussichtlich am <b>27.11.2026</b> · <a href="#kontakt">Platz sichern</a>',
    nav=[('Vorteile', 'vorteile'), ('Team', 'team'), ('Standorte', 'standorte'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Lohne Mo · Di · Do', '18:00 – 20:00'), ('Mobil', '0171 6037555')],
    form_lbl='Führerschein', form_opts=['Pkw · B / B197', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', '125er · B196', 'Traktor · L / T', 'Aufbauseminar (ASF)'],
    form_orte=['Lohne', 'Dinklage'],
    form_h3='Online-Anmeldung', form_p='Trag dich ein, unser Service-Team meldet sich.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Jetzt <em>durchstarten!</em>', kt_p='Lohne, Lindenstraße 18. Telefon 04442 707666.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>', logo_txt='Christians <span style="color:#e2231a">Fahrschul-Team</span>',
    vars='--bg:#f5f5f2;--ink:#151515;--mute:#5a5955;--p:#e2231a;--p-ink:#fff;--a:#e2231a;--a-ink:#fff;--dk:#151515;--s:#fff;--s2:#e9e8e3;--fh:"Big Shoulders Display",Impact,sans-serif;--fb:"Heebo",system-ui,sans-serif;--r:10px;--r2:16px;--br:4px;--mq-bg:#e2231a;--hd-bg:rgba(21,21,21,.92);--hd-ink:#fff;--ft-bg:#0d0d0d',
    css='''.hs h1,.h2{font-weight:900;text-transform:uppercase;letter-spacing:.01em;line-height:1;padding-top:6px}.hs h1{font-size:clamp(64px,9vw,150px)}.h2{font-size:clamp(44px,5vw,80px)}
.hs h1 em{font-style:normal;color:var(--p)}.h2 em{font-style:normal;color:var(--p)}.hd .lt-logo{color:#fff;font-family:var(--fh);font-size:24px}
.tm .grid{grid-template-columns:repeat(3,1fr)}.tm figure img{aspect-ratio:4/3;object-position:50% 40%;filter:grayscale(1) contrast(1.05)}.tm figure:hover img{filter:none}@media (max-width:900px){.tm .grid{grid-template-columns:repeat(2,1fr)}}''')
S['bot'] = BOT('Chris', 'dein Fahrschul-Lotse', 'Christians Fahrschul-Team', S, ['B', 'B197', 'BE', 'B96', 'B196', 'A', 'A2', 'A1', 'AM', 'Mofa', 'L', 'T'],
    {'schnell': 'Die Fahrlehrer tun alles, damit du Theorie und Praxis schaffst. Mit der Trainings-App lernst du überall.', 'ruhe': 'Kompetenz, Qualität und Herzlichkeit seit über 30 Jahren.', 'flex': 'Unterricht in Lohne montags, dienstags und donnerstags abends.', 'angst': 'Im Fahrsimulator kannst du gezielt Ängste abbauen.'},
    qa=[('asf|aufbau|seminar|probezeit', 'Nächstes Aufbauseminar voraussichtlich am 27.11.2026. Sichere dir deinen Platz über das Formular.'), ('simulator', 'Der Fahrsimulator hilft bei der Grundausbildung und beim Abbau von Ängsten.')],
    tour=[('#vorteile', 'Was dich bei uns erwartet.'), ('#team', 'Unser Team.'), ('#standorte', 'Lohne und Dinklage.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'h1.jpg': ('christians/img/i060.jpg', 2000), 'h2.jpg': ('christians/img/i051.jpg', 2000), 'h3.jpg': ('christians/img/i021.jpg', 2000),
    't-christian.jpg': ('christians/img/i008.jpg', 900), 't-olaf.jpg': ('christians/img/i014.jpg', 900), 't-manni.jpg': ('christians/img/i013.jpg', 900), 't-stefan.jpg': ('christians/img/i018.jpg', 900),
    't-holger.jpg': ('christians/img/i011.jpg', 900), 't-rene.jpg': ('christians/img/i016.jpg', 900), 't-erika.jpg': ('christians/img/i010.jpg', 900), 't-sina.jpg': ('christians/img/i017.jpg', 900),
    'd-lohne.jpg': ('christians/img/i028.jpg', 0), 'd-dinklage.jpg': ('christians/img/i009.jpg', 0)}
S['body'] = b_christians

# ───────────── 20. Kaiser Fahrschule, Lohne · Bakum · Diepholz · Oldenburg · Osnabrück · Steinfeld ─────────────
def b_kaiser(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 55%', 'h2.jpg': '50% 55%', 'h3.jpg': '50% 60%'}, big='KAISER', quick=['auto', 'moto', 'anh', 'lkw', 'trak'],
        ey='Kaiser Fahrschule · Lohne und fünf weitere Standorte',
        h1='Werde <em>Kaiser.</em>',
        sub='Führerschein aller Klassen, Berufskraftfahrer, Fahrlehrerausbildung und eine Lkw- und Bus-Flotte zum Mieten. Die Kaiser Fahrschule ist nach AZAV zertifiziert, damit Ausbildungen gefördert werden können.',
        ubar=[('5,0 Sterne', '42 Google-Bewertungen'), ('6 Standorte', 'von Osnabrück bis Oldenburg'), ('AZAV', 'zertifiziert')]))
        + duo('bereiche', 'Vier Bereiche', 'Mehr als <em>eine Fahrschule.</em>', '', [
            ('Fahrschule', 'Alle Klassen', 'd-fs.jpg', 'Führerscheinausbildung aller Klassen, ASF-Kurse und Aus- und Weiterbildung im Güter- und Personenverkehr.', ['Pkw bis Bus', 'ASF-Kurse', 'Online-Anmeldung'], 'Zur Anmeldung'),
            ('Fahrlehrerausbildung', 'Zukunftssicherer Job', 'd-fl.jpg', 'In Oldenburg bereiten wir dich intensiv auf die Prüfungen und die Arbeit als Fahrlehrer vor. Mit guten Verdienstmöglichkeiten.', ['Ausbildungsstätte Oldenburg', 'Klasse BE und mehr'], 'Fahrlehrer werden')], 'alt')
        + panels('flotte', 'Unsere Flotte', 'Vollausstattung, <em>auf Wunsch zugestellt.</em>', 'Alle Fahrzeuge für die Klassen C und D können bei Kaiser Vermietung gemietet werden, auch langfristig.', [
            ('Lkw', 'p-lkw.jpg', 'Klassen C, CE, C1, C1E.', '50% 55%'), ('Bus', 'p-bus.jpg', 'Klassen D und DE.', '50% 55%'), ('Pkw', 'p-pkw.jpg', 'Klassen B und BE.', '50% 55%'), ('Standort', 'p-hof.jpg', 'Dinklager Straße 77, Lohne.', '50% 55%')], 'dk')
        + orte('standorte', 'Standorte', 'Wir sind <em>in deiner Nähe.</em>', 'In Lohne: Anmeldung Keetstraße Mo – Do 17:00 bis 18:30, Unterricht Mo – Do 18:30 Uhr. Dinklager Straße: Mo – Fr 8 bis 13 und 14 bis 17 Uhr.', [
            ('Lohne', 'Keetstraße 40', 'Unterricht Mo – Do'), ('Lohne', 'Dinklager Straße 77', 'Mo – Fr'), ('Bakum', 'Loher Straße 6', ''), ('Diepholz', '', ''), ('Oldenburg', 'Fahrlehrerausbildung', ''), ('Osnabrück', '', ''), ('Steinfeld', '', '')])
        + klassen('klassen', 'Führerschein', 'Alle Klassen <em>unter einem Dach.</em>', '', [
            ('B · B197 · BE · B96', 'Pkw &amp; Anhänger', 'Mit Schaltung oder Automatik.', 'ab 17', 'auto'),
            ('A · A2 · A1 · AM · B196', 'Zweirad', 'Vom Roller bis zum Motorrad.', 'ab 15', 'moto'),
            ('C · CE · C1 · C1E', 'Lkw', 'Auch als Berufskraftfahrer.', 'ab 18', 'lkw'),
            ('D · DE · D1', 'Bus', 'Personenverkehr.', 'ab 21', 'lkw'),
            ('L · T', 'Traktor', 'Für die Landwirtschaft.', 'ab 16', 'trak')], 'alt')
        + reviews(s, ['Für mich die beste Fahrschule im Oldenburger Münsterland. Super Service, höfliche, engagierte und sehr kompetente Fahrlehrer.',
                      'Hier ist jeder in guten Händen, ob Motorrad, Auto, Lkw oder Bus. Die Fahrlehrer gehen auf jeden Schüler ein und arbeiten an Schwächen und Stärken.',
                      'Lehrreiche Stunden, professionelle und angenehme Fahrten. Ich fühlte mich gut vorbereitet.',
                      'Modul hier gemacht: gut organisiert, gutes Essen und alle sehr freundlich.'], 'dk')
        + contact(s) + footer(s))

S = SITES['kaiser'] = site(
    slug='kaiser-fahrschule-lohne', firma='Fahrschule Kaiser GmbH', web='kaiser-lohne.de', fonts='r14kai',
    title='Kaiser Fahrschule – alle Klassen, Berufskraftfahrer & Fahrlehrerausbildung | Lohne', desc='Kaiser Fahrschule in Lohne, Bakum, Diepholz, Oldenburg, Osnabrück und Steinfeld: alle Klassen, Berufskraftfahrer, Fahrlehrerausbildung, AZAV-zertifiziert.',
    tel='04442 7033660', tel_i='+4944427033660', mail='info@kaiser-lohne.de', adresse='Dinklager Straße 77, 49393 Lohne', google=('5,0', 42),
    cta='Online anmelden', nav=[('Bereiche', 'bereiche'), ('Flotte', 'flotte'), ('Standorte', 'standorte'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 13:00 · 14:00 – 17:00'), ('Keetstraße Mo – Do', '17:00 – 18:30')],
    form_lbl='Interesse an', form_opts=['Pkw · B / B197', 'Anhänger · BE / B96', 'Zweirad · A / A2 / A1 / AM', 'Lkw · C / CE', 'Bus · D / DE', 'Traktor · L / T', 'ASF-Kurs', 'Modulschulung BKF', 'Fahrlehrerausbildung', 'Fahrzeug mieten'],
    form_orte=['Lohne', 'Bakum', 'Diepholz', 'Oldenburg', 'Osnabrück', 'Steinfeld'],
    form_h3='Online-Anmeldung', form_p='Wir melden uns schnell bei dir.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Bereit <em>für die Krone?</em>', kt_p='Fahrschule Kaiser GmbH, Dinklager Straße 77, Lohne. Telefon 04442 7033660.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>', logo_txt='<span style="color:#e5007d">KAISER</span> Fahrschule',
    vars='--bg:#f6f6f7;--ink:#1a1b1f;--mute:#5c5e66;--p:#e5007d;--p-ink:#fff;--a:#e5007d;--a-ink:#fff;--dk:#1a1b1f;--s:#fff;--s2:#e9e9ec;--fh:"Saira Condensed",Impact,sans-serif;--fb:"Hind",system-ui,sans-serif;--r:6px;--r2:10px;--br:4px;--mq-bg:#e5007d;--hd-bg:rgba(26,27,31,.92);--hd-ink:#fff;--ft-bg:#111215',
    css='''.hs h1,.h2{font-weight:800;text-transform:uppercase;line-height:1;letter-spacing:.005em;padding-top:5px}.hs h1{font-size:clamp(64px,8.8vw,150px)}.hs h1 em,.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#ff4fae}
.hs .big{font-family:var(--fh);font-weight:800;-webkit-text-stroke:2px rgba(229,0,125,.4)}.hd .lt-logo{color:#fff;font-family:var(--fh);font-size:26px}''')
S['bot'] = BOT('Kai', 'dein Kaiser-Lotse', 'der Kaiser Fahrschule', S, ['B', 'B197', 'BE', 'B96', 'B196', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE', 'D', 'L', 'T'],
    {'schnell': 'In Lohne gibt es Unterricht montags bis donnerstags. Achte auf unsere Crashkurse.', 'ruhe': 'Unsere Fahrlehrer gehen auf jeden Schüler einzeln ein, an Schwächen und Stärken.', 'flex': 'Sechs Standorte, von Osnabrück bis Oldenburg.', 'angst': 'Wir passen die Ausbildung an dein Können an, Schritt für Schritt.'},
    qa=[('azav|gutschein|förder|jobcenter|arbeitsagentur', 'Wir sind nach AZAV zertifiziert, Ausbildungen können gefördert werden.'), ('fahrlehrer|ausbildung zum', 'Unsere Fahrlehrerausbildungsstätte ist in Oldenburg.'), ('miet|vermiet', 'Lkw und Busse der Klassen C und D kannst du bei Kaiser Vermietung mieten, auch langfristig.')],
    tour=[('#bereiche', 'Mehr als eine Fahrschule.'), ('#flotte', 'Unsere Flotte.'), ('#standorte', 'Sechs Standorte.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'h1.jpg': ('kaiser/img/i017.jpg', 0), 'h2.jpg': ('kaiser/img/i041.jpg', 0), 'h3.jpg': ('kaiser/img/i012.jpg', 0),
    'd-fs.jpg': ('kaiser/img/i028.jpg', 0), 'd-fl.jpg': ('kaiser/img/i019.jpg', 0),
    'p-lkw.jpg': ('kaiser/img/i042.jpg', 0), 'p-bus.jpg': ('kaiser/img/i036.jpg', 0), 'p-pkw.jpg': ('kaiser/img/i037.jpg', 0), 'p-hof.jpg': ('kaiser/img/i018.jpg', 0)}
S['body'] = b_kaiser
