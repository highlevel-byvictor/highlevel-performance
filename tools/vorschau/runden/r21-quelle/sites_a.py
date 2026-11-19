"""Runde 21 · Zahnarztpraxen 30 km um Bersenbrück. Texte, Logos und Fotos der Praxen; wo Fotos fehlen, neutrale Pixabay-Bilder (nie als Praxis oder Person beschriftet).
Werberecht (HWG): keine Vorher-Nachher-Bilder, keine Heilversprechen, keine Rabatte."""
from common import *
SITES = {}
PX = '/home/claude/pixa20/'
R = '/home/claude/r20raw/'
OS = ('"Open Sans",system-ui,sans-serif',) * 2; NOTO = ('"Noto Sans",system-ui,sans-serif',) * 2; LATO = ('"Lato",system-ui,sans-serif',) * 2
NUN = ('"Nunito Sans",system-ui,sans-serif',) * 2; RAL = ('"Raleway",system-ui,sans-serif',) * 2; ASAP = ('"Asap",system-ui,sans-serif',) * 2
MONT = ('"Montserrat",system-ui,sans-serif', '"Source Sans 3",system-ui,sans-serif')

CATL = {'pzr': 'Kontrolle oder Zahnreinigung', 'akut': 'Ich habe Schmerzen', 'ersatz': 'Mir fehlt ein Zahn', 'aest': 'Schönere Zähne', 'kind': 'Termin für mein Kind', 'angst': 'Ich habe Angst vor dem Zahnarzt'}
USP = {'zeit': 'Sagen Sie am Telefon ruhig, dass Sie sich Zeit für ein Gespräch wünschen.', 'sanft': 'Sprechen Sie Ihre Sorge offen an. Das Team geht darauf ein.',
       'schnell': 'Am schnellsten geht es per Telefon.', 'klar': 'Fragen Sie nach, bis alles klar ist. Dafür ist das Beratungsgespräch da.'}

def anliegen(s, cats):
    b = ''.join(f'<a href="#kontakt" data-check="{k}">{CATL[k]}</a>' for k in cats)
    return f'<section class="an20"><div class="w"><p>Worum geht es bei Ihnen?</p><div>{b}</div></div></section>'

def notfall(s, txt):
    return f'<section class="nf20"><div class="w"><div><b>Zahnschmerzen?</b><span>{txt}</span></div><a class="btn" href="tel:{s["tel_i"]}">{PH}{s["tel"]}</a></div></section>'

def teamsec(id, ey, h2, paras, img, cap, tl, cls='', mw=None):
    ps = ''.join(f'<p class="lead">{p}</p>' for p in paras); t = ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in tl)
    st = f' style="max-width:{mw}px"' if mw else ''
    return f'<section class="sec tm20 {cls}" id="{id}"><div class="w"><figure data-r{st}><img src="img/{img}" alt="{E(cap)}" loading="lazy"><figcaption>{cap}</figcaption></figure><div data-r="2"><p class="ey">{ey}</p><h2 class="h2">{h2}</h2>{ps}<div class="tl">{t}</div></div></div></section>'

def gal20(id, ey, h2, imgs, cls=''):
    f = ''.join(f'<figure data-r><img src="img/{i}" alt="" loading="lazy" style="object-position:{p}"></figure>' for i, p in imgs)
    return f'<section class="sec gl20 {cls}" id="{id}"><div class="w"><div data-r>{head(ey, h2)}</div><div class="grid">{f}</div></div></section>'

def pops20(items):
    import json
    d = json.dumps([dict(img=i, ey=e, h=h, p=p, btn=b) for i, e, h, p, b in items], ensure_ascii=False).replace("'", '&#39;')
    return f"<div class=\"pop side\" id=\"pop20\" data-items='{d}'><button class=\"x\" aria-label=\"Schließen\">×</button><img src=\"\" alt=\"\"><div><small></small><b></b><p></p><a class=\"btn btn-a\" href=\"#kontakt\"></a></div></div>" + '''<script>(function(){var p=document.getElementById('pop20');if(!p)return;var L=JSON.parse(p.dataset.items),i=0,off=0,im=p.querySelector('img'),sm=p.querySelector('small'),b=p.querySelector('b'),tx=p.querySelector('p'),a=p.querySelector('a');
function show(){if(off||i>=L.length)return;var x=L[i++];im.src='img/'+x.img;sm.textContent=x.ey;b.textContent=x.h;tx.textContent=x.p;a.textContent=x.btn;p.classList.add('in');setTimeout(function(){p.classList.remove('in');setTimeout(show,26000)},13000)}
var armed=0;addEventListener('scroll',function(){if(!armed&&scrollY>innerHeight*.8){armed=1;setTimeout(show,2200)}},{passive:true});
p.querySelector('.x').onclick=function(){off=1;p.classList.remove('in')};a.onclick=function(){off=1;p.classList.remove('in');var f=document.querySelector('#kontakt select');if(f){for(var k=0;k<f.options.length;k++){if(f.options[k].text==b.textContent){f.selectedIndex=k;break}}}}})();</script>'''

CSS20 = '''.an20{background:var(--dk);color:#fff;padding:18px 0}.an20 .w{display:flex;gap:18px;align-items:center;flex-wrap:wrap}.an20 p{font:700 17px var(--fh);margin:0}.an20 div{display:flex;gap:10px;flex-wrap:wrap}
.an20 a{padding:11px 18px;border-radius:999px;border:1.5px solid rgba(255,255,255,.45);color:#fff;text-decoration:none;font:600 15.5px var(--fb);transition:background .2s,color .2s}.an20 a:hover{background:#fff;color:var(--dk)}
.nf20{background:var(--p);color:var(--p-ink);padding:26px 0}.nf20 .w{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}.nf20 b{display:block;font:800 24px var(--fh)}.nf20 span{font-size:17.5px}
.nf20 .btn{background:#fff;color:#161616;border-radius:999px!important;padding:14px 24px;font-weight:700;display:inline-flex;gap:10px;align-items:center}.nf20 .btn svg{width:18px;height:18px}
.tm20 .w{display:grid;grid-template-columns:1.05fr 1fr;gap:clamp(28px,5vw,70px);align-items:center}.tm20 figure{margin:0;justify-self:center;width:100%}.tm20 figure img{width:100%;height:auto;display:block;border-radius:18px}.tm20 figcaption{margin-top:12px;font-size:14.5px;color:var(--mute)}
.tm20 .tl{display:flex;gap:34px;flex-wrap:wrap;margin-top:26px}.tm20 .tl div{font-size:15px;color:var(--mute)}.tm20 .tl b{display:block;font:800 22px var(--fh);color:var(--ink)}
.tm20.dk{background:var(--dk);color:#fff}.tm20.dk .lead,.tm20.dk figcaption,.tm20.dk .tl div{color:rgba(255,255,255,.86)}.tm20.dk .tl b,.tm20.dk .h2{color:#fff}
.gl20 .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:34px}.gl20 figure{margin:0;aspect-ratio:4/3;overflow:hidden;border-radius:0}.gl20 figure:nth-child(4n+1){border-radius:18px}.gl20 img{width:100%;height:100%;object-fit:cover;transition:transform .8s}.gl20 figure:hover img{transform:scale(1.04)}
.vd .frame{border-radius:18px!important;overflow:hidden}.lt-logo{font:800 19px/1.15 var(--fh);color:var(--hd-ink,var(--ink));letter-spacing:.01em;display:block}.lt-logo small{display:block;font:600 12px var(--fb);letter-spacing:.14em;text-transform:uppercase;color:var(--p)}
.ft .lt-logo{color:#fff}.ft .lt-logo small{color:rgba(255,255,255,.7)}
.promo figure img{aspect-ratio:auto!important;height:auto}.pop.side img{height:auto!important;aspect-ratio:auto;max-height:230px;object-fit:cover}.chip20{display:inline-flex!important;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:10px 18px 10px 14px;box-shadow:0 8px 26px rgba(0,0,0,.10);font:600 15.5px var(--fb);margin-bottom:18px}.chip20 b{font:800 20px var(--fh)}.chip20 .st{color:#f5a500;letter-spacing:1px;font-size:17px}
.lot-b,.lot-h{color:var(--p-ink,#fff)}.lot-h button{color:inherit}
.ht20{background:var(--s2);padding-top:var(--hdh,86px)}.ht20 figure{margin:0;max-width:1500px;margin-inline:auto}.ht20 .chip20{margin-bottom:10px}.ht20 figure img{display:block;width:100%;height:auto}
.ht20 .w{display:grid;grid-template-columns:1.05fr 1fr;gap:clamp(24px,5vw,70px);align-items:start;padding-top:44px;padding-bottom:56px}.ht20 h1{font:800 clamp(34px,4.2vw,62px)/1.04 var(--fh);letter-spacing:-.02em;margin:12px 0 0}.ht20 h1 em{font-style:normal;color:var(--p)}
.ht20 .ey{color:var(--p)}.ht20 .sub{font-size:19px;color:var(--mute);margin:0}.ht20 .ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}.ht20 .ub{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:30px;border-top:1px solid rgba(0,0,0,.14)}
.ht20 .ub div{padding-top:14px;font-size:14.5px;color:var(--mute);line-height:1.35}.ht20 .ub b{display:block;font:800 21px var(--fh);color:var(--ink)}
@media(max-width:900px){.ht20{padding-top:66px}.ht20 .w{grid-template-columns:1fr;padding-top:26px;padding-bottom:40px}.ht20 h1{font-size:31px}}
@media(max-width:900px){.tm20 .w{grid-template-columns:1fr}.gl20 .grid{grid-template-columns:1fr 1fr}.an20 p{width:100%}.an20 a{font-size:14.5px;padding:10px 14px}.nf20 b{font-size:21px}}'''

