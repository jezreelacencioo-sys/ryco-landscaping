"""Concept B: Carolina Blue. Clean, trustworthy, conversion-first. Navy + Carolina blue + grass green, Archivo."""
from common import B, TEL, SMS, SERVICES, TOWNS, HOME_FAQS, NAV, e, img, write, write_static

C = 'carolina-blue'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">'

ICONS = {
    'lawn-care': '<path d="M3 20h18M5 20c1-4 1-8 0-12M9 20c0-5 1-9 3-13M14 20c0-4-1-8-3-11M18 20c1-5 0-9-2-12"/>',
    'landscaping': '<path d="M12 21V11M12 11c-4 0-6-3-6-7 4 0 6 3 6 7zM12 14c3 0 5-2 5-6-3 0-5 2-5 6zM5 21h14"/>',
    'tree-services': '<path d="M12 21v-6M7 15h10l-5-12-5 12zM8 21h8"/>',
    'hardscaping': '<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 10h18M3 15h18M9 4v6M15 10v5M9 15v5"/>',
    'fencing': '<path d="M5 21V7l2-3 2 3v14M15 21V7l2-3 2 3v14M3 10h18M3 16h18"/>',
    'christmas-lights': '<path d="M2 6c5 4 15 4 20 0"/><path d="M6 8.5v2M12 9.5v2M18 8.5v2"/><circle cx="6" cy="13" r="2"/><circle cx="12" cy="14" r="2"/><circle cx="18" cy="13" r="2"/>',
    'commercial-hoa': '<path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6"/>',
}


def icon(slug, size=28):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[slug]}</svg>'


