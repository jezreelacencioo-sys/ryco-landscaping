"""Builds every design concept into /concepts/, plus a review page at /concepts/.
Run: python3 _build/concepts/build_all.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import carolina  # noqa: E402
import estate  # noqa: E402
import field  # noqa: E402
import garden  # noqa: E402
import mix  # noqa: E402
import palettes  # noqa: E402
from common import ROOT  # noqa: E402

CONCEPTS = [
    ('premier-mix', 'E', 'Premier Mix (mockup)', 'NEWEST: home page mockup mixing the original site with concept D. Black, deep green, lime and yellow; bold condensed headlines with playful rounded accent words, spinning 5-star badge, grass edge, scrolling services strip, photo cards and dashed process.'),
    ('field-day', 'D', 'Field Day', 'NEW: bold and sporty, based on the example you sent. Deep green, bright lime and a yellow accent with tall condensed headlines, brush-stroke underlines, chunky outlined buttons, photo cards and a numbered process.'),
    ('garden-journal', 'A', 'Garden Journal', 'Warm and editorial. Cream, forest green and terracotta with an elegant serif. Arched photos, a numbered service list and a seasonal "year in your yard" calendar.'),
    ('carolina-blue', 'B', 'Carolina Blue', 'Clean, trustworthy and built to get quotes. Navy, Carolina blue and grass green. Quote form right in the hero, service icons, step-by-step process and stats.'),
    ('estate', 'C', 'Estate', 'Dark, quiet luxury. Charcoal, champagne gold and ivory with a refined serif. Full-screen photo hero and large alternating service sections.'),
]

REVIEW_PAGE = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Website Concepts | Carolina Premier</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
body { margin: 0; font: 400 1rem/1.6 Inter, system-ui, sans-serif; background: #f4f5f2; color: #151a16; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 50px 22px 80px; }
h1 { font-size: clamp(2rem, 5vw, 3rem); margin: 0 0 8px; letter-spacing: -.02em; }
.intro { color: #5b625d; max-width: 62ch; margin: 0 0 40px; }
.grid { display: grid; gap: 26px; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
.card { background: #fff; border-radius: 18px; overflow: hidden; border: 1px solid #e1e5e0; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform .2s, box-shadow .2s; }
.card:hover { transform: translateY(-4px); box-shadow: 0 18px 40px rgba(0, 0, 0, .1); }
.card img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; border-bottom: 1px solid #e1e5e0; }
.card div { padding: 22px 24px 26px; }
.card .tag { font-size: .75rem; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; color: #4f9a2f; }
.card h2 { margin: 6px 0 8px; font-size: 1.5rem; }
.card p { margin: 0 0 14px; color: #5b625d; }
.card b { color: #151a16; }
.note { margin-top: 40px; color: #5b625d; font-size: .95rem; }
</style></head><body><div class="wrap">
<h1>Website concepts</h1>
<p class="intro">New designs built from the same business info, plus the current site for comparison. Concepts A to D are working sites with a home page, all seven service pages, service areas, projects, reviews, about and contact. Concept E is a home page mockup.</p>
<div class="grid">
CARDS
</div>
<p class="note"><b><a href="./colors/">Accent color options for the live design →</a></b></p>
<p class="note">These concept pages are hidden from Google so they don't compete with the real site.</p>
</div></body></html>
'''


def review_page():
    cards = [f'''<a class="card" href="./{slug}/"><img src="./assets/preview-{slug}.jpg" alt="Concept {letter}: {name}" width="960" height="600">
<div><span class="tag">Concept {letter}</span><h2>{name}</h2><p>{desc}</p><b>Open concept {letter} →</b></div></a>'''
             for slug, letter, name, desc in CONCEPTS]
    cards.append('''<a class="card" href="../"><img src="./assets/preview-current.jpg" alt="Current site" width="960" height="600">
<div><span class="tag">Live site</span><h2>Current site</h2><p>The live site: the Premier Mix style (concept E) with the All Green accent, across all 66 pages.</p><b>Open live site →</b></div></a>''')
    (ROOT / 'concepts' / 'index.html').write_text(REVIEW_PAGE.replace('CARDS', '\n'.join(cards)))


for concept in (garden, carolina, estate, field, mix):
    concept.build()
review_page()
palettes.build()
print('built concepts review page')
