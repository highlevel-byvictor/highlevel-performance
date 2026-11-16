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
 // Fahrschul-Lotse (Runde 14): Führerschein-Check, Tour mit Spotlight, freie Fragen
 var B=window.BOT;if(!B)return;
 var R='<svg class="rb" viewBox="0 0 64 64" fill="none"><defs><linearGradient id="rbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#fff" stop-opacity=".55"/></linearGradient><linearGradient id="rbv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#1c2740"/></linearGradient></defs><g class="fl"><line x1="32" y1="12" x2="32" y2="5" stroke="url(#rbg)" stroke-width="2.4" stroke-linecap="round"/><circle class="ant" cx="32" cy="4.5" r="3" fill="var(--bot-glow,#7ef9ff)"/><rect x="11" y="12" width="42" height="34" rx="15" fill="url(#rbg)"/><rect x="16" y="18" width="32" height="20" rx="10" fill="url(#rbv)"/><ellipse class="eye" cx="25.5" cy="28" rx="3.6" ry="4.4" fill="var(--bot-glow,#7ef9ff)"/><ellipse class="eye" cx="38.5" cy="28" rx="3.6" ry="4.4" fill="var(--bot-glow,#7ef9ff)"/><path d="M27 34.2c3 1.8 7 1.8 10 0" stroke="var(--bot-glow,#7ef9ff)" stroke-width="1.6" stroke-linecap="round" opacity=".8"/><rect x="5" y="24" width="5" height="12" rx="2.5" fill="url(#rbg)"/><rect x="54" y="24" width="5" height="12" rx="2.5" fill="url(#rbg)"/><path d="M21 50h22a5 5 0 015 5v3H16v-3a5 5 0 015-5z" fill="url(#rbg)" opacity=".85"/></g></svg>';
 var w=document.createElement('div');w.className='lot bot hide-t';
 w.innerHTML='<div class="lot-t"><button class="x" aria-label="Schließen">×</button><small>'+B.name+' · '+B.tag+'</small><div class="tt">'+B.hello+'</div><div class="bb"><button data-k>'+(B.btnCheck||'Welcher Führerschein passt? · 30 Sek.')+'</button><button data-tour>Kurz durch die Seite</button><button data-q>Ich habe eine Frage</button></div></div>'+
 '<div class="lot-p" role="dialog" aria-label="Chat mit '+B.name+'"><div class="lot-h"><span class="face">'+R+'</span><div><b>'+B.name+'</b><span>'+B.tag+' · online</span></div><button aria-label="Schließen">×</button></div><div class="lot-steps"><i></i><i></i><i></i><i></i></div><div class="lot-m"></div><div class="lot-c"></div><form class="lot-f"><input placeholder="Frag mich etwas …" aria-label="Frage"><button aria-label="Senden">➤</button></form></div>'+
 '<button class="lot-b" aria-label="Chat mit '+B.name+' öffnen"><span class="dock">'+R+'</span><span class="lb"><b>'+B.name+'</b><small>'+B.tag+'</small></span></button>';
 document.body.appendChild(w);
 var m=w.querySelector('.lot-m'),c=w.querySelector('.lot-c'),bars=w.querySelectorAll('.lot-steps i'),A={},du=B.du!==false;
 function say(t,u){var d=document.createElement('div');d.className='msg'+(u?' u':'');d.innerHTML=t;m.appendChild(d);m.scrollTop=1e5}
 function bot(t,cb){var d=document.createElement('div');d.className='typing';d.innerHTML='<i></i><i></i><i></i>';m.appendChild(d);m.scrollTop=1e5;setTimeout(function(){d.remove();say(t);cb&&cb()},520+Math.min(800,t.length*5))}
 function chips(l){c.innerHTML='';l.forEach(function(x){var b=document.createElement('button');b.type='button';b.textContent=x[0];b.onclick=function(){say(x[0],1);c.innerHTML='';x[1]()};c.appendChild(b)})}
 function step(n){bars.forEach(function(b,i){b.classList.toggle('on',i<n)})}
 var has=function(k){return (B.cls||[]).indexOf(k)>=0};
 var VEH=[['Auto','auto',has('B')],['Motorrad','moto',has('A')||has('A2')||has('A1')],['Roller / Moped','roller',has('AM')||has('Mofa')||has('B196')],['Anhänger','anh',has('BE')||has('B96')],['Lkw / Bus','lkw',has('C')||has('CE')||has('D')],['Traktor','trak',has('L')||has('T')]].filter(function(v){return v[2]});
 function q1(pre){step(1);if(pre){A.v=pre;return q2()}bot(du?'Was möchtest du fahren?':'Was möchten Sie fahren?',function(){chips(VEH.map(function(v){return [v[0],function(){A.v=v[1];q2()}]}))})}
 function q2(){step(2);bot(du?'Wie alt bist du?':'Wie alt sind Sie?',function(){chips([['unter 16',function(){A.a=15;q3()}],['16',function(){A.a=16;q3()}],['17',function(){A.a=17;q3()}],['18 – 20',function(){A.a=19;q3()}],['21 – 23',function(){A.a=22;q3()}],['24 oder älter',function(){A.a=30;q3()}]])})}
 function q3(){step(3);bot(du?'Und was ist dir am wichtigsten?':'Und was ist Ihnen am wichtigsten?',function(){chips([['Schnell fertig werden',function(){A.z='schnell';res()}],['Ruhig und ohne Druck lernen',function(){A.z='ruhe';res()}],['Termine neben Schule oder Job',function(){A.z='flex';res()}],['Angst vor der ersten Fahrstunde',function(){A.z='angst';res()}]])})}
 function rec(){var a=A.a,v=A.v,r;
  if(v=='auto'){if(a<16)r=['B · BF17','Mit 16½ '+(du?'kannst du':'können Sie')+' anfangen und mit 17 begleitet fahren.'];else if(a<18)r=['B · BF17','Begleitetes Fahren ab 17: Prüfung mit 17, allein fahren ab 18.'];else r=has('B197')?['B197','Klasse B mit Schlüsselzahl 197: Prüfung auf Automatik, trotzdem Schaltwagen fahren.']:['B','Der klassische Autoführerschein.']}
  else if(v=='moto'){if(a<16)r=['AM','Mopeds bis 45 km/h, ab 15 Jahren.'];else if(a<18)r=['A1','Leichtkrafträder bis 125 ccm, ab 16.'];else if(a<24)r=['A2','Motorräder bis 35 kW, ab 18.'];else r=['A','Unbeschränkt Motorrad fahren, direkt ab 24.']}
  else if(v=='roller'){r=(a>=25&&has('B196'))?['B196','Mit Autoführerschein auch 125er fahren, ohne Prüfung.']:(a<15&&has('Mofa')?['Mofa','Mofa bis 25 km/h.']:['AM','Roller und Mopeds bis 45 km/h, ab 15.'])}
  else if(v=='anh'){r=has('BE')?['BE','Für schwere Anhänger, Pferdeanhänger und Wohnwagen.']:['B96','Gespanne bis 4.250 kg.']}
  else if(v=='lkw'){r=a<21?['C · CE','Lkw ab 21, mit Berufskraftfahrer-Ausbildung auch früher.']:['C · CE','Lkw-Führerschein, auf Wunsch mit Berufskraftfahrer-Modulen.']}
  else r=['L · T','Traktor-Führerschein, je nach Klasse ab 16.'];return r}
 function res(){step(4);var r=rec(),u=(B.usp||{})[A.z]||'';
  bot('Danke! Das passt '+(du?'zu dir':'zu Ihnen')+':',function(){var d=document.createElement('div');d.className='card';d.innerHTML='<small>Empfehlung</small><b>Klasse '+r[0]+'</b><p>'+r[1]+'</p>'+(u?'<p class="u2">'+u+'</p>':'')+'<a href="#kontakt" data-fin>'+(B.finBtn||(du?'Platz sichern':'Termin sichern'))+'</a><em>Die genaue Klasse klären wir gern persönlich.</em>';m.appendChild(d);m.scrollTop=1e5;
   var f=document.querySelector('#kontakt form');if(f){var s=f.querySelector('select'),t=f.querySelector('textarea'),code=r[0].split(' ')[0];if(s){for(var i=0;i<s.options.length;i++){if(s.options[i].text.indexOf(code)>=0||s.options[i].text.indexOf(r[0])>=0){s.selectedIndex=i;break}}}
    if(t)t.value='Führerschein-Check: '+({auto:'Auto',moto:'Motorrad',roller:'Roller / Moped',anh:'Anhänger',lkw:'Lkw / Bus',trak:'Traktor'})[A.v]+', '+(A.a<16?'unter 16':A.a<18?A.a:A.a<21?'18–20':A.a<24?'21–23':'24+')+' Jahre, Empfehlung Klasse '+r[0]+'.';f.classList.add('pre')}
   d.querySelector('[data-fin]').onclick=function(){w.classList.remove('open');var k=document.getElementById('kontakt');if(k){k.classList.add('spot');setTimeout(function(){k.classList.remove('spot')},4200)}};
   chips([['Noch eine Frage',free],[du?'Lieber anrufen':'Lieber anrufen',function(){bot('Gern! '+(du?'Ruf':'Rufen Sie')+' an unter <a href="tel:'+B.tel_i+'"><b>'+B.tel+'</b></a>.')}],['Nochmal von vorn',function(){A={};q1()}]])})}
 function free(){bot((du?'Frag mich gern':'Fragen Sie mich gern')+', zum Beispiel nach '+(B.ex||'Kosten, Theorie oder Anmeldung')+'.')}
 var QA=(B.qa||[]).map(function(x){return [new RegExp(x[0],'i'),x[1]]});
 QA.push([/preis|kost|teuer|euro|€|geld/i,'Was der Führerschein kostet, hängt vor allem davon ab, wie viele Fahrstunden '+(du?'du':'Sie')+' braucht'+(du?'st':'en')+'. Im Beratungsgespräch '+(du?'bekommst du':'bekommen Sie')+' eine ehrliche Einschätzung.']);
 QA.push([/anmeld|start|beginn|wann/i,(du?'Melde dich':'Melden Sie sich')+' einfach über das Formular unten an, wir melden uns dann für den Start.']);
 w.querySelector('.lot-f').addEventListener('submit',function(e){e.preventDefault();var i=this.querySelector('input'),v=i.value.trim();if(!v)return;say(v.replace(/</g,'&lt;'),1);i.value='';var h=QA.find(function(q){return q[0].test(v)});bot(h?h[1]:'Gute Frage! Die beantwortet das Team am besten persönlich: <a href="tel:'+B.tel_i+'"><b>'+B.tel+'</b></a> oder über das <a href="#kontakt"><b>Formular</b></a>.')});
 var started=0;function open(mode,pre){endTour();w.classList.add('open');w.classList.add('hide-t');if(mode=='check'){m.innerHTML='';A={};bot(B.hi,function(){q1(pre)});started=1;return}if(!started){started=1;bot(B.hi,function(){chips([['Führerschein-Check starten',function(){q1()}],['Ich habe eine Frage',free]])})}}
 var T=B.tour||[],ti=-1,tt=w.querySelector('.tt'),bb=w.querySelector('.lot-t .bb');
 function endTour(){document.querySelectorAll('.spot').forEach(function(e){e.classList.remove('spot')});ti=-1}
 function tour(n){endTour();if(n>=T.length){tt.innerHTML=(du?'Das war’s! Bereit für deinen Führerschein?':'Das war’s! Bereit für Ihren Führerschein?');bb.innerHTML='<button data-k>Führerschein-Check</button><button data-x2>Schließen</button>';wire();return}ti=n;var el=document.querySelector(T[n][0]);if(el){el.scrollIntoView({behavior:'smooth',block:'start'});el.classList.add('spot')}tt.innerHTML='<b>'+(n+1)+' / '+T.length+'</b> · '+T[n][1];bb.innerHTML='<button data-nx>Weiter</button><button data-x2>Tour beenden</button>';w.classList.remove('hide-t');wire()}
 function wire(){var b;if(b=bb.querySelector('[data-nx]'))b.onclick=function(){tour(ti+1)};if(b=bb.querySelector('[data-x2]'))b.onclick=function(){endTour();w.classList.add('hide-t')};if(b=bb.querySelector('[data-k]'))b.onclick=function(){open('check')};if(b=bb.querySelector('[data-tour]'))b.onclick=function(){tour(0)};if(b=bb.querySelector('[data-q]'))b.onclick=function(){open()}}
 wire();w.querySelector('.x').onclick=function(){endTour();w.classList.add('hide-t')};
 setTimeout(function(){if(!w.classList.contains('open'))w.classList.remove('hide-t')},3200);
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
