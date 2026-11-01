"""Mascot concept sketches (noindex) at /concepts/mascots/. Rough drafts to brief an illustrator."""
from common import ROOT

G, G2, LIME, INK = '#0a4d24', '#0e5f2d', '#86cf45', '#14201a'


def cap(x, y, s=1.0, rot=0):
    """Carolina Premier ball cap centred on (x, y) = middle of the brim."""
    return f'''<g transform="translate({x} {y}) rotate({rot}) scale({s})">
  <path d="M-92 0 Q-86 -82 0 -88 Q86 -82 92 0 Z" fill="{G}" stroke="{INK}" stroke-width="5"/>
  <path d="M-30 -86 Q0 -92 30 -86" fill="none" stroke="{G2}" stroke-width="6"/>
  <circle cx="0" cy="-90" r="7" fill="{LIME}" stroke="{INK}" stroke-width="3"/>
  <circle cx="0" cy="-42" r="24" fill="{LIME}" stroke="{INK}" stroke-width="4"/>
  <text x="0" y="-34" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="22" fill="{G}">CP</text>
  <path d="M-100 0 Q0 -16 100 0 Q112 12 96 20 Q0 4 -96 20 Q-112 12 -100 0 Z" fill="{LIME}" stroke="{INK}" stroke-width="5"/>
</g>'''


def eye(x, y, r=20, look=4):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="4"/>'
            f'<circle cx="{x + look}" cy="{y + 2}" r="{r * .55}" fill="{INK}"/>'
            f'<circle cx="{x + look + r * .2}" cy="{y - r * .2}" r="{r * .18}" fill="#fff"/>')


def shirt(cx, top, w, h):
    return f'''<path d="M{cx - w} {top + h} Q{cx - w} {top} {cx - w * .45} {top - 6} Q{cx} {top + 24} {cx + w * .45} {top - 6} Q{cx + w} {top} {cx + w} {top + h} Z" fill="{G}" stroke="{INK}" stroke-width="5"/>
<text x="{cx}" y="{top + h * .62}" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="20" fill="{LIME}">PREMIER</text>'''


MASCOTS = []

# 1. Cardinal - NC state bird
MASCOTS.append(('Rocky the Cardinal', 'NC\'s state bird. Instantly "Carolina," friendly and bold. Red pops against your green.', f'''
{shirt(200, 300, 120, 100)}
<ellipse cx="200" cy="205" rx="100" ry="98" fill="#d7263d" stroke="{INK}" stroke-width="5"/>
<path d="M262 120 L330 70 L300 135 L345 128 L282 168 Z" fill="#d7263d" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<path d="M120 205 Q200 150 280 205 Q270 262 200 268 Q130 262 120 205 Z" fill="{INK}"/>
{eye(165, 200, 21, 3)}{eye(235, 200, 21, -1)}
<path d="M172 228 Q200 214 228 228 L200 270 Z" fill="#f6a01a" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
{cap(200, 140, 1.0, -4)}'''))

# 2. Fox
MASCOTS.append(('Rusty the Fox', 'Clever and quick. Reads as "sharp work." Easy to draw in action poses (mowing, trimming).', f'''
{shirt(200, 305, 120, 95)}
<path d="M112 160 L92 62 L168 120 Z" fill="#ef7d22" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<path d="M288 160 L308 62 L232 120 Z" fill="#ef7d22" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<path d="M112 128 L104 84 L140 116 Z M288 128 L296 84 L260 116 Z" fill="{INK}"/>
<path d="M85 200 Q90 120 200 115 Q310 120 315 200 Q300 270 200 300 Q100 270 85 200 Z" fill="#ef7d22" stroke="{INK}" stroke-width="5"/>
<path d="M95 215 Q150 225 200 300 Q250 225 305 215 Q290 268 200 300 Q110 268 95 215 Z" fill="#fff8ee"/>
{eye(160, 200, 19, 2)}{eye(240, 200, 19, -2)}
<ellipse cx="200" cy="245" rx="17" ry="12" fill="{INK}"/>
<path d="M178 265 Q200 285 222 265" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
{cap(200, 150, 1.0, 3)}'''))

