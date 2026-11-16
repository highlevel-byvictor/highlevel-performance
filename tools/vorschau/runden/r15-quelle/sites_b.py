"""Runde 15 · Teil B: Kemper, Hofschröer, Scherpenberg."""
from common import *
SITES = {}
HI = '/home/claude/r15raw/hi/'
PIX = '/home/claude/pixa/'

# ───────────── 5. Fahrschule Kemper, Meppen · Geeste-Dalum ─────────────
def b_kemper(s):
    lc = [('Montag', '15:00 – 18:00', 'Meppen-Esterfeld · Mozartstraße 24'), ('Dienstag', '15:00 – 18:00', 'Geeste-Dalum · Lingener Straße 1'),
          ('Mittwoch', '15:00 – 18:00', 'Meppen-Schleuse · Teglinger Straße 1a'), ('Mo – Do', '09:00 – 11:30', 'Meppen-Esterfeld · Mozartstraße 24')]
    lr = ''.join(f'<li data-r><b>{a}</b><span>{b}</span><small>{c}</small></li>' for a, b, c in lc)
    coach = f"""<section class="sec klc" id="lerncoaching"><div class="w klc-g">
<div data-r><span class="klc-tag">Kostenlos</span><h2 class="h2">Theorie lernen, <em>aber richtig.</em></h2>
<p class="lead">Mit unserem Lerncoaching kommst du sicherer, schneller und entspannter zur Theorieprüfung. Unsere Fahrlehrerin betreut dich persönlich und findet mit dir deinen Lernweg: ob du schnell durchziehen willst oder lieber Schritt für Schritt lernst.</p>
<ul class="klc-v"><li>4× pro Woche, kostenlos</li><li>Persönliche Betreuung durch unsere Fahrlehrerin</li><li>Auch bei Lernschwierigkeiten bestens aufgehoben</li></ul>
<a class="btn btn-a" href="#kontakt">Jetzt anmelden {AR}</a></div>
<div data-r="2"><ol class="klc-l">{lr}</ol></div></div></section>"""
    orte_l = [('Meppen-Schleuse', 'Teglinger Straße 1a, 49716 Meppen', 'Unterricht Mi 18:00 – 19:30'), ('Meppen-Esterfeld', 'Mozartstraße 24, 49716 Meppen', 'Unterricht Do 18:00 – 19:30'), ('Geeste-Dalum', 'Lingener Straße 1, 49744 Geeste-Dalum', 'Unterricht Di 18:00 – 19:30')]
    return (hd(s, False) + hero_x(s, dict(
        img='h-plakat.jpg', pos='50% 50%', bg='h-b96.jpg', quick=['auto', 'moto', 'anh', 'lkw'],
        ey='Fahrschule Kemper · seit 1980 in Meppen',
        h1='Kein Bock mehr zu laufen? <em>Mach deinen Führerschein!</em>',
        sub='Hol dir dein Ticket in die Freiheit: in Meppen und Geeste-Dalum, mit kostenlosem Lerncoaching für die Theorie. Komm einfach 30 Minuten vor dem Unterricht vorbei.',
        ))
        + marquee(['Kostenloses Lerncoaching', 'B · B197 · BE', 'B96 an einem Tag', 'A · A2 · A1 · AM', 'C · CE · D', 'L · T', 'Fit im Auto 65+', 'seit 1980'], 'km')
        + coach
        + eltern('angebote', 'p-b96.jpg', 'B96 in Meppen', 'Wohnwagen-Führerschein <em>an einem Tag.</em>', 'Die Schulung an nur einem Tag, ganz ohne Prüfung. Danach fährst du Gespanne bis 4.250 kg, gültig in der ganzen EU.', ['2,5 Stunden Theorie', '3,5 Stunden Praxis', 'Schlüsselzahl 96 im Führerschein'], 'Termin anfragen', 'alt')
        + eltern('senioren', 'p-senioren.jpg', 'Senioren sicher unterwegs', 'Fit im Auto, <em>mit gutem Gefühl.</em>', 'Eine entspannte Beobachtungsfahrt gibt Klarheit und Sicherheit. Ganz ohne Stress, ganz ohne Angst, den Führerschein abgeben zu müssen. Interesse? Rufen Sie uns an: 05931 / 5300.', ['Training ab 65 Jahren', 'Übungsplatz und Fahrt im Alltag', 'Mit der Landesverkehrswacht Niedersachsen'], 'Platz anfragen', '', True)
        + svc('leistungen', 'Unsere Leistungen', 'Wir bringen <em>jeden ans Ziel.</em>', 'Zur Anmeldung kommst du einfach zum Unterricht oder rufst uns an.', [
            ('Alle Klassen', 'Vom Mofa über Auto und Motorrad bis Lkw, Bus und Traktor.'),
            ('Für Menschen mit Behinderung', 'Wir bilden auch mit Umbauten und Hilfsmitteln aus.'),
            ('MPU-Beratung', 'Wir unterstützen dich auf dem Weg zurück zum Führerschein.'),
            ('Seminare', 'Aufbauseminar für Fahranfänger, Fahreignungsseminar, Spritspar-Stunde.')])
        + orte('standorte', 'Unsere Standorte', 'Dreimal <em>für dich da.</em>', 'Erreichbar unter 05931 / 5300 oder mobil unter 0173 / 5202296.', orte_l, 'dk')
        + klassen('klassen', 'Führerscheinklassen', 'Welcher Führerschein <em>passt zu dir?</em>', 'Tipp auf eine Klasse, dann sagt dir Pia, ob sie passt.', [
            ('B · B197', 'Auto', 'Mit Schaltung oder Automatik mit Schaltkompetenz. Begleitet ab 17.', 'ab 17', 'auto'),
            ('BE · B96', 'Anhänger', 'Wohnwagen und schwere Anhänger.', 'ab 18', 'anh'),
            ('A · A2 · A1 · AM', 'Motorrad &amp; Roller', 'Dazu B196 für Autofahrer.', 'ab 15', 'moto'),
            ('C · CE · D', 'Lkw &amp; Bus', 'Für Beruf und Karriere.', 'ab 18', 'lkw'),
            ('L · T', 'Traktor', 'Für Hof und Feld.', 'ab 16', 'trak')])
        + promo('instagram', 'p-insta.jpg', 'Instagram', 'Kurz, schnell, <em>aktuell informiert.</em>', 'Folge uns auf Instagram: Dort gibt es neue Termine, Tipps für die Prüfung und Einblicke in unseren Fahrschulalltag.', ['@fahrschule_kemper_meppen', 'Mitglied im Fahrlehrerverband Niedersachsen'], 'Jetzt anmelden', 'alt')
        + reviews(s, ['Die Fahrlehrer sind entspannt und locker, man kann mit ihnen lachen. Und wenn mal etwas nicht klappt, bauen sie dich wieder auf.',
                      'Das Lerncoaching hat mir extrem geholfen. Man wird super auf alle Prüfungen vorbereitet.',
                      'Alle sind so herzlich, man fühlt sich wie in einer Familie.',
                      'Theorie und Praxis waren immer angenehm und entspannt. Ich freue mich schon auf weitere Klassen.'])
        + contact(s) + footer(s))

