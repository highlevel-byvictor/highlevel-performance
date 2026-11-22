import sys,hashlib,json
from pathlib import Path
from playwright.sync_api import sync_playwright
H=Path(__file__).parent; ROOT=Path('/home/claude/highlevel-performance'); sys.path.insert(0,str(ROOT/'tools/vorschau')); sys.path.insert(0,str(H))
import qa
from sites import SITES
with sync_playwright() as p:
    br=p.chromium.launch()
    for k in sys.argv[1:] or list(SITES):
        s=SITES[k]; d=ROOT/'vorschau'/(s['slug']+'-'+hashlib.sha1(s['firma'].encode()).hexdigest()[:4])
        fe=qa.check_page(br,d); print('QA',k,'OK' if not fe else '',flush=True)
        for f in fe: print('   ',f[:230])
    br.close()