def mk(k, d):
    g = d.get
    ort = d['ort']; name = d['name']; top = d['top']; fam = d['fam']; p = d['p']; dk = d['dk']; s2 = d['s2']; pi = g('pi', '#fff')
    svcs = d['svcs']; cats = d['cats']; rec = d['rec']
    def body(s):
        hero = d['hero']
        if hero == 'team':
            ub = ''.join(f'<div><b>{x}</b>{y}</div>' for x, y in d['ubar'])
            t = hd(s, False) + (f'<section class="ht20" id="top"><figure><img src="img/h1.jpg" alt="{E(d["team"]["cap"])}"></figure><div class="w"><div data-r>{chip(s)}<p class="ey">{d["ey"]}</p><h1>{d["h1"]}</h1></div>'
                 f'<div data-r="2"><p class="sub">{d["sub"]}</p><div class="ctas"><a class="btn btn-a" href="#kontakt">{s["cta"]} {AR}</a><a class="btn btn-o" href="tel:{s["tel_i"]}">{PH} {s["tel"]}</a></div><div class="ub">{ub}</div></div></div></section>')
        elif hero == 'slides':
            t = hd(s) + hero_slides(s, dict(slides=['h1.jpg', 'h2.jpg'], pos=g('hpos', {}), ey=d['ey'], h1=d['h1'], sub=d['sub'], ubar=d['ubar']))
        else:
            t = hd(s, False) + hero_split(s, dict(imgs=(['h1.jpg', 'h2.jpg'] if d['himgs'][0] != d['himgs'][1] else ['h1.jpg']), cls=('card' if g('card') else ''), pos=g('hpos', {}), side=hero, big='', ubar=d['ubar'], ey=d['ey'], h1=d['h1'], sub=d['sub']))
        b = t + anliegen(s, cats) + marquee([a for a, _ in svcs] + [f'Zahnarzt in {ort}'], 'wm')
        if g('stimmen'): b += reviews_ns(s, d['stimmen'], cls='alt', h2='Das sagen <em>unsere Patienten.</em>')
        if g('video_first'): b += d['video_first']
        b += svc('leistungen', 'Leistungen', d['sv_h2'], d['sv_lead'], svcs[:6])
        b += promo('fokus', 'pr.jpg', top['tag'], top['h2'], top['txt'], top['pts'], top['btn'], 'alt')
        if g('zwei'):
            z = d['zwei']; b += eltern('zwei', 'el.jpg', z['ey'], z['h2'], z['txt'], z['pts'], z['btn'], rev=True)
        b += ablauf('weg', 'Ihr erster Besuch', 'Anrufen, kennenlernen, <em>gut aufgehoben.</em>', 'So läuft es ab, wenn Sie neu zu uns kommen.', [
            ('Termin vereinbaren', f'Rufen Sie an unter {s["tel"]} oder schreiben Sie uns über das Formular. Sagen Sie kurz, worum es geht.'),
            ('In Ruhe ankommen', 'Bringen Sie Ihre Versichertenkarte und, wenn vorhanden, Ihr Bonusheft mit. Wir nehmen uns Zeit für Ihre Fragen.'),
            ('Untersuchung und Beratung', 'Wir schauen uns alles genau an und besprechen mit Ihnen, was sinnvoll ist. Sie entscheiden.')])
        tm = d['team']
        b += teamsec('ueber', tm['ey'], tm['h2'], tm['paras'], 'tm.jpg', tm['cap'], tm['tl'], cls='dk', mw=tm.get('mw'))
        if g('gal'): b += gal20('praxis', 'Einblicke', d.get('gal_h2', 'Ein Blick in <em>unsere Praxis.</em>'), [(f'g{i+1}.jpg', pos) for i, (_, pos) in enumerate(d['gal'])])
        if g('video'): b += d['video']
        b += notfall(s, d['notfall']) + contact(s)
        b += pops20([('pr.jpg', 'Aus unserer Praxis', top['tag'], top['pop'], 'Termin anfragen')] + [(im, 'Aus unserer Praxis', a, tx, 'Termin anfragen') for im, a, tx in d['pops']])
        return b + footer(s)
    opts = [a for a, _ in svcs] + ['Kontrolltermin', 'Schmerzen', 'Sonstiges']
    S = SITES[k] = site(
        slug=d['slug'], firma=d['firma'], web=d['web'], fonts=d['fonts'], branche='Zahnarztpraxis',
        title=f'{d["firma"]} – Ihr Zahnarzt in {ort}', desc=f'{d["firma"]} in {ort}: ' + ', '.join(a for a, _ in svcs[:5]) + '.',
        tel=d['tel'], tel_i=d['tel_i'], mail=g('mail', ''), adresse=f'{d["strasse"]}, {d["plz"]} {ort}', google=g('google'),
        cta='Termin anfragen', nav=[('Leistungen', 'leistungen'), (top['nav'], 'fokus'), ('Erster Besuch', 'weg'), ('Praxis', 'ueber'), ('Kontakt', 'kontakt')],
        hours=d['hours'], form_opts=opts, form_h3='Termin anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
        kt_ey='Kontakt', kt_h2='Wir sind <em>für Sie da.</em>', kt_p='Rufen Sie an oder schreiben Sie uns. Wir melden uns so schnell wie möglich.',
        vars=V.format(ink='#1b1d22', mute='#4d535c', p=p, pi=pi, dk=dk, s2=s2, fh=fam[0], fb=fam[1], lh=g('lh', 58), ft=dk),
        css=f'''.h2,.hz h1,.hs h1{{font-weight:800;letter-spacing:-.02em}}.h2 em,.hz h1 em{{font-style:normal;color:{g('em', p)}}}.hs h1 em{{font-style:normal;color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}.dk .h2 em{{color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}
.mq.wm span{{font-weight:700;font-size:15px}}.alt{{background:var(--s2)}}.sv .row div{{border-top:4px solid {p}}}.rd .road div h3{{color:{g('em', p)}}}.hs .ubar b{{color:#fff}}.hs .ey{{color:#fff!important}}.ft img{{background:#fff;padding:8px 12px;height:66px}}
.promo .tag{{background:{p};color:{pi}}}.el .ey{{color:{g('em', p)}}}
@media(max-width:820px){{.hz h1,.hs h1{{font-size:31px!important;hyphens:none!important;overflow-wrap:normal!important;word-break:normal!important}}}}''' + CSS20)
    card = (f'@media(min-width:901px){{.hz.card{{min-height:min(90vh,800px)}}.hz.card .hz-img{{align-self:center;min-height:0;aspect-ratio:{g("card")};margin:130px clamp(24px,4vw,64px) 60px;border-radius:18px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.18)}}.hz.card .sl img{{animation:none}}}}@media(max-width:900px){{.hz.card .hz-img{{height:auto!important;min-height:0!important;aspect-ratio:{g("card")};margin-top:72px}}}}' if g('card') else '')
    S['css2'] = card + f'.hz{{--hz-bg:{s2};--hz-ink:#1b1d22;--hz-mute:#4d535c;--hz-stroke:rgba(0,0,0,.07);--hz-cols:{g("cols", "46fr 54fr")}}}.hz h1{{font-size:clamp(34px,4.1vw,64px)}}.hz .ey{{color:{g("em", p)}}}' + g('css2', '')
    if g('logo_txt'): S['logo_txt'] = d['logo_txt']
    if g('stimmen') and not g('google'): S['voices'] = True
    nf = d['notfall']
    S['bot'] = dict(auto=(d['hero'] == 'r'), name=d['bot'], tag='Ihr Praxis-Lotse', du=False, tel=d['tel'], tel_i=d['tel_i'], notfall=nf, finBtn='Termin anfragen',
        hello=f'Guten Tag! Ich bin <b>{d["bot"]}</b>, der Lotse der {d["kurz"]}. Soll ich Ihnen helfen, schnell das Richtige zu finden?',
        hi=f'Guten Tag, ich bin {d["bot"]}. Ich stelle Ihnen drei kurze Fragen und zeige Ihnen, was in der Praxis zu Ihrem Anliegen passt.',
        cats=[[CATL[c], c] for c in cats], rec=rec, usp=USP, ex='Sprechzeiten, Leistungen oder Terminen',
        qa=[['zeit|geöffnet|sprech|offen|öffnung', 'Die Sprechzeiten: ' + ', '.join(f'{a} {b}' for a, b in d['hours']) + '.'],
            ['wo|adresse|anfahrt|park', f'Sie finden die Praxis hier: {d["strasse"]}, {d["plz"]} {ort}.'],
            ['leistung|angebot|macht ihr|bieten', 'Zum Beispiel: ' + ', '.join(a for a, _ in svcs[:6]) + '.'],
            ['angst|panik', rec.get('angst', ['', 'Sagen Sie es dem Team gleich am Telefon. Dann nimmt man sich Zeit für Sie.'])[1]],
            ['kind|sohn|tochter', rec.get('kind', ['', 'Auch Kinder sind willkommen. Am besten kurz anrufen.'])[1]]],
        tour=[['#leistungen', 'Das bietet die Praxis an.'], ['#fokus', f'Ein Schwerpunkt: {top["tag"]}.'], ['#weg', 'So läuft Ihr erster Besuch ab.'], ['#ueber', 'Hier lernen Sie die Praxis kennen.'], ['#kontakt', 'Und hier fragen Sie Ihren Termin an.']])
    im = {'h1.jpg': (d['himgs'][0], 0), 'h2.jpg': (d['himgs'][1], 0), 'pr.jpg': (top['img'], 0), 'tm.jpg': (d['team']['img'], 0)}
    if g('logo'): im['logo.png'] = d['logo']
    if g('zwei'): im['el.jpg'] = (d['zwei']['img'], 0)
    for i, (src, _) in enumerate(g('gal', [])): im[f'g{i+1}.jpg'] = (src, 0)
    for x in g('extra_img', {}).items(): im[x[0]] = x[1]
    S['img'] = im; S['body'] = body

GEN_NF = 'Rufen Sie uns in der Sprechzeit direkt an. Außerhalb der Sprechzeiten hilft der zahnärztliche Notdienst.'
def I20(k, n):
    import glob
    f = glob.glob(f'{R}{k}/img/i{n}.*'); assert f, (k, n); return f[0]

