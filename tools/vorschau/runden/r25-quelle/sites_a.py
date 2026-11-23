"""Runde 25 · Augenoptiker und Hörakustiker 60 km um Bersenbrück. Nur Texte, Logos und Fotos der Betriebe.
Hörgeräte sind Medizinprodukte: keine Heilversprechen, keine erfundenen Ergebnisse."""
from common import *
SITES = {}
PX = '/home/claude/pixa20/'
R = '/home/claude/r24raw/'
KO = R + 'komp/'
OS = ('"Open Sans",system-ui,sans-serif',) * 2; NOTO = ('"Noto Sans",system-ui,sans-serif',) * 2; LATO = ('"Lato",system-ui,sans-serif',) * 2
NUN = ('"Nunito Sans",system-ui,sans-serif',) * 2; RAL = ('"Raleway",system-ui,sans-serif',) * 2; ASAP = ('"Asap",system-ui,sans-serif',) * 2
MONT = ('"Montserrat",system-ui,sans-serif', '"Source Sans 3",system-ui,sans-serif')

CATL = {'brille': 'Ich brauche eine neue Brille', 'gleit': 'Gleitsicht oder Lesebrille', 'kl': 'Kontaktlinsen', 'sehtest': 'Sehtest machen', 'hoer': 'Ich höre schlechter', 'hg': 'Service für mein Hörgerät', 'kind': 'Brille für mein Kind', 'rep': 'Brille kaputt', 'ring': 'Trauringe oder Schmuck', 'mobil': 'Beratung bei mir zu Hause', 'iem': 'Gehörschutz oder In-Ear', 'tinn': 'Ohrgeräusche (Tinnitus)'}
USP = {'zeit': 'Sagen Sie am Telefon ruhig, dass Sie sich Zeit für ein Gespräch wünschen.', 'sanft': 'Sprechen Sie Ihre Sorge offen an. Das Team geht darauf ein.',
       'schnell': 'Am schnellsten geht es per Telefon.', 'klar': 'Fragen Sie nach, bis alles klar ist. Dafür ist das Beratungsgespräch da.'}

def anliegen(s, cats):
    b = ''.join(f'<a href="#kontakt" data-check="{k}">{CATL[k]}</a>' for k in cats)
    return f'<section class="an20"><div class="w"><p>Worum geht es bei Ihnen?</p><div>{b}</div></div></section>'

