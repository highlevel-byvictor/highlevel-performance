"""Runde 28 · Physiotherapie-Praxen um Bersenbrück. Nur Texte, Logos und Fotos der Praxen.
Heilmittelwerbegesetz: keine Heilversprechen, keine erfundenen Ergebnisse."""
from common import *
SITES = {}
PX = '/home/claude/pixa20/'
R = '/home/claude/r28raw/'
KO = R + 'komp/'
OS = ('"Open Sans",system-ui,sans-serif',) * 2; NOTO = ('"Noto Sans",system-ui,sans-serif',) * 2; LATO = ('"Lato",system-ui,sans-serif',) * 2
NUN = ('"Nunito Sans",system-ui,sans-serif',) * 2; RAL = ('"Raleway",system-ui,sans-serif',) * 2; ASAP = ('"Asap",system-ui,sans-serif',) * 2
MONT = ('"Montserrat",system-ui,sans-serif', '"Source Sans 3",system-ui,sans-serif')

CATL = {'ruecken': 'Rücken oder Nacken tun weh', 'op': 'Reha nach OP oder Unfall', 'rezept': 'Ich habe ein Rezept', 'lymph': 'Lymphdrainage', 'sport': 'Sportverletzung', 'neuro': 'Neurologie (z. B. nach Schlaganfall)',
        'kind': 'Therapie für mein Kind', 'osteo': 'Osteopathie', 'massage': 'Massage und Entspannung', 'haus': 'Hausbesuch', 'training': 'Gerätetraining', 'cmd': 'Kiefer oder Kopfschmerz (CMD)', 'job': 'Ich möchte bei Ihnen arbeiten', 'akut': 'Akuter Schmerz', 'selbst': 'Ohne Rezept (Selbstzahler)', 'becken': 'Beckenboden'}
USP = {'zeit': 'Sagen Sie am Telefon ruhig, dass Sie sich Zeit für ein Gespräch wünschen.', 'sanft': 'Sprechen Sie Ihre Sorge offen an. Das Team geht darauf ein.',
       'schnell': 'Am schnellsten geht es per Telefon.', 'klar': 'Fragen Sie nach, bis alles klar ist. Dafür ist der erste Termin da.'}

def anliegen(s, cats):
    b = ''.join(f'<a href="#kontakt" data-check="{k}">{CATL[k]}</a>' for k in cats)
    return f'<section class="an20"><div class="w"><p>Worum geht es bei Ihnen?</p><div>{b}</div></div></section>'

def notfall(s, txt):
    return f'<section class="nf20"><div class="w"><div><b>{s.get("nf_t","Schnell einen Termin?")}</b><span>{txt}</span></div><a class="btn" href="tel:{s["tel_i"]}">{PH}{s["tel"]}</a></div></section>'

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

PL = '<span><svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg></span>'

def bewerten(s, du=False):
    """Band unter den Stimmen: zufriedene Patienten zur Google-Bewertung bitten (mehr Vertrauen für Neue)."""
    t = ('Warst du zufrieden?', 'Eine kurze Bewertung hilft anderen bei der Suche nach einer guten Praxis. Danke dir!', 'Jetzt bewerten') if du else \
        ('Waren Sie zufrieden?', 'Eine kurze Bewertung bei Google hilft anderen Patienten bei der Suche nach einer guten Praxis. Herzlichen Dank!', 'Jetzt bewerten')
    return (f'<section class="bw28"><div class="w"><div><b>{t[0]}</b><span>{t[1]}</span></div>'
            f'<a class="btn" href="{gurl(s)}" target="_blank" rel="noopener">★ {t[2]}</a></div></section>')

