"""Runde 26 · Augenoptiker und Hörakustiker 60 km um Werlte. Nur Texte, Logos und Fotos der Betriebe.
Hörgeräte sind Medizinprodukte: keine Heilversprechen, keine erfundenen Ergebnisse."""
from common import *
SITES = {}
PX = '/home/claude/pixa20/'
R = '/home/claude/r26raw/'
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

SSANS = ('"Source Sans 3",system-ui,sans-serif',) * 2; TIT = ('"Titillium Web",system-ui,sans-serif',) * 2; POP = ('"Poppins",system-ui,sans-serif',) * 2
HEEBO = ('"Heebo",system-ui,sans-serif',) * 2; MON = ('"Montserrat",system-ui,sans-serif',) * 2; MAN = ('"Manrope",system-ui,sans-serif',) * 2
REP = 'Rufen Sie kurz an oder kommen Sie vorbei. Kleine Reparaturen erledigen wir meist sofort.'

# 1 ─ Meiners Optik Uhren Schmuck, Westoverledingen-Flachsmeer
mk('meiners', dict(gr=(4.3, 25), slug='meiners-optik-flachsmeer', firma='Meiners Optik Uhren Schmuck', kurz='Meiners', name='Hubertus Meiners', ort='Westoverledingen-Flachsmeer', strasse='Königstraße 149', plz='26810',
    tel='04955 9752799', tel_i='+4949559752799', mail='info@optik-meiners.de', web='optik-meiners.de', p='#da0c0c', dk='#2a2c30', s2='#f6f3f3', fam=SSANS, fonts='r10vagts',
    logo=(J('meiners', '000'), 420, 'trim'), lh=50, hero='r', himgs=[J('meiners', '042'), J('meiners', '042')], cols='48fr 52fr',
    ey='Augenoptik-Meisterbetrieb · Flachsmeer', h1='Ihre Brille. <em>Alles aus einer Hand.</em>',
    sub='Von der Brillenglasbestimmung über die Fassungsberatung bis zur handwerklichen Anfertigung: Bei uns liegt alles in einer Hand. Persönlich beraten von Hubertus und Birgit Meiners.',
    ubar=[('2 Meister', 'Augenoptik'), ('Hausbesuche', 'nach Absprache'), ('Passbilder', 'biometrisch')],
    sv_h2='Gut sehen. <em>Gut beraten.</em>', sv_lead='Als Meisterbetrieb nehmen wir uns Zeit für Ihre Augen und finden die Brille, die zu Ihnen passt.',
    svcs=[('Sehtest', 'Schon nach wenigen Minuten wissen Sie, ob eine neue Brille Ihre Sehkraft verbessert.'),
          ('Brillen', 'Marken wie Baldessarini, Cazal, Eschenbach, Ray Ban oder TitanFlex. Angefertigt im eigenen Meisterbetrieb.'),
          ('Kontaktlinsen', 'Formstabile und weiche Linsen, nach ausführlicher Beratung fachgerecht angepasst.'),
          ('Lupen und Sehhilfen', 'Große Auswahl an vergrößernden Sehhilfen. Hubertus Meiners ist Sonderanpasser dafür.'),
          ('Reparaturservice', 'In den meisten Fällen helfen wir sofort. Dauert es länger, gibt es eine Tasse Kaffee.'),
          ('Uhren, Schmuck, Passbilder', 'Uhren und Schmuck für Damen, Herren und Kinder. Dazu biometrische Passbilder.')],
    top=dict(nav='Hausbesuche', tag='Außer-Haus-Service', h2='Sie können nicht kommen? <em>Wir kommen zu Ihnen.</em>', img=J('meiners', '044'),
             txt='Sollte es Ihnen nicht möglich sein, zu uns zu kommen, rufen Sie einfach an. Wir vereinbaren einen Termin und kommen zu Ihnen nach Hause, auch wenn es nur um das Richten Ihrer Brille geht.',
             pts=['Termin per Telefon', 'Beratung bei Ihnen zu Hause', 'Auch für kleine Anpassungen'], btn='Hausbesuch anfragen', pop='Wir kommen auch zu Ihnen nach Hause.'),
    zwei=dict(ey='Mode und Trend', h2='Eine Brille, <em>die zu Ihnen passt.</em>', img=J('meiners', '043'),
              txt='Augenoptikermeisterin Birgit Meiners hat ihr Spezialgebiet in Mode und Trend. Sie berät Sie bei der Wahl der Fassung, damit Ihre Brille nicht nur gut sitzt, sondern auch zu Ihnen passt.',
              pts=['Persönliche Fassungsberatung', 'Aktuelle Marken', 'Auch außerhalb der Öffnungszeiten nach Termin'], btn='Beratung anfragen'),
    team=dict(ey='Über uns', h2='Zwei Meister <em>für Ihre Augen.</em>', img=J('meiners', '046'), cap='Meiners Optik Uhren Schmuck in Flachsmeer',
              paras=['Hubertus Meiners ist staatlich geprüfter Augenoptikermeister, Betriebswirt des Handwerks und Kontaktlinsenspezialist. Birgit Meiners ist staatlich geprüfte Augenoptikermeisterin mit Spezialgebiet Mode und Trend.',
                     'Wir sind Mitglied der Landesinnung der Augenoptiker und Optometristen in Niedersachsen und Bremen und im Gewerbeverein Flachsmeer.'],
              tl=[('2', 'Meister im Haus'), ('Königstr. 149', 'Flachsmeer')]),
    gal=[(J('meiners', '001'), '50% 50%'), (J('meiners', '002'), '50% 50%'), (J('meiners', '034'), '50% 50%')],
    hours=[('Mo, Di, Do', '9–13 · 14.30–18 Uhr'), ('Mi', '9–13 Uhr'), ('Fr', '9–17 Uhr'), ('Sa', '9–12 Uhr')], cats=['brille', 'gleit', 'kl', 'sehtest', 'rep', 'mobil'], bot='Mia', notfall=REP, mq_end='Augenoptik in Flachsmeer',
    rec={'brille': ['Brillen', 'Alles aus einer Hand, vom Sehtest bis zur fertigen Brille.'], 'gleit': ['Brillen', 'Für Gleitsicht nehmen wir uns Zeit und messen genau.'], 'kl': ['Kontaktlinsen', 'Kontaktlinsen passen wir nach einem Beratungsgespräch an.'],
         'sehtest': ['Sehtest', 'Ein Sehtest dauert nur wenige Minuten.'], 'rep': ['Reparaturservice', 'Die meisten Reparaturen erledigen wir sofort.'], 'mobil': ['Lupen und Sehhilfen', 'Rufen Sie an, wir kommen auch zu Ihnen nach Hause.']},
    pops=[('el.jpg', 'Mode und Trend', 'Persönliche Fassungsberatung von Birgit Meiners.'), ('g1.jpg', 'Reparaturservice', 'Meist sofort erledigt, sonst mit Kaffee.')]))

