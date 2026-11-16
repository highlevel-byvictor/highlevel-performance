"""Runde 15 · Teil A: Haneburger, JeWa, Neehoff, Die Mobilmacher."""
from common import *
SITES = {}
HI = '/home/claude/r15raw/hi/'
PIX = '/home/claude/pixa/'

# ───────────── 1. Fahrschule Haneburger, Papenburg-Aschendorf ─────────────
def b_haneburger(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-laden.jpg', pos='50% 50%', bg='emo.jpg', quick=['auto', 'moto', 'trak', 'lkw'],
        ey='Fahrschule Haneburger · Aschendorf seit 1927',
        h1='Wir fahren mit Spaß <em>auf unser Jubiläum zu.</em>',
        sub='Fast 100 Jahre Fahrschule an der Großen Straße 100. Mofa, Motorrad, Traktor, Auto und Lkw: Wir machen dich sicher, und das mit Spaß.',
        g1=('100 Jahre', 'Jubiläum 2027'), g2=('40 Jahre', 'Fahrlehrer Frank Haneburger')))
        + marquee(['Mofa ab 15', 'AM · A1 · A2 · A', 'B · BE · B96', 'BF17', 'L · T Traktor', 'C1 · C · CE', 'Doppelstunden', 'Große Straße 100'], 'hm')
        + promo('jubilaeum', 'p-plakat.jpg', 'Jubiläum 2027', 'Die Fahrschule, <em>die bleibt!</em>',
                'Am 2. Mai hat Frank Haneburger sein Jubiläum „40 Jahre Fahrlehrer“ gefeiert. 2027 wird die Fahrschule 100 Jahre alt: Belegt ist sie durch einen historischen Führerschein vom 13. Mai 1927. Und Schluss ist damit noch lange nicht.',
                ['Seit 1927 in Aschendorf', '40 Jahre Erfahrung als Fahrlehrer', 'Jetzt anmelden und Teil unserer Geschichte werden'], 'Jetzt anmelden', 'alt')
        + svc('unterricht', 'Unser Unterricht', 'In 14 Tagen <em>durch die Theorie.</em>', 'Der Unterricht findet in unserem Raum an der Großen Straße 100 statt.', [
            ('Mo &amp; Mi, 19:00 – 20:30', 'Feste Theorieabende, jede Woche.'),
            ('Doppelstunden möglich', 'Auf Wunsch zwei Stunden an einem Abend. So schaffst du alle Pflichtstunden in 14 Tagen.'),
            ('Schnellkurse nach Absprache', 'Weitere Unterrichte und Schnellkurse planen wir gern mit dir.'),
            ('Sonderfahrten', 'Klasse B zum Beispiel: 5 Überland-, 4 Autobahn- und 3 Nachtfahrten.')])
        + klassen('klassen', 'Führerscheinklassen', 'Vom Mofa <em>bis zum Lkw.</em>', 'Tipp auf eine Klasse, dann sagt dir Hanna in 30 Sekunden, ob sie passt.', [
            ('Mofa', 'Mofa-Führerschein', '6 Doppelstunden Theorie und 90 Minuten Praxis, ohne praktische Prüfung.', 'ab 15', 'roller'),
            ('AM · A1', 'Roller &amp; 125er', 'Mit 16 auf zwei Rädern los.', 'ab 16', 'moto'),
            ('A2 · A', 'Motorrad', 'A2 ab 18, A direkt ab 24 oder nach zwei Jahren A2.', 'ab 18', 'moto'),
            ('B · BF17', 'Auto', 'Am besten mit 16½ anmelden und pünktlich mit 17 begleitet fahren.', 'ab 17', 'auto'),
            ('BE · B96', 'Anhänger', 'Für schwere Anhänger und Wohnwagen.', 'ab 18', 'anh'),
            ('L · T', 'Zugmaschinen', 'Traktor und Arbeitsmaschinen für Land- und Forstwirtschaft.', 'ab 16', 'trak'),
            ('C1 · C1E · C · CE', 'Lkw', 'Vom 7,5-Tonner bis zum Sattelzug.', 'ab 18', 'lkw')], 'dk')
        + gallery('fahrzeuge', 'Unsere Fahrzeuge', 'Damit lernst du <em>bei uns.</em>', [
            ('f-q3.jpg', 'w2', '50% 60%'), ('f-a4.jpg', '', '50% 60%'), ('f-moto.jpg', '', '50% 60%'), ('f-lkw.jpg', '', '50% 40%'), ('f-schild.jpg', 'w2', '50% 50%')])
        + story('ueber', 'Über uns', 'Tradition, <em>die mitfährt.</em>', [
            'Grundschüler des 4. Jahrgangs durften neulich die traditionsreiche Fahrschule besuchen. Frank Haneburger hat ihnen erzählt, dass die Fahrschule 2027 hundert Jahre alt wird. Vielleicht sogar älter: Gegründet worden sein könnte sie schon 1925.',
            'Unser Ziel ist ein sicherheitsbewusster und energiesparender Fahrer. Dafür bekommst du bei uns eine Top-Ausbildung, in der Klasse B mit dem Audi Q3.'],
            'u-raum.jpg', cap='Unsere Fahrschule an der Großen Straße 100', tl=[('1927', 'ältester Führerschein-Beleg'), ('2026', '40 Jahre Fahrlehrer Frank Haneburger'), ('2027', '100 Jahre Fahrschule')], rev=True)
        + reviews(s, ['Die beste Fahrschule mit tollen Fahrlehrern. Ich habe die Prüfung im ersten Versuch bestanden!',
                      'Hervorragender Unterricht und gute Unterlagen.',
                      'Hervorragend ausgebildet, seit 26 Jahren unfallfrei.',
                      'Gut investiertes Geld, und der Gutschein zum Abschluss war ein netter Bonus.'], 'alt')
        + contact(s) + footer(s))

