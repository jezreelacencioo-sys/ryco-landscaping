"""Concept A: Garden Journal. Warm, editorial, cream + forest + terracotta, Fraunces + Inter."""
from common import B, TEL, SMS, SERVICES, TOWNS, HOME_FAQS, NAV, e, img, write, write_static

C = 'garden-journal'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'

CSS = r''':root { --cream: #f6f1e7; --cream-2: #ece4d3; --forest: #163424; --forest-2: #24503a; --terra: #c4663a; --sage: #8fa98a; --ink: #1d2a22; --muted: #5f6b62; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--cream); color: var(--ink); font: 400 1.05rem/1.7 Inter, system-ui, sans-serif; }
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; }
h1, h2, h3 { font-family: Fraunces, Georgia, serif; font-weight: 400; line-height: 1.08; margin: 0 0 .45em; letter-spacing: -.01em; }
h1 em, h2 em, h3 em { font-style: italic; color: var(--terra); }
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 24px; }
.kicker { font-size: .78rem; letter-spacing: .22em; text-transform: uppercase; font-weight: 600; color: var(--forest-2); margin-bottom: 14px; display: flex; align-items: center; gap: 10px; }
.kicker::before { content: ""; width: 28px; height: 1px; background: currentColor; }
.btn { display: inline-flex; align-items: center; gap: 10px; padding: 15px 26px; border-radius: 999px; font-weight: 600; text-decoration: none; transition: background .2s, color .2s, transform .2s; }
.btn:hover { transform: translateY(-2px); }
.btn-terra { background: var(--terra); color: #fff; }
.btn-terra:hover { background: #a9532b; }
.btn-line { border: 1.5px solid var(--forest); color: var(--forest); }
.btn-line:hover { background: var(--forest); color: var(--cream); }
.actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 28px; }

/* header */
.hdr { position: sticky; top: 0; z-index: 20; background: rgba(246, 241, 231, .94); backdrop-filter: blur(8px); border-bottom: 1px solid var(--cream-2); }
.hdr .wrap { display: flex; align-items: center; justify-content: space-between; height: 86px; gap: 24px; }
.hdr .logo img { width: 130px; }
.nav { display: flex; align-items: center; gap: 30px; }
.nav a { text-decoration: none; font-weight: 500; font-size: .95rem; }
.nav a:hover, .nav a[aria-current] { color: var(--terra); }
.nav .btn { padding: 11px 20px; color: #fff; }
.nav .btn:hover { color: #fff; }
.menu { display: none; background: none; border: 1.5px solid var(--forest); border-radius: 999px; padding: 8px 16px; font: 600 .9rem Inter, sans-serif; color: var(--forest); }

/* hero */
.hero { padding: 70px 0 90px; }
.hero .wrap { display: grid; grid-template-columns: 1.1fr .9fr; gap: 60px; align-items: center; }
.hero h1 { font-size: clamp(3rem, 6.4vw, 5.6rem); }
.hero p.lead { font-size: 1.2rem; color: var(--muted); max-width: 46ch; }
.proof { display: flex; flex-wrap: wrap; gap: 8px 22px; margin-top: 34px; font-size: .92rem; color: var(--muted); }
.proof b { color: var(--ink); }
.arch { position: relative; }
.arch img { border-radius: 999px 999px 24px 24px; aspect-ratio: 4 / 5; object-fit: cover; width: 100%; }
.stamp { position: absolute; left: -36px; bottom: 40px; width: 140px; height: 140px; border-radius: 50%; background: var(--terra); color: #fff; display: grid; place-content: center; text-align: center; font-family: Fraunces, serif; font-size: 1rem; line-height: 1.2; transform: rotate(-10deg); box-shadow: 0 16px 30px rgba(0, 0, 0, .15); }
.stamp b { font-size: 2.2rem; font-weight: 600; display: block; }

section { padding: 96px 0; }
.alt { background: var(--cream-2); }
.forest { background: var(--forest); color: var(--cream); }
.forest .kicker { color: var(--sage); }
.head { max-width: 680px; margin-bottom: 50px; }
.head h2 { font-size: clamp(2.3rem, 4.6vw, 3.6rem); }
.head p { color: var(--muted); font-size: 1.1rem; margin: 0; }
.forest .head p { color: #c9d6cc; }

/* numbered service list */
.svc-list { border-top: 1px solid #d6cdb8; }
.svc-row { display: grid; grid-template-columns: 90px 1.2fr 1.4fr 40px; gap: 24px; align-items: baseline; padding: 30px 0; border-bottom: 1px solid #d6cdb8; text-decoration: none; transition: padding .25s, background .25s; }
.svc-row:hover { padding-left: 14px; background: rgba(196, 102, 58, .06); }
.svc-row .n { font-family: Fraunces, serif; font-style: italic; color: var(--terra); font-size: 1.4rem; }
.svc-row h3 { font-size: 2rem; margin: 0; }
.svc-row p { margin: 0; color: var(--muted); }
.svc-row .ar { font-size: 1.5rem; color: var(--terra); transition: transform .25s; }
.svc-row:hover .ar { transform: translateX(6px); }

/* seasons */
.seasons { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
.season { background: var(--forest-2); border-radius: 24px; padding: 30px 26px; }
.season h3 { font-size: 1.9rem; color: #fff; }
.season h3 small { display: block; font-family: Inter, sans-serif; font-size: .75rem; letter-spacing: .2em; text-transform: uppercase; color: var(--sage); margin-bottom: 8px; }
.season ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 10px; color: #d9e3dc; font-size: .97rem; }
.season li::before { content: "❦ "; color: var(--terra); }

/* split */
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: center; }
.split img { border-radius: 24px; aspect-ratio: 5 / 4; object-fit: cover; width: 100%; }
.split .arch img { aspect-ratio: 4 / 5; }
.prose p { color: var(--muted); }
.ticks { list-style: none; padding: 0; margin: 26px 0; display: grid; gap: 12px; }
.ticks li { padding-left: 34px; position: relative; font-weight: 500; }
.ticks li::before { content: ""; position: absolute; left: 0; top: .35em; width: 20px; height: 12px; border-left: 2px solid var(--terra); border-bottom: 2px solid var(--terra); transform: rotate(-45deg); }

/* reviews */
.rating { display: grid; grid-template-columns: auto 1fr; gap: 60px; align-items: center; }
.rating .big { font-family: Fraunces, serif; font-size: clamp(6rem, 14vw, 11rem); line-height: .9; color: var(--terra); font-style: italic; }
.rating .stars { color: #e7b04a; font-size: 1.6rem; letter-spacing: 4px; }
.rating h2 { font-size: clamp(2rem, 4vw, 3rem); }

/* towns */
.towns { font-family: Fraunces, serif; font-size: clamp(1.8rem, 4vw, 3rem); line-height: 1.35; }
.towns a { text-decoration: none; border-bottom: 2px solid transparent; transition: border-color .2s, color .2s; }
.towns a:hover { color: var(--terra); border-color: var(--terra); }
.towns span { color: var(--sage); }

/* faq */
.faq { display: grid; gap: 0; border-top: 1px solid #d6cdb8; max-width: 860px; }
.faq details { border-bottom: 1px solid #d6cdb8; padding: 4px 0; }
.faq summary { cursor: pointer; list-style: none; padding: 20px 0; font-family: Fraunces, serif; font-size: 1.35rem; display: flex; justify-content: space-between; gap: 20px; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; color: var(--terra); transition: transform .2s; }
.faq details[open] summary::after { transform: rotate(45deg); }
.faq p { margin: 0 0 22px; color: var(--muted); }

/* cta */
.cta { background: var(--terra); color: #fff; border-radius: 300px 300px 32px 32px; padding: 110px 40px 80px; text-align: center; }
.cta h2 { font-size: clamp(2.4rem, 5vw, 4rem); }
.cta p { max-width: 46ch; margin: 0 auto; opacity: .92; }
.cta .actions { justify-content: center; }
.cta .btn-line { border-color: #fff; color: #fff; }
.cta .btn-line:hover { background: #fff; color: var(--terra); }
.cta .btn-cream { background: var(--cream); color: var(--forest); }

/* page header */
.ph { padding: 60px 0 70px; }
.ph .crumbs { font-size: .88rem; color: var(--muted); margin-bottom: 30px; }
.ph .crumbs a { text-decoration: none; }
.ph h1 { font-size: clamp(2.8rem, 6vw, 5rem); max-width: 16ch; }
.ph p { font-size: 1.2rem; color: var(--muted); max-width: 56ch; margin: 0; }
.ph-img { margin-top: 50px; }
.ph-img img { border-radius: 28px; width: 100%; aspect-ratio: 21 / 8; object-fit: cover; }

/* items */
.items { display: grid; grid-template-columns: 1fr 1fr; gap: 0 60px; }
.items div { padding: 24px 0; border-bottom: 1px solid #d6cdb8; }
.items h3 { font-size: 1.5rem; margin-bottom: .2em; }
.items p { margin: 0; color: var(--muted); }

/* form */
.form { background: #fff; border-radius: 28px; padding: 40px; display: grid; gap: 16px; }
.form label { display: grid; gap: 6px; font-weight: 600; font-size: .9rem; }
.form input, .form select, .form textarea { font: inherit; padding: 14px 16px; border: 1.5px solid #d6cdb8; border-radius: 14px; background: var(--cream); }
.form input:focus, .form select:focus, .form textarea:focus { outline: none; border-color: var(--terra); }
.form button { border: 0; cursor: pointer; justify-content: center; font: 600 1rem Inter, sans-serif; }
.note { font-size: .9rem; color: var(--muted); margin: 0; }
.soon { text-align: center; max-width: 640px; margin: 0 auto; }

/* footer */
.ftr { background: var(--forest); color: #c9d6cc; padding: 80px 0 40px; margin-top: 96px; font-size: .95rem; }
.ftr .grid { display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 50px; }
.ftr h4 { font-family: Fraunces, serif; font-weight: 400; color: #fff; font-size: 1.3rem; margin: 0 0 14px; }
.ftr ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; }
.ftr a { text-decoration: none; }
.ftr a:hover { color: #fff; }
.ftr .big-phone { font-family: Fraunces, serif; font-size: 2rem; color: #fff; }
.ftr .copy { border-top: 1px solid rgba(255, 255, 255, .12); margin-top: 50px; padding-top: 24px; font-size: .85rem; }

.rv { opacity: 0; transform: translateY(24px); transition: opacity .8s, transform .8s; }
.rv.in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .rv { opacity: 1; transform: none; transition: none; } }

@media (max-width: 980px) {
  .menu { display: block; }
  .nav { display: none; position: absolute; top: 86px; left: 0; right: 0; background: var(--cream); flex-direction: column; align-items: stretch; gap: 0; padding: 10px 24px 24px; border-bottom: 1px solid var(--cream-2); }
  .nav.open { display: flex; }
  .nav a { padding: 14px 0; border-bottom: 1px solid var(--cream-2); }
  .nav .btn { margin-top: 14px; justify-content: center; }
  .hero .wrap, .split, .rating { grid-template-columns: 1fr; }
  .seasons { grid-template-columns: 1fr 1fr; }
  .svc-row { grid-template-columns: 50px 1fr 30px; }
  .svc-row p { grid-column: 2 / 3; }
  .ftr .grid { grid-template-columns: 1fr; }
  .stamp { left: 10px; }
}
@media (max-width: 620px) {
  section { padding: 70px 0; }
  .seasons, .items { grid-template-columns: 1fr; }
  .cta { border-radius: 200px 200px 24px 24px; padding: 90px 22px 60px; }
  .form { padding: 26px; }
  .stamp { width: 110px; height: 110px; font-size: .85rem; }
  .stamp b { font-size: 1.7rem; }
}
'''


