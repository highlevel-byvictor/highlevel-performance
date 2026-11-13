"""seim & partner Entwurf zusammenbauen: Schriften, Kit, Deutschlandkarte einbetten."""
import json, sys
from pathlib import Path
H=Path(__file__).parent; ROOT=Path('/home/claude/highlevel-performance')
KIT=ROOT/'tools/vorschau/runden/r10-quelle/hand'
D=ROOT/'vorschau/seim-partner-wiesbaden-8e15'
m=json.load(open('/home/claude/seim/map.json'))
hub=m['pts']['Wiesbaden']
svg=[f'<svg viewBox="-20 -10 {m["W"]+40} {m["H"]+20}" role="img" aria-label="Deutschlandkarte mit Projektregionen von seim &amp; partner"><defs><linearGradient id="fiber" x1="0" x2="1"><stop offset="0" stop-color="#F7941D"/><stop offset=".5" stop-color="#3FD0FF"/><stop offset="1" stop-color="#9FC3FF"/></linearGradient></defs><g class="de">']
hot={'Niedersachsen','Baden-Württemberg','Hessen','Sachsen'}
for n,d in m['paths']: svg.append(f'<path class="bl{" hot" if n in hot else ""}" d="{d}"><title>{n}</title></path>')
svg.append('</g><g>')
for n,(x,y) in m['pts'].items():
    if n=='Wiesbaden': continue
    cx=(hub[0]+x)/2+(y-hub[1])*.18; cy=(hub[1]+y)/2-(x-hub[0])*.18
    d=f'M{hub[0]:.1f},{hub[1]:.1f} Q{cx:.1f},{cy:.1f} {x:.1f},{y:.1f}'
    svg.append(f'<path class="route-base" d="{d}"/><path class="route" d="{d}"/>')
svg.append('</g><g>')
lab={'Friesland':(-8,-10,'end'),'Wesermarsch':(10,-6,'start'),'Weser-Ems':(10,8,'start'),'Osnabrück':(-10,4,'end'),'Nordost-Niedersachsen':(10,4,'start'),'Rhein-Neckar':(10,4,'start'),'Hochschwarzwald':(-10,4,'end'),'Pfullendorf':(10,4,'start'),'Klipphausen':(10,4,'start'),'Wiesbaden':(12,5,'start')}
for n,(x,y) in m['pts'].items():
    dx,dy,a=lab[n]; cls='node hub' if n=='Wiesbaden' else 'node'
    svg.append(f'<g class="{cls}" data-n="{n}"><circle class="r" cx="{x:.1f}" cy="{y:.1f}" r="6"/><circle class="c" cx="{x:.1f}" cy="{y:.1f}" r="{7 if n=="Wiesbaden" else 5}"/><text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{a}">{n.replace("Nordost-Niedersachsen","NO-Niedersachsen")}</text></g>')
svg.append('</g></svg>')
html=(H/'seim.html').read_text()
html=html.replace('<!--MAP-->',''.join(svg)).replace('<!--KIT_CSS-->',(KIT/'kit.css').read_text()).replace('<!--KIT_JS-->',(KIT/'kit.js').read_text()).replace('<!--FONTS-->',(ROOT/'tools/vorschau/fonts/seim.css').read_text())
import re
html=re.sub(r'/\*.*?\*/','',html,flags=re.S)
(D/'index.html').write_text(html)
sys.path.insert(0,str(ROOT/'tools/vorschau')); import beauty; print(beauty.karte('Bahnhofstraße 67, 65185 Wiesbaden', D))
print('OK', len(html))
