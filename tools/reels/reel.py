#!/usr/bin/env python3
"""HLP Reel-Engine: Skript (JSON) -> fertiges Reel 9:16 + 1:1.

Aufruf:
  python3 reel.py skript.json --out OUTDIR [--keys keys.env] [--cache CACHEDIR] [--dry]

Skript-Format (siehe beispiel.json):
{
  "id": "2026-11-23_bessere-website",
  "hook_overlay": "Die bessere Website\nbekommt den Auftrag",
  "segments": [
    {"text": "Gesprochener Satz.", "query": "kitchen showroom", "overlay": "optional", "keywords": ["Website"]},
    ...
  ],
  "cta": {"title": "Kommentiere ENTWURF", "sub": "Kostenloser Website-Entwurf in 24 Stunden"}
}

Stimme: ElevenLabs KonradKlar (mz5P37ARbAUej0kN0R11), Tempo per voice_settings.speed.
Stock: Pixabay-Videos (echte Menschen, keine KI). Keine Emojis im Bild.
Untertitel: Poppins Bold, Schluesselwoerter gelb, Position unteres Drittel (nicht ueber Gesichtern
im oberen/mittleren Bild), 9:16-Safe-Zones oben 14 %, unten 20 %.
"""
import argparse, base64, hashlib, json, os, random, re, shutil, subprocess, sys, tempfile, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageFilter

VOICE = "mz5P37ARbAUej0kN0R11"
MODELS = ["eleven_v4", "eleven_multilingual_v2"]
FONT_DIRS = ["/usr/share/fonts/truetype/google-fonts", os.path.join(os.path.dirname(__file__), "fonts")]
BLUE = (24, 119, 242)
YELLOW = (255, 214, 0)
NAVY = (11, 22, 48)


def font(size, name="Poppins-Bold.ttf"):
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        raise SystemExit(f"Fehler bei: {' '.join(cmd[:6])} ...")
    return r.stdout


def keys(path):
    k = {}
    if path and os.path.exists(path):
        for line in open(path):
            if "=" in line:
                a, b = line.strip().split("=", 1)
                k[a] = b
    k.update({x: os.environ[x] for x in ("PIXABAY_KEY", "ELEVENLABS_KEY") if os.environ.get(x)})
    return k


def http_json(url, data=None, headers=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 HLP-Reels", **(headers or {})})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 HLP-Reels"})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)
    return dest


