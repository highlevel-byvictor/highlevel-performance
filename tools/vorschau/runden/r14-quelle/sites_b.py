"""Runde 14 · Teil B: City Fahrschule, Moschitz, Kindermann, Beinke, St. Eggert."""
from common import *
SITES = {}

# ───────────── 6. City Fahrschule, Hasbergen · Osnabrück & Osnabrücker Land ─────────────
def _city_hero(s):
    sl = [('h-team.jpg', 'Schön, Dich hier zu sehen …!', 'Wir sind das Team der City Fahrschule.', 'Unser Team', '#team'),
          ('h-50.jpg', '50 Jahre City Fahrschule', 'Seit 1975 in und um Osnabrück.', 'Unsere Geschichte', '#geschichte'),
          ('h-kunden.jpg', '… und das sind unsere Kunden!', 'Tausende Fahrschüler haben bei uns ihren Führerschein gemacht.', 'Zur Anmeldung', '#anmeldung'),
          ('h-flotte.jpg', 'Berufskraftfahrer sind bei uns richtig.', 'Wir sind zertifizierter Bildungsanbieter.', 'Mehr erfahren', '#fuhrpark'),
          ('h-bikes.jpg', 'Zweiräder.', 'Vom Roller bis zum Motorrad.', 'Mehr erfahren', '#fuhrpark'),
          ('h-traktor.jpg', 'Landlust.', 'Mit Führerschein Klasse T.', 'Mehr erfahren', '#fuhrpark')]
    slides = ''.join(f'''<div data-slide class="{'on' if i == 0 else ''}"><img src="img/{im}" alt="{E(t)}" {'fetchpriority="high"' if i == 0 else 'loading="lazy"'}><div class="cs-cap"><div class="w"><b>{t}</b><span>{x}</span><a href="{href}">{btn} {AR}</a></div></div></div>''' for i, (im, t, x, btn, href) in enumerate(sl))
    dots = ''.join(f'<button data-dot class="{"on" if i == 0 else ""}" aria-label="Bild {i+1}"></button>' for i in range(len(sl)))
    return f'''<section class="cs" id="top" data-slider="6500"><div class="cs-sl">{slides}<button class="cs-ar l" data-prev aria-label="Zurück">‹</button><button class="cs-ar r" data-next aria-label="Weiter">›</button><div class="cs-dots">{dots}</div></div>
<div class="cs-bar"><div class="w">{chip(s)}<div class="ctas"><a class="btn btn-a" href="#anmeldung">{s['cta']} {AR}</a><a class="btn btn-o" href="tel:{s['tel_i']}">{PH} {s['tel']}</a></div></div></div>
<div class="cs-in"><div class="w"><div data-r><p class="ey">City Fahrschule · seit 1975</p><h1>Schön, Dich <em>hier zu sehen.</em></h1></div><div data-r="2"><p class="sub">Wir sind ein Team aus 30 Leuten und bilden in und um Osnabrück aus: alles außer Bus. Mit Simulator, Lerncenter, Ferienfahrschule und Online-Anmeldung in vier Schritten.</p>{quick(s, dict(quick=['auto', 'moto', 'roller', 'anh', 'lkw', 'trak']))}</div></div></div></section>'''

def _city_kunden():
    return '''<section class="sec ck" id="kunden"><div class="w" data-r><p class="ey">Unsere Fahrschüler</p><h2 class="h2">… und das sind <em>unsere Kunden!</em></h2></div>
<figure class="ck-f" data-r="2"><img src="img/h-kunden.jpg" alt="Collage aus Fotos von Fahrschülern der City Fahrschule mit ihrem Führerschein" loading="lazy"></figure>
<div class="w ck-b" data-r><p>Tausende haben bei uns ihren Führerschein gemacht. Du bist die oder der Nächste.</p><a class="btn btn-a" href="#anmeldung">Jetzt online anmelden ''' + AR + '''</a></div></section>'''

def b_city(s):
    return (hd(s, False) + _city_hero(s)
        + marquee(['A · A2 · A1', 'B · B196 · B96 · BE', 'C · CE · C1', 'L · T', 'Simulator', 'Ferienfahrschule', 'Lerncenter', 'Fahrschulwechsel'], 'cm')
        + vgrid('video', 'Mittendrin', 'So fühlt sich <em>City an.</em>', 'Ein Projekt unserer Fahrschüler: vom ersten Schritt bis ins Auto.', [
            ('Schülerprojekt: Neu in Bramsche', 'mp4', 'v-city.mp4', 'v-city.jpg')], 'alt')
        + _city_kunden()
        + ablauf('anmeldung', 'Online anmelden', 'In vier Schritten <em>angemeldet.</em>', 'Wie bei den Großen, nur persönlicher: Du klickst dich durch, wir melden uns mit allen Infos und deiner Anmeldebestätigung.', [
            ('Fahrzeug wählen', 'Auto, Motorrad, Roller, Lkw oder Traktor.'), ('Führerscheintyp', 'Die passende Klasse, auch als Doppelführerschein.'),
            ('Kursart', 'Normal oder als Ferienfahrschule.'), ('Anmelden', 'Abschicken, Bestätigung kommt per Mail.')])

        + flotte('fuhrpark', 'Unser Fuhrpark', 'Vom Mofa <em>bis zum Actros.</em>', 'Alles mit dem City-Schriftzug, alles gepflegt. Auf diesen Fahrzeugen lernst du.', [
            ('f-id3.jpg', 'VW ID.3', 'Elektro · Klasse B', '50% 55%'), ('f-polo.jpg', 'VW Polo', 'Klasse B', '50% 55%'), ('f-tcross.jpg', 'VW T-Cross', 'Klasse B', '50% 55%'),
            ('f-hornet.jpg', 'Honda CB 750 Hornet', 'Klasse A / A2', '50% 55%'), ('f-actros.jpg', 'Mercedes Actros', 'Klasse C / CE', '50% 55%'), ('f-trak.jpg', 'Traktor', 'Klasse L / T', '50% 55%')], 'dk')
        + faces('team', 'Unser Team', 'Fahrlehrer, die <em>Bock auf ihren Job haben.</em>', 'Geschäftsführer Simon Michalowski und das City-Team. Bei uns findest du für jede Klasse den passenden Fahrlehrer.', [
            (f't{i}.jpg', '') for i in range(1, 13)])
        + story('geschichte', 'Unsere Geschichte', 'Seit 1975 <em>auf der Straße.</em>', [
            '1975 hat Gerd Michalowski die erste Fahrschule in Westerkappeln eröffnet. Seit 1977 gibt es die City Fahrschule in Hasbergen, bis heute in der Eichendorffstraße 2.',
            'Weil die Fahrschule in Hasbergen immer voller wurde, kam 1996 Ohrbeck dazu, später weitere Standorte. Heute ist City ein Team von 30 Leuten mit acht Fahrschulen.'],
            'st-50.jpg', cap='50 Jahre City Fahrschule', tl=[('1975', 'erste Fahrschule in Westerkappeln'), ('1977', 'Start in Hasbergen'), ('heute', '30 Leute, 8 Fahrschulen')], cls='alt')
        + orte('standorte', 'Standorte', 'Immer eine City <em>in deiner Nähe.</em>', '', [
            ('Hasbergen', 'Eichendorffstraße 2', 'seit 1977'), ('Osnabrück', 'mehrere Standorte', ''), ('Bissendorf', '', ''), ('Borgloh', '', ''), ('Bramsche', '', 'neu'), ('Lüstringen', '', ''), ('Wallenhorst', '', '')])
        + reviews(s, ['Traum vom Motorradführerschein erfüllt! Man wird hier nicht einfach durchgeschleust, sondern lernt wirklich sicher zu fahren. Der Prüfer meinte: absolut nichts auszusetzen.',
                      'Klasse A in zwei Monaten. Alles lief schnell und unkompliziert, toller Fahrlehrer, und auch der Chef war super freundlich.',
                      'Mega lustiger Fahrlehrer, jede Fahrstunde hat Spaß gemacht, und alles wurde in einfacher Sprache erklärt.',
                      'BE schnell gemacht, und der Preis war genau wie vorher besprochen.'], 'dk')
        + contact(s) + footer(s))