CSS = r''':root { --navy: #0f2a44; --navy-2: #173b5e; --blue: #7bafd4; --blue-l: #e8f2fa; --green: #2e8c3e; --green-d: #23702f; --ink: #142233; --muted: #5a6878; --line: #e2e8ee; --bg: #f7fafc; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: #fff; color: var(--ink); font: 400 1.03rem/1.65 Archivo, system-ui, sans-serif; }
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; }
h1, h2, h3 { font-weight: 800; line-height: 1.1; margin: 0 0 .45em; letter-spacing: -.02em; }
.wrap { max-width: 1200px; margin: 0 auto; padding: 0 22px; }
.tag { display: inline-flex; align-items: center; gap: 8px; background: var(--blue-l); color: var(--navy-2); font-weight: 700; font-size: .82rem; padding: 6px 12px; border-radius: 999px; margin-bottom: 16px; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 15px 24px; border-radius: 10px; font-weight: 700; text-decoration: none; border: 0; cursor: pointer; font-family: inherit; font-size: 1rem; transition: background .15s, transform .15s, box-shadow .15s; }
.btn:hover { transform: translateY(-1px); }
.btn-green { background: var(--green); color: #fff; box-shadow: 0 6px 16px rgba(46, 140, 62, .3); }
.btn-green:hover { background: var(--green-d); }
.btn-navy { background: var(--navy); color: #fff; }
.btn-ghost { background: #fff; color: var(--navy); border: 2px solid var(--line); }
.actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 26px; }

/* utility bar + header */
.util { background: var(--navy); color: #cfe0ee; font-size: .85rem; }
.util .wrap { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-top: 9px; padding-bottom: 9px; }
.util b { color: #ffd166; letter-spacing: 2px; }
.util a { color: #fff; font-weight: 700; text-decoration: none; }
.hdr { position: sticky; top: 0; z-index: 20; background: #fff; border-bottom: 1px solid var(--line); box-shadow: 0 2px 12px rgba(15, 42, 68, .05); }
.hdr .wrap { display: flex; align-items: center; justify-content: space-between; height: 80px; gap: 20px; }
.hdr .logo img { width: 124px; }
.nav { display: flex; align-items: center; gap: 26px; }
.nav a { text-decoration: none; font-weight: 600; color: var(--navy); }
.nav a:hover, .nav a[aria-current] { color: var(--green); }
.nav .phone { font-weight: 800; }
.nav .btn { color: #fff; padding: 12px 20px; }
.menu { display: none; background: var(--navy); color: #fff; border: 0; border-radius: 10px; padding: 10px 16px; font: 700 .9rem Archivo, sans-serif; }

/* hero */
.hero { background: linear-gradient(135deg, var(--blue-l) 0%, #fff 60%); padding: 64px 0 80px; position: relative; overflow: hidden; }
.hero::after { content: ""; position: absolute; right: -180px; top: -180px; width: 520px; height: 520px; border-radius: 50%; background: var(--blue); opacity: .18; }
.hero .wrap { display: grid; grid-template-columns: 1.15fr .85fr; gap: 56px; align-items: center; position: relative; z-index: 1; }
.hero h1 { font-size: clamp(2.6rem, 5.4vw, 4.4rem); color: var(--navy); }
.hero h1 span { color: var(--green); }
.hero .lead { font-size: 1.2rem; color: var(--muted); max-width: 50ch; }
.checks { list-style: none; padding: 0; margin: 22px 0 0; display: grid; grid-template-columns: 1fr 1fr; gap: 10px 20px; }
.checks li { display: flex; gap: 10px; align-items: center; font-weight: 600; }
.checks li::before { content: "✓"; flex: none; width: 24px; height: 24px; border-radius: 50%; background: var(--green); color: #fff; display: grid; place-items: center; font-size: .8rem; font-weight: 900; }
.quote { background: #fff; border-radius: 18px; padding: 30px; box-shadow: 0 24px 60px rgba(15, 42, 68, .16); border-top: 6px solid var(--green); display: grid; gap: 14px; }
.quote h2 { font-size: 1.6rem; margin: 0; color: var(--navy); }
.quote p.sub { margin: -6px 0 4px; color: var(--muted); font-size: .95rem; }
.quote label { display: grid; gap: 5px; font-weight: 700; font-size: .85rem; color: var(--navy); }
.quote input, .quote select, .quote textarea { font: inherit; padding: 12px 14px; border: 1.5px solid var(--line); border-radius: 10px; background: var(--bg); }
.quote input:focus, .quote select:focus, .quote textarea:focus { outline: none; border-color: var(--blue); box-shadow: 0 0 0 3px rgba(123, 175, 212, .3); }
.quote .row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.quote label, .quote .row > * { min-width: 0; }
.quote input, .quote select, .quote textarea { width: 100%; }
.quote .fine { font-size: .82rem; color: var(--muted); margin: 0; text-align: center; }

/* trust row */
.trust { border-bottom: 1px solid var(--line); }
.trust .wrap { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; padding-top: 26px; padding-bottom: 26px; }
.trust div { display: flex; align-items: center; gap: 14px; }
.trust .ic { flex: none; width: 48px; height: 48px; border-radius: 12px; background: var(--blue-l); color: var(--navy-2); display: grid; place-items: center; font-weight: 900; font-size: 1.1rem; }
.trust b { display: block; color: var(--navy); }
.trust span { font-size: .9rem; color: var(--muted); }

section { padding: 88px 0; }
.bg { background: var(--bg); }
.navy { background: var(--navy); color: #fff; }
.head { max-width: 700px; margin-bottom: 44px; }
.head.c { text-align: center; margin-left: auto; margin-right: auto; }
.head h2 { font-size: clamp(2rem, 4vw, 3rem); color: var(--navy); }
.navy .head h2 { color: #fff; }
.head p { color: var(--muted); font-size: 1.1rem; margin: 0; }
.navy .head p { color: #b8cde0; }

/* service cards */
.cards { display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); }
.card { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 28px; text-decoration: none; display: flex; flex-direction: column; transition: box-shadow .2s, transform .2s, border-color .2s; }
.card:hover { transform: translateY(-4px); box-shadow: 0 18px 40px rgba(15, 42, 68, .12); border-color: var(--blue); }
.card .ic { width: 54px; height: 54px; border-radius: 14px; background: var(--blue-l); color: var(--navy-2); display: grid; place-items: center; margin-bottom: 18px; }
.card h3 { font-size: 1.35rem; color: var(--navy); }
.card p { color: var(--muted); margin: 0 0 16px; }
.card ul { list-style: none; padding: 0; margin: 0 0 18px; display: grid; gap: 6px; font-size: .93rem; }
.card li::before { content: "• "; color: var(--green); font-weight: 900; }
.card .go { margin-top: auto; font-weight: 800; color: var(--green); }

/* steps */
.steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; position: relative; }
.steps::before { content: ""; position: absolute; top: 30px; left: 16%; right: 16%; height: 3px; background: repeating-linear-gradient(90deg, var(--blue) 0 10px, transparent 10px 18px); }
.step { text-align: center; position: relative; }
.step .num { width: 62px; height: 62px; border-radius: 50%; background: var(--green); color: #fff; font-weight: 900; font-size: 1.5rem; display: grid; place-items: center; margin: 0 auto 18px; box-shadow: 0 0 0 8px #fff; }
.step h3 { color: var(--navy); font-size: 1.3rem; }
.step p { color: var(--muted); margin: 0; }

/* stats */
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center; }
.stats b { display: block; font-size: clamp(2.6rem, 5vw, 3.8rem); font-weight: 900; color: var(--blue); line-height: 1; margin-bottom: 8px; }
.stats span { color: #cfe0ee; font-weight: 600; }

/* split */
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 56px; align-items: center; }
.split img { border-radius: 18px; width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
.map { width: 100%; height: 380px; border: 0; border-radius: 18px; }
.chips { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
.chips span { background: #fff; border: 1.5px solid var(--line); border-radius: 999px; padding: 8px 16px; font-weight: 700; color: var(--navy); }

/* review band */
.review { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 24px; background: #fff; border: 1px solid var(--line); border-radius: 18px; padding: 34px 38px; }
.review .score { display: flex; align-items: center; gap: 18px; }
.review .score b { font-size: 3.6rem; font-weight: 900; color: var(--navy); line-height: 1; }
.review .stars { color: #f5b301; font-size: 1.4rem; letter-spacing: 3px; }

/* faq */
.faq { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.faq details { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 0 20px; }
.faq summary { cursor: pointer; padding: 18px 0; font-weight: 700; color: var(--navy); list-style: none; display: flex; justify-content: space-between; gap: 14px; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; color: var(--green); font-weight: 900; font-size: 1.3rem; line-height: 1; }
.faq details[open] summary::after { content: "–"; }
.faq p { margin: 0 0 18px; color: var(--muted); }

/* cta */
.cta { background: linear-gradient(120deg, var(--navy) 0%, var(--navy-2) 100%); color: #fff; border-radius: 22px; padding: 54px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 24px; position: relative; overflow: hidden; }
.cta::after { content: ""; position: absolute; right: -80px; bottom: -120px; width: 320px; height: 320px; border-radius: 50%; background: var(--blue); opacity: .25; }
.cta h2 { font-size: clamp(1.8rem, 3.6vw, 2.6rem); margin: 0; }
.cta p { margin: 6px 0 0; color: #cfe0ee; }
.cta .actions { margin: 0; position: relative; z-index: 1; }

/* page header */
.ph { background: linear-gradient(135deg, var(--blue-l), #fff 70%); padding: 54px 0; border-bottom: 1px solid var(--line); }
.crumbs { font-size: .88rem; color: var(--muted); margin-bottom: 18px; }
.crumbs a { text-decoration: none; color: var(--navy-2); font-weight: 600; }
.ph h1 { font-size: clamp(2.3rem, 5vw, 3.6rem); color: var(--navy); max-width: 20ch; }
.ph p { font-size: 1.15rem; color: var(--muted); max-width: 60ch; margin: 0; }
.layout { display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 50px; align-items: start; }
.side { position: sticky; top: 100px; }
.prose p { color: var(--muted); }
.prose h2 { color: var(--navy); font-size: 1.8rem; margin-top: 1.2em; }
.items { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 20px 0 10px; }
.items div { background: var(--bg); border: 1px solid var(--line); border-radius: 12px; padding: 18px 20px; }
.items b { display: block; color: var(--navy); margin-bottom: 4px; }
.items span { color: var(--muted); font-size: .95rem; }
.lead-img { border-radius: 18px; width: 100%; aspect-ratio: 16 / 8; object-fit: cover; margin-bottom: 30px; }
.one-col .faq { grid-template-columns: 1fr; }
.soon { text-align: center; max-width: 640px; margin: 0 auto; background: var(--bg); border: 2px dashed var(--line); border-radius: 18px; padding: 50px 30px; }

/* footer */
.ftr { background: var(--navy); color: #b8cde0; padding: 70px 0 34px; font-size: .95rem; }
.ftr .grid { display: grid; grid-template-columns: 1.3fr 1fr 1fr 1fr; gap: 40px; }
.ftr h4 { color: #fff; margin: 0 0 14px; font-size: 1rem; }
.ftr ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; }
.ftr a { text-decoration: none; }
.ftr a:hover { color: #fff; }
.ftr .ph-big { color: #fff; font-weight: 900; font-size: 1.5rem; }
.ftr .copy { border-top: 1px solid rgba(255, 255, 255, .12); margin-top: 44px; padding-top: 22px; font-size: .85rem; }

.rv { opacity: 0; transform: translateY(18px); transition: opacity .6s, transform .6s; }
.rv.in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .rv { opacity: 1; transform: none; transition: none; } }

@media (max-width: 1000px) {
  .menu { display: block; }
  .nav { display: none; position: absolute; top: 80px; left: 0; right: 0; background: #fff; flex-direction: column; align-items: stretch; gap: 0; padding: 8px 22px 22px; border-bottom: 1px solid var(--line); }
  .nav.open { display: flex; }
  .nav a { padding: 13px 0; border-bottom: 1px solid var(--line); }
  .nav .btn { margin-top: 12px; }
  .hero .wrap, .split, .layout { grid-template-columns: 1fr; }
  .trust .wrap, .stats { grid-template-columns: 1fr 1fr; }
  .ftr .grid { grid-template-columns: 1fr 1fr; }
  .side { position: static; }
}
@media (max-width: 640px) {
  section { padding: 64px 0; }
  .util .hide { display: none; }
  .checks, .faq, .items, .quote .row, .ftr .grid { grid-template-columns: 1fr; }
  .steps { grid-template-columns: 1fr; }
  .steps::before { display: none; }
  .cta { padding: 34px 26px; }
  .trust .wrap { grid-template-columns: 1fr; }
}
'''