def header(cur=''):
    links = ''.join(f'<a href="~/{p}"{" aria-current=page" if cur == p else ""}>{n}</a>' for p, n in NAV)
    return f'''<header class="hdr"><div class="wrap">
  <a class="logo" href="~/"><img src="~~/concepts/assets/logo-forest.png" alt="Carolina Premier Lawn and Tree Services" width="286" height="150"></a>
  <button class="menu" data-menu aria-expanded="false">Menu</button>
  <nav class="nav" data-nav>{links}<a class="btn btn-terra" href="~/contact/">Get an estimate</a></nav>
</div></header>
<main>'''


def footer():
    svc = ''.join(f'<li><a href="~/services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    towns = ''.join(f'<li>{t["name"]}, NC</li>' for t in TOWNS)
    return f'''</main>
<footer class="ftr"><div class="wrap">
  <div class="grid">
    <div><h4>Carolina Premier Lawn &amp; Tree Services</h4><p>Lawn care, landscaping, tree work, hardscaping and fencing for homes and communities across Apex and the Triangle. 100% insured.</p>
      <a class="big-phone" href="{TEL}">{B["phone"]}</a></div>
    <div><h4>Services</h4><ul>{svc}</ul></div>
    <div><h4>Where we work</h4><ul>{towns}</ul></div>
  </div>
  <div class="copy">© 2026 {e(B["name"])} · Design concept A: Garden Journal</div>
</div></footer>'''


def cta():
    return f'''<section><div class="wrap"><div class="cta rv">
  <div class="kicker" style="justify-content:center;color:#fff">Free estimates</div>
  <h2>Let's make your yard <em style="color:var(--cream)">the good kind</em> of busy.</h2>
  <p>Call or text and tell us what you have in mind. We'll come take a look and give you a clear price.</p>
  <div class="actions"><a class="btn btn-cream" href="{TEL}">Call {B["phone"]}</a><a class="btn btn-line" href="{SMS}">Send a text</a></div>
</div></div></section>'''


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items) + '</div>'


