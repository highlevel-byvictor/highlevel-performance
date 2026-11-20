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
  var x0=null;s.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});
  s.addEventListener('touchend',function(e){if(x0===null)return;var d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>40){go(i+(d<0?1:-1));auto()}x0=null});
  if(sl.length>1)auto();
 });
 // Akkordeon
 document.querySelectorAll('[data-acc]').forEach(function(b){b.addEventListener('click',function(){b.parentElement.classList.toggle('open')})});
 // Praxis-Lotse (Runde 21): Zahn-Check, Tour mit Spotlight, freie Fragen
 var B=window.BOT;if(!B)return;
 var R='<svg class="rb" viewBox="0 0 64 64" fill="none"><defs><linearGradient id="rbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#fff" stop-opacity=".55"/></linearGradient><linearGradient id="rbv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#1c2740"/></linearGradient></defs><g class="fl"><line x1="32" y1="12" x2="32" y2="5" stroke="url(#rbg)" stroke-width="2.4" stroke-linecap="round"/><circle class="ant" cx="32" cy="4.5" r="3" fill="var(--bot-glow,#7ef9ff)"/><rect x="11" y="12" width="42" height="34" rx="15" fill="url(#rbg)"/><rect x="16" y="18" width="32" height="20" rx="10" fill="url(#rbv)"/><ellipse class="eye" cx="25.5" cy="28" rx="3.6" ry="4.4" fill="var(--bot-glow,#7ef9ff)"/><ellipse class="eye" cx="38.5" cy="28" rx="3.6" ry="4.4" fill="var(--bot-glow,#7ef9ff)"/><path d="M27 34.2c3 1.8 7 1.8 10 0" stroke="var(--bot-glow,#7ef9ff)" stroke-width="1.6" stroke-linecap="round" opacity=".8"/><rect x="5" y="24" width="5" height="12" rx="2.5" fill="url(#rbg)"/><rect x="54" y="24" width="5" height="12" rx="2.5" fill="url(#rbg)"/><path d="M21 50h22a5 5 0 015 5v3H16v-3a5 5 0 015-5z" fill="url(#rbg)" opacity=".85"/></g></svg>';
 var w=document.createElement('div');w.className='lot bot hide-t';
 w.innerHTML='<div class="lot-t"><button class="x" aria-label="Schließen">×</button><small>'+B.name+' · '+B.tag+'</small><div class="tt">'+B.hello+'</div><div class="bb"><button data-k>'+(B.btnCheck||'Was brauche ich? · Zahn-Check in 30 Sek.')+'</button><button data-tour>Kurz durch die Seite</button><button data-q>Ich habe eine Frage</button></div></div>'+
 '<div class="lot-p" role="dialog" aria-label="Chat mit '+B.name+'"><div class="lot-h"><span class="face">'+R+'</span><div><b>'+B.name+'</b><span>'+B.tag+' · online</span></div><button aria-label="Schließen">×</button></div><div class="lot-steps"><i></i><i></i><i></i><i></i></div><div class="lot-m"></div><div class="lot-c"></div><form class="lot-f"><input placeholder="Ihre Frage …" aria-label="Frage"><button aria-label="Senden">➤</button></form></div>'+
 (B.say?'<button class="lot-s off" type="button">'+B.say+'</button>':'')+'<button class="lot-b" aria-label="Chat mit '+B.name+' öffnen"><span class="dock">'+R+'</span><span class="lb"><b>'+B.name+'</b><small>'+B.tag+'</small></span></button>';
 document.body.appendChild(w);
 var m=w.querySelector('.lot-m'),c=w.querySelector('.lot-c'),bars=w.querySelectorAll('.lot-steps i'),A={},du=B.du!==false;
 function say(t,u){var d=document.createElement('div');d.className='msg'+(u?' u':'');d.innerHTML=t;m.appendChild(d);m.scrollTop=1e5}
 function bot(t,cb){var d=document.createElement('div');d.className='typing';d.innerHTML='<i></i><i></i><i></i>';m.appendChild(d);m.scrollTop=1e5;setTimeout(function(){d.remove();say(t);cb&&cb()},520+Math.min(800,t.length*5))}
 function chips(l){c.innerHTML='';l.forEach(function(x){var b=document.createElement('button');b.type='button';b.textContent=x[0];b.onclick=function(){say(x[0],1);c.innerHTML='';x[1]()};c.appendChild(b)})}
 function step(n){bars.forEach(function(b,i){b.classList.toggle('on',i<n)})}

 var CATS=B.cats||[];
 function q1(pre){step(1);if(pre){A.v=pre;return A.v=='akut'?akut():q2()}bot('Worum geht es bei Ihnen?',function(){chips(CATS.map(function(v){return [v[0],function(){A.v=v[1];A.vl=v[0];v[1]=='akut'?akut():q2()}]}))})}
 function akut(){step(4);bot('Bei Schmerzen bitte nicht warten. Rufen Sie am besten gleich in der Praxis an: <a href="tel:'+B.tel_i+'"><b>'+B.tel+'</b></a>. '+(B.notfall||''),function(){chips([['Trotzdem Termin anfragen',function(){A.v='akut';fill(['Schmerzen','']);goK()}],['Nochmal von vorn',function(){A={};q1()}]])})}
 function q2(){step(2);bot('Wann waren Sie zuletzt beim Zahnarzt?',function(){chips([['In den letzten 12 Monaten',function(){A.a='unter 1 Jahr';q3()}],['Vor 1 bis 2 Jahren',function(){A.a='1–2 Jahre';q3()}],['Länger her',function(){A.a='länger her';q3()}],['Ich bin neu in der Gegend',function(){A.a='neu hier';q3()}]])})}
 function q3(){step(3);bot('Und was ist Ihnen besonders wichtig?',function(){chips([['Dass man sich Zeit für mich nimmt',function(){A.z='zeit';res()}],['Eine schonende Behandlung',function(){A.z='sanft';res()}],['Schnell einen Termin bekommen',function(){A.z='schnell';res()}],['Alles verständlich erklärt bekommen',function(){A.z='klar';res()}]])})}
 function fill(r){var f=document.querySelector('#kontakt form');if(!f)return;var s=f.querySelector('select'),t=f.querySelector('textarea');if(s){for(var i=0;i<s.options.length;i++){if(s.options[i].text.indexOf(r[0])>=0){s.selectedIndex=i;break}}}
  if(t)t.value='Zahn-Check: '+(A.vl||r[0])+(A.a?', letzter Zahnarztbesuch: '+A.a:'')+'.';f.classList.add('pre')}
 function goK(){w.classList.remove('open');var k=document.getElementById('kontakt');if(k){k.scrollIntoView({behavior:'smooth'});k.classList.add('spot');setTimeout(function(){k.classList.remove('spot')},4200)}}
 function res(){step(4);var r=(B.rec||{})[A.v]||['Kontrolltermin','Am besten schauen wir uns alles in Ruhe an.'],u=(B.usp||{})[A.z]||'';
  bot('Danke! Dazu passt in der Praxis:',function(){var d=document.createElement('div');d.className='card';d.innerHTML='<small>Passt zu Ihrem Anliegen</small><b>'+r[0]+'</b><p>'+r[1]+'</p>'+(A.a=='länger her'?'<p class="u2">Wenn der letzte Besuch länger her ist, startet man am besten mit einem Kontrolltermin.</p>':'')+(u?'<p class="u2">'+u+'</p>':'')+'<a href="#kontakt" data-fin>'+(B.finBtn||'Termin anfragen')+'</a><em>Das ersetzt keine Untersuchung. Was wirklich nötig ist, klärt die Praxis mit Ihnen.</em>';m.appendChild(d);m.scrollTop=1e5;fill(r);
   d.querySelector('[data-fin]').onclick=function(){goK()};
   chips([['Noch eine Frage',free],['Lieber anrufen',function(){bot('Gern! Rufen Sie an unter <a href="tel:'+B.tel_i+'"><b>'+B.tel+'</b></a>.')}],['Nochmal von vorn',function(){A={};q1()}]])})}
 function free(){bot((du?'Frag mich gern':'Fragen Sie mich gern')+', zum Beispiel nach '+(B.ex||'Sprechzeiten, Leistungen oder Terminen')+'.')}
 var QA=(B.qa||[]).map(function(x){return [new RegExp(x[0],'i'),x[1]]});
 QA.push([/preis|kost|teuer|euro|€|zuzahl|kasse/i,'Was eine Behandlung kostet und was die Kasse übernimmt, hängt von Ihrem Befund ab. Die Praxis bespricht das vorher offen mit Ihnen.']);
 QA.push([/termin|anmeld|wann|frei/i,'Einen Termin bekommen Sie am schnellsten per Telefon: <a href="tel:'+B.tel_i+'"><b>'+B.tel+'</b></a>. Oder Sie nutzen das <a href="#kontakt"><b>Formular</b></a>, die Praxis meldet sich.']);
 QA.push([/schmerz|notfall|notdienst|akut/i,'Bei Schmerzen bitte direkt anrufen: <a href="tel:'+B.tel_i+'"><b>'+B.tel+'</b></a>. '+(B.notfall||'')]);
 w.querySelector('.lot-f').addEventListener('submit',function(e){e.preventDefault();var i=this.querySelector('input'),v=i.value.trim();if(!v)return;say(v.replace(/</g,'&lt;'),1);i.value='';var h=QA.find(function(q){return q[0].test(v)});bot(h?h[1]:'Gute Frage! Die beantwortet das Team am besten persönlich: <a href="tel:'+B.tel_i+'"><b>'+B.tel+'</b></a> oder über das <a href="#kontakt"><b>Formular</b></a>.')});
 var started=0;function open(mode,pre){endTour();w.classList.add('open');w.classList.add('hide-t');if(mode=='check'){m.innerHTML='';A={};bot(B.hi,function(){q1(pre)});started=1;return}if(!started){started=1;bot(B.hi,function(){chips([['Zahn-Check starten',function(){q1()}],['Ich habe eine Frage',free]])})}}
 var T=B.tour||[],ti=-1,tt=w.querySelector('.tt'),bb=w.querySelector('.lot-t .bb');
 function endTour(){document.querySelectorAll('.spot').forEach(function(e){e.classList.remove('spot')});ti=-1}
 function tour(n){endTour();if(n>=T.length){tt.innerHTML='Das war der Rundgang. Soll ich Ihnen helfen, das Richtige zu finden?';bb.innerHTML='<button data-k>Zahn-Check starten</button><button data-x2>Schließen</button>';wire();return}ti=n;var el=document.querySelector(T[n][0]);if(el){el.scrollIntoView({behavior:'smooth',block:'start'});el.classList.add('spot')}tt.innerHTML='<b>'+(n+1)+' / '+T.length+'</b> · '+T[n][1];bb.innerHTML='<button data-nx>Weiter</button><button data-x2>Tour beenden</button>';w.classList.remove('hide-t');wire()}
 function wire(){var b;if(b=bb.querySelector('[data-nx]'))b.onclick=function(){tour(ti+1)};if(b=bb.querySelector('[data-x2]'))b.onclick=function(){endTour();w.classList.add('hide-t')};if(b=bb.querySelector('[data-k]'))b.onclick=function(){open('check')};if(b=bb.querySelector('[data-tour]'))b.onclick=function(){tour(0)};if(b=bb.querySelector('[data-q]'))b.onclick=function(){open()}}
 wire();w.querySelector('.x').onclick=function(){endTour();w.classList.add('hide-t')};
 if(innerWidth>820&&B.auto!==false)setTimeout(function(){if(!w.classList.contains('open'))w.classList.remove('hide-t')},3200);
 var sp=w.querySelector('.lot-s');if(sp){setTimeout(function(){sp.classList.remove('off')},1500);setTimeout(function(){sp.classList.add('off')},13000);sp.onclick=function(){sp.classList.add('off');w.classList.remove('hide-t')};addEventListener('scroll',function(){if(scrollY>innerHeight*1.2)sp.classList.add('off')},{passive:true})}
 w.querySelector('.lot-b').onclick=function(){w.classList.contains('open')?w.classList.remove('open'):open()};
 w.querySelector('.lot-h button').onclick=function(){w.classList.remove('open')};
 document.querySelectorAll('[data-check]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();open('check',b.dataset.check||null)})});
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