# 2 ─ Borgmann Optik, Haren (Ems)
mk('borgmann', dict(google=(4.9, 20), slug='borgmann-optik-haren', firma='Borgmann Optik', kurz='Borgmann Optik', name='Ulrich Borgmann', ort='Haren (Ems)', strasse='Alter Markt 6', plz='49733',
    tel='05932 1250', tel_i='+4959321250', mail='info@borgmann-optik.de', web='borgmann-optik.de', p='#d4003c', dk='#2b2a2e', s2='#f7f2f4', fam=TIT, fonts='r15han',
    logo=(J('borgmann', '001'), 460, 'trim'), lh=40, hero='r', himgs=[J('borgmann', '010'), J('borgmann', '010')], cols='46fr 54fr',
    ey='Ihr Beratungsoptiker in Haren', h1='Beratung mit Charme <em>und Persönlichkeit.</em>',
    sub='Wir sind ein eingespieltes Team mit viel Erfahrung. Bei uns bekommen Sie eine fachlich kompetente Beratung, damit Sie mit der richtigen Brille nach Hause gehen.',
    ubar=[('Am Alter Markt', 'mitten in Haren'), ('Sehtest', 'nach Termin'), ('Sa geöffnet', '9–13 Uhr')],
    sv_h2='Besser sehen, <em>besser aussehen.</em>', sv_lead='Eine Brille schafft den richtigen Durchblick. Vor allem aber muss sie zu Ihnen passen, technisch und im Design.',
    svcs=[('Sehtest', 'Wir prüfen Ihre Sehschärfe. Auch für Brillenträger ist eine regelmäßige Überprüfung sinnvoll.'),
          ('Brillen', 'Technisch perfekt eingestellt und passend zu Ihrem Gesicht. Persönlich, individuell und sympathisch beraten.'),
          ('Sonnenbrillen', '100 % UV-Schutz, ermüdungsfreies Sehen und natürliche Farben.'),
          ('Kontaktlinsen', 'Finden Sie heraus, ob Kontaktlinsen eine Option für Sie sind.'),
          ('Kinderbrillen', 'Kinder bekommen bei uns viel Zeit für die Auswahl.'),
          ('Service', 'Sitzt die Brille nicht perfekt, richten wir sie freundlich und geduldig nach.')],
    top=dict(nav='Sehtest', tag='Einladung zum Sehtest', h2='Wir stellen Ihre Augen <em>auf die Probe.</em>', img=J('borgmann', '004'),
             txt='Wir testen Ihre Sehschärfe in Ruhe und erklären Ihnen das Ergebnis. Auch wenn Sie schon eine Brille tragen, lohnt sich eine regelmäßige Überprüfung der Augen.',
             pts=['Termin nach Wunsch', 'Ergebnis verständlich erklärt', 'Ehrliche Empfehlung'], btn='Sehtest-Termin anfragen', pop='Vereinbaren Sie Ihren Termin zum Sehtest.'),
    team=dict(ey='Wir', h2='Ein eingespieltes Team <em>am Alter Markt.</em>', img=J('borgmann', '022'), mw=400, cap='Aus dem Team von Borgmann Optik',
              paras=['Persönlich, individuell und sympathisch: So berät unser Team. Wir nehmen uns Zeit für Ihre Wünsche, bei der Technik genauso wie beim Design.',
                     'Inhaber Ulrich Borgmann ist Augenoptiker und führt das Geschäft mitten in Haren.'],
              tl=[('Alter Markt 6', 'Haren (Ems)'), ('Mo–Sa', 'für Sie geöffnet')]),
    gal=[(J('borgmann', '019'), '50% 50%'), (J('borgmann', '021'), '50% 50%'), (J('borgmann', '008'), '50% 50%')],
    hours=[('Mo bis Fr', '9–12.30 · 14–18 Uhr'), ('Sa', '9–13 Uhr')], cats=['brille', 'gleit', 'kl', 'sehtest', 'kind', 'rep'], bot='Lina', notfall=REP, mq_end='Augenoptik in Haren',
    rec={'brille': ['Brillen', 'Wir beraten zu Technik und Design.'], 'gleit': ['Brillen', 'Gleitsicht braucht genaue Messung. Dafür nehmen wir uns Zeit.'], 'kl': ['Kontaktlinsen', 'Wir finden heraus, ob Kontaktlinsen zu Ihnen passen.'],
         'sehtest': ['Sehtest', 'Am besten einen Termin vereinbaren unter 05932 1250.'], 'kind': ['Kinderbrillen', 'Kinder bekommen viel Zeit für die Auswahl.'], 'rep': ['Service', 'Wir richten Ihre Brille gern nach.']},
    pops=[('g2.jpg', 'Brillen', 'Technisch perfekt und passend zu Ihnen.'), ('g1.jpg', 'Besuchen Sie uns', 'Am Alter Markt 6 in Haren.')]))

