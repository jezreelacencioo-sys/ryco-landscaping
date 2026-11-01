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
<p class="intro">Rough drafts to pick a direction. Each wears a Carolina Premier cap in your colors. Once you choose one (or mix ideas), a professional illustrator can turn it into polished artwork for the site, trucks and shirts. <b><a href="./big-jer/">See the refined Big Jer versions →</a></b></p>
<div class="grid">
CARDS
</div></div></body></html>
'''


def build():
    cards = '\n'.join(f'''<div class="card"><div class="art"><svg viewBox="0 0 400 400" role="img" aria-label="{name}">{svg}</svg></div>
<div class="txt"><span class="num">Concept {i + 1}</span><h2>{name}</h2><p>{desc}</p></div></div>''' for i, (name, desc, svg) in enumerate(MASCOTS))
    (ROOT / 'concepts' / 'mascots' / 'index.html').write_text(PAGE.replace('CARDS', cards))
    print('built mascots')


# ---------------------------------------------------------------- Big Jer the Bear, refined versions
FUR, FUR2, MUZ, SHADE = '#4a372f', '#5d4639', '#c99f80', '#3a2b25'


def outlined(d, fill, w=46):
    """A thick rounded limb: dark outline stroke under a fur-colored stroke."""
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w + 10}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def bear_head(shades=False, cap_svg=None):
    eyes = (f'<path d="M140 168 Q160 156 182 166" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M218 166 Q240 156 260 168" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
            + eye(162, 194, 19, 3) + eye(238, 194, 19, -1))
    if shades:
        eyes = (f'<path d="M126 182 Q160 172 190 182 Q192 214 164 218 Q130 216 126 182 Z" fill="{INK}"/>'
                f'<path d="M210 182 Q240 172 274 182 Q270 216 236 218 Q208 214 210 182 Z" fill="{INK}"/>'
                f'<path d="M188 186 Q200 180 212 186" fill="none" stroke="{INK}" stroke-width="7"/>'
                f'<path d="M140 190 L158 184 M224 190 L242 184" stroke="{LIME}" stroke-width="5" stroke-linecap="round"/>')
    return f'''
<circle cx="116" cy="118" r="36" fill="{FUR}" stroke="{INK}" stroke-width="6"/><circle cx="116" cy="118" r="17" fill="{MUZ}"/>
<circle cx="284" cy="118" r="36" fill="{FUR}" stroke="{INK}" stroke-width="6"/><circle cx="284" cy="118" r="17" fill="{MUZ}"/>
<path d="M92 205 Q92 108 200 102 Q308 108 308 205 Q306 300 200 304 Q94 300 92 205 Z" fill="{FUR}" stroke="{INK}" stroke-width="6"/>
<ellipse cx="160" cy="148" rx="46" ry="22" fill="{FUR2}" opacity=".7"/>
<ellipse cx="200" cy="250" rx="56" ry="42" fill="{MUZ}" stroke="{INK}" stroke-width="4"/>
<ellipse cx="140" cy="240" rx="16" ry="10" fill="#d9776a" opacity=".45"/><ellipse cx="260" cy="240" rx="16" ry="10" fill="#d9776a" opacity=".45"/>
{eyes}
<path d="M182 230 Q200 220 218 230 Q216 248 200 252 Q184 248 182 230 Z" fill="{INK}"/>
<ellipse cx="193" cy="231" rx="6" ry="3.5" fill="#fff" opacity=".8"/>
<path d="M170 262 Q200 296 230 262 Q200 274 170 262 Z" fill="#7d2a26" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<path d="M188 267 L188 276 L198 276 L198 268" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
{cap_svg if cap_svg is not None else cap(200, 142, 1.06, -3)}'''


def bear_body():
    return f'''
<path d="M70 400 Q66 318 130 300 Q200 330 270 300 Q334 318 330 400 Z" fill="{G}" stroke="{INK}" stroke-width="6"/>
<path d="M152 304 Q200 336 248 304 L240 296 Q200 322 160 296 Z" fill="{LIME}" stroke="{INK}" stroke-width="4"/>
<circle cx="200" cy="362" r="26" fill="{LIME}" stroke="{INK}" stroke-width="4"/>
<text x="200" y="370" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="20" fill="{G}">CP</text>'''


def backwards_cap():
    return f'''<g transform="translate(200 142) rotate(4)">
  <path d="M-94 2 Q-88 -84 0 -90 Q88 -84 94 2 Z" fill="{G}" stroke="{INK}" stroke-width="5"/>
  <path d="M-60 -6 Q0 -18 60 -6 L52 6 Q0 -4 -52 6 Z" fill="{G2}" stroke="{INK}" stroke-width="4"/>
  <rect x="-22" y="-14" width="44" height="12" rx="4" fill="{LIME}" stroke="{INK}" stroke-width="3"/>
  <path d="M60 -70 Q120 -96 150 -70 Q120 -56 86 -52 Z" fill="{LIME}" stroke="{INK}" stroke-width="5"/>
  <circle cx="0" cy="-92" r="7" fill="{LIME}" stroke="{INK}" stroke-width="3"/>