def team28(people, ey, h2, lead, cls=''):
    p = ''.join(f'<figure data-r><div><img src="img/{i}" alt="{E(n)}" loading="lazy"></div><figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for i, n, r in people)
    return f'<section class="sec tg28 {cls}" id="team"><div class="w"><div data-r>{head(ey, h2, lead)}</div><div class="grid">{p}</div></div></section>'

def vids28(id, ey, h2, lead, items, cls=''):
    on = "var f=this.parentNode,m=f.querySelector('video');this.remove();m.controls=true;m.play()"
    f = ''.join(f'<div class="it" data-r><div class="frame"><video src="img/{v}" poster="img/{p}" preload="none" playsinline></video><button class="play" aria-label="Video abspielen" onclick="{on}">{PL}</button></div><h3>{t}</h3></div>' for v, p, t in items)
    return f'<section class="sec vg {cls}" id="{id}"><div class="w"><div data-r>{head(ey, h2, lead)}</div><div class="grid">{f}</div></div></section>'

CSS28 = '''.bw28{background:var(--s2);padding:26px 0;border-top:1px solid rgba(0,0,0,.06)}.bw28 .w{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}.bw28 b{display:block;font:800 22px var(--fh);color:var(--ink)}.bw28 span{color:var(--mute);font-size:17px}
.bw28 .btn{background:#fff;color:#161616;border:1.5px solid rgba(0,0,0,.15);border-radius:999px!important;padding:13px 22px;font-weight:700}.bw28 .btn:hover{background:var(--p);color:var(--p-ink);border-color:var(--p)}
.tg28 .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:22px;margin-top:34px}.tg28 figure{margin:0}.tg28 figure>div{aspect-ratio:3/4;overflow:hidden;background:var(--s2)}.tg28 figure:nth-child(3n+1)>div{border-radius:18px}
.tg28 img{width:100%;height:100%;object-fit:cover;object-position:50% 8%}.tg28 figcaption{margin-top:10px}.tg28 b{display:block;font:700 17px var(--fh)}.tg28 span{font-size:14.5px;color:var(--mute)}
.vg .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;margin-top:30px}.vg .frame{position:relative;aspect-ratio:16/9;background:#000;border-radius:18px;overflow:hidden}.vg video,.vg .frame img{width:100%;height:100%;object-fit:cover}.vg h3{font:700 17px var(--fh);margin-top:10px}
#jobs figure img,#zwei figure img{aspect-ratio:auto!important;height:auto!important;width:100%}
@media(max-width:900px){.tg28 .grid{grid-template-columns:1fr 1fr;gap:14px}.bw28 b{font-size:19px}}'''

def mk(k, d):
    g = d.get
    ort = d['ort']; top = d['top']; fam = d['fam']; p = d['p']; dk = d['dk']; s2 = d['s2']; pi = g('pi', '#fff')
    svcs = d['svcs']; cats = d['cats']; rec = d['rec']; du = g('du', False)
    Sie = (lambda a, b: b if du else a)
    def body(s):
        hero = d['hero']
        ub = ''.join(f'<div><b>{x}</b>{y}</div>' for x, y in d['ubar'])
        if hero == 'team':
            t = hd(s, False) + (f'<section class="ht20" id="top"><figure><img src="img/h1.jpg" alt="{E(d["hcap"])}"></figure><div class="w"><div data-r>{chip(s)}<p class="ey">{d["ey"]}</p><h1>{d["h1"]}</h1></div>'
                 f'<div data-r="2"><p class="sub">{d["sub"]}</p><div class="ctas"><a class="btn btn-a" href="#kontakt">{s["cta"]} {AR}</a><a class="btn btn-o" href="tel:{s["tel_i"]}">{PH} {s["tel"]}</a></div><div class="ub">{ub}</div></div></div></section>')
        elif hero == 'slides':
            t = hd(s) + hero_slides(s, dict(slides=['h1.jpg', 'h2.jpg'], pos=g('hpos', {}), ey=d['ey'], h1=d['h1'], sub=d['sub'], ubar=d['ubar']))
        else:
            t = hd(s, False) + hero_split(s, dict(imgs=(['h1.jpg', 'h2.jpg'] if d['himgs'][0] != d['himgs'][1] else ['h1.jpg']), cls=('card' if g('card') else ''), pos=g('hpos', {}), side=hero, big='', ubar=d['ubar'], ey=d['ey'], h1=d['h1'], sub=d['sub']))
        b = t + anliegen(s, cats).replace('Worum geht es bei Ihnen?', Sie('Worum geht es bei Ihnen?', 'Worum geht es bei dir?')) + marquee([a for a, _ in svcs] + [d.get('mq_end', f'Physiotherapie in {ort}')], 'wm')
        if g('video_first'): b += d['video_first']
        if g('stimmen'):
            b += (reviews(s, d['stimmen'], cls='alt') if g('google') else reviews_ns(s, d['stimmen'], cls='alt', h2=Sie('Das sagen <em>unsere Patienten.</em>', 'Das sagen <em>unsere Patienten.</em>')))
        b += bewerten(s, du)
        b += svc('leistungen', 'Leistungen', d['sv_h2'], d['sv_lead'], svcs[:6])
        b += promo('fokus', 'pr.jpg', top['tag'], top['h2'], top['txt'], top['pts'], top['btn'], 'alt')
        if g('zwei'):
            z = d['zwei']; b += eltern('zwei', 'el.jpg', z['ey'], z['h2'], z['txt'], z['pts'], z['btn'], rev=True)
        b += ablauf('weg', 'So läuft es ab', Sie('Anrufen, ankommen, <em>loslegen.</em>', 'Anrufen, ankommen, <em>loslegen.</em>'), Sie('So einfach kommen Sie zu uns.', 'So einfach kommst du zu uns.'), [
            ('Termin vereinbaren', Sie(f'Rufen Sie an unter {s["tel"]} oder schreiben Sie uns über das Formular. Halten Sie Ihr Rezept bereit, wenn Sie eins haben.', f'Ruf an unter {s["tel"]} oder schreib uns über das Formular. Halte dein Rezept bereit, wenn du eins hast.')),
            ('Befund und Gespräch', d.get('ab2', Sie('Beim ersten Termin hören wir zu und schauen uns genau an, wo es hakt. Danach planen wir Ihre Behandlung.', 'Beim ersten Termin hören wir zu und schauen uns genau an, wo es hakt. Danach planen wir deine Behandlung.'))),
            ('Behandlung und Übungen', d.get('ab3', Sie('Wir behandeln Sie und zeigen Ihnen Übungen, die Sie zu Hause weitermachen können.', 'Wir behandeln dich und zeigen dir Übungen für zu Hause.')))])
        tm = d['team']
        b += teamsec('ueber', tm['ey'], tm['h2'], tm['paras'], 'tm.jpg', tm['cap'], tm['tl'], cls='dk', mw=tm.get('mw'))
        if g('people'): b += team28([(f'p{i+1}.jpg', n, r) for i, (_, n, r) in enumerate(d['people'])], 'Team', d.get('people_h2', 'Die Menschen <em>hinter der Praxis.</em>'), d.get('people_lead', ''))
        if g('gal'): b += gal20('praxis', 'Einblicke', d.get('gal_h2', 'Ein Blick in <em>unsere Praxis.</em>'), [(f'g{i+1}.jpg', pos) for i, (_, pos) in enumerate(d['gal'])])
        if g('vids'): b += vids28('videos', 'Videos', d.get('vids_h2', 'Schauen Sie <em>uns zu.</em>'), d.get('vids_lead', ''), [(f'v{i+1}.mp4', f'v{i+1}.jpg', t) for i, (_, _, t) in enumerate(d['vids'])])
        if g('job'):
            j = d['job']; b += eltern('jobs', 'jb.jpg', 'Karriere', j['h2'], j['txt'], j['pts'], 'Jetzt melden', rev=False)
        b += notfall(s, d['notfall']) + contact(s)
        b += pops20([('pr.jpg', 'Aus der Praxis', top['tag'], top['pop'], s['cta'])] + [(im, 'Aus der Praxis', a, tx, s['cta']) for im, a, tx in d['pops']])
        return b + footer(s)
    opts = [a for a, _ in svcs] + (['Bewerbung'] if g('job') else []) + ['Sonstiges']
    nav = [('Leistungen', 'leistungen'), (top['nav'], 'fokus'), ('Team', 'team' if g('people') else 'ueber')] + ([('Jobs', 'jobs')] if g('job') else []) + [('Kontakt', 'kontakt')]
    S = SITES[k] = site(
        slug=d['slug'], firma=d['firma'], web=d['web'], fonts=d['fonts'], branche=d.get('branche', 'Physiotherapie'), du=du,
        title=f'{d["firma"]} – {d.get("tt", "Physiotherapie")} in {ort}', desc=f'{d["firma"]} in {ort}: ' + ', '.join(a for a, _ in svcs[:5]) + '.',
        tel=d['tel'], tel_i=d['tel_i'], mail=g('mail', ''), adresse=f'{d["strasse"]}, {d["plz"]} {ort}', google=g('google'),
        cta=d.get('cta', 'Termin anfragen'), nav=nav,
        hours=d['hours'], form_opts=opts, form_h3=d.get('cta', 'Termin anfragen'), form_p=Sie('Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', 'Sag uns kurz, worum es geht. Wir melden uns bei dir.'), form_btn='Rückruf anfordern',
        kt_ey='Kontakt', kt_h2=Sie('Wir sind <em>für Sie da.</em>', 'Wir sind <em>für dich da.</em>'), kt_p=Sie('Rufen Sie an oder schreiben Sie uns. Wir melden uns so schnell wie möglich.', 'Ruf an oder schreib uns. Wir melden uns so schnell wie möglich.'),
        vars=V.format(ink='#1b1d22', mute='#4d535c', p=p, pi=pi, dk=dk, s2=s2, fh=fam[0], fb=fam[1], lh=g('lh', 58), ft=dk),
        css=f'''.h2,.hz h1,.hs h1{{font-weight:800;letter-spacing:-.02em}}.h2 em,.hz h1 em,.ht20 h1 em{{font-style:normal;color:{g('em', p)}}}.hs h1 em{{font-style:normal;color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}.dk .h2 em{{color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}
.mq.wm span{{font-weight:700;font-size:15px}}.alt{{background:var(--s2)}}.sv .row div{{border-top:4px solid {p}}}.rd .road div h3{{color:{g('em', p)}}}.hs .ubar b{{color:#fff}}.hs .ey{{color:#fff!important}}.ft img{{background:#fff;padding:8px 12px;height:66px}}
.promo .tag{{background:{p};color:{pi}}}.el .ey,.ht20 .ey{{color:{g('em', p)}}}
@media(max-width:820px){{.hz h1,.hs h1{{font-size:31px!important;hyphens:none!important;overflow-wrap:normal!important;word-break:normal!important}}}}''' + CSS20 + CSS28)
    card = (f'@media(min-width:901px){{.hz.card{{min-height:min(90vh,800px)}}.hz.card .hz-img{{align-self:center;min-height:0;aspect-ratio:{g("card")};margin:130px clamp(24px,4vw,64px) 60px;border-radius:18px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.18)}}.hz.card .sl img{{animation:none}}}}@media(max-width:900px){{.hz.card .hz-img{{height:auto!important;min-height:0!important;aspect-ratio:{g("card")};margin-top:72px}}}}' if g('card') else '')
    S['css2'] = (f'.promo{{--prmw:{g("prmw")}px}}' if g('prmw') else '') + (f'#zwei figure{{max-width:{g("elmw")}px;justify-self:center}}' if g('elmw') else '') + (f'#jobs figure{{max-width:{g("jbmw")}px;justify-self:center}}' if g('jbmw') else '') + (f'.tg28 figure>div{{aspect-ratio:{g("par")}}}.tg28 img{{object-position:50% 30%}}' if g('par') else '') + card + f'.hz{{--hz-bg:{s2};--hz-ink:#1b1d22;--hz-mute:#4d535c;--hz-stroke:rgba(0,0,0,.07);--hz-cols:{g("cols", "46fr 54fr")}}}.hz h1{{font-size:clamp(34px,4.1vw,64px)}}.hz .ey{{color:{g("em", p)}}}' + g('css2', '')
    S['rv_h2'] = 'Das sagen unsere <em>Patienten.</em>'
    if g('logo_txt'): S['logo_txt'] = d['logo_txt']
    if g('stimmen') and not g('google'): S['voices'] = True
    if g('gr'): S['gr'] = g('gr')
    S['nf_t'] = d.get('nf_t', Sie('Schnell einen Termin?', 'Schnell einen Termin?'))
    hl = Sie('Guten Tag', 'Hallo')
    S['bot'] = dict(auto=False, say=Sie(f'Hallo, ich bin <b>{d["bot"]}</b>, Ihr KI-Assistent. Ich führe Sie durch die Website.', f'Hallo, ich bin <b>{d["bot"]}</b>, dein KI-Assistent. Ich führe dich durch die Website.'),
        name=d['bot'], tag=d.get('bot_tag', 'Ihr Praxis-Lotse' if not du else 'Dein Praxis-Lotse'), du=du, tel=d['tel'], tel_i=d['tel_i'], notfall=d['notfall'], finBtn=d.get('cta', 'Termin anfragen'),
        hello=Sie(f'{hl}! Ich bin <b>{d["bot"]}</b>, der digitale Lotse von {d["kurz"]}. Soll ich Ihnen helfen, schnell das Richtige zu finden?', f'{hl}! Ich bin <b>{d["bot"]}</b>, der digitale Lotse von {d["kurz"]}. Soll ich dir helfen, schnell das Richtige zu finden?'),
        hi=Sie(f'{hl}, ich bin {d["bot"]}. Ich stelle Ihnen drei kurze Fragen und zeige Ihnen, was hier zu Ihrem Anliegen passt.', f'{hl}, ich bin {d["bot"]}. Ich stelle dir drei kurze Fragen und zeige dir, was hier zu deinem Anliegen passt.'),
        cats=[[CATL[c], c] for c in cats], rec=rec, usp=USP, ex='Öffnungszeiten, Leistungen oder Terminen',
        qa=[['zeit|geöffnet|sprech|offen|öffnung', 'Die Öffnungszeiten: ' + ', '.join(f'{a} {b}' for a, b in d['hours']) + '.'],
            ['wo|adresse|anfahrt|park', f'Die Praxis findest du hier: {d["strasse"]}, {d["plz"]} {ort}.' if du else f'Sie finden uns hier: {d["strasse"]}, {d["plz"]} {ort}.'],
            ['leistung|angebot|macht ihr|bieten', 'Zum Beispiel: ' + ', '.join(a for a, _ in svcs[:6]) + '.'],
            ['rezept|verordnung|kasse|krankenkasse|zuzahlung|privat', Sie('Mit ärztlicher Verordnung rechnen wir mit Ihrer Krankenkasse ab. Alles Weitere klären wir gern am Telefon.', 'Mit ärztlicher Verordnung rechnen wir mit deiner Krankenkasse ab. Alles Weitere klären wir gern am Telefon.')],
            ['job|stelle|bewerb|arbeiten|karriere', (Sie('Wir freuen uns über Verstärkung! Melden Sie sich einfach über das Formular oder per Telefon.', 'Wir freuen uns über Verstärkung! Melde dich einfach über das Formular oder per Telefon.') if g('job') else 'Fragen Sie gern direkt in der Praxis nach.')],
            ['kosten|preis', Sie('Das hängt von der Behandlung ab. Am besten fragen Sie direkt in der Praxis, dort bekommen Sie eine ehrliche Auskunft.', 'Das hängt von der Behandlung ab. Frag am besten direkt in der Praxis nach.')]],
        tour=[['#leistungen', 'Das finden Sie hier.' if not du else 'Das findest du hier.'], ['#fokus', f'Ein Schwerpunkt: {top["tag"]}.'], ['#weg', 'So läuft Ihr Termin ab.' if not du else 'So läuft dein Termin ab.'], ['#ueber', 'Hier lernen Sie das Team kennen.' if not du else 'Hier lernst du das Team kennen.'], ['#kontakt', 'Und hier fragen Sie Ihren Termin an.' if not du else 'Und hier fragst du deinen Termin an.']])
    im = {'h1.jpg': (d['himgs'][0], 1800), 'h2.jpg': (d['himgs'][1], 1800), 'pr.jpg': (top['img'], 1400), 'tm.jpg': (d['team']['img'], 1400)}
    if g('logo'): im['logo.png'] = d['logo']
    if g('zwei'): im['el.jpg'] = (d['zwei']['img'], 1400)
    if g('job'): im['jb.jpg'] = (d['job']['img'], 1400)
    for i, (src, _) in enumerate(g('gal', [])): im[f'g{i+1}.jpg'] = (src, 1200)
    for i, (src, _, _) in enumerate(g('people', [])): im[f'p{i+1}.jpg'] = (src, 700)
    for i, (v, po, _) in enumerate(g('vids', [])): im[f'v{i+1}.mp4'] = (v, 0); im[f'v{i+1}.jpg'] = (po, 1000)
    for x in g('extra_img', {}).items(): im[x[0]] = x[1]
    S['img'] = im; S['body'] = body

def J(k, n):
    import glob
    f = glob.glob(f'{R}{k}/img/i{n}.*'); assert f, (k, n); return f[0]

OS = ('"Open Sans",system-ui,sans-serif',) * 2; LATO = ('"Lato",system-ui,sans-serif',) * 2; SSANS = ('"Source Sans 3",system-ui,sans-serif',) * 2
TIT = ('"Titillium Web",system-ui,sans-serif',) * 2; POP = ('"Poppins",system-ui,sans-serif',) * 2; MON = ('"Montserrat",system-ui,sans-serif',) * 2
MAN = ('"Manrope",system-ui,sans-serif',) * 2; NUN = ('"Nunito",system-ui,sans-serif',) * 2; RUB = ('"Rubik",system-ui,sans-serif',) * 2
ROB = ('"Roboto",system-ui,sans-serif',) * 2; FIRA = ('"Fira Sans",system-ui,sans-serif',) * 2; SORA = ('"Sora",system-ui,sans-serif', '"Nunito Sans",system-ui,sans-serif')
JOS = ('"Josefin Sans",system-ui,sans-serif', '"Lato",system-ui,sans-serif'); ARCH = ('"Archivo",system-ui,sans-serif',) * 2
NF = 'Rufen Sie an, wir finden schnell einen passenden Termin. Mit Rezept rechnen wir direkt mit Ihrer Kasse ab.'
NF_DU = 'Ruf an, wir finden schnell einen passenden Termin. Mit Rezept rechnen wir direkt mit deiner Kasse ab.'

# 1 ─ Physiotherapie Oliver Nuss, Bersenbrück
mk('nuss', dict(google=(4.7, 9), slug='physiotherapie-oliver-nuss-bersenbrueck', firma='Physiotherapie Oliver Nuss', kurz='Physiotherapie Nuss', ort='Bersenbrück', strasse='Lindenstraße 11', plz='49593',
    tel='05439 609509', tel_i='+495439609509', mail='physiotherapie.nuss@gmx.de', web='physiotherapieolivernuss.de', p='#2aa6a2', dk='#173a5c', s2='#eef7f7', fam=('"Oswald",system-ui,sans-serif', '"Open Sans",system-ui,sans-serif'), fonts='r10daelken',
    logo=(J('nuss', '000'), 360), lh=62, hero='team', himgs=[J('nuss', '004'), J('nuss', '004')], hcap='Das Team der Physiotherapie Oliver Nuss in Bersenbrück',
    ey='Physiotherapie in Bersenbrück · seit 2012', h1='Ihre Gesundheit <em>in fachkundigen Händen.</em>',
    sub='Krankengymnastik, Manuelle Therapie, Lymphdrainage und mehr. Unsere Therapeuten stimmen jede Behandlung mit Ihnen und Ihrem Arzt individuell ab. Vertrauensvoll und nachhaltig.',
    ubar=[('8 Personen', 'starkes Praxisteam'), ('Seit 2012', 'in Bersenbrück'), ('Barrierefrei', 'mit Rollstuhl erreichbar')],
    sv_h2='Physiotherapie <em>und mehr.</em>', sv_lead='Von orthopädischen Beschwerden wie Bandscheibenvorfall oder Nackenproblemen bis zu neurologischen Erkrankungen: Wir behandeln individuell nach Ihren Bedürfnissen.',
    svcs=[('Krankengymnastik', 'Behandlung von Haltungs- und Bewegungsapparat, nach Verletzungen, Operationen oder bei Fehlentwicklungen.'),
          ('Manuelle Therapie', 'Gezielte Handgriffe für Gelenke und Wirbelsäule, zum Beispiel bei Beschwerden an LWS, BWS oder HWS.'),
          ('Manuelle Lymphdrainage', 'Sanfte Grifftechnik bei Schwellungen, zum Beispiel nach Operationen.'),
          ('Bobath', 'Therapie für Erwachsene mit neurologischen Erkrankungen, etwa nach einem Schlaganfall.'),
          ('Krankengymnastik an Geräten', 'Gezieltes Training im eigenen Trainingsraum der Praxis, angeleitet von unseren Therapeuten.'),
          ('Massage, Taping und mehr', 'Klassische Massage, Triggerpunkttherapie, Kinesiotaping, Extension und Elektrotherapie.')],
    top=dict(nav='Gerätetraining', tag='Krankengymnastik an Geräten', h2='Stärker werden. <em>Mit Anleitung.</em>', img=J('nuss', '023'),
             txt='In unserem hellen Trainingsraum trainieren Sie unter Anleitung unserer Therapeuten an Geräten. So bauen Sie nach Verletzung oder Operation gezielt wieder Kraft und Stabilität auf.',
             pts=['Mit ärztlicher Verordnung', 'Angeleitet von Physiotherapeuten', 'Übungen auch für zu Hause'], btn='Termin anfragen', pop='Training an Geräten, angeleitet von unseren Therapeuten.'),
    team=dict(ey='Über uns', h2='Eine junge Praxis <em>mitten in Bersenbrück.</em>', img=J('nuss', '003'), mw=380, cap='Oliver Nuss, Praxisinhaber und Physiotherapeut',
              paras=['Oliver Nuss hat die Praxis 2012 gegründet. Er ist Physiotherapeut und Heilpraktiker auf dem Gebiet der Physiotherapie, mit Fortbildungen in Manueller Therapie, Bobath, Lymphdrainage, Triggerpunkt-Therapie und struktureller Osteopathie.',
                     'Heute sind wir ein Team aus acht Personen. Die stellvertretende Leitung hat Swetlana Tellmann.'],
              tl=[('2012', 'gegründet'), ('Lindenstr. 11', 'Bersenbrück')]),
    people=[(J('nuss', '003'), 'Oliver Nuss', 'Praxisinhaber, Physiotherapeut'), (J('nuss', '006'), 'Swetlana Tellmann', 'Stellv. Leitung, Physiotherapeutin'), (J('nuss', '005'), 'Tanja Specker', 'Praxisteam'),
            (J('nuss', '007'), 'Silke Kiefer', 'Praxisteam'), (J('nuss', '008'), 'Jenny Thole', 'Praxisteam'), (J('nuss', '009'), 'Kerstin Südbeck', 'Praxisteam'), (J('nuss', '010'), 'Anette Böhmer', 'Praxisteam'), (J('nuss', '011'), 'Sabrina Krampf', 'Praxisteam')],
    gal=[(J('nuss', '021'), '50% 50%'), (J('nuss', '024'), '50% 50%'), (J('nuss', '030'), '50% 50%')],
    job=dict(img=J('nuss', '004'), h2='Wir suchen <em>Verstärkung.</em>', txt='Wir suchen ab sofort eine engagierte Physiotherapeutin oder einen engagierten Physiotherapeuten in Voll- oder Teilzeit. Ein Zertifikat in Manueller Lymphdrainage ist schön, aber kein Muss.',
             pts=['Voll- oder Teilzeit', 'Breites Behandlungsspektrum', 'Nettes Team in Bersenbrück']),
    stimmen=['Sehr gute Physiotherapeuten, die wissen, was sie tun.', 'Nach zwei Unfällen habe ich mich hier sehr wohl gefühlt. Mein Selbstvertrauen wurde in der langen Therapie wieder aufgebaut.', 'Fachlich kompetent, dazu eine Atmosphäre zum Wohlfühlen. Barrierefrei mit Rollstuhl erreichbar.', 'Meine Lieblingspraxis für Physiotherapie.'],
    hours=[('Mo bis Do', '9–18 Uhr'), ('Fr', '9–16 Uhr'), ('Weitere Termine', 'nach Absprache')], cats=['ruecken', 'op', 'rezept', 'lymph', 'neuro', 'job'], bot='Lotta', notfall=NF, mq_end='Physiotherapie in Bersenbrück',
    rec={'ruecken': ['Manuelle Therapie', 'Bei Rücken und Nacken arbeiten wir oft mit Manueller Therapie.'], 'op': ['Krankengymnastik an Geräten', 'Nach einer OP bauen wir mit Ihnen wieder Kraft auf.'], 'rezept': ['Krankengymnastik', 'Rufen Sie mit Ihrem Rezept an, wir finden einen Termin.'],
         'lymph': ['Manuelle Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'], 'neuro': ['Bobath', 'Bei neurologischen Erkrankungen behandeln wir nach Bobath.'], 'job': ['Krankengymnastik', 'Schön! Melden Sie sich gern, wir suchen Verstärkung.']},
    pops=[('g1.jpg', 'Barrierefrei', 'Unsere Praxis ist mit dem Rollstuhl gut erreichbar.'), ('jb.jpg', 'Wir suchen Verstärkung', 'Physiotherapeut/in in Voll- oder Teilzeit gesucht.')]))

# 2 ─ Nicole Vogel, Quakenbrück
mk('vogel', dict(google=(4.8, 22), slug='praxis-vogel-osteopathie-physiotherapie-quakenbrueck', firma='Praxis für Osteopathie & Physiotherapie Nicole Vogel', kurz='Praxis Vogel', ort='Quakenbrück', strasse='Lange Straße 3', plz='49610',
    tel='05431 9288789', tel_i='+4954319288789', web='vogel-osteopathie.de', p='#c8d411', pi='#1b1d22', em='#6b7400', dk='#2b2d2f', s2='#f6f7ec', fam=OS, fonts='r10daelken',
    logo=(J('vogel', '000'), 420, 'trim'), lh=58, hero='r', himgs=[J('vogel', '014'), J('vogel', '014')], hpos={'h1.jpg': '50% 15%', 'h2.jpg': '50% 15%'}, cols='46fr 54fr',
    ey='Osteopathie & Physiotherapie in Quakenbrück', h1='Ganzheitlich. Motiviert. <em>Erfahren.</em>',
    sub='Osteopathie, Physiotherapie oder Akupunktur: Bei uns finden Sie alles unter einem Dach. Mitten in Quakenbrück, am Anfang der Fußgängerzone.',
    ubar=[('Olympia 2024', 'Gold im 3x3-Basketball betreut'), ('DOSB', 'Sportphysiotherapie-Lizenz'), ('3 Räume', 'modern und hell')],
    sv_h2='Alles <em>unter einem Dach.</em>', sv_lead='Am Anfang steht immer ein ausführliches Gespräch. Dann stimmen wir die Behandlung auf Sie ab.',
    svcs=[('Osteopathie', 'Eigenständige Befund- und Behandlungsmethode mit dem geschulten Tastsinn der Hände, in guter Ergänzung zur Schulmedizin.'),
          ('Physiotherapie', 'Krankengymnastik, Lymphdrainage, Massage und physikalische Therapie mit Wärme, Kälte und Hilfsmitteln.'),
          ('Akupunktur', 'Eine der fünf Säulen der Traditionellen Chinesischen Medizin. Vorab gibt es die Chinesische Sprechstunde.'),
          ('Manuelle Lymphdrainage', 'Sanfte Grifftechniken, zum Beispiel nach Sportverletzungen oder Operationen.'),
          ('Kinesiotaping', 'Elastisches Tape, das im Sport und im Alltag eingesetzt wird.'),
          ('Ernährungsberatung', 'Sigrid Lömker unterstützt Sie dabei, Ihr Essverhalten im Alltag langfristig zu verändern.')],
    top=dict(nav='Sport', tag='Sportlerbetreuung', h2='Von der Erstversorgung <em>bis zum Comeback.</em>', img=J('vogel', '028'),
             txt='Seit über 15 Jahren ist Nicole Vogel Sportphysiotherapeutin für den Deutschen Basketball Bund. 2024 war sie mit der 3x3-Nationalmannschaft der Damen bei den Olympischen Spielen in Paris, das Team gewann Gold.',
             pts=['Osteopathie und Sportmassage', 'Lymphdrainage und Akupunktur', 'Erfahrung aus dem Spitzensport'], btn='Termin anfragen', pop='Sportphysiotherapie mit Erfahrung aus dem Spitzensport.'),
    zwei=dict(ey='Akupunktur', h2='Zuerst <em>die Chinesische Sprechstunde.</em>', img=J('vogel', '011'),
              txt='Vor der ersten Akupunktur nehmen wir uns 90 Minuten Zeit: Gespräch, Zungen- und Pulsdiagnostik. Danach entsteht ein individueller Behandlungsplan.',
              pts=['90 Minuten in ruhiger Atmosphäre', 'Ausführliches Befundgespräch', 'Individueller Plan'], btn='Sprechstunde anfragen'),
    video_first=vids28('film', 'Film', 'Einblick in <em>die Praxis Vogel.</em>', 'Ein kurzer Film aus unserer Praxis in Quakenbrück.', [('v1.mp4', 'v1.jpg', 'Die Praxis Vogel'), ('v2.mp4', 'v2.jpg', 'Osteopathie')]),
    extra_img={'v1.mp4': ('/home/claude/r28raw/vogel/vid/home_w.mp4', 0), 'v1.jpg': ('/home/claude/r28raw/vogel/vid/home_p.jpg', 1000), 'v2.mp4': ('/home/claude/r28raw/vogel/vid/osteopathie_w.mp4', 0), 'v2.jpg': ('/home/claude/r28raw/vogel/vid/osteopathie_p.jpg', 1000)},
    team=dict(ey='Über uns', h2='Das Team <em>für Ihre Gesundheit.</em>', img=J('vogel', '002'), cap='Das Team der Praxis Vogel in Quakenbrück',
              paras=['Nicole Vogel ist Osteopathin, Physiotherapeutin und Heilpraktikerin. Sie betreute unter anderem die ARTLAND DRAGONS und seit 2019 die deutschen 3x3-Basketballnationalmannschaften.',
                     'Praxismanagerin Anke Rehberg hält dem Team den Rücken frei und ist Ihre Ansprechpartnerin für Termine.'],
              tl=[('Lange Str. 3', 'Quakenbrück'), ('2 Parkplätze', 'direkt hinter der Praxis')]),
    gal=[(J('vogel', '009'), '50% 50%'), (J('vogel', '021'), '50% 40%'), (J('vogel', '024'), '50% 50%')],
    stimmen=['Nicole konnte mir bei ganz verschiedenen Beschwerden immer helfen. Sie nimmt sich Zeit und erklärt alles klar.', 'Sie behandelt nicht nur Symptome, sondern sucht die Ursache. Ich habe mich sofort wohlgefühlt.', 'Fast familiäre Atmosphäre. Hier ist man keine Nummer.', 'Freundlich, fröhlich und kompetent. Jeder wird ernst genommen.'],
    hours=[('Termine', 'nach Vereinbarung'), ('Akuttermine', 'bitte anrufen')], cats=['ruecken', 'sport', 'osteo', 'akut', 'cmd', 'selbst'], bot='Nele', notfall=NF, mq_end='Osteopathie in Quakenbrück',
    rec={'ruecken': ['Osteopathie', 'Wir suchen gemeinsam nach der Ursache Ihrer Beschwerden.'], 'sport': ['Physiotherapie', 'Sportler betreuen wir von der Erstversorgung bis zum Comeback.'], 'osteo': ['Osteopathie', 'Osteopathie beginnt mit einem ausführlichen Befundgespräch.'],
         'akut': ['Physiotherapie', 'Für akute Fälle gibt es Akuttermine. Rufen Sie an.'], 'cmd': ['Osteopathie', 'Auch Kiefer und Kopfschmerz schauen wir uns an.'], 'selbst': ['Akupunktur', 'Viele Leistungen sind auch ohne Rezept buchbar.']},
    pops=[('el.jpg', 'Akupunktur', 'Startet mit der 90-minütigen Chinesischen Sprechstunde.'), ('g1.jpg', 'Gutscheine', 'Verschenken Sie Gesundheit, Gutscheine gibt es in der Praxis.')]))

# 3 ─ Matthias Theilmann, Damme
mk('theilmann', dict(google=(5.0, 14), slug='physiotherapie-theilmann-damme', firma='Praxis für Physiotherapie Matthias Theilmann', kurz='Praxis Theilmann', ort='Damme', strasse='Achtern Hoff 23', plz='49401',
    tel='05491 1076', tel_i='+4954911076', web='praxis-theilmann.de', p='#2e9a46', dk='#1d3557', s2='#f0f6f1', em='#24803a', fam=NUN, fonts='r10borggreve',
    logo=(J('theilmann', '000'), 600, 'alphacrop'), lh=46, hero='r', card='16/9', himgs=[J('theilmann', '016'), J('theilmann', '016')], cols='44fr 56fr',
    ey='Physiotherapie & Wellness in Damme', h1='Hier fühl ich <em>mich wohl!</em>',
    sub='Das ist unser Motto und unsere Philosophie. Von der Massage über Krankengymnastik bis zur Lymphdrainage: Unser Team ist mit jahrelanger Erfahrung für Sie da, an zwei Standorten in Damme.',
    ubar=[('2 Standorte', 'in Damme'), ('Bis 20 Uhr', 'Mo bis Do'), ('Wellness', 'mit Sauna')],
    sv_h2='Physiotherapie, <em>persönlich für Sie.</em>', sv_lead='Bestens ausgebildet und persönlich auf Ihre Bedürfnisse eingehend.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie, abgestimmt auf Ihre Beschwerden.'), ('Massage', 'Klassische Massage, auch mit Fango oder Heißluft.'),
          ('Lymphdrainage', 'Sanfte Entstauung in 30 oder 45 Minuten.'), ('PNF und neurologische Behandlung', 'Therapie bei neurologischen Erkrankungen.'),
          ('Dorntherapie, Kinesiotape, Schröpfen', 'Ergänzende Methoden für Ihre Behandlung.'), ('Fußpflege', 'Fußpflege und Fußreflexzonenmassage, auch als Hausbesuch.')],
    top=dict(nav='Wellness', tag='Unsere Wellness-Welt', h2='Gönnen Sie sich <em>eine Auszeit.</em>', img=J('theilmann', '002'),
             txt='Ganzkörpermassage mit Saunabesuch und Wellnesstee oder Cranio-Sacral-Therapie: Bei uns finden Sie Ihre entspannende Auszeit. Wir beraten Sie gern nach Ihren Wünschen.',
             pts=['Massage mit Sauna und Tee', 'Cranio-Sacral-Therapie', 'Auch als Gutschein'], btn='Wellness anfragen', pop='Massage, Sauna und Tee: Ihre Auszeit in Damme.'),
    zwei=dict(ey='Zweiter Standort', h2='Praxis <em>im INJOY Damme.</em>', img=J('theilmann', '004'),
              txt='In unserer zweiten Praxis im INJOY an der Robert-Bosch-Straße verbinden wir Physiotherapie mit Training. Physiotherapeuten betreuen Sie dort auch auf der Trainingsfläche.',
              pts=['Robert-Bosch-Str. 24', 'Freitagnachmittag geöffnet', 'Physio und Training vereint'], btn='Termin anfragen'),
    team=dict(ey='Über uns', h2='Ein Team <em>mit Erfahrung.</em>', img=J('theilmann', '017'), mw=300, cap='Matthias Theilmann, Sportphysiotherapeut',
              paras=['Matthias Theilmann ist Sportphysiotherapeut und führt die Praxis mit seinem Team aus Physiotherapeutinnen, Fußpflege und Rezeption.',
                     'Das Wohlgefühl unserer Patienten ist unser oberstes Ziel.'],
              tl=[('10', 'Menschen im Team'), ('Achtern Hoff 23', 'Damme')]),
    gal=[(J('theilmann', '003'), '50% 50%'), (J('theilmann', '001'), '50% 50%'), (J('theilmann', '002'), '50% 50%')],
    job=dict(img=J('theilmann', '016'), h2='Physiotherapeut/in <em>gesucht.</em>', txt='Wir suchen erfahrene Physiotherapeuten oder Osteopathen in Vollzeit, Teilzeit oder auf Stundenbasis für unser junges, dynamisches Team.',
             pts=['Festgehalt und Zuschüsse bei Fortbildungen', 'Physio und Trainingsfläche kombiniert', 'Familiäres Betriebsklima']),
    stimmen=['Tolle Praxis mit kompetentem Team. Meine Rückenschmerzen wurden schnell besser.', 'Kurz gesagt: perfekt. Immer wieder gern, danke an das ganze Team.', 'Ich gehe seit Jahren hin. Gute und freundliche Therapeuten.', 'Sehr freundliches und kompetentes Team!'],
    hours=[('Mo bis Fr', '8–12 Uhr'), ('Mo bis Do', '15–20 Uhr'), ('Fr nachmittags', 'im INJOY')], cats=['ruecken', 'rezept', 'lymph', 'massage', 'haus', 'job'], bot='Mats', notfall=NF, mq_end='Physiotherapie in Damme',
    rec={'ruecken': ['Krankengymnastik', 'Wir schauen uns Ihren Rücken genau an.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, wir finden einen Termin, auch abends.'], 'lymph': ['Lymphdrainage', 'Lymphdrainage gibt es in 30 oder 45 Minuten.'],
         'massage': ['Massage', 'Massage gibt es auch mit Sauna und Wellnesstee.'], 'haus': ['Fußpflege', 'Fußpflege bieten wir auch als Hausbesuch an.'], 'job': ['Krankengymnastik', 'Wir suchen Verstärkung. Melden Sie sich gern!']},
    pops=[('el.jpg', 'Praxis im INJOY', 'Physio und Training an einem Ort.'), ('jb.jpg', 'Wir suchen Verstärkung', 'Physiotherapeut/in oder Osteopath/in gesucht.')]))