# 3 ─ Hölscher, Emsbüren
mk('hoelscher', dict(google=(4.9, 53), slug='hoelscher-augenoptik-hoerakustik-emsbueren', firma='Hölscher Augenoptik & Hörakustik', kurz='Hölscher', name='Carsten Hölscher', ort='Emsbüren', strasse='Dahlhok 29', plz='48488',
    tel='05903 303', tel_i='+495903303', mail='info@brille-hoelscher.de', web='brille-hoelscher.de', p='#213a8f', dk='#152457', s2='#f2f4f9', fam=POP, fonts='r14sch', branche='Augenoptik und Hörakustik', tt='Augenoptik und Hörakustik',
    logo=(J('hoelscher', '000'), 420, 'alphacrop'), lh=50, hero='r', himgs=[J('hoelscher', '030'), J('hoelscher', '038')], cols='46fr 54fr',
    ey='ZEISS Partner · Emsbüren, Spelle, Schüttorf', h1='Für Auge und Ohr. <em>Mit Meisterhand.</em>',
    sub='Ihr Augenoptiker und Hörakustiker im Emsland und in der Grafschaft Bentheim. Mit ZEISS i.Profiler, kostenlosem Hörtest und einem großen Team aus Meisterinnen und Meistern.',
    ubar=[('3 Fachgeschäfte', 'Emsbüren, Spelle, Schüttorf'), ('ZEISS i.Profiler', 'Messung auf 1/100 dpt'), ('Hörtest', 'kostenfrei')],
    sv_h2='Sehen und hören. <em>Unter einem Dach.</em>', sv_lead='Modernste Technik und echtes Handwerk: So finden wir die richtige Lösung für Ihre Augen und Ohren.',
    svcs=[('ZEISS Sehanalyse', 'Der i.Profiler misst Ihre Glasstärke auf 1/100 Dioptrien, auch bei großer Pupille in der Nacht.'),
          ('Brillen und Gleitsicht', 'Einstärken-, Gleitsicht- und Arbeitsplatzgläser, individuell in die Fassung eingearbeitet.'),
          ('Hörgeräte', 'Hörakustikmeister passen Ihr Hörgerät so an, dass es angenehm sitzt und einfach zu bedienen ist.'),
          ('Kontaktlinsen', 'Monats- und Tageslinsen, fachgerecht angepasst.'),
          ('Sonnenschutz und DriveSafe', 'Sonnenschutzgläser und ZEISS DriveSafe für entspanntes Fahren.'),
          ('Optometrie', 'Mit Master Professional Optometrie im Team.')],
    top=dict(nav='Hörtest', tag='Kostenloser Hörtest', h2='Gutes Hören <em>beginnt mit einem Test.</em>', img=J('hoelscher', '044'),
             txt='Wir laden Sie zum kostenfreien Hörtest ein. Unsere Hörakustikmeisterinnen erklären Ihnen das Ergebnis und stellen Ihr Hörgerät so ein, dass es Sie in schwierigen Situationen gut unterstützt.',
             pts=['Hörtest ohne Kosten', 'Hörakustikmeister vor Ort', 'Anpassung, die zum Alltag passt'], btn='Hörtest-Termin anfragen', pop='Wir laden Sie zum kostenfreien Hörtest ein.'),
    zwei=dict(ey='Augenoptik', h2='Gemessen auf <em>1/100 Dioptrien.</em>', img=J('hoelscher', '032'),
              txt='Hölscher ist einer der wenigen Optiker mit der speziellen Seh-Analyse am ZEISS i.Profiler. Mit dem i.Terminal 2 bestimmen wir außerdem den Durchblickspunkt Ihres Glases ganz individuell.',
              pts=['ZEISS i.Profiler', 'ZEISS i.Terminal 2', 'Nachtsehen mitgemessen'], btn='Sehanalyse anfragen'),
    team=dict(ey='Über uns', h2='Ein großes Team <em>für Auge und Ohr.</em>', img=J('hoelscher', '002'), cap='Das Fachgeschäft von Hölscher',
              paras=['Carsten Hölscher ist Augenoptik- und Hörakustikmeister in Emsbüren, Silke Hölscher ist Diplom-Ingenieurin für Augenoptik und Hörakustikmeisterin in Schüttorf.',
                     'Mit Meisterinnen für Augenoptik und Hörakustik in Emsbüren, Spelle und Schüttorf sind wir für Sie da.'],
              tl=[('3', 'Fachgeschäfte'), ('ZEISS', 'Partner')]),
    gal=[(J('hoelscher', '037'), '50% 30%'), (J('hoelscher', '040'), '50% 30%'), (J('hoelscher', '050'), '50% 50%')],
    hours=[('Mo bis Fr', '8–12 · 14–18 Uhr'), ('Sa', '8–12.30 Uhr')], cats=['brille', 'gleit', 'hoer', 'hg', 'kl', 'sehtest'], bot='Hanna', notfall=REP, mq_end='Augenoptik und Hörakustik in Emsbüren',
    ab2='Bringen Sie Ihre Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit für Ihre Fragen.',
    rec={'brille': ['Brillen und Gleitsicht', 'Mit ZEISS-Messung auf 1/100 Dioptrien.'], 'gleit': ['Brillen und Gleitsicht', 'Gleitsichtgläser werden individuell vermessen.'], 'hoer': ['Hörgeräte', 'Am besten mit dem kostenlosen Hörtest anfangen.'],
         'hg': ['Hörgeräte', 'Unsere Hörakustikmeister helfen Ihnen weiter.'], 'kl': ['Kontaktlinsen', 'Monats- und Tageslinsen, fachgerecht angepasst.'], 'sehtest': ['ZEISS Sehanalyse', 'Die Sehanalyse misst auch Ihr Sehen bei Nacht.']},
    pops=[('el.jpg', 'ZEISS Sehanalyse', 'Gemessen auf 1/100 Dioptrien.'), ('g2.jpg', 'Unser Team', 'Meisterinnen und Meister für Auge und Ohr.')]))

# 4 ─ Brillen + Akustik-Studio Reher, Cloppenburg
mk('reher', dict(google=(4.7, 25), slug='brillen-akustik-studio-reher-cloppenburg', firma='Brillen + Akustik-Studio Reher', kurz='Reher', name='Daniel Reher', ort='Cloppenburg', strasse='Bahnhofstraße 4', plz='49661',
    tel='04471 3788', tel_i='+4944713788', mail='info@brillen-reher.de', web='brillen-reher.de', p='#7d2536', dk='#2a1a1e', s2='#f7f2f3', fam=HEEBO, fonts='r14bec', branche='Augenoptik und Hörakustik', tt='Augenoptik und Hörakustik',
    logo=(KO + 'reher-logo.png', 320), lh=56, hero='team', himgs=[J('reher', '003'), J('reher', '003')],
    ey='Familienunternehmen seit 1953 · Cloppenburg', h1='Von jeher <em>zu Reher.</em>',
    sub='Seit fast 70 Jahren Optik und fast 25 Jahren Akustik: Brillen + Akustik-Studio Reher steht in Cloppenburg für bestes Sehen und Hören. Inzwischen in der dritten Generation.',
    ubar=[('Seit 1953', 'Augenoptik'), ('Seit 2000', 'Hörakustik'), ('3. Generation', 'Familienbetrieb')],
    sv_h2='Ihre Augen und Ohren <em>verdienen Aufmerksamkeit.</em>', sv_lead='Erfahrung, handwerkliches Geschick und modernste Technik: Das braucht es für die perfekte Anpassung.',
    svcs=[('Brillenmode', 'Aktuelle Fassungen, persönlich beraten, damit die Brille zu Ihrem Gesicht passt.'),
          ('Brillengläser', 'Gläser für jede Situation, vom Bildschirm bis zum Autofahren.'),
          ('Hörsysteme', 'Moderne Hörgeräte, auch als nahezu unsichtbare Im-Ohr-Systeme.'),
          ('Kontaktlinsen', 'Individuell angepasst und regelmäßig kontrolliert.'),
          ('Kinderbrillen', 'Robuste Brillen und viel Geduld für die Kleinen.'),
          ('Gehörschutz', 'Individuell angefertigt, für Arbeit, Motorsport oder Konzerte.')],
    top=dict(nav='Hören', tag='Hörsysteme', h2='Wieder besser hören. <em>Mehr erleben.</em>', img=J('reher', '004'),
             txt='Gespräche führen, das Lachen von Freunden hören, das Lieblingslied genießen: Wir passen Ihr Hörsystem individuell an, bis es sich gut anfühlt. Auch als kleines Im-Ohr-Gerät, das kaum jemand sieht.',
             pts=['Individuelle Anpassung', 'Im-Ohr-Geräte möglich', 'Gehörschutz nach Maß'], btn='Hörberatung anfragen', pop='Hörsysteme, individuell angepasst.'),
    team=dict(ey='Über uns', h2='Drei Generationen <em>für gutes Sehen und Hören.</em>', img=J('reher', '018'), mw=420, cap='Aus dem Team von Reher',
              paras=['Gegründet von Karl-Heinz Reher und vergrößert von Heinz und Elisabeth Reher, hat Daniel Reher das Geschäft im Jahr 2000 zum Brillen + Akustik-Studio erweitert.',
                     'Mit unserem erfahrenen, langjährigen Team richten wir uns nach Ihren Wünschen. Als Kunde stehen Sie bei uns im Mittelpunkt.'],
              tl=[('1953', 'gegründet'), ('3.', 'Generation')]),
    gal=[(J('reher', '001'), '50% 50%'), (J('reher', '002'), '50% 50%')],
    hours=[('Mo, Di, Do, Fr', '9–12.45 · 14.15–18 Uhr'), ('Mi', '9–13 Uhr'), ('Sa', '10–13 Uhr')], cats=['brille', 'gleit', 'hoer', 'hg', 'kl', 'kind'], bot='Ella', notfall=REP, mq_end='Von jeher zu Reher',
    ab2='Bringen Sie Ihre Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit, ganz ohne Zeitdruck.',
    rec={'brille': ['Brillenmode', 'Wir beraten Sie in Ruhe und ohne Zeitdruck.'], 'gleit': ['Brillengläser', 'Wir finden die Gläser für Ihren Alltag.'], 'hoer': ['Hörsysteme', 'Am besten mit einer Hörberatung anfangen.'],
         'hg': ['Hörsysteme', 'Kommen Sie vorbei, wir schauen uns Ihr Hörgerät an.'], 'kl': ['Kontaktlinsen', 'Kontaktlinsen passen wir individuell an.'], 'kind': ['Kinderbrillen', 'Auch Kinder sind herzlich willkommen.']},
    pops=[('pr.jpg', 'Hörsysteme', 'Fast unsichtbar und individuell angepasst.'), ('g1.jpg', 'Seit 1953', 'Von jeher zu Reher, mitten in Cloppenburg.')]))