# 1 ─ Zahnarztpraxis Alfhausen
mk('alfhausen', dict(slug='zahnarztpraxis-alfhausen', firma='Zahnarztpraxis Alfhausen', kurz='Zahnarztpraxis Alfhausen', name='Dr. Hermann Meyer und Ines Gennermann', ort='Alfhausen', strasse='In den Gärten 1', plz='49594',
    tel='05464 1228', tel_i='+4954641228', mail='info@zahnarztpraxis-alfhausen.de', web='zahnarztpraxis-alfhausen.de', p='#731e35', dk='#3a0f1b', s2='#f7f1f3', fam=NOTO, fonts='r18rec', google=(4.8, 24),
    logo=(I20('alfhausen', '000'), 0), lh=54, hero='team', himgs=[I20('alfhausen', '001'), I20('alfhausen', '006')],
    ey='Zahnarztpraxis Alfhausen · seit drei Generationen', h1='Ihre Zahnärzte in Alfhausen. <em>Mit Zeit für Sie.</em>',
    sub='Ein freundliches, engagiertes Team in entspannter, familiärer Atmosphäre. Direkt im Ortskern, mit Parkplätzen vor dem Haus.',
    ubar=[('Seit 3', 'Generationen'), ('Mo–Do', '7 bis 19 Uhr'), ('Barrierefrei', 'im Ortskern')],
    sv_h2='Für Ihre großen und <em>kleinen Probleme.</em>', sv_lead='Wir beraten und behandeln Sie auf dem stets aktuellen Stand des Wissens.',
    svcs=[('Kontrolle und Vorsorge', 'Regelmäßige Kontrollen beugen Karies und Parodontitis vor. So lassen sich aufwendige Folgebehandlungen oft vermeiden.'),
          ('Professionelle Zahnreinigung', 'Wir befreien Zähne und Zahnzwischenräume gründlich von Belägen, auch dort, wo die Zahnbürste nicht hinkommt.'),
          ('Beratung', 'Wir möchten Sie umfassend und partnerschaftlich beraten und fair und qualifiziert behandeln.'),
          ('Hilfe im Notfall', 'Lockere Krone, abgebrochener Zahn, Schmerzen: Rufen Sie an, wir finden schnell einen Termin.'),
          ('Früh und spät geöffnet', 'Montags bis donnerstags von 7 bis 19 Uhr. So passt der Termin auch vor oder nach der Arbeit.'),
          ('Barrierefreier Zugang', 'Die Praxis liegt direkt im Ortskern, hat einen behindertengerechten Zugang und Parkplätze vor dem Haus.')],
    top=dict(nav='Prophylaxe', tag='Professionelle Zahnreinigung', h2='Vorbeugen ist besser <em>als bohren.</em>', img=I20('alfhausen', '011'),
             txt='Bei der täglichen Zahnpflege lassen sich vor allem die Zahnzwischenräume schwer reinigen. Bei der professionellen Zahnreinigung befreien wir Mundraum und Zähne gründlich von Belägen.',
             pts=['Beugt Karies und Parodontitis vor', 'Reinigt auch die Zahnzwischenräume', 'Mit Tipps für die Pflege zu Hause'], btn='Zahnreinigung anfragen', pop='Gründlich sauber, auch zwischen den Zähnen. Jetzt Termin anfragen.'),
    team=dict(ey='Die Praxis', h2='Seit drei Generationen <em>in Alfhausen.</em>', img=I20('alfhausen', '006'), cap='Der Empfang der Zahnarztpraxis Alfhausen',
              paras=['Unsere Praxis besteht seit drei Generationen. Seit 1993 wird sie von Dr. Hermann Meyer und Zahnärztin Ines Gennermann als Gemeinschaftspraxis geführt.',
                     'Wir legen Wert auf ein harmonisches Miteinander und nehmen uns Zeit für Sie. Den Aufenthalt bei uns möchten wir Ihnen so angenehm wie möglich machen.'],
              tl=[('1993', 'Gemeinschaftspraxis'), ('3', 'Generationen')]),
    gal=[(I20('alfhausen', '003'), '50% 50%'), (I20('alfhausen', '002'), '70% 50%'), (I20('alfhausen', '011'), '50% 30%')],
    stimmen=['Man fühlt sich gut aufgehoben, und das Team nimmt sich Zeit für die Patienten.', 'Ich habe den Zahnarzt mein halbes Leben gemieden. Hier habe ich gelernt, dass die Angst unbegründet war.', 'Sehr gute Beratung, ohne dass unnötige Leistungen angeboten wurden.'],
    hours=[('Mo–Do', '7–19 Uhr'), ('Fr', '7–13 Uhr')], cats=['pzr', 'akut', 'angst'], bot='Alfi', notfall='Außerhalb der Sprechzeiten erreichen Sie den Notdienst im Altkreis Bersenbrück unter 05468 8067777.',
    rec={'pzr': ['Professionelle Zahnreinigung', 'Kontrolle und Zahnreinigung lassen sich gut verbinden. Die Praxis hat montags bis donnerstags von 7 bis 19 Uhr geöffnet.'],
         'angst': ['Beratung', 'Sagen Sie es dem Team gleich am Telefon. In Alfhausen nimmt man sich Zeit für Sie und Ihre Sorgen.']},
    pops=[('tm.jpg', 'Früh und spät geöffnet', 'Montags bis donnerstags von 7 bis 19 Uhr. Termin vor oder nach der Arbeit.'), ('g1.jpg', 'Kontrolle und Vorsorge', 'Der letzte Kontrolltermin ist schon länger her? Wir schauen in Ruhe nach.')]))

# 2 ─ Dr. Stephanie Austermann, Bramsche
mk('austermann', dict(slug='zahnarztpraxis-austermann-bramsche', firma='Zahnarztpraxis Dr. Stephanie Austermann', kurz='Praxis Dr. Austermann', name='Dr. Stephanie Austermann', ort='Bramsche', strasse='Lutterdamm 68-70', plz='49565',
    tel='05461 2775', tel_i='+4954612775', web='dr-austermann.de', p='#5664a0', dk='#2b3252', s2='#eef0f7', fam=OS, fonts='r16ellers',
    logo=(I20('austermann', '007'), 0, 'alphacrop'), lh=62, hero='l', himgs=[I20('austermann', '130'), I20('austermann', '130')], card='4/3', google=(4.8, 17), cols='44fr 56fr',
    ey='Zahnarztpraxis Dr. Stephanie Austermann · Bramsche', h1='Zahnmedizin aus Leidenschaft. <em>Mit eigenem Labor.</em>',
    sub='„Schöne, gesunde Zähne, ein Leben lang.“ Das ist unser Leitgedanke. Wir erklären verständlich und entscheiden gemeinsam mit Ihnen.',
    ubar=[('Eigenlabor', 'seit 1996'), ('Angstpatienten', 'willkommen'), ('Parken', 'direkt am Haus')],
    sv_h2='Alles für <em>gesunde Zähne.</em>', sv_lead='Ob Karies, Zahnfleischprobleme, fehlende Zähne oder einfach ein Kontrolltermin: Wir sind gern für Sie da.',
    svcs=[('Prothetik', 'Kronen, Brücken und Prothesen. Dank Eigenlabor individuell geplant und zeitnah fertig.'),
          ('Prophylaxe', 'Professionelle Zahnreinigung und regelmäßige Vorsorge für den langfristigen Erhalt Ihrer Zähne.'),
          ('Parodontologie', 'Behandlung von Zahnfleischentzündungen, damit Ihre Zähne festen Halt behalten.'),
          ('Chirurgie', 'Zahnärztliche Eingriffe direkt in der Praxis, ruhig und sorgfältig durchgeführt.'),
          ('Kinderzahnheilkunde', 'Mit Geduld und einem freundlichen Wort, damit Kinder gern wiederkommen.'),
          ('Alterszahnheilkunde', 'Zahnmedizin, die sich an die Bedürfnisse im Alter anpasst.')],
    top=dict(nav='Eigenlabor', tag='Zahnersatz aus dem Eigenlabor', h2='Zahnärztin und Zahntechnik <em>unter einem Dach.</em>', img=I20('austermann', '144'),
             txt='Seit 1996 verfügt unsere Praxis über ein modern ausgestattetes Eigenlabor. Für Sie bedeutet das: schnelle Wege, persönliche Beratung und maßgeschneiderte Lösungen.',
             pts=['Individuelle Planung im persönlichen Gespräch', 'Zeitnahe Fertigstellung Ihres Zahnersatzes', 'Reparaturen meist innerhalb kürzester Zeit'], btn='Beratung anfragen', pop='Kronen, Brücken und Reparaturen direkt aus dem hauseigenen Labor.'),
    zwei=dict(ey='Angstpatienten', h2='Angst vor dem Zahnarzt? <em>Sagen Sie es uns.</em>', img=I20('austermann', '134'),
              txt='In ausführlichen und verständlichen Gesprächen erklären wir Ihnen alle Behandlungsmöglichkeiten transparent. Sie bestimmen das Tempo.',
              pts=['Individuelle Beratung mit Herz und Verstand', 'Jeder Schritt wird vorher erklärt', 'Ein Team, bei dem man sich gut aufgehoben fühlt'], btn='Termin anfragen'),
    team=dict(ey='Das Team', h2='Menschen, die ihren <em>Beruf lieben.</em>', img=I20('austermann', '133'), cap='Am Empfang der Praxis am Lutterdamm in Bramsche', mw=620,
              paras=['An jedem Tag setzen wir uns mit viel Engagement für die Gesundheit und den Erhalt Ihrer Zähne ein.',
                     'Sie finden uns am Lutterdamm 68-70, direkt über dem EDEKA-Getränkemarkt. Gut erreichbar zu Fuß, mit dem Bus oder dem Auto.'],
              tl=[('1996', 'Eigenlabor'), ('Bramsche', 'Lutterdamm')]),
    gal=[(I20('austermann', '134'), '50% 30%'), (I20('austermann', '138'), '50% 30%'), (I20('austermann', '145'), '50% 25%'), (I20('austermann', '137'), '50% 50%'), (I20('austermann', '147'), '50% 50%'), (I20('austermann', '149'), '50% 50%')],
    stimmen=['Als Schmerzpatientin zum ersten Mal da: Alles wurde verständlich erklärt, ich habe mich sofort wohlgefühlt.', 'Sie geht sehr einfühlsam mit Angstpatienten um und erklärt jeden Schritt.', 'Gut organisierte Praxis mit kurzen Wartezeiten.'],
    hours=[('Mo, Di, Do', '8–13 · 15–18 Uhr'), ('Mi, Fr', '8–13 Uhr')], cats=['pzr', 'akut', 'ersatz', 'kind', 'angst'], bot='Lumi', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe', 'Regelmäßige Vorsorge und professionelle Zahnreinigung, damit Ihre Zähne lange gesund bleiben.'],
         'ersatz': ['Prothetik', 'Kronen, Brücken und Prothesen entstehen im hauseigenen Labor. Zahnärztin und Zahntechnik stimmen sich direkt ab.'],
         'kind': ['Kinderzahnheilkunde', 'Kinder werden mit Geduld behandelt, damit der Zahnarztbesuch ein gutes Erlebnis bleibt.'],
         'angst': ['Beratung für Angstpatienten', 'Angstpatienten sind ausdrücklich willkommen. Alles wird vorher in Ruhe erklärt.']},
    pops=[('el.jpg', 'Angstpatienten', 'Angst vor dem Zahnarzt? Bei uns wird alles vorher in Ruhe erklärt.'), ('h1.jpg', 'Prophylaxe', 'Vorsorge ist besser als Nachsorge. Jetzt Zahnreinigung anfragen.')]))