def notfall(s, txt):
    return f'<section class="nf20"><div class="w"><div><b>{s.get("nf_t","Brille kaputt?")}</b><span>{txt}</span></div><a class="btn" href="tel:{s["tel_i"]}">{PH}{s["tel"]}</a></div></section>'

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
.promo figure img{aspect-ratio:auto!important;height:auto}.promo figure{max-width:var(--prmw,100%)}.pop.side img{height:auto!important;aspect-ratio:auto;max-height:230px;object-fit:cover}.chip20 i{font-style:normal}.chip20 .sm{display:none}.st5{display:inline-block;letter-spacing:2px;background:linear-gradient(90deg,#f5a500 var(--r,100%),#d5d9e2 var(--r,100%));-webkit-background-clip:text;background-clip:text;color:transparent!important;-webkit-text-fill-color:transparent}.chip20 .st{font-size:19px}.lot{bottom:76px}.lot-b{padding:8px 22px 8px 8px}.lot-b .dock{width:62px;height:62px}.lot-b .lb b{font-size:17px}.lot-b .lb small{font-size:12.5px}.lot-s{position:absolute;right:calc(100% + 14px);bottom:10px;width:max-content;max-width:min(300px,calc(100vw - 110px));background:#fff;color:#141a28;border:0;border-radius:18px 18px 4px 18px;padding:13px 16px;font:600 14.5px/1.4 var(--fb);text-align:left;cursor:pointer;box-shadow:0 16px 40px rgba(6,10,22,.26);transition:opacity .4s,transform .4s}.lot-s b{color:color-mix(in srgb,var(--p) 80%,#000)}.lot-s.off,.lot.open .lot-s,.lot:not(.hide-t) .lot-s{opacity:0;transform:translateX(12px);pointer-events:none}html,body{max-width:100%;overflow-x:clip}@media(max-width:900px){section :where(div,figure,ul,ol,li,form,article,a,p,h1,h2,h3,h4,label),header :where(div,a,nav,span){min-width:0}:where(h1,h2,h3,h4,p,li,small,b,label,figcaption){overflow-wrap:break-word}.btn{white-space:normal!important;max-width:100%;box-sizing:border-box}section img,section video,section iframe{max-width:100%}header .lt-logo{font-size:16px;overflow-wrap:anywhere}footer :where(div,a,p,span,small,b),.ft :where(div,a,p,span,small,b){min-width:0;max-width:100%}.lt-logo small{white-space:normal!important;overflow-wrap:anywhere;letter-spacing:.08em}header img{max-width:58vw;height:auto;object-fit:contain}}@media(max-width:900px){.hz{display:grid!important;grid-template-columns:minmax(0,1fr)!important}.hz>*,.hz-tx,.hz-tx .in,.ht20 .w,.ht20 .w>*,.hp .w>*{min-width:0!important;max-width:100%!important;box-sizing:border-box}.hz h1,.ht20 h1,.hz .sub,.ht20 .sub,.hz .ey,.ht20 .ey{overflow-wrap:break-word!important;max-width:100%}.hz-ub,.ub{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:6px 16px!important}.hz-ub div,.ub div{min-width:0;overflow-wrap:anywhere;hyphens:auto;font-size:13.5px}.hz-ub b,.ub b{font-size:17px!important;overflow-wrap:anywhere;hyphens:auto}.ctas{flex-wrap:wrap!important}.ctas .btn{max-width:100%;white-space:normal}.chip20{white-space:normal!important;max-width:100%;box-sizing:border-box}.chip20 b,.chip20 .st,.chip20 .sm{white-space:nowrap;flex:none}}@media(max-width:820px){.chip20 .lg{display:none}.chip20 .sm{display:inline!important}.chip20{max-width:100%;font-size:13.5px!important;white-space:nowrap;padding:9px 14px 9px 12px!important;gap:8px!important}.chip20 b{font-size:17px!important}.chip20 .st{font-size:16px!important}.lot{bottom:134px}.lot-b{padding:5px}.lot-b .dock{width:54px;height:54px}.lot-s{font-size:13.5px;padding:11px 13px;bottom:4px}}.chip20{display:inline-flex!important;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:10px 18px 10px 14px;box-shadow:0 8px 26px rgba(0,0,0,.10);font:600 15.5px var(--fb);margin-bottom:18px}.chip20 b{font:800 20px var(--fh)}.chip20 .st{color:#f5a500;letter-spacing:1px;font-size:17px}
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
        b = t + anliegen(s, cats) + marquee([a for a, _ in svcs] + [d.get('mq_end', f'Augenoptik in {ort}')], 'wm')
        if g('stimmen'): b += reviews_ns(s, d['stimmen'], cls='alt', h2='Das sagen <em>unsere Kunden.</em>')
        if g('video_first'): b += d['video_first']
        b += svc('leistungen', 'Leistungen', d['sv_h2'], d['sv_lead'], svcs[:6])
        b += promo('fokus', 'pr.jpg', top['tag'], top['h2'], top['txt'], top['pts'], top['btn'], 'alt')
        if g('zwei'):
            z = d['zwei']; b += eltern('zwei', 'el.jpg', z['ey'], z['h2'], z['txt'], z['pts'], z['btn'], rev=True)
        b += ablauf('weg', 'So läuft es ab', 'Termin machen, messen, <em>gut beraten.</em>', 'So einfach kommen Sie zu uns.', [
            ('Termin vereinbaren', f'Rufen Sie an unter {s["tel"]} oder schreiben Sie uns über das Formular. Sagen Sie kurz, worum es geht.'),
            ('In Ruhe ankommen', d.get('ab2', 'Bringen Sie Ihre aktuelle Brille mit, wenn Sie eine haben. Wir nehmen uns Zeit für Ihre Fragen.')),
            ('Messen und beraten', d.get('ab3', 'Wir messen genau und zeigen Ihnen, was zu Ihnen passt. Sie entscheiden in Ruhe.'))])
        tm = d['team']
        b += teamsec('ueber', tm['ey'], tm['h2'], tm['paras'], 'tm.jpg', tm['cap'], tm['tl'], cls='dk', mw=tm.get('mw'))
        if g('gal'): b += gal20('praxis', 'Einblicke', d.get('gal_h2', 'Ein Blick in <em>unser Geschäft.</em>'), [(f'g{i+1}.jpg', pos) for i, (_, pos) in enumerate(d['gal'])])
        if g('video'): b += d['video']
        b += notfall(s, d['notfall']) + contact(s)
        b += pops20([('pr.jpg', 'Bei uns im Geschäft', top['tag'], top['pop'], 'Termin anfragen')] + [(im, 'Bei uns im Geschäft', a, tx, 'Termin anfragen') for im, a, tx in d['pops']])
        return b + footer(s)
    opts = [a for a, _ in svcs] + ['Sonstiges']
    S = SITES[k] = site(
        slug=d['slug'], firma=d['firma'], web=d['web'], fonts=d['fonts'], branche=d.get('branche', 'Augenoptik'),
        title=f'{d["firma"]} – {d.get("tt", "Ihr Optiker")} in {ort}', desc=f'{d["firma"]} in {ort}: ' + ', '.join(a for a, _ in svcs[:5]) + '.',
        tel=d['tel'], tel_i=d['tel_i'], mail=g('mail', ''), adresse=f'{d["strasse"]}, {d["plz"]} {ort}', google=g('google'),
        cta='Termin anfragen', nav=[('Leistungen', 'leistungen'), (top['nav'], 'fokus'), ('Ablauf', 'weg'), (d.get('ueber_nav', 'Über uns'), 'ueber'), ('Kontakt', 'kontakt')],
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
    S['nf_t'] = d.get('nf_t', 'Brille kaputt?')
    S['bot'] = dict(auto=False, say=f'Hallo, ich bin <b>{d["bot"]}</b>, Ihr KI-Assistent. Ich führe Sie durch die Website.', name=d['bot'], tag=d.get('bot_tag', 'Ihr Seh-Lotse'), du=False, tel=d['tel'], tel_i=d['tel_i'], notfall=nf, finBtn='Termin anfragen',
        hello=f'Guten Tag! Ich bin <b>{d["bot"]}</b>, der digitale Lotse von {d["kurz"]}. Soll ich Ihnen helfen, schnell das Richtige zu finden?',
        hi=f'Guten Tag, ich bin {d["bot"]}. Ich stelle Ihnen drei kurze Fragen und zeige Ihnen, was hier zu Ihrem Anliegen passt.',
        cats=[[CATL[c], c] for c in cats], rec=rec, usp=USP, ex='Öffnungszeiten, Leistungen oder Terminen',
        qa=[['zeit|geöffnet|sprech|offen|öffnung', 'Die Öffnungszeiten: ' + ', '.join(f'{a} {b}' for a, b in d['hours']) + '.'],
            ['wo|adresse|anfahrt|park', f'Sie finden uns hier: {d["strasse"]}, {d["plz"]} {ort}.'],
            ['leistung|angebot|macht ihr|bieten', 'Zum Beispiel: ' + ', '.join(a for a, _ in svcs[:6]) + '.'],
            ['kind|sohn|tochter', rec.get('kind', ['', 'Auch Kinder sind willkommen. Am besten kurz anrufen.'])[1]],
            ['kasse|krankenkasse|zuzahlung|kosten|preis', 'Das hängt von Ihrem Bedarf ab. Am besten fragen Sie direkt im Geschäft, dort bekommen Sie eine ehrliche Auskunft.']],
        tour=[['#leistungen', 'Das finden Sie hier.'], ['#fokus', f'Ein Schwerpunkt: {top["tag"]}.'], ['#weg', 'So läuft Ihr Termin ab.'], ['#ueber', 'Hier lernen Sie das Team kennen.'], ['#kontakt', 'Und hier fragen Sie Ihren Termin an.']])
    im = {'h1.jpg': (d['himgs'][0], 0), 'h2.jpg': (d['himgs'][1], 0), 'pr.jpg': (top['img'], 0), 'tm.jpg': (d['team']['img'], 0)}
    if g('logo'): im['logo.png'] = d['logo']
    if g('zwei'): im['el.jpg'] = (d['zwei']['img'], 0)
    for i, (src, _) in enumerate(g('gal', [])): im[f'g{i+1}.jpg'] = (src, 0)
    for x in g('extra_img', {}).items(): im[x[0]] = x[1]
    S['img'] = im; S['body'] = body

GEN_NF = 'Kommen Sie einfach vorbei oder rufen Sie kurz an. Kleine Reparaturen erledigen wir meist sofort.'
HG_NF = 'Hörgerät pfeift oder ist leise? Kommen Sie vorbei, Reinigung und kleine Hilfe gehen meist sofort.'
def I20(k, n):
    import glob
    f = glob.glob(f'{R}{k}/img/i{n}.*'); assert f, (k, n); return f[0]



def J(k, n): return I20(k, n)
SIG = ('"Lato",system-ui,sans-serif',) * 2

# 1 ─ Rapin Augenoptik & Hörakustik, Quakenbrück
mk('rapin', dict(ab2='Bringen Sie Ihre aktuelle Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit für Ihre Fragen.', google=(4.9, 181), slug='rapin-augenoptik-hoerakustik-quakenbrueck', firma='Rapin Augenoptik & Hörakustik', kurz='Rapin', name='Wiebke Rapin-Rohe', ort='Quakenbrück', strasse='Lange Straße 46', plz='49610',
    tel='05431 3635', tel_i='+4954313635', mail='info@rapin-quakenbrueck.de', web='rapin-quakenbrueck.de', p='#e4022e', dk='#2a2a2e', s2='#f7f3f2', fam=LATO, fonts='r10vagts', branche='Augenoptik und Hörakustik', tt='Augenoptik und Hörakustik',
    logo=(J('rapin', '000'), 0), lh=56, hero='team', himgs=[J('rapin', '003'), J('rapin', '003')],
    ey='Augenoptik & Hörakustik · Quakenbrück', h1='Mit allen Sinnen <em>für Sie da.</em>',
    sub='Seit 1850 vertrauen Kunden in Quakenbrück auf unser Handwerk. Heute berät Sie die sechste Generation, mit eigener Meisterwerkstatt für Brillen und Hörgeräte.',
    ubar=[('Seit 1850', 'Familienbetrieb'), ('6. Generation', 'Wiebke Rapin-Rohe'), ('Meisterwerkstatt', 'im eigenen Haus')],
    sv_h2='Sehen und hören. <em>Aus einer Hand.</em>', sv_lead='Unser Team berät Sie in Optik und Akustik: zuhörend, einfühlsam und mit der richtigen Idee für Sie.',
    svcs=[('Brillen und Gleitsicht', 'Typberatung, internationale Marken und Fertigung in der eigenen Werkstatt. Mit ZEISS i.Profiler plus vermessen.'),
          ('Hörgeräte', 'Ausführlicher Hörtest, Probetragen und Anpassung mit Geräten namhafter Hersteller.'),
          ('Kontaktlinsen', 'Individuelle Anpassung, auch bei starker Sehschwäche.'),
          ('Kinderbrillen und Sonnenbrillen', 'Robuste Kinderbrillen und Sonnenbrillen, auch mit Ihrer Stärke.'),
          ('Arbeitsplatzbrillen', 'Professionelle Sehberatung für den Bildschirmarbeitsplatz.'),
          ('Reparatur-Service', 'Brillen und Hörgeräte reparieren wir im Haus, ohne lange Wege.')],
    top=dict(nav='Hören', tag='Hörakustik', h2='Gutes Hören ist <em>ein Stück Lebensqualität.</em>', img=J('rapin', '004'),
             txt='Gespräche wieder mühelos verstehen, Musik genießen, Vögel zwitschern hören: Wir nehmen uns Zeit für Ihren Hörtest und finden das Hörsystem, das zu Ihrem Alltag passt. Meisterin Wiebke Rapin-Rohe ist Hörakustik- und Augenoptikermeisterin.',
             pts=['Ausführlicher Hörtest ohne Wartezeit', 'Probetragen im Alltag', 'Service und Reparatur im eigenen Haus'], btn='Hörtest-Termin anfragen', pop='Hörtest, Probetragen und Service unter einem Dach.'),
    zwei=dict(ey='Augenoptik', h2='Die Brille, <em>die zu Ihnen passt.</em>', img=J('rapin', '019'),
              txt='Die Brille ist längst ein Modeaccessoire. Wir beraten typgerecht, vermessen Ihre Augen mit modernster Technik und fertigen Ihre Brille in unserer Werkstatt.',
              pts=['Detaillierte Augenprüfung', 'ZEISS i.Profiler plus', 'Kostenloser Brillencheck'], btn='Brillen-Beratung anfragen'),
    team=dict(ey='Seit 1850', h2='Ein echter Familienbetrieb <em>mitten in Quakenbrück.</em>', img=J('rapin', '006'), cap='Das Haus von Rapin an der Langen Straße',
              paras=['Seit 1850 vertrauen Kunden auf unsere handwerkliche Perfektion und unser Gefühl für guten Stil. Mit Hörakustik- und Augenoptikermeisterin Wiebke Rapin-Rohe freut sich die sechste Generation auf Sie.',
                     'An ihrer Seite steht ein geschultes Team und eine hauseigene Meisterwerkstatt für die zeitnahe Herstellung und Reparatur von Brillen und Hörgeräten.'],
              tl=[('1850', 'gegründet'), ('6.', 'Generation')]),
    gal=[(J('rapin', '005'), '50% 50%'), (J('rapin', '016'), '50% 50%'), (J('rapin', '018'), '50% 50%')],
    hours=[('Mo bis Fr', '9–13 · 14.30–18 Uhr'), ('Sa', '9–13 Uhr')], cats=['brille', 'gleit', 'hoer', 'hg', 'kl', 'rep'], bot='Rina', notfall=GEN_NF, mq_end='Augenoptik und Hörakustik in Quakenbrück',
    rec={'brille': ['Brillen und Gleitsicht', 'Typberatung und Fertigung in der eigenen Werkstatt.'], 'gleit': ['Brillen und Gleitsicht', 'Die Gleitsichtgläser werden mit ZEISS-Technik vermessen.'], 'hoer': ['Hörgeräte', 'Am besten mit einem Hörtest anfangen. Den gibt es ohne lange Wartezeit.'],
         'hg': ['Reparatur-Service', 'Kommen Sie vorbei. Reinigung und Reparatur gibt es im eigenen Haus.'], 'kl': ['Kontaktlinsen', 'Kontaktlinsen werden individuell angepasst.'], 'rep': ['Reparatur-Service', 'Die meisten Reparaturen erledigt die eigene Werkstatt.']},
    pops=[('el.jpg', 'Augenoptik', 'Typberatung und Brillen aus der eigenen Werkstatt.'), ('g2.jpg', 'Kostenloser Brillencheck', 'Kommen Sie vorbei, wir prüfen Ihre Brille.')]))

# 2 ─ Sabine Welling HörSysteme, Wietmarschen-Lohne
mk('welling', dict(google=(4.9, 23), slug='welling-hoersysteme-wietmarschen', firma='Sabine Welling HörSysteme', kurz='Welling HörSysteme', name='Sabine Welling', ort='Wietmarschen-Lohne', strasse='Hauptstraße 36', plz='49835',
    tel='05908 9371750', tel_i='+4959089371750', mail='info@welling-hoersysteme.de', web='welling-hoersysteme.de', p='#e30613', dk='#232323', s2='#f6f3f3', fam=OS, fonts='r16ellers', branche='Hörakustik', tt='Ihr Hörakustiker', bot_tag='Ihr Hör-Lotse', nf_t='Hörgerät macht Probleme?',
    logo_txt='Sabine Welling<small>HörSysteme · Das Leben klingt schön</small>', hero='team', himgs=[J('welling', '001'), J('welling', '001')],
    ey='Hörakustik-Meisterin · Wietmarschen-Lohne und Emlichheim', h1='Das Leben <em>klingt schön.</em>',
    sub='Über 30 Jahre Fachkompetenz und ein Netzwerk aus Experten bereiten Ihnen den Weg zum guten Hören. Persönlich, kompetent und immer aktuell.',
    ubar=[('30+ Jahre', 'Erfahrung'), ('2 Fachgeschäfte', 'Lohne und Emlichheim'), ('Audiotherapeutin', 'zertifiziert')],
    sv_h2='Alles rund ums <em>gute Hören.</em>', sv_lead='Ob Sie gerade überlegen oder schon lange Hörsysteme tragen: Wir sind an Ihrer Seite.',
    svcs=[('Hörtest', 'Eine kurze Messung schafft Gewissheit. Danach erklären wir die nächsten Schritte.'),
          ('Hörsysteme', 'Moderne Hörgeräte, die sich auch kabellos mit Handy und Fernseher verbinden.'),
          ('In-Ear-Monitoring', 'Maßgefertigte In-Ears für Musiker, mit eigener Fachkraft.'),
          ('Gehörschutz', 'Individueller Gehörschutz für Arbeit, Freizeit und Musik.'),
          ('Implantat-Akustik', 'Zertifizierte Betreuung von Trägern von Hörimplantaten.'),
          ('Service', 'Reinigung, Nachanpassung und Batterien, ganz ohne lange Wartezeit.')],
    top=dict(nav='Hörtest', tag='Ein Hörtest schafft Gewissheit', h2='Erst messen, <em>dann entscheiden.</em>', img=J('welling', '038'),
             txt='Eine kurze Messung in unseren Fachgeschäften zeigt, wie es um Ihr Gehör steht: Reicht Gehörschutz? Kommt eine leichte Versorgung in Frage? Welche Bauform passt zu Ihnen? Diese Fragen beantworten wir in einem persönlichen Gespräch.',
             pts=['Persönlicher Einzeltermin', 'Ergebnis aus Expertensicht', 'Kein Druck, keine Verpflichtung'], btn='Hörtest-Termin anfragen', pop='Ein Hörtest schafft Gewissheit. Vereinbaren Sie Ihren Einzeltermin.'),
    zwei=dict(ey='Für Musiker', h2='In-Ear-Monitoring <em>nach Maß.</em>', img=J('welling', '011'),
              txt='Drummer, Sänger, Gitarristen: Wir fertigen individuelle Ohrabdrücke und passen In-Ear-Systeme und Gehörschutz für die Bühne an. Mit eigener Fachkraft für In-Ear-Monitoring.',
              pts=['Präzise Ohrabdrücke', 'Gehörschutz für Musiker', 'Fachkraft für In-Ear-Monitoring'], btn='In-Ear-Beratung anfragen'),
    team=dict(ey='Über uns', h2='Seit über 10 Jahren <em>für Ihr gutes Hören da.</em>', img=J('welling', '010'), cap='Das Fachgeschäft in Wietmarschen-Lohne',
              paras=['Hörakustik-Meisterin Sabine Welling hat sich in Wietmarschen-Lohne selbstständig gemacht. Schnell wurde das Geschäft eine feste Adresse rund um gutes Hören, später kam ein zweites Fachgeschäft in Emlichheim dazu.',
                     'Für ihr Projekt „Ziemlich beste Verbindung“ erhielt Sabine Welling den „future hearing award“.'],
              tl=[('Lohne', 'Hauptstraße 36'), ('Emlichheim', 'zweites Geschäft')]),
    gal=[(J('welling', '002'), '50% 50%'), (J('welling', '011'), '50% 50%'), (J('welling', '004'), '50% 50%')],
    stimmen=['Hervorragende Beratung, sehr freundliche und kompetente Betreuung. Probleme werden sofort angegangen.', 'Oma kann endlich wieder an Gesprächen teilnehmen. Ruhe, Mühe und Geduld sind wirklich lobenswert.', 'Als Drummer bin ich für meine In-Ear-Monitore hierhin gekommen. Besser geht es nicht.'],
    hours=[('Mo, Di, Do, Fr', '9–12.30 · 15–18 Uhr'), ('Mi', '9–12.30 Uhr')], cats=['hoer', 'hg', 'iem', 'tinn'], bot='Sina', notfall=HG_NF, mq_end='Hörakustik in Wietmarschen-Lohne',
    ab2='Bringen Sie Ihr Hörgerät mit, wenn Sie schon eins tragen. Wir nehmen uns Zeit für Ihre Fragen.', ab3='Wir messen Ihr Gehör und erklären das Ergebnis. Sie entscheiden in Ruhe.',
    rec={'hoer': ['Hörtest', 'Am besten mit einem Hörtest anfangen. Den machen wir im Einzeltermin.'], 'hg': ['Service', 'Reinigung und Nachanpassung gibt es ohne lange Wartezeit.'], 'iem': ['In-Ear-Monitoring', 'Für Musiker gibt es eine eigene Fachkraft für In-Ears und Gehörschutz.'], 'tinn': ['Hörtest', 'Sprechen Sie es im Termin an. Wir hören zu und beraten Sie ehrlich.']},
    pops=[('el.jpg', 'Für Musiker', 'In-Ear-Monitoring und Gehörschutz nach Maß.'), ('g1.jpg', 'Hörsysteme', 'Moderne Hörgeräte, kabellos vernetzt.')]))

# 3 ─ Arthur Müller, Vechta
mk('mueller', dict(ab2='Bringen Sie Ihre aktuelle Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit für Ihre Fragen.', google=(4.6, 11), slug='arthur-mueller-vechta', firma='Arthur Müller', kurz='Arthur Müller', name='Familie Müller', ort='Vechta', strasse='Große Straße 69', plz='49377',
    tel='04441 2391', tel_i='+4944412391', mail='info@arthur-mueller.de', web='arthur-mueller.de', p='#002e55', dk='#0d2236', s2='#f5f1ea', em='#9a7b45', fam=RAL, fonts='r18ant', branche='Augenoptik, Hörakustik und Juwelier', tt='Brillen, Hörgeräte und Schmuck',
    logo_txt='Arthur Müller<small>Seit 1919 · Besser hören. Besser sehen.</small>', hero='r', himgs=[J('mueller', '012'), J('mueller', '012')], cols='54fr 46fr', card='1/1',
    ey='Familienunternehmen seit 1919 · Vechta, Lohne, Visbek', h1='Besser sehen. Besser hören. <em>Seit 1919.</em>',
    sub='Unser Haus wird in der vierten Generation geführt. Neben Uhren und Schmuck haben wir uns auf Brillen und Hörgeräte spezialisiert, mit eigenen Teams und moderner Messtechnik.',
    ubar=[('Seit 1919', 'Familienunternehmen'), ('4. Generation', 'Familie Müller'), ('4 Standorte', 'Vechta, Lohne, Visbek')],
    sv_h2='Alles für Augen, Ohren <em>und schöne Momente.</em>', sv_lead='Höchste Qualität, ehrliche Beratung und Liebe zum Detail.',
    svcs=[('Hörgeräte', 'Moderne Hörakustik, individuell und unabhängig, im Hörgeräteinstitut im Alexanderhaus.'),
          ('Brillen', 'Präzise Sehstärkenbestimmung und eine große Auswahl an Fassungen.'),
          ('Trauringe', 'Individuelle Eheringe, gestaltet mit unserem Konfigurator und Fachpersonal.'),
          ('Uhren', 'Große Auswahl und Uhrmacher-Meisterwerkstatt für Service und Reparatur.'),
          ('Schmuck', 'Schmuckstücke, die Ihre Geschichte erzählen.'),
          ('Goldankauf', 'Faire Bewertung Ihres Altgolds.')],
    top=dict(nav='Hörgeräte', tag='Hörakustik', h2='Moderne Hörakustik, <em>individuell und unabhängig.</em>', img=J('mueller', '004'),
             txt='Im Hörgeräteinstitut im Alexanderhaus in Vechta und in unseren Filialen nehmen sich spezialisierte Hörakustiker Zeit für Sie. Mit neuester Technologie bestimmen wir genau, welche Hörhilfe zu Ihnen passt.',
             pts=['Spezialisiertes Team', 'Moderne Messtechnik', 'In Vechta, Lohne und Visbek'], btn='Hörberatung anfragen', pop='Hörakustik im Alexanderhaus in Vechta.'),
    zwei=dict(ey='Trauringe', h2='Ihre Eheringe, <em>ganz nach Wunsch.</em>', img=J('mueller', '018'),
              txt='Gestalten Sie mit unserem Team und dem Konfigurator Ihr persönliches Paar Eheringe. Beim Kauf von Eheringen ab 2.000 Euro ist der Brautwagen für 3 Stunden inklusive.',
              pts=['Individuelle Gestaltung', 'Material und Steine frei wählbar', 'Brautwagen inklusive ab 2.000 Euro'], btn='Trauring-Beratung anfragen'),
    team=dict(ey='Über uns', h2='Familie Müller <em>freut sich auf Sie.</em>', img=J('mueller', '003'), cap='Arthur Müller an der Großen Straße in Vechta',
              paras=['Seit 1919 setzt unser Familienunternehmen auf höchste Qualität, ehrliche Beratung und Liebe zum Detail. Heute führen wir das Haus in der vierten Generation.',
                     'Für Brillen und Hörgeräte stehen Ihnen spezialisierte Teams mit modernen Präzisionsgeräten zur Verfügung.'],
              tl=[('1919', 'gegründet'), ('4.', 'Generation')]),
    gal=[(J('mueller', '001'), '50% 50%'), (J('mueller', '002'), '50% 50%'), (J('mueller', '004'), '50% 50%')], gal_h2='Unsere <em>Standorte.</em>',
    stimmen=['Sehr kompetent, unglaublich freundlich und immer entgegenkommend. Ob in Visbek oder Vechta.', 'Hervorragende Beratung. Unser Sohn fühlt sich sehr gut aufgehoben.', 'Sehr freundlicher Service und tolle individuelle Beratung.'],
    hours=[('Hörgeräte Vechta Mo, Di, Do, Fr', '8.30–13 · 14.30–18 Uhr'), ('Mi', '8.30–13 Uhr'), ('Hinweis', 'Zeiten der Filialen bitte erfragen')], cats=['hoer', 'hg', 'brille', 'ring'], bot='Arthur', notfall=GEN_NF, mq_end='Seit 1919 in Vechta',
    rec={'hoer': ['Hörgeräte', 'Das Hörgeräteinstitut im Alexanderhaus berät Sie persönlich.'], 'hg': ['Hörgeräte', 'Für Service am Hörgerät einfach vorbeikommen oder anrufen.'], 'brille': ['Brillen', 'Sehstärke wird präzise bestimmt, die Auswahl ist groß.'], 'ring': ['Trauringe', 'Eheringe gestalten Sie mit dem Team ganz nach Wunsch.']},
    pops=[('el.jpg', 'Trauringe', 'Ab 2.000 Euro Brautwagen inklusive.'), ('g1.jpg', 'Seit 1919', 'Vier Generationen Familie Müller.')]))

# 4 ─ Optik Mobil Meyer, Essen (Oldb.)
mk('mobilmeyer', dict(google=(5.0, 21), slug='optik-mobil-meyer-essen-oldenburg', firma='Optik Mobil Meyer', kurz='Optik Mobil Meyer', name='Karina Meyer', ort='Essen (Oldenburg)', strasse='Johannes-Gutenberg-Straße 14a', plz='49632',
    tel='05434 808631', tel_i='+495434808631', mail='info@optik-mobil-meyer.de', web='optik-mobil-meyer.de', p='#cc0d12', dk='#2a1c1c', s2='#f8f2f1', fam=NUN, fonts='r16galerie',
    logo=(R + 'komp/mobilmeyer-logo.png', 300), lh=60, hero='l', himgs=[J('mobilmeyer', '005'), J('mobilmeyer', '005')], cols='44fr 56fr', card='400/230',
    ey='Ihr Optiker in Essen (Oldenburg)', h1='Ihr Optiker. <em>Auch bei Ihnen zu Hause.</em>',
    sub='Große Brillenauswahl in jeder Preisklasse, Messung mit neuester Computertechnik und ein mobiler Service, der zu Ihnen kommt. Gerne auch abends oder am Wochenende.',
    ubar=[('100 m²', 'Ladenfläche seit 2023'), ('Mobil', 'zu Hause und im Betrieb'), ('Amtlich', 'anerkannte Sehteststelle')],
    sv_h2='Gutes Sehen, <em>so wie es Ihnen passt.</em>', sv_lead='Im Geschäft in Osteressen oder direkt bei Ihnen.',
    svcs=[('Brillen in jeder Preisklasse', 'Große Auswahl und individuelle Beratung.'),
          ('Mobiler Service', 'Wir kommen mit unserer Messeinrichtung zu Ihnen nach Hause.'),
          ('Arbeitsplatzbrillen', 'Sehstärke direkt am Arbeitsplatz bestimmen, auch für die G37.'),
          ('Führerschein-Sehtest', 'Amtlich anerkannte Sehteststelle für Lkw- und Busführerschein.'),
          ('Kontaktlinsen', 'Beratung und Anpassung.'),
          ('Myopie-Management', 'Gemeinsam die Kurzsichtigkeit bei Kindern eindämmen.')],
    top=dict(nav='Mobil', tag='Mobiler Service', h2='Der Weg zur neuen Brille <em>war noch nie so einfach.</em>', img=J('mobilmeyer', '076'),
             txt='Unseren Service für zu Hause bieten wir allen an, deren Mobilität eingeschränkt ist, und allen, die für einen normalen Optikerbesuch keine Zeit haben. Sie sind frei von Öffnungszeiten und haben alle Ruhe für die Auswahl.',
             pts=['Termin nach Ihren Wünschen', 'Präzise Sehtests mit neuester Technik', 'Auch abends und am Wochenende'], btn='Wunsch-Termin anfragen', pop='Wir kommen zu Ihnen. Auch abends und am Wochenende.'),
    zwei=dict(ey='Für Berufskraftfahrer', h2='Sehtest für den <em>Lkw- und Busführerschein.</em>', img=J('mobilmeyer', '077'),
              txt='Seit dem 18.08.2026 sind wir amtlich anerkannte Sehteststelle. Geprüft werden Sehschärfe, Farbsehen, Kontrast- und Dämmerungssehen, Gesichtsfeld und räumliches Sehen.',
              pts=['Klassen C, C1, C1E, D, D1, D1E', 'Auch für die Fahrgastbeförderung', 'Neu oder Verlängerung'], btn='Sehtest-Termin anfragen'),
    team=dict(ey='Über uns', h2='Karina Meyer <em>und ihr Team.</em>', img=J('mobilmeyer', '004'), cap='Das Geschäft in Osteressen', mw=400,
              paras=['Im Juli 2023 haben wir unsere Ladenfläche auf 100 Quadratmeter verdoppelt. Bei uns finden Sie eine große Brillenauswahl in jeder Preisklasse.',
                     'Kunden loben die Beratung, die faire Auswahl und dass wir auch Plattdeutsch sprechen.'],
              tl=[('2023', 'Laden vergrößert'), ('100 m²', 'Ladenfläche')]),
    gal=[(J('mobilmeyer', '076'), '50% 50%'), (J('mobilmeyer', '077'), '50% 50%'), (J('mobilmeyer', '006'), '50% 50%')],
    stimmen=['Sehr freundlich, gute Beratung, und man spricht auch Plattdeutsch.', 'Karina berät super, hat eine tolle Auswahl und ist sehr flexibel. Meine Tochter ist glücklich mit ihrer Brille.', 'Super Service, gute Preise, nettes Personal.'],
    hours=[('Mo bis Fr', '8.30–12.30 · 14–18 Uhr'), ('Sa', '9–13 Uhr'), ('Mobil', 'Termine auch abends und am Wochenende')], cats=['brille', 'mobil', 'sehtest', 'kind', 'kl', 'rep'], bot='Kari', notfall=GEN_NF, mq_end='Optiker in Essen (Oldenburg)',
    rec={'brille': ['Brillen in jeder Preisklasse', 'Große Auswahl, am besten mit Termin.'], 'mobil': ['Mobiler Service', 'Das Team kommt zu Ihnen, auch abends oder am Wochenende.'], 'sehtest': ['Führerschein-Sehtest', 'Auch für den Lkw- und Busführerschein.'],
         'kind': ['Myopie-Management', 'Für Kinderaugen gibt es eine eigene Beratung.'], 'kl': ['Kontaktlinsen', 'Beratung und Anpassung im Geschäft.'], 'rep': ['Brillen in jeder Preisklasse', 'Kommen Sie einfach vorbei.']},
    pops=[('el.jpg', 'Führerschein-Sehtest', 'Amtlich anerkannte Sehteststelle für Lkw und Bus.'), ('g3.jpg', 'Brillenmode', 'Große Auswahl in jeder Preisklasse.')]))

# 5 ─ Hörgeräte Steenweg, Nordhorn
mk('steenweg', dict(google=(4.5, 8), slug='hoergeraete-steenweg-nordhorn', firma='Hörgeräte Steenweg', kurz='Hörgeräte Steenweg', name='Stefanie Steenweg', ort='Nordhorn', strasse='Am Vechteufer 1', plz='48529',
    tel='05921 79303', tel_i='+49592179303', mail='info@hoergeraete-steenweg.de', web='hoergeraete-steenweg.de', p='#005285', dk='#1d2c33', s2='#eef3f6', fam=OS, fonts='r16ellers', branche='Hörakustik', tt='Ihr Hörakustiker', bot_tag='Ihr Hör-Lotse', nf_t='Hörgerät macht Probleme?',
    logo=(R + 'komp/steenweg-logo.png', 340), lh=40, hero='r', himgs=[R + 'komp/steenweg-team.jpg', R + 'komp/steenweg-team.jpg'], cols='50fr 50fr', card='1800/690',
    ey='Meisterbetrieb · Nordhorn, Schüttorf, Bad Bentheim', h1='Gut hören. <em>Mit Menschen, die zuhören.</em>',
    sub='Langjährige Erfahrung mit Hörgeräten, Pädakustik und Gehörschutz. Kostenloser Hörtest in unseren drei Fachgeschäften in der Grafschaft Bentheim.',
    ubar=[('Seit 1991', 'Meisterin'), ('3 Filialen', 'in der Grafschaft'), ('Pädakustik', 'für Kinder')],
    sv_h2='Rund um <em>das Hören.</em>', sv_lead='In Zusammenarbeit mit HNO-Ärzten, Uni-Kliniken und Krankenkassen.',
    svcs=[('Kostenloser Hörtest', 'Hörminderung früh erkennen, in allen drei Filialen.'),
          ('Hörgeräte', 'Beratung und Anpassung mit moderner Technik.'),
          ('Pädakustik', 'Hörversorgung für Kinder, mit Pädakustikerin.'),
          ('Tinnitus', 'Beratung und technische Versorgung bei Ohrgeräuschen.'),
          ('Gehörschutz', 'Individueller Gehörschutz nach Maß.'),
          ('Online-Hörtest', 'Ein erster Check bequem von zu Hause.')],
    top=dict(nav='Hörtest', tag='Kostenloser Hörtest', h2='Früh erkennen, <em>gut beraten.</em>', img=J('steenweg', '002'),
             txt='Mit unserem kostenlosen Hörtest in Nordhorn, Schüttorf und Bad Bentheim stellen wir eine Hörminderung frühzeitig fest und beraten Sie individuell. Ohne Verkaufsdruck, mit viel Zeit für Ihre Fragen.',
             pts=['In allen drei Filialen', 'Viel Zeit, kein Verkaufsdruck', 'Zusammenarbeit mit HNO-Ärzten'], btn='Hörtest-Termin anfragen', pop='Kostenloser Hörtest in Nordhorn, Schüttorf und Bad Bentheim.'),
    zwei=dict(ey='Kinder und Tinnitus', h2='Spezialisten für <em>die schwierigen Fälle.</em>', img=J('steenweg', '044'),
              txt='Inhaberin Stefanie Steenweg ist seit 1999 Pädakustikerin und versorgt seit 1998 Kunden mit Tinnitus. Ihr Team bildet sich laufend fort.',
              pts=['Pädakustik seit 1999', 'Tinnitusversorgung seit 1998', 'Hörluchs ICP-zertifiziert'], btn='Beratung anfragen'),
    team=dict(ey='Über uns', h2='Teamwork <em>für Ihr gutes Hören.</em>', img=J('steenweg', '001'), cap='Das Fachgeschäft in Nordhorn',
              paras=['1994 übernahm Hörgeräteakustik-Meisterin Stefanie Steenweg die Hörgeräteabteilung von Optik de Bloom in Nordhorn und Schüttorf. 1998 wurde daraus Hörgeräte Steenweg, 2007 kam Bad Bentheim dazu.',
                     'Bei uns steht der Mensch im Mittelpunkt. Wir möchten unsere Kunden so bedienen, dass sie uns gern weiterempfehlen.'],
              tl=[('1998', 'Hörgeräte Steenweg'), ('3', 'Fachgeschäfte')]),
    gal=[(J('steenweg', '003'), '50% 50%'), (J('steenweg', '007'), '50% 50%'), (J('steenweg', '006'), '50% 50%')],
    stimmen=['Vom ersten Besuch an gut aufgehoben. Fragen wurden geduldig beantwortet, es gibt keinen Verkaufsdruck.', 'Ich brauchte dringend Batterien und habe sogar eine Packung geschenkt bekommen.', 'Immer super freundlich und hilfsbereit.'],
    hours=[('Mo bis Fr', '8.30–12.30 · 14–18 Uhr'), ('Filialen', 'Zeiten in Schüttorf und Bad Bentheim bitte erfragen')], cats=['hoer', 'hg', 'tinn', 'iem'], bot='Stella', notfall=HG_NF, mq_end='Hörakustik in der Grafschaft Bentheim',
    ab2='Bringen Sie Ihr Hörgerät und, wenn vorhanden, die Verordnung vom HNO-Arzt mit.', ab3='Wir messen Ihr Gehör und erklären das Ergebnis. Sie entscheiden in Ruhe.',
    rec={'hoer': ['Kostenloser Hörtest', 'Den kostenlosen Hörtest gibt es in allen drei Filialen.'], 'hg': ['Hörgeräte', 'Kommen Sie vorbei. Das Team hilft schnell.'], 'tinn': ['Tinnitus', 'Für Ohrgeräusche gibt es eine eigene Beratung.'], 'iem': ['Gehörschutz', 'Gehörschutz wird nach Maß angepasst.']},
    pops=[('el.jpg', 'Pädakustik', 'Hörversorgung für Kinder mit Erfahrung seit 1999.'), ('g1.jpg', 'Drei Filialen', 'Nordhorn, Schüttorf und Bad Bentheim.')]))

# 6 ─ Auge und Ohr Motzek, Osnabrück
mk('motzek', dict(ab2='Bringen Sie Ihre aktuelle Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit für Ihre Fragen.', google=(4.8, 113), slug='auge-und-ohr-osnabrueck', firma='Auge und Ohr', kurz='Auge und Ohr', name='Auge und Ohr Motzek', ort='Osnabrück', strasse='Schützenstraße 1', plz='49084',
    tel='0541 2005960', tel_i='+495412005960', mail='info@augeundohr24.de', web='auge-und-ohr.com', p='#2a5a9a', dk='#16263b', s2='#eef2f7', em='#d0701f', fam=NUN, fonts='r16galerie', branche='Augenoptik und Hörakustik', tt='Optiker und Akustiker',
    logo=(J('motzek', '000'), 0), lh=34, hero='r', himgs=[J('motzek', '016'), J('motzek', '016')], cols='50fr 50fr', card='1600/1045',
    ey='Optiker und Akustiker · Schinkel, Nikolaiort, Krahnstraße, Belm', h1='Mehr hören. <em>Mehr sehen.</em>',
    sub='Ihr Optiker und Akustiker in Osnabrück-Schinkel, am Nikolaiort, in der Krahnstraße und in Belm. Mit optometrischer Untersuchung und Hörsystemen der neuesten Generation.',
    ubar=[('4 Standorte', 'Osnabrück und Belm'), ('Optometrie', 'ganzheitliche Augenkontrolle'), ('Sehen + Hören', 'aus einer Hand')],
    sv_h2='Gutes Sehen. <em>Gutes Hören.</em>', sv_lead='Ihre Wünsche stehen bei uns im Mittelpunkt.',
    svcs=[('Brillen', 'Aktuelle Brillenmode regionaler und internationaler Labels, auch für Kinder.'),
          ('Brillengläser', 'Einstärken-, Gleitsicht- und Arbeitsplatzgläser nach genauer Analyse.'),
          ('Kontaktlinsen', 'Tageslinsen, Monatslinsen, formstabil oder weich, je nach Einsatz.'),
          ('Optometrie', 'Augenkontrolle, Gesundheitsvorsorge und Low-Vision-Hilfen.'),
          ('Hörsysteme', 'Besseres Sprachverstehen, Hörkomfort und Konnektivität.'),
          ('Club und Service', 'Reparaturen, oft in wenigen Minuten erledigt.')],
    top=dict(nav='Optometrie', tag='Optometrische Untersuchung', h2='Mehr als <em>ein Sehtest.</em>', img=J('motzek', '015'),
             txt='Die optometrische Untersuchung verbindet die ganzheitliche Augenkontrolle mit der Gesundheitsvorsorge. Sie liefert einen umfassenden Überblick über Ihr Sehen, damit wir die perfekte Sehlösung für Sie finden.',
             pts=['Ganzheitliche Augenkontrolle', 'Low-Vision-Spezialhilfen', 'Zeit für eine eingehende Beratung'], btn='Termin zur Augenkontrolle anfragen', pop='Optometrie: die ganzheitliche Augenkontrolle.'),
    zwei=dict(ey='Hören', h2='Hörsysteme <em>der neuesten Generation.</em>', img=J('motzek', '007'),
              txt='Neben besserem Sprachverstehen zählen Hörkomfort und Konnektivität zu den wichtigsten Merkmalen moderner Hörsysteme. Wir beraten Sie persönlich.',
              pts=['Besseres Sprachverstehen', 'Hörkomfort im Alltag', 'Verbindung mit Handy und TV'], btn='Hörberatung anfragen'),
    team=dict(ey='Unsere Standorte', h2='Viermal für Sie da, <em>in Osnabrück und Belm.</em>', img=J('motzek', '013'), cap='Präzise Arbeit in der Werkstatt',
              paras=['Auge und Ohr finden Sie in Osnabrück-Schinkel, am Nikolaiort, in der Krahnstraße als Brillen Mohr und in Belm.',
                     'Viele Kunden kommen seit Kindertagen zu uns. Dafür sagen wir danke.'],
              tl=[('Schinkel', 'Schützenstraße 1'), ('113', 'Google-Bewertungen')]),
    gal=[(J('motzek', '045'), '50% 50%'), (J('motzek', '047'), '50% 50%'), (J('motzek', '046'), '50% 50%')], gal_h2='Ein Blick in <em>unsere Werkstatt.</em>',
    hours=[('Mo bis Fr', '9–18 Uhr (Schinkel)'), ('Weitere Standorte', 'Zeiten bitte erfragen')], cats=['brille', 'gleit', 'kl', 'sehtest', 'hoer', 'rep'], bot='Otto', notfall=GEN_NF, mq_end='Optiker und Akustiker in Osnabrück',
    rec={'brille': ['Brillen', 'Große Auswahl regionaler und internationaler Labels.'], 'gleit': ['Brillengläser', 'Nach einer genauen Analyse finden wir die passenden Gläser.'], 'kl': ['Kontaktlinsen', 'Je nach Einsatz Tages-, Monats- oder formstabile Linsen.'],
         'sehtest': ['Optometrie', 'Die optometrische Untersuchung geht weit über den Sehtest hinaus.'], 'hoer': ['Hörsysteme', 'Persönliche Hörberatung in den Fachgeschäften.'], 'rep': ['Club und Service', 'Kleine Reparaturen sind oft in Minuten erledigt.']},
    pops=[('el.jpg', 'Hören', 'Hörsysteme der neuesten Generation.'), ('g1.jpg', 'Werkstatt', 'Präzise Fertigung Ihrer Brille.')]))

# 7 ─ Juwelier & Augenoptik Kastner, Meppen
mk('kastner', dict(google=(4.6, 22), slug='kastner-augenoptik-juwelier-meppen', firma='Juwelier & Augenoptik Kastner', kurz='Kastner', name='Familie Kastner', ort='Meppen', strasse='Bahnhofstraße 28', plz='49716',
    tel='05931 6609', tel_i='+4959316609', mail='info@kastner-meppen.de', web='kastner-meppen.de', p='#b39a2e', pi='#1b1a16', dk='#2b271e', s2='#f6f2ea', em='#8d7720', fam=RAL, fonts='r18ant', branche='Augenoptik und Juwelier', tt='Augenoptik und Juwelier',
    logo=(J('kastner', '000'), 0), lh=56, hero='team', himgs=[J('kastner', '029'), J('kastner', '029')],
    ey='TOP-Juwelier und Augenoptiker · Meppen', h1='Persönliche Beratung <em>mit Herz.</em>',
    sub='Seit über 55 Jahren bieten wir Schmuck, Uhren und Brillen in erstklassiger Qualität. Familie Kastner und das Team freuen sich auf Ihren Besuch.',
    ubar=[('55+ Jahre', 'in Meppen'), ('TOP 100', 'Juweliere (Schmuckmagazin)'), ('Branchensieger', 'Augenoptik Meppen')],
    sv_h2='Brillen, Schmuck, Uhren. <em>Mit Leidenschaft.</em>', sv_lead='Wir nehmen uns Zeit, bis Sie das wirklich Passende gefunden haben.',
    svcs=[('Augenoptik', 'Präzise Messung und eine große Auswahl an Fassungen.'),
          ('Trauringe', 'Ihr Spezialist für Trau- und Verlobungsringe in Meppen.'),
          ('Goldschmiede-Atelier', 'Umarbeitungen und individuelle Neuanfertigungen.'),
          ('Uhren', 'Mit 1 Jahr Garantieverlängerung und Uhren-Reparatur.'),
          ('Diamantschmuck', 'Exklusiver Schmuck mit Diamantgutachten.'),
          ('Ohrlochstechen', 'Behutsam, auch für Kinder.')],
    top=dict(nav='Augenoptik', tag='Augenoptik', h2='Branchensieger <em>in der Augenoptik.</em>', img=J('kastner', '003'),
             txt='Bei der letzten unabhängigen Kundenbefragung für Meppen sind wir als Branchensieger hervorgegangen, mit über 90 Prozent Zufriedenheit bei Freundlichkeit, Beratung und Preis-Leistung. Kunden loben die genaue Messung.',
             pts=['Präzise Messung', 'Große Auswahl an Fassungen', 'Beratung ohne Zeitdruck'], btn='Brillen-Beratung anfragen', pop='Branchensieger Augenoptik in Meppen.'),
    zwei=dict(ey='Trauringe', h2='Trau(m)ringe <em>aus Meppen.</em>', img=J('kastner', '054'),
              txt='Große Auswahl und faszinierende Variationen, individuell wie Sie selbst. Im eigenen Goldschmiede-Atelier fertigen wir auch nach Ihren Wünschen.',
              pts=['Große Auswahl', 'Eigenes Goldschmiede-Atelier', '0%-Finanzierung möglich'], btn='Trauring-Beratung anfragen'),
    team=dict(ey='Über uns', h2='Wir bleiben <em>anders.</em>', img=J('kastner', '046'), cap='Das Team von Kastner',
              paras=['Persönliche Beratung mit Herz, das ist seit über 55 Jahren unser Erfolgsrezept. Dafür hat uns das Schmuckmagazin unter die TOP 100 Juweliere im deutschsprachigen Raum gewählt.',
                     'Wir arbeiten jeden Tag daran, das Vertrauen unserer Kunden zu rechtfertigen: durch kompetente Beratung, ehrliche Wertschätzung und umfassenden Service.'],
              tl=[('55+', 'Jahre'), ('TOP 100', 'Juwelier')]),
    gal=[(J('kastner', '034'), '50% 50%'), (J('kastner', '002'), '50% 50%'), (J('kastner', '007'), '50% 50%')],
    stimmen=['Die Beratung war sehr professionell und umfassend. Nach knapp zwei Stunden hatte ich die perfekte Brille.', 'Sehr genaue Messung und tolle Beratung. So gute Brillen hatte ich noch nie.', 'Wir haben hier unsere Trauringe gekauft und sind rundum zufrieden.'],
    hours=[('Mo bis Fr', '9–13 · 14–18 Uhr'), ('Sa', '10–14 Uhr')], cats=['brille', 'gleit', 'sehtest', 'ring', 'rep'], bot='Kasi', notfall=GEN_NF, mq_end='Augenoptik und Juwelier in Meppen',
    rec={'brille': ['Augenoptik', 'Große Auswahl und Beratung ohne Zeitdruck.'], 'gleit': ['Augenoptik', 'Für Gleitsichtgläser wird genau gemessen.'], 'sehtest': ['Augenoptik', 'Am besten kurz einen Termin vereinbaren.'], 'ring': ['Trauringe', 'Große Auswahl und eigenes Goldschmiede-Atelier.'], 'rep': ['Augenoptik', 'Kommen Sie einfach vorbei.']},
    pops=[('el.jpg', 'Trauringe', 'Trau(m)ringe aus dem eigenen Atelier.'), ('g1.jpg', 'Schmuck', 'Ausgezeichnet als TOP-100-Juwelier.')]))

# 8 ─ Brillenstübchen Merzen
mk('stuebchen', dict(gr=(3.8, 5), slug='brillenstuebchen-merzen', firma='Brillenstübchen', kurz='Brillenstübchen', name='Meike Dirla', ort='Merzen', strasse='Hauptstraße 39a', plz='49586',
    tel='05466 936061', tel_i='+495466936061', mail='kontakt@brillenstuebchen.com', web='brillenstuebchen.com', p='#f07a2f', pi='#1b1d22', dk='#3a2a20', s2='#fbf4ee', em='#c4561a', fam=NUN, fonts='r16galerie',
    logo=(R + 'komp/stuebchen-logo.png', 300), lh=46, hero='r', himgs=[J('stuebchen', '004'), J('stuebchen', '004')], cols='48fr 52fr', card='2000/1100',
    ey='Ihre Optikermeisterin in Merzen', h1='Brille und Service <em>aus Meisterhand.</em>',
    sub='Designerbrille, Lesebrille, Gleitsicht, Kinder- oder Sportbrille: Im Brillenstübchen finden wir die Brille, die zu Ihrer Sehstärke, Ihrem Gesicht und Ihrem Alltag passt.',
    ubar=[('Meisterin', 'Meike Dirla'), ('Werkstatt', 'im eigenen Haus'), ('Probetragen', 'zu Hause')],
    sv_h2='Alles rund ums <em>bessere Sehen.</em>', sv_lead='Beratung, Messung und Nachbetreuung aus einer Hand.',
    svcs=[('Brillen', 'Designer-, Lese-, Gleitsicht-, Sport- und Sonnenbrillen.'),
          ('Kinderbrillen', 'Robuste Brillen, die Kindern Spaß machen.'),
          ('Sehtest', 'Fachkundige Augenvermessung mit moderner Messtechnik.'),
          ('Kontaktlinsen', 'Anpassung und Nachbetreuung, auch zum Ausprobieren.'),
          ('Reparaturen', 'Richten, Reinigen und Kleinreparaturen in der eigenen Werkstatt.'),
          ('Schutzbrillen', 'Auch mit Ihrer Sehstärke.')],
    top=dict(nav='Probetragen', tag='Brillenauswahl mit nach Hause', h2='In Ruhe entscheiden. <em>Zu Hause.</em>', img=J('stuebchen', '017'),
             txt='Für alle Unentschlossenen gibt es die Brillenauswahl mit nach Hause. So wählen Sie Ihr Lieblingsmodell nach dem Probetragen ganz in Ruhe aus. Ein ähnlicher Service steht auch bei Kontaktlinsen zur Verfügung.',
             pts=['Modelle zu Hause probetragen', 'Ganz in Ruhe auswählen', 'Auch für Kontaktlinsen'], btn='Beratung anfragen', pop='Brillen mit nach Hause nehmen und in Ruhe probetragen.'),
    team=dict(ey='Über uns', h2='Ihr Brillenstübchen <em>in Merzen.</em>', img=J('stuebchen', '003'), cap='Das Brillenstübchen an der Hauptstraße',
              paras=['Rund um das Thema besser sehen steht der zufriedene Kunde bei mir im Vordergrund. Mit moderner Messtechnik, Fachwissen und langjähriger Erfahrung prüfe ich Ihre exakte Sehstärke.',
                     'Kleinreparaturen und neue Brillen entstehen in der hauseigenen Meisterwerkstatt. Schnell, gründlich und ohne langen Anfahrtsweg.'],
              tl=[('Merzen', 'Hauptstraße 39a'), ('Meisterin', 'Meike Dirla')]),
    gal=[(J('stuebchen', '016'), '50% 50%'), (J('stuebchen', '010'), '50% 30%'), (J('stuebchen', '007'), '50% 30%')],
    stimmen=['Wir haben eine schöne Brille für unsere Tochter bekommen und wurden toll beraten.', 'Frau Dirla hat sich viel Zeit genommen, der Sehtest war super.', 'Gute Auswahl und günstige Preise.'],
    hours=[('Mo, Di, Do, Fr', '9–13 · 14.30–18 Uhr'), ('Mi', '9–13 Uhr')], cats=['brille', 'gleit', 'kind', 'kl', 'sehtest', 'rep'], bot='Mia', notfall=GEN_NF, mq_end='Optikerin in Merzen',
    rec={'brille': ['Brillen', 'Große Auswahl, auch zum Probetragen zu Hause.'], 'gleit': ['Brillen', 'Gleitsicht und Lesebrillen werden genau vermessen.'], 'kind': ['Kinderbrillen', 'Robuste Kinderbrillen mit viel Geduld ausgesucht.'],
         'kl': ['Kontaktlinsen', 'Kontaktlinsen gibt es auch zum Ausprobieren.'], 'sehtest': ['Sehtest', 'Fachkundige Augenvermessung aus Meisterhand.'], 'rep': ['Reparaturen', 'Die eigene Werkstatt erledigt das schnell.']},
    pops=[('g1.jpg', 'Beratung', 'Persönlich und ohne Eile.'), ('tm.jpg', 'Meisterwerkstatt', 'Reparaturen schnell und im Haus.')]))

# 9 ─ Hörcenter Grönegau, Melle
mk('groenegau', dict(css2='#fokus figure{max-width:470px;justify-self:center;margin-inline:auto}', google=(5.0, 34), slug='hoercenter-groenegau-melle', firma='Hörcenter Grönegau', kurz='Hörcenter Grönegau', name='Jens Heimke', ort='Melle', strasse='Grönenberger Straße 12', plz='49324',
    tel='05422 6059021', tel_i='+4954226059021', mail='j.heimke@hc-groenegau.de', web='hoercenter-groenegau.de', p='#9b1b1b', dk='#2a1414', s2='#f7f1ef', fam=SIG, fonts='r10vagts', branche='Hörakustik', tt='Ihr Hörakustiker', bot_tag='Ihr Hör-Lotse', nf_t='Hörgerät macht Probleme?',
    logo_txt='Hörcenter Grönegau<small>Ihr Hörgeräte-Spezialist in Melle</small>', hero='l', himgs=[J('groenegau', '023'), J('groenegau', '023')], cols='42fr 58fr', card='640/720',
    ey='Hörakustik in Melle', h1='Unser Ziel: <em>Dass Sie wieder gut hören.</em>',
    sub='Wir wollen Ihnen keine Technik verkaufen. Wir nehmen uns besonders viel Zeit für Höranalyse, Beratung und Anpassung, damit Sie wieder mitten im Leben sind.',
    ubar=[('5,0 Sterne', 'bei Google'), ('Alle Hersteller', 'namhafte Marken'), ('Probetragen', 'unverbindlich')],
    sv_h2='Hören, <em>wie es zu Ihnen passt.</em>', sv_lead='Hörgeräte und Zubehör aller namhaften Hersteller.',
    svcs=[('Höranalyse', 'Kostenlose professionelle Höranalyse mit moderner Messtechnik.'),
          ('Probetragen', 'Verschiedene Hörgeräte unverbindlich im Alltag testen.'),
          ('Anpassung', 'Persönliche Einstellung auf Ihren Alltag und Ihre Ansprüche.'),
          ('Service', 'Kontrolle, Reinigung und Wartung, auch für Geräte von anderswo.'),
          ('Krankenkasse', 'Direkte Abrechnung mit Ihrer Krankenkasse.'),
          ('Gehörschutz', 'Individueller Gehör-, Schlaf- und Schwimmschutz.')],
    top=dict(nav='Höranalyse', tag='Kostenlose Höranalyse', h2='Viel Zeit. <em>Kein Druck.</em>', img=J('groenegau', '024'),
             txt='Wir kennen uns aus mit Herstellung, Anpassung und Funktionsweise von Hörgeräten. Deshalb nehmen wir uns für die Analyse Ihres Hörvermögens besonders viel Zeit. Kunden testen bei uns oft über Wochen verschiedene Geräte, bis es wirklich passt.',
             pts=['Kostenlose Höranalyse', 'Probetragen über mehrere Wochen', 'Kleine Reparaturen sofort'], btn='Höranalyse-Termin anfragen', pop='Kostenlose Höranalyse und unverbindliches Probetragen.'),
    team=dict(ey='Über uns', h2='Hörakustik, <em>wie sie sein sollte.</em>', img=J('groenegau', '015'), cap='Moderne Messtechnik im Hörcenter Grönegau', mw=400,
              paras=['Wir wissen, wie schwierig es ist, mit eingeschränktem Hörvermögen am Alltag teilzunehmen. Darum steht bei uns nicht der Verkauf im Mittelpunkt, sondern Ihr gutes Hören.',
                     'Das Geschäft ist barrierefrei: Ein kleiner Weg führt um das Haus zum Hintereingang.'],
              tl=[('Melle', 'Grönenberger Straße 12'), ('5,0', 'bei Google')]),
    stimmen=['Ich habe mehrere Akustiker in Melle ausprobiert. Der Unterschied ist wie Tag und Nacht: ehrlich, kompetent, ohne Druck.', 'Ich konnte über Monate verschiedene Geräte testen, jedes wurde genau auf mich eingestellt.', 'Herr Heimke nimmt sich wirklich Zeit und erklärt alles geduldig.'],
    hours=[('Mo bis Do', '9–13 · 14–18 Uhr'), ('Fr', '9–13 · 14–17 Uhr'), ('Sa', 'nach Vereinbarung')], cats=['hoer', 'hg', 'iem', 'tinn'], bot='Hanno', notfall=HG_NF, mq_end='Hörakustik in Melle',
    ab2='Bringen Sie Ihr Hörgerät mit, wenn Sie schon eins tragen, auch wenn Sie es woanders gekauft haben.', ab3='Wir analysieren Ihr Hörvermögen und Sie testen in Ruhe. Sie entscheiden.',
    rec={'hoer': ['Höranalyse', 'Starten Sie mit der kostenlosen Höranalyse.'], 'hg': ['Service', 'Reinigung und kleine Reparaturen gibt es sofort vor Ort, auch für fremde Geräte.'], 'iem': ['Gehörschutz', 'Individueller Gehör-, Schlaf- und Schwimmschutz.'], 'tinn': ['Höranalyse', 'Sprechen Sie es bei der Höranalyse an.']},
    pops=[('tm.jpg', 'Service', 'Wartung auch für Hörgeräte von anderswo.')]))

# 10 ─ Krüßel Hören & Sehen, Lingen
mk('kruessel', dict(ab2='Bringen Sie Ihre aktuelle Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit für Ihre Fragen.', google=(4.9, 59), slug='kruessel-hoeren-sehen-lingen', firma='Krüßel Hören & Sehen', kurz='Krüßel', name='Heinz Krüßel', ort='Lingen', strasse='Konrad-Adenauer-Ring 16a', plz='49808',
    tel='0591 53711', tel_i='+4959153711', mail='info@hoeren-sehen.de', web='hoeren-sehen.de', p='#f2b600', pi='#1b1d22', dk='#1f1f1f', s2='#f7f4ea', em='#a37a00', fam=MONT, fonts='r16geyer', branche='Augenoptik und Hörakustik', tt='Optiker und Hörakustiker',
    logo=(J('kruessel', '000'), 0), lh=50, hero='r', himgs=[R + 'komp/kruessel-duo.jpg', R + 'komp/kruessel-duo.jpg'], cols='56fr 44fr', card='732/466',
    ey='Augenoptik & Hörakustik · Lingen', h1='Gut sehen, gut hören. <em>In Lingen.</em>',
    sub='Höchste fachliche Qualifikation, moderne Geräte und eine entspannte Atmosphäre. Bei uns wird der Brillenkauf zum Vergnügen, und auch beim Hören nehmen wir uns Zeit.',
    ubar=[('4,9 Sterne', '59 Bewertungen'), ('Sehen + Hören', 'unter einem Dach'), ('Wunschtermin', 'online')],
    sv_h2='Unsere Top-Leistungen <em>für Sehen und Hören.</em>', sv_lead='Für Sie nur das Beste.',
    svcs=[('Gleitsichtbrillen', 'Wir analysieren Ihren Sehalltag und passen exakt an.'),
          ('Sehtest', 'Professioneller Sehtest, wenn sich Ihre Sehstärke verändert hat.'),
          ('Brillenmode', 'Stilvolle Brillen namhafter Marken zu fairem Preis.'),
          ('Hörgeräte', 'Diskret, kompetent und individuell.'),
          ('Kontaktlinsen', 'Anpassung und Beratung.'),
          ('Hörgeräte-Service', 'Schnelle Hilfe, auch wenn Sie kein Kunde sind.')],
    top=dict(nav='Gleitsicht', tag='Gleitsichtbrillen', h2='Klar sehen. <em>In jeder Situation.</em>', img=J('kruessel', '001'),
             txt='Ob beim Lesen, Autofahren oder Blick in die Ferne: Wir analysieren Ihren Sehalltag und Ihre Anforderungen. Mit moderner Technik passen wir Ihre Gleitsichtbrille exakt an, damit Sie vom ersten Augenblick an gut sehen.',
             pts=['Analyse Ihres Sehalltags', 'Exakte Anpassung', 'Faires Preis-Leistungs-Verhältnis'], btn='Gleitsicht-Beratung anfragen', pop='Gleitsichtbrillen, exakt angepasst.'),
    zwei=dict(ey='Hören', h2='Hören bedeutet <em>Lebensqualität.</em>', img=J('kruessel', '026'),
              txt='Mit innovativer Technik und persönlicher Beratung finden wir gemeinsam die beste Hörlösung für Sie. Diskret, kompetent und individuell.',
              pts=['Persönliche Hörberatung', 'Moderne Hörsysteme', 'Schnelle Hilfe im Service'], btn='Hörberatung anfragen'),
    team=dict(ey='Über uns', h2='Sie stehen <em>im Mittelpunkt.</em>', img=J('kruessel', '005'), cap='Krüßel am Konrad-Adenauer-Ring in Lingen', mw=520,
              paras=['Durch die hohe Qualifikation unseres Teams und die moderne Ausstattung können wir Ihnen eine breite Palette an Leistungen anbieten.',
                     'Unser größtes Anliegen ist eine umfassende, individuelle und kompetente Beratung, beim Sehen genauso wie beim Hören.'],
              tl=[('Lingen', 'Konrad-Adenauer-Ring 16a'), ('59', 'Google-Bewertungen')]),
    gal=[(J('kruessel', '003'), '50% 50%'), (J('kruessel', '015'), '50% 50%'), (J('kruessel', '016'), '50% 50%')],
    hours=[('Mo, Di, Do, Fr', '8.30–18 Uhr'), ('Mi', '8.30–13 Uhr'), ('Sa', '9–13 Uhr')], cats=['brille', 'gleit', 'sehtest', 'hoer', 'hg', 'kl'], bot='Kurt', notfall=GEN_NF, mq_end='Optiker und Hörakustiker in Lingen',
    rec={'brille': ['Brillenmode', 'Stilvolle Marken zu fairem Preis.'], 'gleit': ['Gleitsichtbrillen', 'Wird genau auf Ihren Sehalltag abgestimmt.'], 'sehtest': ['Sehtest', 'Am besten online einen Wunschtermin buchen.'], 'hoer': ['Hörgeräte', 'Persönliche Hörberatung im Geschäft.'], 'hg': ['Hörgeräte-Service', 'Schnelle Hilfe, auch für Nicht-Kunden.'], 'kl': ['Kontaktlinsen', 'Anpassung und Beratung im Geschäft.']},
    pops=[('el.jpg', 'Hören', 'Diskret, kompetent und individuell.'), ('g1.jpg', 'Brillenmode', 'Namhafte Marken, faire Preise.')]))
