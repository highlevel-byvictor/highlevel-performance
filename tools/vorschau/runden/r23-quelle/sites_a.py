"""Runde 23 · Zahnarztpraxen 40 km um Werlte. Texte, Logos und Fotos der Praxen; wo Fotos fehlen, neutrale Pixabay-Bilder (nie als Praxis oder Person beschriftet).
Werberecht (HWG): keine Vorher-Nachher-Bilder, keine Heilversprechen, keine Rabatte."""
from common import *
SITES = {}
PX = '/home/claude/pixa20/'
R = '/home/claude/r22raw/'
KO = R + 'komp/'
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
.promo figure img{aspect-ratio:auto!important;height:auto}.pop.side img{height:auto!important;aspect-ratio:auto;max-height:230px;object-fit:cover}.chip20 i{font-style:normal}.chip20 .sm{display:none}.st5{display:inline-block;letter-spacing:2px;background:linear-gradient(90deg,#f5a500 var(--r,100%),#d5d9e2 var(--r,100%));-webkit-background-clip:text;background-clip:text;color:transparent!important;-webkit-text-fill-color:transparent}.chip20 .st{font-size:19px}.lot{bottom:76px}.lot-b{padding:8px 22px 8px 8px}.lot-b .dock{width:62px;height:62px}.lot-b .lb b{font-size:17px}.lot-b .lb small{font-size:12.5px}.lot-s{position:absolute;right:calc(100% + 14px);bottom:10px;width:max-content;max-width:min(300px,calc(100vw - 110px));background:#fff;color:#141a28;border:0;border-radius:18px 18px 4px 18px;padding:13px 16px;font:600 14.5px/1.4 var(--fb);text-align:left;cursor:pointer;box-shadow:0 16px 40px rgba(6,10,22,.26);transition:opacity .4s,transform .4s}.lot-s b{color:color-mix(in srgb,var(--p) 80%,#000)}.lot-s.off,.lot.open .lot-s,.lot:not(.hide-t) .lot-s{opacity:0;transform:translateX(12px);pointer-events:none}html,body{max-width:100%;overflow-x:clip}@media(max-width:900px){section :where(div,figure,ul,ol,li,form,article,a,p,h1,h2,h3,h4,label),header :where(div,a,nav,span){min-width:0}:where(h1,h2,h3,h4,p,li,small,b,label,figcaption){overflow-wrap:break-word}.btn{white-space:normal!important;max-width:100%;box-sizing:border-box}section img,section video,section iframe{max-width:100%}header .lt-logo{font-size:16px;overflow-wrap:anywhere}footer :where(div,a,p,span,small,b),.ft :where(div,a,p,span,small,b){min-width:0;max-width:100%}.lt-logo small{white-space:normal!important;overflow-wrap:anywhere;letter-spacing:.08em}header img{max-width:58vw;height:auto;object-fit:contain}}@media(max-width:900px){.hz{display:grid!important;grid-template-columns:minmax(0,1fr)!important}.hz>*,.hz-tx,.hz-tx .in,.ht20 .w,.ht20 .w>*,.hp .w>*{min-width:0!important;max-width:100%!important;box-sizing:border-box}.hz h1,.ht20 h1,.hz .sub,.ht20 .sub,.hz .ey,.ht20 .ey{overflow-wrap:break-word!important;max-width:100%}.hz-ub,.ub{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:6px 16px!important}.hz-ub div,.ub div{min-width:0;overflow-wrap:anywhere;hyphens:auto;font-size:13.5px}.hz-ub b,.ub b{font-size:17px!important;overflow-wrap:anywhere;hyphens:auto}.ctas{flex-wrap:wrap!important}.ctas .btn{max-width:100%;white-space:normal}.chip20{white-space:normal!important;max-width:100%;box-sizing:border-box}.chip20 b,.chip20 .st,.chip20 .sm{white-space:nowrap;flex:none}}@media(max-width:820px){.chip20 .lg{display:none}.chip20 .sm{display:inline!important}.chip20{max-width:100%;font-size:13.5px!important;white-space:nowrap;padding:9px 14px 9px 12px!important;gap:8px!important}.chip20 b{font-size:17px!important}.chip20 .st{font-size:16px!important}.lot{bottom:134px}.lot-b{padding:5px}.lot-b .dock{width:54px;height:54px}.lot-s{font-size:13.5px;padding:11px 13px;bottom:4px}}.chip20{display:inline-flex!important;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:10px 18px 10px 14px;box-shadow:0 8px 26px rgba(0,0,0,.10);font:600 15.5px var(--fb);margin-bottom:18px}.chip20 b{font:800 20px var(--fh)}.chip20 .st{color:#f5a500;letter-spacing:1px;font-size:17px}
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
    if g('gr'): S['gr'] = g('gr')
    nf = d['notfall']
    S['bot'] = dict(auto=False, say=f'Hallo, ich bin <b>{d["bot"]}</b>, Ihr KI-Assistent. Ich führe Sie durch die Website.', name=d['bot'], tag='Ihr Praxis-Lotse', du=False, tel=d['tel'], tel_i=d['tel_i'], notfall=nf, finBtn='Termin anfragen',
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


ST = 'Auszug aus einer Google-Rezension, sinngemäß'
# 1 ─ Dr. Christoph Bauer, Werlte
mk('bauer', dict(google=(4.5, 23), slug='zahnarzt-dr-bauer-werlte', firma='Praxis Dr. Christoph Bauer', kurz='Praxis Dr. Bauer', name='Dr. Christoph Bauer', ort='Werlte', strasse='Hauptstraße 33', plz='49757',
    tel='05951 994606', tel_i='+495951994606', mail='info@dr-bauer-werlte.de', web='dr-bauer-werlte.de', p='#1c5aa6', dk='#12305a', s2='#eaf0f8', fam=OS, fonts='r16ellers',
    logo=(I20('bauer', '002'), 0), lh=58, hero='r', himgs=[I20('bauer', '017'), I20('bauer', '017')], cols='52fr 48fr', card='3/2',
    ey='Oralchirurgie · Implantologie · Werlte', h1='Implantate und Oralchirurgie. <em>In Ruhe erklärt.</em>',
    sub='Seit 2001 sind wir in Werlte Ihre Ansprechpartner für Oralchirurgie, Zahnerhaltung und Implantate. Moderne Zahnmedizin in ruhiger, entspannter Atmosphäre.',
    ubar=[('Seit 2001', 'in Werlte'), ('Eigenes', 'Dentallabor'), ('Auch für', 'Angstpatienten')],
    sv_h2='Chirurgie und Prothetik <em>unter einem Dach.</em>', sv_lead='Als Praxis mit chirurgischem Schwerpunkt arbeiten wir partnerschaftlich mit Ihrem überweisenden Zahnarzt zusammen.',
    svcs=[('Implantologie', 'Flexible, schonende Lösungen für festsitzenden Zahnersatz, von der Planung bis zur fertigen Krone.'),
          ('Oralchirurgie', 'Operative Eingriffe in der Mundhöhle, ambulant und mit ausführlicher Beratung vorab.'),
          ('Zahnästhetik', 'Hochwertige Restaurationen, gefertigt im eigenen Dentallabor.'),
          ('Kinderzähne', 'Behutsame Behandlung für die Kleinen.'),
          ('Prophylaxe', 'Vorsorge, damit Zähne und Implantate lange halten.'),
          ('Überweisungen', 'Bitte bringen Sie Ihren Überweisungsschein und vorhandene Röntgenbilder mit.')],
    top=dict(nav='Implantate', tag='Implantologie', h2='Fester Zahnersatz, <em>der sich wie Ihr eigener anfühlt.</em>', img=I20('bauer', '013'),
             txt='Der Wert eines natürlichen Zahnes wird oft erst bewusst, wenn er fehlt. Implantate sind ein fester Bestandteil unseres Behandlungsspektrums. Chirurgie und Prothetik liegen bei uns in einer Hand.',
             pts=['Ausführliche Beratung und Diagnose', 'Chirurgie und Prothetik unter einem Dach', 'Zahnersatz aus dem eigenen Labor'], btn='Implantat-Beratung anfragen', pop='Fester Zahnersatz, Chirurgie und Prothetik in einer Praxis.'),
    zwei=dict(ey='Angstpatienten', h2='Angst vor dem Eingriff? <em>Wir nehmen uns Zeit.</em>', img=PX + '2584260.jpg',
              txt='Viele Patienten kommen mit einem mulmigen Gefühl. Sagen Sie es uns gleich am Telefon. Wir erklären jeden Schritt, bevor wir beginnen.',
              pts=['Ruhige, entspannte Atmosphäre', 'Jeder Schritt wird vorher erklärt', 'Sie bestimmen das Tempo'], btn='Behutsamen Termin anfragen'),
    team=dict(ey='Die Praxis', h2='Erfahrung seit 2001, <em>mitten in Werlte.</em>', img=I20('bauer', '011'), cap='Moderne Zahnmedizin in ruhiger Atmosphäre',
              paras=['Fachzahnarzt Dr. Christoph Bauer und sein Team begleiten Sie von der ersten Beratung bis zur Nachsorge.',
                     'Mit dem angeschlossenen eigenen Dentallabor entstehen Zahnrestaurationen in enger Abstimmung zwischen Behandler, Zahntechniker und Patient.'],
              tl=[('2001', 'gegründet'), ('Werlte', 'Hauptstraße 33')]),
    stimmen=['Ich kam als Angstpatientin zu Dr. Bauer, und es war die beste Entscheidung.', 'Ein sehr freundliches Team und ein Arzt, der sich Zeit für Fragen nimmt.', 'Seit vielen Jahren Patient. Man fühlt sich hier immer wohl.'],
    hours=[('Mo, Di, Do', '8–16 Uhr'), ('Mi, Fr', '8–14 Uhr'), ('Hinweis', 'Zeiten laut Google, sonst nach Vereinbarung')], cats=['ersatz', 'akut', 'angst', 'pzr', 'kind', 'aest'], bot='Bela', notfall=GEN_NF,
    rec={'ersatz': ['Implantologie', 'Bei fehlenden Zähnen berät die Praxis zu Implantaten. Chirurgie und Zahnersatz kommen aus einer Hand.'], 'angst': ['Oralchirurgie', 'Sagen Sie es gleich am Telefon. Das Team erklärt jeden Schritt in Ruhe.'],
         'pzr': ['Prophylaxe', 'Vorsorge schützt Zähne und Implantate. Am besten kurz anrufen.'], 'kind': ['Kinderzähne', 'Auch Kinder werden in der Praxis behutsam behandelt.'], 'aest': ['Zahnästhetik', 'Restaurationen aus dem eigenen Labor. Was passt, klärt die Beratung.']},
    pops=[('h1.jpg', 'Oralchirurgie', 'Ambulante Eingriffe mit ausführlicher Beratung vorab.'), ('el.jpg', 'Angstpatienten', 'Ruhige Atmosphäre, jeder Schritt wird erklärt.')]))

# 2 ─ Zahnarztpraxis Melanie Malinowski, Molbergen
mk('malinowski', dict(google=(4.7, 46), slug='zahnarztpraxis-malinowski-molbergen', firma='Zahnarztpraxis Melanie Malinowski', kurz='Zahnarztpraxis Malinowski', name='Melanie Malinowski', ort='Molbergen', strasse='Zum Kavenkamp 2', plz='49696',
    tel='04475 9189966', tel_i='+4944759189966', mail='info@zahnarztpraxis-molbergen.de', web='zahnarztpraxismolbergen.de', p='#8a7d56', dk='#4a4436', s2='#f6f2e6', em='#7a6d45', fam=OS, fonts='r16ellers',
    logo_txt='Zahnarztpraxis<small>Melanie Malinowski · Molbergen</small>', hero='l', himgs=[I20('malinowski', '003'), I20('malinowski', '003')], cols='46fr 54fr', card='714/348',
    ey='Zahnarztpraxis Malinowski · Molbergen', h1='Für ein gesundes <em>und schönes Lächeln.</em>',
    sub='Persönliche Nähe und immer ein offenes Ohr: Das ist unser Anspruch seit 2006. Wir nehmen uns Zeit zum Zuhören und erklären verständlich.',
    ubar=[('Seit 2006', 'in Molbergen'), ('Amalgamfrei', 'Füllungen'), ('Spielecke', 'für Kinder')],
    sv_h2='Was können wir <em>für Sie tun?</em>', sv_lead='Ein umfassendes Behandlungsspektrum der modernen Zahnheilkunde, für Kinder, Jugendliche und Erwachsene.',
    svcs=[('Professionelle Zahnreinigung', 'Gründliche Reinigung als Basis für gesunde Zähne und gesundes Zahnfleisch.'),
          ('Kinder- und Jugendprophylaxe', 'Spielerisch und ohne Druck, damit der Zahnarztbesuch von klein auf vertraut ist.'),
          ('Füllungstherapie', 'Amalgamfreie Füllungen.'),
          ('Parodontologie', 'Behandlung von Zahnfleisch und Zahnhalteapparat, auch mit Laser.'),
          ('Endodontie', 'Behandlung der Zahnwurzel, um den eigenen Zahn zu erhalten.'),
          ('Implantatversorgungen', 'In enger Zusammenarbeit mit erfahrenen Implantologen.')],
    top=dict(nav='Kinder', tag='Kinder- und Jugendprophylaxe', h2='Damit Kinder <em>gern wiederkommen.</em>', img=I20('malinowski', '002'),
             txt='Mit Geduld, einem Kuscheltier und viel Erklären zeigen wir Kindern, wie Zähneputzen geht. Im Wartezimmer steht eine Spielecke bereit.',
             pts=['Kinderspielecke im Wartezimmer', 'Erklären statt Drängen', 'Erinnerungsservice für Kontrolltermine'], btn='Termin für mein Kind', pop='Spielerisch, geduldig und mit eigener Spielecke.'),
    zwei=dict(ey='Angstpatienten', h2='Angst vorm Zahnarzt? <em>Die brauchen Sie nicht.</em>', img=I20('malinowski', '017'),
              txt='Ängste nehmen, zuhören und auf Ihre Wünsche eingehen: Das sind unsere Ziele. Wir begleiten Sie durch die Behandlung und erklären jeden Schritt verständlich.',
              pts=['Zeit zum Zuhören', 'Verständliche Aufklärung', 'Auf Wunsch rufen wir Ihnen ein Taxi'], btn='Behutsamen Termin anfragen'),
    team=dict(ey='Die Praxis', h2='Wir lieben das, <em>was wir tun.</em>', img=I20('malinowski', '026'), cap='Der Empfang der Praxis in Molbergen',
              paras=['Zahnärztin Melanie Malinowski stammt aus Löningen, hat in Hannover studiert und 2006 ihre Praxis in Molbergen gegründet.',
                     'Service gehört dazu: aktuelle Zeitschriften, Leihbrillen in verschiedenen Stärken und Zahlung per EC-Karte.'],
              tl=[('2006', 'gegründet'), ('Molbergen', 'Zum Kavenkamp 2')]),
    gal=[(I20('malinowski', '001'), '50% 50%'), (I20('malinowski', '009'), '50% 50%'), (I20('malinowski', '024'), '50% 50%')],
    stimmen=['Tolles Praxisteam. Danke für die schmerzfreie Behandlung.', 'Früher hatte ich große Angst vor Spritzen. Hier wurde sie mir genommen.', 'Als Notfall wurde mir sofort geholfen, obwohl ich kein Patient war.'],
    hours=[('Mo, Di', '8.30–12.30 · 14.30–18 Uhr'), ('Do', '8–12.30 · 14.30–18 Uhr'), ('Mi, Fr', '8–12 Uhr'), ('Hinweis', 'Zeiten laut Google')], cats=['pzr', 'kind', 'angst', 'akut', 'ersatz', 'aest'], bot='Mali', notfall=GEN_NF,
    rec={'pzr': ['Professionelle Zahnreinigung', 'Die Praxis bietet professionelle Zahnreinigung und einen Erinnerungsservice.'], 'kind': ['Kinder- und Jugendprophylaxe', 'Für Kinder gibt es eine Spielecke und viel Geduld.'],
         'angst': ['Kontrolltermin', 'Ängste nehmen ist ein erklärtes Ziel der Praxis. Sagen Sie es gleich am Telefon.'], 'ersatz': ['Implantatversorgungen', 'Implantate entstehen in Zusammenarbeit mit erfahrenen Implantologen.'], 'aest': ['Professionelle Zahnreinigung', 'Oft beginnt ein schöneres Lächeln mit einer gründlichen Reinigung.']},
    pops=[('el.jpg', 'Angstpatienten', 'Zuhören, erklären, Zeit nehmen.'), ('tm.jpg', 'Professionelle Zahnreinigung', 'Mit Erinnerungsservice für den nächsten Termin.')]))

# 3 ─ Gemeinschaftspraxis Dr. Boven, Haselünne
mk('boven', dict(google=(4.6, 29), slug='zahnarztpraxis-dr-boven-haseluenne', firma='Zahnärztliche Gemeinschaftspraxis Dr. H. Boven', kurz='Gemeinschaftspraxis Dr. Boven', name='Dr. Hermann Boven', ort='Haselünne', strasse='Bahnhofstraße 1', plz='49740',
    tel='05961 889', tel_i='+495961889', mail='info@dr-boven.de', web='dr-boven.de', p='#7a5fa6', dk='#3b2f52', s2='#f1edf7', fam=RAL, fonts='r18ant',
    logo=(I20('boven', '004'), 0), lh=76, hero='team', himgs=[I20('boven', '013'), I20('boven', '013')],
    ey='Gemeinschaftspraxis Dr. Boven · Haselünne', h1='Zahnmedizin für die ganze Familie. <em>Seit 1983.</em>',
    sub='Gesunde Zähne und ein schönes Lachen schenken Lebensfreude. Mit mehr als 40 Jahren Erfahrung sind wir für Sie und Ihre Familie da.',
    ubar=[('Seit 1983', 'in Haselünne'), ('Familienpraxis', 'Vater und Töchter'), ('Lachgas', 'auf Wunsch')],
    sv_h2='Moderne Zahnheilkunde <em>für alle Patienten.</em>', sv_lead='Ein engagiertes, freundliches Team mit verständlicher Beratung und verlässlichen Abläufen.',
    svcs=[('Prophylaxe', 'Professionelle Zahnreinigung, damit Karies und Parodontitis gar nicht erst entstehen.'),
          ('Zahnerhaltung', '„Der eigene gesunde Zahn ist immer besser als jedes Implantat.“ Fast unsichtbare Füllungen.'),
          ('Kinderzahnheilkunde', 'Eingewöhnungstermine, damit Kind und Eltern Praxis und Team in Ruhe kennenlernen.'),
          ('Implantate und Zahnersatz', 'Fester, ästhetischer Ersatz für einzelne oder mehrere Zähne.'),
          ('Kieferorthopädie', 'Auch mit unsichtbarer Zahnspange.'),
          ('Schnarch- und Schienentherapie', 'Hilfe bei Schnarchen und Kiefergelenksbeschwerden.')],
    top=dict(nav='Kinder', tag='Kinderzahnheilkunde', h2='Kinderbehandlung fängt <em>mit dem ersten Milchzahn an.</em>', img=I20('boven', '037'),
             txt='Mit Einfühlungsvermögen, Ruhe und Kompetenz schaffen wir für Kinder eine angenehme Atmosphäre. Sie sollen den Besuch beim Zahnarzt in guter Erinnerung behalten.',
             pts=['Eingewöhnungstermine', 'Ruhe und Geduld', 'Lachgas auf Wunsch'], btn='Termin für mein Kind', pop='Eingewöhnungstermine für einen sanften Start.'),
    team=dict(ey='Ihre Zahnärzte', h2='Eine Familie, <em>eine Praxis.</em>', img=I20('boven', '006'), cap='Der Empfang der Praxis in Haselünne',
              paras=['Dr. Hermann Boven hat die Praxis 1983 gegründet. Heute arbeiten auch seine beiden Töchter mit ihm zusammen.',
                     'Regelmäßige Fortbildungen und die Mitgliedschaft in Fachverbänden halten das Team auf dem neuesten Stand.'],
              tl=[('1983', 'gegründet'), ('40+', 'Jahre Erfahrung')]),
    stimmen=['Früher bei Dr. Boven, heute bei seiner Tochter. Alle sind immer sehr freundlich.', 'Man bekommt schnell einen Termin, auch im Notfall.', 'Kompetente Beratung trotz kurzfristigem Termin.'],
    hours=[('Mo, Do, Fr', '8–12 · 14–18 Uhr'), ('Di', '8–13 · 14–19 Uhr'), ('Mi', '8–12 Uhr (laut Google)')], cats=['pzr', 'kind', 'akut', 'ersatz', 'aest', 'angst'], bot='Bovi', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe', 'Die professionelle Zahnreinigung ist ein Schwerpunkt der Praxis.'], 'kind': ['Kinderzahnheilkunde', 'Für Kinder gibt es Eingewöhnungstermine.'], 'ersatz': ['Implantate und Zahnersatz', 'Die Praxis berät Sie zu Implantaten, Brücken und Prothesen.'],
         'aest': ['Kieferorthopädie', 'Von der Zahnreinigung bis zur unsichtbaren Zahnspange. Was passt, klärt die Beratung.'], 'angst': ['Kontrolltermin', 'Sprechen Sie es am Telefon an. Die Praxis bietet auf Wunsch auch Lachgas an.']},
    pops=[('h1.jpg', 'Unsichtbare Zahnspange', 'Zahnkorrektur, die kaum jemand bemerkt.'), ('tm.jpg', 'Schnarchtherapie', 'Hilfe bei Schnarchen, direkt in der Praxis.')]))

# 4 ─ Zahnärzte Meldau & Sowinski, Haselünne
mk('melso', dict(google=(4.8, 47), slug='zahnaerzte-meldau-sowinski-haseluenne', firma='Zahnärzte Meldau & Sowinski', kurz='Praxis Meldau & Sowinski', name='Thomas Meldau und Martin Sowinski', ort='Haselünne', strasse='Markt 12', plz='49740',
    tel='05961 9222', tel_i='+4959619222', mail='info@melso.net', web='melso.net', p='#1089b0', dk='#0d3f52', s2='#e8f6fb', fam=NUN, fonts='r16galerie',
    logo_txt='Zahnärzte<small>Meldau & Sowinski · Haselünne</small>', hero='r', himgs=[KO + 'melso-team.jpg', KO + 'melso-team.jpg'], cols='60fr 40fr', card='884/888',
    ey='Zahnärzte Meldau & Sowinski · Haselünne', h1='Ihr neues Lebensgefühl <em>beginnt mit gesunden Zähnen.</em>',
    sub='Implantologie, Parodontologie und ästhetische Zahnheilkunde am Markt in Haselünne. Mit eigenem Praxislabor im Haus.',
    ubar=[('Seit 1994', 'am Markt'), ('Eigenlabor', 'im Haus'), ('Implantologie', 'seit 1994')],
    sv_h2='Dauerhaft gesunde <em>und schöne Zähne.</em>', sv_lead='Immer mehr Menschen wünschen sich hochwertige, ästhetische und verträgliche Lösungen. Wir zeigen Ihnen die Möglichkeiten.',
    svcs=[('Implantologie', 'Festsitzende, schöne Zähne als Ergänzung zur klassischen Prothetik.'),
          ('Prophylaxe', 'Gesunde eigene Zähne bis ins hohe Alter müssen keine Wunschvorstellung sein.'),
          ('Parodontitistherapie', 'Behandlung von Zahnfleisch und Zahnhalteapparat.'),
          ('Kosmetische Zahnbehandlungen', 'Für ein strahlendes Lächeln, von der Zahnreinigung bis zur Keramik.'),
          ('Füllungstherapie', 'Ausschließlich zahnfarbene Materialien, auf Wunsch computergefräste Keramik aus dem Eigenlabor.'),
          ('Zahnersatz', 'Im persönlichen Gespräch finden wir die passende Lösung.')],
    top=dict(nav='Implantate', tag='Implantologie', h2='Essen, reden, lachen. <em>Ohne an den Zahnersatz zu denken.</em>', img=I20('melso', '009'),
             txt='Lebensqualität hat viele Aspekte. Festsitzende und schöne Zähne gehören dazu. Implantate sind deshalb eine wichtige Ergänzung zur klassischen Prothetik.',
             pts=['Implantologische Tätigkeit seit 1994', 'Zahnersatz aus dem Praxislabor', 'Beratung im persönlichen Gespräch'], btn='Implantat-Beratung anfragen', pop='Fester Zahnersatz, gefertigt im eigenen Labor.'),
    zwei=dict(ey='Praxislabor', h2='Zahnarzt und Zahntechniker <em>unter einem Dach.</em>', img=PX + '7660684.jpg',
              txt='In unserem Praxislabor werden alle Arten von Zahnersatz gefertigt. Weil die Laborräume im Praxisgebäude liegen, arbeiten Patient, Zahnarzt und Zahntechniker direkt zusammen.',
              pts=['Eigenlabor seit 1997', 'Ausgebildete Zahntechniker', 'Kurze Wege, direkte Abstimmung'], btn='Beratung anfragen'),
    team=dict(ey='Das Team', h2='Im Mittelpunkt steht <em>immer der Mensch.</em>', img=I20('melso', '010'), cap='In der Praxis am Markt in Haselünne',
              paras=['Eine freundliche Stimme am Telefon, eine herzliche Aufnahme und eine vertrauensvolle Behandlung: So verstehen wir unsere Arbeit.',
                     'Thomas Meldau und Martin Sowinski führen die Gemeinschaftspraxis am Markt seit 1994.'],
              tl=[('1994', 'eröffnet'), ('1997', 'Eigenlabor')]),
    stimmen=['Die Behandlung war von Anfang an angenehm und professionell.', 'Als neuer Patient mit Notfall bekam ich sofort einen Termin.', 'Seit Jahren Patient. Alles ist immer bestens, alle sind freundlich.'],
    hours=[('Mo, Di, Do', '8–12 · 14–18 Uhr'), ('Mi, Fr', '8–12 Uhr'), ('Außerdem', 'nach Vereinbarung')], cats=['ersatz', 'pzr', 'akut', 'aest', 'angst', 'kind'], bot='Melo', notfall=GEN_NF,
    rec={'ersatz': ['Implantologie', 'Die Praxis setzt seit 1994 Implantate und fertigt den Zahnersatz im eigenen Labor.'], 'pzr': ['Prophylaxe', 'Prophylaxe ist fester Teil des Behandlungskonzepts.'], 'aest': ['Kosmetische Zahnbehandlungen', 'Von der Zahnreinigung bis zur Keramik. Die Beratung zeigt, was passt.'],
         'angst': ['Kontrolltermin', 'Sagen Sie es am Telefon. Das Team nimmt sich Zeit.'], 'kind': ['Prophylaxe', 'Am besten kurz anrufen und einen Termin für Ihr Kind abstimmen.']},
    pops=[('el.jpg', 'Praxislabor', 'Zahnersatz, direkt im Haus gefertigt.'), ('tm.jpg', 'Prophylaxe', 'Gesunde eigene Zähne bis ins hohe Alter.')]))

# 5 ─ Praxis für Zahnheilkunde Dres. Lucke, Löningen
mk('lucke', dict(google=(4.6, 21), slug='zahnarzt-dres-lucke-loeningen', firma='Praxis für Zahnheilkunde Dres. Lucke', kurz='Praxis Dres. Lucke', name='Dr. Tobias Lucke und Dr. Katharina Lucke', ort='Löningen', strasse='Poststraße 17', plz='49624',
    tel='05432 9054105', tel_i='+4954329054105', mail='info@zahnarzt-löningen.de', web='zahnarzt-löningen.de', p='#2a938d', dk='#17504d', s2='#e8f5f4', fam=LATO, fonts='r10vagts',
    logo_txt='Praxis für Zahnheilkunde<small>Dres. Lucke · Löningen</small>', hero='r', himgs=[KO + 'lucke-duo.jpg', KO + 'lucke-duo.jpg'], cols='52fr 48fr', card='2/1',
    ey='Praxis für Zahnheilkunde · Löningen', h1='Familienfreundlich. <em>Für Implantate und Kinderzähne.</em>',
    sub='Herzlich willkommen in Ihrer familienfreundlichen Praxis für Implantologie und Kinderzahnheilkunde. Helle Räume, moderne Technik und ein Team, das sich Zeit nimmt.',
    ubar=[('3D-Röntgen', 'DVT'), ('CEREC', 'Keramik in einer Sitzung'), ('Für Kinder', 'ab dem ersten Zahn')],
    sv_h2='Unsere Leistungen <em>auf einen Blick.</em>', sv_lead='Von der Vorsorge bis zum Implantat, für die ganze Familie.',
    svcs=[('Implantologie', 'Tätigkeitsschwerpunkt Implantologie (DGI), geplant mit dreidimensionaler Röntgentechnik.'),
          ('Kinder- und Jugendzahnheilkunde', '„Gesund beginnt im Mund.“ Der erste Besuch am besten mit dem ersten Zahn.'),
          ('Kieferorthopädie', 'Mit herausnehmbaren und festen Apparaturen.'),
          ('CEREC', 'Vollkeramik in einer Sitzung.'),
          ('Ästhetische Zahnheilkunde', 'Für ein Lächeln, mit dem Sie sich wohlfühlen.'),
          ('Prophylaxe', 'Vorsorge für Kinder und Erwachsene.')],
    top=dict(nav='Kinder', tag='Kinder- und Jugendzahnheilkunde', h2='Der erste Zahnarztbesuch <em>Ihres Kindes.</em>', img=I20('lucke', '012'),
             txt='Der erste Besuch sollte am besten mit dem ersten Zahn, spätestens mit 18 Monaten stattfinden. In der ausführlichen Erstberatung geht es um Zahnpasta, Putztechnik, Schnuller, Flasche und Ernährung.',
             pts=['Ausführliche Erstberatung für Eltern', 'Kleine Kinder sitzen auf dem Schoß', 'Tipps bei Zahnungsproblemen'], btn='Termin für mein Kind', pop='Erstberatung für Eltern, am besten ab dem ersten Zahn.'),
    zwei=dict(ey='Implantologie', h2='Wieder essen, <em>was man will.</em>', img=PX + '2530983.jpg',
              txt='Gehen Zähne verloren, geht auch Lebensqualität verloren. Die Implantologie ersetzt einzelne oder mehrere Zähne fest und dauerhaft. Geplant wird mit 3D-Röntgen.',
              pts=['Tätigkeitsschwerpunkt Implantologie (DGI)', 'Planung mit 3D-Röntgen (DVT)', 'Ausführliche Beratung vorab'], btn='Implantat-Beratung anfragen'),
    team=dict(ey='Ihre Zahnärzte', h2='Zwei Zahnärzte, <em>eine Familie.</em>', img=PX + '2589771.jpg', cap='Symbolbild', mw=640,
              paras=['Dr. Tobias Lucke hat in Göttingen studiert und trägt den Tätigkeitsschwerpunkt Implantologie der DGI. Er führt die Praxis gemeinsam mit Dr. Katharina Lucke.',
                     'In hellen, freundlichen Räumen arbeiten wir mit moderner Technik, unter anderem mit dreidimensionalem Röntgen.'],
              tl=[('DGI', 'Implantologie'), ('Löningen', 'Poststraße 17')]),
    stimmen=['Der Zahnarzt nimmt sich immer Zeit und erklärt genau, was er gefunden hat.', 'Auch für Angstpatienten geeignet. Sehr transparent.', 'Eine moderne, helle Praxis. Dr. Lucke kann wunderbar mit Kindern umgehen.'],
    hours=[('Telefon Mo–Do', '9–12 Uhr'), ('Telefon Mo, Di, Do', '15–17 Uhr'), ('Telefon Fr', '9–12 Uhr'), ('Termine', 'nach Vereinbarung')], cats=['kind', 'ersatz', 'pzr', 'akut', 'aest', 'angst'], bot='Luki', notfall=GEN_NF,
    rec={'kind': ['Kinder- und Jugendzahnheilkunde', 'Die Praxis ist auf Kinder eingestellt. Der erste Besuch am besten mit dem ersten Zahn.'], 'ersatz': ['Implantologie', 'Implantologie ist ein Schwerpunkt der Praxis, geplant mit 3D-Röntgen.'], 'pzr': ['Prophylaxe', 'Vorsorge für Kinder und Erwachsene.'],
         'aest': ['CEREC', 'Vollkeramik in einer Sitzung. Was passt, klärt die Beratung.'], 'angst': ['Kontrolltermin', 'Sagen Sie es am Telefon. Das Team erklärt alles in Ruhe.']},
    pops=[('h1.jpg', 'CEREC', 'Vollkeramik in einer Sitzung.'), ('el.jpg', 'Implantologie', 'Geplant mit 3D-Röntgen.')]))

# 6 ─ Zahnarzt Dr. Rölleke, Meppen
mk('roelleke', dict(gr=(4.3, 32), slug='zahnarzt-dr-roelleke-meppen', firma='Zahnarztpraxis Dr. Christian Rölleke', kurz='Praxis Dr. Rölleke', name='Dr. Christian Rölleke', ort='Meppen', strasse='Kolpingstraße 8', plz='49716',
    tel='05931 2627', tel_i='+4959312627', mail='praxis@roelleke.de', web='roelleke.de', p='#e0601a', pi='#1b1d22', dk='#2a2522', s2='#fbf0e8', em='#c24f10', fam=ASAP, fonts='r16ikum',
    logo=(I20('roelleke', '000'), 0), lh=70, hero='l', himgs=[I20('roelleke', '003'), I20('roelleke', '003')], cols='44fr 56fr', card='600/393',
    ey='Zahnarzt Dr. Rölleke · Meppen', h1='Nehmen Sie <em>beruhigt Platz.</em>',
    sub='Zahnmedizin auf hohem Niveau, in Räumen, die bewusst für eine entspannte Atmosphäre gestaltet sind. Mit welchen Wünschen Sie auch kommen: Wir sind für Sie da.',
    ubar=[('Meppen', 'Kolpingstraße 8'), ('Ab 7.40 Uhr', 'geöffnet'), ('Moderne', 'Praxisräume')],
    sv_h2='Moderne Behandlung <em>in der Zahnarztpraxis.</em>', sv_lead='Regelmäßige Kontrolle und Vorsorge, akute Probleme, ästhetische Korrekturen und aufwendigere Behandlungen.',
    svcs=[('Prophylaxe', 'Regelmäßige Vorsorge für dauerhaft gesunde Zähne.'),
          ('Zahnimplantatversorgung', 'Fester Ersatz für fehlende Zähne.'),
          ('Zahnersatz und Zahnerhalt', 'Inlays, Füllungen, Kronen und Brücken.'),
          ('Parodontitisbehandlung', 'Schonende Behandlung des Zahnhalteapparats.'),
          ('Kiefergelenk (CMD)', 'Hilfe bei Kiefergelenksbeschwerden, auch mit Knirscherschiene.'),
          ('Bleaching und Veneers', 'Ästhetische Korrekturen auf Wunsch.')],
    top=dict(nav='Praxis', tag='Die Praxis', h2='Räume, die <em>Ruhe ausstrahlen.</em>', img=I20('roelleke', '007'),
             txt='Für viele ist der Besuch beim Zahnarzt nach wie vor eine Herausforderung. Deshalb war es schon bei der Gestaltung der Praxisräume unser Ziel, mit einer entspannten Atmosphäre positive Gefühle zu vermitteln.',
             pts=['Helle, moderne Räume', 'Technisch moderne Geräte', 'Ein Team, das auf Sie eingeht'], btn='Termin anfragen', pop='Entspannte Atmosphäre, moderne Technik.'),
    team=dict(ey='Das Team', h2='Professionell, <em>und nah am Patienten.</em>', img=I20('roelleke', '019'), cap='In der Praxis an der Kolpingstraße in Meppen',
              paras=['Unsere Praxis bietet neben technisch modernen Geräten eine professionelle Behandlung, die sich an den Bedürfnissen der Patienten ausrichtet.',
                     'Schöne und gesunde Zähne stehen für Attraktivität und Lebensqualität. Dabei begleiten wir Sie.'],
              tl=[('Meppen', 'Kolpingstraße 8'), ('7.40 Uhr', 'ab morgens')]),
    gal=[(I20('roelleke', '018'), '50% 50%'), (I20('roelleke', '020'), '50% 50%'), (I20('roelleke', '021'), '50% 50%')],
    stimmen=['Mein Schneidezahn brach ab. Ich wurde sofort freundlich und kompetent versorgt.', 'Unsere Kinder gehen gern hin. Das sagt alles.', 'Toller Arzt, tolles Team, tolle Praxis.'],
    hours=[('Mo, Di, Do', '7.40–12 · 14.30–18 Uhr'), ('Mi, Fr', '7.40–12.30 Uhr'), ('Außerdem', 'nach Vereinbarung')], cats=['pzr', 'akut', 'ersatz', 'aest', 'kind', 'angst'], bot='Rölli', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe', 'Regelmäßige Vorsorge ist die Basis. Am besten kurz anrufen.'], 'ersatz': ['Zahnimplantatversorgung', 'Die Praxis berät Sie zu Implantaten und Zahnersatz.'], 'aest': ['Bleaching und Veneers', 'Ästhetische Korrekturen bespricht die Praxis mit Ihnen persönlich.'],
         'kind': ['Prophylaxe', 'Kinder sind willkommen. Rezensionen loben die Geduld mit kleinen Patienten.'], 'angst': ['Kontrolltermin', 'Die Räume sind bewusst entspannt gestaltet. Sagen Sie am Telefon, dass Sie sich Zeit wünschen.']},
    pops=[('h1.jpg', 'Zahnimplantatversorgung', 'Fester Ersatz für fehlende Zähne.'), ('tm.jpg', 'Knirscherschiene', 'Schutz für Zähne und Kiefergelenk.')]))

# 7 ─ Zahnarztpraxis Leicht, Meppen
mk('leicht', dict(gr=(4.4, 23), slug='zahnarztpraxis-leicht-meppen', firma='Zahnarztpraxis Leicht', kurz='Zahnarztpraxis Leicht', name='Ulrich Leicht und Reemt Leicht', ort='Meppen', strasse='Haselünner Str. 53', plz='49716',
    tel='05931 2444', tel_i='+4959312444', mail='info@zahnarzt-leicht.de', web='zahnarzt-leicht.de', p='#2c4ca5', dk='#17265a', s2='#ebeff9', fam=MONT, fonts='r16geyer',
    logo_txt='Zahnarzt Leicht<small>Zahnärzte aus Leidenschaft · Meppen</small>', hero='team', himgs=[I20('leicht', '002'), I20('leicht', '002')],
    ey='Zahnarztpraxis Leicht · Meppen', h1='Zahnärzte aus Leidenschaft. <em>In zweiter Generation.</em>',
    sub='Seit über 40 Jahren für unsere Patienten da. Mit eigenem Meisterlabor, fünf Behandlungsräumen und einem OP-Bereich decken wir alle zahnärztlichen Disziplinen ab.',
    ubar=[('40+ Jahre', 'Erfahrung'), ('Meisterlabor', 'im Haus'), ('Ebenerdig', 'und barrierefrei')],
    sv_h2='Alle Disziplinen <em>in einer Praxis.</em>', sv_lead='Fachliche Kompetenz, verbunden mit der Fähigkeit, Patientenprobleme zu erkennen und individuell zu versorgen.',
    svcs=[('Implantologie', 'Implantate und Implantatprothetik als Tätigkeitsschwerpunkt.'),
          ('Oralchirurgie', 'Auch komplizierte Eingriffe, auf Wunsch in Intubationsnarkose.'),
          ('Zahntechnik', 'Kronen, Brücken und Prothesen ausschließlich aus dem eigenen Labor.'),
          ('Konservierende Zahnheilkunde', 'Zähne erhalten, wo immer es geht.'),
          ('Parodontologie', 'Behandlung von Zahnfleisch und Zahnhalteapparat.'),
          ('Lasertherapie und 3D-Röntgen', 'Moderne bildgebende Röntgentechnik mit dreidimensionaler Darstellung.')],
    top=dict(nav='Implantate', tag='Implantologie und Oralchirurgie', h2='Vom Eingriff bis zur Krone. <em>Alles im eigenen Haus.</em>', img=I20('leicht', '016'),
             txt='Tätigkeitsschwerpunkte der Praxis sind Implantologie, Implantatprothetik und Oralchirurgie. Geplante Behandlungsschritte erläutern wir nachvollziehbar, der Zahntechniker wird in die Abstimmung einbezogen.',
             pts=['OP-Bereich in der Praxis', 'Zahnersatz aus dem eigenen Meisterlabor', 'Nachvollziehbare Erklärung jedes Schritts'], btn='Implantat-Beratung anfragen', pop='Implantat, Chirurgie und Zahntechnik unter einem Dach.'),
    zwei=dict(ey='Zahntechnik', h2='Zahnersatz <em>aus dem eigenen Meisterlabor.</em>', img=I20('leicht', '033'),
              txt='Der Zahnersatz, der bei unseren Patienten eingesetzt wird, stammt ausschließlich aus unseren eigenen Labors. Der Zahntechniker stimmt individuelle Wünsche direkt mit Ihnen ab.',
              pts=['Meisterlabor im Haus', 'CE-zertifizierte Materialien', 'Direkte Abstimmung mit dem Zahntechniker'], btn='Beratung anfragen'),
    team=dict(ey='Die Zahnärzte', h2='Zwei Generationen, <em>eine Berufsauffassung.</em>', img=I20('leicht', '015'), cap='Aus der Zahnarztpraxis Leicht in Meppen', mw=480,
              paras=['Ulrich Leicht behandelt seit über 40 Jahren. Mit Reemt Leicht führt die zweite Generation die Praxis fort.',
                     'Die gesamte Praxis ist ebenerdig und behindertengerecht gebaut, ohne Stufen oder Schwellen. Parkplätze gibt es direkt am Haus.'],
              tl=[('5', 'Behandlungsräume'), ('2.', 'Generation')]),
    gal=[(I20('leicht', '003'), '50% 50%'), (I20('leicht', '017'), '50% 50%'), (I20('leicht', '001'), '50% 50%')],
    stimmen=['Ein fantastischer Zahnarzt mit einem Team, das seit Jahren zusammenarbeitet.', 'Sehr verständnisvoll, gerade wenn man Angst hat.', 'Man bekommt immer schnell einen Termin.'],
    hours=[('Mo, Di, Do', '8–12 · 14.30–18 Uhr'), ('Mi, Fr', '8–12 Uhr'), ('Außerdem', 'nach Vereinbarung')], cats=['ersatz', 'akut', 'pzr', 'angst', 'aest', 'kind'], bot='Leo', notfall=GEN_NF,
    rec={'ersatz': ['Implantologie', 'Implantate sind ein Schwerpunkt der Praxis. Der Zahnersatz kommt aus dem eigenen Meisterlabor.'], 'pzr': ['Konservierende Zahnheilkunde', 'Für Kontrolle und Vorsorge am besten kurz anrufen.'], 'angst': ['Oralchirurgie', 'Größere Eingriffe sind auf Wunsch in Narkose möglich. Sprechen Sie es am Telefon an.'],
         'aest': ['Zahntechnik', 'Im eigenen Labor wird Ihr Wunsch direkt mit dem Zahntechniker abgestimmt.'], 'kind': ['Konservierende Zahnheilkunde', 'Am besten kurz anrufen und einen Termin abstimmen.']},
    pops=[('el.jpg', 'Zahntechnik', 'Zahnersatz aus dem eigenen Meisterlabor.'), ('tm.jpg', 'Oralchirurgie', 'Eingriffe auf Wunsch in Narkose.')]))

# 8 ─ Zahnärzte Bode, Meppen
mk('bode', dict(google=(4.8, 16), slug='zahnaerzte-bode-meppen', firma='Zahnärzte Bode', kurz='Praxis Zahnärzte Bode', name='Dr. Peter Bode und Maximilian Bode', ort='Meppen', strasse='Am Neuen Markt 78', plz='49716',
    tel='05931 18111', tel_i='+49593118111', mail='anmeldung@dres-bode.de', web='zahnarzt-bode.de', p='#0078aa', dk='#083d55', s2='#e7f3f8', fam=OS, fonts='r16ellers',
    logo=(I20('bode', '000'), 0, 'trim'), lh=74, hero='l', himgs=[KO + 'bode-duo.jpg', KO + 'bode-duo.jpg'], cols='44fr 56fr', card='1066/800',
    ey='Zahnärzte Bode · Meppen', h1='Vorsorge, Zahnerhaltung, Ästhetik. <em>Mit Tradition seit 1903.</em>',
    sub='Ihr Wohl als Patient und der Erhalt Ihrer Zähne stehen bei uns an erster Stelle. Wir nehmen uns Zeit für Ihre Fragen und Wünsche.',
    ubar=[('Seit 1903', 'Zahnheilkunde in Meppen'), ('Vater und Sohn', 'in einer Praxis'), ('3D-Röntgen', 'und Diagnostik')],
    sv_h2='Der Erhalt Ihrer Zähne <em>steht an erster Stelle.</em>', sv_lead='Moderne, qualitätsorientierte Behandlung im Sinne der Zahnerhaltung.',
    svcs=[('Vorsorge für Kinder und Jugendliche', 'Früherkennung schon im Säuglingsalter. Bringen Sie Ihr Kind gern zur eigenen Untersuchung mit.'),
          ('Professionelle Zahnreinigung', 'Entfernt, was die Zahnbürste nicht erreicht.'),
          ('Digitales und 3D-Röntgen', 'Erkrankte Stellen früh erkennen, auch an schwer einsehbaren Stellen.'),
          ('Komposit-Füllungen', 'Moderne, zahnfarbene Füllungen in einer Behandlung.'),
          ('Teilkronen und Inlays', 'Wenn der Defekt für eine Füllung zu groß ist.'),
          ('Wurzelkanalbehandlung', 'Damit der eigene Zahn erhalten bleibt.'),
          ('Zahnaufhellung', 'Sicher und professionell in der Praxis.')],
    top=dict(nav='Vorsorge', tag='Vorsorge und Diagnostik', h2='Früh erkennen, <em>statt später reparieren.</em>', img=I20('bode', '026'),
             txt='Regelmäßige Vorsorge ist die wichtigste Voraussetzung für gesunde Zähne. Empfohlen werden zwei Untersuchungen im Jahr. Mit digitalem und 3D-Röntgen sehen wir auch verborgene Stellen.',
             pts=['Vorsorge für Erwachsene mit Bonusheft-Stempel', 'Früherkennung für die Kleinsten', 'Digitales Röntgen und 3D-Diagnostik'], btn='Vorsorgetermin anfragen', pop='Zwei Vorsorgetermine im Jahr halten Zähne gesund.'),
    zwei=dict(ey='Historie', h2='Mehr als ein Jahrhundert <em>Zahnheilkunde in Meppen.</em>', img=I20('bode', '020'),
              txt='In Meppen ist der Name Bode eng mit der Zahnmedizin verbunden. 1903 eröffnete in der Hasestraße das „Zahnatelier“, die damals erste Zahnarztpraxis im Emsland. Das Stadtmagazin DER MEPPENER hat die Geschichte 2021 erzählt.',
              pts=['1903: das „Zahnatelier“ in der Hasestraße', 'Zahnmedizin über Generationen', 'Heute: Dr. Peter Bode und Maximilian Bode'], btn='Termin anfragen'),
    team=dict(ey='Unser Team', h2='In guten <em>Händen.</em>', img=I20('bode', '001'), cap='Der Empfang der Praxis am Neuen Markt', mw=640,
              paras=['Unser Team aus Zahnärzten, Zahntechnikern und medizinischen Fachangestellten kümmert sich fachkundig um Ihre Zahngesundheit.',
                     'Lernen Sie unsere modern und freundlich gestalteten Praxisräume kennen.'],
              tl=[('1903', 'Tradition'), ('Meppen', 'Am Neuen Markt 78')]),
    stimmen=['Der Schwerpunkt liegt auf dem Erhalt der Zähne. Ich werde gründlich beraten.', 'Ein Zahnarzt für die ganze Familie. Er nimmt sich Zeit, ohne Druck.', 'Seit über 25 Jahren Patient und immer bestens behandelt.'],
    hours=[('Mo, Di, Do', '8.30–12.30 · 14.30–18 Uhr'), ('Mi, Fr', '8.30–13 Uhr')], cats=['pzr', 'kind', 'akut', 'aest', 'ersatz', 'angst'], bot='Bodo', notfall=GEN_NF,
    rec={'pzr': ['Professionelle Zahnreinigung', 'Vorsorge und Zahnreinigung sind Schwerpunkte der Praxis.'], 'kind': ['Vorsorge für Kinder und Jugendliche', 'Früherkennung gibt es schon für die Kleinsten.'], 'aest': ['Zahnaufhellung', 'Die Praxis bietet professionelle Zahnaufhellung an. Was möglich ist, klärt die Beratung.'],
         'ersatz': ['Teilkronen und Inlays', 'Die Praxis berät Sie zu ästhetischem Zahnersatz.'], 'angst': ['Kontrolltermin', 'Sagen Sie es am Telefon. Rezensionen loben die Ruhe und Geduld.']},
    pops=[('el.jpg', 'Seit 1903', 'Zahnheilkunde mit Tradition in Meppen.'), ('tm.jpg', 'Zahnaufhellung', 'Sicher und professionell in der Praxis.')]))

# 9 ─ Zahnarztpraxis Dres. Franke, Meppen
mk('franke', dict(google=(5.0, 16), slug='zahnarztpraxis-dres-franke-meppen', firma='Zahnarztpraxis Dres. Franke', kurz='Praxis Dres. Franke', name='Dr. Lutz Franke und Dr. Karin Franke', ort='Meppen', strasse='Lessingstraße 12', plz='49716',
    tel='05931 13242', tel_i='+49593113242', web='dres-franke.de', p='#2b8660', dk='#1a4735', s2='#eaf5f0', fam=NOTO, fonts='r18rec',
    logo_txt='Zahnarztpraxis<small>Dres. Franke · Meppen</small>', hero='r', himgs=[I20('franke', '019'), I20('franke', '019')], cols='54fr 46fr', card='667/432',
    ey='Zahnarztpraxis Dres. Franke · Meppen', h1='Vorsorge ist <em>unser wichtigstes Anliegen.</em>',
    sub='Was gibt es Schöneres, als die eigenen Zähne langfristig gesund und gepflegt zu erhalten? Dafür steht Ihnen unser Team zur Verfügung.',
    ubar=[('Meppen', 'Lessingstraße 12'), ('Prophylaxe', 'als Schwerpunkt'), ('Akupunktur', 'in der Praxis')],
    sv_h2='Unsere <em>Tätigkeitsschwerpunkte.</em>', sv_lead='Ein Einblick in das, was wir für Sie tun.',
    svcs=[('Prophylaxe', 'Regelmäßige Maßnahmen in der Praxis schützen Zähne und Zahnhalteapparat.'),
          ('Ästhetik', 'Ein natürliches Lächeln mit schönen Zähnen.'),
          ('Implantate', 'Künstliche Zahnwurzeln aus verträglichem Material, fest im Kiefer verankert.'),
          ('Füllungen', 'Kleine Defekte möglichst schonend und minimalinvasiv versorgen.'),
          ('Parodontose', 'Behandlung entzündlicher Veränderungen von Zahnfleisch und Zahnbett.'),
          ('Kieferorthopädie', 'Kinderzahnheilkunde und Zahnregulierung.'),
          ('Chirurgie und Akupunktur', 'Kleine chirurgische Eingriffe und Ohrakupunktur.')],
    top=dict(nav='Prophylaxe', tag='Prophylaxe', h2='Die eigenen Zähne <em>ein Leben lang behalten.</em>', img=PX + '2530983.jpg',
             txt='Prophylaxe, zu Deutsch Vorsorge, ist unser wichtigstes Anliegen. Dazu gehört, das heutige Wissen über Ernährung und Mundhygiene anzuwenden, und eine Reihe von Maßnahmen, die regelmäßig in der Praxis stattfinden.',
             pts=['Vorsorge für die ganze Familie', 'Beratung zu Ernährung und Mundhygiene', 'Ein ständig fortgebildetes Team'], btn='Prophylaxe anfragen', pop='Vorsorge für die ganze Familie.'),
    team=dict(ey='Die Praxis', h2='Herzlich willkommen <em>in der Lessingstraße.</em>', img=PX + '2584260.jpg', cap='Symbolbild', mw=600,
              paras=['Dr. Lutz Franke und Dr. Karin Franke begrüßen Sie mit ihrem Team in Meppen.',
                     'Rezensionen loben vor allem die Menschlichkeit und das aufmerksame Zuhören.'],
              tl=[('Meppen', 'Lessingstraße 12'), ('5,0', 'bei Google')]),
    stimmen=['Beide Zahnärzte sind sehr kompetent und leisten hervorragende Arbeit.', 'Frau Dr. Franke ist sehr einfühlsam und hört aufmerksam zu.', 'Seit Jahren Patient. Das Team ist freundlich und kompetent.'],
    hours=[('Mo, Do', '8–12 · 14–18 Uhr'), ('Di, Mi, Fr', '8–12 Uhr'), ('Hinweis', 'Zeiten laut Google')], cats=['pzr', 'akut', 'ersatz', 'aest', 'kind', 'angst'], bot='Franka', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe', 'Vorsorge ist das wichtigste Anliegen der Praxis.'], 'ersatz': ['Implantate', 'Die Praxis berät Sie zu Implantaten und Zahnersatz.'], 'aest': ['Ästhetik', 'Was zu Ihren Zähnen passt, klärt die Beratung.'],
         'kind': ['Kieferorthopädie', 'Kinderzahnheilkunde und Zahnregulierung gehören zum Angebot.'], 'angst': ['Kontrolltermin', 'Rezensionen heben das einfühlsame Zuhören hervor. Sagen Sie es gleich am Telefon.']},
    pops=[('h1.jpg', 'Implantate', 'Fester Ersatz, verankert im Kiefer.'), ('tm.jpg', 'Akupunktur', 'Ohrakupunktur in der Praxis.')]))

