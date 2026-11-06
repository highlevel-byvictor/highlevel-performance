#!/usr/bin/env python3
"""Google Fonts lokal ablegen (nur latin-Teilmenge), damit jede Firma eigene Schriften ohne Google-Abruf bekommt.
Aufruf: python3 tools/vorschau/fonts_holen.py <set-name> "family=Playfair+Display:ital,wght@0,400..700;1,400..700" "family=Montserrat:wght@300..600"
"""
import re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

def holen(name, families):
    url = "https://fonts.googleapis.com/css2?" + "&".join(families) + "&display=swap"
    css = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode()
    out = []
    for block in re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S):
        if block[0] != "latin": continue
        b = block[1]
        src = re.search(r"url\((https://[^)]+\.woff2)\)", b).group(1)
        fn = src.rsplit("/", 1)[1]
        dest = ROOT / "assets" / "fonts" / fn
        if not dest.exists(): dest.write_bytes(urllib.request.urlopen(urllib.request.Request(src, headers=UA), timeout=30).read())
        out.append(b.replace(src, "../../assets/fonts/" + fn))
    (Path(__file__).parent / "fonts" / f"{name}.css").write_text("\n".join(out) + "\n")
    print(name, len(out), "Schnitte")

if __name__ == "__main__":
    holen(sys.argv[1], sys.argv[2:])
