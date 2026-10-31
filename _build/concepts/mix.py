"""Concept E: Premier Mix (home page mockup). Blends the original site (black + lime, Lilita One,
spinning badge, grass edge, ticker) with concept D (deep green + yellow, Barlow Condensed, brush
underlines, outlined buttons, photo cards, dashed process). Nunito body text."""
from common import B, TEL, SMS, SERVICES, TOWNS, HOME_FAQS, e, img, write, write_static

C = 'premier-mix'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Lilita+One&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">'

BRUSH = '<svg class="brush" viewBox="0 0 300 14" preserveAspectRatio="none" aria-hidden="true"><path d="M2 9 C 60 4, 120 6, 180 4 S 270 3, 298 6 L 296 9 C 240 8, 200 10, 140 10 S 40 12, 4 12 Z" fill="currentColor"/><path d="M190 11 L 260 9 L 262 10 L 192 12 Z M 230 4 L 290 3 L 291 4 L 232 5 Z" fill="currentColor" opacity=".6"/></svg>'

GRASS = ('<div class="grass" aria-hidden="true"><svg viewBox="0 0 1440 60" preserveAspectRatio="none"><path fill="#86cf45" d="M0 60 L0 34 '
         + ' '.join(f'L{x} {y}' for x, y in zip(range(8, 1440, 8), [18, 32, 8, 30, 14, 32, 4, 30, 16, 34, 10, 32, 20, 34, 6, 30, 18, 34, 12, 32, 22, 34] * 9))
         + ' L1440 34 L1440 60 Z"/></svg></div>')

BADGE = '''<div class="badge" aria-hidden="true">
  <svg viewBox="0 0 200 200"><defs><path id="circ" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs>
  <text><textPath href="#circ" textLength="486" lengthAdjust="spacing">5-STAR RATED ✦ 100% INSURED ✦ APEX, NC ✦ </textPath></text></svg>
  <span>5.0<small>★★★★★</small></span>
</div>'''