S = SITES['city'] = site(
    slug='city-fahrschule-osnabrueck', firma='City Fahrschule', web='city-fahrschule.de', fonts='r14cit',
    title='City Fahrschule – Führerschein in Osnabrück und im Osnabrücker Land', desc='City Fahrschule seit 1975: 30 Leute, 8 Fahrschulen in und um Osnabrück. Alle Klassen außer Bus, Simulator, Ferienfahrschule, We speak English.',
    tel='0541 29344', tel_i='+4954129344', mail='', adresse='Eichendorffstraße 2, 49205 Hasbergen', google=('4,9', 53),
    cta='Online anmelden', nav=[('Anmeldung', 'anmeldung'), ('Fuhrpark', 'fuhrpark'), ('Team', 'team'), ('Geschichte', 'geschichte'), ('Standorte', 'standorte'), ('Kontakt', 'kontakt')],
    hours=[('Büro', '0541 29344'), ('Mobil', '0171 5217328')],
    form_lbl='Führerschein', form_opts=['Auto · B', 'Auto + Motorrad · Doppelführerschein', 'Motorrad · A / A2 / A1', '125er · B196', 'Roller · AM / Mofa', 'Anhänger · BE / B96', 'Lkw · C / CE / C1', 'Traktor · L / T', 'Fahrschulwechsel'],
    form_orte=['Hasbergen', 'Osnabrück', 'Bissendorf', 'Borgloh', 'Bramsche', 'Lüstringen', 'Wallenhorst'],
    form_h3='Jetzt anmelden', form_p='Nach deiner Anmeldung bekommst du von uns alle Infos und deine Bestätigung.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='So, und jetzt <em>los …</em>', kt_p='Büro 0541 29344, mobil 0171 5217328 oder per WhatsApp.',
    rv_h2='Das sagen <em>unsere Kunden.</em>', logo_txt='<img src="img/logo.png" alt="City Fahrschule" style="height:36px;width:auto;display:block">',
    vars='--bg:#fafafa;--ink:#141414;--mute:#5c5c5c;--p:#e30613;--p-ink:#fff;--a:#e30613;--a-ink:#fff;--dk:#141414;--s:#fff;--s2:#f0eeee;--fh:"Bebas Neue",Impact,sans-serif;--fb:"Work Sans",system-ui,sans-serif;--r:8px;--r2:14px;--br:999px;--mq-bg:repeating-linear-gradient(90deg,#e30613 0 46px,#c50511 46px 92px);--mq-ink:#fff;--hd-bg:rgba(255,255,255,.95);--hd-ink:#141414;--ft-bg:#0c0c0c;--hxw-ar:1500/630',
    css='''.hx h1,.h2{font-weight:400;line-height:1;letter-spacing:.01em;padding-top:6px}.hx h1{font-size:clamp(64px,8vw,132px)}.hx h1 em{font-style:normal;color:var(--p)}.hx .pic{border-radius:0;box-shadow:12px 12px 0 var(--p)}.h2{font-size:clamp(46px,5.4vw,84px)}
.hs h1 em{font-style:normal;background:var(--p);color:#fff;padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#ff4b55}.hs .big{font-family:var(--fh);font-size:clamp(220px,30vw,460px);-webkit-text-stroke:2px rgba(227,6,19,.55)}
.hd.lt .lt-logo{color:#fff}.hd.scr .lt-logo{color:#141414}.lt-logo{font-family:var(--fh);font-weight:400;font-size:30px;letter-spacing:.02em}
.fc{--fc-ar:2/3}.fc .grid{grid-template-columns:repeat(6,1fr)}.fc figcaption{display:none}@media (max-width:820px){.fc .grid{grid-template-columns:repeat(3,1fr)}}
.kl .k b,.or .o b,.rd h3{font-weight:400;font-size:30px}.rd h3{font-size:26px}
.cs{position:relative;padding-top:var(--cs-top,84px);background:#fff}
.cs-sl{position:relative;aspect-ratio:1500/630;max-height:calc(100vh - 230px);min-height:260px;overflow:hidden;background:#111}
.cs-sl [data-slide]{position:absolute;inset:0;opacity:0;transition:opacity .9s ease}.cs-sl [data-slide].on{opacity:1;z-index:1}
.cs-sl [data-slide] img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.04);transition:transform 7s ease}.cs-sl [data-slide].on img{transform:scale(1)}
.cs-cap{position:absolute;left:0;right:0;bottom:0;padding:22px 0 26px;background:linear-gradient(0deg,rgba(0,0,0,.72),rgba(0,0,0,0));color:#fff}
.cs-cap .w{display:flex;align-items:baseline;gap:18px;flex-wrap:wrap}.cs-cap b{font:400 clamp(26px,2.8vw,42px)/1 var(--fh);letter-spacing:.01em}.cs-cap span{font-size:17px;opacity:.9}
.cs-cap a svg,.cs-bar a svg{width:16px;height:16px;vertical-align:-3px}.cs-bar .chip,.cs-bar .chip *{color:#141414}.cs-bar .chip .st{color:#f5a623!important}.cs-cap a{margin-left:auto;color:#fff;font-weight:700;text-decoration:none;border-bottom:2px solid var(--p);padding-bottom:3px;white-space:nowrap}
.cs-ar{position:absolute;top:50%;transform:translateY(-50%);z-index:3;width:48px;height:48px;border-radius:50%;border:0;background:rgba(255,255,255,.85);font-size:30px;line-height:1;cursor:pointer;color:#141414}.cs-ar.l{left:18px}.cs-ar.r{right:18px}
.cs-dots{position:absolute;z-index:3;right:24px;top:18px;display:flex;gap:8px}.cs-dots button{width:26px;height:4px;border:0;border-radius:2px;background:rgba(255,255,255,.5);cursor:pointer}.cs-dots button.on{background:var(--p)}
.cs-bar{background:var(--p);color:#fff}.cs-bar .w{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:14px;padding-bottom:14px}
.cs-bar .chip{background:#fff}.cs-bar .ctas{margin:0}.cs-bar .btn-a{background:#fff!important;color:var(--p)!important}.cs-bar .btn-o{border-color:#fff;color:#fff}
.cs-in .w{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,6fr);gap:clamp(24px,4vw,64px);align-items:end;padding-top:clamp(36px,5vw,64px);padding-bottom:clamp(28px,4vw,48px)}
.cs-in h1{font:400 clamp(52px,6.4vw,104px)/.98 var(--fh);margin:10px 0 0;letter-spacing:.01em}.cs-in h1 em{font-style:normal;color:var(--p)}.cs-in .sub{font-size:18px;color:var(--mute);margin:0 0 18px}
.ck{padding-bottom:clamp(40px,6vw,80px)}.ck-f{margin:30px 0 0}.ck-f img{width:100%;max-width:1500px;display:block;margin:0 auto}
.ck-b{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-top:24px}.ck-b p{font-size:19px;margin:0;font-weight:600}
@media(max-width:820px){.cs-in .w{grid-template-columns:1fr}.cs-cap b{font-size:24px}.cs-cap span{display:none}.cs-ar{display:none}.cs-sl{aspect-ratio:4/3;max-height:none}}''')
S['bot'] = BOT('Cleo', 'deine City-Lotsin', 'der City Fahrschule', S, ['B', 'B196', 'B96', 'BE', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE', 'L', 'T'],
    {'schnell': 'In der Ferienfahrschule kommst du besonders zügig voran. Unsere Fahrschüler haben z. B. Klasse A in zwei Monaten geschafft.', 'ruhe': 'Bei uns wirst du nicht durchgeschleust, du lernst wirklich sicher zu fahren.', 'flex': 'Mit acht Fahrschulen in und um Osnabrück findest du immer einen Termin in deiner Nähe.', 'angst': 'Im Simulator übst du die ersten Handgriffe, ganz ohne Verkehr.'},
    qa=[('english|englisch', 'Yes, we speak English! Auch Anmeldung, Theorie und Praxis gehen auf Englisch.'), ('wechsel', 'Du willst die Fahrschule wechseln? Kein Problem, wir helfen dir dabei.'), ('ferien|schnell|intensiv', 'In der Ferienfahrschule machst du deinen Führerschein besonders zügig.'), ('bus', 'Bus bilden wir nicht aus. Alles andere schon: A, B, C, L und T.')],
    tour=[('#anmeldung', 'In vier Schritten angemeldet.'), ('#fuhrpark', 'Unser Fuhrpark vom Mofa bis zum Actros.'), ('#team', 'Das City-Team.'), ('#standorte', 'Immer eine City in deiner Nähe.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'h-team.jpg': ('city/img/i068.jpg', 0), 'h-50.jpg': ('city/img/i025.jpg', 1500), 'h-kunden.jpg': ('city/img/i002.jpg', 0), 'h-traktor.jpg': ('city/img/i001.jpg', 1500), 'h-flotte.jpg': ('city/img/i074.jpg', 0), 'h-bikes.jpg': ('city/img/i007.jpg', 0), 'st-50.jpg': ('city/img/i025.jpg', 0),
    'v-city.mp4': ('city/vid/v.mp4', 0), 'v-city.jpg': ('city/vid/poster.jpg', 0),
    'f-id3.jpg': ('city/img/i014.jpg', 0), 'f-polo.jpg': ('city/img/i015.jpg', 0), 'f-tcross.jpg': ('city/img/i016.jpg', 0), 'f-hornet.jpg': ('city/img/i027.jpg', 0), 'f-actros.jpg': ('city/img/i013.jpg', 0), 'f-trak.jpg': ('city/img/i055.jpg', 0)}
for i, n in enumerate([34, 35, 36, 39, 40, 41, 42, 43, 45, 47, 49, 50], 1): S['img'][f't{i}.jpg'] = (f'city/img/i{n:03d}.jpg', 0)
S['body'] = b_city

# ───────────── 7. Moschitz … die Fahrschule, Osnabrück ─────────────
def b_moschitz(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-team.jpg', pos='50% 45%', bg='h-cabrio.jpg', quick=['auto', 'moto', 'roller', 'lkw'],
        ey='… die Fahrschule in Osnabrück · seit 1985',
        h1='Die ganze Theorie <em>in sieben Tagen.</em>',
        sub='Seit November 1985 bringen wir Fahrschüler sicher zum Führerschein. Mit Kompaktkursen, Simulator und einem Team, das sich Zeit für dich nimmt. Starte mit einem persönlichen Beratungsgespräch.',
        ))
        + ablauf('konzept', 'Unser Konzept', 'Erfolgreich lernen, <em>sicher fahren.</em>', 'Vier Schritte, die bei uns seit Jahren funktionieren.', [
            ('Beratungsgespräch', 'Wir lernen dich kennen und legen deine persönliche Route zum Führerschein fest.'),
            ('Theorie-Kompaktkurs', 'Alle Theoriestunden in nur 7 Tagen. Für A, C, C1 und CE planen wir individuell.'),
            ('Simulator', 'In Ruhe und ohne Zeitdruck auf die erste Fahrstunde vorbereiten.'),
            ('Praktische Ausbildung', 'Fahrstunden mit erfahrenen Fahrlehrern, bis du sicher bist.')], 'dk')
        + orte('termine', 'Theorie-Kompaktkurse 2026', 'Nächste Termine <em>sichern.</em>', '1. Woche montags bis donnerstags, 2. Woche montags bis mittwochs.', [
            ('16.11. – 25.11.', 'November-Kurs', 'läuft'), ('07.12. – 16.12.', 'Dezember-Kurs', 'Plätze anfragen')])
        + panels('simulator', 'Simulator-Ausbildung', 'Erst üben, <em>dann Straße.</em>', 'Viele haben vor der ersten Fahrstunde Respekt. Im Simulator lernst du die Handgriffe ohne Verkehr und ohne Druck.', [
            ('Ohne Zeitdruck', 'p-sim1.jpg', 'Du bestimmst das Tempo.', '50% 50%'), ('Wie im echten Auto', 'p-sim2.jpg', 'Lenkrad, Pedale, Schaltung.', '50% 50%'), ('Mit Fahrlehrer', 'p-sim3.jpg', 'Wir erklären dir jeden Schritt.', '50% 50%')], 'alt')
        + faces('team', 'Das Team', 'Persönlichkeiten <em>mit Leidenschaft.</em>', 'Gaston und Heide Moschitz haben die Fahrschule gegründet. Heute bilden Siggi Sieck, Matthias Prott, Hartmut Wickenkamp, Christopher Plümer und Malte Völkers aus, Tanja Naouar organisiert im Büro alles.', [
            (f't{i}.jpg', '') for i in range(1, 8)])
        + klassen('klassen', 'Führerscheinklassen', 'Zwei Räder, vier Räder <em>oder ein Lkw?</em>', '', [
            ('A · A2 · A1 · AM', 'Motorrad', 'Die Freiheit auf zwei Rädern.', 'ab 15', 'moto'),
            ('B · B197', 'Auto', 'Mit Schaltung oder Automatik mit Schaltkompetenz.', 'ab 17', 'auto'),
            ('BE · B96 · B196', 'Anhänger &amp; 125er', 'Mehr ziehen, mehr fahren.', 'ab 18', 'anh'),
            ('C1 · C · CE', 'Lkw', 'Den kraftvollen Lkw lenken.', 'ab 18', 'lkw')])
        + vgrid('videos', 'Aus der Fahrschule', 'Moschitz <em>in Bewegung.</em>', 'Filme aus unserer Fahrschule.', [
            ('Moschitz … die Fahrschule', 'vimeo', '1155008952', 'v1.jpg'), ('Unterwegs mit Moschitz', 'vimeo', '120359373', 'v2.jpg')], 'alt')
        + reviews(s, ['Das ganze Team ist herzlich und unterstützend. Hardy schafft mit seiner ruhigen Art eine Atmosphäre, in der man sich in jeder Stunde sicher fühlt.',
                      'Motorrad-Erweiterung hier gemacht und total begeistert: professionell, freundlich und unkompliziert, schon die Infos vorab waren super.',
                      'Tanja hat mir vorab alles verständlich erklärt, Malte war in den Fahrstunden ruhig und unglaublich geduldig. So schnell hätte ich es woanders nicht geschafft.',
                      'Termine waren immer einfach zu bekommen, und ich wurde Schritt für Schritt bestens auf die Prüfung vorbereitet.'], 'dk')
        + contact(s) + footer(s))

S = SITES['moschitz'] = site(
    slug='moschitz-fahrschule-osnabrueck', firma='Moschitz … die Fahrschule', web='moschitz.de', fonts='r14mos',
    title='Moschitz … die Fahrschule – Führerschein in Osnabrück seit 1985', desc='Moschitz … die Fahrschule in Osnabrück: Theorie-Kompaktkurse in 7 Tagen, Simulator, Auto, Motorrad und Lkw. Seit 1985.',
    tel='0541 124114', tel_i='+49541124114', mail='post@moschitz.de', adresse='Natruper Straße 232, 49090 Osnabrück', google=('4,8', 44),
    cta='Beratungstermin buchen', tbar='Nächster Theorie-Kompaktkurs: <b>07.12. – 16.12.2026</b> · <a href="#kontakt">Platz anfragen</a>',
    nav=[('Konzept', 'konzept'), ('Termine', 'termine'), ('Simulator', 'simulator'), ('Team', 'team'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Mo', '15:00 – 18:00'), ('Mi', '15:00 – 18:00'), ('Do', '15:00 – 18:00')],
    form_lbl='Führerschein', form_opts=['Auto · B / B197', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', 'Anhänger · BE / B96', '125er · B196', 'Lkw · C / CE / C1', 'Kompaktkurs 07.12.–16.12.'],
    form_h3='Beratungstermin buchen', form_p='Unverbindliches Infogespräch: Wir melden uns und finden deinen Termin.', form_btn='Termin anfragen',
    kt_ey='Kontakt', kt_h2='Fragen zu <em>deiner Ausbildung?</em>', kt_p='Melde dich über das Formular oder telefonisch. Starte jetzt mit uns durch!',
    rv_h2='Das sagen <em>unsere Kunden.</em>', social=[('Instagram', 'https://www.instagram.com/moschitz_die_fahrschule/'), ('Facebook', 'https://www.facebook.com/moschitz.OS')],
    vars='--bg:#f4f8f8;--ink:#0f1a1c;--mute:#536266;--p:#14a3a1;--p-ink:#fff;--a:#14a3a1;--a-ink:#fff;--dk:#0f1a1c;--s:#fff;--s2:#e3efef;--fh:"Outfit",system-ui,sans-serif;--fb:"Inter",system-ui,sans-serif;--r:20px;--r2:30px;--br:999px;--hd-bg:rgba(244,248,248,.94);--hd-ink:#0f1a1c;--logo-h:44px;--ft-bg:#0b1314;--hx-op:.28;--hx-blur:6px;--tbar-bg:repeating-linear-gradient(135deg,#0f1a1c 0 14px,#14a3a1 14px 28px)',
    css='''.hx h1{font-weight:800}.h2{font-weight:800;letter-spacing:-.02em}.hx h1 em,.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#5fe0dc}
.hx .pic{--hx-ar:16/10}.tbar b{padding:2px 8px;border-radius:6px;background:#0f1a1c}.tbar{text-shadow:0 1px 2px rgba(0,0,0,.4)}
.fc{--fc-ar:13/10}.fc .grid{grid-template-columns:repeat(4,1fr)}.fc figcaption{display:none}.fc figure{border-radius:20px;overflow:hidden}@media (max-width:820px){.fc .grid{grid-template-columns:repeat(2,1fr)}}
.or .o:first-child i{background:#14a3a1;color:#fff}
.hx.hasbg{min-height:min(94vh,900px);display:flex;align-items:center;color:#fff}
.hx.hasbg::before{inset:0!important;filter:none!important;opacity:1!important;background-position:70% 40%!important}
.hx.hasbg::after{content:'';position:absolute;inset:0;z-index:0;background:linear-gradient(90deg,rgba(8,30,34,.86) 0%,rgba(8,30,34,.62) 38%,rgba(8,30,34,0) 62%)}
.hx.hasbg>.w{position:relative;z-index:1;grid-template-columns:minmax(0,640px)!important}
.hx.hasbg .pic{display:none!important}
.hx.hasbg h1{color:#fff}.hx.hasbg .sub{color:rgba(255,255,255,.88)}.hx.hasbg .btn-o{color:#fff;border-color:rgba(255,255,255,.7)}.hx.hasbg .quick span{color:rgba(255,255,255,.8)}.hx.hasbg .quick button{color:#fff;border-color:rgba(255,255,255,.45)}
.hd:not(.scr) .nav a{color:#fff!important}
@media(max-width:820px){.hx.hasbg{padding-top:78vw!important;align-items:flex-end}.hx.hasbg::before{background-size:auto 100vw!important;background-position:76% 0!important;background-repeat:no-repeat!important;background-color:#081e22!important}.hx.hasbg::after{background:linear-gradient(0deg,#081e22 0%,#081e22 calc(100% - 100vw),rgba(8,30,34,.1) calc(100% - 62vw),rgba(8,30,34,.35) 100%)}}''')
S['bot'] = BOT('Mo', 'dein Moschitz-Lotse', 'Moschitz', S, ['B', 'B197', 'BE', 'B96', 'B196', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE'],
    {'schnell': 'Im Kompaktkurs schaffst du die komplette Theorie in 7 Tagen. Nächster Start: 07.12.2026.', 'ruhe': 'Unsere Fahrschüler loben die ruhige, geduldige Art unserer Fahrlehrer.', 'flex': 'Termine für Fahrstunden sind bei uns laut unseren Fahrschülern einfach zu bekommen.', 'angst': 'Im Simulator bereitest du dich ohne Zeitdruck auf die erste Fahrstunde vor.'},
    qa=[('kompakt|theorie|7 tage|sieben', 'Die komplette Theorie in 7 Tagen: nächster Kompaktkurs vom 07.12. bis 16.12.2026.'), ('simulator', 'Im Simulator übst du in Ruhe und ohne Zeitdruck, bevor es auf die Straße geht.')],
    tour=[('#konzept', 'Unser Konzept in vier Schritten.'), ('#termine', 'Die nächsten Kompaktkurse.'), ('#simulator', 'Erst üben, dann Straße.'), ('#team', 'Das Moschitz-Team.'), ('#kontakt', 'Hier buchst du dein Beratungsgespräch.')])
S['img'] = {'logo.png': ('moschitz/img/i023.png', 0, 'alphacrop'), 'h-team.jpg': ('moschitz/img/i037.jpg', 0), 'h-road.jpg': ('moschitz/img/i012.jpg', 0), 'h-cabrio.jpg': ('/home/claude/r14raw/moschitz/extra/hero.jpg', 1920, (0, 0, 1, 0.905)),
    'p-sim1.jpg': ('moschitz/img/i036.jpg', 0), 'p-sim2.jpg': ('moschitz/img/i042.png', 0), 'p-sim3.jpg': ('moschitz/img/i039.png', 0),
    'v1.jpg': ('moschitz/img/i021.jpg', 0), 'v2.jpg': ('moschitz/img/i020.jpg', 0)}
for i, n in enumerate(range(24, 31), 1): S['img'][f't{i}.jpg'] = (f'moschitz/img/i{n:03d}.jpg', 0)
S['body'] = b_moschitz

# ───────────── 8. Fahrschule Kindermann, Osnabrück & Bad Essen ─────────────
def b_kindermann(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg'], pos={'h1.jpg': '50% 60%', 'h2.jpg': '50% 50%'}, quick=['auto', 'moto', 'roller', 'anh'],
        ey='Fahrschule Kindermann · Osnabrück &amp; Bad Essen',
        h1='Persönlich. Kompetent. <em>Nah.</em>',
        sub='Der Führerschein ist ein großer Schritt in die Selbstständigkeit. Wir begleiten dich mit Erfahrung, Geduld und einer Ausbildung, die über die Prüfung hinausgeht.',
        ubar=[('4,6 Sterne', '109 Google-Bewertungen'), ('bis 5× Theorie', 'pro Woche, jede Filiale'), ('Antragsservice', 'kein Termin im Stadthaus')]))
        + svc('vorteile', 'Darum Kindermann', 'Weniger Stress, <em>mehr Fahren.</em>', 'Was unsere Fahrschüler am meisten entlastet.', [
            ('Antragsservice', 'Keine Lust auf Termine im Stadthaus? Wir bringen deine Unterlagen für den Führerscheinantrag zur Führerscheinstelle, gegen eine kleine Servicegebühr.'),
            ('Theorie, wann es passt', 'Du kannst jede Filiale besuchen. Bis zu fünfmal pro Woche Unterricht, ganz nach deinem Zeitplan.'),
            ('Praxisnahe Ausbildung', 'Individuelle Fahrstunden, die dich auf die Prüfung und den sicheren Alltag vorbereiten.'),
            ('Seminare', 'Aufbauseminare für Fahranfänger und Fahreignungsseminare.')])
        + sorgen('umschreiben', 'Führerschein aus dem Ausland?', 'Umschreiben <em>ohne Umwege.</em>', 'Viele unserer Fahrschüler kommen mit einem ausländischen Führerschein zu uns. Das schreiben sie über uns:', [
            ('Werde ich nur abgezockt?', 'Ein Fahrschüler aus der Türkei schreibt: Hier konnte ich <b>genau so viele Stunden nehmen, wie ich brauchte</b>, nicht mehr.'),
            ('Ich spreche noch wenig Deutsch.', 'Ehrlich, konzentriert und geduldig: Ein anderer hatte seinen Führerschein <b>nach rund 7 bis 8 Wochen</b>.'),
            ('Wer hilft mir mit den Unterlagen?', 'Unser <b>Antragsservice</b> bringt deine Unterlagen zur Führerscheinstelle.'),
            ('Wie fange ich an?', '<b>Vorbeikommen, anmelden, loslegen</b>: drei Schritte, wir erklären dir alles vor Ort.')], 'dk')
        + faces('team', 'Unser Team', 'Lerne uns <em>kennen.</em>', 'Fahrlehrerinnen und Fahrlehrer mit Herz, und das Büro, das alles zusammenhält.', [
            ('t-andre.jpg', 'André Kindermann'), ('t-cd.jpg', 'Claus-Dieter Kindermann'), ('t-nicole.jpg', 'Nicole Brockmann'), ('t-torsten.jpg', 'Torsten Seydlitz'),
            ('t-sven.jpg', 'Sven Scharfscheer'), ('t-sascha.jpg', 'Sascha Wruck'), ('t-steffi.jpg', 'Stephanie Simon'), ('t-maik.jpg', 'Maik Helm'),
            ('t-maraike.jpg', 'Maraike Maybach Seydlitz'), ('t-andrea.jpg', 'Andrea Michael'), ('t-marko.jpg', 'Marko Beck'), ('t-ingo.jpg', 'Ingo Birnbacher'),
            ('t-jochen.jpg', 'Jochen Kupke'), ('t-ruediger.jpg', 'Rüdiger Hagen'), ('t-eckart.jpg', 'Eckart Watermann'), ('t-gordana.jpg', 'Gordana Neeven')])
        + klassen('klassen', 'Führerscheine', 'Der passende Führerschein <em>für dich.</em>', '', [
            ('B · B197', 'Auto', 'Mit Schaltung oder Automatik mit Schaltkompetenz. Mit 17 begleitet starten.', 'ab 17', 'auto'),
            ('BE · B96', 'Anhänger', 'Wohnwagen, Pferdeanhänger, schwere Gespanne.', 'ab 18', 'anh'),
            ('A · A2 · A1', 'Motorrad', 'Dein Weg zum Motorradführerschein.', 'ab 16', 'moto'),
            ('AM · Mofa', 'Roller', 'Der erste Schritt zur eigenen Mobilität.', 'ab 15', 'roller')], 'alt')
        + gallery('einblicke', 'Unterwegs', 'Fahren lernen <em>mit Vertrauen.</em>', [
            ('g1.jpg', 'w2', '50% 55%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + reviews(s, ['Ich habe mich für Kindermann entschieden, weil viele Bekannte dort waren und sie empfohlen haben. Ich kann nur zustimmen: sehr gute Fahrschule, sehr gute Fahrlehrer.',
                      'Auch wenn man einen Fehler macht, muss man sich keine Sorgen machen. Die Fahrlehrer bleiben ruhig und erklären es, bis man es verstanden hat.',
                      'Ich hatte mehrere Fahrschulen in Osnabrück ausprobiert, hier waren alle freundlich, die Autos gut, und ich hatte meinen Führerschein schnell.',
                      'Wenn Gordana sagt, du bist bereit für die Prüfung, dann bist du es auch!'], 'dk')
        + contact(s) + footer(s))

S = SITES['kindermann'] = site(
    slug='fahrschule-kindermann-osnabrueck', firma='Fahrschule Kindermann', web='fahrschule-kindermann.de', fonts='r14kin',
    title='Fahrschule Kindermann – Persönlich. Kompetent. Nah. | Osnabrück & Bad Essen', desc='Fahrschule Kindermann in Osnabrück und Bad Essen: Auto, Motorrad, Anhänger, Antragsservice, Theorie bis zu fünfmal pro Woche, Seminare.',
    tel='0541 82200', tel_i='+4954182200', mail='info@fahrschule-kindermann.de', adresse='Sutthauser Straße 87, 49080 Osnabrück', google=('4,6', 109),
    cta='Jetzt anmelden', nav=[('Vorteile', 'vorteile'), ('Umschreiben', 'umschreiben'), ('Team', 'team'), ('Führerscheine', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '14:30 – 18:30'), ('Fr', '10:00 – 13:00'), ('Bad Essen', '05472 5256')],
    form_lbl='Führerschein', form_opts=['Auto · B / B197', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', 'Ausländischen Führerschein umschreiben', 'Seminar (ASF / FES)'],
    form_orte=['Osnabrück · Sutthauser Straße', 'Osnabrück · Haste', 'Bad Essen'],
    form_h3='Anmeldung &amp; Antrag', form_p='Schick uns deine Daten, wir melden uns und erklären dir die nächsten Schritte.', form_btn='Anmeldung abschicken',
    kt_ey='Direkt zu uns', kt_h2='Wir freuen uns <em>auf dich.</em>', kt_p='Office Osnabrück 0541 82200, Office Bad Essen 05472 5256.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#f5f5f3;--ink:#0d0d0d;--mute:#5b5b58;--p:#0d0d0d;--p-ink:#fff;--a:#ffffff;--a-ink:#0d0d0d;--dk:#0d0d0d;--s:#fff;--s2:#e9e9e5;--fh:"Syne",system-ui,sans-serif;--fb:"IBM Plex Sans",system-ui,sans-serif;--r:4px;--r2:6px;--br:2px;--mq-bg:#0d0d0d;--hd-bg:rgba(13,13,13,.92);--hd-ink:#fff;--logo-h:40px;--ft-bg:#000;--bot-glow:#fff;--hero-ov:linear-gradient(90deg,rgba(0,0,0,.85) 0%,rgba(0,0,0,.5) 50%,rgba(0,0,0,.1) 85%)',
    css='''.hs h1,.h2{font-weight:800;letter-spacing:-.02em;line-height:1.02}.hs h1 em{font-style:normal;-webkit-text-stroke:2px #fff;color:transparent}.h2 em{font-style:normal;text-decoration:underline;text-decoration-thickness:4px;text-underline-offset:8px}
.kt .btn-a,.kl .btn-a,.el .btn-a{background:#0d0d0d;color:#fff}.hd .btn-a{background:#fff;color:#0d0d0d}.hd .logo img{filter:brightness(0) invert(1)}.ft img{filter:brightness(0) invert(1)}
.fc{--fc-ar:3/2}.fc .grid{grid-template-columns:repeat(4,1fr)}@media (max-width:820px){.fc .grid{grid-template-columns:repeat(2,1fr)}}.kl .k b{color:#0d0d0d}.lot{--p:#0d0d0d}
.sv .row div{border-left:3px solid #0d0d0d}@media (max-width:600px){.hs h1{font-size:30px}}''')
S['bot'] = BOT('Kim', 'dein Kindermann-Lotse', 'der Fahrschule Kindermann', S, ['B', 'B197', 'BE', 'B96', 'A', 'A2', 'A1', 'AM', 'Mofa'],
    {'schnell': 'Theorie bis zu fünfmal pro Woche, in jeder Filiale. So bist du schnell durch.', 'ruhe': 'Unsere Fahrlehrer bleiben ruhig und erklären, bis du es verstanden hast.', 'flex': 'Du kannst jede Filiale besuchen, ganz wie es in deinen Zeitplan passt.', 'angst': 'Fehler sind bei uns kein Drama. Wir erklären es in Ruhe nochmal.'},
    qa=[('ausland|umschreib|türk|international', 'Ausländischen Führerschein umschreiben? Machen wir regelmäßig. Du nimmst nur so viele Stunden, wie du wirklich brauchst.'), ('antrag|stadthaus|führerscheinstelle', 'Unser Antragsservice bringt deine Unterlagen zur Führerscheinstelle, gegen eine kleine Servicegebühr.'), ('seminar|asf|aufbau|fes', 'Wir bieten Aufbauseminare für Fahranfänger und Fahreignungsseminare an.')],
    tour=[('#vorteile', 'Was dich bei uns entlastet.'), ('#umschreiben', 'Führerschein aus dem Ausland? So geht’s.'), ('#team', 'Unser Team.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('kindermann/img/i017.png', 0, 'alphacrop'), 'h1.jpg': ('kindermann/img/i005.jpg', 0), 'h2.jpg': ('kindermann/img/i007.jpg', 0), 'h3.jpg': ('kindermann/img/i026.jpg', 0),
    'g1.jpg': ('kindermann/img/i006.jpg', 0), 'g2.jpg': ('kindermann/img/i040.jpg', 900), 'g3.jpg': ('kindermann/img/i004.jpg', 0), 'g4.jpg': ('kindermann/img/i036.jpeg', 0), 'g5.jpg': ('kindermann/img/i039.png', 0)}
for k, n in [('andre', 2), ('cd', 3), ('nicole', 21), ('torsten', 28), ('sven', 25), ('sascha', 23), ('steffi', 24), ('maik', 18), ('maraike', 19), ('andrea', 1), ('marko', 20), ('ingo', 14), ('jochen', 15), ('ruediger', 22), ('eckart', 10), ('gordana', 11)]:
    S['img'][f't-{k}.jpg'] = (f'kindermann/img/i{n:03d}.jpg', 0)
S['body'] = b_kindermann

# ───────────── 9. Fahrschule Beinke, Osnabrück Rosenplatz ─────────────
def b_beinke(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-thomas.jpg', pos='50% 15%', bg='h-cabrio.jpg', quick=['auto', 'moto', 'anh'],
        ey='Fahrschule Beinke · Osnabrück Rosenplatz',
        h1='Läufst du noch, <em>oder fährst du schon?</em>',
        sub='Direkt am Rosenplatz, viermal pro Woche Theorie, geduldige Fahrlehrer und die praktische Lern-App. Bei uns lernst du, wie es geht. We speak English.',
        g1=('4× pro Woche', 'Theorieunterricht')))
        + marquee(['Klasse B', 'B197 Automatik', 'BF17', 'BE · B96', 'A · A2 · A1 · AM', 'B196', 'We speak English', 'Kartenzahlung'], 'bm')
        + svc('vorteile', 'Was dich erwartet', 'Vier Gründe, <em>warum Beinke.</em>', 'Eine gute Erfolgsquote und zahlreiche zufriedene Fahrschüler können nicht irren. Frag einfach mal deine Bekannten.', [
            ('Zentralste Lage', 'Direkt am Rosenplatz, mitten in Osnabrück.'), ('Moderne Fahrzeuge', 'Leicht zu fahren, mit Schaltung oder Automatik.'),
            ('Geduldige Fahrlehrer', 'Sympathisch, ruhig und kompetent, wir gehen auf dein Lerntempo ein.'), ('4× Theorie pro Woche', 'Und die praktische Lern-App für unterwegs.')])
        + team('team', 'Nice to meet you', 'Gemeinsam <em>zum Führerschein.</em>', 'Erfahrene Fahrlehrer, die ihr Wissen klar und praxisnah vermitteln.', [
            ('t-thomas.jpg', 'Thomas Beinke', 'Fahrlehrer · A, B, BE'), ('t-hendrick.jpg', 'Hendrick Hallmann', 'Fahrlehrer · B'), ('t-andreas.jpg', 'Andreas Beinke', 'Fahrlehrer · B'), ('t-martin.jpg', 'Martin Kutza', 'Fahrlehrer · B, BE')], 'alt')
        + sorgen('english', 'International', 'We speak <em>English.</em>', 'Many of our students learn to drive in English. Here is what they say:', [
            ('Can I take lessons in English?', 'Yes. One student writes: <b>we had our lessons in English</b>, and his English is really good.'),
            ('My German is not perfect yet.', '<b>Passed theory and practical on the first attempt</b>, even without good German. Martin explained everything clearly.'),
            ('I want to drive manual.', 'Hendrick is recommended as <b>patient, calm and very professional</b>, also for the manual car course.'),
            ('How do I start?', 'Contact us by phone or form. We explain the <b>Antragsservice</b> and all next steps.')], 'dk')
        + klassen('klassen', 'Führerscheine', 'Welcher Führerschein <em>passt zu dir?</em>', '', [
            ('B · B197', 'PKW', 'Schaltung oder Automatik? Mit B197 beides.', 'ab 17', 'auto'),
            ('A · A2 · A1 · AM', 'Motorrad', 'Motorrad fahren, die pure Freiheit.', 'ab 15', 'moto'),
            ('BE · B96', 'Anhänger', 'Du möchtest viel transportieren? Jetzt losziehen.', 'ab 18', 'anh'),
            ('B196', '125er', 'Mit dem Autoführerschein aufs Leichtkraftrad.', 'ab 25', 'roller')])
        + gallery('fahrzeuge', 'Unsere Fahrzeuge', 'Bereit, <em>wenn du es bist.</em>', [
            ('g1.jpg', 'w2', '50% 55%'), ('g2.jpg', '', '50% 60%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 60%'), ('g5.jpg', 'w2', '50% 55%')], 'alt')
        + reviews(s, ['Ich hatte meine Fahrstunden bei Hendrick und bin wirklich happy. Er ist ein toller Lehrer, und wir hatten die Stunden auf Englisch.',
                      'Die beste Fahrschule der Stadt: Man lernt nicht nur, die Prüfung zu bestehen, sondern ein Leben lang verantwortungsvoll zu fahren.',
                      'Mein Deutsch war nicht gut, trotzdem lief dank Martin alles reibungslos. Theorie und Praxis beim ersten Versuch bestanden.',
                      'B196 hier gemacht. Thomas war super, die Fahrten haben richtig Spaß gemacht.'], 'dk')
        + contact(s) + footer(s))

S = SITES['beinke'] = site(
    slug='fahrschule-beinke-osnabrueck', firma='Fahrschule Beinke', web='fahrschule-beinke.de', fonts='r14bei',
    title='Fahrschule Beinke – Fahrschule am Rosenplatz in Osnabrück', desc='Fahrschule Beinke am Rosenplatz in Osnabrück: Auto, Motorrad, Anhänger, B196, Theorie viermal pro Woche, Lern-App, We speak English.',
    tel='0171 2156446', tel_i='+491712156446', mail='fahrschule-beinke@gmx.de', adresse='Rosenplatz 22, 49074 Osnabrück', google=('4,9', 197),
    cta='Jetzt anmelden', nav=[('Vorteile', 'vorteile'), ('Team', 'team'), ('English', 'english'), ('Führerscheine', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Mo', '17:00 – 18:30'), ('Di', '18:30 – 20:00'), ('Do', '09:00 – 10:30 · 17:00 – 18:30')],
    form_lbl='Führerschein', form_opts=['PKW · B / B197', 'Motorrad · A / A2 / A1 / AM', 'Anhänger · BE / B96', '125er · B196', 'English course'],
    form_h3='Jetzt anmelden', form_p='Schick uns deine Daten, wir melden uns für den Start.', form_btn='Anmeldung abschicken',
    kt_ey='So findest du uns', kt_h2='Direkt am <em>Rosenplatz.</em>', kt_p='Rosenplatz 22, 49074 Osnabrück. Telefon 0171 2156446 oder 0171 2156448.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#f3f7fb;--ink:#0e1b2c;--mute:#55627a;--p:#0e2a4f;--p-ink:#fff;--a:#11c4d4;--a-ink:#0e1b2c;--dk:#0e2a4f;--s:#fff;--s2:#e4eef6;--fh:"Sora",system-ui,sans-serif;--fb:"Inter",system-ui,sans-serif;--r:18px;--r2:26px;--br:999px;--mq-bg:#0e2a4f;--mq-ink:#11c4d4;--hd-bg:rgba(243,247,251,.94);--hd-ink:#0e1b2c;--logo-h:24px;--ft-bg:#081a33;--hx-bg:linear-gradient(160deg,#f3f7fb 55%,#d8f5f8)',
    css='''.hx h1{font-weight:800}.h2{font-weight:800;letter-spacing:-.02em}.hx h1 em,.h2 em{font-style:normal;color:#0aa3b2}.dk .h2 em{color:#11c4d4}
.hx .pic{--hx-ar:4/5;--hx-r:28px;max-width:440px;justify-self:end}.tm figure img{aspect-ratio:3/4;object-position:50% 8%}.hd .logo img{height:24px}.ft img{background:#fff;padding:8px 10px;border-radius:6px;height:40px}
.hx.hasbg::before{inset:0!important;filter:none!important;opacity:1!important;background-position:center 62%!important}.hx .pic{max-width:360px;justify-self:end}.hx.hasbg::after{content:'';position:absolute;inset:0;z-index:0;background:linear-gradient(90deg,rgba(243,247,251,.97) 0%,rgba(243,247,251,.9) 34%,rgba(243,247,251,0) 52%)}.hx.hasbg>.w{position:relative;z-index:1}''')
S['bot'] = BOT('Rosi', 'deine Lotsin vom Rosenplatz', 'der Fahrschule Beinke', S, ['B', 'B197', 'BE', 'B96', 'B196', 'A', 'A2', 'A1', 'AM'],
    {'schnell': 'Viermal pro Woche Theorie, dazu die Lern-App: So geht es zügig voran.', 'ruhe': 'Wir gehen individuell auf dein Lerntempo ein, in einer ruhigen, konzentrierten Lernumgebung.', 'flex': 'Theorie viermal pro Woche, mitten in der Stadt am Rosenplatz.', 'angst': 'Unsere Fahrlehrer gelten als geduldig und ruhig. Auf Wunsch auch auf Englisch.'},
    qa=[('english|englisch', 'Yes, we speak English! Lessons are possible in English.'), ('karte|zahl|ec', 'Bei uns kannst du auch mit Karte zahlen.'), ('antrag', 'Wir bieten einen Führerschein-Antragsservice an.')],
    tour=[('#vorteile', 'Warum Beinke.'), ('#team', 'Deine Fahrlehrer.'), ('#english', 'Learning to drive in English.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('beinke/img/i007.png', 0, 'alphacrop'), 'h-cabrio.jpg': ('beinke/img/i009.jpg', 1800), 'h-thomas.jpg': ('beinke/img/i034.jpg', 1000),
    't-thomas.jpg': ('beinke/img/i034.jpg', 900), 't-hendrick.jpg': ('beinke/img/i031.jpg', 900), 't-andreas.jpg': ('beinke/img/i029.jpg', 900), 't-martin.jpg': ('beinke/img/i032.jpg', 900),
    'g1.jpg': ('beinke/img/i003.jpg', 0), 'g2.jpg': ('beinke/img/i020.jpg', 0), 'g3.jpg': ('beinke/img/i017.jpg', 900), 'g4.jpg': ('beinke/img/i005.jpg', 0), 'g5.jpg': ('beinke/img/i002.jpg', 0)}
S['body'] = b_beinke

# ───────────── 10. Fahrschule St. Eggert, Dissen · Osnabrück · Belm ─────────────
def b_eggert(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 55%', quick=['auto', 'moto', 'roller', 'anh', 'lkw', 'trak'],
        ey='Fahrschule Eggert · völlig abgefahren …!',
        h1='Unabhängig vom Bus. <em>Ab jetzt fährst du.</em>',
        sub='Selbst entscheiden, wann und wohin: Wir bringen dir alles bei, was du über den Straßenverkehr wissen musst. In Dissen, Osnabrück und Belm, mit Fahrsimulator und unserer neuen Frauenfahrschule.',
        badge=('Neu', 'Frauenfahrschule in Osnabrück')))
        + promo('frauen', 'p-frauen.jpg', 'Jetzt neu', 'Die Frauenfahrschule. <em>Von und für Frauen.</em>', 'In der Iburger Straße 67 in Osnabrück gibt es jetzt unsere Frauenfahrschule: eine Filiale von und für Frauen. Ruf an, schreib per WhatsApp oder komm einfach vorbei.', ['Iburger Straße 67, Osnabrück', 'Eine Fahrschule von und für Frauen', 'Erreichbar auch per WhatsApp'], 'Platz anfragen', 'alt')
        + orte('filialen', 'Unsere Filialen', 'Sechsmal <em>in deiner Nähe.</em>', 'Anmeldung an allen Filialen immer ab 60 Minuten vor dem Unterricht.', [
            ('Dissen', 'Osnabrücker Straße 5 · Hauptfiliale mit Simulator', ''), ('Osnabrück', 'Bremer Straße 196', ''), ('Osnabrück', 'Schützenstraße 70', ''),
            ('Osnabrück', 'Martinistraße 103', 'Mo &amp; Mi 18–20 Uhr'), ('Osnabrück', 'Sutthauser Straße 23', ''), ('Belm', 'Marktring 14', ''), ('Frauenfahrschule', 'Iburger Straße 67, Osnabrück', 'neu')])
        + klassen('klassen', 'Wir bilden dich aus', 'Unsere <em>Fahrschulklassen.</em>', 'Klasse A, T oder C auf Anfrage, oder folg uns auf Instagram für Sonderunterrichte.', [
            ('Mofa · AM', 'Roller', 'Ab 15 auf zwei Rädern.', 'ab 15', 'roller'),
            ('A1 · A2 · A', 'Motorrad', 'Von der 125er bis zur großen Maschine.', 'ab 16', 'moto'),
            ('B', 'Auto', 'Dein Start in die Freiheit.', 'ab 17', 'auto'),
            ('B196', '125er ohne Prüfung', 'Mit dem Autoführerschein aufs Leichtkraftrad.', 'ab 25', 'roller'),
            ('BE · B96', 'Anhänger', 'Für Wohnwagen und Pferdeanhänger.', 'ab 18', 'anh'),
            ('C1 · C · CE', 'Lkw', 'Auf Anfrage.', 'ab 18', 'lkw'),
            ('L · T', 'Traktor', 'Auf Anfrage.', 'ab 16', 'trak')], 'dk')
        + gallery('flotte', 'Unsere Flotte', 'Unübersehbar <em>auf der Straße.</em>', [
            ('g1.jpg', 'w2', '50% 55%'), ('g2.jpg', '', '50% 55%'), ('g3.jpg', '', '50% 55%'), ('g4.jpg', '', '50% 55%'), ('g5.jpg', '', '50% 55%'), ('g6.jpg', 'w2', '50% 55%')])
        + reviews(s, ['Ich kann die Fahrschule Eggert nur empfehlen, vor allem meine Fahrlehrerin Kosovare. Herzlich, offen und mit unglaublicher Geduld, auch wenn man Dinge mehrmals erklärt braucht.',
                      'Gzim ist ein geduldiger, ruhiger und verständnisvoller Fahrlehrer, der mich immer motiviert hat. Ich fühlte mich perfekt vorbereitet.',
                      'Niklas nimmt sich Zeit und ist unglaublich geduldig. Die Termine waren flexibel, und ich habe beim ersten Versuch bestanden.',
                      'Frau Eggert macht als Ansprechpartnerin einen tollen Job und hat mich immer unterstützt.'], 'alt')
        + contact(s) + footer(s))

S = SITES['eggert'] = site(
    slug='fahrschule-eggert-dissen', firma='Fahrschule St. Eggert', web='fahrschule-st-eggert.de', fonts='r14egg',
    title='Fahrschule St. Eggert – völlig abgefahren | Dissen, Osnabrück, Belm', desc='Fahrschule St. Eggert in Dissen, Osnabrück und Belm: alle Klassen, Fahrsimulator und neue Frauenfahrschule in Osnabrück.',
    tel='05421 930123', tel_i='+495421930123', mail='fseggert@aol.com', adresse='Osnabrücker Straße 5, 49201 Dissen am Teutoburger Wald', google=('4,8', 37),
    cta='Jetzt anmelden', nav=[('Frauenfahrschule', 'frauen'), ('Filialen', 'filialen'), ('Klassen', 'klassen'), ('Flotte', 'flotte'), ('Kontakt', 'kontakt')],
    hours=[('Mobil', '0172 8865499'), ('Anmeldung', 'ab 60 Min. vor dem Unterricht')],
    form_lbl='Führerschein', form_opts=['Auto · B', 'Frauenfahrschule · B', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', '125er · B196', 'Anhänger · BE / B96', 'Lkw · C1 / C / CE', 'Traktor · L / T'],
    form_orte=['Dissen', 'Osnabrück · Bremer Straße', 'Osnabrück · Schützenstraße', 'Osnabrück · Martinistraße', 'Osnabrück · Sutthauser Straße', 'Belm', 'Frauenfahrschule · Iburger Straße'],
    form_h3='Info &amp; Anmeldung', form_p='Wir melden uns schnell bei dir, gern auch per WhatsApp.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Du entscheidest, <em>wohin.</em>', kt_p='Anrufen, WhatsApp oder Formular. Wir freuen uns auf dich, dein Team der Fahrschule Eggert.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>',
    vars='--bg:#fbfbf6;--ink:#17201a;--mute:#56605a;--p:#e5291f;--p-ink:#fff;--a:#ffcb05;--a-ink:#17201a;--dk:#17201a;--s:#fff;--s2:#f5f1ea;--fh:"Montserrat",system-ui,sans-serif;--fb:"Montserrat",system-ui,sans-serif;--r:24px;--r2:32px;--br:999px;--hd-bg:rgba(251,251,246,.95);--hd-ink:#17201a;--logo-h:46px;--ft-bg:#101611;--hp-bg:linear-gradient(90deg,#fbfbf6 38%,rgba(251,251,246,.72) 62%,rgba(251,251,246,.35)),url(img/h-road.jpg) center 70%/cover no-repeat',
    css='''.hp h1,.h2{font-weight:800;line-height:1.04;letter-spacing:-.02em}.hp h1 em,.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:var(--a)}
.comp{height:470px}.comp figure{border-radius:28px}.comp .c1{transform:rotate(-2deg)}.comp .badge{background:#e5007d;color:#fff}.comp .badge b,.comp .badge *{color:#fff!important}.promo figure{max-width:430px;justify-self:center}.promo .tag{background:#e5007d;color:#fff}
.kl .k b{font-weight:800}.or .o b{font-weight:800}.or .o i{background:#fdc300!important;color:#17201a!important;padding:4px 10px!important;clip-path:polygon(0 0,92% 0,100% 50%,92% 100%,0 100%)}.ft img{background:#fff;padding:8px 12px;border-radius:12px}
.or .grid{border-top:0!important;gap:26px 22px!important}.or .o,.or .o+.o{border:0!important;padding:0!important}.or .o b{display:inline-block;align-self:flex-start;background:#fdc300;color:#17201a;font-size:clamp(18px,1.5vw,22px)!important;text-transform:uppercase;padding:12px 34px 12px 16px;clip-path:polygon(0 0,90% 0,100% 50%,90% 100%,0 100%);box-shadow:inset 0 0 0 2px rgba(0,0,0,.06)}.or .o b::after{content:'';display:block}.or .o{position:relative}.or .o::before{content:'';position:absolute;left:18px;top:44px;bottom:-10px;width:5px;background:#9aa0a6;z-index:-1;opacity:.0}.or .o b{overflow-wrap:normal!important;white-space:nowrap}
.hp{background:linear-gradient(90deg,var(--bg) 0%,color-mix(in srgb,var(--bg) 92%,transparent) 34%,color-mix(in srgb,var(--bg) 25%,transparent) 56%,color-mix(in srgb,var(--bg) 10%,transparent) 100%),url(img/emo.jpg) 62% 50%/cover no-repeat!important}.hp::before{opacity:.35}@media(max-width:820px){.hp{background:linear-gradient(0deg,var(--bg) 52%,color-mix(in srgb,var(--bg) 30%,transparent) 80%),url(img/emo.jpg) 62% 50%/auto 62% no-repeat!important}}''')
S['bot'] = BOT('Edda', 'deine Eggert-Lotsin', 'der Fahrschule Eggert', S, ['B', 'B196', 'B96', 'BE', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE', 'L', 'T'],
    {'schnell': 'Mit sechs Filialen findest du immer einen Unterricht in deiner Nähe.', 'ruhe': 'Unsere Fahrschüler loben vor allem die Geduld unserer Fahrlehrer, auch wenn man etwas mehrmals erklärt braucht.', 'flex': 'Unsere Fahrschüler schreiben: Die Termine waren flexibel.', 'angst': 'In Dissen kannst du erst am Fahrsimulator üben. Und es gibt unsere Frauenfahrschule, von und für Frauen.'},
    qa=[('frau', 'Unsere Frauenfahrschule in der Iburger Straße 67 in Osnabrück ist von und für Frauen.'), ('simulator', 'Am Fahrsimulator in unserer Hauptfiliale in Dissen kannst du fahren lernen, bevor es auf die Straße geht.'), ('whatsapp', 'Klar, schreib uns gern per WhatsApp.')],
    tour=[('#frauen', 'Neu: unsere Frauenfahrschule.'), ('#filialen', 'Sechsmal in deiner Nähe.'), ('#klassen', 'Alle Klassen auf einen Blick.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('eggert/img/i020.png', 0, 'alphacrop'), 'h-road.jpg': ('eggert/img/i028.jpg', 1800), 'h1.jpg': ('eggert/img/i047.jpg', 0), 'h2.jpg': ('eggert/img/i058.jpg', 900), 'h3.jpg': ('eggert/img/i056.jpg', 0),
    'p-frauen.jpg': ('eggert/img/i010.jpg', 0),
    'g1.jpg': ('eggert/img/i050.jpg', 0), 'g2.jpg': ('eggert/img/i029.jpg', 0), 'g3.jpg': ('eggert/img/i037.jpg', 0), 'g4.jpg': ('eggert/img/i022.jpg', 0), 'g5.jpg': ('eggert/img/i012.jpg', 0), 'g6.jpg': ('eggert/img/i045.jpg', 0)}
S['body'] = b_eggert

SITES['city']['img']['logo.png'] = ('/home/claude/r14raw/logos/city.png', 0)

SITES['eggert']['img']['emo.jpg'] = ('/home/claude/pixa/emo_eggert.jpg', 0)