# 5 ─ Sibo Müller, Rhauderfehn
mk('sibo', dict(google=(4.8, 284), slug='sibo-mueller-rhauderfehn', firma='Sibo Müller', kurz='Sibo Müller', name='Sibo Müller', ort='Rhauderfehn', strasse='Untenende 69', plz='26817',
    tel='04952 3140', tel_i='+4949523140', mail='info@sibomueller.de', web='sibomueller.de', p='#1f97c2', dk='#123a4a', s2='#f1f7fa', em='#13739a', fam=HEEBO, fonts='r14bec', branche='Augenoptik und Hörakustik', tt='Augenoptiker und Hörakustiker',
    logo=(KO + 'sibo-logo.png', 240), lh=64, hero='r', himgs=[J('sibo', '022'), J('sibo', '022')], cols='50fr 50fr', card='930/1409',
    ey='Augenoptik & Hörakustik · Rhauderfehn und Weener', h1='Sehen und hören. <em>Seit 1873.</em>',
    sub='Was 1873 als Uhrengeschäft in der Rhauderwieke begann, führt Sibo Müller heute in fünfter Generation: mit modernen Praxisräumen für Augenoptik und Hörakustik.',
    ubar=[('Seit 1873', 'Familienbetrieb'), ('5. Generation', 'Sibo Müller'), ('2 Standorte', 'Rhauderfehn, Weener')],
    sv_h2='Ihr Seh- und Hörkomfort <em>steht im Mittelpunkt.</em>', sv_lead='Wir nehmen uns bewusst Zeit für Sie, ganz ohne Zeitdruck, und beraten ehrlich und individuell.',
    svcs=[('Augenvorsorge', 'Moderne Geräte in eigenen Praxisräumen für einen genauen Blick auf Ihre Augen.'),
          ('Brillenmode und Gläser', 'Fassungen, die Ihnen stehen, und Gläser für jede Situation.'),
          ('Hörsysteme', 'Moderne Hörgeräte, auch als nahezu unsichtbare Im-Ohr-Systeme.'),
          ('Kinder', 'Kinderbrillen und Pädakustik, mit Geduld und Zeit.'),
          ('Kontaktlinsen', 'Individuell angepasst und gut betreut.'),
          ('Trauringe und Gehörschutz', 'Trauringe, Uhren und Schmuck, dazu Gehörschutz nach Maß.')],
    top=dict(nav='Hören', tag='Hörakustik', h2='Mehr hören, <em>mehr leben.</em>', img=J('sibo', '015'),
             txt='Sibo Müller ist Augenoptiker- und Hörakustikmeister, Optometrist, Pädakustiker und Hör-Therapeut. Gemeinsam finden wir das Hörsystem, mit dem Sie Gespräche wieder entspannt genießen.',
             pts=['Hör-Therapeut im Haus', 'Pädakustik für Kinder', 'Im-Ohr-Geräte möglich'], btn='Hörberatung anfragen', pop='Hörberatung beim Meister und Hör-Therapeuten.'),
    zwei=dict(ey='Schnelle Hilfe', h2='Brille kaputt? <em>Wir helfen sofort.</em>', img=J('sibo', '025'),
              txt='Ob nach einem Fahrradsturz oder an einem stressigen Tag: Unsere Kunden erzählen, wie schnell ihnen hier geholfen wurde. Rufen Sie an, wir kümmern uns.',
              pts=['Schnelle Reparatur', 'Freundliches Team', 'Ehrliche Beratung'], btn='Jetzt anrufen'),
    team=dict(ey='Über uns', h2='Handwerk, Herz <em>und Sehkomfort.</em>', img=J('sibo', '023'), mw=380, cap='Sibo Müller, Augenoptiker- und Hörakustikmeister',
              paras=['1873 eröffneten Uhrmacher Simon Immanuel Müller und seine Frau Taalke in der Rhauderwieke ein Uhrengeschäft. 1999 übernahm Sibo Müller in fünfter Generation und lenkte den Fokus auf Augenoptik und Hörakustik.',
                     'Freude am Umgang mit Menschen, hohe Fachkompetenz und Leidenschaft für Brillen, Hörsysteme, Schmuck und Uhren: Dafür steht das Team von Sibo Müller.'],
              tl=[('1873', 'gegründet'), ('5.', 'Generation')]),
    gal=[(J('sibo', '026'), '50% 50%'), (J('sibo', '027'), '50% 50%')],
    hours=[('Mo bis Fr', '9–13 · 14–18 Uhr'), ('Sa', '9–13 Uhr')], cats=['brille', 'gleit', 'hoer', 'hg', 'kind', 'ring'], bot='Tala', notfall=REP, mq_end='Augenoptik und Hörakustik in Rhauderfehn',
    ab2='Bringen Sie Ihre Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit für Ihre Fragen.',
    rec={'brille': ['Brillenmode und Gläser', 'Wir beraten ehrlich, auch wenn eine Brille nicht passt.'], 'gleit': ['Brillenmode und Gläser', 'Gleitsicht wird bei uns genau vermessen.'], 'hoer': ['Hörsysteme', 'Am besten mit einer Hörberatung anfangen.'],
         'hg': ['Hörsysteme', 'Kommen Sie vorbei, wir helfen Ihnen weiter.'], 'kind': ['Kinder', 'Kinderbrillen und Pädakustik mit viel Geduld.'], 'ring': ['Trauringe und Gehörschutz', 'Trauringe und Schmuck gibt es direkt bei uns.']},
    pops=[('pr.jpg', 'Hörakustik', 'Beratung beim Meister und Hör-Therapeuten.'), ('g1.jpg', 'Seit 1873', 'Familienbetrieb in fünfter Generation.')]))

