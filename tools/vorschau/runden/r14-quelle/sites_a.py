"""Runde 14 · Teil A: Saller, Albers, HP 66, Beckermann, Tepe."""
from common import *
SITES = {}

SALLER_CSS = """
.hd,.hd.scr{background:var(--hd-bg)!important;color:#fff!important;box-shadow:0 2px 0 rgba(0,0,0,.08)}.hd a,.hd .nav a{color:#fff}.hd .btn-a,.hd .cta{background:var(--y)!important;color:#1d1d1f!important}
.h2{font-weight:800;text-transform:uppercase;letter-spacing:-.01em;line-height:1.05}.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:var(--y)}
.btn-a{background:var(--p);color:#fff}
/* Hero wie im Original: Schlüsselübergabe vollflächig, gelbe Buttons, Kasten mit Botschaft */
.sx{position:relative;min-height:min(96vh,900px);padding-top:var(--sxt,88px);display:flex;color:#fff;overflow:hidden;background:#222}
.sx-bg{position:absolute;inset:var(--sxt,88px) 0 0 0}.sx-bg img{width:100%;height:100%;object-fit:cover;object-position:30% 40%}
.sx-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,0) 30%),linear-gradient(0deg,rgba(0,0,0,.72),rgba(0,0,0,0) 60%)}
.sx-in{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:40px;padding:28px 24px 56px;width:100%}
.sx-ctas{display:flex;gap:16px;justify-content:flex-end;flex-wrap:wrap}
.sx-y{display:inline-flex;align-items:center;gap:10px;background:var(--y);color:#1d1d1f;font:800 15px/1.2 var(--fb);text-transform:uppercase;letter-spacing:.02em;padding:16px 22px;border-radius:4px;text-decoration:none;box-shadow:0 10px 30px rgba(0,0,0,.25);transition:transform .2s}
.sx-y:hover{transform:translateY(-2px)}.sx-y svg{color:var(--p)}
.sx-pan{max-width:600px;background:rgba(255,255,255,.93);color:#1d1d1f;padding:30px 34px;border-left:6px solid var(--p);backdrop-filter:blur(6px)}
.sx-pan h1{font:800 clamp(32px,3.6vw,52px)/1.03 var(--fh);text-transform:uppercase;color:var(--p);margin:14px 0 12px;letter-spacing:-.01em}
.sx-call{font:700 clamp(20px,1.8vw,26px) var(--fh);margin:0}.sx-call a{color:var(--p);text-decoration:none;white-space:nowrap}
.sx-sub{margin:8px 0 0;font-size:17px;color:#45454b}
.sx-pan .qk,.sx-pan .quick{margin-top:18px}
@media(max-width:820px){.sx{flex-direction:column;min-height:0}.sx-bg{position:relative;height:56vw}.sx-bg::after{background:none}.sx-in{padding:18px 16px 28px;gap:18px}.sx-ctas{justify-content:stretch;flex-direction:column}.sx-y{justify-content:center}.sx-pan{padding:22px 20px;background:#fff}}
/* Intro mit Henrik */
.si-g{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(28px,5vw,80px);align-items:center}
.si-pic{margin:0;position:relative}.si-pic img{width:100%;aspect-ratio:4/5;object-fit:cover;object-position:50% 20%;display:block}
.si-pic::before{content:"";position:absolute;inset:18px -18px -18px 18px;border:3px solid var(--p);z-index:-1}
.si-pic figcaption{font-size:14px;color:var(--mute);margin-top:30px}
.si-fvn img{height:74px;width:auto;margin:6px 0 22px}
.si-v{list-style:none;padding:0;margin:clamp(40px,6vw,80px) 0 0;display:grid;grid-template-columns:repeat(4,1fr);border-top:3px solid var(--p)}
.si-v li{padding:22px 22px 0 0}.si-v li+li{padding-left:22px;border-left:1px solid #e3e1de}
.si-v b{display:block;font:800 clamp(28px,2.6vw,40px)/1 var(--fh);color:var(--p)}.si-v span{display:block;font-weight:700;margin:6px 0}.si-v small{color:var(--mute);font-size:15px;line-height:1.45}
@media(max-width:820px){.si-g{grid-template-columns:1fr}.si-v{grid-template-columns:1fr 1fr}.si-v li:nth-child(3){padding-left:0;border-left:0}}
/* Region */
.sre{background:var(--s2)}.sre-g{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(28px,5vw,72px);align-items:center}
.sre-p{display:grid;grid-template-columns:1fr 1fr;gap:18px}.sre-p figure{margin:0}.sre-p figure:nth-child(2){margin-top:48px}
.sre-p img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}.sre-p figcaption{font-weight:700;margin-top:10px;font-size:15px}
@media(max-width:820px){.sre-g{grid-template-columns:1fr}}
/* Rote Standort-Sektion wie im Original */
.sor{background:var(--p);color:#fff}.sor .ey{color:#fff!important;opacity:.85}.sor .h2,.sor .h2 em{color:#fff}.sor .h2 em{color:var(--y)}
.sor-g{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,4vw,56px) clamp(28px,4vw,64px);margin-top:44px}
.so-o{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:22px;align-items:center}
.so-o figure{margin:0;background:#fff;padding:8px 8px 8px;transform:rotate(-1.4deg);box-shadow:0 14px 34px rgba(0,0,0,.25);max-width:380px}
.so-o:nth-child(even) figure{transform:rotate(1.2deg)}
.so-o figure img{width:100%;aspect-ratio:11/7;object-fit:cover;display:block}
.so-tag{color:var(--y);font-weight:800;text-transform:uppercase;letter-spacing:.05em;font-size:14px;margin:0}
.so-o h3{font:800 clamp(28px,2.6vw,38px)/1 var(--fh);text-transform:uppercase;margin:6px 0 8px;color:#fff}
.so-o p{margin:0;font-size:16px;color:rgba(255,255,255,.92)}.so-l{margin-top:12px!important;display:flex;gap:16px;flex-wrap:wrap}
.so-l a svg{width:16px;height:16px;vertical-align:-3px}.so-l a{color:#fff;font-weight:700;text-decoration:none;border-bottom:2px solid var(--y);padding-bottom:2px}
@media(max-width:900px){.sor-g{grid-template-columns:1fr}}@media(max-width:520px){.so-o{grid-template-columns:1fr}}
/* Erste Hilfe */
.seh{background:linear-gradient(90deg,#fff 0 60%,var(--y) 60% 100%)}.seh-g{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(28px,5vw,80px);align-items:center}
.seh-f{margin:0;justify-self:center}.seh-f img{width:min(340px,70vw);display:block;box-shadow:0 24px 60px rgba(0,0,0,.25);transform:rotate(2deg)}
.seh-n{margin:22px 0;padding:16px 0 16px 18px;border-left:5px solid var(--p)}.seh-n span{display:block;font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--mute);font-weight:700}
.seh-n b{display:block;font:800 26px var(--fh);color:var(--p)}.seh-n small{color:var(--mute)}
@media(max-width:820px){.seh{background:#fff}.seh-g{grid-template-columns:1fr}}
/* Fuhrpark */
.sfp-top{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(28px,5vw,72px);align-items:center}
.sfp-hero{margin:0}.sfp-hero img{width:100%;aspect-ratio:16/11;object-fit:cover;object-position:50% 55%;display:block}
.sfp-l{list-style:none;padding:0;margin:clamp(36px,5vw,64px) 0 0;display:grid;grid-template-columns:repeat(4,1fr);gap:34px 26px}
.sfp-l img{width:100%;max-width:300px;aspect-ratio:1;object-fit:cover;display:block;background:#fff}
.sfp-l b{display:block;font:800 22px var(--fh);text-transform:uppercase;margin-top:12px;border-top:3px solid var(--p);padding-top:10px}.sfp-l span{color:var(--mute);font-size:15px}
@media(max-width:900px){.sfp-top{grid-template-columns:1fr}.sfp-l{grid-template-columns:1fr 1fr}}
/* Medienräume */
.smr-g{display:grid;grid-template-columns:1.4fr 1fr 1fr;grid-auto-rows:clamp(180px,19vw,270px);gap:14px;margin-top:40px}.smr-g figure:last-child{grid-column:span 2}
.smr-g figure{margin:0;position:relative;overflow:hidden}.smr-g figure:first-child{grid-row:span 2}
.smr-g img{width:100%;height:100%;object-fit:cover;display:block;min-height:200px}
.smr-g figcaption{position:absolute;left:0;bottom:0;background:var(--p);color:#fff;font-weight:800;text-transform:uppercase;font-size:13px;letter-spacing:.06em;padding:7px 12px}
@media(max-width:820px){.smr-g{grid-template-columns:1fr 1fr}.smr-g figure:first-child{grid-column:span 2;grid-row:auto}}
/* Behörde, App, Gruß */
.sbh{background:var(--s2)}.sbh-g{display:grid;grid-template-columns:1fr 1fr 1fr;gap:clamp(24px,4vw,60px);align-items:start}
.sbh-a{font-size:17px;line-height:1.6;margin:0}.sbh-s{display:flex;gap:10px;margin-top:14px}.sbh-s img{height:40px;width:auto}
.sbh-grus p{font:800 28px/1.1 var(--fh);text-transform:uppercase;margin:0;color:var(--p)}.sbh-grus b{display:block;margin-top:8px;font-size:18px}
@media(max-width:820px){.sbh-g{grid-template-columns:1fr}}
.kl .k b{font-weight:800}
"""

