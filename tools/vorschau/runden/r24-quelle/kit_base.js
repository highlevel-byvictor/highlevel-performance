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
