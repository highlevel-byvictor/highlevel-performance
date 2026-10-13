/* High Level Performance – DE/EN-Umschalter
   Deutsch ist der Originaltext im HTML. Englisch kommt aus assets/i18n/en.json
   (Schlüssel = deutscher Text bzw. inneres HTML eines Textblocks, Wert = englische Fassung). */
(function(){
  var KEY = 'hlp_lang', DICT_URL = 'assets/i18n/en.json?v=20261014';
  var INLINE = {B:1,STRONG:1,I:1,EM:1,BR:1,SPAN:1,A:1,SMALL:1,SUP:1,SUB:1,U:1,MARK:1,S:1,ABBR:1,TIME:1,WBR:1};
  var SKIP = {SCRIPT:1,STYLE:1,SVG:1,CANVAS:1,TEXTAREA:1,CODE:1,NOSCRIPT:1,TEMPLATE:1,IFRAME:1,VIDEO:1,AUDIO:1,SELECT:1};
  var ATTRS = ['alt','placeholder','aria-label','title'];
  var HAS_LETTER = /[A-Za-zÄÖÜäöüß]/;
  var dict = null, lang = 'de', applying = false;
  var origHTML = new WeakMap(), origText = new WeakMap(), origAttr = new WeakMap();

  function norm(s){ return String(s).replace(/\s+/g,' ').trim(); }
  function skipEl(el){ return SKIP[el.tagName] || (el.closest && el.closest('#lg-impressum,#lg-datenschutz,[data-i18n-skip]')); }
  function inlineOnly(el){
    var all = el.getElementsByTagName('*');
    for (var i=0;i<all.length;i++){ if(!INLINE[all[i].tagName]) return false; }
    return true;
  }
  /* Elemente, die von anderen Skripten angesprochen werden (Zähler, Countdown …), nie per innerHTML ersetzen */
  var GUARD = '[id],.cnt,.ak-cd,.ak-spots,.rel-count,.ak-bar,.nl-msg,.spot-play,.rel-btn,.refs-btn,[data-cd],[data-to],[data-go],[data-intro],[data-intro-hide],[data-upload],[data-spot],[data-view]';
  function guarded(el){ return el.matches('.cnt,.ak-cd,.ak-spots,.rel-count,.ak-bar,[data-cd],[data-to]') || !!el.querySelector(GUARD); }
  function units(root, out){
    out = out || [];
    if (root.nodeType !== 1 || skipEl(root)) return out;
    if (root !== document.body && inlineOnly(root) && !guarded(root) && HAS_LETTER.test(root.textContent)) { out.push({el:root}); return out; }
    for (var n=root.firstChild; n; n=n.nextSibling){
      if (n.nodeType === 3){ if (HAS_LETTER.test(n.nodeValue)) out.push({text:n}); }
      else if (n.nodeType === 1) units(n, out);
    }
    return out;
  }
  function attrEls(root){
    var res = [];
    var sel = ATTRS.map(function(a){return '['+a+']';}).join(',');
    var list = root.querySelectorAll ? root.querySelectorAll(sel) : [];
    for (var i=0;i<list.length;i++){ if(!(list[i].closest && list[i].closest('#lg-impressum,#lg-datenschutz,[data-i18n-skip]'))) res.push(list[i]); }
    if (root.matches && root.matches(sel)) res.push(root);
    return res;
  }

  /* Für den Build: alle Schlüssel einsammeln */
  function collect(){
    var keys = {}, us = units(document.body);
    us.forEach(function(u){ var k = u.el ? norm(u.el.innerHTML) : norm(u.text.nodeValue); if(k && HAS_LETTER.test(k)) keys[k]=1; });
    attrEls(document.body).forEach(function(el){ ATTRS.forEach(function(a){ var v = el.getAttribute(a); if(v && HAS_LETTER.test(v)) keys[norm(v)]=1; }); });
    keys[norm(document.title)] = 1;
    var md = document.querySelector('meta[name=description]'); if(md) keys[norm(md.content)] = 1;
    return Object.keys(keys);
  }

  var rev = null;
  function back(k){ if(!dict) return null; if(!rev){ rev = {}; for (var x in dict) rev[norm(dict[x])] = x; } return Object.prototype.hasOwnProperty.call(rev,k) ? rev[k] : null; }
  function tr(k){ return dict && Object.prototype.hasOwnProperty.call(dict,k) ? dict[k] : null; }
  function applyTo(root){
    if (!dict) return;
    applying = true;
    units(root).forEach(function(u){
      if (u.el){
        var el = u.el, cur = norm(el.innerHTML);
        if (lang === 'en'){
          if (!origHTML.has(el)) origHTML.set(el, el.innerHTML);
          var t = tr(norm(origHTML.get(el))); if (t != null && cur !== norm(t)) el.innerHTML = t;
        } else if (origHTML.has(el)) { el.innerHTML = origHTML.get(el); origHTML.delete(el); }
        else { var bk = back(cur); if (bk != null) el.innerHTML = bk; }
      } else {
        var n = u.text, v = n.nodeValue;
        if (lang === 'en'){
          if (!origText.has(n)) origText.set(n, v);
          var o = origText.get(n), t2 = tr(norm(o));
          if (t2 != null){ var nv = o.match(/^\s*/)[0] + t2 + o.match(/\s*$/)[0]; if (v !== nv) n.nodeValue = nv; }
        } else if (origText.has(n)) { n.nodeValue = origText.get(n); origText.delete(n); }
        else { var bk2 = back(norm(v)); if (bk2 != null) n.nodeValue = v.match(/^\s*/)[0] + bk2 + v.match(/\s*$/)[0]; }
      }
    });
    attrEls(root).forEach(function(el){
      var store = origAttr.get(el) || {};
      ATTRS.forEach(function(a){
        if (!el.hasAttribute(a)) return;
        if (lang === 'en'){
          if (!(a in store)) store[a] = el.getAttribute(a);
          var t = tr(norm(store[a])); if (t != null) el.setAttribute(a, t);
        } else if (a in store) { el.setAttribute(a, store[a]); }
      });
      if (lang === 'en') origAttr.set(el, store); else origAttr.delete(el);
    });
    if (mo) mo.takeRecords();
    applying = false;
  }
  var mo = null;
  var origTitle = document.title, md0 = document.querySelector('meta[name=description]'), origDesc = md0 ? md0.content : '';
  function applyAll(){
    applyTo(document.body);
    document.documentElement.lang = lang;
    if (lang === 'en'){ var t = tr(norm(origTitle)); if (t) document.title = t; if (md0){ var d = tr(norm(origDesc)); if (d) md0.content = d; } }
    else { document.title = origTitle; if (md0) md0.content = origDesc; }
    var btns = document.querySelectorAll('[data-lang]');
    for (var i=0;i<btns.length;i++){ var on = btns[i].getAttribute('data-lang') === lang; btns[i].classList.toggle('on', on); btns[i].setAttribute('aria-pressed', on ? 'true' : 'false'); }
  }
  function loadDict(cb){
    if (dict) return cb();
    fetch(DICT_URL).then(function(r){ return r.json(); }).then(function(d){ dict = d; cb(); }).catch(function(){ dict = {}; cb(); });
  }
  function setLang(l, save){
    lang = l === 'en' ? 'en' : 'de';
    if (save) { try { localStorage.setItem(KEY, lang); } catch(e){} }
    if (lang === 'en') loadDict(applyAll); else applyAll();
  }

  /* Später eingefügte Inhalte (Slider, Meldungen) ebenfalls übersetzen */
  mo = new MutationObserver(function(muts){
    if (applying || lang !== 'en' || !dict) return;
    muts.forEach(function(m){
      if (m.type === 'childList') m.addedNodes.forEach(function(n){ if (n.nodeType === 1) applyTo(n); else if (n.nodeType === 3 && n.parentNode && n.parentNode.nodeType === 1) applyTo(n.parentNode); });
      else if (m.type === 'characterData' && m.target.parentNode) applyTo(m.target.parentNode);
    });
  });

  document.addEventListener('click', function(e){
    var b = e.target.closest && e.target.closest('[data-lang]'); if (!b) return;
    e.preventDefault(); setLang(b.getAttribute('data-lang'), true);
  });

  window.HLP_I18N = { collect: collect, setLang: setLang, get lang(){ return lang; } };

  function init(){
    mo.observe(document.body, { childList: true, subtree: true, characterData: true });
    var q = (location.search.match(/[?&]lang=(de|en)/) || [])[1], s = null;
    try { s = localStorage.getItem(KEY); } catch(e){}
    var l = q || s || 'de';
    if (l === 'en') setLang('en', !!q); else applyAll();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