# ───────────── 1. Fahrschule K.H. Saller, Badbergen · Alfhausen · Ankum · Bersenbrück ─────────────
# Nach Viktors Vorgabe 16.11.: Original-Aufbau von fahrschule-saller.de 1:1 übernehmen, nur moderner.
def _sal_map(adr):
    return 'https://www.google.com/maps/search/?api=1&amp;query=' + adr.replace(' ', '+')

def b_saller(s):
    hero = f"""<section class="sx" id="top">
  <div class="sx-bg"><img src="img/h-schluessel.jpg" alt="Schlüsselübergabe nach bestandener Prüfung" fetchpriority="high"></div>
  <div class="w sx-in">
    <div class="sx-ctas" data-r>
      <a class="sx-y" href="#kontakt">{CAR} Anmeldung Führerschein</a>
      <a class="sx-y" href="#erste-hilfe">{AID} Erste Hilfe &amp; Sehtest: Kursinfos und Anmeldung</a>
    </div>
    <div class="sx-pan" data-r="2">
      {chip(s)}
      <h1>Bei Saller macht man seinen Führerschein!</h1>
      <p class="sx-call">Rufe uns an: <a href="tel:{s['tel_i']}">0171-3866717</a></p>
      <p class="sx-sub">Wir beraten Dich gerne. Unterricht und Anmeldung in Badbergen, Alfhausen, Ankum und Bersenbrück.</p>
      {quick(s, dict(quick=['auto', 'moto', 'roller', 'anh']))}
    </div>
  </div>
</section>"""
    vorteile = [('4', 'Unterrichtsorte', 'Mo Badbergen · Di Alfhausen · Mi Ankum · Do Bersenbrück'),
                ('1989', 'gegründet', 'von Kalle Saller, seit 2023 geführt von Henrik Grover'),
                ('B · BE', '+ alle Zweiräder', 'Auto, Anhänger, Motorrad, 125er und Roller'),
                ('Erste Hilfe', '+ Sehtest', 'direkt bei uns, samstags in Badbergen')]
    vt = ''.join(f'<li data-r><b>{a}</b><span>{b}</span><small>{c}</small></li>' for a, b, c in vorteile)
    intro = f"""<section class="sec si" id="ueber">
  <div class="w si-g">
    <figure class="si-pic" data-r><img src="img/p-henrik.jpg" alt="Henrik Grover, Inhaber der Fahrschule Saller" loading="lazy"><figcaption>Henrik Grover · Fahrlehrer mit Leib und Seele</figcaption></figure>
    <div class="si-tx" data-r="2">
      <p class="ey">Fahrschule Saller · Inh. Henrik Grover</p>
      <h2 class="h2">Wir begleiten Dich auf dem Weg <em>zum Führerschein.</em></h2>
      <p class="lead">Henrik war zwölf Jahre Soldat, hat bei Saller seine Ausbildung zum Fahrlehrer gemacht und gehört seit 2007 fest dazu. Seit Mai 2023 führt er die Fahrschule. Er bildet B und BE sowie alle Zweiradklassen aus und fährt in seiner Freizeit selbst leidenschaftlich Motorrad.</p>
      <div class="si-fvn"><img src="img/fvn.png" alt="Fahrlehrerverband Niedersachsen e.V. – Ihre Verbandsfahrschule" loading="lazy"></div>
      <a class="btn btn-a" href="#kontakt">Jetzt anmelden {AR}</a>
    </div>
  </div>
  <div class="w"><ul class="si-v">{vt}</ul></div>
</section>"""
    orte_l = [('Badbergen', 'Hauptstraße 64', '49635 Badbergen', 'Montags', 'o-badbergen.jpg', 'Hauptstraße 64 49635 Badbergen'),
              ('Alfhausen', 'Hauptstraße 6', '49594 Alfhausen', 'Dienstags', 'o-alfhausen.jpg', 'Hauptstraße 6 49594 Alfhausen'),
              ('Ankum', 'Hauptstraße 75 (Gebäude OLB)', '49577 Ankum', 'Mittwochs', 'o-ankum.jpg', 'Hauptstraße 75 49577 Ankum'),
              ('Bersenbrück', 'Bramscher Straße 54', '49593 Bersenbrück', 'Donnerstags', 'o-bersenbrueck.jpg', 'Bramscher Straße 54 49593 Bersenbrück')]
    oc = ''.join(f"""<article class="so-o" data-r>
      <figure><img src="img/{img}" alt="Schulungsraum der Fahrschule Saller in {o}" loading="lazy"></figure>
      <div><p class="so-tag">{tag} · 18:00 – 19:45 Uhr</p><h3>{o}</h3><p>{st}<br>{pl}</p>
      <p class="so-l"><a href="{_sal_map(q)}" target="_blank" rel="noopener">Route planen {AR}</a> <a href="tel:{s['tel_i']}">Mobil 0171-3866717</a></p></div>
    </article>""" for o, st, pl, tag, img, q in orte_l)
    orte_sec = f"""<section class="sec sor" id="orte">
  <div class="w"><div data-r><p class="ey">Unterricht und Anmeldung</p><h2 class="h2">Unsere Schulungsräume <em>findest du in:</em></h2></div>
  <div class="sor-g">{oc}</div></div>
</section>"""
    eh = f"""<section class="sec seh" id="erste-hilfe">
  <div class="w seh-g">
    <div data-r><p class="ey">Erste-Hilfe-Kurs &amp; Sehtest</p><h2 class="h2">Alles für deinen Antrag <em>an einem Samstag.</em></h2>
      <p class="lead">Für den Führerschein brauchst du einen Erste-Hilfe-Kurs und einen Sehtest. Beides bekommst du direkt bei uns: Der Kurs findet ein- bis zweimal im Monat samstags in Badbergen statt, den Sehtest buchst du einfach dazu.</p>
      <p class="seh-n"><span>Nächster Termin</span><b>Samstag, 19.12.2026</b><small>in Badbergen · Anmeldung über das Formular oder telefonisch</small></p>
      <a class="btn btn-a" href="#kontakt">Platz im Kurs sichern {AR}</a></div>
    <figure class="seh-f" data-r="2"><img src="img/eh-flyer.jpg" alt="Flyer Erste-Hilfe-Kurs der Fahrschule Saller" loading="lazy"></figure>
  </div>
</section>"""
    flotte_k = [('f-cooper.jpg', 'Cooper', 'VW Golf VIII · Klasse B'), ('f-octavia.jpg', 'Octavia', 'Skoda Octavia · Schaltung'), ('f-obelix.jpg', 'Obelix', 'Koch-Anhänger 2.700 kg · BE'),
                ('f-ladyk.jpg', 'Lady K', 'Kawasaki Z650 · A'), ('f-er6.jpg', 'ER-6n', 'Kawasaki · A2'), ('f-duke.jpg', 'KTM Duke', 'A1 / B196'),
                ('f-z125.jpg', 'Z125', 'Kawasaki · A1'), ('f-matilda.jpg', 'Matilda', 'Hyosung Aquila GV 125 S')]
    fk = ''.join(f'<li data-r><img src="img/{i}" alt="{t}" loading="lazy"><b>{t}</b><span>{x}</span></li>' for i, t, x in flotte_k)
    fuhr = f"""<section class="sec sfp" id="fuhrpark">
  <div class="w sfp-top">
    <figure class="sfp-hero" data-r><img src="img/f-oskar.jpg" alt="Skoda Octavia RS Automatik „Oskar“" loading="lazy"></figure>
    <div data-r="2"><p class="ey">Fuhrpark</p><h2 class="h2">Darf ich vorstellen: <em>Oskar.</em></h2>
      <p class="lead">Unser Skoda Octavia RS mit Automatik ist der Neue im Team und perfekt für B197. Bei uns haben die Fahrzeuge Namen, und jedes ist für einen bestimmten Führerschein da.</p></div>
  </div>
  <div class="w"><ul class="sfp-l">{fk}</ul></div>
</section>"""
    medien = f"""<section class="sec smr" id="medienraeume">
  <div class="w"><div data-r><p class="ey">Medienräume</p><h2 class="h2">Theorie in <em>modernen Medienräumen.</em></h2><p class="lead">In allen vier Orten lernst du in hellen Räumen mit moderner Technik. Dazu kommt die FahrAPP, mit der du unterwegs am Handy übst.</p></div>
  <div class="smr-g">
    <figure data-r><img src="img/m-badbergen.jpg" alt="" loading="lazy"><figcaption>Badbergen</figcaption></figure>
    <figure data-r><img src="img/m-alfhausen.jpg" alt="" loading="lazy"><figcaption>Alfhausen</figcaption></figure>
    <figure data-r><img src="img/m-ankum.jpg" alt="" loading="lazy"><figcaption>Ankum</figcaption></figure>
    <figure data-r><img src="img/m-bersenbrueck.jpg" alt="" loading="lazy"><figcaption>Bersenbrück</figcaption></figure>
  </div></div>
</section>"""
    region = f"""<section class="sec sre" id="region">
  <div class="w sre-g">
    <div data-r><p class="ey">Für die Region</p><h2 class="h2">Gemeinsam engagieren wir uns <em>für die Region.</em></h2><p class="lead">Ob Festanhänger oder Fußballdart XXL: Wir unterstützen Vereine und Veranstaltungen bei uns im Artland.</p>
      <a class="btn btn-o" href="https://p-h-s-druck.eu/075729/" target="_blank" rel="noopener">Mehr erfahren {AR}</a></div>
    <div class="sre-p">
      <figure data-r><img src="img/r-fest.jpg" alt="Festanhänger mit Fahrschule-Saller-Werbung" loading="lazy"><figcaption>Festanhänger</figcaption></figure>
      <figure data-r="2"><img src="img/r-dart.jpg" alt="Fußballdart XXL" loading="lazy"><figcaption>Fußballdart XXL</figcaption></figure>
    </div>
  </div>
</section>"""
    behoerde = f"""<section class="sec sbh">
  <div class="w sbh-g">
    <div data-r><p class="ey">Zuständige Fahrerlaubnisbehörde</p><p class="sbh-a"><b>Landkreis Osnabrück</b><br>Am Schölerberg 1<br>49082 Osnabrück</p></div>
    <div data-r="2"><p class="ey">Lernen am Handy</p><p class="sbh-a"><b>FahrAPP &amp; FahrPRAXIS</b><br>Theorie üben und Fahrstunden im Blick, wann und wo du willst.</p>
      <p class="sbh-s"><img src="img/appstore.png" alt="Download im App Store" loading="lazy"><img src="img/googleplay.png" alt="Jetzt bei Google Play" loading="lazy"></p></div>
    <div data-r="3" class="sbh-grus"><p>Wir freuen uns auf Dich!</p><b>Euer Henrik Grover</b></div>
  </div>
</section>"""
    return (hd(s, False) + hero
        + marquee(['Klasse B', 'B197 Automatik', 'BF17', 'BE Anhänger', 'A · A2 · A1', 'B196', 'AM · Mofa', 'Erste Hilfe &amp; Sehtest'])
        + intro + region + orte_sec + eh + fuhr
        + klassen('klassen', 'FS-Klassen', 'Welcher Führerschein <em>passt zu dir?</em>', 'Tipp auf eine Klasse, dann sagt dir Oskar in 30 Sekunden, ob sie passt.', [
            ('B', 'Auto', 'Der klassische Führerschein. Mit BF17 schon ab 17 begleitet fahren.', 'ab 17', 'auto'),
            ('B197', 'Automatik mit Schaltkompetenz', 'Prüfung auf Automatik, trotzdem darfst du Schaltwagen fahren.', 'ab 17', 'auto'),
            ('BE', 'Anhänger', 'Für Pferdeanhänger, Wohnwagen und schwere Gespanne.', 'ab 18', 'anh'),
            ('A2', 'Motorrad bis 35 kW', 'Der Einstieg ins richtige Motorradfahren.', 'ab 18', 'moto'),
            ('A1', 'Leichtkraftrad 125', 'Mit 16 aufs Motorrad.', 'ab 16', 'moto'),
            ('A', 'Motorrad unbeschränkt', 'Direkt ab 24, mit A80 ab 21.', 'ab 24', 'moto'),
            ('B196', '125er mit Autoführerschein', 'Schulung ohne Prüfung, wenn du 25 bist und 5 Jahre B hast.', 'ab 25', 'roller'),
            ('AM · Mofa', 'Roller', 'Mopeds und Roller, schon ab 15.', 'ab 15', 'roller')])
        + medien
        + story('geschichte', 'Über uns', 'Seit 1989 <em>im Artland.</em>', [
            '1989 hat Kalle Saller die Fahrschule gegründet und viele Jahre mit seiner Frau Irmgard geführt. Viele tausend glückliche Fahrschüler später hat er den Stab weitergegeben.',
            'Seit dem 1. Mai 2023 ist Henrik Grover Inhaber. Mit im Team: seine Frau Moni, die als Erste-Hilfe-Ausbilderin die Kurse in Badbergen gibt.'],
            'p-kalle.jpg', cap='Kalle Saller, Gründer der Fahrschule', tl=[('1989', 'Kalle Saller gründet die Fahrschule'), ('2007', 'Henrik kommt ins Team'), ('2023', 'Henrik übernimmt als Inhaber')], cls='alt')
        + ablauf('ablauf', 'So läuft’s', 'In vier Schritten <em>zum Führerschein.</em>', '', [
            ('Anmelden', 'Online oder an einem der vier Abende vor Ort. Wir beraten dich gern.'),
            ('Erste Hilfe &amp; Sehtest', 'Gibt es direkt bei uns, samstags in Badbergen.'),
            ('Theorie', 'Unterricht an vier Abenden pro Woche, dazu die FahrAPP zum Üben am Handy.'),
            ('Fahren &amp; bestehen', 'Fahrstunden mit Henrik, Sonderfahrten, dann ab in die Prüfung.')])
        + reviews(s, ['Ich weiß gar nicht, wo ich anfangen soll: Alles war super verständlich und ich konnte jederzeit Fragen stellen. Wenn ich etwas nochmal üben wollte, haben wir das gemacht.',
                      'Von der Anmeldung bis zur Prüfung lief alles perfekt. Henrik ist ein super Fahrlehrer, der genau weiß, was er tut.',
                      'Der Unterricht ist nicht langweilig und die Fahrlehrer sind sehr nett.',
                      'Gut erklärt, fair, und ich habe mich bei den Fahrstunden richtig wohlgefühlt. Danke an das ganze Team!'], 'dk')
        + sorgen('fragen', 'Ehrlich gefragt', 'Was dich vorher <em>beschäftigt.</em>', '', [
            ('Ich wohne in Ankum. Muss ich jedes Mal nach Badbergen?', 'Nein. Theorie und Anmeldung gibt es <b>in Badbergen, Alfhausen, Ankum und Bersenbrück</b>, an jedem Abend in einem anderen Ort.'),
            ('Wo bekomme ich Erste Hilfe und Sehtest her?', 'Direkt bei uns. Der <b>Erste-Hilfe-Kurs</b> läuft samstags in Badbergen, den <b>Sehtest</b> kannst du gleich mitbuchen.'),
            ('Ich will Automatik fahren, aber nicht festgelegt sein.', 'Dafür gibt es <b>B197</b>: Du machst die Prüfung auf Oskar mit Automatik und darfst trotzdem Schaltwagen fahren.'),
            ('Ich hab Respekt vor der ersten Stunde.', 'Musst du nicht. Unsere Fahrschüler schreiben: <b>Man kann jederzeit fragen</b>, und was noch nicht sitzt, wird einfach nochmal geübt.')])
        + behoerde + contact(s) + footer(s))