# 3 ─ Zahnarztpraxis Am Markt, Badbergen
mk('badbergen', dict(slug='zahnarztpraxis-am-markt-badbergen', firma='Zahnarztpraxis Am Markt · Sigrid E. Meyer', kurz='Zahnarztpraxis Am Markt', name='Sigrid E. Meyer', ort='Badbergen', strasse='Am Markt 1', plz='49635',
    tel='05433 6000', tel_i='+4954336000', web='zahnarzt-badbergen.de', p='#b5152b', dk='#33292b', s2='#f7f2f3', fam=LATO, fonts='r10vagts',
    logo=(I20('badbergen', '042'), 0), lh=58, hero='r', himgs=[I20('badbergen', '045'), I20('badbergen', '045')], cols='54fr 46fr', card='4/3',
    ey='Zahnarztpraxis Am Markt · Badbergen', h1='Gesunde Zähne. <em>Mitten in Badbergen.</em>',
    sub='Uns ist daran gelegen, Sie und Ihre Zähne gesund zu erhalten. Wir empfangen Sie in einer freundlichen, menschlichen Atmosphäre.',
    ubar=[('Seit 2009', 'Am Markt 1'), ('Für Kinder', 'und Erwachsene'), ('Fortbildung', 'laufend')],
    sv_h2='Vorbeugen, erhalten, <em>ersetzen.</em>', sv_lead='Wir beraten Sie fachlich und behandeln vorbeugend und therapierend, medizinisch und technisch auf dem neuesten Stand.',
    svcs=[('Professionelle Zahnreinigung', 'Umfangreiche, individuelle Zahnreinigung, Politur und Fluoridierung, dazu Tipps für die tägliche Pflege.'),
          ('Parodontitisbehandlung', 'Zahnfleischbluten oder gerötetes Zahnfleisch? Wir kümmern uns um den Halt Ihrer Zähne.'),
          ('Füllungen', 'Wir informieren Sie genau über die Möglichkeiten, von der direkten Füllung bis zum Keramikinlay.'),
          ('Zahnersatz', 'Festsitzend oder herausnehmbar: Kronen, Brücken und Prothesen, passend zu Ihrer Situation.'),
          ('Wurzelbehandlung', 'Die Möglichkeit, einen Zahn zu erhalten, wenn der Zahnnerv geschädigt ist.'),
          ('Implantate', 'Wir stehen Ihnen in Fragen der Implantatversorgung zur Seite und besprechen auch die Kosten offen.'),
          ('Schienentherapie', 'Bei nächtlichem Zähneknirschen und Verspannungen untersuchen wir Ihr Kiefergelenk.')],
    top=dict(nav='Prophylaxe', tag='Professionelle Zahnreinigung', h2='Sauber, poliert, <em>gut geschützt.</em>', img=I20('badbergen', '021'),
             txt='Bei der Individual-Prophylaxe reinigen, polieren und fluoridieren wir Ihre Zähne gründlich. Wir zeigen, wie Zahnkrankheiten entstehen und welche Hilfsmittel bei der täglichen Pflege helfen.',
             pts=['Für Kinder und Erwachsene', 'Mit Anleitung für die Pflege zu Hause', 'In freundlicher, ruhiger Atmosphäre'], btn='Zahnreinigung anfragen', pop='Gründliche Reinigung, Politur und Fluoridierung. Für Groß und Klein.'),
    team=dict(ey='Ihre Zahnärztin', h2='Sigrid E. Meyer, <em>seit 2009 Am Markt.</em>', img=I20('badbergen', '015'), cap='Ein Behandlungszimmer der Praxis Am Markt', mw=600,
              paras=['Studium der Zahnmedizin in Würzburg, Assistenzzeit in Dortmund, danach Tätigkeit in einer Gemeinschaftspraxis in Damme. Seit 2009 niedergelassen in der Zahnarztpraxis Am Markt 1.',
                     'Durch ständige Fortbildungen halten wir uns medizinisch und technisch auf dem neuesten Stand.'],
              tl=[('2009', 'Niederlassung'), ('Badbergen', 'Am Markt 1')]),
    gal=[(I20('badbergen', '009'), '50% 50%'), (I20('badbergen', '017'), '50% 50%'), (I20('badbergen', '013'), '70% 30%')],
    stimmen=['Sehr freundlich, auch die Mitarbeiterinnen. Es hat nichts weh getan.', 'Immer nett, freundlich und professionell.', 'Viele Parkplätze direkt vor der Praxis.'],
    hours=[('Mo, Di, Do', '8–12 · 14–18 Uhr'), ('Mi, Fr', '8–12 Uhr')], cats=['pzr', 'akut', 'ersatz', 'kind', 'angst'], bot='Mia', notfall=GEN_NF,
    rec={'pzr': ['Professionelle Zahnreinigung', 'Reinigung, Politur und Fluoridierung, dazu Tipps für die tägliche Pflege.'],
         'ersatz': ['Zahnersatz', 'Ob Krone, Brücke, Prothese oder Implantat: Die Praxis bespricht mit Ihnen die Möglichkeiten und die Kosten.'],
         'kind': ['Professionelle Zahnreinigung', 'Auch die Kleinen sind willkommen. Im Wartezimmer gibt es eine Spielecke.'],
         'angst': ['Kontrolltermin', 'Sagen Sie es gleich am Telefon. Die Praxis empfängt Sie in ruhiger, menschlicher Atmosphäre.']},
    pops=[('tm.jpg', 'Zahnersatz', 'Krone, Brücke oder Implantat? Wir beraten Sie und besprechen die Kosten offen.'), ('h1.jpg', 'Schienentherapie', 'Zähneknirschen und Verspannungen? Wir untersuchen Ihr Kiefergelenk.')]))