# 4 ─ Physiotherapie Centrum Damme
mk('damme', dict(google=(5.0, 8), slug='physiotherapie-centrum-damme', firma='Physiotherapie Centrum Damme', kurz='Physiotherapie Centrum Damme', ort='Damme', strasse='Lindenstraße 10–12', plz='49401',
    tel='05491 955400', tel_i='+495491955400', mail='physiotherapie@gesundheitscentrum.de', web='physiotherapie-damme.de', p='#c73b5e', dk='#3b2a33', s2='#f8f1f3', fam=FIRA, fonts='r12beckermann',
    logo=(J('damme', '009'), 420, 'alphacrop'), lh=42, hero='l', himgs=[J('damme', '001'), J('damme', '005')], hpos={'h1.jpg': '40% 50%', 'h2.jpg': '50% 60%'}, cols='50fr 50fr',
    ey='Im Gesundheits Centrum Damme', h1='Moderne Physiotherapie <em>in Damme.</em>',
    sub='Von Krankengymnastik und Massage über Manuelle Therapie bis zu Bewegungsbad, Trainingsraum und Osteopathie: alles unter einem Dach im Gesundheits Centrum Damme.',
    ubar=[('Bewegungsbad', 'im Haus'), ('Mo bis Fr', '8–20 Uhr'), ('Podologie', 'neu im Haus')],
    sv_h2='Mobilität. Kraft. <em>Ausdauer.</em>', sv_lead='Für eine auf Sie abgestimmte Behandlung analysieren wir zuerst Ihr Bewegungsverhalten.',
    svcs=[('Krankengymnastik', 'Mobilisation, Weichteiltechniken, Kräftigung und Dehnung, abgestimmt auf Sie.'), ('Manuelle Therapie', 'Spezielle Handgriffe, um Bewegungsstörungen an Gelenken und Wirbelsäule zu finden und zu behandeln.'),
          ('KG-ZNS Bobath', 'Therapie für Erwachsene mit neurologischen Beeinträchtigungen.'), ('Rehabilitation', 'Bewegungsbad und Trainingsraum im Erdgeschoss.'),
          ('Osteopathie', 'Mit Osteopathin Verena Püttschneider.'), ('Prävention und Wellness', 'Rückenschule, Massagen und Wärmetherapie.')],
    top=dict(nav='Bewegungsbad', tag='Bewegungsbad und Training', h2='Bewegung, <em>die leichter fällt.</em>', img=J('damme', '006'),
             txt='Im Erdgeschoss des Gesundheits Centrums haben wir ein eigenes Bewegungsbad und einen Trainingsraum. Ideal, um nach Verletzung oder Operation wieder in Bewegung zu kommen.',
             pts=['Eigenes Bewegungsbad', 'Trainingsraum mit Geräten', 'Begleitet von Therapeuten'], btn='Termin anfragen', pop='Mit eigenem Bewegungsbad und Trainingsraum.'),
    team=dict(ey='Über uns', h2='Ihr Team <em>im Centrum.</em>', img=J('damme', '016'), mw=420, cap='Aus dem Physiotherapie Centrum Damme',
              paras=['Leitung Physiotherapie: Kerstin Trenk. Unsere Räume liegen im 1. Obergeschoss und im Erdgeschoss des Gesundheits Centrums Damme an der Lindenstraße.',
                     'Neu im Haus: eine Podologin für medizinische Fußpflege.'],
              tl=[('15', 'Menschen im Team'), ('Lindenstr. 10–12', 'Damme')]),
    gal=[(J('damme', '011'), '50% 50%'), (J('damme', '003'), '50% 50%'), (J('damme', '013'), '50% 50%')],
    job=dict(img=J('damme', '020'), h2='Komm <em>in unser Team!</em>', txt='Wir brauchen Verstärkung. Werde Teil unseres Teams im Gesundheits Centrum Damme und bewirb dich jetzt.',
             pts=['Moderne Räume mit Bad und Training', 'Großes, nettes Team', 'Mitten in Damme']),
    stimmen=['Seit fünf Jahren komme ich zur Lymphdrainage und bin in den allerbesten Händen.', 'Alle sind super nett. Man fühlt sich sofort gut aufgehoben.', 'Sehr freundlich und vor allem sehr kompetent. Dafür fahre ich gern ein paar Kilometer mehr.', 'Immer freundlich, perfekter Service.'],
    hours=[('Mo bis Fr', '8–20 Uhr')], cats=['ruecken', 'op', 'rezept', 'lymph', 'neuro', 'job'], bot='Pia', notfall=NF, mq_end='Physiotherapie in Damme',
    rec={'ruecken': ['Manuelle Therapie', 'Wir finden heraus, wo die Bewegung hakt.'], 'op': ['Rehabilitation', 'Bewegungsbad und Training helfen beim Wiedereinstieg.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, wir haben bis 20 Uhr geöffnet.'],
         'lymph': ['Prävention und Wellness', 'Lymphdrainage gehört fest zu unserem Angebot.'], 'neuro': ['KG-ZNS Bobath', 'Bei neurologischen Erkrankungen arbeiten wir nach Bobath.'], 'job': ['Krankengymnastik', 'Wir suchen Verstärkung. Melde dich gern!']},
    pops=[('g2.jpg', 'Podologie', 'Neu im Haus: medizinische Fußpflege.'), ('jb.jpg', 'Wir suchen dich', 'Komm in unser Team!')]))