S = SITES['kemper'] = site(
    slug='fahrschule-kemper-meppen', firma='Fahrschule Kemper', web='fahrschule-kemper-meppen.de', fonts='r15kem',
    title='Fahrschule Kemper – seit 1980 in Meppen & Geeste-Dalum', desc='Fahrschule Kemper in Meppen und Geeste-Dalum: kostenloses Lerncoaching, B96 an einem Tag, Fit im Auto für Senioren, alle Klassen.',
    tel='05931 5300', tel_i='+4959315300', mail='post@fahrschule-meppen.de', adresse='Teglinger Straße 1a, 49716 Meppen', google=('5,0', 16),
    social=[('Instagram', 'https://www.instagram.com/fahrschule_kemper_meppen/'), ('Facebook', 'https://www.facebook.com/fahrschulekempermeppen')],
    cta='Jetzt anmelden', nav=[('Lerncoaching', 'lerncoaching'), ('B96', 'angebote'), ('Senioren', 'senioren'), ('Standorte', 'standorte'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Schleuse', 'Mi 18:00 – 19:30'), ('Esterfeld', 'Do 18:00 – 19:30'), ('Dalum', 'Di 18:00 – 19:30')],
    form_lbl='Anliegen', form_opts=['Führerschein Auto · B / B197', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1 / AM', 'Lkw / Bus · C / CE / D', 'Traktor · L / T', 'Kostenloses Lerncoaching', 'Fit im Auto (65+)', 'Seminar (ASF / FES)'],
    form_orte=['Meppen-Schleuse', 'Meppen-Esterfeld', 'Geeste-Dalum'],
    form_h3='Jetzt anmelden', form_p='Schick uns deine Daten, wir melden uns und beraten dich gern.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Pack deine Sachen <em>und los geht’s.</em>', kt_p='Ruf an unter 05931 / 5300, mobil 0173 / 5202296, oder schreib an post@fahrschule-meppen.de.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#fdf8e8;--ink:#0d1f2d;--mute:#4f5d68;--p:#032e4f;--p-ink:#fff;--a:#f3c244;--a-ink:#032e4f;--dk:#032e4f;--s:#fff;--s2:#f6eccb;--fh:"Bebas Neue",system-ui,sans-serif;--fb:"Roboto",system-ui,sans-serif;--r:14px;--r2:20px;--br:6px;--mq-bg:#f3c244;--mq-ink:#032e4f;--hd-bg:rgba(3,46,79,.96);--hd-ink:#fff;--logo-h:54px;--ft-bg:#032e4f;--hx-ar:4/5;--hx-r:6px',
    css=EMO('3,46,79', 'center 50%', dark=True, pic_w=360) + '''
.hx h1,.h2{font-weight:400;letter-spacing:.01em;line-height:.98}.hx h1{font-size:clamp(50px,6.4vw,104px)}.hx h1 em,.h2 em{font-style:normal;color:#f3c244}.h2{font-size:clamp(42px,4.6vw,72px)}.kt .h2 em,.sv .h2 em,.kl .h2 em,.rv .h2 em,.alt .h2 em{color:#b8860b}
.hd .btn-a{background:#f3c244;color:#032e4f}.hx .pic{transform:rotate(2deg);box-shadow:0 40px 90px rgba(0,0,0,.45)}.hx .gl{background:#f3c244;color:#032e4f}.hx .ey{color:#f3c244!important}
.klc{background:#fff}.klc-g{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(30px,5vw,80px);align-items:center}.klc-tag{display:inline-block;background:#f3c244;color:#032e4f;font:400 24px var(--fh);padding:6px 16px;transform:rotate(-2deg)}
.klc-v{list-style:none;padding:0;margin:20px 0 26px}.klc-v li{padding:7px 0 7px 32px;position:relative;font-weight:500}.klc-v li::before{content:"";position:absolute;left:0;top:13px;width:18px;height:10px;border-left:3px solid #f3c244;border-bottom:3px solid #f3c244;transform:rotate(-45deg)}
.klc-l{list-style:none;padding:0;margin:0;display:grid;gap:12px}.klc-l li{display:grid;grid-template-columns:120px 1fr;gap:2px 16px;background:#032e4f;color:#fff;border-radius:14px;padding:18px 22px}
.klc-l b{grid-row:span 2;font:400 30px var(--fh);color:#f3c244;align-self:center}.klc-l span{font-weight:700;font-size:18px}.klc-l small{color:#c8d3dc}
@media(max-width:860px){.klc-g{grid-template-columns:1fr}.klc-l li{grid-template-columns:96px 1fr}}
.el figure{max-width:440px;justify-self:center;aspect-ratio:auto!important;height:auto!important;background:none;box-shadow:none}.el figure img{border-radius:10px;height:auto!important;aspect-ratio:auto!important;object-fit:contain!important;box-shadow:0 30px 60px rgba(3,46,79,.25)}.hx .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.promo figure{max-width:340px;justify-self:center}.or .o b{font-weight:400;font-size:30px}.kl .k b{font-weight:400;font-size:34px;color:#032e4f}
.ft .logo img,.ft img{height:56px}.hd .logo img{height:54px}''')
S['bot'] = BOT('Pia', 'deine Kemper-Lotsin', 'der Fahrschule Kemper', S, ['B', 'B197', 'BE', 'B96', 'B196', 'A', 'A2', 'A1', 'AM', 'C', 'CE', 'D', 'L', 'T'],
    {'schnell': 'Mit dem kostenlosen Lerncoaching kommst du schneller durch die Theorie.', 'ruhe': 'Unsere Fahrlehrer sind entspannt und bauen dich auf, wenn mal was nicht klappt.', 'flex': 'Drei Standorte in Meppen und Geeste-Dalum.', 'angst': 'Auch bei Lernschwierigkeiten bist du bei uns bestens aufgehoben.'},
    qa=[('lerncoach|theorie|lernen', 'Kostenloses Lerncoaching gibt es 4× pro Woche: Mo, Di und Mi nachmittags und Mo bis Do vormittags.'), ('b96|wohnwagen|anhänger', 'B96 machst du bei uns an einem Tag, ganz ohne Prüfung.'), ('senior|65|fit im auto', 'Fit im Auto ist unser Training für Senioren ab 65, ganz ohne Angst um den Führerschein.')],
    tour=[('#lerncoaching', 'Kostenloses Lerncoaching.'), ('#angebote', 'B96 und Fit im Auto.'), ('#standorte', 'Unsere drei Standorte.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': (HI + 'kem_logo.png', 600), 'h-b96.jpg': ('kemper/img/i015.jpeg', 2000), 'h-plakat.jpg': ('kemper/img/i001.png', 900),
    'p-b96.jpg': ('kemper/img/i013.jpg', 1400), 'p-senioren.jpg': ('kemper/img/i005.png', 1000), 'p-insta.jpg': ('kemper/img/i014.png', 800)}
S['body'] = b_kemper

# ───────────── 6. Fahrschule Hofschröer, Lingen ─────────────
def b_hofschroeer(s):
    hero = f"""<section class="hh" id="top"><div class="hh-bg"><img src="img/h-fassade.jpg" alt="" fetchpriority="high"></div>
<div class="w hh-t" data-r>{chip(s)}<p class="hh-s">Herzlich willkommen</p><h1>Dein Weg <em>zur mobilen Freiheit.</em></h1>
<p class="sub">Seit über 25 Jahren in Lingen, drei Filialen und ein Team, das dich sicher, selbstbewusst und mit einem guten Gefühl auf die Straße bringt.</p>
<div class="ctas"><a class="btn btn-a" href="#kontakt">{s['cta']} {AR}</a><a class="btn btn-o" href="tel:{s['tel_i']}">{PH} {s['tel']}</a></div>{quick(s, dict(quick=['auto', 'moto', 'roller', 'anh', 'lkw']))}</div>
<figure class="w hh-team" data-r="2"><img src="img/h-team.jpg" alt="Das Team der Fahrschule Hofschröer"></figure></section>"""
    filialen = [('Laxten', 'Frerener Straße 5', 'Mo &amp; Mi', 'f-laxten.jpg'), ('Innenstadt', 'Lindenstraße 1 (gegenüber Arbeitsagentur)', 'Di &amp; Do', 'f-innenstadt.jpg'), ('Brögbern', 'Duisenburger Straße 7', 'Mo &amp; Do', 'f-broegbern.jpg')]
    fl = ''.join(f'<article class="hf" data-r><figure><img src="img/{i}" alt="Filiale {a} der Fahrschule Hofschröer" loading="lazy"></figure><div><h3>Filiale {a}</h3><p>{b}<br>49809/49811 Lingen</p><p class="hf-t">{c} · Anmeldung ab 18:30 · Unterricht 19:00 – 20:30</p></div></article>' for a, b, c, i in filialen)
    fil = f'<section class="sec hfs" id="standorte"><div class="w"><div data-r>{head("Unsere Standorte", "Drei Filialen, <em>vier Theorieabende.</em>", "14 Theorieeinheiten wiederholen sich regelmäßig, du kannst jederzeit einsteigen. Und gern auch einfach mal unverbindlich reinschnuppern.")}</div><div class="hf-g">{fl}</div></div></section>'
    return (hd(s, True) + hero
        + marquee(['Theorie 4× pro Woche', 'Ferien- &amp; Intensivkurse', 'Automatik', 'Umschreibung', 'Deutsch · English · Polski', 'AM · A1 · A2 · A', 'B · BE', 'C1 · C · CE · L · T'], 'hm')
        + svc('leistungen', 'Unsere Leistungen', 'Klar <em>und kompakt.</em>', 'Du kannst jederzeit den Fahrlehrer deines Vertrauens wählen.', [
            ('Theorie 4× pro Woche', 'An drei Standorten, Einstieg jederzeit.'), ('Ferien- &amp; Intensivkurse', 'Kompakt und effizient zum Führerschein.'),
            ('Automatik-Ausbildung', 'Einfacher lernen, auf Wunsch mit Automatik.'), ('Umschreibung', 'Beratung und Vorbereitung für ausländische Führerscheine.'),
            ('Auffrischungsstunden', 'Ideal für Wiedereinsteiger oder bei Fahrangst.'), ('Sicher zur Prüfung', 'Gezielte Vorbereitung, auch auf die Technikfragen.')])
        + team('team', 'Das Team', 'Hier findest du <em>unsere Fahrlehrer.</em>', 'Mit Geduld, Know-how und Leidenschaft. Unterricht auf Deutsch, Englisch oder Polnisch.', [
            ('t-christian.jpg', 'Christian Hofschröer', 'Inhaber · AM, A1, A2, A, B, BE · DE/EN'), ('t-haydar.jpg', 'Haydar Lamp', 'B, BE, C1, C, C1E, CE, L, T'),
            ('t-gerold.jpg', 'Gerold Aubreville', 'AM, A1, A2, A, B, BE · DE/EN'), ('t-mathias.jpg', 'Mathias Dust', 'B, BE'),
            ('t-tobias.jpg', 'Tobias Müller', 'B, BE'), ('t-matze.jpg', 'Maciej „Matze“ Karys', 'AM, A1, A2, A, B, BE · DE/PL'),
            ('t-raphael.jpg', 'Raphael Wedler', 'B, BE'), ('t-ali.jpg', 'Ali Sürmeli', 'B, BE')], 'alt')
        + fil
        + gallery('zweirad', 'Zweiradausbildung', 'Sicher unterwegs <em>von Anfang an.</em>', [
            ('z1.jpg', 'w2', '50% 60%'), ('z2.jpg', '', '50% 50%'), ('z3.jpg', '', '50% 50%'), ('z4.jpg', '', '50% 50%'), ('z5.jpg', 'w2', '50% 55%')], 'dk')
        + klassen('klassen', 'Führerscheine', 'Auto, Motorrad, <em>Lkw oder Traktor?</em>', 'Tipp auf eine Klasse, dann prüft Hoffi mit dir, ob sie passt.', [
            ('B · BE · BF17', 'Auto &amp; Anhänger', 'Mit Schaltung oder Automatik.', 'ab 17', 'auto'),
            ('A1 · A2 · A', 'Motorrad', 'Mit unseren Zweirädern vor der Filiale.', 'ab 16', 'moto'),
            ('AM · Mofa', 'Roller', 'Der erste Schritt in die Freiheit.', 'ab 15', 'roller'),
            ('C1 · C · CE', 'Lkw', 'Mit Haydar zum Berufskraftfahrer.', 'ab 18', 'lkw'),
            ('L · T', 'Traktor', 'Für Landwirtschaft und Lohnunternehmen.', 'ab 16', 'trak')])
        + reviews(s, ['Ich war vorher in einer anderen Fahrschule in Lingen, mit vielen unnötigen Stunden. Hier hätte ich von Anfang an sein sollen. Gerold ist professionell, geduldig und unterstützend.',
                      'Besonders hilfreich fand ich, wie Gerold Verkehrssituationen mit Whiteboard und Spielzeugautos erklärt.',
                      'Theorie und Praxis jeweils im ersten Versuch bestanden. Vielen Dank an meinen Fahrlehrer!',
                      'Den Motorradführerschein Klasse A habe ich hier gemacht: Die Theorie ging dank vieler Termine schnell, die Fahrstunden waren gut aufgebaut.'], 'alt')
        + contact(s) + footer(s))

S = SITES['hofschroeer'] = site(
    slug='fahrschule-hofschroeer-lingen', firma='Fahrschule Hofschröer GmbH', web='fahrschule-hofschroeer.de', fonts='r15hof',
    title='Fahrschule Hofschröer – Dein Weg zur mobilen Freiheit | Lingen', desc='Fahrschule Hofschröer in Lingen: drei Filialen, Theorie 4× pro Woche, Ferienkurse, Automatik, Umschreibung, Unterricht auf Deutsch, Englisch und Polnisch.',
    tel='0591 9669146', tel_i='+495919669146', mail='info@fahrschule-hofschroeer.de', adresse='Frerener Straße 5, 49809 Lingen (Ems)', google=('4,9', 65),
    social=[('Instagram', 'https://www.instagram.com/fahrschule.hofschroeer'), ('Facebook', 'https://www.facebook.com/fahrschule.hofschroeer'), ('WhatsApp', 'https://api.whatsapp.com/send/?phone=491709621722')],
    cta='Jetzt anmelden', nav=[('Leistungen', 'leistungen'), ('Team', 'team'), ('Standorte', 'standorte'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Laxten', 'Mo &amp; Mi ab 18:30'), ('Innenstadt', 'Di &amp; Do ab 18:30'), ('Brögbern', 'Mo &amp; Do ab 18:30')],
    form_lbl='Führerschein', form_opts=['Auto · B / BE / BF17', 'Automatik', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', 'Lkw · C1 / C / CE', 'Traktor · L / T', 'Umschreibung ausländischer Führerschein', 'Auffrischungsstunden', 'Ferien- / Intensivkurs'],
    form_orte=['Laxten · Frerener Straße', 'Innenstadt · Lindenstraße', 'Brögbern · Duisenburger Straße'],
    form_h3='Jetzt anmelden', form_p='Wir rufen dich zurück und vereinbaren einen Termin in der Filiale deiner Wahl.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Melde dich einfach, <em>wir freuen uns auf dich.</em>', kt_p='Telefon 0591 966 91 46, per Mail an info@fahrschule-hofschroeer.de oder ganz unkompliziert per WhatsApp.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#fff;--ink:#141414;--mute:#5a5a5a;--p:#e2001a;--p-ink:#fff;--a:#e2001a;--a-ink:#fff;--dk:#141414;--s:#fff;--s2:#f4f4f4;--fh:"Inter Tight",system-ui,sans-serif;--fb:"Inter Tight",system-ui,sans-serif;--r:18px;--r2:24px;--br:999px;--mq-bg:#141414;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.96);--hd-ink:#141414;--logo-h:40px;--ft-bg:#141414',
    css='''.hh{position:relative;padding:130px 0 0;overflow:hidden;background:#fff}.hh-bg{position:absolute;inset:0 0 34% 0}.hh-bg img{width:100%;height:100%;object-fit:cover;object-position:50% 40%}
.hh-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.95) 45%,rgba(255,255,255,.55) 70%,rgba(255,255,255,0) 85%),linear-gradient(0deg,#fff 0%,rgba(255,255,255,0) 30%)}
.hh-t{position:relative;z-index:1;max-width:min(1240px,100% - 48px)}.hh-t>*{max-width:600px}.hh-s{font:400 clamp(44px,5vw,70px)/1 "Allison",cursive;color:#e2001a;margin:14px 0 6px}
.hh h1{font:800 clamp(42px,5.4vw,80px)/1.02 var(--fh);letter-spacing:-.03em;margin:0}.hh h1 em{font-style:normal;color:#e2001a;display:block}.hh .sub{font-size:19px;color:#3d3d3d;margin-top:20px}.hh .ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.hh-team{position:relative;z-index:1;margin:40px auto 0}.hh-team img{width:100%;display:block}
.h2{font-weight:800;letter-spacing:-.03em}.h2 em{font-style:normal;color:#e2001a}.dk .h2 em{color:#ff5466}
.sv .row{grid-template-columns:repeat(3,1fr)}.sv .row div{border-left:4px solid #e2001a;border-radius:0 18px 18px 0}@media(max-width:820px){.sv .row{grid-template-columns:1fr}}
.tm .grid{grid-template-columns:repeat(4,1fr)}.tm figure img{aspect-ratio:4/5;object-position:50% 22%}@media(max-width:820px){.tm .grid{grid-template-columns:repeat(2,1fr)}}
.hf-g{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}.hf{border-radius:24px;overflow:hidden;background:#f4f4f4}.hf figure{margin:0;aspect-ratio:4/3;overflow:hidden}.hf img{width:100%;height:100%;object-fit:cover}
.hf div{padding:20px 22px 24px}.hf h3{margin:0;font:800 24px var(--fh)}.hf p{margin:6px 0 0;color:#5a5a5a}.hf .hf-t{color:#e2001a;font-weight:700;font-size:15px}@media(max-width:860px){.hf-g{grid-template-columns:1fr}}
.kl .k b{color:#e2001a}.hd .logo img{height:40px}.ft img{background:#fff;padding:8px 12px;border-radius:10px}
@media(max-width:820px){.hh{padding-top:100px}.hh-bg{inset:0 0 50% 0}.hh-bg::after{background:linear-gradient(0deg,#fff 10%,rgba(255,255,255,.88) 60%,rgba(255,255,255,.6))}}''')
S['bot'] = BOT('Hoffi', 'dein Hofschröer-Lotse', 'der Fahrschule Hofschröer', S, ['B', 'BF17', 'BE', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C1', 'C', 'CE', 'L', 'T'],
    {'schnell': 'Theorie an vier Abenden pro Woche, dazu Ferien- und Intensivkurse.', 'ruhe': 'Du wählst den Fahrlehrer deines Vertrauens. Alle bilden sich regelmäßig weiter.', 'flex': 'Drei Filialen in Lingen: Laxten, Innenstadt und Brögbern.', 'angst': 'Für Wiedereinsteiger und bei Fahrangst gibt es Auffrischungsstunden.'},
    qa=[('english|englisch|polnisch|polski', 'Unterricht gibt es auf Deutsch, Englisch und Polnisch.'), ('umschreib|ausländ', 'Wir beraten und bereiten dich auf die Umschreibung deines ausländischen Führerscheins vor.'), ('automatik', 'Automatik-Ausbildung bieten wir an. Einfacher lernen, auf Wunsch.')],
    tour=[('#leistungen', 'Unsere Leistungen.'), ('#team', 'Das Team.'), ('#standorte', 'Drei Filialen in Lingen.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('hofschroeer/img/i002.png', 900), 'h-fassade.jpg': (HI + 'hof_i035.jpg', 2000), 'h-team.jpg': (HI + 'hof_i051.png', 2000, (0, .17, 1, 1)),
    't-christian.jpg': (HI + 'hof_i020.jpg', 1100, (.2, 0, .8, 1)), 't-haydar.jpg': (HI + 'hof_i030.jpg', 1100, (.2, 0, .8, 1)), 't-gerold.jpg': (HI + 'hof_i028.jpg', 1100, (.2, 0, .8, 1)),
    't-mathias.jpg': (HI + 'hof_i046.jpg', 1100, (.2, 0, .8, 1)), 't-tobias.jpg': (HI + 'hof_i047.jpg', 1100, (.2, 0, .8, 1)), 't-matze.jpg': (HI + 'hof_i045.jpg', 1100, (.2, 0, .8, 1)),
    't-raphael.jpg': (HI + 'hof_i054.png', 1100, (.2, 0, .8, 1)), 't-ali.jpg': (HI + 'hof_i018.jpg', 1100, (.2, 0, .8, 1)),
    'f-laxten.jpg': (HI + 'hof_i033.jpg', 1400), 'f-innenstadt.jpg': (HI + 'hof_i015.jpeg', 1400), 'f-broegbern.jpg': (HI + 'hof_i032.jpg', 1400),
    'z1.jpg': (HI + 'hof_i057.jpg', 1800), 'z2.jpg': (HI + 'hof_i059.jpg', 1000), 'z3.jpg': (HI + 'hof_i061.jpg', 1000), 'z4.jpg': (HI + 'hof_i060.jpg', 1000), 'z5.jpg': (HI + 'hof_i058.jpg', 1800)}
S['body'] = b_hofschroeer

# ───────────── 7. Fahrschule Scherpenberg, Fürstenau · Lingen · Bippen ─────────────
def b_scherpenberg(s):
    ic = [('i-b.jpg', 'B', 'Auto'), ('i-be.jpg', 'BE', 'Anhänger'), ('i-a.jpg', 'A', 'Motorrad'), ('i-c.jpg', 'C', 'Lkw'), ('i-ce.jpg', 'CE', 'Lkw mit Anhänger'), ('i-t.jpg', 'T', 'Traktor')]
    icons = ''.join(f'<button type="button" class="si" data-r data-check="{ {"B": "auto", "BE": "anh", "A": "moto", "C": "lkw", "CE": "lkw", "T": "trak"}[k] }"><img src="img/{i}" alt="Klasse {k}" loading="lazy"><b>{k}</b><span>{t}</span></button>' for i, k, t in ic)
    kl = f'<section class="sec sk" id="klassen"><div class="w"><div data-r>{head("Führerscheinklassen", "Wir haben die passende <em>Klasse für dich.</em>", "Tipp auf eine Klasse, dann prüft Sina mit dir, ob sie passt.")}</div><div class="sk-g">{icons}</div></div></section>'
    zeiten = [('Fürstenau', 'Di &amp; Do', '19:00 – 20:30'), ('Lingen (Ems)', 'Di &amp; Do', '19:00 – 20:30'), ('Lingen (Ems)', 'Mo &amp; Mi', '19:00 – 20:30'), ('Bippen', 'Mo &amp; Mi', '19:00 – 20:30')]
    zt = ''.join(f'<li data-r><b>{a}</b><span>{b}</span><i>{c}</i></li>' for a, b, c in zeiten)
    zsec = f'<section class="sec sz" id="zeiten"><div class="w sz-g"><div data-r>{head("Unterrichtszeiten", "Viermal pro Woche <em>Theorie.</em>", "In Fürstenau, Lingen und Bippen. Such dir den Abend aus, der zu dir passt.")}</div><ul class="sz-l">{zt}</ul></div></section>'
    return (hd(s, True) + hero_x(s, dict(
        img='h-fahrerin.jpg', pos='62% 30%', bg='h-auto.jpg', quick=['auto', 'anh', 'moto', 'lkw', 'trak'],
        ey='Fahrschule Scherpenberg · Fürstenau · Lingen · Bippen',
        h1='Der sichere Weg <em>zu deinem Führerschein.</em>',
        sub='Traditionell und innovativ zugleich: Unser motiviertes Team bringt dich schnell und sicher ans Ziel. Und das mit jeder Menge Spaß.',
        g1=('5,0 ★', '60 Google-Bewertungen')))
        + marquee(['Der sichere Weg!', 'Fürstenau', 'Lingen (Ems)', 'Bippen', 'B · BE', 'A', 'C · CE', 'T'], 'sm')
        + svc('vorteile', 'Darum Scherpenberg', 'Locker, ehrlich <em>und professionell.</em>', 'Unser Ziel: sichere und verantwortungsbewusste Fahrer.', [
            ('Zeit für jeden', 'Wir kümmern uns wirklich um unsere Schüler und nehmen uns für jeden Zeit.'),
            ('Entspannte Fahrstunden', 'Eher ein Kumpel-Verhältnis, das nimmt viel Nervosität.'),
            ('Gegen die Angst', 'Geduldige Fahrlehrer, die dir helfen, deine Angst zu überwinden.'),
            ('Immer erreichbar', 'Melde dich jederzeit, per Anruf oder WhatsApp.')], 'dk')
        + kl + zsec
        + story('ueber', 'Herzlich willkommen', 'Deine zuverlässige <em>Fahrschule.</em>', [
            'Seit vielen Jahren begleiten wir unsere Fahrschüler in Fürstenau, Lingen (Ems) und Bippen auf dem Weg zum Führerschein.',
            'Überzeuge dich selbst von unserer Qualität und unserem Service. Unsere Fahrschüler danken es uns mit 5,0 Sternen bei Google.'],
            'u-logo.jpg', cap='Fahrschule Scherpenberg', rev=True, cls='alt')
        + reviews(s, ['Meine Frau und ich haben hier beide den Führerschein gemacht. Ein besonderer Dank an Lisa: Sie verdient nicht 5, sondern 1.000 Sterne!',
                      'Ihr kümmert euch wirklich um eure Schüler und nehmt euch für jeden Zeit. Bei den Fahrstunden entsteht eher ein Kumpel-Verhältnis, das nimmt viel Nervosität.',
                      'Ich hatte meine Fahrstunden mit Horst. Er hat mir unglaublich geholfen, meine Angst zu überwinden, und war immer geduldig.',
                      'Die Fahrstunden waren entspannt, mit vielen Witzen, aber trotzdem professionell. Shout-out an Erik!'])
        + contact(s) + footer(s))

S = SITES['scherpenberg'] = site(
    slug='fahrschule-scherpenberg-fuerstenau', firma='Fahrschule Scherpenberg', web='fahrschule-scherpenberg.de', fonts='r15sch',
    title='Fahrschule Scherpenberg – Der sichere Weg! | Fürstenau, Lingen, Bippen', desc='Fahrschule Scherpenberg in Fürstenau, Lingen (Ems) und Bippen: B, BE, A, C, CE und T. 5,0 Sterne aus 60 Google-Bewertungen.',
    tel='0151 14100374', tel_i='+4915114100374', mail='', adresse='St.-Georg-Straße 1, 49584 Fürstenau', google=('5,0', 60),
    social=[('Instagram', 'https://instagram.com/fahrschule_scherpenberg'), ('WhatsApp', 'https://wa.me/4915114100374')],
    cta='Jetzt anmelden', nav=[('Vorteile', 'vorteile'), ('Klassen', 'klassen'), ('Zeiten', 'zeiten'), ('Stimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Fürstenau', 'Di &amp; Do 19:00'), ('Lingen', 'Mo – Do 19:00'), ('Bippen', 'Mo &amp; Mi 19:00')],
    form_lbl='Führerschein', form_opts=['Auto · B', 'Anhänger · BE', 'Motorrad · A', 'Lkw · C / CE', 'Traktor · T'],
    form_orte=['Fürstenau', 'Lingen (Ems)', 'Bippen'],
    form_h3='Zögere nicht!', form_p='Schick uns deine Daten, Elisa oder Michael melden sich bei dir.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Wir freuen uns, <em>dich kennenzulernen.</em>', kt_p='Elisa Kottig Rodrigues 0151 14100374, Michael Kottig 0151 17757116. Gern auch per WhatsApp.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#fff;--ink:#111;--mute:#555;--p:#b51d1d;--p-ink:#fff;--a:#b51d1d;--a-ink:#fff;--dk:#0b0b0b;--s:#fff;--s2:#f3f1f1;--fh:"Oswald",system-ui,sans-serif;--fb:"Montserrat",system-ui,sans-serif;--r:4px;--r2:6px;--br:2px;--mq-bg:#0b0b0b;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#111;--logo-h:46px;--ft-bg:#0b0b0b;--hx-ar:4/5;--hx-r:4px',
    css=EMO('11,11,11', 'center 60%', dark=True, pic_w=380) + '''
.hx h1,.h2{font-weight:700;text-transform:uppercase;letter-spacing:.005em;line-height:1}.hx h1 em,.h2 em{font-style:normal;color:#e23b3b}.alt .h2 em,.kt .h2 em,.sz .h2 em,.sk .h2 em,.rv .h2 em{color:#b51d1d}
.hx .pic{border:6px solid #fff;outline:3px solid #b51d1d;outline-offset:6px}.hx .gl{background:#b51d1d;color:#fff}.hx .gl b{color:#fff}
.hx::before{content:"";position:absolute;right:0;top:0;width:180px;height:100%;z-index:1;background:repeating-conic-gradient(#fff 0 25%,#0b0b0b 0 50%) 0 0/36px 36px;opacity:.08}
.sk{background:#0b0b0b;color:#fff}.sk .lead{color:#bbb}.sk .h2 em{color:#e23b3b}.sk-g{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:40px}
.si{all:unset;cursor:pointer;display:grid;gap:4px;justify-items:center;text-align:center;padding:16px 10px 20px;border:1px solid #2a2a2a;transition:border-color .25s,transform .25s}.si:hover{border-color:#b51d1d;transform:translateY(-4px)}
.si img{width:100%;max-width:170px}.si b{font:700 34px var(--fh);color:#e23b3b}.si span{font-size:14px;color:#ccc}@media(max-width:860px){.sk-g{grid-template-columns:repeat(3,1fr)}}
.sz-g{display:grid;grid-template-columns:1fr 1.1fr;gap:clamp(30px,5vw,70px);align-items:center}.sz-l{list-style:none;padding:0;margin:0;display:grid;gap:10px}
.sz-l li{display:grid;grid-template-columns:1fr auto auto;gap:20px;align-items:center;padding:18px 22px;background:#f3f1f1;border-left:5px solid #b51d1d}.sz-l b{font:700 22px var(--fh);text-transform:uppercase}.sz-l i{font-style:normal;font-weight:700;color:#b51d1d}
@media(max-width:860px){.sz-g{grid-template-columns:1fr}.sz-l li{grid-template-columns:1fr auto;}.sz-l i{grid-column:2}}
.st figure{background:#fff;box-shadow:none}.st figure img{object-fit:contain;padding:30px}.hd,.hd.scr{background:#fff!important}.hd .nav a{color:#111!important}.hx .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hd .logo img{height:46px}.ft img{background:#fff;padding:8px 12px}''')
S['bot'] = BOT('Sina', 'deine Scherpenberg-Lotsin', 'der Fahrschule Scherpenberg', S, ['B', 'BE', 'A', 'C', 'CE', 'T'],
    {'schnell': 'Theorie an vier Abenden pro Woche in Fürstenau, Lingen und Bippen.', 'ruhe': 'Unsere Fahrschüler beschreiben die Fahrstunden als entspannt, mit Witz und trotzdem professionell.', 'flex': 'Drei Orte, vier Theorieabende: Such dir aus, was passt.', 'angst': 'Unsere Fahrlehrer helfen dir geduldig, deine Angst zu überwinden.'},
    qa=[('whatsapp', 'Klar, schreib uns per WhatsApp an 0151 14100374.'), ('wo|ort|lingen|bippen|fürstenau', 'Unterricht gibt es in Fürstenau, Lingen (Ems) und Bippen, jeweils 19:00 bis 20:30 Uhr.'), ('instagram', 'Folge uns auf Instagram: @fahrschule_scherpenberg.')],
    tour=[('#vorteile', 'Darum Scherpenberg.'), ('#klassen', 'Unsere Klassen.'), ('#zeiten', 'Unterrichtszeiten.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('scherpenberg/img/i003.jpg', 700), 'h-auto.jpg': ('scherpenberg/img/i004.jpg', 2048), 'h-fahrerin.jpg': (PIX + 'emo15_scherpenberg.jpg', 0, (.42, 0, 1, 1)),
    'u-logo.jpg': ('scherpenberg/img/i015.jpg', 0),
    'i-b.jpg': ('scherpenberg/img/i001.jpg', 0), 'i-be.jpg': ('scherpenberg/img/i005.jpg', 0), 'i-a.jpg': ('scherpenberg/img/i010.jpg', 0), 'i-c.jpg': ('scherpenberg/img/i013.jpg', 0), 'i-ce.jpg': ('scherpenberg/img/i006.jpg', 0), 'i-t.jpg': ('scherpenberg/img/i011.jpg', 0)}
S['body'] = b_scherpenberg
