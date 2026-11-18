# HLP Reel-Engine (organischer Content @highlevel.byvictor)

- `reel.py skript.json --out OUT --keys keys.env` → `<id>_9x16.mp4`, `<id>_1x1.mp4`, `<id>_info.json` (Stock-Nachweise).
- Schlüssel liegen NICHT im Repo: auf Viktors Mac in `~/Movies/HLP-Reels/_system/keys.env` (PIXABAY_KEY, ELEVENLABS_KEY).
- Stimme KonradKlar (mz5P37ARbAUej0kN0R11), Tempo 1,15, Untertitel Poppins Bold mit gelben Schlüsselwörtern, Hook-Box oben, CTA-Karte am Ende, Musikbett + Whoosh aus ElevenLabs-Soundeffekten (einmal erzeugt, dann Cache), -14 LUFS.
- Skripte: `skripte/*.json` (Woche 1 ab 23.11.2026). Quelle = Gewinner-Video aus der Datenbank (Projekt-Doc „claude/hlp-social-playbook.md“).
- Test ohne Stimme: `HLP_FAKE_TTS=1 python3 reel.py ...`
- Videos für Metricool: Branch `tiktok-uploads`, Ordner `hlp/` → `https://raw.githubusercontent.com/highlevel-byvictor/highlevel-performance/tiktok-uploads/hlp/<datei>.mp4`