# 6 ─ Lonnemann sehen | hören | erleben, Spelle
mk('lonnemann', dict(google=(4.8, 48), slug='lonnemann-sehen-hoeren-spelle', firma='Lonnemann sehen | hören | erleben', kurz='Lonnemann', name='Mariele Lonnemann', ort='Spelle', strasse='Hauptstraße 26', plz='48480',
    tel='05977 928788', tel_i='+495977928788', mail='spelle@lonnemann-optiks.de', web='lonnemann-optiks.de', p='#ed5306', dk='#2b2b2b', s2='#fbf4ef', em='#c74404', fam=HEEBO, fonts='r14bec', branche='Augenoptik und Hörakustik', tt='Augenoptik und Hörakustik',
    logo=(KO + 'lonnemann-logo.png', 300), lh=60, hero='l', himgs=[J('lonnemann', '004'), J('lonnemann', '004')], cols='50fr 50fr', card='1/1',
    ey='Augenoptik & Hörakustik aus Meisterhand · Spelle und Emsbüren', h1='Sehen. Hören. <em>Erleben.</em>',
    sub='Lonnemann steht in Spelle und Emsbüren seit vielen Jahren als Familienunternehmen für bestes Sehen und Hören. Mit viel Zeit, modernster Technik und einem eingespielten Team.',
    ubar=[('2 Standorte', 'Spelle, Emsbüren'), ('Sehanalyse', 'in 6 Schritten'), ('Führerschein-Sehtest', 'kostenfrei')],
    sv_h2='Wir geben uns nicht <em>mit dem Zweitbesten zufrieden.</em>', sv_lead='Erfahrung, handwerkliches Geschick und modernste Technik: So passen wir Brille, Kontaktlinse und Hörsystem perfekt an.',
    svcs=[('Sehanalyse', 'In sechs Schritten zu besserem Sehen, von der Sehkraft bis zur Optimierung beim Lesen.'),
          ('Brillen und Officebrillen', 'Aktuelle Brillenmode und Gläser für Bildschirm, Schreibtisch und Alltag.'),
          ('Hörsysteme', 'Hörsysteme der neuesten Generation, individuell angepasst.'),
          ('Pädakustik', 'Hörgeräte für Kinder vom ersten Lebensmonat an, betreut von unserer Pädakustikerin.'),
          ('Kontaktlinsen', 'Anpassung in vier Schritten, Nachbestellung in 60 Sekunden.'),
          ('Vergrößernde Sehhilfen', 'Lupenbrillen und Sehhilfen, wenn die normale Brille nicht mehr reicht.')],
    top=dict(nav='Kinder', tag='Pädakustik', h2='Gutes Hören <em>für Ihr Kind.</em>', img=J('lonnemann', '044'),
             txt='Jedes Kind ist einzigartig. Deshalb kümmert sich bei uns ausschließlich unsere speziell ausgebildete Pädakustikerin um Ihr Kind, mit kindgerechter Mess- und Anpasstechnik und Hörgeräten namhafter Hersteller.',
             pts=['Eigene Pädakustikerin', 'Kindgerechte Atmosphäre', 'Zubehör für Schule und Handy'], btn='Pädakustik-Termin anfragen', pop='Unsere Pädakustikerin kümmert sich um Ihr Kind.'),
    zwei=dict(ey='Extras', h2='Passbilder sofort <em>zum Mitnehmen.</em>', img=J('lonnemann', '003'),
              txt='Biometrische Passbilder bekommen Sie bei uns ohne Termin in Spelle und Emsbüren. Dazu Uhrenbatteriewechsel und den kostenlosen Führerscheinsehtest als amtlich anerkannte Sehteststelle.',
              pts=['Passbilder ohne Termin', 'Führerscheinsehtest kostenfrei', 'Uhrenbatterie-Service'], btn='Termin anfragen'),
    team=dict(ey='Über uns', h2='Ihre Profis für <em>gutes Sehen und Hören.</em>', img=J('lonnemann', '001'), cap='Lonnemann in Spelle',
              paras=['Bei Lonnemann geben wir täglich unser Bestes, damit Sie perfekt sehen und hören. Dafür setzen wir auf Aus- und Weiterbildung, modernste Mess- und Anpasstechnik und langjährige Erfahrung.',
                     'Inhaberin Mariele Lonnemann ist Augenoptikermeisterin. Unser Service begleitet Sie auch lange nach dem Kauf Ihrer Brille oder Ihres Hörsystems.'],
              tl=[('Spelle', 'Hauptstraße 26'), ('Emsbüren', 'zweites Geschäft')]),
    gal=[(J('lonnemann', '002'), '50% 50%'), (J('lonnemann', '008'), '50% 50%'), (J('lonnemann', '011'), '50% 50%')],
    hours=[('Mo', 'geschlossen'), ('Di bis Fr', '9–12.30 · 14–18 Uhr'), ('Sa', '9–12.30 Uhr')], cats=['brille', 'gleit', 'hoer', 'kind', 'kl', 'sehtest'], bot='Lotte', notfall=REP, mq_end='sehen · hören · erleben',
    ab2='Bringen Sie Ihre Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Termine außerhalb der Öffnungszeiten sind nach Absprache möglich.',
    rec={'brille': ['Brillen und Officebrillen', 'Wir beraten Sie ganz ohne Zeitdruck.'], 'gleit': ['Sehanalyse', 'Ab 40 prüfen wir gezielt das Sehen in der Nähe.'], 'hoer': ['Hörsysteme', 'Am besten mit einer Hörberatung anfangen.'],
         'kind': ['Pädakustik', 'Unsere Pädakustikerin ist für Kinder da.'], 'kl': ['Kontaktlinsen', 'Anpassung in vier Schritten.'], 'sehtest': ['Sehanalyse', 'In sechs Schritten zu besserem Sehen.']},
    pops=[('pr.jpg', 'Pädakustik', 'Gutes Hören für Ihr Kind.'), ('el.jpg', 'Passbilder', 'Sofort zum Mitnehmen, ohne Termin.')]))