# 5 ─ Praxis Seebeck & Ortmann-Seebeck, Dinklage
mk('seebeck', dict(slug='physiotherapie-seebeck-dinklage', firma='Praxis Seebeck & Ortmann-Seebeck', kurz='Praxis Seebeck', ort='Dinklage', strasse='Clemens-August-Straße 3', plz='49413',
    tel='04443 978841', tel_i='+494443978841', web='thomasseebeck.de', p='#2b9fb0', dk='#333c4e', s2='#eef5f7', fam=MON, fonts='r12meyer',
    logo_txt='Praxis Seebeck<small>Physiotherapie · Dinklage</small>', hero='l', himgs=[J('seebeck', '005'), J('seebeck', '003')], cols='46fr 54fr',
    ey='Physiotherapie in Dinklage · seit 2002', h1='Der Mensch <em>im Mittelpunkt.</em>',
    sub='Seit 2002 begrüßen Thomas Seebeck und Kerstin Ortmann-Seebeck große und kleine Patienten in ihrer modernen, hellen Praxis in Dinklage.',
    ubar=[('Seit 2002', 'in Dinklage'), ('Groß und klein', 'alle willkommen'), ('Rückruf', 'schnellstmöglich')],
    sv_h2='Behandlung <em>mit Herz und Hand.</em>', sv_lead='In freundlicher und heller Atmosphäre nehmen wir uns Zeit für Sie.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie für den ganzen Bewegungsapparat.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'), ('Osteopathische Selbstbehandlung', 'Kurse, in denen Sie lernen, sich selbst etwas Gutes zu tun.'),
          ('Beckenbodentraining', 'Gezieltes Training für den Beckenboden.'), ('Kinder', 'Auch kleine Patienten sind bei uns willkommen.')],
    top=dict(nav='Kurse', tag='Osteopathische Selbstbehandlung', h2='Lernen, <em>sich selbst zu helfen.</em>', img=J('seebeck', '004'),
             txt='Thomas Seebeck ist Autor des Buchs „Die osteopathische Selbstbehandlung“. In unseren Kursen zeigen wir Ihnen Griffe und Übungen, die Sie zu Hause selbst anwenden können.',
             pts=['Kurse in der Praxis', 'Vom Buchautor selbst', 'Übungen für zu Hause'], btn='Kursplatz anfragen', pop='Kurse zur osteopathischen Selbstbehandlung.'),
    team=dict(ey='Wir sind das Team', h2='Thomas Seebeck <em>und Kerstin Ortmann-Seebeck.</em>', img=J('seebeck', '004'), cap='Die Praxis in Dinklage',
              paras=['Seit Praxisbeginn 2002 steht für uns der Mensch im Mittelpunkt. Unsere moderne Praxis begrüßt in freundlicher und heller Atmosphäre große und kleine Patienten.',
                     'Termine vergeben wir telefonisch. Sprechen Sie auf den Anrufbeantworter, wir rufen schnellstmöglich zurück.'],
              tl=[('2002', 'gegründet'), ('Clemens-August-Str. 3', 'Dinklage')]),
    par='5/4', people=[(J('seebeck', '000'), 'Thomas Seebeck', 'Physiotherapeut'), (J('seebeck', '001'), 'Kerstin Ortmann-Seebeck', 'Physiotherapeutin')],
    gal=[(J('seebeck', '005'), '50% 50%'), (J('seebeck', '003'), '50% 50%'), (J('seebeck', '004'), '50% 50%')],
    hours=[('Mo, Di, Do', '8–18 Uhr'), ('Mi, Fr', '8–12 Uhr')], cats=['ruecken', 'rezept', 'lymph', 'becken', 'kind', 'selbst'], bot='Theo', notfall=NF, mq_end='Physiotherapie in Dinklage',
    rec={'ruecken': ['Manuelle Therapie', 'Wir schauen uns Ihren Rücken genau an.'], 'rezept': ['Krankengymnastik', 'Sprechen Sie auf den Anrufbeantworter, wir rufen zurück.'], 'lymph': ['Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'],
         'becken': ['Beckenbodentraining', 'Beckenbodentraining gehört zu unserem Angebot.'], 'kind': ['Kinder', 'Auch Kinder behandeln wir gern.'], 'selbst': ['Osteopathische Selbstbehandlung', 'In unseren Kursen lernen Sie, sich selbst zu helfen.']},
    pops=[('g1.jpg', 'Termine', 'Rufen Sie an, wir melden uns schnellstmöglich zurück.')]))

# 6 ─ ATHLETICS, Wallenhorst
mk('athletics', dict(google=(4.9, 120), slug='athletics-therapiezentrum-wallenhorst', firma='ATHLETICS Functional Training & Physiotherapie', kurz='ATHLETICS', ort='Wallenhorst', strasse='Hansastraße 1a', plz='49134',
    tel='05407 8841002', tel_i='+4954078841002', mail='info@athletics-therapiezentrum.de', web='athletics-therapiezentrum.de', p='#6cc51f', pi='#14170f', em='#3f8a0c', dk='#2f3133', s2='#f1f4ee', fam=ROB, fonts='r10liekam',
    logo_txt='ATHLETICS<small>Functional Training & Physiotherapie</small>', hero='r', card='16/9', himgs=[J('athletics', '007'), J('athletics', '023')], cols='44fr 56fr',
    ey='Therapiezentrum in Wallenhorst', h1='Therapie und Training. <em>Unter einem Dach.</em>',
    sub='DAS orthopädisch spezialisierte Therapiezentrum: Physiotherapie, Lasertherapie und funktionelles Training auf großer Fläche. Bei akuten Schmerzen sind wir 24 Stunden am Tag erreichbar.',
    ubar=[('4,9 Sterne', '120 Google-Bewertungen'), ('24/7', 'schnelle Hilfe bei Schmerz'), ('Bis 21 Uhr', 'Mo bis Do')],
    sv_h2='Von der Therapie <em>zurück ins Training.</em>', sv_lead='Wir verbinden klassische Physiotherapie mit gezieltem Training, damit Sie stabil und belastbar werden.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie nach ärztlicher Verordnung.'), ('Manuelle Therapie', 'Gezielte Handgriffe für Gelenke und Wirbelsäule.'),
          ('Lasertherapie', 'Ergänzende Behandlung mit Laser in unserem Therapiezentrum.'), ('Gerätegestützte KG', 'Training an modernen Geräten unter Anleitung.'),
          ('Functional Training', 'Funktionelles Training für Alltag und Sport.'), ('Reha Basic & Pro', 'Trainingsprogramme für Prävention und Reha.')],
    top=dict(nav='24/7-Hilfe', tag='Schnelle Hilfe, 24/7', h2='Akuter Schmerz? <em>Wir sind erreichbar.</em>', img=J('athletics', '011'),
             txt='Bei akuten Schmerzen braucht man schnelle Hilfe. Die bekommen Sie bei uns 24 Stunden am Tag, 7 Tage die Woche. Auch außerhalb der Öffnungszeiten erreichen Sie uns über eine extra Telefonnummer.',
             pts=['Auch außerhalb der Öffnungszeiten', 'Extra Notfall-Telefonnummer', 'Oft noch am selben Tag'], btn='Jetzt Termin anfragen', pop='Akuter Schmerz? Wir sind 24/7 erreichbar.'),
    zwei=dict(ey='Training', h2='Große Trainingsfläche <em>mit Betreuung.</em>', img=J('athletics', '018'),
              txt='Auf unserer Trainingsfläche trainieren Sie an modernen Geräten, mit Functional-Training-Bereich und Betreuung durch unser Team.',
              pts=['Fitness und Functional Training', 'Prävention und Reha', 'Persönliche Betreuung'], btn='Probetraining anfragen'),
    team=dict(ey='Über uns', h2='Inhaber <em>Horst Angrick.</em>', img=J('athletics', '020'), cap='Das Therapiezentrum ATHLETICS in Wallenhorst',
              paras=['Horst Angrick und sein Team behandeln orthopädische Beschwerden ganzheitlich: erst die genaue Analyse, dann Therapie und gezieltes Training.',
                     'In den Bewertungen loben Patienten vor allem die schnelle Diagnose, die verständlichen Erklärungen und die kurzfristigen Termine.'],
              tl=[('120', 'Google-Bewertungen'), ('Hansastr. 1a', 'Wallenhorst')]),
    gal=[(J('athletics', '017'), '50% 50%'), (J('athletics', '004'), '50% 50%'), (J('athletics', '024'), '50% 50%')],
    stimmen=['Morgens verhoben, abends noch als Notfall dran und am nächsten Tag war fast alles weg. Horst erklärt hervorragend.', 'Meine Schulterprobleme wurden gründlich analysiert, der Plan war genau auf mich abgestimmt.', 'Nach meinem Kreuzbandriss hat mich das Training optimal auf die Rückkehr zum Fußball vorbereitet.', 'Schon nach der ersten Behandlung spürte ich Besserung. Tolle Atmosphäre, sehr herzlicher Empfang.'],
    hours=[('Mo bis Do', '7.30–21 Uhr'), ('Fr', '7.30–19 Uhr'), ('Sa', '8–14 Uhr')], cats=['akut', 'ruecken', 'op', 'sport', 'rezept', 'training'], bot='Max', notfall='Akuter Schmerz? Rufen Sie an, wir sind auch außerhalb der Öffnungszeiten erreichbar.', mq_end='Therapie und Training in Wallenhorst',
    rec={'akut': ['Krankengymnastik', 'Bei akuten Schmerzen sind wir 24/7 erreichbar.'], 'ruecken': ['Manuelle Therapie', 'Wir analysieren genau und behandeln gezielt.'], 'op': ['Gerätegestützte KG', 'Nach der OP bauen wir mit Ihnen wieder Kraft auf.'],
         'sport': ['Functional Training', 'Wir bereiten Sie auf die Rückkehr in Ihren Sport vor.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, wir haben lange geöffnet.'], 'training': ['Reha Basic & Pro', 'Training auf großer Fläche mit Betreuung.']},
    pops=[('el.jpg', 'Training', 'Große Trainingsfläche mit Betreuung.'), ('g3.jpg', 'Besuchen Sie uns', 'Hansastraße 1a in Wallenhorst.')]))

# 7 ─ PhysioPlus, Lohne
mk('physioplus', dict(google=(4.8, 12), slug='physioplus-lohne', firma='PhysioPlus – Physiotherapie & Osteopathie', kurz='PhysioPlus', ort='Lohne (Oldenburg)', strasse='Brinkstraße 1–3', plz='49393',
    tel='04442 8083528', tel_i='+4944428083528', mail='info@physioplus-lohne.de', web='physioplus-lohne.de', p='#8cb30c', pi='#14170f', em='#5e7d00', dk='#2e3236', s2='#f3f7ea', fam=MAN, fonts='mykonos',
    logo=(J('physioplus', '000'), 420, 'alphacrop'), lh=56, hero='r', card='3/2', himgs=[J('physioplus', '020'), J('physioplus', '021')], cols='46fr 54fr',
    ey='Physiotherapie & Osteopathie in Lohne', h1='Zeit für Sie. <em>Und für Ihren Körper.</em>',
    sub='Seit 2015 begrüßen Oliver Slak und sein Team die Patienten in großzügigen, modernen Praxisräumen mitten in Lohne. Barrierefrei per Fahrstuhl, Parkplätze direkt am Haus.',
    ubar=[('Seit 2015', 'in Lohnes Stadtmitte'), ('Fahrstuhl', 'barrierefrei'), ('Bis 20 Uhr', 'Mo und Di')],
    sv_h2='Physiotherapie, <em>Osteopathie und mehr.</em>', sv_lead='Wir nehmen uns Zeit für das Erstgespräch, erklären verständlich und geben Ihnen Übungen für zu Hause mit.',
    svcs=[('Osteopathie', 'Manuelle Befund- und Behandlungsform, die Bewegungseinschränkungen im Körper aufspüren und lösen soll.'), ('Physiotherapie', 'Krankengymnastik, Massage, Lymphdrainage und Wärmeanwendungen.'),
          ('Rehabilitation', 'Gerätegestützte Krankengymnastik in unserem Trainingsbereich.'), ('Fasziendistorsionsmodell', 'Als EFDMA-Mitglied arbeiten wir nach dem Fasziendistorsionsmodell.'),
          ('Prävention', 'Training und Tipps, damit Beschwerden gar nicht erst entstehen.'), ('Neurologische Behandlung', 'Therapie bei neurologischen Erkrankungen.')],
    top=dict(nav='Osteopathie', tag='Osteopathie bei PhysioPlus', h2='Die Ursache finden, <em>nicht nur das Symptom.</em>', img=J('physioplus', '012'),
             txt='Oliver Slak ist Physiotherapeut und Osteopath. Er nimmt sich viel Zeit für das Erstgespräch, erklärt die Behandlungsansätze und zeigt Ihnen Übungen für zu Hause.',
             pts=['Ausführliches Erstgespräch', 'Verständliche Erklärungen', 'Übungen für den Alltag'], btn='Osteopathie-Termin anfragen', pop='Osteopathie mit viel Zeit für das Erstgespräch.'),
    team=dict(ey='Über uns', h2='Gegründet <em>von Oliver Slak.</em>', img=J('physioplus', '018'), mw=360, cap='Oliver Slak, Physiotherapeut und Osteopath',
              paras=['Am 1. Juli 2015 hat Oliver Slak PhysioPlus in Lohnes Stadtmitte gegründet. Seitdem begrüßen er und sein Team die Patienten in Räumen mit Wohlfühlatmosphäre.',
                     'Sie erreichen uns im ersten Obergeschoss bequem per Fahrstuhl. Kostenlose Parkplätze gibt es direkt am Haus.'],
              tl=[('2015', 'gegründet'), ('Brinkstr. 1–3', 'Lohne')]),
    gal=[(J('physioplus', '022'), '50% 50%'), (J('physioplus', '025'), '50% 50%'), (J('physioplus', '027'), '50% 50%')],
    job=dict(img=J('physioplus', '026'), h2='Werden Sie <em>Teil des Teams.</em>', txt='PhysioPlus sucht Verstärkung. Melden Sie sich, wenn Sie in einer modernen Praxis mit Osteopathie-Schwerpunkt arbeiten möchten.',
             pts=['Moderne, große Praxisräume', 'Osteopathie im Haus', 'Mitten in Lohne']),
    stimmen=['Beim ersten Termin habe ich mich sehr wohlgefühlt. Alles wurde klar erklärt, dazu Übungen für zu Hause.', 'Viel Zeit für das Erstgespräch, zuverlässige Terminvergabe und eine moderne, großzügige Praxis.', 'Sehr freundliches, kompetentes Team und eine extrem positive Atmosphäre.', 'Nach Jahren mit Beschwerden fühle ich mich hier unglaublich gut aufgehoben.'],
    hours=[('Mo, Di', '8–20 Uhr'), ('Mi', '8–19 Uhr'), ('Do', '8–18 Uhr'), ('Fr', '8–14 Uhr')], cats=['ruecken', 'osteo', 'op', 'rezept', 'sport', 'job'], bot='Ole', notfall=NF, mq_end='Physiotherapie in Lohne',
    rec={'ruecken': ['Physiotherapie', 'Wir nehmen uns Zeit und erklären alles verständlich.'], 'osteo': ['Osteopathie', 'Osteopathie bei Oliver Slak, mit ausführlichem Erstgespräch.'], 'op': ['Rehabilitation', 'Nach der OP trainieren wir gezielt an Geräten.'],
         'rezept': ['Physiotherapie', 'Rufen Sie an, wir haben bis 20 Uhr geöffnet.'], 'sport': ['Fasziendistorsionsmodell', 'Auch Sportler sind bei uns gut aufgehoben.'], 'job': ['Physiotherapie', 'Wir suchen Verstärkung. Melden Sie sich gern!']},
    pops=[('g3.jpg', 'Barrierefrei', 'Per Fahrstuhl, Parkplätze direkt am Haus.'), ('jb.jpg', 'Stellenangebot', 'PhysioPlus sucht Verstärkung.')]))

