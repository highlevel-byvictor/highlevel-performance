// Inhaber-Anfrage (Formular #hlp-anfrage) → kontakt.php (Mail an info@) + Pabbly „HLP Business – Google Leads“ (SMS, Tabelle) + Newsletter nur per Double-Opt-in (Brevo-Liste 23 Website)
(function(){
 var f=document.querySelector('#hlp-anfrage form');if(!f)return;var msg=f.querySelector('.msg');
 var HOOK='https://connect.pabbly.com/webhook-listener/webhook/IjU3NjAwNTZmMDYzZTA0MzE1MjY4NTUzNyI_3D_pc/IjU3NjcwNTY4MDYzZjA0MzY1MjY4NTUzMjUxMzEi_pc';
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