def header(cur=''):
    links = ''.join(f'<a href="~/{p}"{" aria-current=page" if cur == p else ""}>{n}</a>' for p, n in NAV)
    return f'''<div class="util"><div class="wrap"><span><b>★★★★★</b> 5.0 on Google · 100% insured<span class="hide"> · Serving Apex &amp; the Triangle</span></span><a href="{TEL}">{B["phone"]}</a></div></div>
<header class="hdr"><div class="wrap">
  <a class="logo" href="~/"><img src="~~/concepts/assets/logo-navy.png" alt="Carolina Premier Lawn and Tree Services" width="286" height="150"></a>
  <button class="menu" data-menu aria-expanded="false">Menu</button>
  <nav class="nav" data-nav>{links}<a class="btn btn-green" href="~/contact/">Free Quote</a></nav>
</div></header>
<main>'''


def footer():
    svc = ''.join(f'<li><a href="~/services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    towns = ''.join(f'<li>{t["name"]}, NC</li>' for t in TOWNS)
    return f'''</main>
<footer class="ftr"><div class="wrap">
  <div class="grid">
    <div><h4>Carolina Premier Lawn &amp; Tree Services LLC</h4><p>Apex, NC · 100% insured · 5.0 on Google</p><a class="ph-big" href="{TEL}">{B["phone"]}</a></div>
    <div><h4>Services</h4><ul>{svc}</ul></div>
    <div><h4>Service areas</h4><ul>{towns}</ul></div>
    <div><h4>Company</h4><ul><li><a href="~/about/">About</a></li><li><a href="~/projects/">Projects</a></li><li><a href="~/reviews/">Reviews</a></li><li><a href="~/contact/">Contact</a></li></ul></div>
  </div>
  <div class="copy">© 2026 {e(B["name"])} · Design concept B: Carolina Blue</div>
</div></footer>'''


def quote_form(title='Get your free quote'):
    opts = ''.join(f'<option>{e(s["name"])}</option>' for s in SERVICES)
    towns = ''.join(f'<option>{t["name"]}</option>' for t in TOWNS)
    return f'''<form class="quote" data-sms>
  <h2>{title}</h2><p class="sub">Takes 30 seconds. No obligation.</p>
  <label>Name<input name="Name" required autocomplete="name"></label>
  <label>Property address<input name="Address" required autocomplete="street-address"></label>
  <div class="row"><label>Town<select name="Town">{towns}<option>Other</option></select></label>
  <label>Service<select name="Service">{opts}</select></label></div>
  <button class="btn btn-green" type="submit">Send my request</button>
  <p class="fine">Opens a text to us with your details. Or call <a href="{TEL}">{B["phone"]}</a>.</p>
</form>'''


def cards(services):
    return '<div class="cards">' + ''.join(f'''<a class="card rv" href="~/services/{s["slug"]}/">
  <div class="ic">{icon(s["slug"])}</div><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p>
  <ul>{''.join(f"<li>{e(n)}</li>" for n, _ in s["items"][:3])}</ul><span class="go">See details →</span></a>''' for s in services) + '</div>'


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items) + '</div>'