# 7 ─ Optik Klötgen, Freren
mk('kloetgen', dict(google=(4.8, 12), slug='optik-kloetgen-freren', firma='Optik Klötgen', kurz='Optik Klötgen', name='Dirk Klötgen', ort='Freren', strasse='Bahnhofstraße 21', plz='49832',
    tel='05902 7627', tel_i='+4959027627', mail='optik-kloetgen@ewe.net', web='optikklötgen.de', p='#192da8', dk='#1c2340', s2='#f3f4fa', fam=OS, fonts='r16ellers',
    logo_txt='Optik Klötgen<small>Bestes Sehen in allen Bereichen</small>', hero='l', himgs=[J('kloetgen', '017'), J('kloetgen', '017')], cols='50fr 50fr',
    ey='Familienunternehmen · Freren', h1='Bestes Sehen <em>in allen Bereichen.</em>',
    sub='Jahrzehntelange Erfahrung und die Innovationskraft der zweiten Generation: Mit Wissen aus Meisterhand und neuester Messtechnik finden wir Ihre Brille.',
    ubar=[('2. Generation', 'Familienbetrieb'), ('Computer-Sehtest', 'kostenlos'), ('3D-Refraktion', 'Brillenglasbestimmung')],
    sv_h2='Unser <em>Service.</em>', sv_lead='Eine große Auswahl modischer Brillen und Kontaktlinsen zu bezahlbaren Preisen. Lassen Sie sich in Ruhe beraten.',
    svcs=[('Computer-Sehtest', 'Kostenlos und schnell: der erste Blick auf Ihre Sehkraft.'),
          ('Allround Check-Up', 'Wellenfrontanalyse, Hornhauttopographie und Augeninnendruckmessung.'),
          ('Brillen', 'Modische Brillen zu bezahlbaren Preisen, mit Foto-Brillen-Beratung am Computer.'),
          ('Kontaktlinsen', 'Anpassung mit genauer Vermessung Ihrer Hornhaut.'),
          ('Pass- und Bewerbungsfotos', 'Fotos für Ausweis, Führerschein und Bewerbung.'),
          ('Uhren und Batterieservice', 'Uhren mit 2 Jahren Garantie, Batteriewechsel meist in wenigen Minuten.')],
    top=dict(nav='Check-Up', tag='Allround Check-Up', h2='Ihr Sehtest. <em>Mit Rundum-Check.</em>', img=J('kloetgen', '009'),
             txt='Jedes Auge hat eine einzigartige Architektur. Deshalb verbinden wir Ihren Sehtest mit einem Allround Check-Up: Tag- und Nachtfehlsichtigkeit, Hornhaut, Augeninnendruck und Wellenfrontmessung mit 1/100 Dioptrien.',
             pts=['Tag- und Nachtsehen', 'Vermessung der Hornhaut', 'Messung des Augeninnendrucks'], btn='Check-Up-Termin anfragen', pop='Sehtest mit Allround Check-Up.'),
    team=dict(ey='Das sind wir', h2='Erfahrung trifft <em>zweite Generation.</em>', img=J('kloetgen', '003'), cap='Das Team von Optik Klötgen',
              paras=['Als traditionelles Familienunternehmen bietet Optik Klötgen eine Beratung, die genau auf Sie abgestimmt ist, und einen besonders umfassenden Service.',
                     'Geschäftsführer Dirk Klötgen ist Augenoptikermeister. Unser Ziel ist, dass Sie lange zufrieden mit Ihrer Brille oder Kontaktlinse sind.'],
              tl=[('Freren', 'Bahnhofstraße 21'), ('Meister', 'im Haus')]),
    gal=[(J('kloetgen', '002'), '50% 50%'), (J('kloetgen', '016'), '50% 30%'), (J('kloetgen', '022'), '50% 50%')],
    hours=[('Mo, Di, Do, Fr', '9–12.30 · 14.30–18 Uhr'), ('Mi, Sa', '9–12.30 Uhr')], cats=['brille', 'gleit', 'kl', 'sehtest', 'rep'], bot='Kira', notfall=REP, mq_end='Augenoptik in Freren',
    rec={'brille': ['Brillen', 'Große Auswahl zu bezahlbaren Preisen.'], 'gleit': ['Brillen', 'Wir messen mit 3D-Refraktion.'], 'kl': ['Kontaktlinsen', 'Wir vermessen Ihre Hornhaut genau.'],
         'sehtest': ['Computer-Sehtest', 'Der Computer-Sehtest ist kostenlos.'], 'rep': ['Brillen', 'Kommen Sie vorbei, wir helfen Ihnen.']},
    pops=[('pr.jpg', 'Allround Check-Up', 'Sehtest mit Rundum-Check.'), ('g1.jpg', 'Optik Klötgen', 'Besuchen Sie uns in Freren.')]))