# 4 ─ Zahnarztpraxis Galina Spasova, Rieste
mk('rieste', dict(slug='zahnarztpraxis-spasova-rieste', firma='Zahnarztpraxis Galina Spasova', kurz='Zahnarztpraxis Spasova', name='Galina Spasova', ort='Rieste', strasse='Malgartener Str. 5', plz='49597',
    tel='05464 5275', tel_i='+4954645275', mail='praxis.spasova@gmx.de', web='zahnarzt-rieste.de', p='#19778a', dk='#0e4450', s2='#e8f1f3', fam=NUN, fonts='r16galerie',
    logo_txt='Zahnarztpraxis<small>Galina Spasova · Rieste</small>', hero='l', himgs=[I20('rieste', '009'), I20('rieste', '009')], cols='44fr 56fr', card='192/111',
    ey='Zahnarztpraxis Galina Spasova · Rieste', h1='Gesunde Zähne für ein <em>gesundes Lachen.</em>',
    sub='Ihr Lächeln ist uns wichtig. Wir sind erst zufrieden, wenn Sie es sind. Moderne Technik, regelmäßige Fortbildungen und ein Team, das sich kümmert.',
    ubar=[('Digitales', 'Röntgen'), ('Für Kinder', 'und Erwachsene'), ('Rieste', 'Malgartener Str. 5')],
    sv_h2='Das Beste für <em>Ihre Zähne.</em>', sv_lead='Nichts ist schöner als ein gesundes Lächeln. Darum setzt unser Team alles daran, Sie dauerhaft gesund zu halten.',
    svcs=[('Prophylaxe', 'Professionelle Zahnreinigung mit Airflow. Maßgeschneiderte Vorsorge für Kinder und Erwachsene.'),
          ('Zahnfüllungen und Inlays', 'Ein Loch im Zahn heilt nicht von selbst. Wir stellen den Zahn wieder her, bevor mehr verloren geht.'),
          ('Zahnersatz', 'Kronen, Brücken und Veneers aus Vollkeramik, individuell gefertigt.'),
          ('Parodontose', 'Für gesunde Zähne ist gesundes Zahnfleisch wichtig. Wir setzen rechtzeitig mit der Therapie ein.'),
          ('Wurzelkanalbehandlung', 'Aufwendig, aber es lohnt sich: So bleibt der natürliche Zahn erhalten.'),
          ('Knirscherschienen', 'Nachts mit den Zähnen knirschen? Eine Schiene schützt Zähne und Kiefergelenk.'),
          ('Bleaching', 'Auf Wunsch hellen wir Ihre Zähne auf.')],
    top=dict(nav='Prophylaxe', tag='Prophylaxe', h2='Vorsorge für <em>Zähne und Zahnfleisch.</em>', img=I20('rieste', '016'),
             txt='Mit unseren Prophylaxe-Maßnahmen sorgen wir für den dauerhaften Erhalt von Zahnfleisch, Zähnen, Mundschleimhaut und Implantaten. Für Kinder und Erwachsene entwickeln wir passende Konzepte.',
             pts=['Professionelle Zahnreinigung', 'Airflow (Pulverstrahlgerät)', 'Konzepte für Kinder und Erwachsene'], btn='Prophylaxe anfragen', pop='Professionelle Zahnreinigung mit Airflow. Für Kinder und Erwachsene.'),
    team=dict(ey='Das Praxisteam', h2='Ein Team, das sich <em>für Sie Zeit nimmt.</em>', img=I20('rieste', '025'), cap='Aus der Praxis in Rieste', mw=640,
              paras=['Am freundlich gestalteten Empfang vereinbaren Sie Ihre Termine und besprechen alles Wichtige rund um Behandlung und Abrechnung.',
                     'Unsere Behandlungszimmer sind modern und bequem eingerichtet. Im Wartezimmer liegen Kinderbücher für eine entspannte Wartezeit bereit.'],
              tl=[('Rieste', 'Malgartener Str. 5'), ('Digital', 'Röntgen')]),
    gal=[(I20('rieste', '015'), '50% 50%'), (I20('rieste', '030'), '50% 50%'), (I20('rieste', '041'), '50% 50%')],
    stimmen=['Das Team ist sehr freundlich, alles wird genau erklärt.', 'Ich bin dankbar, dass wir in Rieste eine so gute Zahnärztin haben.', 'Professionell und kompetent, sehr angenehme Atmosphäre.'],
    hours=[('Termine', 'nach Vereinbarung'), ('Telefon', '05464 5275')], cats=['pzr', 'akut', 'ersatz', 'aest', 'kind', 'angst'], bot='Rio', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe', 'Professionelle Zahnreinigung mit Airflow, abgestimmt auf Sie.'], 'ersatz': ['Zahnersatz', 'Kronen, Brücken oder Veneers aus Vollkeramik. Die Praxis berät Sie zu den Möglichkeiten.'],
         'aest': ['Bleaching', 'Die Praxis bietet Bleaching und Veneers an. Was zu Ihren Zähnen passt, klärt die Beratung.'], 'kind': ['Prophylaxe', 'Für Kinder gibt es eigene Prophylaxe-Konzepte und Kinderbücher im Wartezimmer.'],
         'angst': ['Kontrolltermin', 'Sagen Sie es gleich am Telefon. Sollte Ihnen bei einer Behandlung unwohl sein, ist das Team für Sie da.']},
    pops=[('h1.jpg', 'Knirscherschienen', 'Morgens wie gerädert? Eine Schiene schützt Zähne und Kiefergelenk.'), ('tm.jpg', 'Zahnersatz', 'Kronen und Brücken aus Vollkeramik, individuell für Sie gefertigt.')]))

# 5 ─ Zahnarzt Thomas Kiefert, Neuenkirchen-Vörden
mk('kiefert', dict(slug='zahnarzt-kiefert-neuenkirchen-voerden', firma='Zahnarztpraxis Thomas Kiefert', kurz='Zahnarztpraxis Kiefert', name='Thomas Kiefert', ort='Neuenkirchen-Vörden', strasse='Lindenstr. 1', plz='49434',
    tel='05495 994899', tel_i='+495495994899', mail='kontakt@zahnarzt-voerden.de', web='zahnarzt-kiefert.de', p='#3e8f08', em='#2f7305', dk='#012b55', s2='#eef6e8', fam=RAL, fonts='r18ant',
    logo_txt='Thomas Kiefert<small>Zahnarzt · Vörden</small>', hero='r', himgs=[I20('kiefert', '017'), I20('kiefert', '017')], cols='44fr 56fr', card='1920/1301',
    ey='Thomas Kiefert · Zahnarzt in Neuenkirchen-Vörden', h1='Ihre Zahnarztpraxis in Vörden. <em>Seit über 25 Jahren.</em>',
    sub='Gemeinsam mit unseren Kooperationspartnern begleiten wir Sie auf dem Weg zu Ihrer persönlichen Zahngesundheit. Vom ersten Milchzahn bis zum Implantat.',
    ubar=[('Seit 1999', 'in Vörden'), ('Implantate', 'seit über 20 Jahren'), ('Für Kinder', 'ab dem ersten Zahn')],
    sv_h2='Unsere Leistungen <em>im Überblick.</em>', sv_lead='Fortbildungen sind ein großer Bestandteil unserer Praxis. Damit Sie das bestmögliche Ergebnis bekommen.',
    svcs=[('Implantologie', 'Einer der Schwerpunkte unserer Praxis. Gut gearbeitete Implantate geben Sicherheit beim Essen, Sprechen und Lachen.'),
          ('Prophylaxe', 'Ihre Zahngesundheit liegt uns am Herzen. Unser Anliegen ist die Gesunderhaltung von Zähnen und Zahnfleisch.'),
          ('Prothetik', 'Zahnersatz, der passt und zu Ihnen passt, von der Krone bis zur Prothese.'),
          ('Wurzelbehandlung', 'Endodontie: damit ein erkrankter Zahn erhalten bleiben kann.'),
          ('Kinderzahnheilkunde', 'Kinder brauchen eine besondere Betreuung. Unser Ziel: Die Kleinen kommen gern und gehen gut gelaunt.'),
          ('Beratung', 'Wir nehmen uns Zeit, erklären die Möglichkeiten und entscheiden gemeinsam mit Ihnen.')],
    top=dict(nav='Implantate', tag='Implantologie', h2='Fest zubeißen. <em>Frei lachen.</em>', img=I20('kiefert', '011'),
             txt='Gut gearbeitete Implantate sind von echten Zähnen kaum zu unterscheiden. Thomas Kiefert setzt Implantate seit über 20 Jahren und hat sich dafür schon 2000 strukturiert fortgebildet.',
             pts=['Schwerpunkt der Praxis', 'Erfahrung seit über 20 Jahren', 'Ausführliche Beratung vorab'], btn='Implantat-Beratung anfragen', pop='Schwerpunkt der Praxis, Erfahrung seit über 20 Jahren. Jetzt Beratung anfragen.'),
    zwei=dict(ey='Kinderzahnheilkunde', h2='Damit Kinder <em>gern zum Zahnarzt gehen.</em>', img=I20('kiefert', '034'),
              txt='Das Abbauen von Ängsten und das Schaffen von Vertrauen stehen bei uns im Vordergrund. Die Vorsorge sollte schon ab dem ersten Zahn beginnen.',
              pts=['Vorsorge ab dem ersten Zahn', 'Fissurenversiegelung gegen Karies', 'Beratung für Eltern schon in der Schwangerschaft'], btn='Kindertermin anfragen'),
    team=dict(ey='Die Praxis', h2='Über 25 Jahre <em>für Vörden.</em>', img=I20('kiefert', '002'), cap='Das Team der Zahnarztpraxis Kiefert',
              paras=['„Vor nunmehr über 25 Jahren eröffnete ich im Ortsteil Vörden die Zahnarztpraxis Kiefert. Ohne Sie, mein Team und all die anderen Helferinnen und Helfer wären diese zweieinhalb Jahrzehnte nicht möglich gewesen.“',
                     'Schwerpunkte: Curricula in Prothetik, Implantologie, Endodontologie und Parodontologie.'],
              tl=[('1999', 'Niederlassung'), ('4', 'Curricula')]),
    stimmen=['Sehr freundlicher, kompetenter und einfühlsamer Zahnarzt. Auch für Kinder zu empfehlen.', 'Seit über 25 Jahren Patient: zuverlässig und immer aufmerksam.', 'Ob Behandlung oder Prophylaxe: Das ganze Team ist sehr freundlich.'],
    hours=[('Mo', '8–13 · 14–18 Uhr'), ('Di', '9–13 · 14–18 Uhr'), ('Mi–Fr', 'ab 8 Uhr'), ('Nachmittags', 'nach Vereinbarung')], cats=['pzr', 'akut', 'ersatz', 'kind', 'angst'], bot='Kiefi', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe', 'Die Gesunderhaltung von Zähnen und Zahnfleisch ist ein großes Anliegen der Praxis.'], 'ersatz': ['Implantologie', 'Implantate sind ein Schwerpunkt der Praxis, mit über 20 Jahren Erfahrung. Auch klassischer Zahnersatz ist möglich.'],
         'kind': ['Kinderzahnheilkunde', 'Kinder werden behutsam an den Zahnarztbesuch herangeführt, am besten ab dem ersten Zahn.'], 'angst': ['Beratung', 'Sagen Sie es gleich am Telefon. Vertrauen aufbauen steht in der Praxis im Vordergrund.']},
    pops=[('el.jpg', 'Kinderzahnheilkunde', 'Vorsorge ab dem ersten Zahn. Damit Kinder gern wiederkommen.'), ('h1.jpg', 'Prophylaxe', 'Ihre Zahngesundheit liegt uns am Herzen. Jetzt Termin anfragen.')]))