def review_band():
    return f'''<div class="review rv"><div class="score"><b>5.0</b><div><div class="stars">★★★★★</div><div>{B["review_count"]} Google reviews · every one 5 stars</div></div></div>
<a class="btn btn-navy" href="~/reviews/">Read reviews</a></div>'''


def cta():
    return f'''<section><div class="wrap"><div class="cta rv"><div><h2>Ready for a free quote?</h2><p>Call, text or send a request. We'll get back to you with a clear price.</p></div>
<div class="actions"><a class="btn btn-green" href="~/contact/">Get my free quote</a><a class="btn btn-ghost" href="{TEL}">Call {B["phone"]}</a></div></div></div></section>'''


def ph(crumb, h1, lead):
    return f'<section class="ph"><div class="wrap"><div class="crumbs"><a href="~/">Home</a> / {crumb}</div><h1>{h1}</h1><p>{lead}</p></div></section>'


def home():
    chips = ''.join(f'<span>{t["name"]}</span>' for t in TOWNS)
    body = header() + f'''
<section class="hero"><div class="wrap">
  <div>
    <div class="tag">★ 5.0 Google rated · Apex, NC</div>
    <h1>Apex's 5-star <span>lawn, landscape &amp; tree</span> crew.</h1>
    <p class="lead">From weekly mowing to new patios, fences, tree removal and Christmas lights. One insured local company for everything outside.</p>
    <ul class="checks"><li>100% insured</li><li>Free estimates</li><li>Homes, HOAs &amp; businesses</li><li>Local to Apex</li></ul>
    <div class="actions"><a class="btn btn-navy" href="{TEL}">Call {B["phone"]}</a><a class="btn btn-ghost" href="~/services/">View services</a></div>
  </div>
  {quote_form()}
</div></section>
<div class="trust"><div class="wrap">
  <div><span class="ic">5.0</span><p style="margin:0"><b>Google rated</b><span>{B["review_count"]} five-star reviews</span></p></div>
  <div><span class="ic">✓</span><p style="margin:0"><b>100% insured</b><span>Protected on every job</span></p></div>
  <div><span class="ic">$0</span><p style="margin:0"><b>Free estimates</b><span>Clear, upfront pricing</span></p></div>
  <div><span class="ic">7</span><p style="margin:0"><b>Services</b><span>One company for it all</span></p></div>
</div></div>

<section class="bg"><div class="wrap">
  <div class="head c rv"><div class="tag">Our services</div><h2>Everything outside, handled.</h2><p>Pick a service to see exactly what's included.</p></div>
  {cards(SERVICES)}
</div></section>

<section><div class="wrap">
  <div class="head c rv"><div class="tag">How it works</div><h2>Three simple steps</h2></div>
  <div class="steps">
    <div class="step rv"><div class="num">1</div><h3>Request a quote</h3><p>Call, text or send the form with your address and what you need.</p></div>
    <div class="step rv"><div class="num">2</div><h3>Get a clear price</h3><p>We look at the job and give you a straightforward estimate.</p></div>
    <div class="step rv"><div class="num">3</div><h3>Enjoy your yard</h3><p>We do the work and leave your property clean.</p></div>
  </div>
</div></section>

<section class="navy"><div class="wrap stats">
  <div class="rv"><b>5.0</b><span>Google rating</span></div>
  <div class="rv"><b>{B["review_count"]}</b><span>Five-star reviews</span></div>
  <div class="rv"><b>100%</b><span>Insured</span></div>
  <div class="rv"><b>6</b><span>Towns served</span></div>
</div></section>

<section><div class="wrap split">
  <div class="rv"><div class="tag">Service areas</div><h2 style="font-size:clamp(2rem,4vw,2.8rem);color:var(--navy)">Proudly serving Apex &amp; the Triangle</h2>
    <p style="color:var(--muted)">Based in Apex, we work throughout southwest Wake County.</p><div class="chips">{chips}</div>
    <div class="actions"><a class="btn btn-green" href="~/service-areas/">See service areas</a></div></div>
  <iframe class="map rv" title="Map of Apex, NC" src="https://www.google.com/maps?q=Apex,+NC&amp;z=10&amp;output=embed" loading="lazy"></iframe>
</div></section>

<section class="bg"><div class="wrap">{review_band()}</div></section>

<section><div class="wrap">
  <div class="head c rv"><div class="tag">FAQ</div><h2>Questions, answered</h2></div>{faq(HOME_FAQS)}
</div></section>
{cta()}''' + footer()
    write(C, '', 'Carolina Premier Lawn & Tree | Concept B', body, FONTS)


