"""Accent color mockups: the live home page re-rendered with a different accent color in place
of the yellow. Output: /concepts/colors/<slug>/ plus a comparison page at /concepts/colors/."""
import re

from common import ROOT

# slug, name, description, accent, accent-d (shadow), accent-h (hover), on-accent (text on it), accent-ink (accent as text on dark),
# and optionally extra CSS for that palette
PALETTES = [
    ('sunshine-yellow', 'Sunshine Yellow', 'The previous accent. Warm and energetic.',
     '#ffc20e', '#c99500', '#ffd04a', '#073a1b', '#ffc20e'),
    ('fresh-lime', 'All Green (live)', 'Chosen for the live site. No second color, just your greens. A brighter lime takes the yellow\'s place, so everything matches the logo.',
     '#a6e35f', '#6fae32', '#b9ec7c', '#073a1b', '#a6e35f'),
    ('carolina-blue', 'Carolina Blue', 'A sky blue accent. Fresh and clean, with a nod to North Carolina.',
     '#6ec1f5', '#3a8ccc', '#8fd0f8', '#062b44', '#8fd0f8'),
    ('sunset-orange', 'Sunset Orange', 'A bold orange accent. The most playful and eye-catching option.',
     '#ff7a21', '#c4540a', '#ff9447', '#2b1200', '#ff8f3f'),
    ('clean-white', 'Clean White', 'White in place of yellow. The most professional and minimal option.',
     '#ffffff', '#b9cdb5', '#eef6ea', '#0a4d24', '#ffffff', '.svc-cta { box-shadow: inset 0 0 0 4px #0a4d24, 6px 6px 0 #86cf45; }'),
    ('black-lime', 'Black & Lime', 'Black buttons with lime text. Sporty and high contrast, with no extra color.',
     '#0b0f0c', '#000000', '#1d2620', '#86cf45', '#86cf45'),
]

PAGE = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Accent Color Options | Carolina Premier</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
body { margin: 0; font: 400 1rem/1.6 Inter, system-ui, sans-serif; background: #f4f5f2; color: #151a16; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 50px 22px 80px; }
h1 { font-size: clamp(2rem, 5vw, 3rem); margin: 0 0 8px; letter-spacing: -.02em; }
.intro { color: #5b625d; max-width: 64ch; margin: 0 0 40px; }
.grid { display: grid; gap: 26px; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
.card { background: #fff; border-radius: 18px; overflow: hidden; border: 1px solid #e1e5e0; text-decoration: none; color: inherit; transition: transform .2s, box-shadow .2s; }
.card:hover { transform: translateY(-4px); box-shadow: 0 18px 40px rgba(0, 0, 0, .1); }
.card img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; object-position: top; border-bottom: 1px solid #e1e5e0; }
.card div { padding: 20px 22px 24px; }
.sw { display: flex; gap: 8px; margin-bottom: 10px; }
.sw span { width: 28px; height: 28px; border-radius: 8px; border: 1px solid rgba(0, 0, 0, .15); }
.card h2 { margin: 0 0 6px; font-size: 1.4rem; }
.card p { margin: 0 0 12px; color: #5b625d; }
</style></head><body><div class="wrap">
<h1>Accent color options</h1>
<p class="intro">Same design as the live site. Only the accent color changes (the top bar, secondary buttons, the spinning badge center, the "Not sure what you need?" card, the stripes and the phone call bar). Greens and lime stay to match your logo. Open each one on your phone too.</p>
<div class="grid">
CARDS
</div></div></body></html>
'''


def build():
    src = (ROOT / 'index.html').read_text()
    for slug, name, desc, accent, accent_d, accent_h, on_accent, ink, *extra in PALETTES:
        html = src.replace('"./', '"../../../').replace("'./", "'../../../").replace('(./', '(../../../')
        html = re.sub(r'<link rel="canonical"[^>]*>\n', '', html)
        override = (f'<meta name="robots" content="noindex, nofollow">\n<style>:root {{ --accent: {accent}; --accent-d: {accent_d}; '
                    f'--accent-h: {accent_h}; --on-accent: {on_accent}; --accent-ink: {ink}; }}{"".join(extra)}</style>\n</head>')
        html = html.replace('</head>', override, 1)
        out = ROOT / 'concepts' / 'colors' / slug / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
    cards = [f'''<a class="card" href="./{slug}/"><img src="./preview-{slug}.jpg" alt="{name}" width="960" height="600">
<div><div class="sw"><span style="background:#0a4d24"></span><span style="background:#86cf45"></span><span style="background:{accent}"></span></div>
<h2>{name}</h2><p>{desc}</p><b>Open {name.split(" (")[0]} →</b></div></a>''' for slug, name, desc, accent, *_ in PALETTES]
    (ROOT / 'concepts' / 'colors' / 'index.html').write_text(PAGE.replace('CARDS', '\n'.join(cards)))
    print('built color options')
