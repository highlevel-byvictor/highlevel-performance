/* High Level Performance – Google Ads Conversion-Tracking
   Lädt Google Ads NUR mit Marketing-Einwilligung (Schlüssel hlp_consent_v1, wie Cookie-Banner).
   IDs nach dem Anlegen des Google-Ads-Kontos eintragen. Leer = es wird nichts geladen. */
(function(){
  var CFG = {
    ADS_ID: '',            // z. B. 'AW-123456789'
    CONV: {
      lead: '',            // Label "Potenzialanalyse angefragt"  (Formular Business-Seite)
      entwurf: '',         // Label "Website-Entwurf angefordert" (Fragebogen /website-business/)
      anruf: ''            // Label "Klick auf Telefonnummer"
    },
    WEBHOOK: ''            // Pabbly-Connect-Webhook "HLP Business – Google Leads"
  };
  var K = 'hlp_consent_v1', loaded = false;

  function getConsent(){ try{ return JSON.parse(localStorage.getItem(K) || 'null'); }catch(e){ return null; } }
  function setConsent(v){ try{ localStorage.setItem(K, JSON.stringify(v)); }catch(e){} }

  function gt(){ window.dataLayer = window.dataLayer || []; if(!window.gtag){ window.gtag = function(){ dataLayer.push(arguments); }; } return window.gtag; }

  function load(c){
    if(!c || !c.mkt || !CFG.ADS_ID || loaded) return;
    loaded = true;
    var g = gt();
    g('consent', 'default', { ad_storage:'denied', ad_user_data:'denied', ad_personalization:'denied', analytics_storage:'denied' });
    g('consent', 'update', { ad_storage:'granted', ad_user_data:'granted', ad_personalization:'granted', analytics_storage: c.stat ? 'granted' : 'denied' });
    if(!document.querySelector('script[src*="googletagmanager.com/gtag/js"]')){
      var s = document.createElement('script'); s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + CFG.ADS_ID;
      document.head.appendChild(s);
      g('js', new Date());
    }
    g('config', CFG.ADS_ID);
  }

  function conv(name){
    var label = CFG.CONV[name];
    if(!loaded || !label || !window.gtag) return;
    window.gtag('event', 'conversion', { send_to: CFG.ADS_ID + '/' + label });
  }

  /* Herkunft der Anfrage (Google-Klick-ID, Kampagne, Keyword) – nur aus der aktuellen URL, ohne Speicherung */
  function quelle(){
    var h = location.hash.indexOf('?') > -1 ? location.hash.slice(location.hash.indexOf('?') + 1) : '';
    var p = new URLSearchParams(location.search.slice(1) + (h ? '&' + h : '')), out = [];
    ['utm_source','utm_campaign','utm_term','gclid','gbraid','wbraid'].forEach(function(k){ var v = p.get(k); if(v) out.push(k + '=' + v.slice(0,120)); });
    return out.join(' | ');
  }

  /* Klick auf Telefonnummer zählen */
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="tel:"]');
    if(a) conv('anruf');
  }, true);

  /* Kleiner Cookie-Hinweis für Unterseiten ohne eigenes Banner */
  function banner(){
    if(getConsent()) return;
    var d = document.createElement('div');
    d.setAttribute('role','dialog'); d.setAttribute('aria-label','Cookie-Einstellungen');
    d.style.cssText = 'position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;display:flex;justify-content:center;font:400 14px/1.5 Manrope,Arial,sans-serif';
    d.innerHTML = '<div style="max-width:720px;background:#fff;color:#0B1630;border:1px solid #DCE5F3;border-radius:16px;padding:18px 20px;box-shadow:0 24px 60px -20px rgba(10,42,102,.45)">'
      + '<b style="font:700 16px Poppins,Arial,sans-serif">Cookies &amp; Datenschutz</b>'
      + '<p style="margin:6px 0 12px;color:#4A5874">Wir nutzen technisch notwendige Speicherung. Mit Ihrer Zustimmung setzen wir zusätzlich Statistik (Google Analytics) und Marketing (Meta-Pixel, Google Ads) ein, um unsere Seite und Werbung zu verbessern. Mehr in der <a href="/datenschutz/" style="color:#1877F2">Datenschutzerklärung</a>.</p>'
      + '<div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end">'
      + '<button type="button" data-c="no" style="font:600 14px Poppins,Arial;padding:10px 16px;border-radius:10px;border:1px solid #DCE5F3;background:#fff;color:#0B1630;cursor:pointer">Nur notwendige</button>'
      + '<button type="button" data-c="all" style="font:600 14px Poppins,Arial;padding:10px 16px;border-radius:10px;border:0;background:#1877F2;color:#fff;cursor:pointer">Alle akzeptieren</button>'
      + '</div></div>';
    d.addEventListener('click', function(e){
      var b = e.target.closest('button[data-c]'); if(!b) return;
      var all = b.getAttribute('data-c') === 'all';
      var c = { stat: all, mkt: all, t: Date.now() };
      setConsent(c); d.remove(); load(c);
    });
    document.body.appendChild(d);
  }

  /* Anfrage zusätzlich an den Pabbly-Workflow schicken (Brevo, ClickSend, Benachrichtigung) */
  function hook(fd, formular){
    if(!CFG.WEBHOOK) return;
    try{
      var o = {}; fd.forEach(function(v, k){ if(typeof v === 'string' && k !== 'website') o[k] = v; });
      o.formular = formular; o.quelle = o.quelle || quelle(); o.seite = location.href.split('#')[0]; o.zeit = new Date().toISOString();
      fetch(CFG.WEBHOOK, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain' }, body: JSON.stringify(o), keepalive: true });
    }catch(e){}
  }

  window.HLP_ADS = { load: load, conv: conv, quelle: quelle, banner: banner, hook: hook, config: CFG };
  load(getConsent());
})();