def svc_list(services):
    return '<div class="svc-list">' + ''.join(f'''<a class="svc-row rv" href="~/services/{s["slug"]}/">
  <span class="n">No. {i + 1:02d}</span><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="ar">→</span></a>''' for i, s in enumerate(services)) + '</div>'


def ph(crumb, h1, lead, image=None):
    pic = f'<div class="ph-img rv">{img(image, lazy=False)}</div>' if image else ''
    return f'''<section class="ph"><div class="wrap">
  <div class="crumbs"><a href="~/">Home</a> / {crumb}</div>
  <h1>{h1}</h1><p>{lead}</p>{pic}
</div></section>'''


def home():
    towns = '<span> · </span>'.join(f'<a href="~/service-areas/">{t["name"]}</a>' for t in TOWNS)
    body = header() + f'''
<section class="hero"><div class="wrap">
  <div>
    <div class="kicker">Lawn · Landscape · Trees · Apex, NC</div>
    <h1>Yards worth <em>coming home</em> to.</h1>
    <p class="lead">Carolina Premier takes care of everything outside your home: the weekly mow, the new patio, the tree that has to go, even the Christmas lights.</p>
    <div class="actions"><a class="btn btn-terra" href="~/contact/">Get a free estimate</a><a class="btn btn-line" href="~/services/">Explore services</a></div>
    <div class="proof"><span><b>★ 5.0</b> on Google</span><span><b>24</b> five-star reviews</span><span><b>100%</b> insured</span></div>
  </div>
  <div class="arch rv">{img("hero-home.jpg", "A well-kept home and lawn at dusk", lazy=False)}<div class="stamp"><b>5.0</b>Google<br>rated</div></div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="head rv"><div class="kicker">What we do</div><h2>Seven ways we <em>take care</em> of your property.</h2>
  <p>One local crew for the lawn, the beds, the trees and the stonework, so you never have to juggle companies.</p></div>
  {svc_list(SERVICES)}
</div></section>

<section class="forest"><div class="wrap">
  <div class="head rv"><div class="kicker">A year in your yard</div><h2>The right work at the <em style="color:#e9a27c">right time</em>.</h2>
  <p>Triangle yards run on their own calendar. Here's how we plan the seasons.</p></div>
  <div class="seasons">
    <div class="season rv"><h3><small>Mar – May</small>Spring</h3><ul><li>Spring cleanups</li><li>Fresh mulch &amp; pine straw</li><li>New beds &amp; planting</li><li>Mowing season starts</li></ul></div>
    <div class="season rv"><h3><small>Jun – Aug</small>Summer</h3><ul><li>Mowing high for heat</li><li>Shrub &amp; hedge trimming</li><li>Patios &amp; fire pits</li><li>Fence installs</li></ul></div>
    <div class="season rv"><h3><small>Sep – Nov</small>Fall</h3><ul><li>Aeration &amp; overseeding</li><li>Fall fertilization</li><li>Leaf removal</li><li>Christmas light installs</li></ul></div>
    <div class="season rv"><h3><small>Dec – Feb</small>Winter</h3><ul><li>Tree pruning &amp; removal</li><li>Stump grinding</li><li>Holiday light takedown</li><li>Planning next year's design</li></ul></div>
  </div>
</div></section>

<section><div class="wrap split">
  <div class="arch rv">{img("garden-path.jpg", "Garden path with clipped hedges")}</div>
  <div class="prose rv"><div class="kicker">Why Carolina Premier</div><h2 style="font-size:clamp(2.2rem,4.4vw,3.4rem)">Local roots, <em>careful</em> work.</h2>
    <p>We're based in Apex, so we know what Triangle yards are up against: red clay, July heat and fescue that needs real attention every fall.</p>
    <ul class="ticks"><li>100% insured on every job</li><li>Rated 5.0 by every Google reviewer</li><li>Free, no-pressure estimates</li><li>Homes, HOAs and commercial properties</li></ul>
    <a class="btn btn-line" href="~/about/">Our story</a></div>
</div></section>

<section class="alt"><div class="wrap rating">
  <div class="big rv">5.0</div>
  <div class="rv"><div class="stars">★★★★★</div><h2>Every review, <em>five stars</em>.</h2>
    <p style="color:var(--muted)">{B["review_count"]} homeowners have reviewed us on Google, and every one gave us five stars.</p>
    <a class="btn btn-terra" href="~/reviews/">Read the reviews</a></div>
</div></section>

<section><div class="wrap">
  <div class="kicker rv">Where we work</div>
  <p class="towns rv">{towns}</p>
</div></section>

<section class="alt"><div class="wrap">
  <div class="head rv"><div class="kicker">Questions</div><h2>Good to <em>know</em>.</h2></div>
  {faq(HOME_FAQS)}
</div></section>
{cta()}''' + footer()
    write(C, '', 'Carolina Premier Lawn & Tree | Concept A', body, FONTS)