def services_hub():
    body = header('services/') + ph('Services', 'Lawn, landscape, tree &amp; outdoor services', 'Seven services from one insured, 5-star rated local company.') + f'''
<section class="bg"><div class="wrap">{cards(SERVICES)}</div></section>{cta()}''' + footer()
    write(C, 'services/', 'Services | Concept B', body, FONTS)


def service(s):
    items = ''.join(f'<div><b>{e(n)}</b><span>{e(d)}</span></div>' for n, d in s['items'])
    intro = ''.join(f'<p>{e(p)}</p>' for p in s['intro'])
    local = ''.join(f'<p>{e(p)}</p>' for p in s['local'])
    h1 = s['h1'].replace(' class="hl"', '')
    body = header('services/') + ph(f'<a href="~/services/">Services</a> / {e(s["name"])}', h1, e(s['lead'])) + f'''
<section><div class="wrap layout">
  <div class="prose">
    {img(s["img"] + ".jpg", s["name"], cls="lead-img", lazy=False)}
    {intro}
    <h2>What's included</h2><div class="items">{items}</div>
    <h2>{e(s["local_title"])}</h2>{local}
    <h2>Frequently asked questions</h2><div class="one-col">{faq(s["faqs"])}</div>
  </div>
  <aside class="side">{quote_form()}</aside>
</div></section>
<section class="bg"><div class="wrap"><div class="head rv"><h2>Other services</h2></div>{cards([o for o in SERVICES if o is not s][:3])}</div></section>
{cta()}''' + footer()
    write(C, f'services/{s["slug"]}/', f'{s["name"]} | Concept B', body, FONTS)