CSS = r''':root { --black: #0b0f0c; --black-2: #141b16; --green: #0a4d24; --green-2: #0e5f2d; --green-3: #073a1b; --lime: #86cf45; --lime-d: #5e9e2a; --yellow: #ffc20e; --ink: #101a13; --muted: #55625a; --off: #f2f7ee; --fun: "Lilita One", "Arial Rounded MT Bold", sans-serif; --cond: "Barlow Condensed", Impact, sans-serif; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: #fff; color: var(--ink); font: 400 1.06rem/1.7 Nunito, system-ui, sans-serif; }
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; }
h1, h2, h3 { font-family: var(--cond); font-weight: 800; text-transform: uppercase; line-height: 1; margin: 0 0 .3em; letter-spacing: .005em; }
/* the playful accent: rounded Lilita One, lime, slightly skewed */
.pop { font-family: var(--fun); font-weight: 400; text-transform: none; color: var(--lime); display: inline-block; transform: rotate(-2deg) skewX(-6deg); letter-spacing: 0; }
.on-light .pop { color: var(--lime-d); }
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 20px; }
.brush { display: block; width: 240px; height: 14px; color: var(--lime); margin: 8px 0 24px; }
.center { text-align: center; }
.center .brush { margin-left: auto; margin-right: auto; }
.title { font-size: clamp(2.5rem, 5.8vw, 4.2rem); color: var(--green); }
.dark .title, .green .title { color: #fff; }
.sub { color: var(--muted); font-size: 1.12rem; max-width: 62ch; margin: 0; }
.center .sub { margin: 0 auto; }
.dark .sub, .green .sub { color: #cfe0cc; }

.btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 17px 32px; border-radius: 16px; font: 900 1rem Nunito, sans-serif; text-transform: uppercase; letter-spacing: .1em; text-decoration: none; cursor: pointer; border: 0; transition: transform .15s, background .15s; }
.btn:hover { transform: translateY(-2px) rotate(-1deg); }
.btn-green { background: var(--green); color: #fff; box-shadow: 0 0 0 4px var(--lime); }
.btn-green:hover { background: var(--green-2); }
.btn-yellow { background: var(--yellow); color: var(--green-3); box-shadow: 0 6px 0 #c99500; }
.btn-yellow:hover { background: #ffd04a; }
.btn-ghost { color: #fff; box-shadow: inset 0 0 0 3px #fff; }
.btn-ghost:hover { background: #fff; color: var(--green-3); }
.actions { display: flex; flex-wrap: wrap; gap: 18px; margin-top: 30px; }
.center .actions { justify-content: center; }

/* top bar + header */
.topbar { display: grid; grid-template-columns: 1fr 1fr; font: 900 .84rem Nunito, sans-serif; text-transform: uppercase; letter-spacing: .08em; }
.topbar a { padding: 10px; text-align: center; text-decoration: none; white-space: nowrap; }
.topbar a:first-child { background: var(--yellow); color: var(--green-3); }
.topbar a:last-child { background: var(--black); color: #fff; }
.hdr { position: sticky; top: 0; z-index: 30; background: var(--green); }
.hdr::after { content: ""; display: block; height: 6px; background: linear-gradient(90deg, var(--yellow) 0 18%, var(--lime) 18% 100%); }
.hdr .wrap { display: flex; align-items: center; justify-content: space-between; height: 88px; gap: 20px; }
.hdr .logo { display: block; background: var(--black); border: 3px solid var(--lime); border-radius: 14px; padding: 4px 10px; transform: rotate(-1.5deg); }
.hdr .logo img { width: 112px; }
.nav { display: flex; align-items: center; gap: 26px; }
.nav a { color: #fff; text-decoration: none; font-family: var(--cond); font-weight: 700; font-size: 1.25rem; text-transform: uppercase; letter-spacing: .04em; }
.nav a:hover { color: var(--lime); }
.nav .btn { font-size: .88rem; padding: 12px 20px; box-shadow: 0 4px 0 #c99500; }
.menu { display: none; width: 56px; height: 50px; background: var(--black); border: 3px solid var(--lime); border-radius: 12px; color: #fff; }

/* hero: original layout + badge, D buttons and brush */
.hero { position: relative; color: #fff; background: var(--black) center / cover no-repeat; min-height: 640px; display: flex; align-items: center; }
.hero::before { content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(5, 12, 7, .94) 0%, rgba(7, 40, 20, .78) 50%, rgba(7, 40, 20, .35) 100%); }
.hero .wrap { position: relative; width: 100%; padding-top: 80px; padding-bottom: 160px; display: flex; align-items: center; justify-content: space-between; gap: 40px; }
.hero h1 { font-size: clamp(3rem, 6.2vw, 5.2rem); max-width: 13ch; }
.hero h1 .pop { font-size: 1.04em; }
.hero p { font-size: 1.2rem; max-width: 50ch; color: #e1ebde; margin: 0; }
.eyebrow { display: inline-block; background: var(--lime); color: var(--green-3); font: 900 .78rem Nunito, sans-serif; letter-spacing: .14em; text-transform: uppercase; padding: 6px 12px; border-radius: 8px; margin-bottom: 18px; transform: rotate(-1.5deg); }
.badge { position: relative; flex: none; width: 220px; height: 220px; }
.badge svg { width: 100%; height: 100%; animation: spin 22s linear infinite; }
.badge text { font-family: var(--fun); font-size: 17px; letter-spacing: 3px; fill: #fff; }
.badge span { position: absolute; inset: 44px; border-radius: 50%; background: var(--yellow); color: var(--green-3); display: grid; place-content: center; text-align: center; font-family: var(--fun); font-size: 2.8rem; line-height: 1; transform: rotate(-8deg); box-shadow: 0 0 0 5px var(--lime), 0 12px 30px rgba(0, 0, 0, .35); }
.badge small { font-size: .85rem; letter-spacing: 2px; margin-top: 4px; }
@keyframes spin { to { transform: rotate(360deg); } }

/* grass edge + tilted trust banner with D diamonds */
.grass { position: relative; margin-top: -86px; z-index: 2; }
.grass svg { display: block; width: 100%; height: 60px; }
.trust { background: var(--lime); padding: 0 20px 34px; }
.trust ul { list-style: none; margin: 0 auto; padding: 20px 30px; max-width: 1000px; background: var(--green); border: 4px solid #fff; color: #fff; border-radius: 20px; display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 12px 26px; font: 800 clamp(1.3rem, 2.6vw, 1.8rem) / 1 var(--cond); text-transform: uppercase; transform: translateY(-14px) rotate(-1.2deg); box-shadow: 0 16px 30px rgba(0, 0, 0, .25); }
.trust li { display: flex; align-items: center; gap: 26px; }
.trust li + li::before { content: ""; width: 12px; height: 12px; background: var(--yellow); transform: rotate(45deg); border-radius: 2px; }

/* ticker */
.ticker { background: var(--black); overflow: hidden; padding: 14px 0; border-bottom: 5px solid var(--yellow); }
.ticker-track { display: flex; width: max-content; animation: ticker 40s linear infinite; }
.ticker span { font: 800 1.7rem var(--cond); text-transform: uppercase; color: #fff; padding: 0 24px; white-space: nowrap; }
.ticker span::after { content: "✦"; color: var(--lime); margin-left: 48px; }
@keyframes ticker { to { transform: translateX(-50%); } }

section { padding: 92px 0; }
.green { background: var(--green); color: #e1ebde; }
.dark { background: var(--black); color: #e1ebde; }
.off { background: var(--off); }

/* cards (D) + lime CTA card (original) */
.cards { display: grid; gap: 24px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); margin-top: 44px; }
.card { position: relative; display: flex; align-items: flex-end; min-height: 360px; border-radius: 24px; overflow: hidden; text-decoration: none; color: #fff; background: var(--green); }
.card img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform .5s; }
.card::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10, 77, 36, 0) 28%, rgba(7, 40, 20, .96) 90%); }
.card:hover img { transform: scale(1.07) rotate(.6deg); }
.card .plus { position: absolute; z-index: 2; top: 18px; right: 18px; width: 54px; height: 54px; border-radius: 14px; background: var(--lime); border: 3px solid var(--green-3); color: var(--green-3); display: grid; place-items: center; font: 2.2rem/1 var(--fun); transition: transform .25s; }
.card:hover .plus { transform: rotate(90deg); }
.card div { position: relative; z-index: 1; padding: 24px; text-align: left; }
.card h3 { font-size: 1.85rem; margin: 0; }
.card p { margin: 6px 0 0; color: #d6e6d2; font-size: .98rem; }
.card-cta { background: var(--yellow); color: var(--green-3); transform: rotate(-1.2deg); }
.card-cta::after { content: none; }
.card-cta h3 { font-family: var(--fun); text-transform: none; font-size: 2.2rem; font-weight: 400; }
.card-cta p { color: var(--green-3); }
.card-cta .go { display: inline-block; margin-top: 14px; font-weight: 900; text-transform: uppercase; letter-spacing: .1em; font-size: .85rem; }

/* reviews: original big rotated number */
.rev { display: grid; grid-template-columns: auto 1fr; gap: 50px; align-items: center; background: var(--black-2); border: 3px solid var(--lime); border-radius: 28px; padding: 46px; }
.rev .n { font: 9rem/.85 var(--fun); color: var(--lime); transform: rotate(-5deg); display: block; }
.rev .l { font: 800 2.2rem/1 var(--cond); text-transform: uppercase; color: #fff; }
.rev .stars { color: var(--yellow); font-size: 1.8rem; letter-spacing: 5px; }
.rev h2 { font-size: clamp(2.2rem, 4.4vw, 3.4rem); color: #fff; margin-top: 6px; }
.rev p { color: #cfe0cc; }

/* why us split */
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
.photo { border-radius: 26px; border: 6px solid var(--lime); overflow: hidden; transform: rotate(1.5deg); box-shadow: -14px 14px 0 var(--green); }
.photo img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
.ticks { list-style: none; padding: 0; margin: 24px 0 0; display: grid; gap: 12px; }
.ticks li { display: flex; gap: 12px; font-weight: 800; }
.ticks li::before { content: "✓"; flex: none; width: 28px; height: 28px; border-radius: 8px; background: var(--lime); color: var(--green-3); display: grid; place-items: center; font-weight: 900; }

/* process (D) with Lilita numbers */
.process { max-width: 860px; margin: 44px auto 0; border-left: 5px dashed var(--lime); padding-left: 34px; display: grid; gap: 8px; }
.process details { padding: 12px 0; }
.process summary { cursor: pointer; list-style: none; display: flex; align-items: center; gap: 20px; }
.process summary::-webkit-details-marker { display: none; }
.process .n { font: 3rem/1 var(--fun); color: var(--yellow); -webkit-text-stroke: 2px var(--green-3); paint-order: stroke fill; transform: rotate(-4deg); }
.process h3 { font-size: 2rem; color: #fff; margin: 0; }
.process p { margin: 10px 0 0; color: #cfe0cc; font-size: 1.1rem; }

/* towns */
.towns { display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; margin-top: 34px; }
.towns a { background: #fff; border: 3px solid var(--green); color: var(--green); border-radius: 14px; padding: 10px 22px; font: 800 1.45rem var(--cond); text-transform: uppercase; text-decoration: none; box-shadow: 4px 4px 0 var(--lime); transition: transform .15s, background .15s; }
.towns a:hover { background: var(--lime); transform: rotate(-2deg); }

/* faq */
.faq { max-width: 900px; margin: 40px auto 0; display: grid; gap: 14px; }
.faq details { border: 3px solid var(--green); border-radius: 16px; padding: 0 22px; background: #fff; }
.faq summary { cursor: pointer; list-style: none; padding: 18px 0; font-weight: 800; font-size: 1.12rem; color: var(--green); display: flex; justify-content: space-between; gap: 16px; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; flex: none; width: 32px; height: 32px; border-radius: 9px; background: var(--lime); color: var(--green-3); display: grid; place-items: center; font: 1.5rem/1 var(--fun); transition: transform .2s; }
.faq details[open] summary::after { transform: rotate(45deg); }
.faq p { margin: 0 0 20px; color: var(--muted); }

/* cta band (original lime) */
.cta { background: var(--lime); padding: 76px 0; }
.cta .wrap { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 20px; }
.cta h2 { font-size: clamp(2.4rem, 5.4vw, 4rem); color: var(--green-3); margin: 0; }
.cta h2 .pop { color: #fff; -webkit-text-stroke: 2px var(--green-3); paint-order: stroke fill; }
.cta .brush { color: var(--green-3); }
.cta p { margin: 0; font-weight: 800; color: var(--green-3); }

/* footer */
.ftr { background: var(--black); color: #b9c9b6; padding: 0 0 100px; }
.ftr::before { content: ""; display: block; height: 6px; background: linear-gradient(90deg, var(--lime) 0 80%, var(--yellow) 80% 100%); margin-bottom: 70px; }
.ftr .grid { display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 40px; }
.ftr .logo img { width: 170px; }
.ftr h4 { font: 800 1.5rem var(--cond); text-transform: uppercase; color: var(--lime); margin: 0 0 12px; }
.ftr ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 7px; }
.ftr .tel { font: 2.1rem var(--fun); color: var(--yellow); text-decoration: none; }
.ftr .copy { margin-top: 50px; border-top: 1px solid rgba(255, 255, 255, .1); padding-top: 22px; font-size: .88rem; }

.mbar { display: none; position: fixed; left: 0; right: 0; bottom: 0; z-index: 40; grid-template-columns: 1fr 1fr; }
.mbar a { padding: 16px; text-align: center; font: 1.15rem var(--fun); text-decoration: none; }
.mbar a:first-child { background: var(--green); color: #fff; }
.mbar a:last-child { background: var(--yellow); color: var(--green-3); }

.rv { opacity: 0; transform: translateY(24px); transition: opacity .6s, transform .6s; }
.rv.in { opacity: 1; transform: none; }
.photo.rv.in { transform: rotate(1.5deg); }
.card-cta.rv.in { transform: rotate(-1.2deg); }
@media (prefers-reduced-motion: reduce) { .rv { opacity: 1; transform: none; transition: none; } .badge svg, .ticker-track { animation: none; } }

@media (max-width: 1020px) {
  .menu { display: grid; place-items: center; }
  .nav { display: none; position: absolute; top: 94px; left: 0; right: 0; background: var(--green); flex-direction: column; align-items: stretch; gap: 0; padding: 6px 20px 24px; border-bottom: 6px solid var(--lime); }
  .nav.open { display: flex; }
  .nav a { padding: 14px 0; border-bottom: 1px solid rgba(255, 255, 255, .12); font-size: 1.5rem; }
  .nav .btn { margin-top: 16px; }
  .split, .rev { grid-template-columns: 1fr; }
  .badge { display: none; }
  .mbar { display: grid; }
  .ftr .grid { grid-template-columns: 1fr; }
}
@media (max-width: 620px) {
  section { padding: 70px 0; }
  .topbar { font-size: .7rem; }
  .hero { min-height: 0; }
  .hero .wrap { padding-top: 60px; padding-bottom: 140px; }
  .actions .btn { width: 100%; }
  .trust ul { flex-direction: column; gap: 10px; }
  .trust li { flex-direction: column; gap: 10px; }
  .rev { padding: 30px; gap: 16px; }
  .rev .n { font-size: 6.5rem; }
  .process { padding-left: 22px; }
  .process .n { font-size: 2.4rem; }
  .process h3 { font-size: 1.6rem; }
}
'''