S = SITES['haneburger'] = site(
    slug='fahrschule-haneburger-aschendorf', firma='Fahrschule Haneburger', web='haneburger.app', fonts='r15han',
    title='Fahrschule Haneburger – seit 1927 in Aschendorf | Papenburg', desc='Fahrschule Haneburger an der Großen Straße 100 in Aschendorf: Mofa, Motorrad, Traktor, Auto, Anhänger und Lkw. 100 Jahre Fahrschule 2027.',
    tel='04962 1299', tel_i='+4949621299', mail='', adresse='Große Straße 100, 26871 Papenburg-Aschendorf', google=('4,6', 10),
    logo_txt='<i>FH</i><span>Fahrschule Haneburger</span>',
    cta='Jetzt anmelden', nav=[('Jubiläum', 'jubilaeum'), ('Unterricht', 'unterricht'), ('Klassen', 'klassen'), ('Fahrzeuge', 'fahrzeuge'), ('Kontakt', 'kontakt')],
    hours=[('Theorie Mo', '19:00 – 20:30'), ('Theorie Mi', '19:00 – 20:30'), ('Weitere', 'nach Absprache')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1', 'Roller · AM', 'Mofa', 'Traktor · L / T', 'Lkw · C1 / C / CE'],
    form_h3='Jetzt anmelden', form_p='Schick uns deine Daten. Wir melden uns und besprechen deinen Start.', form_btn='Anmeldung abschicken',
    kt_ey='So erreichst du uns', kt_h2='Große Straße 100, <em>Aschendorf.</em>', kt_p='Ruf uns an unter 04962 / 12 99 oder komm zum Unterricht montags oder mittwochs um 19 Uhr vorbei.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#faf7f6;--ink:#1d1a1a;--mute:#5c5555;--p:#ac0000;--p-ink:#fff;--a:#ac0000;--a-ink:#fff;--dk:#1d1a1a;--s:#fff;--s2:#f1eae8;--fh:"Titillium Web",system-ui,sans-serif;--fb:"Titillium Web",system-ui,sans-serif;--r:6px;--r2:10px;--br:4px;--mq-bg:#ac0000;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.96);--hd-ink:#1d1a1a;--logo-h:40px;--ft-bg:#1d1a1a;--hx-ar:21/10;--hx-r:10px',
    css=EMO('250,247,246', 'center 35%', pic_w=520) + '''
.hx .pic{display:none}.hx .w{grid-template-columns:minmax(0,640px)!important}.hx{min-height:min(92vh,820px);display:flex;align-items:center}.hx>.w{flex:none}@media(max-width:820px){.hx.hasbg::before{background-position:78% 30%!important;height:52vh;bottom:auto!important}.hx{padding-top:calc(52vh - 40px)}}
.lt-logo{display:inline-flex;align-items:center;gap:10px;font:900 italic 19px/1 var(--fh);text-transform:uppercase;letter-spacing:.01em}.lt-logo i{background:#ac0000;color:#fff;padding:7px 9px;font-style:italic;transform:skewX(-10deg)}.lt-logo span{border-bottom:4px solid #ac0000;padding-bottom:3px}
.ft .lt-logo{color:#fff}.hx h1{font-weight:900;text-transform:uppercase;font-style:italic;letter-spacing:-.01em}.hx h1 em{display:block;color:#ac0000}
.h2{font-weight:900;font-style:italic;text-transform:uppercase;letter-spacing:-.01em}.h2 em{font-style:italic;color:#ac0000}.dk .h2 em{color:#ff6b6b}
.hx .gl{border-left:5px solid #ac0000;border-radius:6px}.hx .pic{transform:rotate(1.5deg)}.promo figure{max-width:380px;justify-self:center;transform:rotate(-2deg)}.promo figure img{box-shadow:0 30px 60px rgba(0,0,0,.25)}
.sv .row div{border-top:4px solid #ac0000;border-radius:0}.kl .k b{color:#ac0000;font-style:italic}.st figure{border-radius:6px}''')
S['bot'] = BOT('Hanna', 'deine Haneburger-Lotsin', 'der Fahrschule Haneburger', S, ['B', 'BF17', 'BE', 'B96', 'A', 'A2', 'A1', 'AM', 'Mofa', 'L', 'T', 'C1', 'C', 'CE'],
    {'schnell': 'Mit Doppelstunden schaffst du alle Pflichtstunden in 14 Tagen.', 'ruhe': 'Fast 100 Jahre Erfahrung: Bei uns lernst du sicher und mit Spaß.', 'flex': 'Weitere Unterrichte und Schnellkurse machen wir nach Absprache.', 'angst': 'Unser Ziel ist ein sicherer Fahrer. Wir nehmen uns die Zeit, die du brauchst.'},
    qa=[('jubil|100|1927', '2027 wird die Fahrschule Haneburger 100 Jahre alt. Belegt durch einen Führerschein vom 13. Mai 1927.'), ('trakt|landwirt|l |t ', 'Traktor-Führerschein L ab 16, T ab 16 bzw. 18. Bilden wir aus.'), ('lkw|c1|ce', 'Lkw bilden wir aus: C1, C1E, C und CE.')],
    tour=[('#jubilaeum', 'Fast 100 Jahre Fahrschule.'), ('#unterricht', 'So läuft der Unterricht.'), ('#klassen', 'Alle Klassen vom Mofa bis zum Lkw.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'h-laden.jpg': ('haneburger/img/i002.png', 0), 'emo.jpg': (PIX + 'emo15_haneburger_m.jpg', 0), 'p-plakat.jpg': ('haneburger/img/i009.jpeg', 0),
    'f-q3.jpg': ('haneburger/img/i003.jpeg', 0), 'f-a4.jpg': ('haneburger/img/i004.jpeg', 0), 'f-moto.jpg': ('haneburger/img/i006.jpeg', 0), 'f-lkw.jpg': ('haneburger/img/i010.jpeg', 0), 'f-schild.jpg': ('haneburger/img/i005.jpg', 0),
    'u-raum.jpg': ('haneburger/img/i007.jpg', 0)}
S['body'] = b_haneburger

# ───────────── 2. Fahrschule JeWa, Lingen · Haselünne · Beesten ─────────────
def b_jewa(s):
    filialen = f"""<section class="sec jf" id="standorte"><div class="w"><div data-r>{head('Unsere Filialen', 'Dreimal <em>im Emsland.</em>', 'Komm einfach zum Unterricht vorbei. Zwei Räume kannst du dir vorher schon im 360°-Rundgang ansehen.')}</div>
<div class="jf-g">
<article data-r><div><h3>Lingen</h3><p>Schwedenschanze 87<br>49809 Lingen (Ems)</p><span class="jf-t">Di &amp; Do · 18:30 – 20:30</span></div></article>
<article data-r><div><h3>Haselünne</h3><p>Hopfenmarkt 1<br>49740 Haselünne</p><span class="jf-t">Mo &amp; Mi · 18:30 – 20:30</span></div></article>
<article data-r><div><h3>Beesten</h3><p>Frerener Straße 11<br>49832 Beesten</p><span class="jf-t">Di · 18:00 – 21:30</span></div></article>
</div><div class="jf-p" data-r><img src="img/o-lingen.jpg" alt="Filiale der Fahrschule JeWa" loading="lazy"><img src="img/o-raum1.jpg" alt="Unterrichtsraum der Fahrschule JeWa" loading="lazy"><img src="img/o-raum2.jpg" alt="Unterrichtsraum der Fahrschule JeWa" loading="lazy"><img src="img/o-raum3.jpg" alt="Unterrichtsraum der Fahrschule JeWa" loading="lazy"></div><p class="jf-360"><a href="https://my.matterport.com/show/?m=Bh3DKwfY9Z6" target="_blank" rel="noopener">360°-Rundgang 1 ↗</a><a href="https://my.matterport.com/show/?m=46ettLSN49D" target="_blank" rel="noopener">360°-Rundgang 2 ↗</a></p></div></section>"""
    return (hd(s, False) + hero_x(s, dict(
        img='h-tiguan.jpg', pos='50% 50%', bg='h-duo.jpg', quick=['auto', 'moto', 'lkw', 'trak'],
        ey='Fahrschule JeWa · Schwindeler &amp; Schierling',
        h1='Dein Führerschein. <em>Unser Antrieb.</em>',
        sub='Jens und Waldemar bilden dich in Lingen, Haselünne und Beesten aus. Vom Roller bis zum Lkw, auf Wunsch auch auf Russisch.',
        g1=('3 Filialen', 'Lingen · Haselünne · Beesten')))
        + marquee(['Klasse AM', 'A · A2 · A1', 'B · BE · B17', 'C · CE · C1 · C1E', 'L · T', 'Deutsch &amp; Russisch', 'Fahren Lernen Max'], 'jm')
        + filialen
        + story('team', 'Wir sind Fahrschule JeWa', 'Zwei Fahrlehrer, <em>eine Leidenschaft.</em>', [
            '<b>Jens Schwindeler</b>, geboren in Haselünne, hat 2001 bei der Bundeswehr die Ausbildung zum Fahrlehrer für B/BE und C/CE gemacht und ist seit 2002 auch zivil Fahrlehrer. Er bildet A, B/BE, C/CE und T aus.',
            '<b>Waldemar Schierling</b> lebt mit seiner Familie in Lingen und ist seit 2010 Fahrlehrer. Er bildet A, B/BE, C/CE und T aus, auf Deutsch und auf Russisch.',
            'Und beide fahren in ihrer Freizeit am liebsten: Motorrad.'],
            't-jens.jpg', cap='Jens Schwindeler', cls='dk')
        + klassen('klassen', 'Fahrerlaubnisklassen', 'Was willst du <em>fahren?</em>', 'Tipp auf eine Klasse, dann prüft Jo mit dir, ob sie passt.', [
            ('AM', 'Roller', 'Mopeds bis 45 km/h, schon ab 15.', 'ab 15', 'roller'),
            ('A1 · A2 · A', 'Motorrad', 'Vom Leichtkraftrad bis zur offenen Maschine.', 'ab 16', 'moto'),
            ('B · B17', 'Auto', 'Mit 16½ anmelden und ab 17 begleitet fahren.', 'ab 17', 'auto'),
            ('BE', 'Anhänger', 'Für Gespanne bis 3,5 t Anhängelast.', 'ab 18', 'anh'),
            ('C1 · C · CE', 'Lkw', 'Für Beruf und Grundqualifikation.', 'ab 18', 'lkw'),
            ('L · T', 'Traktor', 'Land- und Forstwirtschaft.', 'ab 16', 'trak')])
        + promo('theorie', 'p-app.jpg', 'Theorie', 'Lernen mit <em>Fahren Lernen Max.</em>', 'Wir unterrichten den kompletten Grundstoff und geben dir dazu viele Tipps aus unserer langjährigen Erfahrung. Zuhause und unterwegs übst du mit dem Lernprogramm Fahren Lernen Max.',
                ['14 Themen im Grundstoff', 'Lern-App für zwischendurch', 'Sonderfahrten: 5 Überland, 4 Autobahn, 3 Nacht (B und A)'], 'Jetzt anmelden', 'alt')
        + gallery('flotte', 'Unsere Flotte', 'Bereit <em>für die Straße.</em>', [
            ('g1.jpg', 'w2', '50% 55%'), ('g2.jpg', '', '50% 60%'), ('g3.jpg', '', '50% 55%'), ('g4.jpg', '', '50% 60%'), ('g5.jpg', 'w2', '50% 60%')], 'dk')
        + reviews(s, ['Jens war mein Fahrlehrer für Klasse A, ich kann ihn jedem empfehlen. Keine Stunde war langweilig, und er hat alles verständlich erklärt.',
                      'Waldemar ist aufmerksam, geduldig und professionell. Ich habe beide Prüfungen beim ersten Mal bestanden.',
                      'Mit Abstand die beste Fahrschule in Lingen: tolles Team, super Unterricht und eine richtig gute App.',
                      'Neue und bequeme Autos, auf denen das Lernen Spaß macht.'], 'alt')
        + contact(s) + footer(s))

S = SITES['jewa'] = site(
    slug='fahrschule-jewa-lingen', firma='Fahrschule JeWa GmbH', web='fahrschule-jewa.de', fonts='r15jew',
    title='Fahrschule JeWa – Lingen, Haselünne, Beesten', desc='Fahrschule JeWa von Jens Schwindeler und Waldemar Schierling: AM, A, B, BE, C, CE, L und T in Lingen, Haselünne und Beesten. Unterricht auch auf Russisch.',
    tel='0171 2371388', tel_i='+491712371388', mail='info@fahrschule-jewa.de', adresse='Schwedenschanze 87, 49809 Lingen (Ems)', google=('4,8', 26),
    cta='Jetzt anmelden', nav=[('Filialen', 'standorte'), ('Team', 'team'), ('Klassen', 'klassen'), ('Theorie', 'theorie'), ('Kontakt', 'kontakt')],
    hours=[('Lingen', 'Di &amp; Do 18:30 – 20:30'), ('Haselünne', 'Mo &amp; Mi 18:30 – 20:30'), ('Beesten', 'Di 18:00 – 21:30')],
    form_lbl='Führerschein', form_opts=['Auto · B / B17', 'Anhänger · BE', 'Motorrad · A / A2 / A1', 'Roller · AM', 'Lkw · C / CE / C1', 'Traktor · L / T'],
    form_orte=['Lingen', 'Haselünne', 'Beesten'],
    form_h3='Melde dich noch heute an', form_p='Schick uns deine Daten, Jens oder Waldemar melden sich bei dir.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Mach heute <em>den ersten Schritt.</em>', kt_p='Waldemar 0171 2371388, Jens 0171 2371966, oder per Mail an info@fahrschule-jewa.de.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#2b2b2b;--ink:#f2f2f2;--mute:#b9b9b9;--p:#c8ff00;--p-ink:#0b0f2e;--a:#c8ff00;--a-ink:#0b0f2e;--dk:#1b1b1b;--s:#353535;--s2:#232323;--line:#474747;--fh:"Rubik",system-ui,sans-serif;--fb:"Rubik",system-ui,sans-serif;--r:14px;--r2:20px;--br:999px;--mq-bg:#020659;--mq-ink:#c8ff00;--hd-bg:rgba(20,20,20,.92);--hd-ink:#fff;--logo-h:46px;--ft-bg:#111;--hx-r:20px;--hx-ar:4/5',
    css=EMO('27,27,27', 'center 55%', dark=True, pic_w=380) + '''
.hx h1{font-weight:800}.hx h1 em,.h2 em{font:400 1em/1 "Permanent Marker",cursive;color:#c8ff00;font-style:normal}.h2{font-weight:800}
.hd .logo img{height:46px}.btn-a{box-shadow:0 0 0 0 rgba(200,255,0,.5);animation:jp 2.6s infinite}@keyframes jp{70%{box-shadow:0 0 0 14px rgba(200,255,0,0)}100%{box-shadow:0 0 0 0 rgba(200,255,0,0)}}
.hx .gl{background:rgba(2,6,89,.9);color:#fff}.hx .gl b{color:#c8ff00}
.jf-g{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}.jf-g article{background:#353535;border:2px solid #020659;border-radius:20px;overflow:hidden}
.jf-g figure{margin:0;aspect-ratio:16/10;overflow:hidden}.jf-g img{width:100%;height:100%;object-fit:cover;transition:transform .6s}.jf-g article:hover img{transform:scale(1.05)}
.jf-g div{padding:26px 24px 28px}.jf-p{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:22px}.jf-p img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:14px}@media(max-width:860px){.jf-p{grid-template-columns:1fr 1fr}}.jf-g h3{font:400 30px "Permanent Marker",cursive;color:#c8ff00;margin:0 0 6px}.jf-g p{margin:0;color:#ccc}.jf-t{display:inline-block;margin-top:14px;background:#020659;color:#fff;font-weight:700;font-size:14px;padding:7px 14px;border-radius:999px}
.jf-360{display:flex;gap:14px;flex-wrap:wrap;margin-top:24px}.jf-360 a{color:#c8ff00;font-weight:700;border:2px solid #c8ff00;border-radius:999px;padding:10px 18px;text-decoration:none}
@media(max-width:860px){.jf-g{grid-template-columns:1fr}}
.tm .grid{grid-template-columns:repeat(2,minmax(0,360px));justify-content:center}.tm figure img{aspect-ratio:4/5;object-position:50% 25%}
.kl .k{background:#353535;border-color:#474747}.kl .k b{color:#c8ff00}.rv .cd{background:#353535}.kt .bx{background:#353535}.kt input,.kt select,.kt textarea{background:#2b2b2b;color:#fff;border-color:#555}
.ft .logo img,.ft img{height:44px}''')
S['bot'] = BOT('Jo', 'dein JeWa-Lotse', 'der Fahrschule JeWa', S, ['B', 'B17', 'BE', 'A', 'A2', 'A1', 'AM', 'C', 'CE', 'C1', 'L', 'T'],
    {'schnell': 'Theorie an drei Standorten, an fünf Abenden pro Woche. Da findest du immer einen Termin.', 'ruhe': 'Unsere Fahrschüler loben vor allem, dass Jens und Waldemar geduldig und ruhig erklären.', 'flex': 'Drei Filialen: Lingen, Haselünne und Beesten.', 'angst': 'Bei uns lernst du entspannt und ohne Stress. Auf Wunsch auch auf Russisch.'},
    qa=[('russ', 'Waldemar bildet auf Deutsch und Russisch aus.'), ('360|rundgang|raum', 'Zwei unserer Räume kannst du dir im 360°-Rundgang ansehen. Die Links findest du bei den Filialen.'), ('app|max|lernen', 'Die Theorie übst du mit der App Fahren Lernen Max.')],
    tour=[('#standorte', 'Unsere drei Filialen.'), ('#team', 'Jens und Waldemar.'), ('#klassen', 'Alle Klassen auf einen Blick.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('jewa/img/i007.png', 0), 'h-tiguan.jpg': ('jewa/img/i029.jpg', 1100), 'h-duo.jpg': ('jewa/img/i024.jpg', 2000),
    'o-lingen.jpg': ('jewa/img/i043.jpg', 0), 'o-raum1.jpg': ('jewa/img/i047.jpg', 0), 'o-raum2.jpg': ('jewa/img/i012.jpg', 900), 'o-raum3.jpg': ('jewa/img/i048.jpg', 0),
    't-jens.jpg': ('jewa/img/i014.jpg', 0), 't-auto.jpg': ('jewa/img/i023.jpg', 900), 'p-app.jpg': ('jewa/img/i019.jpg', 1200),
    'g1.jpg': ('jewa/img/i034.jpg', 1800), 'g2.jpg': ('jewa/img/i030.jpg', 1000), 'g3.jpg': ('jewa/img/i035.jpg', 1400), 'g4.jpg': ('jewa/img/i042.jpg', 1400), 'g5.jpg': ('jewa/img/i032.jpg', 1800)}
S['body'] = b_jewa

# ───────────── 3. Fahrschule Bernd Neehoff, Haren (Ems) ─────────────
def b_neehoff(s):
    tage = [('1', 'Mo 16.11.', '1 &amp; 2'), ('2', 'Di 17.11.', '3 &amp; 4'), ('3', 'Mi 18.11.', '5 &amp; 6'), ('4', 'Do 19.11.', '7 &amp; 8'), ('5', 'Mo 23.11.', '9 &amp; 10'), ('6', 'Di 24.11.', '11 &amp; 12'), ('7', 'Mi 25.11.', '13 &amp; 14')]
    tg = ''.join(f'<li data-r><b>Tag {a}</b><span>{b}</span><small>Themen {c}</small></li>' for a, b, c in tage)
    kurs = f"""<section class="sec nk" id="kurs"><div class="w nk-g">
<div data-r><p class="ey">Theorie ab 7 Werktagen</p><h2 class="h2">Alle 14 Themen <em>in sieben Abenden.</em></h2>
<p class="lead">Seit 2018 läuft unser Unterricht als Kurs. Jeden Monat startet ein neuer, jeweils von 18 bis 21 Uhr. Danach behalten wir deinen Lernstand im Blick und legen den Prüfungstermin gemeinsam mit dir fest.</p>
<ul class="nk-v"><li>Mehr Zeit für Schule, Hobby und Beruf</li><li>Mehr Zeit für die Fahrstunden am Abend</li><li>Schnell und kompakt zum Führerschein</li></ul>
<p class="nk-hint">Nur begrenzte Plätze: am besten ein halbes Jahr vor dem Mindestalter anmelden.</p><a class="btn btn-a" href="#kontakt">Platz im nächsten Kurs sichern {AR}</a></div>
<div data-r="2" class="nk-plan"><p class="nk-h">Aktueller Kurs · 16. bis 25. November 2026 · 18 – 21 Uhr</p><ol>{tg}</ol><p class="nk-f">Kurse beginnen 1× im Monat. Änderungen vorbehalten.</p></div>
</div></section>"""
    return (hd(s, True) + hero_x(s, dict(
        img='h-emo.jpg', pos='78% 40%', bg='h-autos.jpg', quick=['auto', 'moto', 'lkw', 'trak'],
        ey='Fahrschule Neehoff · Haren (Ems) seit 1995',
        h1='Sicherheit, Vertrauen <em>und Spaß am Fahren.</em>',
        sub='Die älteste Fahrschule im Harener Ortskern. Theorie in nur sieben Abenden, Fahrstunden mit Bernd und Timo. Ruf an oder schreib per WhatsApp.',
        g1=('7 Abende', 'komplette Theorie')))
        + marquee(['Theorie in 7 Tagen', 'Kurse 1× im Monat', 'B · BE · BF17', 'A · A1 · A2 · AM', 'C · CE', 'L · T · Mofa', 'Lange Straße, Haren'], 'nm')
        + kurs
        + svc('vorteile', 'Darum Neehoff', 'Sprich erst mit uns, <em>bevor du dich entscheidest.</em>', 'Preise erklären wir dir lieber persönlich. Jeden Mittwoch von 17:00 bis 17:45 Uhr sind wir im Büro für dich da.', [
            ('Seit 1995 in Haren', 'Seit 2008 an der Lange Straße, die älteste Fahrschule im Ortskern.'),
            ('Kurs statt Warten', 'Theorie in sieben Abenden statt über Wochen verteilt.'),
            ('Bernd &amp; Timo', 'Zwei Fahrlehrer, die ruhig und geduldig erklären.'),
            ('WhatsApp', 'Infos und Anmeldung auch ganz einfach per WhatsApp.')])
        + klassen('klassen', 'Unsere Leistungen', 'Jede Klasse <em>ist eine Klasse für sich.</em>', 'Auch der Führerschein ab 17 ist bei uns möglich.', [
            ('B · BF17', 'Auto', 'Ab 17 begleitet, ab 18 allein.', 'ab 17', 'auto'),
            ('BE', 'Anhänger', 'Gespanne bis 7.000 kg.', 'ab 18', 'anh'),
            ('A · A1 · A2', 'Motorrad', 'Vom 125er bis zur großen Maschine.', 'ab 16', 'moto'),
            ('AM · Mofa', 'Roller', 'Der erste Schritt in die Freiheit.', 'ab 15', 'roller'),
            ('C · CE', 'Lkw', 'Für den Beruf hinterm Steuer.', 'ab 18', 'lkw'),
            ('L · T', 'Traktor', 'Für Hof und Feld.', 'ab 16', 'trak')], 'alt')
        + gallery('raeume', 'Fahrschulbilder', 'Komm vorbei und <em>schau dich um.</em>', [
            ('r1.jpg', 'w2', '50% 50%'), ('r2.jpg', '', '50% 50%'), ('r3.jpg', '', '50% 50%'), ('r4.jpg', '', '50% 50%'), ('r5.jpg', 'w2', '50% 60%')])
        + eltern('erste-hilfe', 'p-eh.jpg', 'Erste-Hilfe-Kurs', 'Erste Hilfe <em>ohne Anmeldung.</em>', 'Die Sanitätsschule Schmitz bietet 2026 regelmäßig samstags die Erste-Hilfe-Ausbildung an, ganz ohne Anmeldung. Die Termine findest du auf dem Aushang.', ['Samstags, ohne Anmeldung', 'Bescheinigung für deinen Antrag', 'Termine auf dem Aushang'], 'Fragen? Schreib uns', 'dk', True)
        + reviews(s, ['Theorie und Praxis im ersten Versuch bestanden. Der Unterricht war verständlich aufgebaut, die Fahrstunden haben immer Spaß gemacht.',
                      'Der Crashkurs in Theorie und danach die Fahrstunden mit Timo und Bernd: geduldig, kompetent, und schnell war die Prüfung geschafft.',
                      'Ich habe mich vom ersten Tag an wohlgefühlt, die Fahrlehrer sind ruhig und angenehm. Auf jede Stunde habe ich mich gefreut.',
                      'Meine Tochter hat hier den Führerschein gemacht und beide Prüfungen auf Anhieb bestanden. Klare Empfehlung.'])
        + contact(s) + footer(s))

S = SITES['neehoff'] = site(
    slug='fahrschule-neehoff-haren', firma='Fahrschule Bernd Neehoff', web='neehoff.de', fonts='r15nee',
    title='Fahrschule Neehoff – Theorie in 7 Tagen | Haren (Ems)', desc='Fahrschule Bernd Neehoff in Haren (Ems) seit 1995: Theorie in sieben Abenden, Kurse jeden Monat, alle Klassen von Mofa bis Lkw.',
    tel='0171 5086270', tel_i='+491715086270', mail='info@neehoff.de', adresse='Lange Straße 56, 49733 Haren (Ems)', google=('4,7', 93),
    cta='Kursplatz sichern', nav=[('7-Tage-Kurs', 'kurs'), ('Vorteile', 'vorteile'), ('Klassen', 'klassen'), ('Bilder', 'raeume'), ('Kontakt', 'kontakt')],
    hours=[('Büro', 'Mi 17:00 – 17:45'), ('Theoriekurs', '18:00 – 21:00'), ('Timo', '0151 14905245')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17', 'Anhänger · BE', 'Motorrad · A / A1 / A2', 'Roller · AM / Mofa', 'Lkw · C / CE', 'Traktor · L / T'],
    form_h3='Platz im Kurs sichern', form_p='Schick uns deine Daten. Bernd oder Timo melden sich bei dir.', form_btn='Anmeldung abschicken',
    kt_ey='Anmeldung &amp; Infos', kt_h2='Ruf an oder <em>schreib per WhatsApp.</em>', kt_p='Bernd 0171 / 50 86 270, Timo 0151 / 14 90 52 45. Im Büro jeden Mittwoch von 17:00 bis 17:45 Uhr.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#f6f7f8;--ink:#1b232c;--mute:#55606b;--p:#e3000f;--p-ink:#fff;--a:#e3000f;--a-ink:#fff;--dk:#242f3a;--s:#fff;--s2:#e9edf0;--fh:"Archivo",system-ui,sans-serif;--fb:"Archivo",system-ui,sans-serif;--r:8px;--r2:12px;--br:6px;--mq-bg:#242f3a;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#1b232c;--logo-h:52px;--ft-bg:#242f3a;--hxw-ar:24/9;--hx-r:12px',
    css=EMO('246,247,248', '60% 70%', pic_w=400) + '''
.hx h1{font-weight:900;font-style:italic;text-transform:uppercase;letter-spacing:-.02em}.hx h1 em{color:#e3000f}.h2{font-weight:900;font-style:italic;letter-spacing:-.02em}.h2 em{color:#e3000f}.dk .h2 em{color:#ff5a63}
.hx .gl{background:#e3000f;color:#fff}.hx .gl b{color:#fff}
.nk{background:#242f3a;color:#fff}.nk .ey{color:#ff8a90}.nk .lead{color:#d6dde3}.nk-g{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5vw,70px);align-items:start}
.nk-v{list-style:none;padding:0;margin:20px 0}.nk-v li{padding:8px 0 8px 30px;position:relative;font-weight:600}.nk-v li::before{content:"✓";position:absolute;left:0;color:#e3000f;font-weight:900}
.nk-hint{border-left:4px solid #e3000f;padding-left:14px;color:#d6dde3;margin:0 0 24px}
.nk-plan{background:#fff;color:#1b232c;border-radius:12px;padding:26px;box-shadow:0 30px 70px rgba(0,0,0,.35)}.nk-h{font-weight:800;margin:0 0 16px;color:#e3000f}
.nk-plan ol{list-style:none;padding:0;margin:0;display:grid;gap:8px}.nk-plan li{display:grid;grid-template-columns:70px 1fr auto;align-items:center;gap:12px;padding:12px 14px;background:#f1f3f5;border-radius:8px}
.nk-plan li b{font-weight:900;font-style:italic;color:#e3000f}.nk-plan li small{color:#55606b}.nk-f{margin:14px 0 0;font-size:14px;color:#55606b}
@media(max-width:860px){.nk-g{grid-template-columns:1fr}}.el figure{max-width:360px;justify-self:center}.kl .k b{color:#e3000f;font-style:italic}''')
S['bot'] = BOT('Nele', 'deine Neehoff-Lotsin', 'der Fahrschule Neehoff', S, ['B', 'BF17', 'BE', 'A', 'A1', 'A2', 'AM', 'Mofa', 'C', 'CE', 'L', 'T'],
    {'schnell': 'Die ganze Theorie in sieben Abenden. Jeden Monat startet ein neuer Kurs.', 'ruhe': 'Unsere Fahrschüler schreiben, dass Bernd und Timo ruhig und geduldig erklären.', 'flex': 'Fahrstunden in den Abendstunden, weil die Theorie schnell erledigt ist.', 'angst': 'Viele haben sich bei uns vom ersten Tag an wohlgefühlt. Das schaffen wir auch mit dir.'},
    qa=[('kurs|termin|wann', 'Der aktuelle Kurs läuft vom 16. bis 25. November 2026, jeweils 18 bis 21 Uhr. Kurse starten 1× im Monat.'), ('preis|kost', 'Preise erklären wir dir lieber persönlich, jeden Mittwoch von 17:00 bis 17:45 Uhr im Büro.'), ('erste hilfe', 'Erste Hilfe gibt es bei der Sanitätsschule Schmitz, samstags und ohne Anmeldung.')],
    tour=[('#kurs', 'Theorie in sieben Abenden.'), ('#vorteile', 'Warum Neehoff.'), ('#klassen', 'Alle Klassen.'), ('#kontakt', 'Hier sicherst du dir deinen Platz.')])
S['img'] = {'logo.png': ('neehoff/img/i007.jpeg', 0, 'trim'), 'h-autos.jpg': ('neehoff/img/i002.jpg', 0), 'h-emo.jpg': (PIX + 'emo15_neehoff.jpg', 0, (.12, 0, .78, 1)),
    'r1.jpg': ('neehoff/img/i010.jpg', 0), 'r2.jpg': ('neehoff/img/i004.jpeg', 1000), 'r3.jpg': ('neehoff/img/i006.jpeg', 1000), 'r4.jpg': ('neehoff/img/i011.jpg', 0), 'r5.jpg': ('neehoff/img/i003.jpeg', 1600, (0, .2, 1, .7)),
    'p-eh.jpg': ('neehoff/img/i009.jpg', 900)}
S['body'] = b_neehoff

# ───────────── 4. Die Mobilmacher, Meppen · Twist ─────────────
def b_mobilmacher(s):
    st = [('Meppen I', 'Gropiusplatz 7, 49716 Meppen', 'Unterricht Di 18:30 – 20:00', 'Anmeldung Di 17:30 – 18:30', 'o-gropius.jpg'),
          ('Meppen II', 'Schullendamm 67, 49716 Meppen', 'Unterricht Mi 18:30 – 20:00', 'Anmeldung Mi 17:30 – 18:30', 'o-schullendamm.jpg'),
          ('Twist', 'Auf dem Bült 30, 49767 Twist', 'Unterricht Di &amp; Do 19:00 – 20:30', 'Anmeldung 18:00 – 19:00', 'o-twist.jpg')]
    so = ''.join(f'<article class="mo" data-r><div><h3>{a}</h3><p>{b}</p><p class="mo-t"><b>{c}</b><br>{d}</p><a href="{MAPL(b)}" target="_blank" rel="noopener">Route planen {AR}</a></div></article>' for a, b, c, d, i in st)
    standorte = f'<section class="sec mst" id="standorte"><div class="w"><div data-r>{head("Unsere Standorte", "Zweimal Meppen, <em>einmal Twist.</em>", "Zum Anmelden kommst du einfach 15 Minuten vor dem Unterricht vorbei oder rufst an.")}</div><div class="mst-p" data-r><img src="img/o-gropius.jpg" alt="Fahrschule Die Mobilmacher von außen" loading="lazy"><img src="img/o-schullendamm.jpg" alt="Fahrschule Die Mobilmacher von außen" loading="lazy"><img src="img/o-twist.jpg" alt="Schaufenster der Mobilmacher" loading="lazy"></div><div class="mst-g">{so}</div></div></section>'
    tm = [('Martin', 'Seit 16 Jahren Fahrlehrer', 'B/BE und A · Ausbildungsfahrlehrer'), ('Simone', 'Seit 25 Jahren Fahrlehrerin', 'B/BE, A und ASF · Ausbildungsfahrlehrerin'),
          ('Jörg', 'Seit 21 Jahren Fahrlehrer', 'B/BE'), ('Henning', 'Seit 6 Jahren Fahrlehrer', 'B/BE und Flurförderzeuge'), ('Robert', 'Seit 2 Jahren Fahrlehrer', 'B/BE')]
    tl = ''.join(f'<li data-r><b>{a}</b><span>{b}</span><small>{c}</small></li>' for a, b, c in tm)
    team_sec = f'''<section class="sec mtm" id="team"><div class="w mtm-g"><div data-r>{head("Unser Team", "Zusammen fast <em>70 Jahre Erfahrung.</em>", "Fünf Fahrlehrer, die dich auf ganz unkomplizierte Weise zum Führerschein bringen.")}<ul class="mtm-l">{tl}</ul></div>
<div class="mtm-p" data-r="2"><figure><img src="img/t1.jpg" alt="Fahrlehrerin der Mobilmacher am Fahrschulauto" loading="lazy"></figure><figure><img src="img/t2.jpg" alt="Fahrlehrer der Mobilmacher am Fahrschulauto" loading="lazy"></figure><figure><img src="img/t3.jpg" alt="Fahrlehrer der Mobilmacher" loading="lazy"></figure><figure><img src="img/t4.jpg" alt="Motorradausbildung bei den Mobilmachern" loading="lazy"></figure></div></div></section>'''
    return (hd(s, True) + hero_x(s, dict(
        img='h-team.jpg', pos='35% 30%', bg='emo.jpg', quick=['auto', 'moto', 'roller', 'anh'],
        ey='Die Mobilmacher · Meppen &amp; Twist',
        h1='Du willst <em>MOBIL werden?</em>',
        sub='Keine Lust mehr, dich von Eltern und Freunden fahren zu lassen? Wir bringen dich unkompliziert zum Führerschein. Egal ob Auto oder Motorrad: Komm zu uns!',
        g1=('Fair Fahren!', 'schnell und effizient zum Führerschein')))
        + marquee(['Fair Fahren!', 'B · BE', 'A · A1 · A2', 'Mofa · AM', 'Führerschein mit 17', 'ASF', 'Meppen &amp; Twist', 'WhatsApp'], 'mm')
        + svc('kompakt', 'Kompakt zum Führerschein', 'Wir machen <em>keine Umwege.</em>', 'Du durchläufst die Stufen zum Führerschein effizient und gut abgestimmt. So sparst du am Ende Zeit, Nerven und Geld.', [
            ('Kompakt', 'Gut abgestimmte Schritte von der Anmeldung bis zur Prüfung.'), ('Effizienter', 'Kürzere Lernzeit, weil nichts doppelt läuft.'),
            ('Günstiger', 'Weniger Umwege heißt weniger Kosten.'), ('Faire Preise', 'Dafür stehen wir mit unserem Namen: Fair Fahren!')])
        + standorte
        + klassen('klassen', 'Unser Schulungsangebot', 'Auto, Motorrad <em>oder Roller?</em>', 'Tipp auf eine Klasse, dann sagt dir Mo, ob sie passt.', [
            ('B', 'Auto', 'Kraftwagen bis 3,5 t, Anhänger bis 750 kg inklusive.', 'ab 17', 'auto'),
            ('BE', 'Anhänger', 'Anhänger über 750 kg bis 3.500 kg.', 'ab 18', 'anh'),
            ('A1 · A2 · A', 'Motorrad', 'Vom Leichtkraftrad bis zur offenen Maschine.', 'ab 16', 'moto'),
            ('Mofa · AM', 'Mofa &amp; Mopeds', 'Bis 25 bzw. 45 km/h.', 'ab 15', 'roller')], 'dk')
        + eltern('mit17', 'e-17.jpg', 'Führerschein mit 17', 'Schon mit 17 <em>hinters Steuer.</em>', 'Ein halbes Jahr vor deinem 17. Geburtstag kannst du starten. Nach der Prüfung fährst du in Begleitung, mit 18 tauschst du den vorläufigen Führerschein gegen den Kartenführerschein.',
               ['Start bis 6 Monate vor dem 17. Geburtstag', 'Begleitung ab 30 Jahren, 5 Jahre Klasse B, max. 1 Punkt', 'Für den Antrag: Passbild, Sehtest, Erste Hilfe, Ausweis'], 'Jetzt mit 16½ anmelden', 'alt')
        + team_sec
        + reviews(s, ['Meine Freundin und ich haben hier beide den Motorradführerschein gemacht. Alle sind freundlich, verständnisvoll und professionell, auch wenn mal etwas nicht klappt.',
                      'Ich habe mich in jeder Fahrstunde wohlgefühlt und war super auf die Prüfung vorbereitet. Auch der Theorieunterricht war gut aufgebaut.',
                      'Nach vielen Stunden in einer anderen Fahrschule bin ich gewechselt. Wenige Stunden später hatte ich bestanden. Schade, dass ich nicht von Anfang an hier war!',
                      'Faire Preise, zuverlässig bei den Terminen und super nette Leute. Ich hatte meinen Führerschein relativ schnell.'], 'alt')
        + contact(s) + footer(s))

S = SITES['mobilmacher'] = site(
    slug='die-mobilmacher-meppen', firma='Fahrschule Die Mobilmacher', web='die-mobilmacher.info', fonts='r15mob',
    title='Die Mobilmacher – Fahrschule in Meppen & Twist', desc='Fahrschule Die Mobilmacher von Martin Steinkamp und Simone Gröninger: kompakt, fair und effizient zum Führerschein in Meppen und Twist.',
    tel='0176 22882443', tel_i='+4917622882443', mail='info@die-mobilmacher.info', adresse='Gropiusplatz 7, 49716 Meppen', google=('5,0', 32),
    social=[('WhatsApp', 'https://api.whatsapp.com/send?phone=4917622882443'), ('Facebook', 'https://www.facebook.com/DieMobilmacher')],
    cta='Jetzt anmelden', nav=[('Kompakt', 'kompakt'), ('Standorte', 'standorte'), ('Klassen', 'klassen'), ('Mit 17', 'mit17'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Meppen I', 'Di ab 17:30'), ('Meppen II', 'Mi ab 17:30'), ('Twist', 'Di &amp; Do ab 18:00')],
    form_lbl='Führerschein', form_opts=['PKW · B', 'Anhänger · BE', 'Motorrad · A / A1 / A2', 'Mofa / AM', 'Führerschein mit 17', 'ASF-Seminar'],
    form_orte=['Meppen · Gropiusplatz', 'Meppen · Schullendamm', 'Twist'],
    form_h3='Jetzt anmelden', form_p='Schick uns deine Daten oder schreib per WhatsApp.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Ruf an oder <em>melde dich per WhatsApp!</em>', kt_p='Martin 0176 22882443, Simone 0171 7830607.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#fff;--ink:#2a2a2c;--mute:#6f7072;--p:#d4007a;--p-ink:#fff;--a:#d4007a;--a-ink:#fff;--dk:#2a2a2c;--s:#fff;--s2:#f6eef3;--fh:"Saira",system-ui,sans-serif;--fb:"Saira",system-ui,sans-serif;--r:16px;--r2:24px;--br:999px;--mq-bg:#d4007a;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#2a2a2c;--logo-h:48px;--ft-bg:#6f7072;--hx-ar:16/10',
    css=EMO('255,255,255', 'center 55%', pic_w=560) + '''
.hx h1{font-weight:800;margin-top:22px;line-height:1.08}.hx h1 em{color:#d4007a}.h2{font-weight:800}.h2 em{color:#d4007a}.dk .h2 em{color:#ff6fbd}
.hx .pic{border-radius:24px 24px 24px 120px}.hx .gl{background:#d4007a;color:#fff;border-radius:50%;width:150px;height:150px;display:grid;place-content:center;text-align:center;padding:16px;font-size:12.5px;transform:rotate(-8deg);left:auto!important;right:-14px;top:auto!important;bottom:-34px!important}.hx .pic{overflow:visible}.hx .pic img{border-radius:24px 24px 24px 120px}.hx .gl b{color:#fff;font-style:italic;font-size:22px}
.mst-p{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:14px;margin-top:36px}.mst-p img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:20px}.mst-g{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}.mo{background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 20px 50px rgba(212,0,122,.12)}.mo figure{margin:0;aspect-ratio:4/3;overflow:hidden}.mo img{width:100%;height:100%;object-fit:cover}
.mo div{padding:22px 24px 26px}.mo h3{margin:0;font:800 26px var(--fh);color:#d4007a}.mo p{margin:6px 0 0;color:#6f7072}.mo .mo-t{margin-top:12px;color:#2a2a2c}.mo a{display:inline-block;margin-top:14px;color:#d4007a;font-weight:700;text-decoration:none}.mo a svg{width:16px;height:16px;vertical-align:-3px}
.mtm{background:#f6eef3}.mtm-g{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5vw,70px);align-items:center}.mtm-l{list-style:none;padding:0;margin:28px 0 0;display:grid;gap:10px}
.mtm-l li{background:#fff;border-radius:16px;padding:14px 18px;display:grid;grid-template-columns:110px 1fr;gap:2px 14px}.mtm-l b{grid-row:span 2;font:800 22px var(--fh);color:#d4007a;align-self:center}.mtm-l small{color:#6f7072}
.mtm-p{display:grid;grid-template-columns:1fr 1fr;gap:14px}.mtm-p figure{margin:0;border-radius:20px;overflow:hidden;aspect-ratio:4/3}.mtm-p figure:nth-child(even){transform:translateY(26px)}.mtm-p img{width:100%;height:100%;object-fit:cover}
@media(max-width:860px){.mst-p{grid-template-columns:1fr 1fr}.mst-g,.mtm-g{grid-template-columns:1fr}.hx .gl{width:118px;height:118px;right:4px;bottom:-40px!important;font-size:10.5px}.hx .gl b{font-size:17px}.hx{padding-bottom:90px}}.kl .k b{color:#d4007a}.ft img{background:#fff;padding:6px 10px;border-radius:10px}''')
S['bot'] = BOT('Mo', 'dein Mobilmacher-Lotse', 'den Mobilmachern', S, ['B', 'BE', 'A', 'A1', 'A2', 'AM', 'Mofa'],
    {'schnell': 'Kompakt zum Führerschein: Wir machen keine Umwege.', 'ruhe': 'Unsere Fahrschüler loben, dass bei uns alles geduldig erklärt wird, auch wenn mal etwas nicht klappt.', 'flex': 'Drei Standorte in Meppen und Twist, Unterricht an drei Abenden.', 'angst': 'Viele kommen nach schlechten Erfahrungen zu uns und bestehen nach wenigen Stunden.'},
    qa=[('17|begleit', 'Führerschein mit 17? Du kannst bis zu sechs Monate vor deinem 17. Geburtstag starten.'), ('whatsapp', 'Klar, schreib uns per WhatsApp an 0176 22882443.'), ('preis|kost|fair', 'Faire Preise sind unser Versprechen. Die Details besprechen wir gern mit dir.')],
    tour=[('#kompakt', 'Kompakt zum Führerschein.'), ('#standorte', 'Unsere drei Standorte.'), ('#mit17', 'Führerschein mit 17.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': (HI + 'mob_t70.png', 0), 'h-team.jpg': (HI + 'mob_i010.jpg', 0, (.12, 0, .78, 1)), 'emo.jpg': (PIX + 'emo15_mobilmacher2.jpg', 0),
    'o-gropius.jpg': ('mobilmacher/img/i027.jpg', 0), 'o-schullendamm.jpg': ('mobilmacher/img/i021.jpg', 0), 'o-twist.jpg': ('mobilmacher/img/i009.jpg', 0),
    'e-17.jpg': (HI + 'mob_i016.jpg', 0, (.05, 0, .65, 1)),
    't1.jpg': ('mobilmacher/img/i011.jpg', 0), 't2.jpg': ('mobilmacher/img/i019.jpg', 0), 't3.jpg': ('mobilmacher/img/i023.jpg', 0), 't4.jpg': ('mobilmacher/img/i004.jpg', 0)}
S['body'] = b_mobilmacher
