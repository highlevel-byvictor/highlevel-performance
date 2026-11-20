import asyncio,glob,os,sys,json
from playwright.async_api import async_playwright
D=sorted(d for d in glob.glob('/home/claude/highlevel-performance/vorschau/*') if any(k in d for k in ['zahnarztpraxis-alfhausen-1633','austermann-bramsche-7523','am-markt-badbergen','spasova-rieste','kiefert-neuenkirchen','coenen-ankum','tischler-damme','lefert-kohl','osada-damme','natorp-holdorf']))
JS='''()=>{const vw=document.documentElement.clientWidth;const bad=[];document.querySelectorAll('h1,h2,h3,h4,p,a,button,b,strong,li,label,small,figcaption,input,select,textarea,img,figure,video,iframe,form,table').forEach(e=>{if(e.classList.contains('hp')||e.closest('.trk,.mq,.lot,.pop,.hlp-note,.mcall,[data-slider] .sl,.sl,.dots,nav,.mnav,.menu'))return;const cs=getComputedStyle(e);if(cs.display=='none'||cs.visibility=='hidden'||cs.opacity=='0')return;const r=e.getBoundingClientRect();if(r.width>0&&r.height>0&&(r.right>vw+1||r.left<-1))bad.push((e.tagName+'.'+String(e.className)).slice(0,30)+' '+Math.round(r.left)+'..'+Math.round(r.right)+' y'+Math.round(r.top+scrollY)+' '+(e.textContent||'').trim().slice(0,24))});return {sw:document.documentElement.scrollWidth,n:bad.length,bad:bad.slice(0,6)}}'''
WIDE=len(sys.argv)>1
async def main():
    tot=0
    async with async_playwright() as pw:
        b=await pw.webkit.launch()
        for W in (320,360,375,393,430):
            ctx=await b.new_context(viewport={'width':W,'height':780},device_scale_factor=2,is_mobile=True,has_touch=True,user_agent=pw.devices['iPhone 14']['user_agent'])
            for d in D:
                p=await ctx.new_page(); await p.goto('file://'+d+'/index.html'); 
                if WIDE: await p.add_style_tag(content='*{font-family:"DejaVu Sans",Verdana,sans-serif!important}')
                await p.evaluate("document.querySelectorAll('[data-r]').forEach(e=>e.classList.add('in'))")
                await p.wait_for_timeout(900)
                r=await p.evaluate(JS); n=os.path.basename(d)[:26]
                if r['n']: tot+=1; print(W,n,json.dumps(r,ensure_ascii=False))
                if W==393 and WIDE: await p.screenshot(path=f'/home/claude/r20shots/wk-{n}.png')
                await p.close()
            await ctx.close()
        await b.close()
    print('PROBLEME',tot)
asyncio.run(main())