# 8 ─ Ulrich Henke, Bramsche-Engter
mk('henke', dict(slug='physiotherapie-henke-engter', firma='Praxis für Physiotherapie Ulrich Henke', kurz='Praxis Henke', ort='Bramsche-Engter', strasse='Venner Straße 14', plz='49565',
    tel='05468 9915', tel_i='+4954689915', web='physiotherapie-engter.de', p='#2e559e', dk='#1c2f57', s2='#f1f4fa', em='#2e559e', fam=TIT, fonts='r15han',
    logo=(J('henke', '000'), 300), lh=62, prmw=400, elmw=400, hero='r', card='4/3', himgs=[J('henke', '012'), J('henke', '012')], cols='44fr 56fr',
    ey='Physiotherapie in Engter', h1='Schnell untersucht. <em>Gut behandelt.</em>',
    sub='Ulrich Henke ist als Heilpraktiker für Physiotherapie zugelassen. So können Sie bei uns auch ohne ärztliche Verordnung untersucht, beraten und behandelt werden.',
    ubar=[('Heilpraktiker', 'ohne Rezept möglich'), ('T-RENA', 'Nachsorge der DRV'), ('Bis 20 Uhr', 'Di und Do')],
    sv_h2='Mehr als <em>Krankengymnastik.</em>', sv_lead='Zusatzqualifikationen in Manueller Therapie, Bobath, gerätegestützter KG und Lymphdrainage.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie nach Verordnung.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Bobath für Erwachsene', 'Therapie bei neurologischen Erkrankungen.'), ('Gerätegestützte KG', 'Training an Geräten unter Anleitung.'),
          ('Manuelle Lymphdrainage', 'Spezielle Handgriffe mit rhythmischen, kreisenden und pumpenden Bewegungen.'), ('Heilpraktikerleistungen', 'Zum Beispiel Osteopathie, Akupunktur und Atemtherapie.')],
    top=dict(nav='T-RENA', tag='T-RENA Nachsorge', h2='Nach der Reha <em>dranbleiben.</em>', img=J('henke', '007'),
             txt='Wir betreuen T-RENA, die Trainingstherapeutische Rehabilitationsnachsorge der Deutschen Rentenversicherung. So festigen Sie nach der Reha, was Sie erreicht haben.',
             pts=['Nachsorge der Deutschen Rentenversicherung', 'Training an Geräten', 'In kleinen Gruppen'], btn='T-RENA anfragen', pop='T-RENA: Nachsorge nach der Reha.'),
    zwei=dict(ey='Heilpraktiker', h2='Auch <em>ohne Rezept.</em>', img=J('henke', '006'),
              txt='Seit 2014 ist Ulrich Henke als sektoraler Heilpraktiker für Physiotherapie zugelassen. Privatversicherte, Beihilfeberechtigte und Selbstzahler können so direkt zu uns kommen.',
              pts=['Ohne ärztliche Verordnung', 'Für Privatversicherte und Selbstzahler', 'Schnell untersucht und beraten'], btn='Termin anfragen'),
    team=dict(ey='Über uns', h2='Ulrich Henke <em>und Maren Ruhnau.</em>', img=J('henke', '001'), cap='Aus dem Team der Praxis Henke',
              paras=['In der Praxis arbeiten Ulrich Henke und Maren Ruhnau mit ihrem Team. Wir betreuen Versicherte in der T-RENA-Nachsorge der Deutschen Rentenversicherung.',
                     'Patienten schätzen vor allem die flexiblen Termine, auch bei Schichtarbeit.'],
              tl=[('Seit 2014', 'Heilpraktiker'), ('Venner Str. 14', 'Engter')]),
    gal=[(J('henke', '005'), '50% 50%'), (J('henke', '008'), '50% 30%'), (J('henke', '002'), '50% 50%')],
    stimmen=['Herr Henke hilft mir immer wieder bei meinen Schulterproblemen.', 'Hier wurde mir immer geholfen. Trotz Schichtarbeit gab es immer einen Termin.', 'Hervorragende Behandlung, flexible Termine und sehr freundliches Personal.'],
    hours=[('Mo', '8–19 Uhr'), ('Di', '9–20 Uhr'), ('Mi', '8–13 Uhr'), ('Do', '8–20 Uhr'), ('Fr', '8–18 Uhr')], cats=['ruecken', 'rezept', 'selbst', 'neuro', 'lymph', 'training'], bot='Ulla', notfall=NF, mq_end='Physiotherapie in Engter',
    rec={'ruecken': ['Manuelle Therapie', 'Wir schauen uns Ihren Rücken genau an.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, auch abends gibt es Termine.'], 'selbst': ['Heilpraktikerleistungen', 'Als Heilpraktiker behandeln wir auch ohne Rezept.'],
         'neuro': ['Bobath für Erwachsene', 'Bei neurologischen Erkrankungen arbeiten wir nach Bobath.'], 'lymph': ['Manuelle Lymphdrainage', 'Lymphdrainage gibt es mit Verordnung.'], 'training': ['Gerätegestützte KG', 'Training an Geräten, auch als T-RENA-Nachsorge.']},
    pops=[('el.jpg', 'Ohne Rezept', 'Als Heilpraktiker behandeln wir auch ohne Verordnung.')]))

# 9 ─ Redzich-Frye, Belm
mk('redzichfrye', dict(slug='physiotherapie-redzich-frye-belm', firma='Physiotherapie Redzich-Frye', kurz='Physiotherapie Redzich-Frye', ort='Belm', strasse='Lindenstraße 56a', plz='49191',
    tel='05406 7463', tel_i='+4954067463', mail='redzich-frye@t-online.de', web='physiotherapie-redzich-frye.com', p='#1468a8', dk='#0f2f55', s2='#eef4f9', fam=LATO, fonts='r10vagts',
    logo=(J('redzichfrye', '000'), 420, 'trim'), lh=58, prmw=500, hero='l', card='3/4', himgs=[J('redzichfrye', '016'), J('redzichfrye', '016')], hpos={'h1.jpg': '50% 40%'}, cols='52fr 48fr',
    ey='Physiotherapie in Belm · seit 1989', h1='Mehr als <em>Krankengymnastik.</em>',
    sub='Jede Behandlung wird individuell auf Sie abgestimmt. Unsere Therapeuten sind über den Standard hinaus qualifiziert. Barrierefrei, klimatisiert, Bushaltestelle direkt nebenan.',
    ubar=[('Seit 1989', 'in Belm'), ('Klimatisiert', 'und barrierefrei'), ('Bus', 'Haltestelle in der Nähe')],
    sv_h2='Fachgerecht <em>und individuell.</em>', sv_lead='Unsere Therapeuten bilden sich laufend fort, damit Sie die passende Behandlung bekommen.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie nach ärztlicher Verordnung.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Manuelle Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'), ('Bobath', 'Therapie bei neurologischen Erkrankungen.'),
          ('CMD-Behandlung', 'Behandlung bei Kiefergelenksbeschwerden.'), ('Massage, Fango, Schlingentisch', 'Ergänzende Anwendungen für Ihre Behandlung.')],
    top=dict(nav='Hausbesuche', tag='Hausbesuche', h2='Sie können nicht kommen? <em>Wir kommen zu Ihnen.</em>', img=J('redzichfrye', '019'),
             txt='Wenn Sie die Praxis nicht aufsuchen können, behandeln wir Sie auch zu Hause. Voraussetzung ist eine Verordnung für Hausbesuche.',
             pts=['Mit Verordnung für Hausbesuch', 'In Belm und Umgebung', 'Gleiche Qualität wie in der Praxis'], btn='Hausbesuch anfragen', pop='Wir behandeln Sie auch zu Hause.'),
    team=dict(ey='Das Team', h2='Ein Team, <em>über den Standard hinaus.</em>', img=J('redzichfrye', '001'), cap='Das Team der Physiotherapie Redzich-Frye',
              paras=['Seit 1989 ist unsere Praxis in Belm. Kerstin Redzich-Frye führt die Praxis mit einem eingespielten Team aus Therapeutinnen und Therapeuten.',
                     'Unsere Räume sind barrierefrei und klimatisiert. Eine Bushaltestelle liegt in unmittelbarer Nähe.'],
              tl=[('1989', 'gegründet'), ('Lindenstr. 56a', 'Belm')]),
    gal=[(J('redzichfrye', '019'), '50% 50%'), (J('redzichfrye', '022'), '50% 50%'), (J('redzichfrye', '021'), '50% 50%')],
    stimmen=['Eine Praxis, in der man sich gut aufgehoben fühlt. Kompetent und freundlich behandelt.', 'Angenehme Atmosphäre, kompetente Therapeuten. Ich habe sehr nützliche Tipps bekommen.', 'Ein sehr kompetentes und freundliches Team!'],
    hours=[('Mo, Di, Do', '8.30–18 Uhr'), ('Mi, Fr', '8.30–11.30 Uhr')], cats=['ruecken', 'rezept', 'lymph', 'neuro', 'cmd', 'haus'], bot='Kira', notfall=NF, mq_end='Physiotherapie in Belm',
    rec={'ruecken': ['Manuelle Therapie', 'Wir stimmen die Behandlung genau auf Sie ab.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, wir finden einen Termin.'], 'lymph': ['Manuelle Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'],
         'neuro': ['Bobath', 'Bei neurologischen Erkrankungen arbeiten wir nach Bobath.'], 'cmd': ['CMD-Behandlung', 'Auch Kieferbeschwerden behandeln wir.'], 'haus': ['Krankengymnastik', 'Mit Verordnung kommen wir zu Ihnen nach Hause.']},
    pops=[('g1.jpg', 'Barrierefrei', 'Klimatisierte Räume, Bus direkt nebenan.')]))

# 10 ─ Körperhelden, Belm
mk('koerperhelden', dict(google=(5.0, 12), du=True, slug='koerperhelden-belm', firma='Körperhelden Physiotherapie', kurz='Körperhelden', ort='Belm', strasse='Jeggener Straße 40', plz='49191',
    tel='01575 2389960', tel_i='+4915752389960', mail='christina@koerperhelden.de', web='koerperhelden.de', p='#1f8a8c', dk='#173f45', s2='#eef6f6', em='#e8862a', fam=NUN, fonts='r10borggreve',
    logo=(J('koerperhelden', '000'), 520, 'trim'), lh=46, hero='r', himgs=[J('koerperhelden', '002'), J('koerperhelden', '002')], hpos={'h1.jpg': '50% 20%'}, cols='48fr 52fr',
    ey='Kinderphysiotherapie auf dem Wellingerhof', h1='Jedes Kind <em>ist ein Held.</em>',
    sub='Bei uns stehen Kinder und Jugendliche mit ihren eigenen Stärken im Mittelpunkt. Mit Herz, Fachkompetenz und Freude an Bewegung begleiten wir dein Kind auf seinem Weg.',
    ubar=[('Intensivwochen', 'unser Herzstück'), ('0 bis 18', 'vom Säugling bis Teenager'), ('Wellingerhof', 'Belm')],
    sv_h2='Bewegung, <em>die Spaß macht.</em>', sv_lead='Ob Entwicklungsverzögerung, neurologische oder orthopädische Erkrankung: Wir schauen vor allem auf das, was dein Kind kann.',
    svcs=[('Intensivwoche', 'Eine kompakte Therapiewoche mit konkretem Ziel. Neue Bewegungsmuster werden eingeübt und automatisiert.'), ('Physiotherapie', '1–2x wöchentlich, mit denselben Bausteinen wie in der Intensivwoche.'),
          ('Neurologie', 'Zum Beispiel bei Cerebralparese oder anderen neurologischen Erkrankungen.'), ('Orthopädie', 'Bei orthopädischen Erkrankungen und motorischen Auffälligkeiten.'),
          ('Hilfsmittel', 'Wir zeigen Möglichkeiten für Therapie und Alltag zu Hause.'), ('Fortbildung', 'Fachkollegialer Austausch für Therapeutinnen und Therapeuten.')],
    top=dict(nav='Intensivwoche', tag='Die Intensivwoche', h2='Eine Woche. <em>Ein klares Ziel.</em>', img=J('koerperhelden', '019'),
             txt='Unser Herzstück: eine kompakte Therapiewoche mit konkretem Therapieziel. Neue Bewegungsmuster werden spielerisch eingeübt, wiederholt und automatisiert. Familien von weiter weg können direkt auf dem Hof übernachten.',
             pts=['Kompakt und zielgerichtet', 'Spielerisch und motivierend', 'Viele Ideen für zu Hause'], btn='Intensivwoche anfragen', pop='Intensivwoche: eine Woche, ein klares Ziel.'),
    team=dict(ey='Über uns', h2='Christina Wörmann <em>und Inga Bolz.</em>', img=J('koerperhelden', '002'), mw=360, cap='Die Praxisinhaberinnen der Körperhelden',
              paras=['Die beiden Physiotherapeutinnen (B.Sc.) führen die Körperhelden auf dem Wellingerhof in Belm. Mit ihrem Team begleiten sie Kinder und Jugendliche vom Säuglingsalter bis zum Teenager.',
                     'Zum Team gehören Hanna Tölle, Jasmin Dieterle, Manuel Brauers, Corinna Kötter und Sophie Sambale.'],
              tl=[('7', 'Menschen im Team'), ('Wellingerhof', 'Belm')]),
    gal=[(J('koerperhelden', '003'), '50% 50%'), (J('koerperhelden', '004'), '50% 50%'), (J('koerperhelden', '007'), '50% 50%')],
    stimmen=['Unser Kind hat in der Intensivwoche Fortschritte gemacht, die uns begeistert haben. Unglaublich geduldig und einfühlsam.', 'Wir waren schon zum zweiten Mal da und haben auch in der Praxis übernachtet. Die Kinder werden spielerisch gefördert und gefordert.', 'Als Eltern fühlten wir uns komplett unterstützt. Keine Frage blieb offen.', 'Innovativ, umfassend und extrem engagiert. Das Kind wird motiviert, ohne überfordert zu werden.'],
    hours=[('Mo bis Fr', '8–18 Uhr')], cats=['kind', 'neuro', 'rezept', 'selbst'], bot='Hanni', notfall=NF_DU, mq_end='Kinderphysiotherapie in Belm', bot_tag='Dein Praxis-Lotse',
    rec={'kind': ['Physiotherapie', 'Wir begleiten dein Kind vom Säugling bis zum Teenager.'], 'neuro': ['Intensivwoche', 'Gerade bei neurologischen Erkrankungen lohnt sich die Intensivwoche.'], 'rezept': ['Physiotherapie', 'Ruf an, wir finden einen Termin.'], 'selbst': ['Intensivwoche', 'Frag uns gern nach den Möglichkeiten.']},
    pops=[('g1.jpg', 'Wellingerhof', 'Therapie auf einem schönen Hof in Belm.')]))

# 11 ─ Andreas Pflug, Osnabrück
mk('pflug', dict(google=(5.0, 9), slug='physiotherapie-pflug-osnabrueck', firma='Praxis für Physiotherapie Andreas Pflug', kurz='Praxis Pflug', ort='Osnabrück', strasse='August-Hölscher-Straße 45', plz='49080',
    tel='0541 47557', tel_i='+4954147557', mail='info@physio-in-os.de', web='physio-in-os.de', p='#c9c916', pi='#1b1d22', em='#7a7a00', dk='#2b3a42', s2='#f3f4ee', fam=ARCH, fonts='r10siefker',
    logo=(J('pflug', '008'), 520, 'trim'), lh=62, hero='r', himgs=[J('pflug', '000'), J('pflug', '002')], cols='46fr 54fr',
    ey='Physiotherapie in Osnabrück', h1='Zeit für Sie. <em>Auch vor und nach der Arbeit.</em>',
    sub='Manuelle Therapie, Lymphdrainage und Cranio-Sacrale-Therapie. Wir haben ab 7 Uhr und bis in den Abend geöffnet, damit Ihr Termin zu Ihrem Alltag passt.',
    ubar=[('Ab 7 Uhr', 'Mo bis Fr'), ('Bis 19.30 Uhr', 'Mo, Di, Do'), ('7 Therapeuten', 'kleines, erfahrenes Team')],
    sv_h2='Kleine Praxis, <em>hohe Qualität.</em>', sv_lead='Unsere Therapeuten nehmen sich Zeit, um Sie und Ihre Beschwerden zu verstehen.',
    svcs=[('Manuelle Therapie', 'Gezielte Handgriffe für Gelenke und Wirbelsäule.'), ('Manuelle Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'),
          ('Cranio-Sacrale-Therapie', 'Sanfte Behandlung an Schädel, Wirbelsäule und Kreuzbein.'), ('Krankengymnastik', 'Klassische Physiotherapie nach Verordnung, auch nach Bobath.'),
          ('Kiefergelenk (CMD)', 'Behandlung bei Kiefergelenksbeschwerden.'), ('Hausbesuche', 'Mit Verordnung behandeln wir Sie auch zu Hause.')],
    top=dict(nav='Cranio', tag='Cranio-Sacrale-Therapie', h2='Sanft behandelt, <em>in Ruhe.</em>', img=J('pflug', '010'),
             txt='Die Cranio-Sacrale-Therapie ist eine besonders sanfte Behandlungsform. Bei uns nehmen sich die Therapeuten dafür viel Zeit.',
             pts=['Sanfte Technik', 'Ruhige Atmosphäre', 'Auch für Selbstzahler'], btn='Termin anfragen', pop='Cranio-Sacrale-Therapie in ruhiger Atmosphäre.'),
    team=dict(ey='Das Team', h2='Andreas Pflug <em>und sein Team.</em>', img=J('pflug', '002'), cap='Der Empfang der Praxis Pflug',
              paras=['Therapeuten: Andreas Pflug, Carolin Koddenberg, Hannah Hülsmann, Theresa Kaase, Ute Nussbaum, Jan Pieper und Michael Steglich.',
                     'An der Anmeldung begrüßen Sie Silvia Haunert und Monika Weller.'],
              tl=[('9', 'Menschen im Team'), ('August-Hölscher-Str. 45', 'Osnabrück')]),
    gal=[(J('pflug', '003'), '50% 50%'), (J('pflug', '004'), '50% 50%'), (J('pflug', '001'), '50% 50%')],
    job=dict(img=J('pflug', '000'), h2='Physiotherapeut:in <em>ab sofort gesucht.</em>', txt='Wir suchen zu sofort eine Physiotherapeutin oder einen Physiotherapeuten (m/w/d) in Voll- oder Teilzeit.',
             pts=['Voll- oder Teilzeit', 'Kleines, eingespieltes Team', 'Flexible Zeiten von 7 bis 19.30 Uhr']),
    stimmen=['Die Öffnungszeiten sind ein Traum für Berufstätige. Die Therapeuten nehmen sich Zeit, einen zu verstehen.', 'Kleine Praxis mit hochqualifizierten Therapeuten. Sehr freundlich und engagiert.', 'Ausgezeichnete Cranio-Sacral-Behandlung. Danke.', 'Sehr, sehr gut. Kann ich nur empfehlen.'],
    hours=[('Mo, Di, Do', '7–19.30 Uhr'), ('Mi', '7–19 Uhr'), ('Fr', '7–18 Uhr')], cats=['ruecken', 'rezept', 'lymph', 'cmd', 'haus', 'job'], bot='Paul', notfall=NF, mq_end='Physiotherapie in Osnabrück',
    rec={'ruecken': ['Manuelle Therapie', 'Wir nehmen uns Zeit, Ihre Beschwerden zu verstehen.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, Termine gibt es ab 7 Uhr.'], 'lymph': ['Manuelle Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'],
         'cmd': ['Kiefergelenk (CMD)', 'Auch Kieferbeschwerden behandeln wir.'], 'haus': ['Hausbesuche', 'Mit Verordnung kommen wir zu Ihnen.'], 'job': ['Krankengymnastik', 'Wir suchen ab sofort Verstärkung. Melden Sie sich!']},
    pops=[('jb.jpg', 'Wir suchen Verstärkung', 'Physiotherapeut:in in Voll- oder Teilzeit.')]))