# 6 ─ Dr. Michael Coenen, Ankum
mk('coenen', dict(slug='zahnarzt-dr-coenen-ankum', firma='Zahnarztpraxis Dr. Michael Coenen', kurz='Praxis Dr. Coenen', name='Dr. Michael Coenen', ort='Ankum', strasse='Aslager Straße 6', plz='49577',
    tel='05462 71717', tel_i='+49546271717', mail='info@zahnarzt-in-ankum.de', web='zahnarzt-in-ankum.de', p='#197f74', dk='#0f4a44', s2='#e6f3f1', fam=ASAP, fonts='r16ikum', google=(4.8, 13),
    logo=(I20('coenen', '000'), 0, 'trim'), lh=70, hero='team', himgs=[I20('coenen', '001'), I20('coenen', '004')],
    ey='Zahnarzt Dr. Michael Coenen · Ankum', h1='Ihre Zähne erhalten <em>statt ersetzen.</em>',
    sub='Zu Füßen des Artländer Doms versorgen wir Patienten von jung bis alt. Sorgfältige Langzeitbehandlung statt „Minuten-Zahnmedizin“.',
    ubar=[('Angstfrei', 'und schmerzarm'), ('Geringe', 'Wartezeiten'), ('Implantate', 'aus einer Hand')],
    sv_h2='Worauf wir <em>besonderen Wert legen.</em>', sv_lead='Uns sind das Vertrauen unserer Patienten und das Miteinander sehr wichtig.',
    svcs=[('Beratung', 'Zahnheilkunde ist Vertrauenssache. Vor Behandlungsbeginn zeigen wir Ihnen verschiedene Behandlungswege auf.'),
          ('Erhaltung', 'Der Erhalt Ihrer eigenen Zähne liegt uns am Herzen, mit Maßnahmen und Therapien mit Augenmaß.'),
          ('Prophylaxe', 'Vorsorge hat bei uns einen höheren Stellenwert als Bohren, Stopfen, Reparieren oder Ziehen.'),
          ('Implantologie', 'Ihr fester Biss: Implantate ohne lange Wege aus einer Hand.'),
          ('Ganzheitlichkeit', 'Nebenwirkungsarme, verträgliche Füllungsmaterialien und Zahnersatz, auf Wunsch kinesiologisch getestet.'),
          ('Biss-Check', 'Kopf- und Nackenschmerzen können von einem „falschen“ Biss herrühren. Wir überprüfen ihn.')],
    top=dict(nav='Prophylaxe', tag='Prophylaxe', h2='Am liebsten sehen wir Sie <em>nur zur Vorsorge.</em>', img=PX + '2127681.jpg',
             txt='Wir streben an, dass Sie lediglich zur Untersuchung und zur Professionellen Zahnreinigung zu uns kommen. Wir wollen Zahnschäden vorbeugen. Treten sie trotzdem auf, behandeln wir früh, um viel eigene Zahnsubstanz zu erhalten.',
             pts=['Vorsorge vor Bohren und Ziehen', 'Tipps, um vermeidbare Arztbesuche zu sparen', 'Termine möglichst ohne Wartezeit'], btn='Prophylaxe-Termin anfragen', pop='Vorsorge statt Bohren. Termine möglichst ohne Wartezeit.'),
    zwei=dict(ey='Implantologie', h2='Ihr fester Biss. <em>Aus einer Hand.</em>', img=I20('coenen', '009'),
              txt='Wir überlegen mit Ihnen gemeinsam, ob Implantate eine sinnvolle Alternative zu herkömmlichem Zahnersatz sind und ob Ihr Kiefer eine Implantation zulässt.',
              pts=['Beratung, Implantation und Zahnersatz in einer Praxis', 'Keine langen Wege', 'Ehrliche Einschätzung vorab'], btn='Implantat-Beratung anfragen'),
    team=dict(ey='Das Team', h2='Ihre Zeit ist uns wichtig. <em>Sie sind uns wichtig.</em>', img=I20('coenen', '004'), cap='Ein Behandlungszimmer der Praxis in Ankum',
              paras=['Wir vereinbaren Termine mit Ihnen möglichst ohne Wartezeit. Bei Schmerzen, Beschwerden oder Reparaturen am Zahnersatz bemühen wir uns, noch am selben Tag zu helfen.',
                     'Unsere Praxis liegt in Ankum, im Nordkreis Osnabrücks, zu Füßen des Artländer Doms.'],
              tl=[('Ankum', 'Aslager Straße 6'), ('Hilfe', 'möglichst am selben Tag')]),
    stimmen=['Sehr freundlich und gründlich. Er nimmt sich Zeit und beantwortet alle Fragen.', 'Seit ich bei Dr. Coenen bin, gehe ich tatsächlich gern zum Zahnarzt.', 'Kurze Wartezeiten und eine sehr sorgfältige Zahnreinigung.'],
    hours=[('Termine', 'nach Vereinbarung'), ('Telefon', '05462 71717')], cats=['pzr', 'akut', 'ersatz', 'angst'], bot='Coco', notfall='Wir bemühen uns, Ihnen bei Schmerzen noch am selben Tag zu helfen. Außerhalb der Sprechzeiten hilft der zahnärztliche Notdienst.',
    rec={'pzr': ['Prophylaxe', 'Vorsorge hat in der Praxis einen höheren Stellenwert als Bohren oder Ziehen.'], 'ersatz': ['Implantologie', 'Die Praxis prüft mit Ihnen, ob ein Implantat sinnvoll ist. Beratung, Implantation und Zahnersatz kommen aus einer Hand.'],
         'angst': ['Beratung', 'Die Praxis legt besonderen Wert auf eine angstfreie und schmerzarme Behandlung. Sagen Sie es gleich am Telefon.']},
    pops=[('el.jpg', 'Implantologie', 'Implantate ohne lange Wege: Beratung, Implantation und Zahnersatz aus einer Hand.'), ('h1.jpg', 'Biss-Check', 'Kopf- oder Nackenschmerzen? Wir überprüfen Ihren Biss.')]))

# 7 ─ Carsten Tischler, Damme
mk('tischler', dict(slug='zahnarzt-tischler-damme', firma='Zahnarztpraxis Carsten Tischler', kurz='Zahnarztpraxis Tischler', name='Carsten Tischler', ort='Damme', strasse='Mühlenstraße 32', plz='49401',
    tel='05491 5290', tel_i='+4954915290', mail='zahnarzt-tischler-damme@ewe.net', web='zahnarzt-in-damme.de', p='#95cc60', pi='#14280a', em='#4c8a1c', dk='#26301f', s2='#f1f7ea', fam=OS, fonts='r16ellers', google=(4.9, 34),
    logo=(I20('tischler', '000'), 0), lh=64, hero='l', himgs=[I20('tischler', '003'), I20('tischler', '003')], cols='50fr 50fr', card='674/281',
    ey='Zahnarzt Carsten Tischler · Damme', h1='Ihr Zahnarzt in Damme. <em>Auch für Angstpatienten.</em>',
    sub='Sie stehen bei uns im Mittelpunkt und können sich auf eine umfangreiche und verständliche Beratung verlassen. Von der Prophylaxe bis zum Zahnimplantat.',
    ubar=[('Seit 2003', 'Carsten Tischler'), ('Angstpatienten', 'willkommen'), ('Implantate', 'und Zahnersatz')],
    sv_h2='Ein breites <em>Leistungsspektrum.</em>', sv_lead='Bei jeder Behandlung betrachten wir die Zahnsituation jedes Patienten individuell.',
    svcs=[('Behandlung von Angstpatienten', 'Schlechte Erfahrungen gemacht? Wir helfen Ihnen, die Zahnarztangst Schritt für Schritt abzubauen.'),
          ('Prophylaxe und Zahnreinigung', 'Damit Ihre Zähne bis ins hohe Alter gesund bleiben.'),
          ('Zahnimplantate', 'Implantatgetragener Zahnersatz direkt in unserer Praxis in Damme.'),
          ('Kinderzahnheilkunde', 'Freundlich und geduldig, damit Kinder Vertrauen fassen.'),
          ('Wurzelbehandlung', 'Schonende maschinelle Wurzelkanalbehandlung, um den Zahn zu erhalten.'),
          ('Parodontitis', 'Wir behandeln Entzündungen des Zahnhalteapparats, bevor Zähne ihren Halt verlieren.'),
          ('Seniorenzahnmedizin', 'Zahnheilkunde 50+: abgestimmt auf die Bedürfnisse im Alter.'), ('Bleaching', 'Für ein selbstbewusstes, schönes Lächeln.')],
    top=dict(nav='Angstpatienten', tag='Behandlung von Angstpatienten', h2='Angst vor dem Zahnarzt? <em>Sie sind nicht allein.</em>', img=I20('tischler', '025'),
             txt='Viele Patienten leiden unter Zahnarztangst, weil sie schlechte oder schmerzhafte Erfahrungen gemacht haben. Uns liegt Ihr Wohl am Herzen. Deshalb haben wir es uns zur Aufgabe gemacht, Angstpatienten bei der Behandlung zu begleiten.',
             pts=['Verständliche Beratung vor jedem Schritt', 'Ein Team, das sich Zeit nimmt', 'Sie bestimmen das Tempo'], btn='Behutsamen Termin anfragen', pop='Schlechte Erfahrungen gemacht? Bei uns bestimmen Sie das Tempo.'),
    team=dict(ey='Die Praxis', h2='Seit den 1980ern <em>in der Mühlenstraße.</em>', img=PX + '2530983.jpg', cap='Symbolbild', mw=600,
              paras=['Unsere Praxis in der Mühlenstraße 32, gegenüber dem Postbörsen-Markt, gibt es schon seit den 1980er Jahren. Seit 2003 wird sie von Zahnarzt Carsten Tischler geführt.',
                     'Unser kompetentes und motiviertes Team nimmt sich Zeit für Ihre Anliegen und steht Ihnen mit Rat und Tat zur Seite.'],
              tl=[('2003', 'Carsten Tischler'), ('Damme', 'Mühlenstraße 32')]),
    gal=[(I20('tischler', '010'), '50% 50%'), (I20('tischler', '023'), '50% 50%'), (I20('tischler', '022'), '50% 50%')],
    stimmen=['Ich bin ein echter Angsthase, aber bei Herrn Tischler und seinem Team fühle ich mich wohl.', 'Im Notdienst sofort versorgt und jetzt schmerzfrei. Das ganze Team war sehr freundlich.', 'Er nimmt sich Zeit für Fragen und erklärt alles verständlich.'],
    hours=[('Mo, Di', '8:30–13 · 14–17:30 Uhr'), ('Mi', '8–12 Uhr'), ('Do', '8:30–13 · 14–18:30 Uhr'), ('Fr', '8:30–12 Uhr (laut Google)')], cats=['pzr', 'akut', 'ersatz', 'aest', 'kind', 'angst'], bot='Tilo', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe und Zahnreinigung', 'Regelmäßige Prophylaxe, damit Ihre Zähne bis ins hohe Alter gesund bleiben.'], 'ersatz': ['Zahnimplantate', 'Die Praxis bietet implantatgetragenen Zahnersatz an und berät Sie zu den Möglichkeiten.'],
         'aest': ['Bleaching', 'Die Praxis bietet Bleaching an. Ob es für Ihre Zähne passt, klärt die Beratung.'], 'kind': ['Kinderzahnheilkunde', 'Kinder werden freundlich und geduldig behandelt.'],
         'angst': ['Behandlung von Angstpatienten', 'Das ist ein Schwerpunkt der Praxis. Sagen Sie es gleich am Telefon, dann plant das Team mehr Zeit ein.']},
    pops=[('h1.jpg', 'Zahnimplantate', 'Implantatgetragener Zahnersatz direkt in Damme. Jetzt Beratung anfragen.'), ('tm.jpg', 'Prophylaxe und Zahnreinigung', 'Gesunde Zähne bis ins hohe Alter. Jetzt Termin anfragen.')]))