CAR = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M5 11l1.5-4.5A2 2 0 0 1 8.4 5h7.2a2 2 0 0 1 1.9 1.5L19 11a2 2 0 0 1 2 2v4h-2v2h-3v-2H8v2H5v-2H3v-4a2 2 0 0 1 2-2zm2.1 0h9.8l-1-3H8.1zM6.5 15a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm11 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/></svg>'
AID = '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M9 3h6v3h5a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h5zm2 0v3h2V3zm0 7v3H8v2h3v3h2v-3h3v-2h-3v-3z"/></svg>'

S = SITES['saller'] = site(
    slug='fahrschule-saller-badbergen', firma='Fahrschule K.H. Saller', web='fahrschule-saller.de', fonts='r14sal',
    title='Fahrschule Saller – Führerschein in Badbergen, Alfhausen, Ankum & Bersenbrück', desc='Fahrschule K.H. Saller, Inh. Henrik Grover: Auto, Motorrad, Roller und Anhänger. Unterricht in Badbergen, Alfhausen, Ankum und Bersenbrück.',
    tel='0171 3866717', tel_i='+491713866717', mail='info@fahrschule-saller.de', adresse='Hauptstraße 64, 49635 Badbergen', google=('4,8', 23),
    cta='Jetzt anmelden', logo_txt='<img src="img/logo.png" alt="Fahrschule K.H. Saller, Inh. Henrik Grover" style="height:52px;width:auto;display:block">',
    nav=[('Über uns', 'ueber'), ('Standorte', 'orte'), ('Erste Hilfe', 'erste-hilfe'), ('Fuhrpark', 'fuhrpark'), ('FS-Klassen', 'klassen')],
    hours=[('Mo · Badbergen', '18:00 – 19:45'), ('Di · Alfhausen', '18:00 – 19:45'), ('Mi · Ankum', '18:00 – 19:45'), ('Do · Bersenbrück', '18:00 – 19:45')],
    form_lbl='Führerschein', form_opts=['Auto · Klasse B / BF17', 'Automatik · B197', 'Anhänger · BE', 'Motorrad · A / A2 / A1', '125er · B196', 'Roller · AM / Mofa', 'Erste-Hilfe-Kurs &amp; Sehtest'],
    form_orte=['Badbergen', 'Alfhausen', 'Ankum', 'Bersenbrück'],
    form_h3='Anmeldung Führerschein', form_p='Schnell und unkompliziert anmelden. Henrik meldet sich bei dir und ihr klärt den Start.', form_btn='Anmeldung abschicken',
    kt_ey='Anmeldung', kt_h2='Wir freuen uns <em>auf Dich!</em>', kt_p='Ruf an, schreib uns oder komm an einem der vier Abende vorbei.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>', social=[('Instagram', 'https://www.instagram.com/fahrschule.saller')],
    vars='--bg:#ffffff;--ink:#1d1d1f;--mute:#55555c;--p:#e60000;--p-ink:#fff;--a:#e60000;--a-ink:#fff;--y:#fef518;--dk:#1d1d1f;--s:#fff;--s2:#f4f2ef;--fh:"Archivo",Arial,sans-serif;--fb:"Archivo",system-ui,sans-serif;--r:6px;--r2:10px;--br:6px;--mq-bg:#e60000;--mq-ink:#fff;--hd-bg:#e60000;--hd-ink:#fff;--ft-bg:#141416',
    css=SALLER_CSS)
