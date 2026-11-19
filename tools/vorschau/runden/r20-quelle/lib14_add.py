

# ───────────── Runde 14: Fahrschul-Bausteine ─────────────
ICO = {
 'auto': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 15l1.6-5.2A2 2 0 016.5 8.4h11a2 2 0 011.9 1.4L21 15v3a1 1 0 01-1 1h-1.5a1 1 0 01-1-1v-1H6.5v1a1 1 0 01-1 1H4a1 1 0 01-1-1z"/><circle cx="7.5" cy="14.2" r="1.2"/><circle cx="16.5" cy="14.2" r="1.2"/></svg>',
 'moto': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="5.5" cy="16.5" r="3"/><circle cx="18.5" cy="16.5" r="3"/><path d="M5.5 16.5l4-6h5l4 6M9.5 10.5L8 7.5h3M14.5 10.5l1.5-3h2.5"/></svg>',
 'roller': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="6" cy="17" r="2.5"/><circle cx="18" cy="17" r="2.5"/><path d="M8.5 17h7M15 6h2l1.5 8.5M6 17l3-6h5"/></svg>',
 'anh': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="7" y="7" width="12" height="8" rx="1.5"/><circle cx="12" cy="17.5" r="2"/><path d="M7 13H2"/></svg>',
 'lkw': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 6h12v10H2zM14 10h4l3 3v3h-7z"/><circle cx="6" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></svg>',
 'trak': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="7" cy="16" r="4"/><circle cx="18" cy="17" r="2.5"/><path d="M7 12V6h6l2 6h3l2 3M11 6v6"/></svg>'}
QN = {'auto': 'Auto', 'moto': 'Motorrad', 'roller': 'Roller', 'anh': 'Anhänger', 'lkw': 'Lkw / Bus', 'trak': 'Traktor'}

def quick(s, h=None):
    q = (h or {}).get('quick', s.get('quick'))
    if not q: return ''
    lbl = (h or {}).get('qlbl', 'Was willst du fahren?' if s.get('du') else 'Was möchten Sie fahren?')
    b = ''.join(f'<button type="button" data-check="{k}">{ICO[k]}{QN[k]}</button>' for k in q)
    return f'<div class="quick"><span>{lbl}</span>{b}</div>'

def orte_sel(s):
    o = s.get('form_orte')
    if not o: return ''
    return '<label>Standort<select>' + ''.join(f'<option>{x}</option>' for x in o) + '</select></label>'

def tbar(s):
    t = s.get('tbar')
    return f'<div class="tbar">{t}</div>' if t else ''

def klassen(id, ey, h2, lead, items, cls='', note=''):
    """items: (code, titel, text, alter, fahrzeug-key fürs Quiz)"""
    k = ''.join(f'<button type="button" class="k" data-r data-check="{v}"><small>{a}</small><b>{c}</b><h3>{t}</h3><p>{x}</p><span class="go">Passt das zu mir? →</span></button>' for c, t, x, a, v in items)
    n = f'<p class="note">{note}</p>' if note else ''
    return f'<section class="sec kl {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="grid">{k}</div>{n}</div></section>'

def ablauf(id, ey, h2, lead, items, cls=''):
    r = ''.join(f'<div data-r data-n="{i+1}"><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(items))
    return f'<section class="sec rd {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="road">{r}</div></div></section>'

def sorgen(id, ey, h2, lead, items, cls=''):
    r = ''.join(f'<div class="it" data-r><q>{a}</q><p>{b}</p></div>' for a, b in items)
    return f'<section class="sec so {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="grid">{r}</div></div></section>'

def orte(id, ey, h2, lead, items, cls=''):
    r = ''.join(f'<div class="o" data-r><b>{a}</b><span>{b}</span>{f"<i>{c}</i>" if c else ""}</div>' for a, b, c in items)
    return f'<section class="sec or {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="grid">{r}</div></div></section>'

def flotte(id, ey, h2, lead, items, cls='', cut=False):
    r = ''.join(f'<article class="v{" cut" if cut else ""}"><figure><img src="img/{i}" alt="{E(t)}" loading="lazy" style="object-position:{p}"></figure><div><h3>{t}</h3><span>{x}</span></div></article>' for i, t, x, p in items)
    return f'<section class="sec fl {cls}" id="{id}"><div class="w top" data-r>{head(ey,h2,lead)}</div><div class="trk">{r}</div></section>'

def eltern(id, img, ey, h2, txt, pts, btn, cls='', rev=False):
    li = ''.join(f'<li>{p}</li>' for p in pts)
    fig = f'<figure data-r><img src="img/{img}" alt="" loading="lazy"></figure>'
    tx = f'<div data-r="2"><p class="ey">{ey}</p><h2 class="h2">{h2}</h2><p class="lead">{txt}</p><ul>{li}</ul><a class="btn btn-a" href="#kontakt">{btn} {AR}</a></div>'
    return f'<section class="sec el {cls}" id="{id}"><div class="w">{tx + fig if rev else fig + tx}</div></section>'

def hero_x(s, h):
    g1 = h.get('g1'); g2 = h.get('g2')
    gl = (f'<div class="gl g1"><b>{g1[0]}</b>{g1[1]}</div>' if g1 else '') + (f'<div class="gl g2"><b>{g2[0]}</b>{g2[1]}</div>' if g2 else '')
    bg = f'<div class="bgimg"><img src="img/{h["bg"]}" alt=""></div>' if h.get('bg') else ''
    ctas = f'<div class="ctas"><a class="btn btn-a" href="#kontakt">{s["cta"]} {AR}</a><a class="btn btn-o" href="tel:{s["tel_i"]}">{PH} {s["tel"]}</a></div>'
    pic = f'<div class="pic" data-r="2"><img src="img/{h["img"]}" alt="{E(h.get("alt", s["firma"]))}" style="object-position:{h.get("pos","50% 50%")}">{gl}</div>'
    txt = f'<div data-r>{chip(s)}<p class="ey">{h["ey"]}</p><h1>{h["h1"]}</h1><p class="sub">{h["sub"]}</p>{ctas}{quick(s, h)}</div>'
    return f'<section class="hx" id="top">{bg}<div class="w">{txt}{pic}</div></section>'