def services_hub():
    body = header('services/') + ph('Services', 'Everything <em>outside</em> your home.',
                                     'Seven services, one crew. Pick one to see exactly what\'s included.', 'lawn.jpg') + f'''
<section style="padding-top:20px"><div class="wrap">{svc_list(SERVICES)}</div></section>{cta()}''' + footer()
    write(C, 'services/', 'Services | Concept A', body, FONTS)


def service(s):
    items = ''.join(f'<div class="rv"><h3>{e(n)}</h3><p>{e(d)}</p></div>' for n, d in s['items'])
    intro = ''.join(f'<p>{e(p)}</p>' for p in s['intro'])
    local = ''.join(f'<p>{e(p)}</p>' for p in s['local'])
    others = [o for o in SERVICES if o is not s][:3]
    body = header('services/') + ph(f'<a href="~/services/">Services</a> / {e(s["name"])}', s['h1'].replace('class="hl"', '').replace('<span >', '<em>').replace('</span>', '</em>'), e(s['lead']), s['img'] + '.jpg') + f'''
<section style="padding-top:20px"><div class="wrap split" style="align-items:start">
  <div class="prose rv"><div class="kicker">Overview</div>{intro}<div class="actions"><a class="btn btn-terra" href="~/contact/">Get a free estimate</a></div></div>
  <div class="prose rv"><div class="kicker">{e(s["local_title"])}</div>{local}</div>
</div></section>
<section class="alt"><div class="wrap">
  <div class="head rv"><div class="kicker">What's included</div><h2>{e(s["name"])}, <em>in detail</em>.</h2></div>
  <div class="items">{items}</div>
</div></section>
<section><div class="wrap">
  <div class="head rv"><div class="kicker">Questions</div><h2>Good to <em>know</em>.</h2></div>{faq(s["faqs"])}
</div></section>
<section class="alt"><div class="wrap"><div class="head rv"><div class="kicker">Also from us</div><h2>More <em>services</em>.</h2></div>{svc_list(others)}</div></section>
{cta()}''' + footer()
    write(C, f'services/{s["slug"]}/', f'{s["name"]} | Concept A', body, FONTS)