# 3. Box turtle with a mowed-lawn shell
MASCOTS.append(('Shelby the Turtle', 'NC\'s state reptile, with a shell that looks like a freshly striped lawn. Unique and memorable.', f'''
<defs><clipPath id="shell"><path d="M70 300 Q70 150 235 145 Q390 150 390 300 Z"/></clipPath></defs>
<g clip-path="url(#shell)">{''.join(f'<rect x="{x}" y="140" width="40" height="170" fill="{"#5fb83c" if i % 2 else "#4a9a2d"}" transform="skewX(-14)"/>' for i, x in enumerate(range(60, 470, 40)))}</g>
<path d="M70 300 Q70 150 235 145 Q390 150 390 300 Z" fill="none" stroke="{INK}" stroke-width="6"/>
<path d="M60 300 Q230 330 400 300" fill="{G}" stroke="{INK}" stroke-width="6"/>
<ellipse cx="120" cy="325" rx="32" ry="22" fill="#9ccc65" stroke="{INK}" stroke-width="5"/>
<ellipse cx="330" cy="325" rx="32" ry="22" fill="#9ccc65" stroke="{INK}" stroke-width="5"/>
<path d="M95 270 Q40 260 45 205" fill="none" stroke="#9ccc65" stroke-width="48" stroke-linecap="round"/>
<circle cx="70" cy="185" r="58" fill="#9ccc65" stroke="{INK}" stroke-width="5"/>
{eye(52, 178, 15, 3)}{eye(92, 178, 15, 3)}
<path d="M52 212 Q72 228 92 212" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
{cap(70, 140, .62, -6)}'''))

# 4. Gray squirrel - NC state mammal
MASCOTS.append(('Acorn the Squirrel', 'NC\'s state mammal, always busy in the yard. Holding an acorn, it ties right into tree services.', f'''
<path d="M250 340 C390 330 395 170 330 105 C295 72 248 92 268 140 C292 195 292 262 238 300 Z" fill="#8d8d93" stroke="{INK}" stroke-width="5"/>
<path d="M300 120 C340 160 345 230 320 280" fill="none" stroke="#b9b9c0" stroke-width="10" stroke-linecap="round"/>
{shirt(190, 290, 95, 100)}
<path d="M125 140 L118 92 L160 125 Z M255 140 L262 92 L220 125 Z" fill="#8d8d93" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<ellipse cx="190" cy="205" rx="88" ry="85" fill="#8d8d93" stroke="{INK}" stroke-width="5"/>
<ellipse cx="190" cy="240" rx="52" ry="38" fill="#d9d9de"/>
{eye(158, 195, 19, 3)}{eye(222, 195, 19, -1)}
<ellipse cx="190" cy="228" rx="12" ry="8" fill="{INK}"/>
<rect x="180" y="242" width="20" height="16" rx="3" fill="#fff" stroke="{INK}" stroke-width="3"/>
<g transform="translate(250 300)"><ellipse cx="0" cy="12" rx="22" ry="26" fill="#b5772f" stroke="{INK}" stroke-width="4"/><path d="M-26 -2 Q0 -22 26 -2 Q0 8 -26 -2 Z" fill="#6b4320" stroke="{INK}" stroke-width="4"/></g>
{cap(190, 138, .95, -3)}'''))

# 5. Lawn mower character
MASCOTS.append(('Mo the Mower', 'A friendly mower with a face. Says "lawn care" at a glance and works great on trucks and yard signs.', f'''
<path d="M300 210 L350 70" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
<path d="M330 70 L372 76" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
<path d="M70 300 Q70 200 160 190 L300 190 Q340 195 340 250 L340 300 Z" fill="{LIME}" stroke="{INK}" stroke-width="6"/>
<rect x="60" y="292" width="290" height="24" rx="12" fill="{G}" stroke="{INK}" stroke-width="5"/>
<circle cx="110" cy="330" r="30" fill="{INK}"/><circle cx="110" cy="330" r="11" fill="#cfd8cf"/>
<circle cx="300" cy="330" r="30" fill="{INK}"/><circle cx="300" cy="330" r="11" fill="#cfd8cf"/>
{eye(150, 240, 20, 4)}{eye(210, 240, 20, 4)}
<path d="M150 275 Q180 295 212 275" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
{''.join(f'<path d="M{x} 360 l6 -26 l6 26" fill="{LIME}" stroke="{G}" stroke-width="3"/>' for x in range(20, 390, 22))}
{cap(195, 196, .8, -8)}'''))

