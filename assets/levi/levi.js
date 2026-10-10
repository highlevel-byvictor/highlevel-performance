/* Levi – KI-Assistent von High Level Performance
   Lädt ElevenLabs erst, wenn der Besucher selbst schreibt oder auf „Sprechen“ tippt. */
(function () {
  'use strict';
  var AGENT = 'agent_0901m4kksbrfetjvmrea2q2wgvne';
  var VOICES = { m: 'buUrS4YSeOZtlCKnzwkC', w: 'M39iqBUcu1jyiwM5PfSy' };
  // Stimme an/aus: auf highlevel-performance.de aus (nur Chat). Für Kunden mit Sprach-Budget auf true setzen.
  var VOICE = !!(window.LEVI_VOICE);
  var SDK = (document.currentScript && document.currentScript.src || '').replace(/levi\.js.*$/, 'elevenlabs-client.js');
  var TEL = '+49 15561 068899', MAIL = 'info@highlevel-performance.de';

  var store = {
    get: function (k) { try { return localStorage.getItem('levi_' + k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem('levi_' + k, v); } catch (e) {} },
    sget: function (k) { try { return sessionStorage.getItem('levi_' + k); } catch (e) { return null; } },
    sset: function (k, v) { try { sessionStorage.setItem('levi_' + k, v); } catch (e) {} }
  };

  var uid = 0;
  function bot() {
    var u = 'lv' + (++uid);
    return '<svg class="lv-bot" viewBox="0 0 120 140" aria-hidden="true">' +
      '<defs>' +
      '<radialGradient id="' + u + 'h" cx="35%" cy="28%" r="80%"><stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#E4EAF4"/><stop offset="1" stop-color="#9DA9BF"/></radialGradient>' +
      '<linearGradient id="' + u + 'v" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16213B"/><stop offset="1" stop-color="#03060E"/></linearGradient>' +
      '<radialGradient id="' + u + 'b" cx="38%" cy="25%" r="85%"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="#D9E0EC"/><stop offset="1" stop-color="#8E9AB1"/></radialGradient>' +
      '<filter id="' + u + 'g" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="2.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>' +
      '</defs>' +
      '<ellipse cx="60" cy="134" rx="26" ry="4.5" fill="#000" opacity=".22"/>' +
      '<g class="lv-float">' +
      // Körper
      '<ellipse cx="60" cy="110" rx="27" ry="20" fill="url(#' + u + 'b)"/>' +
      '<ellipse cx="60" cy="110" rx="27" ry="20" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width=".8"/>' +
      '<circle cx="60" cy="110" r="7" fill="url(#' + u + 'v)"/>' +
      '<circle cx="60" cy="110" r="4" style="fill:var(--lv-acc)" filter="url(#' + u + 'g)"/>' +
      // Arm (zeigt)
      '<g class="lv-arm"><rect x="83" y="100" width="20" height="9" rx="4.5" fill="url(#' + u + 'b)"/><circle cx="102" cy="104.5" r="5.2" fill="url(#' + u + 'h)"/></g>' +
      '<rect x="17" y="100" width="20" height="9" rx="4.5" fill="url(#' + u + 'b)" transform="rotate(20 27 104)"/>' +
      // Antenne
      '<line x1="60" y1="24" x2="60" y2="11" stroke="#AEB8CB" stroke-width="2.4" stroke-linecap="round"/>' +
      '<circle class="lv-tip" cx="60" cy="9" r="4.4" style="fill:var(--lv-acc)" filter="url(#' + u + 'g)"/>' +
      // Kopf
      '<rect x="15" y="22" width="90" height="70" rx="32" fill="url(#' + u + 'h)"/>' +
      '<rect x="15" y="22" width="90" height="70" rx="32" fill="none" stroke="#fff" stroke-opacity=".7" stroke-width=".8"/>' +
      '<rect x="8" y="48" width="10" height="20" rx="5" fill="#B8C3D6"/><rect x="102" y="48" width="10" height="20" rx="5" fill="#B8C3D6"/>' +
      '<rect x="10" y="54" width="4" height="8" rx="2" style="fill:var(--lv-acc)" opacity=".85"/><rect x="106" y="54" width="4" height="8" rx="2" style="fill:var(--lv-acc)" opacity=".85"/>' +
      // Visier
      '<rect x="25" y="38" width="70" height="40" rx="20" fill="url(#' + u + 'v)"/>' +
      '<path d="M33 44 Q60 36 87 44" stroke="#fff" stroke-opacity=".22" stroke-width="3" fill="none" stroke-linecap="round"/>' +
      // Augen
      '<rect class="lv-eye" x="38" y="49" width="12" height="15" rx="6" style="fill:var(--lv-acc)" filter="url(#' + u + 'g)"/>' +
      '<rect class="lv-eye r" x="70" y="49" width="12" height="15" rx="6" style="fill:var(--lv-acc)" filter="url(#' + u + 'g)"/>' +
      // Mund (Equalizer)
      '<g class="lv-mouth"><rect x="54" y="66" width="3" height="7" rx="1.5" style="fill:var(--lv-acc)"/><rect x="58.5" y="66" width="3" height="7" rx="1.5" style="fill:var(--lv-acc)"/><rect x="63" y="66" width="3" height="7" rx="1.5" style="fill:var(--lv-acc)"/></g>' +
      // Glanz
      '<ellipse cx="38" cy="31" rx="13" ry="5" fill="#fff" opacity=".75" transform="rotate(-14 38 31)"/>' +
      '</g></svg>';
  }

  var IC = {
    x: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    send: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l16-8-6 16-3-7-7-1z"/></svg>',
    mic: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>',
    reset: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>'
  };

  function area() { var b = document.body.classList; return b.contains('biz') ? 'business' : b.contains('art') ? 'artists' : 'start'; }

  var TXT = {
    start: {
      hi: 'Hey, schön dass du da bist! Ich bin Levi, der KI-Assistent von High Level Performance. Bist du Musiker oder hast du einen Betrieb? Ich zeig dir gern alles.',
      tease: 'Hey, schön dass du da bist! Soll ich dir die Seite zeigen?',
      voice: 'Hey, schön dass du da bist! Ich bin Levi, der KI-Assistent von High Level Performance. Was kann ich Gutes für dich tun?',
      chips: ['Was macht High Level Performance?', 'Ich bin Musiker', 'Ich habe einen Betrieb', 'Was kostet eine Website?']
    },
    business: {
      hi: 'Willkommen! Ich bin Levi, Ihr KI-Assistent. Ich beantworte Ihre Fragen und zeige Ihnen gern die Seite. Womit fangen wir an?',
      tease: 'Willkommen! Soll ich Ihnen in 30 Sekunden zeigen, wie wir Ihnen neue Kunden bringen?',
      voice: 'Willkommen bei High Level Performance! Ich bin Levi, Ihr KI-Assistent. Wie kann ich Ihnen helfen?',
      chips: ['Was macht High Level Performance?', 'Erklär mir eure Leistungen', 'Was kostet eine Website?', 'Was ist die Oktober-Aktion?']
    },
    artists: {
      hi: 'Yo, willkommen bei High Level! Ich bin Levi, dein KI-Assistent. Frag mich alles zu Studio, Website oder Release – ich zeig dir den Weg.',
      tease: 'Yo! Willst du sehen, wie wir aus deiner Musik eine Marke machen?',
      voice: 'Yo, willkommen bei High Level! Ich bin Levi, dein KI-Assistent. Was steht bei dir gerade an?',
      chips: ['Was macht ihr für Artists?', 'Zeig mir das Studio', 'Was kostet eine Artist-Website?', 'Wie reiche ich meine Musik ein?']
    }
  };

  /* ---------- DOM ---------- */
  var root = document.createElement('div');
  root.className = 'lv';
  root.innerHTML =
    '<div class="lv-tease" role="button" tabindex="0"><button class="x" type="button" aria-label="Hinweis schließen">×</button><b>Levi</b><span class="t"></span></div>' +
    '<button class="lv-launch" type="button" aria-label="Levi, KI-Assistent, öffnen">' + bot() + '</button>' +
    '<section class="lv-panel" role="dialog" aria-label="Levi – KI-Assistent" aria-hidden="true">' +
      '<header class="lv-head"><div class="lv-ava">' + bot() + '</div>' +
        '<div class="lv-ttl"><b>Levi <em class="lv-ki">KI-ASSISTENT</em></b><span><i></i><span class="st">Dein Level-Up-Experte</span></span></div>' +
        '<button class="lv-ic lv-reset" type="button" aria-label="Neues Gespräch" title="Neues Gespräch">' + IC.reset + '</button>' +
        '<button class="lv-ic lv-close" type="button" aria-label="Schließen">' + IC.x + '</button></header>' +
      '<div class="lv-peekbar"><p></p><button type="button">Chat öffnen</button></div>' +
      (VOICE ? '<div class="lv-bar"><span>Stimme</span><div class="lv-sex" role="group" aria-label="Stimme wählen"><button type="button" data-sex="m">Mann</button><button type="button" data-sex="w">Frau</button></div></div>' : '') +
      '<div class="lv-log" aria-live="polite"></div>' +
      '<div class="lv-chips"></div>' +
      '<div class="lv-voice"><div class="lv-wave"><i></i><i></i><i></i><i></i><i></i></div><span class="vs">Verbinde…</span><button type="button" class="lv-end">Beenden</button></div>' +
      '<form class="lv-form" autocomplete="off"><input class="lv-in" type="text" maxlength="500" placeholder="Frag Levi etwas…" aria-label="Nachricht an Levi">' +
        (VOICE ? '<button class="lv-mic" type="button" aria-label="Mit Levi sprechen" title="Mit Levi sprechen">' + IC.mic + '</button>' : '') +
        '<button class="lv-send" type="submit" aria-label="Senden">' + IC.send + '</button></form>' +
      '<p class="lv-legal">Levi ist eine KI und kann sich irren. Erst wenn du schreibst, wird dein Gespräch zur Beantwortung an unseren Dienstleister ElevenLabs übertragen. Bitte keine sensiblen Daten eingeben. <a href="#" data-legal="datenschutz">Datenschutz</a></p>' +
    '</section>';
  var guide = document.createElement('div');
  guide.className = 'lv-guide';
  guide.innerHTML = bot() + '<span class="lv-say">Hier!</span>';

  function $(s) { return root.querySelector(s); }
  var panel = $('.lv-panel'), log = $('.lv-log'), chips = $('.lv-chips'), input = $('.lv-in'), form = $('.lv-form'),
      tease = $('.lv-tease'), launch = $('.lv-launch'), st = $('.st'), vs = $('.vs'), peekP = $('.lv-peekbar p');
  var bots = function () { return root.querySelectorAll('.lv-bot'); };

  var conv = null, mode = null, connecting = null, chatted = false, waitTimer = null, typingEl = null, lastAi = '';
  var sex = store.get('sex') === 'w' ? 'w' : 'm';

  /* ---------- Darstellung ---------- */
  function scroll() { log.scrollTop = log.scrollHeight; }
  function add(text, who) {
    var d = document.createElement('div');
    d.className = 'lv-m ' + who;
    d.textContent = text;
    log.appendChild(d);
    if (who === 'ai') { lastAi = text; peekP.textContent = text; }
    scroll();
    return d;
  }
  function typing(on) {
    if (on && !typingEl) { typingEl = document.createElement('div'); typingEl.className = 'lv-typing'; typingEl.innerHTML = '<i></i><i></i><i></i>'; log.appendChild(typingEl); scroll(); }
    if (!on && typingEl) { typingEl.remove(); typingEl = null; }
  }
  function botState(cls, on) { bots().forEach(function (b) { b.classList.toggle(cls, !!on); }); }
  function renderChips() {
    chips.innerHTML = '';
    if (chatted) return;
    TXT[area()].chips.forEach(function (c) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'lv-chip'; b.textContent = c;
      b.addEventListener('click', function () { send(c); });
      chips.appendChild(b);
    });
  }
  function welcome() {
    log.innerHTML = ''; lastAi = '';
    add(TXT[area()].hi, 'ai');
    renderChips();
  }
  function setSex(s) {
    sex = s; store.set('sex', s);
    root.querySelectorAll('[data-sex]').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.sex === s ? 'true' : 'false'); });
  }

  /* ---------- Öffnen / Schließen ---------- */
  function open() {
    root.classList.add('open'); root.classList.remove('peek');
    panel.setAttribute('aria-hidden', 'false');
    tease.classList.remove('on'); store.sset('teased', '1');
    if (!log.children.length) welcome();
    botState('wave', true); setTimeout(function () { botState('wave', false); }, 1600);
    if (window.matchMedia('(min-width:761px)').matches) setTimeout(function () { input.focus(); }, 250);
  }
  function close() {
    root.classList.remove('open', 'peek');
    panel.setAttribute('aria-hidden', 'true');
    if (mode === 'voice') stop();
  }
  function peek() { if (window.matchMedia('(max-width:760px)').matches && root.classList.contains('open')) root.classList.add('peek'); }

  /* ---------- Seitenführung (Client-Tools) ---------- */
  function wait(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function goArea(v) {
    if (area() === v) return Promise.resolve(false);
    var real = document.querySelector('[data-go="' + v + '"]');
    if (real) real.click(); else location.hash = '#' + v;
    return wait(650).then(function () { return true; });
  }
  var guideT = null;
  function flyTo(el, say) {
    var r = el.getBoundingClientRect(), vw = innerWidth, vh = innerHeight;
    var top = Math.max(80, Math.min(vh - 170, r.top + 24));
    var left = vw > 760 ? Math.max(14, Math.min(vw - 520, r.left + 24)) : 14;
    var from = launch.getBoundingClientRect();
    guide.style.transition = 'none';
    guide.style.transform = 'translate(' + (from.left) + 'px,' + (from.top) + 'px)';
    guide.classList.remove('flip');
    guide.querySelector('.lv-say').textContent = say || 'Hier!';
    void guide.offsetWidth;
    guide.style.transition = '';
    guide.classList.add('on');
    guide.querySelector('.lv-bot').classList.add('point');
    guide.style.transform = 'translate(' + left + 'px,' + top + 'px)';
    clearTimeout(guideT);
    guideT = setTimeout(function () { guide.classList.remove('on'); guide.querySelector('.lv-bot').classList.remove('point'); }, 4200);
  }
  function highlight(el) { el.classList.remove('lv-hl'); void el.offsetWidth; el.classList.add('lv-hl'); setTimeout(function () { el.classList.remove('lv-hl'); }, 2700); }
  var NAMES = { 'b-aktion': 'Oktober-Aktion', 'b-spot': 'Werbespot', 'b-system': 'So geht’s', 'b-leistungen': 'Leistungen', 'b-pakete': 'Pakete', 'b-faq': 'FAQ', 'b-kontakt': 'Potenzialanalyse',
    'a-spot': 'Spot', 'a-studio': 'Studio', 'a-leistungen': 'Leistungen', 'a-victor': 'Victor', 'a-team': 'Team', 'a-kontakt': 'Musik einreichen' };
  var PAGES = { 'website-business': ['Website für Ihren Betrieb', 'website-business/'], 'website-artists': ['Website für Artists', 'website-artists/'] };

  var tools = {
    bereich_wechseln: function (p) {
      var z = p && p.ziel; if (!TXT[z]) return 'Unbekannter Bereich.';
      peek();
      return goArea(z).then(function () { window.scrollTo({ top: 0, behavior: 'smooth' }); return 'Bereich ' + z + ' wird jetzt angezeigt.'; });
    },
    zu_abschnitt: function (p) {
      var id = p && p.ziel; if (!id || !NAMES[id]) return 'Diesen Abschnitt gibt es nicht.';
      peek();
      return goArea(id.charAt(0) === 'b' ? 'business' : 'artists').then(function () {
        var el = document.getElementById(id); if (!el) return 'Abschnitt nicht gefunden.';
        var y = el.getBoundingClientRect().top + scrollY - 70;
        var y0 = scrollY;
        window.scrollTo({ top: y, behavior: 'smooth' });
        return wait(750).then(function () {
          if (Math.abs(scrollY - y0) < 2 && Math.abs(y - y0) > 40) window.scrollTo(0, y); highlight(el); flyTo(el, NAMES[id] + '!'); return 'Der Besucher sieht jetzt den Abschnitt ' + NAMES[id] + '.'; });
      });
    },
    seite_oeffnen: function (p) {
      var s = p && p.seite;
      if (s === 'impressum' || s === 'datenschutz') {
        var a = document.querySelector('[data-legal="' + s + '"]'); if (a) a.click();
        peek(); return 'Das Fenster ' + s + ' ist geöffnet.';
      }
      var pg = PAGES[s]; if (!pg) return 'Diese Seite gibt es nicht.';
      var c = document.createElement('a'); c.className = 'lv-card'; c.href = pg[1]; c.target = '_blank'; c.rel = 'noopener';
      c.textContent = pg[0] + ' öffnen →';
      log.appendChild(c); scroll();
      return 'Ein Button zur Seite „' + pg[0] + '“ wird im Chat angezeigt. Bitte den Besucher, ihn anzutippen.';
    },
    musik_einreichen: function () {
      return goArea('artists').then(function () {
        var a = document.querySelector('[data-upload]'); if (a) a.click();
        peek(); return 'Das Fenster „Musik einreichen“ ist geöffnet.';
      });
    }
  };

  /* ---------- Verbindung zu ElevenLabs ---------- */
  var sdkP = null;
  function sdk() {
    if (window.ElevenLabsClient) return Promise.resolve(window.ElevenLabsClient);
    if (!sdkP) sdkP = new Promise(function (ok, fail) {
      var s = document.createElement('script'); s.src = SDK; s.async = true;
      s.onload = function () { window.ElevenLabsClient ? ok(window.ElevenLabsClient) : fail(new Error('SDK')); };
      s.onerror = function () { sdkP = null; fail(new Error('SDK')); };
      document.head.appendChild(s);
    });
    return sdkP;
  }
  function fail() {
    typing(false); clearTimeout(waitTimer);
    add('Ich bin gerade nicht erreichbar, sorry! Ruf uns gern an (' + TEL + ') oder schreib an ' + MAIL + '. Wir melden uns schnell.', 'ai');
    setStatus('Dein Level-Up-Experte');
  }
  function setStatus(t) { st.textContent = t; }

  function start(kind) {
    if (conv && mode === kind) return Promise.resolve(conv);
    if (connecting && mode === kind) return connecting;
    var prev = conv; conv = null;
    var done = prev ? prev.endSession().catch(function () {}) : Promise.resolve();
    mode = kind;
    connecting = done.then(sdk).then(function (E) {
      var voice = kind === 'voice';
      var o = {
        agentId: AGENT,
        connectionType: 'websocket',
        dynamicVariables: { bereich: area() },
        clientTools: tools,
        overrides: voice
          ? { tts: { voiceId: VOICES[sex] }, agent: { firstMessage: chatted ? 'Da bin ich – sprich einfach los.' : TXT[area()].voice } }
          : { conversation: { textOnly: true }, agent: { firstMessage: '' } },
        onMessage: function (m) {
          var role = m.role || (m.source === 'ai' ? 'agent' : 'user');
          if (role === 'user') { if (voice && m.message) add(m.message, 'me'); return; }
          if (!m.message) return;
          if (!voice && !chatted) return;
          typing(false); clearTimeout(waitTimer);
          add(m.message, 'ai');
        },
        onModeChange: function (x) {
          var speaking = x && x.mode === 'speaking';
          root.classList.toggle('speaking', voice && speaking);
          botState('talk', voice && speaking); botState('listen', voice && !speaking);
          if (voice) vs.textContent = speaking ? 'Levi spricht…' : 'Levi hört zu…';
        },
        onDisconnect: function () {
          if (mode === kind) { conv = null; connecting = null; if (voice) voiceOff(); }
        },
        onError: function () {}
      };
      if (!voice) o.textOnly = true;
      return E.Conversation.startSession(o);
    }).then(function (c) {
      if (mode !== kind) { c.endSession(); return null; }
      conv = c; connecting = null; return c;
    }, function (e) {
      connecting = null; conv = null;
      if (kind === 'voice') { voiceOff(); add(e && e.name === 'NotAllowedError' ? 'Ich brauche kurz dein Mikrofon, damit wir reden können. Du kannst mir aber auch einfach schreiben!' : 'Sprechen klappt gerade nicht – schreib mir einfach!', 'ai'); }
      else fail();
      mode = null; return null;
    });
    return connecting;
  }

  function send(text) {
    text = (text || '').trim(); if (!text) return;
    if (!chatted) { chatted = true; chips.innerHTML = ''; }
    add(text, 'me'); input.value = '';
    typing(true); setStatus('Levi tippt…');
    clearTimeout(waitTimer); waitTimer = setTimeout(fail, 25000);
    var kind = mode === 'voice' ? 'voice' : 'text';
    start(kind).then(function (c) { if (c) { c.sendUserMessage(text); } });
  }
  // Statuszeile zurücksetzen, sobald eine Antwort kommt
  new MutationObserver(function () { if (!typingEl && mode !== 'voice') setStatus('Dein Level-Up-Experte'); }).observe(log, { childList: true });

  function voiceOn() {
    root.classList.add('voice'); vs.textContent = 'Verbinde…';
    botState('listen', true);
    start('voice').then(function (c) { if (!c) voiceOff(); });
  }
  function voiceOff() {
    root.classList.remove('voice', 'speaking'); botState('talk', false); botState('listen', false);
    if (mode === 'voice') mode = null;
  }
  function stop() {
    var c = conv; conv = null; connecting = null; mode = null; voiceOff();
    if (c) c.endSession().catch(function () {});
  }

  /* ---------- Events ---------- */
  launch.addEventListener('click', open);
  tease.addEventListener('click', function (e) { if (e.target.closest('.x')) { e.stopPropagation(); tease.classList.remove('on'); store.sset('teased', '1'); return; } open(); });
  $('.lv-close').addEventListener('click', close);
  $('.lv-peekbar button').addEventListener('click', function () { root.classList.remove('peek'); });
  $('.lv-reset').addEventListener('click', function () { stop(); chatted = false; typing(false); clearTimeout(waitTimer); welcome(); setStatus('Dein Level-Up-Experte'); });
  if (VOICE) $('.lv-mic').addEventListener('click', function () { if (mode === 'voice') stop(); else voiceOn(); });
  $('.lv-end').addEventListener('click', stop);
  form.addEventListener('submit', function (e) { e.preventDefault(); send(input.value); });
  root.querySelectorAll('[data-sex]').forEach(function (b) {
    b.addEventListener('click', function () { var was = mode === 'voice'; setSex(b.dataset.sex); if (was) { stop(); voiceOn(); } });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('open')) close(); });
  var lastArea = null;
  function onArea() {
    var a = area(); if (a === lastArea) return; lastArea = a;
    if (!chatted && root.classList.contains('open')) welcome();
    tease.querySelector('.t').textContent = TXT[a].tease;
    if (conv && conv.sendContextualUpdate) { try { conv.sendContextualUpdate('Der Besucher ist jetzt im Bereich: ' + a); } catch (e) {} }
  }
  new MutationObserver(function () { setTimeout(onArea, 50); }).observe(document.body, { attributes: true, attributeFilter: ['class'] });

  function boot() {
    document.body.appendChild(root); document.body.appendChild(guide);
    setSex(sex);
    lastArea = area(); tease.querySelector('.t').textContent = TXT[lastArea].tease;
    if (!store.sget('teased')) {
      var tries = 0;
      (function later() {
        var ck = document.getElementById('ck');
        if (ck && !ck.hidden && tries++ < 120) { setTimeout(later, 1000); return; }
        setTimeout(function () { if (!root.classList.contains('open') && !store.sget('teased')) { tease.classList.add('on'); botState('wave', true); setTimeout(function () { botState('wave', false); }, 1600); } }, 1800);
      })();
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