# 8 ─ Lütkeniehoff, Wietmarschen
mk('luetkeniehoff', dict(google=(5.0, 65), slug='luetkeniehoff-wietmarschen', firma='Lütkeniehoff Augenoptik & Hörakustik', kurz='Lütkeniehoff', name='Miriam Altenschulte', ort='Wietmarschen', strasse='Lingener Straße 8', plz='49835',
    tel='05925 333', tel_i='+495925333', mail='info@xn--ltkeniehoff-thb.de', web='lütkeniehoff.de', p='#a21e0b', dk='#3a1410', s2='#f8f3f2', fam=MON, fonts='r14egg', branche='Augenoptik und Hörakustik', tt='Augenoptik und Hörakustik',
    logo=(KO + 'luetkeniehoff-logo.png', 340), lh=56, hero='r', himgs=[J('luetkeniehoff', '033'), J('luetkeniehoff', '033')], cols='46fr 54fr',
    ey='Familienunternehmen seit 1957 · Wietmarschen, Lohne, Twist', h1='Mit Fachkompetenz <em>und Leidenschaft.</em>',
    sub='In entspannter und freundlicher Atmosphäre stehen Ihre Seh- und Hörbedürfnisse im Mittelpunkt. Ganz individuell und mit modernster Technik.',
    ubar=[('Seit 1957', 'Familienbetrieb'), ('3 Filialen', 'Wietmarschen, Lohne, Twist'), ('Meisterin', 'Augenoptik und Hörakustik')],
    sv_h2='Alle guten Dinge <em>sind drei.</em>', sv_lead='Augenoptik, Hörakustik, Uhren und Schmuck: Unsere Filialen beeindrucken mit ganz unterschiedlicher Expertise.',
    svcs=[('Augenoptik', 'Brillen für Büro, Lesen und unterwegs. Die passenden Gläser und Fassungen machen den Unterschied.'),
          ('Gleitsicht', 'Ausführliche Beratung, damit die erste Gleitsicht gleich gut sitzt.'),
          ('Hörakustik', 'Hörgeräte mit viel Geduld und Verständnis angepasst.'),
          ('Kontaktlinsen', 'Individuell angepasst und gut betreut.'),
          ('Uhren und Schmuck', 'Schmuck, der tickt. Uhren, die glänzen. Mit Goldschmied und Uhrmacher.'),
          ('Service', 'Reparaturen für Brillen, Uhren und Schmuck aus eigener Hand.')],
    top=dict(nav='Hören', tag='Hörakustik', h2='Das kann sich <em>hören lassen.</em>', img=J('luetkeniehoff', '039'),
             txt='Wir begleiten Sie mit Geduld, Freundlichkeit und Verständnis. Inhaberin Miriam Altenschulte ist Augenoptik- und Hörakustikmeisterin und berät Sie persönlich und gründlich.',
             pts=['Persönliche Beratung', 'Flexible Termine', 'Anpassung in Ruhe'], btn='Hörberatung anfragen', pop='Hörberatung mit viel Geduld.'),
    zwei=dict(ey='Uhren & Schmuck', h2='Schmuck, der tickt. <em>Uhren, die glänzen.</em>', img=J('luetkeniehoff', '044'),
              txt='Mit diesem Fachgeschäft fing 1957 alles an. Bis heute beraten Sie bei uns Fachkräfte für Uhren und Schmuck, mit Goldschmied und Uhrmacher im Team.',
              pts=['Goldschmied im Team', 'Uhrmacher im Team', 'Große Auswahl'], btn='Beratung anfragen'),
    team=dict(ey='Historie', h2='Aus der Tradition <em>geboren.</em>', img=J('luetkeniehoff', '029'), mw=460, cap='Aus der Firmengeschichte seit 1957',
              paras=['1957 eröffneten Heinrich und Agnes Lütkeniehoff das erste Fachgeschäft für Uhren und Schmuck in Wietmarschen. 1986 kam unter Sigrid und Manfred Lütkeniehoff die Augenoptik dazu.',
                     'Heute führt Miriam Altenschulte, geborene Lütkeniehoff, das Familienunternehmen in dritter Generation, mit Filialen in Wietmarschen, Lohne und Twist.'],
              tl=[('1957', 'gegründet'), ('3.', 'Generation')]),
    gal=[(J('luetkeniehoff', '034'), '50% 30%'), (J('luetkeniehoff', '036'), '50% 30%'), (J('luetkeniehoff', '045'), '50% 30%')],
    hours=[('Mo bis Fr', '8.30–12.30 · 14–18 Uhr'), ('Sa', '8.30–12.30 Uhr')], cats=['brille', 'gleit', 'hoer', 'hg', 'kl', 'ring'], bot='Mira', notfall=REP, mq_end='Augenoptik und Hörakustik in Wietmarschen',
    ab2='Bringen Sie Ihre Brille oder Ihr Hörgerät mit, wenn Sie eins haben. Wir nehmen uns Zeit für Ihre Fragen.',
    rec={'brille': ['Augenoptik', 'Wir beraten Sie zu Gläsern und Fassung.'], 'gleit': ['Gleitsicht', 'Für die erste Gleitsicht nehmen wir uns besonders viel Zeit.'], 'hoer': ['Hörakustik', 'Am besten mit einer Hörberatung anfangen.'],
         'hg': ['Hörakustik', 'Kommen Sie vorbei, wir helfen Ihnen weiter.'], 'kl': ['Kontaktlinsen', 'Kontaktlinsen passen wir individuell an.'], 'ring': ['Uhren und Schmuck', 'Goldschmied und Uhrmacher sind im Team.']},
    pops=[('pr.jpg', 'Hörakustik', 'Beratung mit Geduld und Verständnis.'), ('el.jpg', 'Uhren & Schmuck', 'Schmuck, der tickt. Uhren, die glänzen.')]))

# 9 ─ Optik Busse & Keute, Rhauderfehn
mk('buskeu', dict(google=(4.8, 33), slug='optik-busse-keute-rhauderfehn', firma='Optik Busse & Keute', kurz='Busse & Keute', name='Hans Peter Keute', ort='Rhauderfehn', strasse='Rhauderwieke 3–5', plz='26817',
    tel='04952 81761', tel_i='+49495281761', mail='info@optik-busse-keute.de', web='optik-busse-keute.de', p='#ef4123', dk='#2b2e35', s2='#f6f4f3', em='#c9301a', fam=POP, fonts='r14sch',
    logo=(J('buskeu', '004'), 300), lh=56, hero='team', himgs=[J('buskeu', '001'), J('buskeu', '001')],
    ey='Ihr Optiker im Medical Center · Rhauderfehn', h1='Ihr Team <em>für klare Sicht.</em>',
    sub='Gut sehen, gut aussehen: Bei uns finden Sie die Brille für klare Sicht und Ihren Stil. Auf über 90 Quadratmetern mitten im Herzen von Rhauderfehn.',
    ubar=[('90 m²', 'Brillenauswahl'), ('IGA Optic', 'Top-Mode, faire Preise'), ('Sa geöffnet', '9–13 Uhr')],
    sv_h2='Fachberatung <em>trifft Vielfalt.</em>', sv_lead='Ob stilvolle Fassung oder individuelle Gläser: Wir verbinden Handwerkskunst mit modischen und funktionalen Lösungen.',
    svcs=[('Brillen', 'Modische Fassungen und hochwertige Gläser zu besten Konditionen.'),
          ('Gleitsichtberatung', 'Ausführliche Beratung, damit Sie mit Ihrer Gleitsicht gut zurechtkommen.'),
          ('Sonnenbrillen', 'Sonnenbrillen, auch mit Ihrer Stärke.'),
          ('Sportbrillen', 'Angler-, Schieß- und Motorradbrillen für Ihr Hobby.'),
          ('Monoframe', 'Besondere Fassungen für einen besonderen Look.'),
          ('Kontaktlinsen', 'Probelinsen und Beratung, freundlich und kompetent.')],
    top=dict(nav='Gleitsicht', tag='Gleitsichtglasberatung', h2='Gleitsicht, <em>die zu Ihnen passt.</em>', img=J('buskeu', '002'),
             txt='Wer zum ersten Mal Gleitsicht trägt, hat viele Fragen. Wir nehmen uns Zeit, messen genau und erklären Ihnen, worauf es ankommt. So gewöhnen Sie sich schnell an Ihre neue Brille.',
             pts=['Genaue Messung', 'Verständlich erklärt', 'Nachbetreuung inklusive'], btn='Gleitsicht-Beratung anfragen', pop='Gleitsicht in Ruhe beraten.'),
    zwei=dict(ey='Für Ihr Hobby', h2='Brillen für Angler, <em>Schützen und Biker.</em>', img=J('buskeu', '003'),
              txt='Für den Angelsee, den Schießstand oder das Motorrad gibt es bei uns passende Spezialbrillen. Wir beraten Sie, welche Gläser für Ihr Hobby am besten sind.',
              pts=['Anglerbrillen', 'Schießbrillen', 'Motorradbrillen'], btn='Beratung anfragen'),
    team=dict(ey='Wir über uns', h2='Betreuung <em>mit Herz.</em>', img=J('buskeu', '005'), cap='Unser Fachgeschäft im Medical Center Rhauderfehn',
              paras=['Unser modernes Fachgeschäft liegt mitten im Herzen von Rhauderfehn im 2010 neu errichteten Medical Center. Unser Anliegen: hochwertige Brillen und Kontaktlinsen zu günstigen Konditionen.',
                     'Als Mitglied der Einkaufsgemeinschaft IGA Optic bieten wir Top-Mode zu einem fairen Preis. Schauen Sie rein und lassen Sie sich beraten.'],
              tl=[('Medical Center', 'Rhauderwieke 3–5'), ('IGA Optic', 'Mitglied')]),
    gal=[(J('buskeu', '007'), '50% 50%'), (J('buskeu', '009'), '50% 50%'), (J('buskeu', '021'), '50% 50%')],
    hours=[('Mo bis Fr', '9–13 · 14–18 Uhr'), ('Sa', '9–13 Uhr')], cats=['brille', 'gleit', 'kl', 'sehtest', 'rep'], bot='Fenja', notfall=REP, mq_end='Ihr Optiker in Rhauderfehn',
    rec={'brille': ['Brillen', 'Top-Mode zu fairen Preisen.'], 'gleit': ['Gleitsichtberatung', 'Wir nehmen uns Zeit und messen genau.'], 'kl': ['Kontaktlinsen', 'Probelinsen gibt es nach Beratung.'],
         'sehtest': ['Brillen', 'Rufen Sie kurz an unter 04952 81761.'], 'rep': ['Brillen', 'Kommen Sie vorbei, wir helfen Ihnen schnell.']},
    pops=[('pr.jpg', 'Gleitsicht', 'Beratung in Ruhe, genau gemessen.'), ('el.jpg', 'Für Ihr Hobby', 'Angler-, Schieß- und Motorradbrillen.')]))