# 8 ─ Dr. Constanze Lefert & Jana Kohl, Dinklage
mk('lefert', dict(slug='zahnarztpraxis-lefert-kohl-dinklage', firma='Zahnarztpraxis Dr. Constanze Lefert & Jana Kohl', kurz='Praxis Lefert & Kohl', name='Dr. Constanze Lefert und Jana Kohl', ort='Dinklage', strasse='Bahnhofstraße 9', plz='49413',
    tel='04443 2677', tel_i='+4944432677', mail='info@zahnarztpraxis-lefert-kohl.de', web='zahnarztpraxis-lefert-kohl.de', p='#0089ab', dk='#0b4a5c', s2='#e8f5f9', fam=ASAP, fonts='r16ikum',
    logo=(I20('lefert', '000'), 0), lh=72, hero='r', himgs=[I20('lefert', '006'), I20('lefert', '006')], cols='52fr 48fr', card='60/77', google=(4.6, 21),
    ey='Dr. Constanze Lefert & Jana Kohl · Dinklage', h1='Ihr Familienzahnarzt <em>im Herzen Dinklages.</em>',
    sub='Das gesamte Spektrum der modernen Zahnheilkunde für Jung und Alt. Unsere Praxisphilosophie: Wir beraten, der Patient entscheidet.',
    ubar=[('Für Jung', 'und Alt'), ('Laser', 'fest im Konzept'), ('Schmerzen?', 'schneller Termin')],
    sv_h2='Unsere Leistungen <em>für Ihre Zähne.</em>', sv_lead='Als Ihr Familienzahnarzt sind wir für die ganze Familie da.',
    svcs=[('Professionelle Zahnreinigung', 'Zweimal jährlich zum „Zahn-TÜV“: Unsere qualifizierten Mitarbeiterinnen erwarten Sie zur Zahnprophylaxe.'),
          ('Laser', 'Bei schonenden chirurgischen Eingriffen, in der Wurzelbehandlung oder zur Parodontitistherapie.'),
          ('Junge Kieferorthopädie', 'Wir informieren Eltern frühzeitig über Zahnfehlstellungen bei ihren Kindern und beraten dazu.'),
          ('Implantate', 'Wir informieren Sie umfassend. Den implantatgetragenen Zahnersatz fertigen wir mit unserem Zahntechnikerteam.'),
          ('Familienzahnarzt', 'Das gesamte Spektrum der modernen Zahnheilkunde, vom Kind bis zu den Großeltern.'),
          ('Hilfe bei Schmerzen', 'Bei Schmerz- oder Notfällen rufen Sie uns an. Sie erhalten so schnell wie möglich einen Termin.')],
    top=dict(nav='Laser', tag='Laser', h2='Früher ein Mythos. <em>Bei uns längst etabliert.</em>', img=I20('lefert', '012'),
             txt='Ob bei schonenden chirurgischen Eingriffen, in der Wurzelbehandlung oder zur Parodontitistherapie, ob bei Lippenherpes, Aphthen oder überempfindlichen Zahnhälsen: Der Laser ist ein fester Bestandteil unseres Behandlungskonzeptes.',
             pts=['Bei chirurgischen Eingriffen', 'In der Wurzelbehandlung', 'Zur Parodontitistherapie'], btn='Beratung anfragen', pop='Der Laser ist fester Bestandteil unseres Behandlungskonzeptes. Jetzt beraten lassen.'),
    team=dict(ey='Ihre Zahnärztinnen', h2='Wir beraten. <em>Sie entscheiden.</em>', img=I20('lefert', '009'), cap='Ein Behandlungszimmer der Praxis in Dinklage', mw=620,
              paras=['Als Ihr „Familienzahnarzt“ bieten wir Ihnen das gesamte Spektrum der modernen Zahnheilkunde für Jung und Alt.',
                     'Als Mitglied im Fachkreis „Junge Kieferorthopädie“ informieren wir Eltern frühzeitig über Zahnfehlstellungen bei ihren Kindern.'],
              tl=[('Dinklage', 'Bahnhofstraße 9'), ('Familie', 'von Jung bis Alt')]),
    gal=[(I20('lefert', '007'), '50% 50%'), (I20('lefert', '010'), '50% 50%'), (I20('lefert', '011'), '50% 50%')],
    stimmen=['Seit ich hier bin, gehe ich gern zum Zahnarzt. Bei Schmerzen bekommt man sehr schnell einen Termin.', 'Ich war 15 Jahre nicht beim Zahnarzt. Jetzt gehe ich wieder regelmäßig.', 'Im Notdienst am Sonntagabend: freundlich, schnell und unkompliziert.'],
    hours=[('Mo–Do', '8–12 · 15–18 Uhr'), ('Fr', '8–13 Uhr')], cats=['pzr', 'akut', 'ersatz', 'kind', 'angst'], bot='Leo', notfall='Rufen Sie uns an. Sie erhalten so schnell wie möglich einen Termin. Am Wochenende: Notdienst im Kreis Vechta unter 04446 9882763.',
    rec={'pzr': ['Professionelle Zahnreinigung', 'Die Praxis empfiehlt zweimal im Jahr den „Zahn-TÜV“ mit professioneller Zahnreinigung.'], 'ersatz': ['Implantate', 'Die Praxis informiert Sie umfassend über Implantate und fertigt den Zahnersatz mit ihrem Zahntechnikerteam.'],
         'kind': ['Junge Kieferorthopädie', 'Die Praxis berät Eltern früh zu Zahnfehlstellungen und ist Familienzahnarzt für Jung und Alt.'], 'angst': ['Familienzahnarzt', 'Sagen Sie es gleich am Telefon. Die Praxis berät, Sie entscheiden.']},
    pops=[('tm.jpg', 'Professionelle Zahnreinigung', 'Zeit für den „Zahn-TÜV“? Jetzt Termin zur Zahnprophylaxe anfragen.'), ('g3.jpg', 'Junge Kieferorthopädie', 'Zahnfehlstellung beim Kind? Wir beraten Eltern frühzeitig.')]))