# ---------- Sprache ----------
def tts(text, k, cache, speed=1.15):
    h = hashlib.sha1((text + str(speed)).encode()).hexdigest()[:16]
    mp3, js = os.path.join(cache, f"tts_{h}.mp3"), os.path.join(cache, f"tts_{h}.json")
    if os.path.exists(mp3) and os.path.exists(js):
        return mp3, json.load(open(js))
    if not k.get("ELEVENLABS_KEY"):
        if os.environ.get("HLP_FAKE_TTS"):  # nur zum Testen der Bildspur
            secs = max(1.0, len(text) * 0.055)
            sh(["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=mono", "-t", f"{secs:.2f}", "-q:a", "9", mp3])
            chars = list(text)
            step = secs / max(1, len(chars))
            return mp3, {"characters": chars, "character_start_times_seconds": [i * step for i in range(len(chars))],
                         "character_end_times_seconds": [(i + 1) * step for i in range(len(chars))]}
        raise SystemExit("ELEVENLABS_KEY fehlt (keys.env)")
    last = None
    for model in MODELS:
        try:
            out = http_json(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128",
                            {"text": text, "model_id": model,
                             "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "speed": speed}},
                            {"xi-api-key": k["ELEVENLABS_KEY"]})
            break
        except urllib.error.HTTPError as e:
            last = e.read().decode()[:300]
            out = None
    if not out:
        raise SystemExit("ElevenLabs-Fehler: " + str(last))
    open(mp3, "wb").write(base64.b64decode(out["audio_base64"]))
    al = out.get("normalized_alignment") or out["alignment"]
    json.dump(al, open(js, "w"))
    return mp3, al


def words_from_alignment(al, offset):
    chars, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    words, cur, t0 = [], "", None
    for c, a, b in zip(chars, st, en):
        if c.isspace():
            if cur:
                words.append([cur, t0 + offset, last + offset])
            cur, t0 = "", None
        else:
            if t0 is None:
                t0 = a
            cur += c
            last = b
    if cur:
        words.append([cur, t0 + offset, last + offset])
    return words


def dur(path):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", path]).strip())


def trim_silence(src, dst):
    sh(["ffmpeg", "-y", "-i", src, "-af",
        "silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.25:stop_threshold=-45dB",
        dst])
    return dst


# ---------- Stock ----------
def pixabay_video(query, k, cache, used, min_dur):
    """Echtes Footage (video_type=film), Tags muessen zum Suchbegriff passen. Mehrere Begriffe mit | moeglich."""
    for q0 in [x.strip() for x in query.split("|") if x.strip()]:
        q = urllib.parse.quote(q0)
        url = f"https://pixabay.com/api/videos/?key={k['PIXABAY_KEY']}&q={q}&per_page=40&safesearch=true&video_type=film&order=popular"
        data = http_json(url)
        words = [w.lower() for w in q0.split() if len(w) > 2]
        def ok(h):
            tags = h.get("tags", "").lower()
            return sum(w in tags for w in words) >= max(1, len(words) - 1)
        hits = [h for h in data.get("hits", []) if h["id"] not in used and ok(h)]
        long_ = [h for h in hits if h["duration"] >= min_dur]
        hits = long_ or hits
        if hits:
            h = hits[0]
            used.add(h["id"])
            v = h["videos"].get("large") or {}
            if not v.get("url") or v.get("width", 0) < 1280:
                v = h["videos"].get("medium") if (h["videos"].get("medium") or {}).get("width", 0) > v.get("width", 0) else v
            return download(v["url"], os.path.join(cache, f"px_{h['id']}.mp4")), h
    raise SystemExit(f"Kein passendes Pixabay-Video fuer: {query}")


# ---------- Grafik ----------
def wrap(draw, text, fnt, maxw):
    lines = []
    for para in text.split("\n"):
        line = ""
        for w in para.split():
            t = (line + " " + w).strip()
            if draw.textlength(t, font=fnt) <= maxw:
                line = t
            else:
                if line:
                    lines.append(line)
                line = w
        lines.append(line)
    return lines


def caption_png(words, keywords, W, H, path, y_frac):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    size = int(W * 0.075)
    f = font(size)
    text = " ".join(w.upper() for w in words)
    lines = wrap(d, text, f, W * 0.84)
    lh = int(size * 1.18)
    y = int(H * y_frac) - lh * len(lines) // 2
    kw = {re.sub(r"\W", "", x).upper() for x in keywords}
    for line in lines:
        x = (W - d.textlength(line, font=f)) / 2
        for tok in line.split(" "):
            col = YELLOW if re.sub(r"\W", "", tok) in kw else (255, 255, 255)
            d.text((x, y), tok, font=f, fill=col, stroke_width=max(4, size // 11), stroke_fill=(0, 0, 0))
            x += d.textlength(tok + " ", font=f)
        y += lh
    img.save(path)


def hook_png(text, W, H, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    size = int(W * 0.068)
    f = font(size)
    lines = wrap(d, text, f, W * 0.82)
    lh = int(size * 1.2)
    pad = int(size * 0.45)
    top = int(H * 0.15)
    boxw = max(d.textlength(l, font=f) for l in lines) + pad * 2
    boxh = lh * len(lines) + pad * 2
    x0 = (W - boxw) / 2
    d.rounded_rectangle([x0, top, x0 + boxw, top + boxh], radius=int(size * 0.35), fill=(255, 255, 255, 240))
    y = top + pad
    for l in lines:
        d.text(((W - d.textlength(l, font=f)) / 2, y), l, font=f, fill=NAVY)
        y += lh
    img.save(path)


def cta_png(cta, W, H, path):
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    # Verlaufsstreifen oben (Markenfarben)
    for x in range(W):
        t = x / W
        d.line([(x, 0), (x, 14)], fill=(int(233 * (1 - t) + 56 * t), int(14 * (1 - t) + 200 * t), int(14 * (1 - t) + 255 * t)))
    f1, f2, f3 = font(int(W * 0.05)), font(int(W * 0.085)), font(int(W * 0.042), "Poppins-Regular.ttf")
    y = int(H * 0.30)
    for l in ["HIGH LEVEL PERFORMANCE"]:
        d.text(((W - d.textlength(l, font=f1)) / 2, y), l, font=f1, fill=(255, 255, 255))
    y += int(W * 0.14)
    for l in wrap(d, cta["title"], f2, W * 0.86):
        d.text(((W - d.textlength(l, font=f2)) / 2, y), l, font=f2, fill=YELLOW)
        y += int(W * 0.11)
    y += int(W * 0.03)
    for l in wrap(d, cta.get("sub", ""), f3, W * 0.8):
        d.text(((W - d.textlength(l, font=f3)) / 2, y), l, font=f3, fill=(220, 228, 245))
        y += int(W * 0.065)
    # Button
    bw, bh = int(W * 0.62), int(W * 0.12)
    bx, by = (W - bw) // 2, y + int(W * 0.06)
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=bh // 2, fill=BLUE)
    lab = cta.get("button", "Link in der Bio")
    fb = font(int(W * 0.045))
    d.text(((W - d.textlength(lab, font=fb)) / 2, by + (bh - int(W * 0.06)) / 2), lab, font=fb, fill=(255, 255, 255))
    img.save(path)


# ---------- Musik / SFX ----------
def elevenlabs_sfx(prompt, seconds, k, cache, name):
    p = os.path.join(cache, name)
    if os.path.exists(p):
        return p
    if not k.get("ELEVENLABS_KEY"):
        return None
    req = urllib.request.Request("https://api.elevenlabs.io/v1/sound-generation",
                                 data=json.dumps({"text": prompt, "duration_seconds": seconds, "prompt_influence": 0.5}).encode(),
                                 headers={"xi-api-key": k["ELEVENLABS_KEY"], "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            open(p, "wb").write(r.read())
        return p
    except Exception as e:
        sys.stderr.write(f"SFX nicht erzeugt ({name}): {e}\n")
        return None


# ---------- Render ----------
def render(script, out, k, cache, W, H, tag, speech, words, seg_times, clips):
    tmp = tempfile.mkdtemp()
    total = seg_times[-1][1]
    cta_len = 2.6
    # 1) Bildspur: jeder Abschnitt in 2-3-Sekunden-Schnitte zerlegt
    parts = []
    for i, ((t0, t1), (clip, meta)) in enumerate(zip(seg_times, clips)):
        L = t1 - t0
        n = max(1, round(L / 2.6))
        sub = L / n
        cd = meta["duration"]
        for j in range(n):
            ss = (j * sub * 1.3) % max(0.1, cd - sub - 0.1)
            o = os.path.join(tmp, f"p{i}_{j}.mp4")
            sh(["ffmpeg", "-y", "-ss", f"{ss:.2f}", "-t", f"{sub:.3f}", "-i", clip, "-an", "-vf",
                f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                f"fps=30,zoompan=z='min(1+0.0016*on,1.08)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps=30,eq=contrast=1.05:saturation=1.08,setsar=1",
                "-r", "30", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", o])
            parts.append(o)
    ctap = os.path.join(tmp, "cta.png")
    cta_png(script["cta"], W, H, ctap)
    ctav = os.path.join(tmp, "cta.mp4")
    sh(["ffmpeg", "-y", "-loop", "1", "-t", str(cta_len), "-i", ctap, "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", ctav])
    parts.append(ctav)
    lst = os.path.join(tmp, "l.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    base = os.path.join(tmp, "base.mp4")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])

    # 2) Overlays: Hook (erste 2,8 s) + Untertitel in 2-3-Wort-Gruppen
    ovl, inputs = [], ["-i", base]
    hp = os.path.join(tmp, "hook.png")
    hook_png(script["hook_overlay"], W, H, hp)
    inputs += ["-i", hp]
    ovl.append((1, 0.0, min(2.8, total)))
    groups, g = [], []
    for w in words:
        g.append(w)
        if len(g) == 3 or w[0][-1] in ".,!?:":
            groups.append(g)
            g = []
    if g:
        groups.append(g)
    kws = [x for s in script["segments"] for x in s.get("keywords", [])]
    y_frac = 0.66 if H > W else 0.74
    for gi, grp in enumerate(groups):
        p = os.path.join(tmp, f"c{gi}.png")
        caption_png([w[0] for w in grp], kws, W, H, p, y_frac)
        inputs += ["-i", p]
        end = groups[gi + 1][0][1] if gi + 1 < len(groups) else grp[-1][2] + 0.2
        ovl.append((len(inputs) // 2 - 1, grp[0][1], min(end, total)))
    fc, last = [], "[0:v]"
    for n, (idx, a, b) in enumerate(ovl):
        o = f"[v{n}]"
        fc.append(f"{last}[{idx}:v]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})'{o}")
        last = o
    vid = os.path.join(tmp, "vid.mp4")
    fcp = os.path.join(tmp, "fc.txt")
    open(fcp, "w").write(";".join(fc))
    sh(["ffmpeg", "-y", *inputs, "-filter_complex_script", fcp, "-map", last, "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", vid])

    # 3) Ton: Sprache + Musikbett (leise, immer hoerbar) + Whoosh an Schnitten, -14 LUFS
    music = elevenlabs_sfx("modern corporate lo-fi beat, soft kick, warm keys, motivating, no vocals, seamless loop", 22, k, cache, "music_bed.mp3")
    whoosh = elevenlabs_sfx("short soft swoosh transition, clean, subtle", 1, k, cache, "whoosh.mp3")
    ain = ["-i", speech]
    af = ["[1:a]apad=pad_dur=%.2f,volume=1.0[sp]" % cta_len]
    mix = ["[sp]"]
    if music:
        ain += ["-stream_loop", "-1", "-i", music]
        af.append(f"[2:a]volume=0.13,atrim=0:{total + cta_len:.2f},afade=t=out:st={total + cta_len - 1:.2f}:d=1[mu]")
        mix.append("[mu]")
    if whoosh:
        cuts = [t for t, _ in seg_times[1:]] + [total]
        base_i = len(ain) // 2 + 1
        for ci, t in enumerate(cuts):
            ain += ["-i", whoosh]
            af.append(f"[{base_i + ci}:a]volume=0.25,adelay={int(max(0, t - 0.15) * 1000)}|{int(max(0, t - 0.15) * 1000)}[w{ci}]")
            mix.append(f"[w{ci}]")
    af.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    fin = os.path.join(out, f"{script['id']}_{tag}.mp4")
    sh(["ffmpeg", "-y", "-i", vid, *ain, "-filter_complex", ";".join(af), "-map", "0:v", "-map", "[a]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", fin])
    shutil.rmtree(tmp, ignore_errors=True)
    return fin


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--out", default=".")
    ap.add_argument("--keys", default=os.path.expanduser("~/.hlp/keys.env"))
    ap.add_argument("--cache", default=os.path.expanduser("~/.hlp/cache"))
    ap.add_argument("--speed", type=float, default=1.15)
    ap.add_argument("--formats", default="9x16,1x1")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    os.makedirs(a.cache, exist_ok=True)
    k = keys(a.keys)
    s = json.load(open(a.script))
    # Sprache pro Abschnitt, damit Schnitte auf Satzgrenzen liegen
    tmp = tempfile.mkdtemp()
    seg_audio, words, seg_times, t = [], [], [], 0.0
    for i, seg in enumerate(s["segments"]):
        mp3, al = tts(seg["text"], k, a.cache, a.speed)
        wav = os.path.join(tmp, f"s{i}.wav")
        sh(["ffmpeg", "-y", "-i", mp3, "-ar", "44100", "-ac", "1", wav])
        L = dur(wav)
        words += words_from_alignment(al, t)
        seg_times.append((t, t + L))
        seg_audio.append(wav)
        t += L
    lst = os.path.join(tmp, "a.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in seg_audio))
    speech = os.path.join(tmp, "speech.wav")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", speech])
    used, clips = set(), []
    for (t0, t1), seg in zip(seg_times, s["segments"]):
        clips.append(pixabay_video(seg["query"], k, a.cache, used, t1 - t0))
    res = []
    for f in a.formats.split(","):
        W, H = (1080, 1920) if f == "9x16" else (1080, 1080)
        res.append(render(s, a.out, k, a.cache, W, H, f, speech, words, seg_times, clips))
    credits = [{"pixabay_id": m["id"], "user": m["user"], "page": m["pageURL"]} for _, m in clips]
    json.dump({"files": res, "dauer_s": round(seg_times[-1][1] + 2.6, 1), "stock": credits},
              open(os.path.join(a.out, f"{s['id']}_info.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    main()