# 12 ─ PhysioPortal an der Soeste, Cloppenburg
mk('physioportal', dict(google=(4.7, 12), slug='physioportal-cloppenburg', firma='Nickels PhysioPortal an der Soeste', kurz='PhysioPortal', ort='Cloppenburg', strasse='Mühlenstraße 27', plz='49661',
    tel='04471 9582233', tel_i='+4944719582233', mail='info@physio-portal.de', web='physio-portal.de', p='#8c8276', dk='#2f2c29', s2='#f5f3f0', em='#6f665b', fam=('"Marcellus",Georgia,serif', '"Manrope",system-ui,sans-serif'), fonts='mykonos',
    logo=(J('physioportal', '002'), 420, 'trim'), lh=64, prmw=440, hero='team', himgs=[J('physioportal', '010'), J('physioportal', '010')], hcap='Das Team im PhysioPortal an der Soeste',
    ey='Physiotherapie in Cloppenburg', h1='Glücklich, wer die Ursachen <em>der Dinge erkennt.</em>',
    sub='Nach diesem Leitsatz von Vergil arbeiten wir: Wir suchen die Ursache Ihrer Beschwerden. Das PhysioPortal an der Soeste verbindet Physiotherapie, Rehabilitation, Sport und Medical Wellness.',
    ubar=[('Sa geöffnet', '8–13 Uhr'), ('NGYM', 'Training im Haus'), ('An der Soeste', 'mitten in Cloppenburg')],
    sv_h2='Therapie in <em>schönen Räumen.</em>', sv_lead='Helle Behandlungsräume, ein eingespieltes Team und ein eigener Trainingsbereich.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie nach ärztlicher Verordnung.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'), ('Rehabilitation', 'Gerätegestützte Krankengymnastik im eigenen NGYM.'),
          ('Osteopathie', 'Ganzheitliche Befundung und Behandlung mit den Händen.'), ('Sportphysiotherapie', 'Betreuung für Sportlerinnen und Sportler.')],
    top=dict(nav='Rehabilitation', tag='Rehabilitation und NGYM', h2='Erst Therapie, <em>dann Training.</em>', img=J('physioportal', '006'),
             txt='Im NGYM, unserem Trainingsbereich im PhysioPortal, bauen Sie nach der Therapie gezielt Kraft und Beweglichkeit auf. Begleitet von unseren Therapeuten.',
             pts=['Gerätegestützte Krankengymnastik', 'Eigener Trainingsbereich', 'Betreuung durch Therapeuten'], btn='Termin anfragen', pop='Therapie und Training unter einem Dach.'),
    team=dict(ey='Das Team', h2='Ihr Team <em>vom PhysioPortal.</em>', img=J('physioportal', '004'), cap='Empfang im PhysioPortal an der Soeste',
              paras=['Das PhysioPortal an der Soeste steht für Physiotherapie, Sports und Medical Wellness. Unser Team begrüßt Sie in hellen, hochwertig eingerichteten Räumen.',
                     'Patienten loben in ihren Bewertungen die schöne Atmosphäre und das freundliche Team.'],
              tl=[('Mo bis Sa', 'geöffnet'), ('Mühlenstr. 27', 'Cloppenburg')]),
    gal=[(J('physioportal', '023'), '50% 50%'), (J('physioportal', '027'), '50% 50%'), (J('physioportal', '026'), '50% 50%')],
    job=dict(img=J('physioportal', '004'), h2='In 60 Sekunden <em>beworben.</em>', txt='Zur Verstärkung unseres Teams suchen wir zum nächstmöglichen Zeitpunkt unter anderem Physiotherapeuten (m/w/d).',
             pts=['Bewerbung in 60 Sekunden', 'Hochwertige Praxisräume', 'Therapie und Training im Haus']),
    stimmen=['Freundliches Personal, hilfsbereit und flexibel bei Terminen. Kann ich sehr empfehlen!', 'Ich bin vom Team und seiner Leistung sehr beeindruckt. 100 % Empfehlung.', 'Freundlicher Empfang, nettes Team, professionelle Behandlungen.', 'Schöne Atmosphäre, sehr freundliches Personal. Hoher Wohlfühlfaktor.'],
    hours=[('Mo bis Fr', '8–19 Uhr'), ('Sa', '8–13 Uhr')], cats=['ruecken', 'op', 'rezept', 'sport', 'osteo', 'job'], bot='Nico', notfall=NF, mq_end='Physiotherapie in Cloppenburg',
    rec={'ruecken': ['Manuelle Therapie', 'Wir suchen die Ursache Ihrer Beschwerden.'], 'op': ['Rehabilitation', 'Nach der OP trainieren Sie bei uns im NGYM.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, wir haben auch samstags geöffnet.'],
         'sport': ['Sportphysiotherapie', 'Sportler betreuen wir gezielt.'], 'osteo': ['Osteopathie', 'Osteopathie gehört zu unserem Angebot.'], 'job': ['Krankengymnastik', 'Bewerben Sie sich in nur 60 Sekunden!']},
    pops=[('g1.jpg', 'Samstags geöffnet', 'Termine auch am Samstag von 8 bis 13 Uhr.'), ('jb.jpg', 'Wir suchen Sie', 'Bewerbung in nur 60 Sekunden.')]))

# 13 ─ Therapiezentrum Lienert, Diepholz
mk('lienert', dict(google=(4.8, 140), slug='therapiezentrum-lienert-diepholz', firma='Therapiezentrum Silke und Ralf Lienert', kurz='Therapiezentrum Lienert', ort='Diepholz', strasse='Wankelstraße 2', plz='49356',
    tel='05441 6882', tel_i='+4954416882', mail='ralf.silke.lienert@t-online.de', web='therapiezentrum-lienert.info', p='#1b365d', dk='#12243f', s2='#f1f4f8', em='#1b6aa8', fam=('"DM Serif Display",Georgia,serif', '"Nunito Sans",system-ui,sans-serif'), fonts='r12albers',
    logo_txt='Therapiezentrum Lienert<small>Osteopathie · Physiotherapie</small>', hero='team', himgs=[J('lienert', '017'), J('lienert', '017')], hcap='Das Team des Therapiezentrums Lienert in Diepholz',
    ey='Osteopathie und Physiotherapie in Diepholz · seit 1997', h1='Wir betrachten den Menschen <em>als Ganzes.</em>',
    sub='Als Osteopathie- und Physiotherapie-Zentrum legen wir großen Wert auf die ganzheitliche Betrachtung Ihrer Beschwerden. Mit über 30 Jahren Erfahrung und einem großen Team.',
    ubar=[('4,8 Sterne', '140 Google-Bewertungen'), ('Seit 1997', 'in Diepholz'), ('8–20 Uhr', 'Mo bis Fr, auch ab 7 Uhr')],
    sv_h2='Ganzheitlich <em>behandelt.</em>', sv_lead='Unser Team besteht aus hervorragend ausgebildeten und motivierten Therapeuten.',
    svcs=[('Osteopathische Behandlung', 'Ganzheitliche Befundung und Behandlung mit den Händen.'), ('Osteopathische Kinesiologie', 'Ergänzende Methode in unserem Zentrum.'),
          ('Osteopathie für Babys und Kinder', 'Mit Kinderosteopathin Silke Lienert.'), ('Krankengymnastik', 'Klassische Physiotherapie, auch auf Kassenrezept.'),
          ('Massage', 'Klassische Massagen für Muskeln und Wohlbefinden.'), ('Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.')],
    top=dict(nav='Kinder', tag='Osteopathie für Babys und Kinder', h2='Sanfte Hände <em>für die Kleinsten.</em>', img=J('lienert', '002'),
             txt='Silke Lienert ist Kinderosteopathin. Sie nimmt sich Zeit für Babys, Kinder und die Fragen der Eltern, in ruhiger und kindgerechter Atmosphäre.',
             pts=['Kinderosteopathin im Haus', 'Ruhige, kindgerechte Atmosphäre', 'Zeit für die Fragen der Eltern'], btn='Termin anfragen', pop='Osteopathie für Babys und Kinder.'),
    team=dict(ey='Über uns', h2='Silke und <em>Ralf Lienert.</em>', img=J('lienert', '000'), cap='Das Team des Therapiezentrums Lienert',
              paras=['Ralf Lienert ist Physiotherapeut, Osteopath, osteopathischer Kinesiologe und Diplom-Sportlehrer. Silke Lienert ist Kinderosteopathin.',
                     'Seit 1997 sind wir in Diepholz. Manche Patienten kommen seit über 20 Jahren zu uns.'],
              tl=[('30+', 'Jahre Erfahrung'), ('Wankelstr. 2', 'Diepholz')]),
    people=[(J('lienert', '005'), 'Silke Lienert', 'Kinderosteopathin'), (J('lienert', '006'), 'Ralf Lienert', 'Physiotherapeut, Osteopath')],
    job=dict(img=J('lienert', '023'), h2='Werde Teil <em>unseres Teams!</em>', txt='Wir suchen Physiotherapeuten (m/w/d) zum sofortigen Eintritt. Bei uns arbeitest du in einem großen, herzlichen Team mit Schwerpunkt Osteopathie.',
             pts=['Großes, herzliches Team', 'Osteopathie und Physiotherapie', 'Moderne Praxis in Diepholz']),
    stimmen=['Eine tolle Praxis mit herzlichem Team. Die Behandlungen waren sehr sanft und professionell.', 'Echte Profis! Ich komme seit über 20 Jahren, wenn ich eine Behandlung brauche.', 'Ich gehe etwa alle drei Monate hin. Alles sauber, tolles Team.', 'Besonders gefallen hat mir, dass individuell auf mich eingegangen wurde.'],
    hours=[('Mo bis Fr', '8–20 Uhr'), ('Nach Vereinbarung', 'auch ab 7 Uhr')], cats=['osteo', 'kind', 'ruecken', 'rezept', 'lymph', 'job'], bot='Lio', notfall=NF, mq_end='Osteopathie in Diepholz',
    rec={'osteo': ['Osteopathische Behandlung', 'Wir betrachten Ihre Beschwerden ganzheitlich.'], 'kind': ['Osteopathie für Babys und Kinder', 'Silke Lienert ist Kinderosteopathin.'], 'ruecken': ['Krankengymnastik', 'Wir schauen uns Ihren Rücken genau an.'],
         'rezept': ['Krankengymnastik', 'Rufen Sie an, wir haben bis 20 Uhr geöffnet.'], 'lymph': ['Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'], 'job': ['Krankengymnastik', 'Wir suchen Verstärkung. Melde dich gern!']},
    pops=[('pr.jpg', 'Für Kinder', 'Osteopathie für Babys und Kinder.'), ('jb.jpg', 'Wir suchen dich', 'Physiotherapeut (m/w/d) zum sofortigen Eintritt.')]))

# 14 ─ PhysioTeam Bissendorf
mk('bissendorf', dict(google=(4.9, 8), slug='physioteam-bissendorf', firma='PhysioTeam Bissendorf Iris Campbell', kurz='PhysioTeam Bissendorf', ort='Bissendorf', strasse='Osnabrücker Straße 5', plz='49143',
    tel='05402 691533', tel_i='+495402691533', mail='info@physioteambissendorf.de', web='physioteambissendorf.de', p='#c9d400', pi='#1b1d22', em='#6f7600', dk='#4c514b', s2='#f5f6ec', fam=FIRA, fonts='r12beckermann',
    logo=(J('bissendorf', '000'), 440, 'trim'), lh=64, hero='r', himgs=[J('bissendorf', '002'), J('bissendorf', '004')], cols='46fr 54fr',
    ey='Physiotherapie und Krankengymnastik in Bissendorf', h1='Wir sind <em>für Sie da.</em>',
    sub='Ein erfahrenes Team aus Physiotherapeuten und Podologen. Wir möchten Sie dabei unterstützen, Beschwerden zu lindern und Ihr persönliches Wohlbefinden zu stärken.',
    ubar=[('Podologie', 'im Haus'), ('Alle Kassen', 'privat und Selbstzahler'), ('Gutscheine', 'zum Verschenken')],
    sv_h2='Therapie in <em>persönlicher Atmosphäre.</em>', sv_lead='Unsere Angebote gelten für Kassenpatienten, Privatpatienten und Selbstzahler.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie, auch nach Bobath und PNF.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Manuelle Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'), ('Kiefergelenk (CMD) und Schwindel', 'Behandlung bei Kieferbeschwerden und Schwindel.'),
          ('Kinder', 'Auch kleine Patienten behandeln wir.'), ('Massage, Fango, Wellness', 'Wohltuende Anwendungen, auch als Gutschein.')],
    top=dict(nav='Podologie', tag='Podologie im Haus', h2='Gut zu Fuß. <em>Fachlich betreut.</em>', img=J('bissendorf', '011'),
             txt='In unserer Praxis arbeiten auch Podologinnen und Podologen. So bekommen Sie medizinische Fußpflege und Physiotherapie unter einem Dach.',
             pts=['Medizinische Fußpflege', 'Eigener Behandlungsraum', 'Physio und Podologie an einem Ort'], btn='Termin anfragen', pop='Podologie und Physiotherapie unter einem Dach.'),
    team=dict(ey='Über uns', h2='Iris Campbell <em>und ihr Team.</em>', img=J('bissendorf', '005'), cap='Behandlungsraum im PhysioTeam Bissendorf',
              paras=['„Mein Team und ich möchten Ihnen qualitativ hochwertige Behandlung bieten.“ So beschreibt Inhaberin Iris Campbell ihren Anspruch.',
                     'In persönlicher Atmosphäre können Sie bei uns auch vorbeugend etwas für Ihre Gesundheit tun.'],
              tl=[('Helle Räume', 'frisch und freundlich'), ('Osnabrücker Str. 5', 'Bissendorf')]),
    gal=[(J('bissendorf', '006'), '50% 50%'), (J('bissendorf', '007'), '50% 50%'), (J('bissendorf', '008'), '50% 50%')],
    job=dict(img=J('bissendorf', '004'), h2='Wir suchen <em>Verstärkung.</em>', txt='Für unser Team in Bissendorf suchen wir Physiotherapeutinnen und Physiotherapeuten. Melden Sie sich gern bei uns.',
             pts=['Helle, moderne Räume', 'Persönliche Atmosphäre', 'Physiotherapie und Podologie']),
    stimmen=['Meine Therapeutin ist hochkompetent und dazu unglaublich sympathisch. Ich kann sie von Herzen empfehlen!', 'Nach einer Sportverletzung wurde ich so gut behandelt, dass ich schnell wieder trainieren konnte. Sehr kompetentes Team!'],
    hours=[('Termine', 'nach Vereinbarung')], cats=['ruecken', 'rezept', 'lymph', 'cmd', 'kind', 'job'], bot='Ida', notfall=NF, mq_end='Physiotherapie in Bissendorf',
    rec={'ruecken': ['Manuelle Therapie', 'Wir unterstützen Sie dabei, Beschwerden zu lindern.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, wir finden einen Termin.'], 'lymph': ['Manuelle Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'],
         'cmd': ['Kiefergelenk (CMD) und Schwindel', 'Auch Kiefer und Schwindel behandeln wir.'], 'kind': ['Kinder', 'Kinder sind bei uns willkommen.'], 'job': ['Krankengymnastik', 'Wir suchen Verstärkung. Melden Sie sich!']},
    pops=[('g3.jpg', 'Gutscheine', 'Gutes verschenken: Gutscheine für das PhysioTeam.')]))