# 10 ─ Optik Sürken, Papenburg-Aschendorf
mk('suerken', dict(google=(4.7, 90), slug='optik-suerken-aschendorf', firma='Optik Sürken', kurz='Sürken', name='Karl-Heinz Sürken', ort='Papenburg-Aschendorf', strasse='Große Straße 82', plz='26871',
    tel='04962 914020', tel_i='+494962914020', mail='info@suerken.de', web='suerken.de', p='#a8874a', dk='#1c1a17', s2='#f7f4ef', em='#8a6b30', fam=MAN, fonts='mykonos', branche='Augenoptik, Hörakustik und Schmuck', tt='Optik, Akustik und Schmuck',
    logo=(J('suerken', '000'), 380), lh=52, hero='r', himgs=[J('suerken', '027'), J('suerken', '027')], cols='48fr 52fr', card='4/3',
    ey='Familienunternehmen seit 1908 · 5 Filialen im Emsland und Ostfriesland', h1='Für die schönsten <em>und wichtigsten Momente.</em>',
    sub='Von Trauringen und feinem Schmuck bis zu präziser Augenoptik, Optometrie und gutem Hören: persönlich, ehrlich und mit viel Liebe zum Detail.',
    ubar=[('Seit 1908', 'Familienbetrieb'), ('5 Filialen', 'Emsland und Ostfriesland'), ('Optik · Akustik', 'Schmuck · Uhren')],
    sv_h2='Beste Sicht. <em>Bester Stil.</em>', sv_lead='Augenoptik, Hörakustik, Trauringe, Uhren und Schmuck: Bei Sürken finden Sie alles unter einem Dach.',
    svcs=[('Augenoptik', 'Moderne Augenoptik mit persönlicher Beratung.'),
          ('Optometrie und Screening', 'Genaue Messungen für einen gründlichen Blick auf Ihre Augen.'),
          ('Hörakustik', 'Individuelle Hörlösungen, auch Pädakustik für Kinder.'),
          ('Trauringe', 'Eheringe, Verlobungs- und Freundschaftsringe für die schönsten Momente.'),
          ('Uhren und Schmuck', 'Persönlichkeit und Qualität, dazu fachgerechte Reparaturen.'),
          ('Altgoldankauf und Passbilder', 'Fairer Altgoldankauf und Passbilder in der Filiale.')],
    top=dict(nav='Trauringe', tag='Ringe fürs Leben', h2='Trauringe für <em>die schönsten Momente.</em>', img=J('suerken', '019'),
             txt='Eheringe, Verlobungsringe oder Freundschaftsringe: Wir nehmen uns Zeit für Sie beide und beraten Sie persönlich, bis Sie die Ringe gefunden haben, die zu Ihnen passen.',
             pts=['Persönliche Beratung', 'Große Auswahl', 'Termin nach Wunsch'], btn='Trauring-Beratung anfragen', pop='Ringe fürs Leben, persönlich beraten.'),
    zwei=dict(ey='Augenoptik', h2='Beste Sicht. <em>Bester Stil.</em>', img=J('suerken', '014'),
              txt='Brillen, Kontaktlinsen, Low Vision und Optometrie: Unsere Augenoptikerinnen und Augenoptikermeister beraten Sie in allen fünf Filialen.',
              pts=['Brillen und Kontaktlinsen', 'Optometrie', 'Low Vision'], btn='Termin anfragen'),
    team=dict(ey='Über uns', h2='Tradition und Vertrauen <em>seit 1908.</em>', img=J('suerken', '008'), cap='Ein Fachgeschäft von Sürken',
              paras=['Seit über einem Jahrhundert steht Sürken für Qualität, Kompetenz und persönlichen Service. Gegründet 1908, verbinden wir Erfahrung mit modernster Technik.',
                     'Geführt von Karl-Heinz und Petra Sürken, sind wir mit Filialen in Aschendorf, Papenburg, Dörpen, Lathen und Weener für Sie da.'],
              tl=[('1908', 'gegründet'), ('5', 'Filialen')]),
    gal=[(J('suerken', '009'), '50% 50%'), (J('suerken', '010'), '50% 50%'), (J('suerken', '011'), '50% 50%')],
    hours=[('Mo, Di, Do, Fr', '9–13 · 14–18 Uhr'), ('Mi, Sa', '9–13 Uhr')], cats=['brille', 'gleit', 'hoer', 'kl', 'ring', 'rep'], bot='Ines', notfall=REP, mq_end='Sürken seit 1908',
    rec={'brille': ['Augenoptik', 'Persönliche Beratung in allen Filialen.'], 'gleit': ['Augenoptik', 'Wir messen genau und beraten Sie in Ruhe.'], 'hoer': ['Hörakustik', 'Am besten mit einer Hörberatung anfangen.'],
         'kl': ['Augenoptik', 'Kontaktlinsen passen wir individuell an.'], 'ring': ['Trauringe', 'Vereinbaren Sie einen Termin zur Trauring-Beratung.'], 'rep': ['Uhren und Schmuck', 'Reparaturen erledigen wir fachgerecht.']},
    pops=[('pr.jpg', 'Trauringe', 'Ringe fürs Leben.'), ('el.jpg', 'Augenoptik', 'Beste Sicht. Bester Stil.')]))