def areas():
    cards_html = ''.join(f'<div class="card rv"><h3>{t["name"]}, NC</h3><p>{e(t["lead"])}</p></div>' for t in TOWNS)
    body = header('service-areas/') + ph('Service Areas', 'Serving Apex &amp; the Triangle', 'Based in Apex, we serve homes, HOAs and businesses across southwest Wake County.') + f'''
<section class="bg"><div class="wrap"><div class="cards">{cards_html}</div></div></section>
<section><div class="wrap"><iframe class="map" title="Map of Apex, NC" src="https://www.google.com/maps?q=Apex,+NC&amp;z=10&amp;output=embed" loading="lazy"></iframe></div></section>{cta()}''' + footer()
    write(C, 'service-areas/', 'Service Areas | Concept B', body, FONTS)


def projects():
    body = header('projects/') + ph('Projects', 'Recent projects', 'Before-and-after photos from jobs across the Triangle.') + f'''
<section><div class="wrap"><div class="soon rv"><h2 style="color:var(--navy)">Project photos coming soon</h2>
<p style="color:var(--muted)">We're putting together before-and-after photos. Until then, see photos of our work on Google.</p>
<div class="actions" style="justify-content:center"><a class="btn btn-green" href="{B["google_url"]}" target="_blank" rel="noopener">See photos on Google</a></div></div></div></section>{cta()}''' + footer()
    write(C, 'projects/', 'Projects | Concept B', body, FONTS)