</g>'''


def thumbs_up():
    return f'''{bear_body()}
{outlined("M300 362 Q336 340 342 290", FUR)}
<rect x="322" y="200" width="24" height="56" rx="12" transform="rotate(-12 334 228)" fill="{FUR}" stroke="{INK}" stroke-width="6"/>
<rect x="316" y="238" width="62" height="52" rx="18" fill="{FUR}" stroke="{INK}" stroke-width="6"/>
<path d="M346 252 L376 252 M346 264 L376 264 M346 276 L374 276" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
{bear_head()}'''


def with_rake():
    tines = ''.join(f'<path d="M{x} 70 L{x - 4} 102" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>' for x in range(22, 112, 14))
    return f'''<g transform="rotate(-8 70 230)">
<path d="M66 70 L74 380" stroke="{INK}" stroke-width="16" stroke-linecap="round"/><path d="M66 70 L74 380" stroke="#c08a4a" stroke-width="9" stroke-linecap="round"/>
<path d="M16 60 Q66 44 116 60 L112 74 Q66 60 20 74 Z" fill="{LIME}" stroke="{INK}" stroke-width="5"/>{tines}</g>
{bear_body()}
{outlined("M120 340 Q90 320 86 290", FUR)}
<circle cx="84" cy="282" r="28" fill="{FUR}" stroke="{INK}" stroke-width="6"/>
{bear_head()}'''


def cool():
    return f'''{bear_body()}
{outlined("M300 352 Q338 330 338 300", FUR)}
<circle cx="338" cy="290" r="27" fill="{FUR}" stroke="{INK}" stroke-width="6"/>
<path d="M330 268 L318 226 M346 268 L356 226" stroke="{INK}" stroke-width="18" stroke-linecap="round"/>
<path d="M330 268 L318 226 M346 268 L356 226" stroke="{FUR}" stroke-width="8" stroke-linecap="round"/>
{bear_head(shades=True, cap_svg=backwards_cap())}'''


def badge():
    return f'''<defs><path id="ring" d="M200 200 m-150 0 a150 150 0 1 1 300 0 a150 150 0 1 1 -300 0"/></defs>
<circle cx="200" cy="200" r="190" fill="{G}" stroke="{INK}" stroke-width="8"/>
<circle cx="200" cy="200" r="122" fill="#e9f6df" stroke="{LIME}" stroke-width="8"/>
<text font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="30" fill="{LIME}" letter-spacing="2">
<textPath href="#ring" startOffset="0" textLength="900" lengthAdjust="spacing">CAROLINA PREMIER ✦ LAWN &amp; TREE ✦ APEX, NC ✦</textPath></text>
<g transform="translate(200 214) scale(.58) translate(-200 -205)">{bear_head()}</g>'''


BEAR = [
    ('Thumbs up', 'Main website version: friendly and confident. Works in the home page banner and beside the Free Estimate button.', thumbs_up()),
    ('Ready to work', 'Holding a rake, for yard cleanups, mulch and landscaping pages, plus social posts.', with_rake()),
    ('Cool Jer', 'Backwards cap and shades. The fun version for Instagram, stickers and the back of shirts.', cool()),
    ('Badge', 'Round emblem for shirts, hats, truck doors and your profile picture.', badge()),
]


def build_bear():
    cards = '\n'.join(f'''<div class="card"><div class="art"><svg viewBox="0 0 400 400" role="img" aria-label="Big Jer {name}">{svg}</svg></div>
<div class="txt"><span class="num">Version {i + 1}</span><h2>{name}</h2><p>{desc}</p></div></div>''' for i, (name, desc, svg) in enumerate(BEAR))
    html = PAGE.replace('<h1>Mascot concepts</h1>', '<h1>Big Jer the Bear</h1>').replace(
        PAGE[PAGE.index('<p class="intro">'):PAGE.index('</p>', PAGE.index('<p class="intro">')) + 4],
        '<p class="intro">Your chosen mascot, refined: bigger expression, eyebrows, a grin and a Carolina Premier shirt and cap. Four versions for different uses. These are drafts to brief an illustrator, or to use as-is on the site. <a href="../">← All concepts</a></p>')
    out = ROOT / 'concepts' / 'mascots' / 'big-jer' / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html.replace('CARDS', cards))
    print('built big jer')