S['bot'] = BOT('Oskar', 'dein Führerschein-Lotse', 'Fahrschule Saller', S, ['B', 'B197', 'BE', 'A', 'A2', 'A1', 'B196', 'AM', 'Mofa'],
    {'schnell': 'Mit vier Unterrichtsabenden pro Woche kommst du bei uns zügig durch die Theorie.', 'ruhe': 'Henrik nimmt sich Zeit. Was noch nicht sitzt, wird nochmal geübt.', 'flex': 'Theorie gibt es Montag bis Donnerstag in vier Orten. Such dir den Abend aus, der passt.', 'angst': 'Unsere Fahrschüler sagen: Man kann jederzeit fragen, und was nicht sitzt, wird nochmal geübt.'},
    qa=[('erste hilfe|sehtest', 'Den Erste-Hilfe-Kurs bieten wir samstags in Badbergen an, nächster Termin ist der 19.12.2026. Den Sehtest kannst du dazubuchen.'), ('wo|ort|adresse|ankum|alfhausen|bersenbrück|badbergen', 'Unterricht und Anmeldung: Mo Badbergen, Di Alfhausen, Mi Ankum, Do Bersenbrück, jeweils 18:00–19:45 Uhr.'), ('motorrad|125|b196', 'Henrik bildet alle Zweiradklassen aus, von AM bis A. Für B196 brauchst du 25 Jahre und 5 Jahre Klasse B.')],
    tour=[('#ueber', 'Das ist Henrik, dein Fahrlehrer.'), ('#orte', 'Vier Orte, vier Abende: Such dir aus, wo du Theorie machst.'), ('#erste-hilfe', 'Erste Hilfe und Sehtest gibt es direkt bei uns.'), ('#fuhrpark', 'Unsere Fahrzeuge, alle mit Namen.'), ('#kontakt', 'Und hier meldest du dich an.')])
S['img'] = {'h-schluessel.jpg': ('saller/img/i001.jpeg', 1500), 'p-henrik.jpg': ('saller/img/i002.jpeg', 900), 'logo.png': ('saller/img/i020.png', 0), 'fvn.png': ('saller/img/i021.png', 0),
    'o-badbergen.jpg': ('saller/img/i007.jpeg', 0), 'o-alfhausen.jpg': ('saller/img/i003.jpg', 0), 'o-ankum.jpg': ('saller/img/i005.jpg', 0), 'o-bersenbrueck.jpg': ('saller/img/i009.jpg', 0),
    'm-badbergen.jpg': ('saller/img/i008.jpg', 0), 'm-alfhausen.jpg': ('saller/img/i004.jpg', 0), 'm-ankum.jpg': ('saller/img/i006.jpg', 0), 'm-bersenbrueck.jpg': ('saller/img/i010.jpg', 0),
    'eh-flyer.jpg': ('saller/img/i019.jpeg', 700), 'r-fest.jpg': ('saller/img/i017.jpeg', 900), 'r-dart.jpg': ('saller/img/i018.jpeg', 900), 'p-kalle.jpg': ('saller/img/i012.jpg', 0),
    'f-oskar.jpg': ('saller/img/i013.jpg', 1300), 'f-cooper.jpg': ('saller/img/i025.jpg', 0), 'f-octavia.jpg': ('saller/img/i030.jpg', 0), 'f-obelix.jpg': ('saller/img/i028.jpg', 0),
    'f-ladyk.jpg': ('saller/img/i032.png', 0), 'f-er6.jpg': ('saller/img/i027.jpg', 0), 'f-duke.jpg': ('saller/img/i026.jpg', 0), 'f-z125.jpg': ('saller/img/i031.jpg', 0),
    'f-matilda.jpg': ('saller/img/i024.png', 0), 'appstore.png': ('saller/img/i022.png', 0), 'googleplay.png': ('saller/img/i023.png', 0)}
S['body'] = b_saller

# ───────────── 2. Fahrschule Bernhard Albers, Ankum ─────────────
def b_albers(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 60%', quick=['auto', 'moto', 'lkw'],
        ey='Fahrschule · Aus- und Weiterbildung · Ankum',
        h1='Vom ersten Führerschein <em>bis zum Berufskraftfahrer.</em>',
        sub='Die Fahrschule Bernhard Albers in Ankum bildet Fahranfänger aus und qualifiziert Berufskraftfahrer: Auto, Motorrad, Lkw, Stapler und Erste Hilfe aus einer Hand.',
        badge=('Ankum', 'Fahrschule im Artland')))
        + marquee(['Pkw', 'Motorrad', 'Lkw', 'Beschleunigte Grundqualifikation', 'Weiterbildung Lkw &amp; Bus', 'Ladungssicherung', 'Staplerschein', 'Erste Hilfe'])
        + svc('angebot', 'Zwei Bereiche', 'Fahrschule <em>und Weiterbildung.</em>', 'Für Fahrschüler genauso wie für Unternehmen, die ihre Fahrer schulen wollen.', [
            ('Fahren lernen', 'Theorie in unseren Unterrichtsräumen, Fahrstunden in Fahrzeugen mit dem Albers-Schriftzug. Für Auto und Motorrad.'),
            ('Anmeldung &amp; Beratung', 'Persönlich, telefonisch oder mit unseren Formularen. Wir klären, welche Klasse passt.'),
            ('Aus- und Weiterbildung', 'Beschleunigte Grundqualifikation, Weiterbildung Lkw &amp; Bus, Ladungssicherung.'),
            ('Stapler &amp; Erste Hilfe', 'Gabelstaplerausbildung und Erste-Hilfe-Kurse aus einer Hand.')])
        + gallery('einblicke', 'Einblicke', 'So sieht es <em>bei uns aus.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%')], 'alt')
        + klassen('klassen', 'Was Sie bei uns lernen', 'Vom Auto <em>bis zum Lkw.</em>', 'Welche Klasse die richtige ist, klären wir gern im Gespräch. Oder Sie machen den Schnell-Check.', [
            ('B', 'Auto', 'Der Führerschein für den Alltag.', 'ab 17', 'auto'),
            ('A', 'Motorrad', 'Vom Leichtkraftrad bis zur großen Maschine.', 'ab 16', 'moto'),
            ('C · CE', 'Lkw', 'Für Beruf und Gewerbe, auf Wunsch mit Berufskraftfahrer-Qualifikation.', 'ab 21', 'lkw'),
            ('Stapler', 'Gabelstapler', 'Staplerschein für Mitarbeiter und Unternehmen.', 'Beruf', 'lkw')])
        + ablauf('ablauf', 'Ihr Weg', 'So kommen Sie <em>zum Führerschein.</em>', '', [
            ('Beraten lassen', 'Rufen Sie an oder kommen Sie vorbei. Wir klären, welche Klasse passt.'),
            ('Anmelden', 'Formulare gibt es bei uns, die Anmeldung dauert nur ein paar Minuten.'),
            ('Theorie &amp; Erste Hilfe', 'Unterricht in unseren Räumen, den Erste-Hilfe-Kurs bekommen Sie gleich mit.'),
            ('Fahren &amp; Prüfung', 'Fahrstunden in unseren Fahrzeugen, dann die Prüfung.')])
        + promo('unternehmen', 'p-lkw.jpg', 'Für Unternehmen', 'Kraftfahrer gesucht? <em>Wir schulen sie.</em>', 'Ob Grundqualifikation für neue Fahrer, Pflicht-Weiterbildung oder Ladungssicherung: Wir stellen ein passendes Weiterbildungspaket für Ihre Mitarbeiter zusammen.', ['Beschleunigte Grundqualifikation', 'Weiterbildungsmodule Lkw &amp; Bus', 'Handwerker-Spezial'], 'Paket anfragen', 'dk')
        + contact(s) + footer(s))