# 15 ─ Westerhoff, Visbek
mk('westerhoff', dict(google=(4.6, 29), slug='physiotherapie-westerhoff-visbek', firma='Physiotherapie Westerhoff', kurz='Physiotherapie Westerhoff', ort='Visbek', strasse='Overbergstraße 6', plz='49429',
    tel='04445 1833', tel_i='+4944451833', mail='info@westerhoff-physio.de', web='westerhoff-physio.de', p='#0080c8', dk='#0c2f47', s2='#eef6fb', fam=RUB, fonts='r10kicker',
    logo=(J('westerhoff', '000'), 420, 'trim'), lh=62, hero='r', card='4/3', himgs=[J('westerhoff', '001'), J('westerhoff', '001')], cols='46fr 54fr',
    ey='Krankengymnastik · Physiotherapie in Visbek', h1='Für Ihr <em>Wohlbefinden.</em>',
    sub='Physiotherapie, Rehasport, Funktionstraining und Pilates in Visbek. Unser Team ist morgens ab 7 Uhr und abends bis 20 Uhr für Sie da.',
    ubar=[('Ab 7 Uhr', 'Mo bis Fr'), ('Bis 20 Uhr', 'Mo bis Do'), ('Rehasport', 'und Pilates')],
    sv_h2='Unsere Leistungen <em>für Ihr Wohlbefinden.</em>', sv_lead='Ein breites Angebot, von der klassischen Krankengymnastik bis zum Kurs.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie, auch nach Bobath und PNF.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Manuelle Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'), ('Rehasport und Funktionstraining', 'Kurse mit ausgebildeten Übungsleiterinnen.'),
          ('Pilates', 'Mattenpilates mit zertifizierten Pilatestrainerinnen.'), ('Massage und Wellness', 'Zum Beispiel Hot-Stone-Massage und Fußreflexzonentherapie.')],
    top=dict(nav='Kurse', tag='Rehasport und Pilates', h2='Gemeinsam <em>in Bewegung bleiben.</em>', img=J('westerhoff', '015'),
             txt='In unseren Kursen trainieren Sie in der Gruppe: Rehasport und Funktionstraining mit ausgebildeten Übungsleiterinnen, dazu Mattenpilates mit zertifizierten Trainerinnen.',
             pts=['Rehasport und Funktionstraining', 'Mattenpilates', 'Heller Kursraum'], btn='Kursplatz anfragen', pop='Rehasport, Funktionstraining und Pilates.'),
    team=dict(ey='Das Team', h2='Unser Team <em>für Ihr Wohlbefinden.</em>', img=J('westerhoff', '002'), mw=380, cap='Aus dem Team der Physiotherapie Westerhoff',
              paras=['Inhaberin der Praxis ist Heike Zwanefeld. Unser Team hat Zusatzqualifikationen von der Lymphdrainage über das Fasziendistorsionsmodell (FDM nach Typaldos) bis zum kinesiologischen Tapen.',
                     'Termine vergeben wir nach telefonischer Vereinbarung.'],
              tl=[('4,6 Sterne', 'bei Google'), ('Overbergstr. 6', 'Visbek')]),
    gal=[(J('westerhoff', '003'), '50% 30%'), (J('westerhoff', '004'), '50% 30%'), (J('westerhoff', '025'), '50% 50%')],
    stimmen=['Mir wurde dort sehr schnell geholfen. Jedes Mal einfach top.', 'Ich gehe gern in die Praxis. Die Therapeuten sind freundlich und kompetent.', 'Kein Problem mit Terminen, dazu netter Service und gute Massagen.'],
    hours=[('Mo bis Do', '7–12.30 · 14–20 Uhr'), ('Fr', '7–13 Uhr')], cats=['ruecken', 'rezept', 'lymph', 'training', 'massage', 'haus'], bot='Wim', notfall=NF, mq_end='Physiotherapie in Visbek',
    rec={'ruecken': ['Manuelle Therapie', 'Wir schauen uns Ihren Rücken genau an.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, Termine gibt es ab 7 Uhr.'], 'lymph': ['Manuelle Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'],
         'training': ['Rehasport und Funktionstraining', 'In unseren Kursen bleiben Sie in Bewegung.'], 'massage': ['Massage und Wellness', 'Zum Beispiel mit einer Hot-Stone-Massage.'], 'haus': ['Krankengymnastik', 'Fragen Sie am Telefon nach Hausbesuchen.']},
    pops=[('g3.jpg', 'Kursraum', 'Heller Raum für Rehasport und Pilates.')]))

# 16 ─ Therapiezentrum Hörstel
mk('hoerstel', dict(google=(4.6, 20), slug='therapiezentrum-hoerstel', firma='Therapiezentrum Hörstel', kurz='Therapiezentrum Hörstel', ort='Hörstel', strasse='Alte Glashüttenstraße 2', plz='48477',
    tel='05459 98198', tel_i='+49545998198', web='tzhoerstel.de', p='#6b7350', dk='#3a3f2a', s2='#f3f2ec', fam=SORA, fonts='r11physiovital',
    logo=('/home/claude/r28raw/hoerstel/logo.png', 400), lh=64, hero='r', card='16/9', himgs=[J('hoerstel', '003'), J('hoerstel', '003')], cols='44fr 56fr',
    ey='Therapiezentrum Hörstel · Dreierwalde', h1='Gut betreut. <em>An zwei Standorten.</em>',
    sub='Physiotherapie, Reha-Sport, T-RENA und Gesundheitscoaching in Hörstel und Dreierwalde. Termine vereinbaren Sie rund um die Uhr über unsere Online-Rezeption.',
    ubar=[('2 Standorte', 'Hörstel und Dreierwalde'), ('Online-Rezeption', 'rund um die Uhr'), ('Seit über 25 Jahren', 'für die Region da')],
    sv_h2='Alles für <em>Ihre Gesundheit.</em>', sv_lead='Vom Rezept bis zum Gesundheitscoaching: Wir begleiten Sie mit einem großen Team.',
    svcs=[('Physiotherapie', 'Krankengymnastik, Manuelle Therapie, Bobath, Lymphdrainage und mehr.'), ('Reha-Sport', 'Bewegung in der Gruppe, ärztlich verordnet.'),
          ('T-RENA und RV-FIT', 'Nachsorge und Prävention der Deutschen Rentenversicherung.'), ('Heilpraktische Behandlung', 'Behandlung auch ohne ärztliche Verordnung.'),
          ('Gesundheitscoaching', 'Beratung für einen gesunden Alltag.'), ('Kinder', 'Auch Kinder sind bei uns in guten Händen.')],
    top=dict(nav='Online-Rezeption', tag='Online-Rezeption', h2='Termine, <em>wann es Ihnen passt.</em>', img=J('hoerstel', '020'),
             txt='Ohne Warten am Telefon: Über unsere Online-Rezeption können Sie von überall und zu jeder Zeit Termine vereinbaren, verschieben oder absagen und Verordnungen einreichen.',
             pts=['Rund um die Uhr erreichbar', 'Termine vereinbaren und verschieben', 'Verordnung einfach einreichen'], btn='Termin anfragen', pop='Termine rund um die Uhr über die Online-Rezeption.'),
    team=dict(ey='Über uns', h2='Ein Team, <em>das zuhört.</em>', img=J('hoerstel', '003'), cap='Empfang im Therapiezentrum Hörstel',
              paras=['Patienten beschreiben uns als sehr kompetentes Team, das berät, unterstützt und immer ein offenes Ohr hat. Manche Familien kommen seit 25 Jahren zu uns.',
                     'Sie finden uns in Hörstel an der Alten Glashüttenstraße und in Dreierwalde an der Hopstener Straße.'],
              tl=[('2', 'Standorte'), ('Alte Glashüttenstr. 2', 'Hörstel')]),
    gal=[(J('hoerstel', '019'), '50% 50%'), (J('hoerstel', '018'), '50% 50%'), (J('hoerstel', '023'), '50% 50%')],
    stimmen=['Wir wurden herzlich empfangen, alles wurde klar erklärt. Der Umgang mit Kindern war einfach tadellos.', 'Seit 25 Jahren hole ich mir hier Hilfe für meine Kinder und mich. Sehr kompetente Therapeuten mit offenem Ohr.', 'Freundliches und engagiertes Team, auch am Telefon immer patientenorientiert.'],
    hours=[('Mo bis Do', '8–19 Uhr'), ('Fr', '8–17 Uhr')], cats=['ruecken', 'rezept', 'op', 'kind', 'selbst', 'training'], bot='Toni', notfall=NF, mq_end='Physiotherapie in Hörstel',
    rec={'ruecken': ['Physiotherapie', 'Wir beraten Sie und zeigen Übungen für zu Hause.'], 'rezept': ['Physiotherapie', 'Am schnellsten geht es über die Online-Rezeption.'], 'op': ['T-RENA und RV-FIT', 'Nach der Reha bleiben Sie mit T-RENA dran.'],
         'kind': ['Kinder', 'Kinder behandeln wir mit viel Geduld.'], 'selbst': ['Heilpraktische Behandlung', 'Auch ohne Verordnung können wir behandeln.'], 'training': ['Reha-Sport', 'Reha-Sport gibt es bei uns in der Gruppe.']},
    pops=[('g1.jpg', 'Zwei Standorte', 'In Hörstel und in Dreierwalde.')]))

# 17 ─ Therapiezentrum Im Kamp, Hasbergen
KB = '/home/claude/r28raw/imkamp/big/'
mk('imkamp', dict(google=(5.0, 11), slug='therapiezentrum-im-kamp-hasbergen', firma='Therapiezentrum Im Kamp', kurz='Therapiezentrum Im Kamp', ort='Hasbergen', strasse='Im Kamp 57', plz='49205',
    tel='05405 6080590', tel_i='+4954056080590', mail='therapiezentrum-im-kamp@web.de', web='therapiezentrum-im-kamp.de', p='#e21a4e', dk='#3f4041', s2='#f6f2f3', fam=ROB, fonts='r10liekam',
    logo=(J('imkamp', '000'), 480, 'trim'), lh=40, hero='r', himgs=[KB + '05.jpg', KB + '07.jpg'], cols='46fr 54fr',
    ey='Physiotherapie in Hasbergen', h1='Wir nehmen uns <em>die Zeit.</em>',
    sub='Frau Komning und ihr Team bieten eine qualifizierte und individuelle Behandlung. Wir nehmen Patienten aller Krankenkassen an und kommen Ihnen bei den Terminen entgegen.',
    ubar=[('Alle Kassen', 'und privat'), ('Bis 19 Uhr', 'Di und Do'), ('Parkplätze', 'direkt am Haus')],
    sv_h2='Ihre Gesundheit <em>ist uns wichtig.</em>', sv_lead='Verschaffen Sie sich einen Überblick über unsere Leistungen.',
    svcs=[('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'), ('FDM – Fasziendistorsionsmodell', 'Neu bei uns: Behandlung nach dem Fasziendistorsionsmodell.'),
          ('CMD – Kiefergelenksbehandlung', 'Behandlung bei Beschwerden am Kiefergelenk.'), ('Bobath-Therapie', 'Therapie bei neurologischen Erkrankungen.'),
          ('Lymphdrainage und Krankengymnastik', 'Klassische Physiotherapie nach Verordnung.'), ('Hausbesuche', 'Mit Verordnung behandeln wir Sie auch zu Hause.')],
    top=dict(nav='Wellness', tag='Wellnessangebote', h2='Eine Massage <em>als Geschenk.</em>', img=KB + '08.jpg',
             txt='Klassische Massage, Luxus-Massage über 60 Minuten oder ergänzend Fango-Wärmetherapie: Unsere Wellnessangebote gibt es auch als Gutschein zum Verschenken.',
             pts=['Klassische Massage ab 20 Minuten', 'Luxus-Massage 60 Minuten', 'Gutscheine erhältlich'], btn='Wellness anfragen', pop='Massagen auch als Gutschein zum Verschenken.'),
    team=dict(ey='Über uns', h2='Frau Komning <em>und ihr Team.</em>', img=J('imkamp', '006'), cap='Empfang im Therapiezentrum Im Kamp',
              paras=['Patienten beschreiben Frau Komning als sehr kompetent und einfühlsam. Sie beantwortet Fragen gründlich und gibt Übungen mit, die sich zu Hause leicht fortführen lassen.',
                     'Die Praxis ist hell, schön und sauber. Parkplätze gibt es direkt am Haus.'],
              tl=[('5,0 Sterne', 'bei Google'), ('Im Kamp 57', 'Hasbergen')]),
    gal=[(KB + '06.jpg', '50% 50%'), (KB + '01.jpg', '50% 50%'), (KB + '12.jpg', '50% 50%')],
    job=dict(img=KB + '03.jpg', h2='Wir haben <em>einen Job für Sie!</em>', txt='Wir suchen tatkräftige Unterstützung für unser Team in Hasbergen. Sind Sie auf der Suche nach einer Anstellung als Physiotherapeut:in (m/w/d)?',
             pts=['Team in Hasbergen', 'Helle, freundliche Praxis', 'Großzügige Zeitplanung']),
    stimmen=['Ich bin seit Jahren bei Frau Komning und fühle mich sehr gut aufgehoben. Die Praxis ist hell, schön und sauber.', 'Sehr kompetent und einfühlsam. Ich empfehle sie ohne Zögern weiter.', 'Zwei andere Praxen hatten abgesagt, hier bekam ich sofort einen Termin. Sehr hilfsbereit.', 'Sehr angenehm, sehr kompetent, sehr zu empfehlen!'],
    hours=[('Mo, Mi', '8–12 Uhr'), ('Di, Do', '7–19 Uhr'), ('Fr', '8–12 · 15–19 Uhr')], cats=['ruecken', 'rezept', 'cmd', 'neuro', 'haus', 'job'], bot='Kim', notfall=NF, mq_end='Physiotherapie in Hasbergen',
    rec={'ruecken': ['Manuelle Therapie', 'Wir nehmen uns Zeit für Ihre Beschwerden.'], 'rezept': ['Lymphdrainage und Krankengymnastik', 'Rufen Sie an, wir kommen Ihnen bei den Zeiten entgegen.'], 'cmd': ['CMD – Kiefergelenksbehandlung', 'Kieferbeschwerden behandeln wir gezielt.'],
         'neuro': ['Bobath-Therapie', 'Bei neurologischen Erkrankungen arbeiten wir nach Bobath.'], 'haus': ['Hausbesuche', 'Mit Verordnung kommen wir zu Ihnen.'], 'job': ['Manuelle Therapie', 'Wir haben einen Job für Sie. Melden Sie sich!']},
    pops=[('jb.jpg', 'Verstärkung gesucht', 'Physiotherapeut:in (m/w/d) für Hasbergen.')]))