STEPS = [
    ('Free Estimate', 'Call, text or request a quote online. We look at your property, talk through what you want and give you a clear, upfront price.'),
    ('Scheduling', 'Pick a date for your project, or set up weekly or bi-weekly service for ongoing care.'),
    ('The Work', 'Our crew handles it start to finish, done right for Triangle clay and weather.'),
    ('Clean Up & Enjoy', 'We clean up, haul away the debris and leave the property looking sharp.'),
]


def home():
    cards = ''.join(f'''<a class="card rv" href="#">{img(s["img"] + ".jpg", s["name"])}<span class="plus" aria-hidden="true">+</span>
  <div><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p></div></a>''' for s in SERVICES)
    cards += '''<a class="card card-cta rv" href="#"><div><h3>Not sure what you need?</h3><p>Tell us about your property and we'll put together a free estimate.</p><span class="go">Get a free quote →</span></div></a>'''
    ticker = ''.join(f'<span>{e(s["name"])}</span>' for s in SERVICES)
    steps = ''.join(f'<details class="rv"{" open" if i == 0 else ""}><summary><span class="n">{i + 1:02d}</span><h3>{t}</h3></summary><p>{e(d)}</p></details>'
                    for i, (t, d) in enumerate(STEPS))
    towns = ''.join(f'<a href="#">{t["name"]}</a>' for t in TOWNS)
    faqs = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in HOME_FAQS)
    body = f'''<div class="topbar"><a href="#">Get a Free Quote</a><a href="{TEL}">Call {B["phone"]}</a></div>
<header class="hdr"><div class="wrap">
  <a class="logo" href="./"><img src="~~/images/logo.png" alt="Carolina Premier Lawn and Tree Services" width="286" height="150"></a>
  <button class="menu" data-menu aria-expanded="false" aria-label="Menu"><svg width="26" height="22" viewBox="0 0 26 22" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round"><path d="M2 3h22M2 11h22M2 19h22"/></svg></button>
  <nav class="nav" data-nav><a href="#">Services</a><a href="#">Areas</a><a href="#">Projects</a><a href="#">Reviews</a><a href="#">About</a><a class="btn btn-yellow" href="#">Free Quote</a></nav>
</div></header>
<main>
<section class="hero" style="background-image:url('~~/images/hero-home.jpg')"><div class="wrap">
  <div>
    <span class="eyebrow">Lawn · Landscape · Trees</span>
    <h1>Lawn, Landscape &amp; Tree Pros in <span class="pop">Apex, NC</span></h1>{BRUSH}
    <p>Lawn care, landscaping, tree work, hardscaping, fencing and even Christmas lights. One local, 100% insured crew for everything outside.</p>
    <div class="actions"><a class="btn btn-green" href="#">Get a Free Quote</a><a class="btn btn-yellow" href="#">View Services</a></div>
  </div>
  {BADGE}
</div></section>
{GRASS}
<div class="trust"><ul><li>100% Insured</li><li>5 Stars on Google</li><li>Homes, HOAs &amp; Businesses</li></ul></div>
<div class="ticker" aria-hidden="true"><div class="ticker-track">{ticker}{ticker}</div></div>

<section class="on-light"><div class="wrap center">
  <h2 class="title">Our <span class="pop">Services</span></h2>{BRUSH}
  <p class="sub">From the weekly mow to a new patio, one call covers everything outside your home.</p>
  <div class="cards">{cards}</div>
</div></section>

<section class="dark"><div class="wrap"><div class="rev rv">
  <div><span class="n">{B["review_count"]}</span><span class="l">5-Star<br>Google Reviews</span></div>
  <div><div class="stars">★★★★★</div><h2>Top-rated by our <span class="pop">neighbors</span></h2>
  <p>Every customer who reviewed us on Google gave us five stars.</p><div class="actions"><a class="btn btn-yellow" href="#">Read Reviews</a></div></div>
</div></div></section>

<section class="on-light"><div class="wrap split">
  <div class="rv"><h2 class="title">One crew. <span class="pop">Zero hassle.</span></h2>{BRUSH}
    <p class="sub">Skip juggling a mowing company, a tree guy and a landscaper. We know Triangle yards (red clay, July heat and fescue that needs real care every fall), and we handle it all.</p>
    <ul class="ticks"><li>100% insured on every job</li><li>Rated 5.0 by every Google reviewer</li><li>Free, upfront estimates</li><li>Local to Apex</li></ul>
    <div class="actions"><a class="btn btn-green" href="#">About Us</a></div></div>
  <div class="photo rv">{img("garden-path.jpg", "Landscaped garden path")}</div>
</div></section>

<section class="green"><div class="wrap">
  <div class="center"><h2 class="title">How It <span class="pop">Works</span></h2>{BRUSH}<div class="actions"><a class="btn btn-yellow" href="#">Get a Free Quote</a></div></div>
  <div class="process">{steps}</div>
</div></section>

<section class="off on-light"><div class="wrap center">
  <h2 class="title">Areas We <span class="pop">Serve</span></h2>{BRUSH}
  <p class="sub">Based in Apex, serving homes, HOAs and businesses across southwest Wake County.</p>
  <div class="towns">{towns}</div>
</div></section>

<section class="on-light"><div class="wrap center"><h2 class="title">Got <span class="pop">Questions?</span></h2>{BRUSH}<div class="faq" style="text-align:left">{faqs}</div></div></section>

<section class="cta"><div class="wrap">
  <div><h2>Ready for a <span class="pop">better yard?</span></h2>{BRUSH}<p>Free estimates across Apex and the Triangle.</p></div>
  <div class="actions" style="margin:0"><a class="btn btn-green" href="#">Get a Free Quote</a><a class="btn btn-yellow" href="{TEL}">Call {B["phone"]}</a></div>
</div></section>
</main>
<footer class="ftr"><div class="wrap">
  <div class="grid">
    <div><a class="logo" href="./"><img src="~~/images/logo.png" alt="Carolina Premier" width="286" height="150"></a>
      <p>Lawn care, landscaping, tree work, hardscaping and fencing across Apex and the Triangle. 100% insured.</p><a class="tel" href="{TEL}">{B["phone"]}</a></div>
    <div><h4>Services</h4><ul>{''.join(f"<li>{e(s['name'])}</li>" for s in SERVICES)}</ul></div>
    <div><h4>Service Areas</h4><ul>{''.join(f"<li>{t['name']}, NC</li>" for t in TOWNS)}</ul></div>
  </div>
  <div class="copy">© 2026 {e(B["name"])} · Design concept E: Premier Mix (home page mockup)</div>
</div></footer>
<div class="mbar"><a href="{TEL}">Call Now</a><a href="{SMS}">Text Us</a></div>'''
    write(C, '', 'Carolina Premier | Concept E mockup', body, FONTS)


def build():
    write_static(C, CSS)
    home()
    print('built', C)
