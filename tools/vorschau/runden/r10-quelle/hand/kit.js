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