# 18 ─ PhysioAktiv, Georgsmarienhütte
mk('physioaktiv', dict(google=(5.0, 20), slug='physioaktiv-georgsmarienhuette', firma='PhysioAktiv Tanja Sudowe', kurz='PhysioAktiv', ort='Georgsmarienhütte', strasse='Osterheide 7', plz='49124',
    tel='05401 8059639', tel_i='+4954018059639', mail='info@physioaktiv-os.de', web='physioaktiv-os.de', p='#3497a4', dk='#262628', s2='#eef6f7', fam=POP, fonts='r14sch',
    logo=(J('physioaktiv', '000'), 480, 'trim'), lh=58, hero='r', himgs=[J('physioaktiv', '011'), J('physioaktiv', '001')], cols='46fr 54fr',
    ey='Physiotherapie in Georgsmarienhütte', h1='Der Mensch steht <em>bei uns im Mittelpunkt.</em>',
    sub='Individuelle Lösungen für Ihre Gesundheit und Ihr Wohlbefinden. Mit einem geschulten Team, regelmäßigen Fortbildungen und dem Blick auf aktuelle Behandlungsmethoden.',
    ubar=[('5,0 Sterne', '20 Google-Bewertungen'), ('Hausbesuche', 'auf Verordnung'), ('Parkplätze', 'direkt an der Praxis')],
    sv_h2='Individuell <em>für Sie geplant.</em>', sv_lead='Wir nehmen uns Zeit und gehen auf jedes Problem einzeln ein.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie, auch nach Bobath.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Manuelle Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'), ('Massage und Fango', 'Wohltuende Anwendungen für die Muskulatur.'),
          ('Kinesiotaping und Triggerpunkte', 'Ergänzende Methoden für Ihre Behandlung.'), ('Hausbesuche', 'Physiotherapie, die zu Ihnen kommt.')],
    top=dict(nav='Hausbesuche', tag='Hausbesuche', h2='Physiotherapie, <em>die zu Ihnen kommt.</em>', img=J('physioaktiv', '002'),
             txt='Wir helfen Ihnen auch dann, wenn ein Besuch in der Praxis nicht möglich ist. Ein Hausbesuch ist möglich, wenn Ihr Arzt ihn verordnet hat, zum Beispiel bei Pflegebedürftigkeit.',
             pts=['Mit ärztlicher Verordnung', 'Auch bei Pflegebedürftigkeit', 'Enge Absprache mit Arzt und Angehörigen'], btn='Hausbesuch anfragen', pop='Wir kommen auch zu Ihnen nach Hause.'),
    team=dict(ey='Das Team', h2='Tanja Sudowe <em>und ihr Team.</em>', img=J('physioaktiv', '001'), cap='Behandlungsraum bei PhysioAktiv',
              paras=['Praxisinhaberin Tanja Sudowe arbeitet mit den Physiotherapeuten Stephan Runte, Melina Wachau und Birgit Menke. Am Empfang begrüßen Sie Sarah Jane de Rijk-Rosczich und Nina Pluscyk.',
                     'Und dann ist da noch Zara, unser Praxishund.'],
              tl=[('20', 'Bewertungen, alle mit 5 Sternen'), ('Osterheide 7', 'Georgsmarienhütte')]),
    css2='.tg28 .grid{grid-template-columns:repeat(auto-fill,150px)!important}.tg28 figure>div{aspect-ratio:1/1!important;border-radius:50%!important}.tg28 img{object-position:50% 30%!important}', people=[(J('physioaktiv', '012'), 'Tanja Sudowe', 'Praxisinhaberin'), (J('physioaktiv', '013'), 'Stephan Runte', 'Physiotherapeut'), (J('physioaktiv', '014'), 'Melina Wachau', 'Physiotherapeutin'), (J('physioaktiv', '015'), 'Birgit Menke', 'Physiotherapeutin'), (J('physioaktiv', '017'), 'Zara', 'Praxishund')],
    gal=[(J('physioaktiv', '003'), '50% 50%'), (J('physioaktiv', '004'), '50% 50%'), (J('physioaktiv', '006'), '50% 50%')],
    stimmen=['Sehr persönliche und fachlich kompetente Physiotherapie. Das ganze Team ist fantastisch.', 'Fachlich und menschlich einfach herausragend. Hier nimmt man sich wirklich Zeit.', 'Nach einem Besuch in der Notaufnahme bekam ich schnell eine zusätzliche Behandlung, die mir sehr geholfen hat.', 'Termine sind einfach und schnell zu bekommen, die Räume sind ordentlich und sauber.'],
    hours=[('Mo bis Do', '8–18 Uhr'), ('Fr', '8–13 Uhr')], cats=['ruecken', 'rezept', 'lymph', 'haus', 'neuro', 'massage'], bot='Zoe', notfall=NF, mq_end='Physiotherapie in Georgsmarienhütte',
    rec={'ruecken': ['Manuelle Therapie', 'Wir gehen auf jedes Problem einzeln ein.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, Termine gibt es meist schnell.'], 'lymph': ['Manuelle Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'],
         'haus': ['Hausbesuche', 'Mit Verordnung kommen wir zu Ihnen nach Hause.'], 'neuro': ['Krankengymnastik', 'Bei neurologischen Erkrankungen arbeiten wir nach Bobath.'], 'massage': ['Massage und Fango', 'Massage und Fango tun der Muskulatur gut.']},
    pops=[('g1.jpg', 'Praxishund Zara', 'Bei uns begrüßt Sie auch Zara.')]))

# 19 ─ Reinermann, Fürstenau
mk('reinermann', dict(google=(4.9, 11), slug='physiotherapie-reinermann-fuerstenau', firma='Physiotherapie R. Reinermann', kurz='Physiotherapie Reinermann', ort='Fürstenau', strasse='Schorfteichstraße 13', plz='49584',
    tel='05901 7766', tel_i='+4959017766', web='physiotherapie-reinermann.de', p='#d8952f', pi='#1b1d22', em='#a56a10', dk='#252629', s2='#f8f4ec', fam=MON, fonts='r12meyer',
    logo_txt='Physiotherapie Reinermann<small>Fürstenau</small>', prmw=400, hero='r', card='3/2', himgs=[J('reinermann', '017'), J('reinermann', '017')], cols='44fr 56fr',
    ey='Physiotherapie in Fürstenau', h1='Professionell. <em>Und doch persönlich.</em>',
    sub='Bei uns stehen Sie im Mittelpunkt. Fühlen Sie sich gut aufgehoben und gut behandelt. So möchte man behandelt werden.',
    ubar=[('Ab 7.30 Uhr', 'Mo bis Fr'), ('10 Menschen', 'im Team'), ('Trainingsraum', 'in der Praxis')],
    sv_h2='Der Mensch <em>im Mittelpunkt.</em>', sv_lead='Physiotherapie ist eine sehr persönliche Angelegenheit. Deshalb lernen wir unsere Patienten zuerst kennen.',
    svcs=[('Krankengymnastik', 'Klassische Physiotherapie nach ärztlicher Verordnung.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Lymphdrainage', 'Sanfte Entstauung, zum Beispiel nach Operationen.'), ('Krankengymnastik am Gerät', 'Training im eigenen Trainingsraum unter Anleitung.'),
          ('Kiefergelenk (CMD) und Schwindel', 'Behandlung bei Kieferbeschwerden und Schwindel.'), ('Massage', 'Klassische Massage, auch für Selbstzahler.')],
    top=dict(nav='Training', tag='Training in der Praxis', h2='Kraft aufbauen, <em>gut angeleitet.</em>', img=J('reinermann', '013'),
             txt='In unserem Trainingsraum trainieren Sie an Geräten, angeleitet von unseren Therapeutinnen und Therapeuten. Ideal nach Verletzungen oder bei Rückenbeschwerden.',
             pts=['Eigener Trainingsraum', 'Angeleitet vom Praxisteam', 'Mit Verordnung oder privat'], btn='Termin anfragen', pop='Training an Geräten in unserer Praxis.'),
    team=dict(ey='Über uns', h2='Rudolf Reinermann <em>und sein Team.</em>', img=J('reinermann', '019'), cap='Empfang der Physiotherapie Reinermann',
              paras=['Inhaber Rudolf Reinermann führt die Praxis mit sieben Therapeutinnen und zwei Kolleginnen an der Rezeption.',
                     'Manche Patienten kommen seit fast 20 Jahren jede Woche zu uns.'],
              tl=[('10', 'Menschen im Team'), ('Schorfteichstr. 13', 'Fürstenau')]),
    people=[(J('reinermann', '003'), 'Rudolf Reinermann', 'Inhaber'), (J('reinermann', '004'), 'Birgit Tegethoff', 'Therapeutin'), (J('reinermann', '005'), 'Franka Chabalowitz', 'Therapeutin'), (J('reinermann', '006'), 'Melanie Rickhaus', 'Therapeutin'),
            (J('reinermann', '007'), 'Pauline Gülker', 'Therapeutin'), (J('reinermann', '008'), 'Kristin Lohstroh', 'Therapeutin'), (J('reinermann', '009'), 'Maren Wolke', 'Therapeutin'), (J('reinermann', '010'), 'Marianne Wulfern', 'Rezeption'),
            (J('reinermann', '011'), 'Frederieke Möller-Herrman', 'Therapeutin'), (J('reinermann', '012'), 'Petra Hein', 'Rezeption')],
    gal=[(J('reinermann', '014'), '50% 50%'), (J('reinermann', '015'), '50% 50%'), (J('reinermann', '016'), '50% 50%')],
    stimmen=['Eine echte Hilfe für gestresste Rücken. Ich sitze viel bei der Arbeit und komme privat.', 'Sehr zu empfehlen. Termine werden eingehalten, das Team ist immer freundlich. Ich komme seit fast 20 Jahren.', 'Sehr freundliches Personal und kompetente Behandlung.'],
    hours=[('Mo, Di, Do', '7.30–19 Uhr'), ('Mi', '7.30–18.30 Uhr'), ('Fr', '7.30–14 Uhr')], cats=['ruecken', 'rezept', 'op', 'lymph', 'training', 'selbst'], bot='Rudi', notfall=NF, mq_end='Physiotherapie in Fürstenau',
    rec={'ruecken': ['Manuelle Therapie', 'Gerade bei langem Sitzen können wir helfen.'], 'rezept': ['Krankengymnastik', 'Rufen Sie an, Termine gibt es ab 7.30 Uhr.'], 'op': ['Krankengymnastik am Gerät', 'Nach der OP bauen wir mit Ihnen wieder Kraft auf.'],
         'lymph': ['Lymphdrainage', 'Lymphdrainage bieten wir mit Verordnung an.'], 'training': ['Krankengymnastik am Gerät', 'Wir haben einen eigenen Trainingsraum.'], 'selbst': ['Massage', 'Viele Patienten kommen auch privat zu uns.']},
    pops=[('g1.jpg', 'Trainingsraum', 'Training an Geräten direkt in der Praxis.')]))

# 20 ─ Stefanie Tröbs, Diepholz
mk('troebs', dict(slug='physiotherapie-troebs-diepholz', firma='Stefanie Tröbs – Praxis für Physiotherapie', kurz='Praxis Tröbs', ort='Diepholz', strasse='Richtweg 1', plz='49356',
    tel='05441 1275', tel_i='+4954411275', web='stefanie-troebs.de', p='#4fb3b5', pi='#10292a', em='#2a8a8c', dk='#21343a', s2='#eef7f7', fam=ROB, fonts='r10liekam',
    logo=(J('troebs', '000'), 620, 'alphacrop'), lh=44, hero='r', himgs=[J('troebs', '011'), J('troebs', '016')], cols='46fr 54fr',
    ey='Physiotherapie in Diepholz', h1='Meine Bewegung. <em>Meine Gesundheit.</em>',
    sub='Mit mehr als 30 Jahren Erfahrung helfen wir Ihnen gern dabei, Ihre Beschwerden gezielt zu behandeln und Ihr Allgemeinbefinden zu verbessern. Auch ohne ärztliche Verordnung.',
    ubar=[('30+ Jahre', 'Erfahrung'), ('Bis 19.30 Uhr', 'Mo bis Do'), ('Ohne Rezept', 'möglich')],
    sv_h2='Individuell auf Sie <em>und Ihr Krankheitsbild.</em>', sv_lead='Bei verordneten Leistungen übernimmt die Krankenkasse bis zu 100 % der Kosten. Sprechen Sie uns gern an.',
    svcs=[('Physiotherapie', 'Behandelt Einschränkungen der Bewegungs- und Funktionsfähigkeit des Körpers.'), ('Manuelle Therapie', 'Gezielte Techniken für Gelenke und Wirbelsäule.'),
          ('Lymphdrainage', 'Mit ausgebildeten Lymphdrainagetherapeutinnen.'), ('Schmerztherapie nach Liebscher und Bracht', 'Stefanie Tröbs-Kütemann ist dafür ausgebildet.'),
          ('Präventionskurse', 'Kurse unter Leitung unserer Therapeutinnen.'), ('Training', 'Großer Trainingsbereich mit Seilzügen, Sprossenwand und Boxsack.')],
    top=dict(nav='Training', tag='Der Trainingsbereich', h2='Bewegung, <em>die Spaß macht.</em>', img=J('troebs', '013'),
             txt='Unser Trainingsbereich ist mehr als ein Geräteraum: Seilzüge, Kletterwand, Schlingentrainer und Boxsack bringen Abwechslung in Ihre Therapie.',
             pts=['Großer, heller Trainingsbereich', 'Vielseitige Geräte', 'Begleitet von Therapeutinnen'], btn='Termin anfragen', pop='Ein Trainingsbereich, der Spaß macht.'),
    team=dict(ey='Über uns', h2='Stefanie Tröbs-Kütemann <em>und ihr Team.</em>', img=J('troebs', '010'), cap='Das Team der Praxis Tröbs',
              paras=['Praxisinhaberin Stefanie Tröbs-Kütemann ist Heilpraktikerin für Physiotherapie, Manual- und Lymphdrainagetherapeutin und Schmerztherapeutin nach Liebscher und Bracht.',
                     'Patienten nennen die Praxis „eine echte Oase“ und loben, dass jede Behandlung Übungen für zu Hause enthält.'],
              tl=[('30+', 'Jahre Erfahrung'), ('Richtweg 1', 'Diepholz')]),
    gal=[(J('troebs', '012'), '50% 50%'), (J('troebs', '015'), '50% 50%'), (J('troebs', '014'), '50% 50%')],
    stimmen=['Goldene Hände! Die Therapeutin findet genau die Stellen, die Beschwerden machen. Das ganze Team ist herzlich und kompetent.', 'Ich rief an und hatte 20 Minuten später einen Termin. Alle waren sehr freundlich.', 'Die Praxis ist eine echte Oase. Jede Behandlung ist gut aufgebaut, mit Übungen für zu Hause.', 'Die Physiotherapie ist genau auf mich abgestimmt. Freundliches Personal, einfache Terminvergabe.'],
    hours=[('Mo bis Do', '8–19.30 Uhr'), ('Fr', '8–15.30 Uhr'), ('Weitere Termine', 'nach Vereinbarung')], cats=['ruecken', 'akut', 'rezept', 'selbst', 'lymph', 'training'], bot='Steffi', notfall=NF, mq_end='Physiotherapie in Diepholz',
    rec={'ruecken': ['Schmerztherapie nach Liebscher und Bracht', 'Wir suchen die Stellen, die Beschwerden machen.'], 'akut': ['Physiotherapie', 'Rufen Sie an, oft geht es sehr schnell.'], 'rezept': ['Physiotherapie', 'Mit Rezept übernimmt die Kasse bis zu 100 %.'],
         'selbst': ['Physiotherapie', 'Termine gibt es auch ohne ärztliche Verordnung.'], 'lymph': ['Lymphdrainage', 'Lymphdrainage mit ausgebildeten Therapeutinnen.'], 'training': ['Training', 'Unser Trainingsbereich macht Spaß.']},
    pops=[('g2.jpg', 'Ohne Rezept', 'Termine auch ohne ärztliche Verordnung.')]))