S = SITES['albers'] = site(
    slug='fahrschule-albers-ankum', firma='Fahrschule Bernhard Albers', web='fahrschule-albers.de', fonts='r14alb', du=False,
    title='Fahrschule Bernhard Albers – Fahrschule und Weiterbildung in Ankum', desc='Fahrschule Bernhard Albers in Ankum: Führerschein für Auto, Motorrad und Lkw, Berufskraftfahrer-Qualifikation, Ladungssicherung, Staplerschein und Erste Hilfe.',
    tel='05462 323', tel_i='+495462323', mail='fahrschule-albers@gmx.de', adresse='49577 Ankum', google=None,
    cta='Beratung anfragen', nav=[('Angebot', 'angebot'), ('Klassen', 'klassen'), ('Ablauf', 'ablauf'), ('Unternehmen', 'unternehmen'), ('Kontakt', 'kontakt')],
    hours=[('Telefon', '05462 323'), ('Fax', '05462 961100')],
    form_lbl='Interesse an', form_opts=['Führerschein Auto · B', 'Motorrad · A', 'Lkw · C / CE', 'Grundqualifikation / Weiterbildung', 'Staplerschein', 'Erste Hilfe'],
    form_h3='Beratung anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Sprechen Sie <em>mit uns.</em>', kt_p='Fahrschule Bernhard Albers in Ankum, Telefon 05462 323.',
    social=[('Facebook', 'https://www.facebook.com/pages/Fahrschule-Bernhard-Albers/208075782567502')],
    vars='--bg:#fbfbf7;--ink:#1b2326;--mute:#58646a;--p:#8fb31d;--p-ink:#13200a;--a:#1aa1b8;--a-ink:#fff;--dk:#13262c;--s:#fff;--s2:#eef3e6;--fh:"Bitter",Georgia,serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:12px;--r2:18px;--br:8px;--mq-bg:#8fb31d;--mq-ink:#13200a;--hd-bg:rgba(251,251,247,.95);--hd-ink:#1b2326;--logo-h:46px;--ft-bg:#0d1c21',
    css='''.hp h1{font-weight:800;line-height:1.08}.h2{font-weight:800;line-height:1.1}.hp h1 em,.h2 em{font-style:normal;color:#1aa1b8}.dk .h2 em{color:#b9dd4a}
.comp{height:380px}.comp .c1{width:62%}@media (max-width:600px){.comp{height:300px}.comp .c1{width:52%}}.promo figure{max-width:430px;justify-self:center}.gl .grid{grid-template-columns:repeat(4,1fr)}.gl .grid .w2{grid-column:span 1}.comp figure img{object-fit:cover}.hd .logo img{height:46px}.ft img{background:#fff;padding:8px 12px;border-radius:6px}
.gl .grid{grid-auto-rows:210px}.kl .k b{font-family:var(--fh)}
.hp{background:linear-gradient(90deg,var(--bg) 0%,color-mix(in srgb,var(--bg) 92%,transparent) 34%,color-mix(in srgb,var(--bg) 25%,transparent) 56%,color-mix(in srgb,var(--bg) 10%,transparent) 100%),url(img/emo.jpg) 30% 50%/cover no-repeat!important}.hp::before{opacity:.35}@media(max-width:820px){.hp{background:linear-gradient(0deg,var(--bg) 52%,color-mix(in srgb,var(--bg) 30%,transparent) 80%),url(img/emo.jpg) 30% 50%/auto 62% no-repeat!important}}''')
S['bot'] = BOT('Bruno', 'Ihr Fahrschul-Lotse', 'der Fahrschule Albers', S, ['B', 'A', 'A2', 'A1', 'C', 'CE'],
    {'schnell': 'Rufen Sie uns an, dann planen wir den schnellsten Weg zur Prüfung.', 'ruhe': 'Bei uns lernen Sie in Ruhe, mit Fahrlehrern, die sich Zeit nehmen.', 'flex': 'Fahrstunden stimmen wir mit Ihnen ab, auch neben dem Job.', 'angst': 'Sprechen Sie es einfach an. Wir starten so, dass Sie sich sicher fühlen.'},
    qa=[('stapler', 'Ja, wir bieten die Gabelstaplerausbildung an, für Einzelpersonen und Unternehmen.'), ('bkf|berufskraft|modul|weiterbild|grundqual', 'Wir bieten die beschleunigte Grundqualifikation und die Weiterbildungsmodule für Lkw und Bus an.')],
    tour=[('#angebot', 'Zwei Bereiche: Fahrschule und Weiterbildung.'), ('#klassen', 'Vom Auto bis zum Lkw.'), ('#unternehmen', 'Für Unternehmen: Schulungspakete für Ihre Fahrer.'), ('#kontakt', 'Hier fragen Sie Beratung an.')], du=False)
C = (0, .1, 1, 1)
S['img'] = {'logo.png': ('albers/img/i008.jpg', 0, 'trimalpha'), 'h1.jpg': ('albers/img/i014.jpg', 0, C), 'h2.jpg': ('albers/img/i015.jpg', 0, C), 'h3.jpg': ('albers/img/i017.jpg', 0, C),
    'd-fs.jpg': ('albers/img/i018.jpg', 0, C), 'd-bkf.jpg': ('albers/img/i013.jpg', 0, C), 'p-lkw.jpg': ('albers/img/i009.jpg', 0, C),
    'g1.jpg': ('albers/img/i016.jpg', 0, C), 'g2.jpg': ('albers/img/i011.jpg', 0, C), 'g3.jpg': ('albers/img/i012.jpg', 0, C), 'g4.jpg': ('albers/img/i010.jpg', 0, C), 'g5.jpg': ('albers/img/i017.jpg', 0, C), 'g6.jpg': ('albers/img/i014.jpg', 0, C)}
S['body'] = b_albers

# ───────────── 3. Fahrschule HP 66, Nortrup · Dinklage · Gehrde ─────────────
def b_hp66(s):
    return (hd(s) + hero_x(s, dict(
        img='h-car.jpg', pos='50% 50%', quick=['auto', 'moto', 'roller', 'lkw', 'trak'],
        ey='Fahrschule HP 66 · Nortrup · Dinklage · Gehrde',
        h1='Sicher in die Prüfung. <em>Ohne Umwege.</em>',
        sub='Peter Hackmann und Claudia Hackmann-Paschert begleiten dich von der Anmeldung bis zur praktischen Prüfung. Zu fairen Preisen, mit entspannten Fahrlehrern und modernen BMW.'))
        + marquee(['Klasse B &amp; BF17', 'BE · B96', 'A · A2 · A1 · AM', 'C · CE · C1', 'D · D1', 'Traktor T', 'EU-Berufskraftfahrer'], 'hpm')
        + sorgen('fragen', 'Häufige Fragen', 'Das wollen <em>alle wissen.</em>', '', [
            ('Wie lange dauert mein Führerschein?', 'Das hängt davon ab, wie oft du zur Theorie kommst und Zeit zum Fahren hast. Als Richtwert: <b>etwa 3 bis 6 Monate.</b>'),
            ('Was passiert nach der Online-Anmeldung?', 'Wir melden uns bei dir und besprechen <b>persönlich</b>, wie deine Ausbildung bei uns läuft.'),
            ('Welche Autos habt ihr?', 'Vor allem die <b>BMW X1</b> und den <b>3er</b>, mit Schaltung und mit Automatik.'),
            ('Was brauche ich für den Antrag?', 'Antrag (bekommst du von uns), <b>biometrisches Passbild, Sehtest und Erste-Hilfe-Nachweis</b>. Bei Erweiterungen eine Kopie deines Führerscheins.')], 'dk')
        + flotte('fahrzeuge', 'Unsere Fahrzeuge', 'Moderne Marken, <em>sauber vorbereitet.</em>', 'Nicht nur die Fahrlehrer sind wichtig, auch die Fahrzeuge. Darum setzen wir auf moderne Markenhersteller.', [
            ('f-x1.png', 'BMW X1', 'Klasse B', '50% 50%'), ('f-3er.png', 'BMW 3er Touring', 'Klasse B · Schaltung &amp; Automatik', '50% 50%'), ('f-z.png', 'Kawasaki', 'Klasse A / A2', '50% 50%'),
            ('f-z2.png', 'Kawasaki', 'Klasse A1', '50% 50%'), ('f-roller.png', 'Roller', 'Klasse AM', '50% 50%'), ('f-anh.png', 'Anhänger', 'Klasse BE · B96', '50% 50%')], cls='show dk', cut=True)
        + orte('orte', 'Standorte', 'Drei Orte, <em>drei Abende.</em>', 'Anmeldung und Unterricht jeweils ab 18:30 Uhr.', [
            ('Nortrup', 'Kirchstraße 1', 'Donnerstags'), ('Dinklage', 'Burgstraße 7', 'Montags'), ('Gehrde', 'Lindenstraße 22', 'Dienstags')], 'alt')
        + ablauf('ablauf', 'Auf geht’s', 'Dein Weg <em>zum Führerschein.</em>', '', [
            ('Online anmelden', 'Klassen auswählen, abschicken. Bei Minderjährigen brauchen wir die Unterschrift der Eltern.'),
            ('Persönlich starten', 'Beim ersten Besuch bekommst du deinen Ausbildungsvertrag mit allen Infos.'),
            ('Theorie &amp; Online lernen', 'Unterricht in Nortrup, Dinklage oder Gehrde, dazu online lernen.'),
            ('Fahren &amp; bestehen', 'Fahrstunden im BMW, dann sicher in die Prüfung.')])
        + reviews(s, ['Tolle Fahrschule, alles wurde perfekt erklärt, um die Prüfung zu bestehen. Es hat immer richtig Spaß gemacht. Danke euch beiden!',
                      'Sehr freundlich, alles wird gut erklärt und es gibt hilfreiche Tipps. Ich kann den Führerschein hier nur empfehlen.',
                      'Super Fahrschule, super Fahrlehrer. Hier bestehst du deine Prüfung.',
                      'Klasse Fahrstunden. Die Nachtfahrt inklusive Stopp an der Dönerbude war ein Highlight!'], 'dk')
        + contact(s) + footer(s))

