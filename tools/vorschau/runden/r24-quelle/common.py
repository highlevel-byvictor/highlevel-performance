"""Runde 14: gemeinsame Helfer für die Fahrschul-Seiten."""
from lib import *

def BOT(name, tag, firma, s, cls, usp, qa=(), tour=(), du=True, ex=None, fin=None):
    """Fahrschul-Lotse: Führerschein-Check (Klasse + Alter + Wunsch) füllt die Anmeldung vor."""
    if du:
        hello = f'Hey! Ich bin <b>{name}</b> von {firma}. In 30 Sekunden finden wir raus, welcher Führerschein zu dir passt.'
        hi = f'Hey, ich bin {name}! Drei kurze Fragen, dann weißt du, welche Klasse du brauchst, und deine Anmeldung ist schon vorausgefüllt.'
    else:
        hello = f'Guten Tag! Ich bin <b>{name}</b> von {firma}. In 30 Sekunden finden wir heraus, welcher Führerschein zu Ihnen passt.'
        hi = f'Guten Tag, ich bin {name}! Drei kurze Fragen, dann wissen Sie, welche Klasse Sie brauchen, und Ihre Anmeldung ist schon vorausgefüllt.'
    return dict(name=name, tag=tag, hello=hello, hi=hi, du=du, cls=cls, usp=usp, qa=[list(x) for x in qa], tour=[list(x) for x in tour],
                tel=s['tel'], tel_i=s['tel_i'], ex=ex, finBtn=fin)

def site(**kw):
    s = dict(kw)
    s.setdefault('du', True)
    return s

def EMO(rgb, pos='center 50%', dark=False, pic_w=420):
    """Beinke-Hero: Emotionsbild scharf im Hintergrund, Verlauf in Markenfarbe von links, Text links, eigenes Foto rechts."""
    c = rgb
    ink = '#fff' if dark else 'inherit'
    return (f".hx.hasbg::before{{inset:0!important;filter:none!important;opacity:1!important;background-position:{pos}!important}}"
            f".hx.hasbg::after{{content:'';position:absolute;inset:0;z-index:0;background:linear-gradient(90deg,rgba({c},.97) 0%,rgba({c},.9) 36%,rgba({c},.25) 62%,rgba({c},0) 80%)}}"
            f".hx.hasbg>.w{{position:relative;z-index:1}}.hx .pic{{max-width:{pic_w}px;justify-self:end}}"
            + (f".hx h1,.hx .sub,.hx .ey{{color:{ink}}}.hx .sub{{opacity:.9}}" if dark else '')
            + f"@media(max-width:820px){{.hx.hasbg::after{{background:linear-gradient(0deg,rgba({c},1) 48%,rgba({c},.82) 70%,rgba({c},.35))}}.hx .pic{{justify-self:stretch;max-width:none}}}}")

def MAPL(adr):
    import urllib.parse
    return 'https://www.google.com/maps/search/?api=1&amp;query=' + urllib.parse.quote_plus(adr)