# 6. Black bear
MASCOTS.append(('Big Jer the Bear', 'Black bears live in NC. Strong and dependable, a good fit for tree work and heavy jobs.', f'''
{shirt(200, 300, 125, 100)}
<circle cx="118" cy="125" r="34" fill="#3a2e2a" stroke="{INK}" stroke-width="5"/><circle cx="118" cy="125" r="15" fill="#8c6e5d"/>
<circle cx="282" cy="125" r="34" fill="#3a2e2a" stroke="{INK}" stroke-width="5"/><circle cx="282" cy="125" r="15" fill="#8c6e5d"/>
<ellipse cx="200" cy="205" rx="105" ry="98" fill="#3a2e2a" stroke="{INK}" stroke-width="5"/>
<ellipse cx="200" cy="245" rx="48" ry="38" fill="#b08b70"/>
{eye(162, 198, 19, 2)}{eye(238, 198, 19, -2)}
<ellipse cx="200" cy="232" rx="16" ry="11" fill="{INK}"/>
<path d="M182 256 Q200 272 218 256" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
{cap(200, 140, 1.02, 2)}'''))

PAGE = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Mascot Concepts | Carolina Premier</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800&family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">
<style>
body { margin: 0; font: 400 1rem/1.6 Nunito, system-ui, sans-serif; background: #f2f7ee; color: #101a13; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 44px 20px 80px; }
h1 { font: 800 clamp(2.4rem, 6vw, 3.6rem)/1 "Barlow Condensed", sans-serif; text-transform: uppercase; color: #0a4d24; margin: 0 0 10px; }
.intro { color: #55625a; max-width: 66ch; margin: 0 0 34px; }
.grid { display: grid; gap: 24px; grid-template-columns: repeat(auto-fill, minmax(min(320px, 100%), 1fr)); }
.card { background: #fff; border: 3px solid #0a4d24; border-radius: 22px; overflow: hidden; box-shadow: 6px 6px 0 #86cf45; }
.art { background: radial-gradient(circle at 50% 45%, #e9f6df, #cfe8bd); display: grid; place-items: center; padding: 10px; }
.art svg { width: 100%; max-width: 320px; height: auto; }
.card div.txt { padding: 18px 22px 22px; }
.num { font-weight: 800; color: #5e9e2a; text-transform: uppercase; letter-spacing: .12em; font-size: .78rem; }
h2 { font: 800 1.9rem/1 "Barlow Condensed", sans-serif; text-transform: uppercase; color: #0a4d24; margin: 4px 0 8px; }
.card p { margin: 0; color: #55625a; }
</style></head><body><div class="wrap">
<h1>Mascot concepts</h1>
<p class="intro">Rough drafts to pick a direction. Each wears a Carolina Premier cap in your colors. Once you choose one (or mix ideas), a professional illustrator can turn it into polished artwork for the site, trucks and shirts.</p>
<div class="grid">
CARDS
</div></div></body></html>
'''


def build():
    cards = '\n'.join(f'''<div class="card"><div class="art"><svg viewBox="0 0 400 400" role="img" aria-label="{name}">{svg}</svg></div>
<div class="txt"><span class="num">Concept {i + 1}</span><h2>{name}</h2><p>{desc}</p></div></div>''' for i, (name, desc, svg) in enumerate(MASCOTS))
    (ROOT / 'concepts' / 'mascots' / 'index.html').write_text(PAGE.replace('CARDS', cards))
    print('built mascots')