S = SITES['hp66'] = site(
    slug='fahrschule-hp66-nortrup', firma='Fahrschule HP 66', web='fahrschule-hp-66.de', fonts='r14hp',
    title='Fahrschule HP 66 – Führerschein in Nortrup, Dinklage & Gehrde', desc='Fahrschule HP 66, Inh. Peter Hackmann: alle Klassen vom Mofa bis zum Bus, EU-Berufskraftfahrer. Standorte Nortrup, Dinklage und Gehrde.',
    tel='0170 2112506', tel_i='+491702112506', mail='fahrschule-hp-66@t-online.de', adresse='Kirchstraße 1, 49638 Nortrup', google=('5,0', 10),
    cta='Jetzt anmelden', nav=[('Fragen', 'fragen'), ('Fahrzeuge', 'fahrzeuge'), ('Standorte', 'orte'), ('Ablauf', 'ablauf'), ('Kontakt', 'kontakt')],
    hours=[('Mo · Dinklage', 'ab 18:30'), ('Di · Gehrde', 'ab 18:30'), ('Do · Nortrup', 'ab 18:30')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', 'Lkw · C / CE / C1', 'Bus · D / D1', 'Traktor · T', 'EU-Berufskraftfahrer'],
    form_orte=['Nortrup', 'Dinklage', 'Gehrde'],
    form_h3='Auf die Plätze, fertig, los', form_p='Melde dich an, wir rufen dich an und besprechen den Start.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Dein schneller <em>Draht zu uns.</em>', kt_p='Anrufen, WhatsApp oder Formular, wie es dir am liebsten ist.',
    rv_h2='Was Fahrschüler <em>über uns sagen.</em>', social=[('Instagram', 'https://www.instagram.com/fahrschulehp66/'), ('Facebook', 'https://www.facebook.com/FahrschuleHP66/'), ('WhatsApp', 'https://wa.me/491702112506')],
    logo_txt='<img src="img/logo.svg" alt="Fahrschule HP 66" style="height:46px;width:auto;display:block">',
    vars='--bg:#f4f5f2;--ink:#0e0e0e;--mute:#4f5450;--p:#b8ff25;--p-ink:#0e0e0e;--a:#b8ff25;--a-ink:#0e0e0e;--dk:#0e0e0e;--s:#fff;--s2:#e8ebe4;--fh:"Montserrat",system-ui,sans-serif;--fb:"Montserrat",system-ui,sans-serif;--r:16px;--r2:24px;--br:999px;--mq-bg:#121513;--mq-ink:#8bd12a;--hd-bg:rgba(14,14,14,.94);--hd-ink:#fff;--ft-bg:#0e0e0e;--hx-bg:#0e0e0e;--fl-bg:#fff',
    css='''.hx{color:#fff}.hx .sub{color:rgba(255,255,255,.75)}.hx .btn-o{color:#fff}.hx h1{font-weight:700}.hx h1 em{color:var(--p)}.hx .pic{--hx-ar:16/11;--hx-r:28px}
.hx::before{content:"";position:absolute;right:-10%;top:-20%;width:60%;height:140%;background:radial-gradient(closest-side,rgba(139,209,42,.22),transparent);z-index:1}
.hx .chip{background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2);color:#fff}.h2{font-weight:700;letter-spacing:-.02em}.h2 em{font-style:normal;color:#5e9a10}.dk .h2 em{color:var(--p)}
.hd .lt-logo{color:#fff}.fl .v figure{background:#fff}
.hx .pic{background:transparent!important;box-shadow:none!important;border-radius:0!important;overflow:visible}.hx .pic img{object-fit:contain;border-radius:0}
section:not(.hx):not(.dk) .ey{color:#3f6b00}''')
S['bot'] = BOT('Paul', 'dein HP-66-Lotse', 'der Fahrschule HP 66', S, ['B', 'BE', 'B96', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE', 'D', 'T', 'L'],
    {'schnell': 'Als Richtwert brauchst du 3 bis 6 Monate. Je öfter du zur Theorie kommst, desto schneller geht’s.', 'ruhe': 'Unsere Fahrschüler loben vor allem eins: entspannte Fahrlehrer, alles wird gut erklärt.', 'flex': 'Unterricht gibt es montags in Dinklage, dienstags in Gehrde, donnerstags in Nortrup.', 'angst': 'Bei uns geht es entspannt zu. Und es gibt die BMW auch mit Automatik.'},
    qa=[('auto|bmw|automatik', 'Wir fahren BMW X1 und 3er, mit Schaltung und mit Automatik.'), ('dauer|lange', 'Als Richtwert 3 bis 6 Monate, je nachdem, wie oft du Zeit für Theorie und Fahrstunden hast.'), ('antrag|unterlagen|passbild', 'Für den Antrag brauchst du ein biometrisches Passbild, Sehtest und Erste-Hilfe-Nachweis. Den Antrag selbst bekommst du von uns.')],
    tour=[('#fragen', 'Die häufigsten Fragen, direkt beantwortet.'), ('#fahrzeuge', 'Unsere Fahrzeuge.'), ('#orte', 'Drei Standorte, drei Abende.'), ('#kontakt', 'Und hier geht’s zur Anmeldung.')])
S['img'] = {'h-car.jpg': ('hp66/img/i001.webp', 0, '#0e0e0e'), 'logo.svg': ('hp66/brand/logo.svg', 0), 'f-x1.png': ('hp66/img/i006.webp', 0), 'f-3er.png': ('hp66/img/i003.webp', 0), 'f-z.png': ('hp66/img/i005.webp', 0),
    'f-z2.png': ('hp66/img/i004.webp', 0), 'f-roller.png': ('hp66/img/i007.webp', 0), 'f-anh.png': ('hp66/img/i002.webp', 0)}
S['body'] = b_hp66

# ───────────── 4. Fahrschule Beckermann, Quakenbrück · Bramsche · Alfhausen · Merzen · Osnabrück ─────────────
def b_beckermann(s):
    return (hd(s) + hero_x(s, dict(
        img='h1.jpg', pos='50% 60%', wide=True, quick=['auto', 'moto', 'roller', 'lkw', 'trak'],
        ey='Fahrschule Beckermann · fünfmal in deiner Nähe',
        h1='Dein Führerschein. <em>Deine Freiheit.</em>',
        sub='Vom Roller bis zum Reisebus: Die Fahrschule Beckermann bildet in Quakenbrück, Bramsche, Alfhausen, Merzen und Osnabrück aus. Mit eigener Lkw-, Bus- und Traktor-Flotte.',
        g1=('5 Standorte', 'zwischen Artland und Osnabrück'), g2=('Alle Klassen', 'vom Mofa bis DE')))
        + klassen('klassen', 'Führerscheinklassen', 'Such dir aus, <em>was du fahren willst.</em>', 'Ein Klick auf die Klasse, und unser Lotse sagt dir, ob sie zu deinem Alter passt.', [
            ('AM · Mofa', 'Roller', 'Ab 15 Jahren, ohne Vorbesitz.', 'ab 15', 'roller'),
            ('A1 · A2 · A', 'Motorrad', 'Stufenweise oder direkt ab 24.', 'ab 16', 'moto'),
            ('B · BF17', 'Auto', 'Mit 17 begleitet starten.', 'ab 17', 'auto'),
            ('B197 · B196', 'Automatik &amp; 125er', 'Schaltkompetenz trotz Automatik-Prüfung und 125er mit Autoführerschein.', 'ab 17 / 25', 'auto'),
            ('BE · B96', 'Anhänger', 'Für Wohnwagen und Pferdeanhänger.', 'ab 17', 'anh'),
            ('C · CE', 'Lkw', 'Mit Berufskraftfahrer-Qualifikation.', 'ab 18 / 21', 'lkw'),
            ('D · DE', 'Bus', 'Personenverkehr, auch im Reisebus.', 'ab 21 / 24', 'lkw'),
            ('L · T', 'Traktor', 'Für Landwirtschaft und Lohnunternehmen.', 'ab 16', 'trak')], 'alt')
        + panels('flotte', 'Unsere Flotte', 'Vom Roller <em>bis zum Reisebus.</em>', 'Unsere Fahrzeuge tragen das Beckermann-Design. Damit lernst du genau das, was du später fährst.', [
            ('Lkw', 'p-lkw.jpg', 'Für C und CE, auch für die Berufskraftfahrer-Ausbildung.', '50% 55%'), ('Bus', 'p-bus.jpg', 'Für die Klassen D und DE.', '50% 55%'),
            ('Traktor', 'p-trak.jpg', 'Für L und T.', '50% 50%'), ('Autos', 'p-auto.jpg', 'Für B, BE und BF17.', '50% 60%'), ('Roller', 'p-roller.jpg', 'Für AM und A1.', '50% 40%')], 'dk')
        + duo('weiterbildung', 'Für Profis', 'Weiterbildung <em>für Berufskraftfahrer.</em>', 'Pflicht-Module nach dem Berufskraftfahrerqualifikationsgesetz, für Lkw und Bus. Termine findest du im Weiterbildungskalender.', [
            ('Lkw', 'Modul 1 bis 5', 'd-lkw.jpg', 'Eco-Training, Vorschriften im Güterverkehr, Sicherheitstechnik, Schaltstelle Fahrer und Ladungssicherung.', ['Eco-Training', 'Sozialvorschriften', 'Ladungssicherung'], 'Termin anfragen'),
            ('Bus', 'Modul 1 bis 5', 'd-bus.jpg', 'Eco-Training, Markt und Image, Sicherheit, Sozialvorschriften und Fahrgastsicherheit.', ['Eco-Training', 'Markt &amp; Image', 'Fahrgastsicherheit'], 'Termin anfragen')])
        + orte('orte', 'Standorte', 'Fahrschule Beckermann, <em>in deiner Nähe.</em>', 'Verwaltung in Bramsche, Unterricht unter anderem in Merzen und Bramsche dienstags und donnerstags von 18:30 bis 20:00 Uhr.', [
            ('Quakenbrück', 'Artland', ''), ('Bramsche', 'Verwaltung', 'Di &amp; Do 18:30–20:00'), ('Merzen', 'Unterricht', 'Di &amp; Do 18:30–20:00'), ('Alfhausen', 'Unterricht', ''), ('Osnabrück', 'Unterricht', '')], 'alt')
        + promo('jobs', 'p-job.jpg', 'Wir suchen dich', 'Fahrlehrer (m/w/d) <em>gesucht.</em>', 'In Voll- oder Teilzeit. Wenn du Lust hast, Menschen sicher auf die Straße zu bringen, freuen wir uns auf deine Bewerbung.', ['Voll- oder Teilzeit', 'Fünf Standorte', 'Moderne Fahrzeuge vom Auto bis zum Bus'], 'Jetzt melden')
        + contact(s, 'dk') + footer(s))

S = SITES['beckermann'] = site(
    slug='fahrschule-beckermann', firma='Fahrschule Beckermann', web='fahrschule-beckermann.de', fonts='r14bec',
    title='Fahrschule Beckermann – Quakenbrück, Bramsche, Alfhausen, Merzen & Osnabrück', desc='Fahrschule Beckermann: alle Führerscheinklassen vom Roller bis zum Bus, EU-Berufskraftfahrer-Weiterbildung. Fünf Standorte.',
    tel='05461 933955', tel_i='+495461933955', mail='info@fahrschule-beckermann.de', adresse='Osnabrücker Straße 16, 49565 Bramsche', google=None,
    cta='Jetzt anmelden', nav=[('Klassen', 'klassen'), ('Flotte', 'flotte'), ('Weiterbildung', 'weiterbildung'), ('Standorte', 'orte'), ('Jobs', 'jobs'), ('Kontakt', 'kontakt')],
    hours=[('Di &amp; Do', '18:30 – 20:00')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17 / B197', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1', 'Roller · AM / Mofa', '125er · B196', 'Lkw · C / CE', 'Bus · D / DE', 'Traktor · L / T', 'Weiterbildung BKF'],
    form_orte=['Quakenbrück', 'Bramsche', 'Alfhausen', 'Merzen', 'Osnabrück'],
    form_h3='Online anmelden', form_p='Trag dich ein, wir melden uns für den Start bei dir.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Los geht’s <em>mit deinem Führerschein.</em>', kt_p='Telefon 05461 933955 oder einfach das Formular.',
    social=[('Instagram', 'https://www.instagram.com/fahrschule_beckermann/'), ('Facebook', 'https://www.facebook.com/FahrschuleBeckermann/')], logo_txt='<img src="img/logo.png" alt="Fahrschule Beckermann" style="height:46px;width:auto;display:block">',
    vars='--hx-bg:#151515;--hxw-ar:1024/560;--bg:#f7f5f0;--ink:#151515;--mute:#5a5853;--p:#ff6600;--p-ink:#151515;--a:#ff6600;--a-ink:#151515;--dk:#151515;--s:#fff;--s2:#efeae0;--fh:"Barlow Condensed",Impact,sans-serif;--fb:"Heebo",system-ui,sans-serif;--r:6px;--r2:10px;--br:4px;--mq-bg:#ff6600;--hd-bg:#ffffff;--hd-ink:#151515;--logo-h:40px;--ft-bg:#0d0d0d',
    css='''.hx{color:#fff}.hx .sub{color:rgba(255,255,255,.75)}.hx .btn-o{color:#fff}.hx .chip{background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2);color:#fff}.hx h1,.h2{font-weight:800;text-transform:uppercase;line-height:1;letter-spacing:.005em}.hx h1{font-size:clamp(54px,6.4vw,104px);padding-top:6px}.hx h1 em{font-style:normal;color:var(--p)}.h2{font-size:clamp(40px,4.6vw,72px);padding-top:4px}
.hs h1 em{font-style:normal;color:var(--p)}.h2 em{font-style:normal;color:#cc5200}.dk .h2 em{color:var(--p)}.hs .big{font-family:var(--fh);-webkit-text-stroke:2px rgba(240,163,10,.35)}
.hd .lt-logo{color:#fff;font-family:var(--fh);font-size:26px;letter-spacing:.02em}
.hd{background:#fff!important;color:#151515!important;box-shadow:0 1px 0 rgba(0,0,0,.08)}.hd .nav a{color:#151515}''')
S['bot'] = BOT('Becky', 'deine Führerschein-Lotsin', 'der Fahrschule Beckermann', S, ['B', 'B197', 'B196', 'BE', 'B96', 'A', 'A2', 'A1', 'AM', 'Mofa', 'C', 'CE', 'D', 'L', 'T'],
    {'schnell': 'Mit fünf Standorten findest du schnell einen Unterrichtstermin, der passt.', 'ruhe': 'Wir nehmen uns Zeit für dich, von der ersten Stunde bis zur Prüfung.', 'flex': 'Unterricht an mehreren Orten, unter anderem dienstags und donnerstags abends.', 'angst': 'Sag es uns einfach. Wir starten so, dass du dich sicher fühlst.'},
    qa=[('bus|lkw|bkf|modul', 'Wir bilden Lkw und Bus aus und bieten die Weiterbildungsmodule für Berufskraftfahrer an.'), ('job|fahrlehrer|bewerb', 'Wir suchen Fahrlehrer (m/w/d) in Voll- oder Teilzeit. Schreib uns an info@fahrschule-beckermann.de.')],
    tour=[('#klassen', 'Alle Klassen auf einen Blick.'), ('#flotte', 'Unsere Flotte vom Roller bis zum Bus.'), ('#weiterbildung', 'Weiterbildung für Berufskraftfahrer.'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'logo.png': ('beckermann/img/i008.png', 0, 'alphacrop'), 'h1.jpg': ('beckermann/img/i005.jpg', 0), 'h2.jpg': ('beckermann/img/i009.jpg', 0), 'h3.jpg': ('beckermann/img/i011.jpg', 0),
    'p-lkw.jpg': ('beckermann/img/i009.jpg', 0), 'p-bus.jpg': ('beckermann/img/i011.jpg', 0), 'p-trak.jpg': ('beckermann/img/i010.jpg', 0), 'p-auto.jpg': ('beckermann/img/i005.jpg', 0), 'p-roller.jpg': ('beckermann/img/i006.jpg', 0),
    'd-lkw.jpg': ('beckermann/img/i009.jpg', 0), 'd-bus.jpg': ('beckermann/img/i011.jpg', 0), 'p-job.jpg': ('beckermann/img/i015.jpg', 0)}
S['body'] = b_beckermann

# ───────────── 5. Fahrschule Tepe, Bramsche ─────────────
def b_tepe(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 55%', 'h2.jpg': '50% 60%', 'h3.jpg': '50% 60%'}, quick=['auto', 'moto', 'roller', 'anh', 'trak'],
        ey='Fahrschule Tepe · Bramsche',
        h1='Spontan ans Meer. <em>Ganz ohne Mama und Papa.</em>',
        sub='Wir begleiten dich Schritt für Schritt vom Theorieunterricht bis zur Fahrprüfung. Entspannt, persönlich und in deinem Tempo. Und wer Respekt vor der ersten Stunde hat, startet im Fahrsimulator.',
        ubar=[('4,7 Sterne', 'bei Google'), ('Simulator', 'erst üben, dann Straße'), ('Mo &amp; Do', 'Theorie ab 19:30 Uhr')]))
        + sorgen('angst', 'Kennst du das?', 'Respekt vor der <em>ersten Fahrstunde?</em>', 'Völlig normal. Darum geht es bei uns entspannt los.', [
            ('Was, wenn ich am Anfang alles falsch mache?', 'Dann übst du zuerst im <b>Fahrsimulator</b>: ein Gefühl fürs Fahren bekommen, ohne Verkehr und ohne Druck.'),
            ('Ich lerne langsamer als andere.', 'Jeder lernt anders. <b>Du bestimmst selbst</b>, wie schnell du vorankommen möchtest.'),
            ('Theorie ist nicht so mein Ding.', 'Zwölf Themenblöcke, montags und donnerstags ab 19:30 Uhr. Dazu die <b>App</b>: Sie zeigt dir an, wann du bereit für die Prüfung bist.'),
            ('Wie läuft die Anmeldung?', '<b>Online anmelden</b>, dann vor dem Theorieunterricht vorbeikommen. Wir schauen alles gemeinsam durch, und los geht’s.')])
        + team('team', 'Unser Team', 'Gespannt, wer dir <em>das Fahren beibringt?</em>', 'Persönlicher Kontakt und individuelle Betreuung: Das ist uns wichtig.', [
            ('t-reinhold.jpg', 'Reinhold Tepe', 'Geschäftsführer'), ('t-verena.jpg', 'Verena Abing', 'geb. Tepe'), ('t-ingo.jpg', 'Ingo Hörnschemeyer', 'Team Tepe'), ('t-hubert.jpg', 'Hubert Abing', 'Team Tepe')], 'alt')
        + gallery('fahrzeuge', 'Unsere Fahrzeuge', 'Roller, Auto, Lkw? <em>Hier findest du alles.</em>', [
            ('g1.jpg', 'w2', '50% 60%'), ('g2.jpg', '', '50% 55%'), ('g3.jpg', '', '50% 60%'), ('g4.jpg', '', '50% 55%'), ('g5.jpg', '', '50% 55%'), ('g6.jpg', 'w2', '50% 55%')])
        + klassen('klassen', 'Fahrzeugklassen', 'Welche Klasse <em>brauchst du?</em>', '', [
            ('AM · A1 · A2 · A', 'Zweirad', 'Vom Roller ab 15 bis zum großen Motorrad.', 'ab 15', 'moto'),
            ('B · BE', 'Auto &amp; Anhänger', 'Der Klassiker, auch als BF17 mit Begleitung.', 'ab 17', 'auto'),
            ('L · T', 'Traktor', 'Für Hof und Landwirtschaft.', 'ab 16', 'trak'),
            ('C1 · C · CE', 'Lkw', 'Für den Beruf.', 'ab 18', 'lkw')], 'dk')
        + ablauf('ablauf', 'Anmeldung', 'Einfacher <em>geht’s nicht.</em>', '', [
            ('Online anmelden', 'Bequem von zu Hause aus.'), ('Vorbeikommen', 'Vor dem Theorieunterricht schauen wir die Anmeldung gemeinsam durch.'),
            ('Unterlagen', 'Ausweis, Passbild, Sehtest und Erste-Hilfe-Kurs für den Antrag.'), ('Losfahren', 'Theorie, Simulator, Fahrstunden, Prüfung.')])
        + reviews(s, ['Super Fahrschule! Die Theorie war leicht verständlich und alles wurde in Ruhe erklärt. Ich hatte vorher ziemlich Bammel und hatte meinen Führerschein trotzdem ruckzuck.',
                      'Auto und Anhänger bei Tepe gemacht und rundum zufrieden. Freundlich, geduldig und kompetent.',
                      'Mein Fahrlehrer war super nett und geduldig und hat alles richtig gut erklärt. Die Stunden haben Spaß gemacht.',
                      'Sehr zufrieden mit den Fahrlehrern, und auch der Preis ist im Vergleich wirklich fair.'], 'alt')
        + contact(s) + footer(s))

S = SITES['tepe'] = site(
    slug='fahrschule-tepe-bramsche', firma='Fahrschule Tepe GmbH', web='fahrschule-tepe.de', fonts='r14tep',
    title='Fahrschule Tepe – Dein Führerschein in Bramsche', desc='Fahrschule Tepe in Bramsche: Auto, Motorrad, Roller, Traktor und Lkw. Persönliche Betreuung, Fahrsimulator und Theorie montags und donnerstags.',
    tel='05461 880088', tel_i='+495461880088', mail='', adresse='Mühlenstraße 12, 49565 Bramsche', google=('4,7', 34),
    cta='Online anmelden', nav=[('Erste Stunde', 'angst'), ('Team', 'team'), ('Fahrzeuge', 'fahrzeuge'), ('Klassen', 'klassen'), ('Kontakt', 'kontakt')],
    hours=[('Theorie Mo &amp; Do', '19:30 – 21:00'), ('Anmeldung Di', '16:00 – 18:30'), ('Mo &amp; Do', 'ab 18:30 vor dem Unterricht')],
    form_lbl='Führerschein', form_opts=['Auto · B / BF17', 'Anhänger · BE', 'Motorrad · A / A2 / A1', 'Roller · AM', 'Traktor · L / T', 'Lkw · C1 / C / CE'],
    form_h3='Zur Online-Anmeldung', form_p='Trag dich ein und komm danach vor dem Theorieunterricht vorbei.', form_btn='Anmeldung abschicken',
    kt_ey='Kupplung kommen lassen', kt_h2='Und Gas <em>geben?</em>', kt_p='Komm einfach vorbei, um dich beraten zu lassen, oder melde dich online an.',
    rv_h2='Das sagen <em>unsere Fahrschüler.</em>', social=[('Instagram', 'https://www.instagram.com/fahrschule_tepe/'), ('Facebook', 'https://www.facebook.com/p/Fahrschule-Tepe-100063510102567/')],
    logo_txt='<img src="img/logo.png" alt="Fahrschule Tepe" style="height:54px;width:auto;display:block">',
    vars='--bg:#fffaf4;--ink:#1d1a17;--mute:#615a52;--p:#f07d00;--p-ink:#fff;--a:#f07d00;--a-ink:#fff;--dk:#2a1f17;--s:#fff;--s2:#fcefe0;--fh:"Fraunces",Georgia,serif;--fb:"Nunito Sans",system-ui,sans-serif;--r:22px;--r2:30px;--br:999px;--mq-bg:#f07d00;--hd-bg:rgba(255,250,244,.95);--hd-ink:#1d1a17;--ft-bg:#1d1611;--hero-ov:linear-gradient(95deg,rgba(29,20,12,.82) 0%,rgba(29,20,12,.45) 50%,rgba(29,20,12,.05) 85%)',
    css='''.hs h1{font-weight:700;line-height:1.04;font-size:clamp(46px,6vw,92px)}.hs h1 em{color:#ffb15c}.h2{font-weight:700;line-height:1.08}.h2 em{color:var(--p)}.dk .h2 em{color:#ffb15c}
.hd.lt .lt-logo{color:#fff}.hd.scr .lt-logo{color:var(--ink)}.tm figure div{border-radius:26px}.tm figure img{aspect-ratio:1/1;object-position:50% 30%}.so .it{border-radius:26px}
.hd{background:rgba(255,250,244,.97)!important;color:#1d1a17!important;box-shadow:0 1px 0 rgba(0,0,0,.06)}.hd .nav a{color:#1d1a17}''')
S['bot'] = BOT('Lotta', 'deine Fahrschul-Lotsin', 'der Fahrschule Tepe', S, ['B', 'BE', 'A', 'A2', 'A1', 'AM', 'C', 'CE', 'L', 'T'],
    {'schnell': 'Bestimme dein Tempo selbst. Mit der App siehst du, wann du bereit für die Theorieprüfung bist.', 'ruhe': 'Persönlicher Kontakt und individuelle Betreuung: Wir bringen dir das Fahren ganz entspannt bei.', 'flex': 'Theorie montags und donnerstags ab 19:30 Uhr, Anmeldung auch dienstags nachmittags.', 'angst': 'Starte einfach im Fahrsimulator: ohne Verkehr, ohne Druck.'},
    qa=[('simulator', 'Im Fahrsimulator bekommst du ein Gefühl fürs Fahren, ohne Verkehr und ohne Druck. Perfekt vor der ersten Stunde.'), ('theorie|unterricht', 'Theorie: 12 Themenblöcke, montags und donnerstags ab 19:30 Uhr. Dazu die App zum Üben.')],
    tour=[('#angst', 'Respekt vor der ersten Stunde? Hier steht, wie wir das lösen.'), ('#team', 'Das Team, das dir das Fahren beibringt.'), ('#klassen', 'Welche Klasse brauchst du?'), ('#kontakt', 'Hier meldest du dich an.')])
S['img'] = {'h1.jpg': ('tepe/img/i006.jpg', 1900), 'h2.jpg': ('tepe/img/i017.jpg', 1900), 'h3.jpg': ('tepe/img/i020.jpg', 1900),
    't-reinhold.jpg': ('tepe/img/i041.jpg', 0), 't-verena.jpg': ('tepe/img/i042.jpg', 0), 't-ingo.jpg': ('tepe/img/i040.jpg', 0), 't-hubert.jpg': ('tepe/img/i039.jpg', 0),
    'g1.jpg': ('tepe/img/i016.jpg', 1400), 'g2.jpg': ('tepe/img/i022.jpg', 0), 'g3.jpg': ('tepe/img/i013.jpg', 0), 'g4.jpg': ('tepe/img/i019.jpg', 1000), 'g5.jpg': ('tepe/img/i021.jpg', 1000), 'g6.jpg': ('tepe/img/i025.jpg', 0)}
S['body'] = b_tepe

SITES['beckermann']['img']['logo.png'] = ('/home/claude/r14raw/logos/beckermann.png', 0)

SITES['tepe']['img']['logo.png'] = ('/home/claude/r14raw/logos/tepe.png', 0)

SITES['albers']['img']['emo.jpg'] = ('/home/claude/pixa/emo_albers.jpg', 0)