# 9 ─ Zahnärzte Osada, Damme
mk('osada', dict(slug='zahnaerzte-osada-damme', firma='Zahnärzte Osada', kurz='Praxis Zahnärzte Osada', name='Falk und Tina-Vanessa Osada', ort='Damme', strasse='Bahnhofstraße 3', plz='49401',
    tel='05491 4004', tel_i='+4954914004', web='zahnaerzte-osada.de', p='#5d5d5d', dk='#2c2c2c', s2='#f2f2f2', fam=RAL, fonts='r18ant', google=(4.5, 33),
    logo=(I20('osada', '000'), 0, 'trim'), lh=62, hero='r', himgs=[I20('osada', '003'), I20('osada', '003')], cols='46fr 54fr', card='1528/1080',
    ey='Zahnärzte Osada · Damme', h1='Gesunde Zähne für ein <em>schönes Lächeln.</em>',
    sub='Moderne Technik, regelmäßige Fortbildungen und der Blick auf aktuelle Entwicklungen: Wir tun alles für eine fachkundige Behandlung Ihrer Zähne.',
    ubar=[('Für Kinder', 'mit Herz'), ('Implantate', 'und Zahnersatz'), ('Damme', 'Bahnhofstraße 3')],
    sv_h2='Ein Behandlungskonzept, <em>abgestimmt auf Sie.</em>', sv_lead='Gemeinsam mit Ihnen entwickeln wir ein individuell abgestimmtes Behandlungskonzept. Unser Ziel ist Ihre Zahngesundheit.',
    svcs=[('Prophylaxe', 'Maßgeschneiderte Prophylaxe-Konzepte für Kinder und Erwachsene, für den dauerhaften Erhalt von Zähnen und Zahnfleisch.'),
          ('Kinderbehandlung', 'Unsere kleinen Patienten liegen uns besonders am Herzen. Der Zahnarztbesuch soll ein positives Erlebnis werden.'),
          ('Parodontologie', 'Zahnbestand sichern: Wir greifen rechtzeitig ein, bevor Entzündungen Ihr Gebiss schädigen.'),
          ('Implantate', 'Künstliche Zahnwurzeln aus Titan. So lässt sich das Beschleifen gesunder Nachbarzähne vermeiden.'),
          ('Zahnersatz', 'Kronen, Brücken und Prothesen, auf Wunsch metallfrei und komplett aus Keramik.'),
          ('Ästhetik', 'Verschiedene Möglichkeiten zur Verschönerung der Zähne, zum Beispiel Bleaching.')],
    top=dict(nav='Kinder', tag='Kinderbehandlung', h2='Unsere kleinen Patienten <em>liegen uns am Herzen.</em>', img=PX + '2450766.jpg',
             txt='Wir legen großen Wert auf eine kindgerechte und entspannte Atmosphäre, damit der Besuch beim Zahnarzt ein positives Erlebnis wird.',
             pts=['Kindgerechte, entspannte Atmosphäre', 'Eigene Prophylaxe-Konzepte für Kinder', 'Zeit und Geduld'], btn='Kindertermin anfragen', pop='Kindgerecht und entspannt, damit der Zahnarztbesuch ein gutes Erlebnis wird.'),
    zwei=dict(ey='Zahnersatz', h2='Lücken schließen. <em>Wieder gut kauen.</em>', img=PX + '2589770.jpg',
              txt='Je nach Wunsch fertigen wir Ihre Brücke auch metallfrei und komplett aus Keramik. Metallfreier Zahnersatz sieht natürlicher aus und ist bei Unverträglichkeiten eine sinnvolle Lösung.',
              pts=['Kronen, Brücken und Prothesen', 'Auf Wunsch metallfrei aus Keramik', 'Implantate als Alternative zur Brücke'], btn='Beratung anfragen'),
    team=dict(ey='Die Praxis', h2='Entspannte Atmosphäre, <em>freundlicher Service.</em>', img=PX + '2458202.jpg', cap='Symbolbild', mw=560,
              paras=['Eine entspannte Atmosphäre in unseren Räumlichkeiten und einen freundlichen Service halten wir für selbstverständlich.',
                     'Sie finden uns in der Bahnhofstraße 3 in Damme.'],
              tl=[('Damme', 'Bahnhofstraße 3'), ('Familie', 'Kinder und Erwachsene')]),
    stimmen=['Als Angstpatientin habe ich mich selten so wohl beim Zahnarzt gefühlt.', 'Alles wurde verständlich erklärt, ich wurde die ganze Zeit ernst genommen.', 'Im Notdienst trotz voller Praxis freundlich und schnell behandelt.'],
    hours=[('Mo, Di, Do', '8–13 · 14–18 Uhr'), ('Mi, Fr', '8–13 Uhr'), ('Angaben', 'laut Google')], cats=['pzr', 'akut', 'ersatz', 'aest', 'kind', 'angst'], bot='Oskar', notfall='Den diensthabenden Zahnarzt des Notdienstes erfahren Sie unter 05494 9800963.',
    rec={'pzr': ['Prophylaxe', 'Die Praxis entwickelt für Kinder und Erwachsene passende Prophylaxe-Konzepte.'], 'ersatz': ['Zahnersatz', 'Kronen, Brücken, Prothesen oder Implantate, auf Wunsch metallfrei aus Keramik.'],
         'aest': ['Ästhetik', 'Die Praxis bietet verschiedene Möglichkeiten, zum Beispiel Bleaching mit Schiene für zu Hause oder direkt in der Praxis.'], 'kind': ['Kinderbehandlung', 'Kinder liegen der Praxis besonders am Herzen. Die Atmosphäre ist kindgerecht und entspannt.'],
         'angst': ['Prophylaxe', 'Sagen Sie es gleich am Telefon. Patienten loben, dass man hier ernst genommen wird.']},
    pops=[('el.jpg', 'Zahnersatz', 'Kronen und Brücken, auf Wunsch metallfrei aus Keramik.'), ('h1.jpg', 'Prophylaxe', 'Vorsorge für Kinder und Erwachsene. Jetzt Termin anfragen.')]))

# 10 ─ Dr. Michaela Natorp, Holdorf
YT = ytvideo('video', 'Aus der Praxis-Seite', 'Parodontitis: <em>Was hilft?</em>', 'Interview mit Heilpraktiker Peter Aalbers. Ein Video des Kanals „Grün &amp; Gesund“, das die Praxis auf ihrer Website zeigt.', 'zSpXEYHiesM', 'yt.jpg', 'alt')
mk('natorp', dict(slug='zahnarztpraxis-dr-natorp-holdorf', firma='Zahnarztpraxis Dr. Michaela Natorp', kurz='Praxis Dr. Natorp', name='Dr. Michaela Natorp', ort='Holdorf', strasse='Große Straße 32 b', plz='49451',
    tel='05494 995511', tel_i='+495494995511', mail='michaela.natorp@ewetel.net', web='drnatorp.de', p='#eaae89', pi='#2a1608', em='#b3561f', dk='#4d4b4a', s2='#fbf1ea', fam=MONT, fonts='r16geyer',
    logo_txt='Dr. Michaela Natorp<small>Zahnarztpraxis · Holdorf</small>', hero='l', himgs=[PX + '2458202.jpg', PX + '2589771.jpg'], cols='46fr 54fr',
    ey='Zahnarztpraxis Dr. med. dent. Michaela Natorp · Holdorf', h1='Eigene Zähne erhalten. <em>Ohne Angst.</em>',
    sub='Dr. Michaela Natorp und das gesamte Team heißen Sie herzlich willkommen. Uns liegen das Wohl und die Gesundheit unserer Patienten sehr am Herzen.',
    ubar=[('Angstpatienten', 'willkommen'), ('Zahnersatz', 'auch metallfrei'), ('Abends', 'Di bis 19 Uhr')],
    sv_h2='Moderne Zahnmedizin <em>in Holdorf.</em>', sv_lead='Wir bieten Ihnen Behandlungen aus unterschiedlichen Bereichen der modernen Zahnmedizin an und beraten Sie gern persönlich.',
    svcs=[('Behandlung von Angstpatienten', 'Viele Patienten haben Zahnarztangst, weil sie schlechte Erfahrungen gemacht haben. Wir nehmen uns dafür Zeit.'),
          ('Prophylaxe', 'Gesunde Zähne und frischer Atem: So werden Karies und Parodontitis früh erkannt.'),
          ('Wurzelbehandlung', 'Eigene Zähne erhalten und hohe Kosten für Zahnersatz und Implantate vermeiden.'),
          ('Zahnersatz', 'Fehlende Zähne stabil und schön ersetzen, festsitzend oder herausnehmbar, auch metallfrei.'),
          ('Implantate', 'Mehr Lebensqualität: essen, reden und lachen wie mit eigenen Zähnen.'),
          ('Parodontose', 'Wenn das Zahnfleisch entzündet ist und Zähne locker sind: Ursachen finden und behandeln.'),
          ('Kiefergelenk und Zähneknirschen', 'Häufige Kopf-, Ohren- oder Rückenschmerzen können vom Kiefer kommen.')],
    top=dict(nav='Angstpatienten', tag='Behandlung von Angstpatienten', h2='Schlechte Erfahrungen gemacht? <em>Das verstehen wir.</em>', img=PX + '563429.jpg',
             txt='Viele Patienten leiden unter Zahnarztangst, weil sie schlechte oder schmerzhafte Erfahrungen gemacht haben. Uns liegen Ihr Wohl und Ihre Gesundheit am Herzen. Deshalb begleiten wir Angstpatienten besonders behutsam.',
             pts=['Zeit für ein Gespräch vorab', 'Jeder Schritt wird erklärt', 'Sie bestimmen das Tempo'], btn='Behutsamen Termin anfragen', pop='Zahnarztangst? Wir nehmen uns Zeit und erklären jeden Schritt.'),
    zwei=dict(ey='Kiefergelenk', h2='Kopfschmerzen, Nacken verspannt? <em>Es kann am Kiefer liegen.</em>', img=PX + '2530983.jpg',
              txt='Sie wachen morgens auf und fühlen sich wie gerädert, der Kiefer knackt, der Nacken ist verspannt? Dahinter kann nächtliches Zähneknirschen stecken. Wir schauen uns das an.',
              pts=['Untersuchung des Kiefergelenks', 'Beratung zu den Ursachen', 'Individuelle Schiene, wenn sinnvoll'], btn='Termin anfragen'),
    team=dict(ey='Die Praxis', h2='Persönlich für Sie da, <em>mitten in Holdorf.</em>', img=I20('natorp', '000'), cap='Die Praxis an der Großen Straße 32 b in Holdorf',
              paras=['Gerne heißen wir Sie persönlich in unseren Räumlichkeiten willkommen. Bitte bringen Sie Ihre gültige Versicherungskarte und, wenn vorhanden, den Medikamentenplan Ihrer Hausarztpraxis mit.',
                     'Wenn Sie zufrieden mit uns waren, empfehlen Sie uns bitte. Wenn Sie Kritik haben, sagen Sie es uns.'],
              tl=[('Holdorf', 'Große Straße 32 b'), ('Abendtermine', 'dienstags bis 19 Uhr')]),
    video_first=YT, extra_img={'yt.jpg': (R + 'natorp/yt.jpg', 0)},
    hours=[('Mo, Do', '8–12:20 · 14–18 Uhr'), ('Di', '8–12:20 · 14–19 Uhr'), ('Mi, Fr', '8–12:20 Uhr')], cats=['pzr', 'akut', 'ersatz', 'angst'], bot='Nala', notfall='Abgesehen von akuten Schmerzfällen bitten wir um vorherige Terminvereinbarung. Notdiensttelefon: 04446 9882763.',
    rec={'pzr': ['Prophylaxe', 'Regelmäßige Prophylaxe hilft, Karies und Parodontitis früh zu erkennen.'], 'ersatz': ['Zahnersatz', 'Festsitzend, herausnehmbar oder Implantat, auch metallfrei. Die Praxis berät Sie zu allen Wegen.'],
         'angst': ['Behandlung von Angstpatienten', 'Die Praxis hat es sich zur Aufgabe gemacht, Angstpatienten behutsam zu begleiten. Sagen Sie es gleich am Telefon.']},
    pops=[('el.jpg', 'Kiefergelenk und Zähneknirschen', 'Morgens wie gerädert? Wir untersuchen Ihr Kiefergelenk.'), ('h1.jpg', 'Wurzelbehandlung', 'Eigene Zähne erhalten statt ersetzen. Jetzt beraten lassen.')]))
