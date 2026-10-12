/**
 * High Level Performance – Bewertungen
 * Google Apps Script für die Tabelle „HLP Bewertungen“.
 * Einrichtung: Tabelle öffnen → Erweiterungen → Apps Script → diesen Code einfügen →
 * einmal die Funktion setup() ausführen (erlaubt den Zugriff) →
 * Bereitstellen → Neue Bereitstellung → Web-App, Ausführen als: Ich, Zugriff: Jeder.
 */
var SHEET = 'Bewertungen';
var HEAD = ['ID', 'Datum', 'Name', 'Firma / Branche', 'Sterne', 'Text', 'Freigegeben'];

function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET) || ss.insertSheet(SHEET);
  if (sh.getLastRow() === 0) { sh.appendRow(HEAD); sh.setFrozenRows(1); }
  var p = PropertiesService.getScriptProperties();
  if (!p.getProperty('KEY')) p.setProperty('KEY', Utilities.getUuid());
}

function sheet_() { return SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET); }
function clean_(s, n) { return String(s || '').replace(/<[^>]*>/g, '').trim().slice(0, n); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

function doPost(e) {
  var d = {};
  try { d = JSON.parse(e.postData.contents); } catch (err) { return json_({ ok: false }); }
  if (d.website) return json_({ ok: true });               // Honeypot: Bots ignorieren
  var name = clean_(d.name, 60), firma = clean_(d.firma, 80), text = clean_(d.text, 600);
  var sterne = Math.max(1, Math.min(5, parseInt(d.sterne, 10) || 5));
  if (name.length < 2 || text.length < 10) return json_({ ok: false });
  var id = Utilities.getUuid().slice(0, 8);
  sheet_().appendRow([id, new Date(), name, firma, sterne, text, '']);
  var key = PropertiesService.getScriptProperties().getProperty('KEY');
  var link = ScriptApp.getService().getUrl() + '?action=approve&id=' + id + '&key=' + key;
  MailApp.sendEmail({
    to: Session.getEffectiveUser().getEmail(),
    subject: 'Neue Bewertung: ' + sterne + ' Sterne von ' + name,
    htmlBody: '<p><b>' + name + '</b>' + (firma ? ' (' + firma + ')' : '') + ' – ' + sterne + ' von 5 Sternen</p>' +
      '<p>„' + text + '“</p><p><a href="' + link + '" style="background:#1877F2;color:#fff;padding:12px 20px;border-radius:8px;text-decoration:none">Freigeben</a></p>' +
      '<p style="color:#666">Nicht freigeben? Einfach ignorieren.</p>'
  });
  return json_({ ok: true });
}

function doGet(e) {
  var a = (e.parameter.action || 'list');
  if (a === 'approve') {
    var key = PropertiesService.getScriptProperties().getProperty('KEY');
    if (e.parameter.key !== key) return HtmlService.createHtmlOutput('Kein Zugriff.');
    var sh = sheet_(), v = sh.getDataRange().getValues();
    for (var i = 1; i < v.length; i++) if (v[i][0] === e.parameter.id) {
      sh.getRange(i + 1, 7).setValue('Ja');
      return HtmlService.createHtmlOutput('<h2 style="font-family:sans-serif">Freigegeben ✔</h2><p style="font-family:sans-serif">Die Bewertung von ' + v[i][2] + ' steht jetzt auf der Website.</p>');
    }
    return HtmlService.createHtmlOutput('Nicht gefunden.');
  }
  var rows = sheet_().getDataRange().getValues().slice(1)
    .filter(function (r) { return String(r[6]).toLowerCase() === 'ja'; })
    .reverse().slice(0, 30)
    .map(function (r) { return { name: r[2], firma: r[3], sterne: r[4], text: r[5] }; });
  return json_({ ok: true, reviews: rows });
}