def areas():
    cards = ''.join(f'<div class="season rv"><h3><small>North Carolina</small>{t["name"]}</h3><p style="color:#d9e3dc;margin:0">{e(t["lead"])}</p></div>' for t in TOWNS)
    body = header('service-areas/') + ph('Service Areas', 'Rooted in <em>Apex</em>.', 'We take care of homes and communities across southwest Wake County.') + f'''
<section class="forest"><div class="wrap"><div class="seasons" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{cards}</div></div></section>{cta()}''' + footer()
    write(C, 'service-areas/', 'Service Areas | Concept A', body, FONTS)


def projects():
    body = header('projects/') + ph('Projects', 'Our <em>work</em>.', 'Before-and-after photos from around the Triangle.') + f'''
<section class="alt"><div class="wrap soon rv"><h2>Photos <em>coming soon</em>.</h2>
  <p style="color:var(--muted)">We're gathering before-and-after photos of recent jobs. Until then, browse photos of our work on Google.</p>
  <div class="actions" style="justify-content:center"><a class="btn btn-terra" href="{B["google_url"]}" target="_blank" rel="noopener">See photos on Google</a></div></div></section>{cta()}''' + footer()
    write(C, 'projects/', 'Projects | Concept A', body, FONTS)


def reviews():
    body = header('reviews/') + ph('Reviews', 'Five stars, <em>every time</em>.', f'{B["review_count"]} Google reviews from homeowners across the Triangle.') + f'''
<section class="alt"><div class="wrap rating">
  <div class="big rv">5.0</div>
  <div class="rv"><div class="stars">★★★★★</div><h2>Read what our <em>neighbors</em> say.</h2>
  <div class="actions"><a class="btn btn-terra" href="{B["google_url"]}" target="_blank" rel="noopener">Read reviews on Google</a><a class="btn btn-line" href="{B["google_url"]}" target="_blank" rel="noopener">Leave a review</a></div></div>
</div></section>{cta()}''' + footer()
    write(C, 'reviews/', 'Reviews | Concept A', body, FONTS)


