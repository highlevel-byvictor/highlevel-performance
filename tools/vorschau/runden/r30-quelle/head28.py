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