def reviews():
    body = header('reviews/') + ph('Reviews', '5.0 stars on Google', f'{B["review_count"]} reviews, every one of them five stars.') + f'''
<section class="bg"><div class="wrap">{review_band()}
<div class="actions" style="justify-content:center"><a class="btn btn-green" href="{B["google_url"]}" target="_blank" rel="noopener">Read all reviews on Google</a><a class="btn btn-ghost" href="{B["google_url"]}" target="_blank" rel="noopener">Leave a review</a></div></div></section>{cta()}''' + footer()
    write(C, 'reviews/', 'Reviews | Concept B', body, FONTS)


def about():
    body = header('about/') + ph('About', 'Your local, insured outdoor team', 'Based in Apex, NC and rated 5.0 on Google.') + f'''
<section><div class="wrap split">
  {img("planting.jpg", "Planting by hand")}
  <div class="prose rv"><div class="tag">About us</div><h2 style="font-size:2.4rem;margin-top:0">Reliable work, done right, every time.</h2>
  <p>Carolina Premier Lawn &amp; Tree Services LLC takes care of lawns, landscapes, trees, hardscapes and fences for homeowners, HOAs and businesses across Apex and the Triangle.</p>
  <p>We're 100% insured, we give free estimates, and every customer who has reviewed us on Google has given us five stars.</p>
  <ul class="checks" style="grid-template-columns:1fr"><li>100% insured</li><li>5.0 stars on Google</li><li>Free estimates</li></ul></div>
</div></section>{cta()}''' + footer()
    write(C, 'about/', 'About | Concept B', body, FONTS)


def contact():
    body = header() + ph('Contact', 'Get your free quote', 'Send a request by text or call us directly.') + f'''
<section class="bg"><div class="wrap split" style="align-items:start">
  {quote_form("Request a quote")}
  <div class="prose rv"><h2 style="margin-top:0">Call or text</h2><p style="font-size:2rem;font-weight:900;color:var(--navy);margin:0"><a href="{TEL}" style="text-decoration:none">{B["phone"]}</a></p>
  <p>Serving Apex, Cary, Holly Springs, Fuquay-Varina, Morrisville and southwest Raleigh.</p>{review_band()}</div>
</div></section>''' + footer()
    write(C, 'contact/', 'Contact | Concept B', body, FONTS)


def build():
    write_static(C, CSS)
    home(); services_hub()
    for s in SERVICES:
        service(s)
    areas(); projects(); reviews(); about(); contact()
    print('built', C)