# 10 ─ Zahnarztpraxis Dr. Carolin Degener, Friesoythe
mk('degener', dict(slug='zahnarztpraxis-dr-degener-friesoythe', firma='Zahnarztpraxis Dr. Carolin Degener', kurz='Praxis Dr. Degener', name='Dr. Carolin Degener', ort='Friesoythe', strasse='Bookgastweg 67', plz='26169',
    tel='04491 9330499', tel_i='+4944919330499', web='zahnarztpraxis-dr-carolin-degener.de', p='#5f8418', dk='#2f3d14', s2='#f1f6e4', fam=RAL, fonts='r18ant',
    logo_txt='Zahnarztpraxis<small>Dr. Carolin Degener · Friesoythe</small>', hero='team', himgs=[I20('degener', '031'), I20('degener', '031')],
    ey='Zahnarztpraxis Dr. Degener · Friesoythe', h1='Wir erhalten <em>Ihr Lächeln.</em>',
    sub='Eine moderne Zahnarztpraxis mit umfassendem Behandlungsspektrum, in komfortabler Umgebung und besonders auf kleine Patienten vorbereitet.',
    ubar=[('Seit 2018', 'am Bookgastweg'), ('Für Kinder', 'vorbereitet'), ('Di und Do', 'bis 19 Uhr')],
    sv_h2='Alle Bereiche <em>der Zahnmedizin.</em>', sv_lead='Fortgeschrittene Diagnostik und Behandlung von Zahn- und Munderkrankungen, einschließlich Prophylaxe.',
    svcs=[('Prophylaxe', 'Vorsorge für Kinder und Erwachsene.'),
          ('Diagnostik', 'Moderne zahnmedizinische Geräte für eine genaue Untersuchung.'),
          ('Zahnerhaltung', 'Behandlung von Zahn- und Munderkrankungen.'),
          ('Kinderbehandlung', 'Die Praxis ist besonders auf kleine Patienten vorbereitet.'),
          ('Beratung', 'Wir nehmen uns Zeit für Ihre Fragen.')],
    top=dict(nav='Kinder', tag='Für kleine Patienten', h2='Auch die Kleinen <em>sind bei uns gut aufgehoben.</em>', img=I20('degener', '004'),
             txt='Mit modernen Geräten und in einer komfortablen Umgebung sind wir vor allem auch auf kleine Patienten vorbereitet.',
             pts=['Komfortable Umgebung', 'Moderne Geräte', 'Ein eingespieltes Team'], btn='Termin anfragen', pop='Komfortabel, modern, auch für Kinder.'),
    team=dict(ey='Die Zahnärztin', h2='Dr. Carolin Degener, <em>seit 2003 in Friesoythe.</em>', img=I20('degener', '010'), cap='Dr. Carolin Degener', mw=420,
              paras=['Approbation 1994, Promotion 1996. Nach Jahren als angestellte Zahnärztin in Bad Zwischenahn und Oldenburg ließ sie sich 2003 in Friesoythe nieder.',
                     'Im Juli 2018 gründete sie die eigene Praxis am Bookgastweg 67.'],
              tl=[('2003', 'in Friesoythe'), ('2018', 'eigene Praxis')]),
    gal=[(I20('degener', '002'), '50% 50%'), (I20('degener', '015'), '50% 50%'), (I20('degener', '017'), '50% 50%')],
    stimmen=['Ein sehr freundliches und kompetentes Team. Ich fühle mich in guten Händen.', 'Im Urlaub als Notfall gekommen und gut versorgt worden.', 'Keine Schmerzen, weder bei noch nach der Behandlung.'],
    hours=[('Mo', '8–12.30 · 14.30–17 Uhr'), ('Di, Do', '8–12.30 · 14–19 Uhr'), ('Mi, Fr', '8–12.30 Uhr')], cats=['pzr', 'kind', 'akut', 'ersatz', 'aest', 'angst'], bot='Dega', notfall=GEN_NF,
    rec={'pzr': ['Prophylaxe', 'Prophylaxe gehört fest zum Angebot.'], 'kind': ['Kinderbehandlung', 'Die Praxis ist besonders auf kleine Patienten vorbereitet.'], 'ersatz': ['Beratung', 'Am besten im Beratungsgespräch klären, was für Sie passt.'],
         'aest': ['Beratung', 'Was möglich ist, bespricht die Praxis mit Ihnen.'], 'angst': ['Kontrolltermin', 'Sagen Sie es am Telefon. Das Team nimmt sich Zeit.']},
    pops=[('h1.jpg', 'Abendtermine', 'Dienstag und Donnerstag bis 19 Uhr.'), ('tm.jpg', 'Prophylaxe', 'Vorsorge für Kinder und Erwachsene.')]))
