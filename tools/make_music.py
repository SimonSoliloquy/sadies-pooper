"""Make Sadie's Pooper's background music with Google's Lyria (Gemini API), as Simon asked (2026-11-18).

Reads the key from GEMINI_API_KEY or ~/.config/excelsior/gemini_key. Lyria's clip model returns 30 seconds of audio;
this saves it raw in music/raw/, then (with ffmpeg) trims a loop and writes music/loop.mp3 for the game.
  python3 tools/make_music.py          # generate and encode
  python3 tools/make_music.py --recut  # only re-encode the saved raw clip
"""
import base64, json, os, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT, RAW = ROOT / 'music', ROOT / 'music' / 'raw'
URL = 'https://generativelanguage.googleapis.com/v1beta/interactions'
MODEL = 'lyria-3-clip-preview'
PROMPT = ('A silly, bouncy, goofy cartoon chase tune for a funny video game about a dog that poops and a woman chasing it '
          'with a poop bag. Oompah tuba bass line, buzzing kazoo melody, plucky pizzicato, slide whistle accents, woodblock and '
          'snare. Upbeat, playful and cheeky, around 140 BPM, major key. Instrumental only, no vocals. Steady energy from start '
          'to end so it loops seamlessly.')


def key():
    k = os.environ.get('GEMINI_API_KEY')
    if not k:
        p = Path.home() / '.config' / 'excelsior' / 'gemini_key'
        k = p.read_text().strip() if p.exists() else None
    if not k:
        raise SystemExit('No Gemini API key (GEMINI_API_KEY or ~/.config/excelsior/gemini_key).')
    return k


def generate():
    body = json.dumps({'model': MODEL, 'input': PROMPT}).encode()
    req = urllib.request.Request(URL, data=body, method='POST', headers={
        'Content-Type': 'application/json', 'Api-Revision': '2026-05-20', 'x-goog-api-key': key()})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f'Google answered {e.code}. {e.read().decode("utf-8", "replace")[:400]}')
    for step in data.get('steps', []):
        if step.get('type') != 'model_output':
            continue
        for block in step.get('content', []):
            if block.get('type') == 'audio' and block.get('data'):
                return base64.b64decode(block['data']), block.get('mime_type') or block.get('mimeType') or ''
    raise SystemExit(f'The response had no audio in it: {json.dumps(data)[:300]}')


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    if '--recut' not in sys.argv:
        audio, mime = generate()
        ext = 'mp3' if 'mpeg' in mime or 'mp3' in mime else 'wav' if 'wav' in mime else 'bin'
        (RAW / f'loop.{ext}').write_bytes(audio)
        print(f'saved music/raw/loop.{ext} ({len(audio) // 1024} KB, {mime or "unknown type"})')
    src = next(RAW.glob('loop.*'))
    # 28 s of the clip, with a short fade at both ends so the loop seam is soft
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostdin', '-y', '-i', str(src), '-t', '28',
                        '-af', 'afade=t=in:d=0.08,afade=t=out:st=27.6:d=0.4', '-ac', '2', '-b:a', '128k', str(OUT / 'loop.mp3')],
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr[-600:])
    print('wrote music/loop.mp3', (OUT / 'loop.mp3').stat().st_size // 1024, 'KB')


if __name__ == '__main__':
    main()