def about():
    body = header('about/') + ph('About', 'A local crew that <em>cares</em> how it looks.', 'Based in Apex, NC. 100% insured. Rated five stars on Google.') + f'''
<section style="padding-top:10px"><div class="wrap split">
  <div class="arch rv">{img("planting.jpg", "Planting by hand")}</div>
  <div class="prose rv"><div class="kicker">Our story</div><h2 style="font-size:clamp(2.2rem,4.4vw,3.2rem)">Show up. Do it right. <em>Leave it clean.</em></h2>
  <p>Carolina Premier Lawn &amp; Tree Services takes care of lawns, landscapes, trees and outdoor spaces for homeowners, HOAs and businesses across Apex and the Triangle.</p>
  <p>Every job, from a weekly mow to a new patio, gets the same attention: the right technique for our clay and climate, and a clean property when we leave.</p>
  <ul class="ticks"><li>100% insured</li><li>5.0 stars on Google</li><li>Free estimates</li></ul></div>
</div></section>{cta()}''' + footer()
    write(C, 'about/', 'About | Concept A', body, FONTS)


def contact():
    opts = ''.join(f'<option>{e(s["name"])}</option>' for s in SERVICES)
    towns = ''.join(f'<option>{t["name"]}</option>' for t in TOWNS)
    body = header() + ph('Contact', 'Let\'s <em>talk</em> about your yard.', 'Send a request by text, or just call. Estimates are always free.') + f'''
<section style="padding-top:10px"><div class="wrap split" style="align-items:start">
  <form class="form rv" data-sms>
    <label>Name<input name="Name" required></label>
    <label>Address<input name="Address" required></label>
    <label>Town<select name="Town">{towns}<option>Other</option></select></label>
    <label>Service<select name="Service">{opts}</select></label>
    <label>Details<textarea name="Details" rows="4"></textarea></label>
    <button class="btn btn-terra" type="submit">Send by text</button>
    <p class="note">Opens your texting app with your request filled in.</p>
  </form>
  <div class="prose rv"><div class="kicker">Call or text</div><h2 style="font-size:3rem"><a href="{TEL}" style="text-decoration:none">{B["phone"]}</a></h2>
  <p>Serving Apex, Cary, Holly Springs, Fuquay-Varina, Morrisville and southwest Raleigh.</p>
  <ul class="ticks"><li>Free estimates</li><li>100% insured</li><li>5.0 stars on Google</li></ul></div>
</div></section>''' + footer()
    write(C, 'contact/', 'Contact | Concept A', body, FONTS)


def build():
    write_static(C, CSS)
    home(); services_hub()
    for s in SERVICES:
        service(s)
    areas(); projects(); reviews(); about(); contact()
    print('built', C)
