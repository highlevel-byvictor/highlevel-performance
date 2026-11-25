"""Akquise DM 25.11.2026: gemeinsame Helfer (Kosmetikstudios)."""
from lib import *

def site(**kw):
    s = dict(kw); s.setdefault('du', False); s.setdefault('branche', 'Kosmetikstudio'); s.setdefault('runde', 'Akquise DM 25.11.2026'); return s

def BOT(name, tag, firma, s, qa, tour):
    return dict(name=name, tag=tag, hello=f'Guten Tag! Ich bin <b>{name}</b>. Soll ich Ihnen kurz zeigen, was Sie bei {firma} erwartet?',
                hi=f'Guten Tag, ich bin {name} von {firma}. Wobei darf ich helfen?', qa=[list(x) for x in qa], tour=[[t] for t in tour])

def EMO(rgb, pos='center 50%', dark=False, pic_w=420, flip=False, mpos='50% 30%', mh=44, bgl=0):
    """Beinke-Hero: Emotionsbild scharf im Hintergrund, Verlauf in Markenfarbe von links, Text links, eigenes Foto rechts unten.
    Handy: Bild als Band oben (mh vh), Text darunter, damit nie Text über Gesichtern liegt."""
    c = rgb; fl = 'transform:scaleX(-1);' if flip else ''
    return (f".hx.hasbg::before{{inset:0!important;filter:none!important;opacity:1!important;background-position:{pos}!important;{fl}left:{bgl}%!important}}"
            f".hx.hasbg::after{{content:'';position:absolute;inset:0;z-index:0;background:linear-gradient(90deg,rgba({c},1) 0%,rgba({c},.95) {max(bgl,36)}%,rgba({c},.25) {max(bgl,36)+(12 if bgl else 24)}%,rgba({c},0) {max(bgl,36)+(20 if bgl else 38)}%)}}"
            f".hx.hasbg>.w{{position:relative;z-index:1}}.hx .pic{{max-width:{pic_w}px;justify-self:end;align-self:end}}.hx.hasbg{{min-height:min(94vh,880px);display:flex;align-items:center}}"
            + (".hx h1,.hx .sub,.hx .ey{color:#fff}.hx .sub{opacity:.9}" if dark else '')
            + f"@media(max-width:820px){{.hx.hasbg{{display:block;padding-top:calc({mh}vh + 14px)}}.hx.hasbg::before{{height:{mh}vh;bottom:auto!important;background-position:{mpos}!important;left:0!important;transform:none}}"
            f".hx.hasbg::after{{background:linear-gradient(0deg,rgba({c},1) calc(100% - {mh}vh),rgba({c},0) calc(100% - {mh}vh + 120px))}}.hx .pic{{justify-self:stretch;max-width:none}}.hx h1{{hyphens:manual}}}}")
PIX = '/home/claude/pixa16/'
HI = '/home/claude/r28raw/'

def BOTDU(name, tag, firma, s, qa, tour):
    return dict(name=name, tag=tag, hello=f'Hallo! Ich bin <b>{name}</b>. Soll ich dir kurz zeigen, was dich bei {firma} erwartet?',
                hi=f'Hallo, ich bin {name} von {firma}. Wobei darf ich helfen?', qa=[list(x) for x in qa], tour=[[t] for t in tour])

V = '--bg:#fff;--ink:{ink};--mute:{mute};--p:{p};--p-ink:{pi};--a:{p};--a-ink:{pi};--dk:{dk};--s:#fff;--s2:{s2};--fh:{fh};--fb:{fb};--r:0px;--r2:0px;--br:2px;--mq-bg:{dk};--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:{ink};--logo-h:{lh}px;--ft-bg:{ft};--hp-bg:{s2}'
DKHD = ';--hd-bg:{c};--hd-ink:#fff'
RUND = '.btn{border-radius:999px}.chip{border-radius:999px}.play span{border-radius:50%}.tag{border-radius:999px}.mcall a{border-radius:999px}'
