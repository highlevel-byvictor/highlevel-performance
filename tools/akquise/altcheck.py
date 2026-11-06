#!/usr/bin/env python3
"""Vorfilter für den Website-Akquise-Agenten: Wie veraltet ist eine Website?
Aufruf: python3 tools/akquise/altcheck.py https://firma.de [weitere ...]
Gibt pro Seite Punkte (0-10, höher = veralteter) und konkrete Schwachstellen aus (Basis für die Nachricht).
Nur ein Vorfilter – die Seite wird danach trotzdem angeschaut (Skill website-audit).
"""
import sys, re, ssl, time, json, urllib.request, datetime

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
JAHR = datetime.date.today().year

def hole(url):
    t = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25, context=ssl.create_default_context()) as r:
        html = r.read(3_000_000).decode("utf-8", "ignore"); final = r.geturl()
    return html, final, time.time() - t

def check(url):
    if not url.startswith("http"): url = "https://" + url
    try: html, final, dt = hole(url)
    except Exception as e:
        try: html, final, dt = hole(url.replace("https://", "http://"))
        except Exception as e2: return dict(url=url, fehler=str(e2)[:120], punkte=None)
    low = html.lower(); P = 0; S = []
    def pt(n, txt): nonlocal P; P += n; S.append(txt)
    if final.startswith("http://"): pt(2, "keine sichere Verbindung (kein https)")
    if 'name="viewport"' not in low and "name=viewport" not in low: pt(3, "nicht fürs Handy optimiert (kein mobiles Layout)")
    yrs = [int(y) for y in re.findall(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?((?:19|20)\d{2})", low)]
    if yrs and max(yrs) <= JAHR - 4: pt(2, f"Copyright-Hinweis steht noch auf {max(yrs)}")
    gen = re.findall(r'<meta name="generator" content="([^"]+)"', html, re.I)
    if any(re.search(r"wordpress [1-4]\.", g, re.I) for g in gen): pt(2, f"sehr alte WordPress-Version ({gen[0]})")
    if re.search(r"jquery[.-]1\.\d|jquery/1\.\d", low): pt(1, "veraltete Technik (jQuery 1.x)")
    if low.count("<table") >= 3 and "<div" in low and low.count("<table") > low.count("<section"): pt(2, "Layout aus Tabellen (Technik der 2000er)")
    if "<font" in low or "<marquee" in low or "<center>" in low: pt(2, "veraltetes HTML (font/center-Tags)")
    if ".swf" in low or "flash" in low and "shockwave" in low: pt(2, "Flash-Inhalte")
    if not re.search(r"tel:\+?\d", low): pt(1, "Telefonnummer nicht antippbar")
    if not re.search(r"termin|buchen|anfrag|kontakt", low[: len(low) // 2]): pt(1, "kein klarer Button zum Buchen/Anfragen oben")
    if dt > 4: pt(1, f"lädt langsam ({dt:.1f} s)")
    if "jimdo" in low and "jimdo-dolphin" not in low: pt(1, "alter Jimdo-Baukasten")
    if re.search(r"1&1|ionos.{0,20}(mywebsite|baukasten)|webbaukasten", low): pt(1, "einfacher Baukasten")
    if re.search(r"cookie", low) and re.search(r"(borlabs|cookiebot|consent)", low): S.append("(Cookie-Box vorhanden – prüfen, ob sie Inhalte verdeckt)")
    imgs = len(re.findall(r"<img", low))
    if imgs < 3: pt(1, "kaum Bilder auf der Startseite")
    return dict(url=final, punkte=min(P, 10), schwachstellen=S, ladezeit=round(dt, 1), bilder=imgs, generator=gen[:1])

if __name__ == "__main__":
    out = [check(u) for u in sys.argv[1:]]
    for o in sorted(out, key=lambda o: -(o["punkte"] or -1)):
        print(json.dumps(o, ensure_ascii=False))
