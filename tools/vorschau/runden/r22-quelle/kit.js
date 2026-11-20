(function(){
 // Einblenden beim Scrollen
 var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'}):null;
 document.querySelectorAll('[data-r]').forEach(function(el){io?io.observe(el):el.classList.add('in')});
 // Navigation mobil
 document.querySelectorAll('[data-nav]').forEach(function(b){b.addEventListener('click',function(){document.body.classList.toggle('nav-open')})});
 document.querySelectorAll('.nav a').forEach(function(a){a.addEventListener('click',function(){document.body.classList.remove('nav-open')})});
 // Header beim Scrollen
 var hd=document.querySelector('[data-hd]');
 if(hd){var f=function(){hd.classList.toggle('scr',scrollY>40)};f();addEventListener('scroll',f,{passive:true})}
 // Hinweis schließen
 var nx=document.querySelector('.hlp-note button');if(nx)nx.addEventListener('click',function(){document.body.classList.add('note-x')});
 // Formulare (Demo)
 document.querySelectorAll('form.fm').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();f.classList.add('sent')})});
 // Slider
 document.querySelectorAll('[data-slider]').forEach(function(s){
  var sl=s.querySelectorAll('[data-slide]'),dots=s.querySelectorAll('[data-dot]'),i=0,t;
  function go(n){sl[i].classList.remove('on');dots[i]&&dots[i].classList.remove('on');i=(n+sl.length)%sl.length;sl[i].classList.add('on');dots[i]&&dots[i].classList.add('on')}
  function auto(){clearInterval(t);t=setInterval(function(){go(i+1)},+(s.dataset.slider||6500))}
  dots.forEach(function(d,k){d.addEventListener('click',function(){go(k);auto()})});
  s.querySelectorAll('[data-prev]').forEach(function(b){b.addEventListener('click',function(){go(i-1);auto()})});
  s.querySelectorAll('[data-next]').forEach(function(b){b.addEventListener('click',function(){go(i+1);auto()})});
  if(sl.length>1)auto();
 });
 // Akkordeon
 document.querySelectorAll('[data-acc]').forEach(function(b){b.addEventListener('click',function(){b.parentElement.classList.toggle('open')})});
 // KI-Assistent
 var B=window.BOT;if(!B)return;
 var R='<svg viewBox="0 0 48 48" fill="none"><rect x="9" y="14" width="30" height="24" rx="9" fill="#fff"/><circle cx="19" cy="26" r="3.6" fill="currentColor"/><circle cx="29" cy="26" r="3.6" fill="currentColor"/><path d="M19 33c3 2 7 2 10 0" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M24 14V8" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><circle cx="24" cy="6.5" r="2.6" fill="#fff"/><rect x="4" y="22" width="4" height="9" rx="2" fill="#fff"/><rect x="40" y="22" width="4" height="9" rx="2" fill="#fff"/></svg>';
 var w=document.createElement('div');w.className='bot hide-t';
 w.innerHTML='<div class="bot-t"><button class="bx" aria-label="Schließen">×</button><small>'+B.name+' · '+B.tag+'</small>'+B.hello+'<div class="bb"><button data-y>Ja, gern</button><button data-q>Ich habe eine Frage</button></div></div>'+
 '<div class="bot-p" role="dialog" aria-label="Chat mit '+B.name+'"><div class="bot-h"><span style="width:34px;height:34px;display:grid;place-items:center;border-radius:50%;background:rgba(255,255,255,.18)">'+R.replace('viewBox','width="26" height="26" viewBox')+'</span><div><b>'+B.name+'</b><span>'+B.tag+' · online</span></div><button aria-label="Schließen">×</button></div><div class="bot-m"></div><div class="bot-c"></div></div>'+
 '<button class="bot-b" aria-label="Chat mit '+B.name+' öffnen">'+R+'</button>';
 document.body.appendChild(w);
 var m=w.querySelector('.bot-m'),c=w.querySelector('.bot-c');
 function say(t,u){var d=document.createElement('div');if(u)d.className='u';d.innerHTML=t;m.appendChild(d);m.scrollTop=1e5}
 function chips(){c.innerHTML='';B.qa.forEach(function(x){var b=document.createElement('button');b.textContent=x[0];b.onclick=function(){say(x[0],1);setTimeout(function(){say(x[1])},450)};c.appendChild(b)})}
 function open(){w.classList.add('open');if(!m.children.length){say(B.hi);chips()}}
 setTimeout(function(){w.classList.remove('hide-t')},2600);
 w.querySelector('.bx').onclick=function(){w.classList.add('hide-t')};
 w.querySelector('.bot-b').onclick=function(){w.classList.contains('open')?w.classList.remove('open'):open()};
 w.querySelector('.bot-h button').onclick=function(){w.classList.remove('open')};
 w.querySelector('[data-q]').onclick=open;
 w.querySelector('[data-y]').onclick=function(){w.classList.add('hide-t');var s=B.tour||[];var k=0;(function nx(){if(k>=s.length)return;var el=document.querySelector(s[k][0]);if(el){el.scrollIntoView({behavior:'smooth',block:'start'})}k++;setTimeout(nx,3200)})()};
})();
// Inhaber-Anfrage (Formular #hlp-anfrage) → kontakt.php (Mail an info@) + Pabbly „HLP Business – Google Leads“ (SMS, Tabelle) + Newsletter nur per Double-Opt-in (Brevo-Liste 23 Website)
(function(){
 var f=document.querySelector('#hlp-anfrage form');if(!f)return;var msg=f.querySelector('.msg');
 var HOOK='https://connect.pabbly.com/webhook-listener/webhook/IjU3NjAwNTZmMDYzZTA0MzE1MjY4NTUzNyI_3D_pc/IjU3NjcwNTZiMDYzNTA0MzM1MjZiNTUzMDUxMzUi_pc';
 var DOI='https://connect.pabbly.com/webhook-listener/webhook/IjU3NjAwNTZmMDYzZTA0MzE1MjY4NTUzNyI_3D_pc/IjU3NjcwNTY4MDYzZjA0MzI1MjY0NTUzMTUxM2Ii_pc';
 f.addEventListener('submit',function(e){e.preventDefault();if(f.website.value)return;
  if(!f.checkValidity()){f.reportValidity();return}
  var b=f.querySelector('button[type=submit]');b.disabled=true;b.textContent='Wird gesendet …';
  var fd=new FormData(f);fd.delete('ds');var th=fd.getAll('thema').join(', ')||'-';fd.delete('thema');fd.set('themen',th);var seite=location.href.split('#')[0];
  fd.set('quelle','Brief Website-Entwurf ('+((window.HLP_E||{}).runde||'')+')');
  fd.set('ziel','Website-Entwurf per Brief | Firma: '+fd.get('firma')+' | Tätigkeit: '+fd.get('branche')+' | Erreichbar: '+fd.get('zeit_wunsch')+' | Trifft zu: '+th+' | Herausforderung: '+(fd.get('wunsch')||'-')+' | Entwurf: '+seite);
  fetch('https://formular.highlevel-performance.de/kontakt.php',{method:'POST',body:fd}).then(function(r){return r.json()}).then(function(j){if(!j||!j.ok)throw 0;
   try{var o=new URLSearchParams();fd.forEach(function(v,k){if(typeof v==='string'&&k!=='website')o.append(k,v)});var nl=o.get('newsletter')==='ja';
    var iso=new Date().toLocaleDateString('sv-SE',{timeZone:'Europe/Berlin'});
    if(nl){var em=o.get('email'),vn=(o.get('name')||'').trim().split(' ')[0];
     var tk=btoa(unescape(encodeURIComponent(JSON.stringify({e:em,n:vn,l:'website',d:iso})))).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
     var d=new URLSearchParams();d.append('email',em);d.append('vorname',vn);d.append('liste','website');d.append('list_id','23');d.append('datum',iso);d.append('token',tk);
     d.append('betreff','Bitte bestätigen Sie Ihre Anmeldung');d.append('headline','Fast geschafft'+(vn?', '+vn:'')+'!');d.append('text','Bitte bestätigen Sie mit einem Klick Ihre Anmeldung zum Newsletter von High Level Performance. Damit sind Ihre 15 % auf Ihre nächste Leistung bei uns gesichert, und Sie bekommen regelmäßig die wichtigsten Neuigkeiten rund um Websites, Google und mehr Anfragen.');
     d.append('button','Anmeldung bestätigen');d.append('hinweis','Sie haben sich nicht angemeldet? Dann ignorieren Sie diese E-Mail einfach. Ohne Bestätigung tragen wir Sie nicht ein.');d.append('bild','https://www.highlevel-performance.de/assets/mail/img/b01.jpg');
     fetch(DOI,{method:'POST',mode:'no-cors',body:d,keepalive:true});o.set('newsletter','doi')}else o.set('newsletter','nein');
    o.set('formular','brief-entwurf');o.set('seite',seite);o.set('zeit',new Date().toLocaleString('de-DE',{timeZone:'Europe/Berlin'}));o.set('datum',iso);
    fetch(HOOK,{method:'POST',mode:'no-cors',body:o,keepalive:true})}catch(_){}
   f.innerHTML='<div class="ok w2"><b>Danke, Ihre Anfrage ist da.</b><p>Unser Hotline-Service ruft Sie innerhalb von 24 Stunden an ('+fd.get('zeit_wunsch')+').'+(fd.get('newsletter')==='ja'?' Damit Ihre 15 % Rabatt gelten, bitte noch kurz den Link in unserer Bestätigungsmail anklicken.':'')+'</p></div>';
  }).catch(function(){b.disabled=false;b.textContent='Rückruf anfordern';msg.hidden=false;msg.innerHTML='Das hat leider nicht geklappt. Rufen Sie uns direkt an: <a href="tel:+4917663213512">+49 176 63213512</a>.'});
 });
})();
;(function(){var v=document.querySelectorAll('video[data-auto]');if(!v.length)return;
 var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
 var io=new IntersectionObserver(function(es){es.forEach(function(e){var x=e.target;if(e.isIntersecting){if(x.preload!=='auto'){x.preload='auto'}if(!rm)x.play().catch(function(){})}else{x.pause()}})},{threshold:.35});
 v.forEach(function(x){io.observe(x)});
 document.querySelectorAll('[data-snd]').forEach(function(b){b.addEventListener('click',function(){var s=b.closest('section'),x=s.querySelector('video');x.muted=false;x.loop=false;x.currentTime=0;x.controls=true;x.play();s.classList.add('on')})});
})();
