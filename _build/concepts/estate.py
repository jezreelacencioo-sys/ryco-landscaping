"""Concept C: Estate. Dark, quiet luxury. Charcoal + champagne gold + ivory, Cormorant Garamond + Manrope."""
from common import B, TEL, SMS, SERVICES, TOWNS, HOME_FAQS, NAV, e, img, write, write_static

C = 'estate'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">'

CSS = r''':root { --bg: #121311; --bg-2: #1a1b18; --bg-3: #23241f; --gold: #c9a86a; --gold-l: #e2c993; --ivory: #f0e8d6; --muted: #a39d8f; --line: rgba(201, 168, 106, .22); }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--ivory); font: 300 1.04rem/1.8 Manrope, system-ui, sans-serif; }
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; }
h1, h2, h3 { font-family: "Cormorant Garamond", Georgia, serif; font-weight: 400; line-height: 1.05; margin: 0 0 .4em; }
h1 em, h2 em, h3 em { color: var(--gold); }
.wrap { max-width: 1240px; margin: 0 auto; padding: 0 28px; }
.eyebrow { font-size: .72rem; letter-spacing: .38em; text-transform: uppercase; color: var(--gold); font-weight: 500; margin-bottom: 22px; }
.rule { width: 60px; height: 1px; background: var(--gold); margin: 28px 0; }
.btn { display: inline-flex; align-items: center; gap: 12px; padding: 16px 30px; font: 500 .78rem Manrope, sans-serif; letter-spacing: .24em; text-transform: uppercase; text-decoration: none; border: 1px solid var(--gold); color: var(--gold); transition: background .3s, color .3s; cursor: pointer; background: none; }
.btn:hover, .btn-solid { background: var(--gold); color: var(--bg); }
.btn-solid:hover { background: var(--gold-l); }
.actions { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 34px; }

/* header */
.hdr { position: absolute; top: 0; left: 0; right: 0; z-index: 20; }
.hdr .wrap { display: flex; align-items: center; justify-content: space-between; height: 100px; gap: 24px; }
.hdr .logo img { width: 128px; }
.nav { display: flex; align-items: center; gap: 34px; }
.nav a { text-decoration: none; font-size: .74rem; letter-spacing: .26em; text-transform: uppercase; font-weight: 500; }
.nav a:hover, .nav a[aria-current] { color: var(--gold); }
.nav .btn { padding: 12px 22px; }
.menu { display: none; background: none; border: 1px solid var(--gold); color: var(--gold); padding: 10px 18px; font: 500 .72rem Manrope, sans-serif; letter-spacing: .24em; text-transform: uppercase; }

/* hero */
.hero { position: relative; min-height: 100vh; display: flex; align-items: flex-end; background: var(--bg) center / cover no-repeat; }
.hero::before { content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(18, 19, 17, .82) 0%, rgba(18, 19, 17, .45) 55%, rgba(18, 19, 17, .15) 100%), linear-gradient(180deg, rgba(18, 19, 17, .5) 0%, rgba(18, 19, 17, 0) 35%, rgba(18, 19, 17, .96) 100%); }
.hero .wrap { position: relative; width: 100%; padding-bottom: 110px; }
.hero h1 { font-size: clamp(3.6rem, 10vw, 8.4rem); max-width: 10ch; font-weight: 300; }
.hero p { max-width: 46ch; font-size: 1.12rem; color: #d9d1bf; margin: 0; }
.scroll { position: absolute; right: 28px; bottom: 110px; writing-mode: vertical-rl; font-size: .7rem; letter-spacing: .4em; text-transform: uppercase; color: var(--gold); }

section { padding: 130px 0; }
.bg2 { background: var(--bg-2); }
.statement { text-align: center; max-width: 920px; margin: 0 auto; }
.statement p { font-family: "Cormorant Garamond", serif; font-size: clamp(1.9rem, 3.6vw, 2.9rem); line-height: 1.3; margin: 0; }
.statement .rule { margin: 40px auto; }
.metrics { display: flex; justify-content: center; flex-wrap: wrap; gap: 20px 70px; margin-top: 60px; }
.metrics div { text-align: center; }
.metrics b { display: block; font-family: "Cormorant Garamond", serif; font-weight: 400; font-size: 3.4rem; color: var(--gold); line-height: 1; }
.metrics span { font-size: .72rem; letter-spacing: .3em; text-transform: uppercase; color: var(--muted); }

/* zig-zag services */
.head { max-width: 760px; margin-bottom: 70px; }
.head h2 { font-size: clamp(2.8rem, 5.6vw, 4.6rem); }
.head p { color: var(--muted); margin: 0; }
.zig { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; padding: 50px 0; border-top: 1px solid var(--line); text-decoration: none; }
.zig:nth-child(even) .zig-img { order: 2; }
.zig-img { overflow: hidden; }
.zig-img img { width: 100%; aspect-ratio: 3 / 2; object-fit: cover; transition: transform 1.2s; filter: saturate(.85); }
.zig:hover .zig-img img { transform: scale(1.05); }
.zig .num { font-family: "Cormorant Garamond", serif; font-style: italic; color: var(--gold); font-size: 1.3rem; }
.zig h3 { font-size: clamp(2.2rem, 4vw, 3.4rem); margin: 6px 0 14px; }
.zig p { color: var(--muted); margin: 0 0 22px; max-width: 44ch; }
.zig .more { font-size: .72rem; letter-spacing: .3em; text-transform: uppercase; color: var(--gold); }

/* process */
.process { display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; }
.process div { border-top: 1px solid var(--gold); padding-top: 30px; }
.process b { font-family: "Cormorant Garamond", serif; font-weight: 400; font-style: italic; font-size: 1.4rem; color: var(--gold); }
.process h3 { font-size: 2.2rem; margin-top: 10px; }
.process p { color: var(--muted); margin: 0; }

/* rating */
.rating { text-align: center; }
.rating .score { font-family: "Cormorant Garamond", serif; font-size: clamp(7rem, 16vw, 13rem); line-height: .9; color: var(--gold); font-weight: 300; }
.rating .stars { color: var(--gold); letter-spacing: 12px; font-size: 1.3rem; margin: 18px 0; }
.rating p { color: var(--muted); }

/* towns */
.towns { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--line); }
.towns li { padding: 30px 0; border-bottom: 1px solid var(--line); font-family: "Cormorant Garamond", serif; font-size: 2.2rem; display: flex; justify-content: space-between; align-items: baseline; padding-right: 30px; }
.towns small { font-family: Manrope, sans-serif; font-size: .7rem; letter-spacing: .3em; color: var(--muted); }

/* faq */
.faq { max-width: 900px; margin: 0 auto; border-top: 1px solid var(--line); }
.faq details { border-bottom: 1px solid var(--line); }
.faq summary { cursor: pointer; list-style: none; padding: 26px 0; font-family: "Cormorant Garamond", serif; font-size: 1.6rem; display: flex; justify-content: space-between; gap: 20px; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; color: var(--gold); font-family: Manrope, sans-serif; font-weight: 300; transition: transform .3s; }
.faq details[open] summary::after { transform: rotate(45deg); }
.faq p { margin: 0 0 26px; color: var(--muted); max-width: 70ch; }

/* cta */
.cta { position: relative; padding: 170px 0; text-align: center; background: var(--bg) center / cover no-repeat; }
.cta::before { content: ""; position: absolute; inset: 0; background: rgba(18, 19, 17, .78); }
.cta .wrap { position: relative; }
.cta h2 { font-size: clamp(3rem, 7vw, 5.6rem); font-weight: 300; }
.cta p { color: #d9d1bf; max-width: 50ch; margin: 0 auto; }
.cta .actions { justify-content: center; }

/* inner */
.ph { position: relative; padding: 210px 0 100px; background: var(--bg) center / cover no-repeat; }
.ph::before { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(18, 19, 17, .7), rgba(18, 19, 17, .95)); }
.ph .wrap { position: relative; }
.crumbs { font-size: .72rem; letter-spacing: .26em; text-transform: uppercase; color: var(--muted); margin-bottom: 34px; }
.crumbs a { text-decoration: none; color: var(--gold); }
.ph h1 { font-size: clamp(3rem, 7vw, 6rem); font-weight: 300; max-width: 14ch; }
.ph p { max-width: 56ch; color: #d9d1bf; margin: 0; font-size: 1.1rem; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 90px; }
.prose p { color: var(--muted); }
.items { display: grid; grid-template-columns: 1fr 1fr; gap: 0 60px; border-top: 1px solid var(--line); }
.items div { padding: 30px 0; border-bottom: 1px solid var(--line); }
.items h3 { font-size: 1.9rem; margin-bottom: 6px; }
.items p { margin: 0; color: var(--muted); }
.soon { text-align: center; max-width: 680px; margin: 0 auto; }
.soon p { color: var(--muted); }

/* form */
.form { display: grid; gap: 26px; }
.form label { display: grid; gap: 8px; font-size: .7rem; letter-spacing: .3em; text-transform: uppercase; color: var(--gold); }
.form input, .form select, .form textarea { font: 300 1.05rem Manrope, sans-serif; color: var(--ivory); background: transparent; border: 0; border-bottom: 1px solid var(--line); padding: 10px 0; width: 100%; }
.form select option { background: var(--bg); }
.form input:focus, .form select:focus, .form textarea:focus { outline: none; border-color: var(--gold); }
.form .note { font-size: .85rem; color: var(--muted); margin: 0; }

/* footer */
.ftr { border-top: 1px solid var(--line); padding: 90px 0 40px; font-size: .92rem; color: var(--muted); }
.ftr .grid { display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 60px; }
.ftr .logo img { width: 150px; margin-bottom: 18px; }
.ftr h4 { font-size: .7rem; letter-spacing: .3em; text-transform: uppercase; color: var(--gold); font-weight: 500; margin: 0 0 18px; }
.ftr ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; }
.ftr a { text-decoration: none; }
.ftr a:hover { color: var(--ivory); }
.ftr .tel { font-family: "Cormorant Garamond", serif; font-size: 2.2rem; color: var(--ivory); }
.ftr .copy { margin-top: 70px; font-size: .75rem; letter-spacing: .14em; }

.rv { opacity: 0; transform: translateY(30px); transition: opacity 1.1s ease, transform 1.1s ease; }
.rv.in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .rv { opacity: 1; transform: none; transition: none; } }

@media (max-width: 1000px) {
  .menu { display: block; }
  .nav { display: none; position: absolute; top: 100px; left: 0; right: 0; background: var(--bg); flex-direction: column; align-items: stretch; gap: 0; padding: 10px 28px 28px; border-bottom: 1px solid var(--line); }
  .nav.open { display: flex; }
  .nav a { padding: 16px 0; border-bottom: 1px solid var(--line); }
  .nav .btn { margin-top: 16px; justify-content: center; }
  .zig, .two { grid-template-columns: 1fr; gap: 34px; }
  .zig:nth-child(even) .zig-img { order: 0; }
  .process { grid-template-columns: 1fr; gap: 40px; }
  .towns { grid-template-columns: 1fr 1fr; }
  .ftr .grid { grid-template-columns: 1fr; }
  .scroll { display: none; }
}
@media (max-width: 640px) {
  section { padding: 90px 0; }
  .towns, .items { grid-template-columns: 1fr; }
  .towns li { font-size: 1.8rem; }
  .hero .wrap { padding-bottom: 70px; }
  .hero::before { background: linear-gradient(180deg, rgba(18, 19, 17, .7) 0%, rgba(18, 19, 17, .72) 50%, rgba(18, 19, 17, .97) 100%); }
  .ph { padding: 170px 0 70px; }
}
'''


def header(cur=''):
    links = ''.join(f'<a href="~/{p}"{" aria-current=page" if cur == p else ""}>{n}</a>' for p, n in NAV)
    return f'''<header class="hdr"><div class="wrap">
  <a class="logo" href="~/"><img src="~~/concepts/assets/logo-ivory.png" alt="Carolina Premier Lawn and Tree Services" width="286" height="150"></a>
  <button class="menu" data-menu aria-expanded="false">Menu</button>
  <nav class="nav" data-nav>{links}<a class="btn" href="~/contact/">Inquire</a></nav>
</div></header>
<main>'''


def footer():
    svc = ''.join(f'<li><a href="~/services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    towns = ''.join(f'<li>{t["name"]}</li>' for t in TOWNS)
    return f'''</main>
<footer class="ftr"><div class="wrap">
  <div class="grid">
    <div><a class="logo" href="~/"><img src="~~/concepts/assets/logo-ivory.png" alt="Carolina Premier" width="286" height="150"></a>
      <p>Grounds care, landscape and outdoor living for homes and communities in Apex and the Triangle. Fully insured.</p><a class="tel" href="{TEL}">{B["phone"]}</a></div>
    <div><h4>Services</h4><ul>{svc}</ul></div>
    <div><h4>Serving</h4><ul>{towns}</ul></div>
  </div>
  <div class="copy">© 2026 {e(B["name"]).upper()} · DESIGN CONCEPT C: ESTATE</div>
</div></footer>'''


def cta(image='garden.jpg'):
    return f'''<section class="cta" style="background-image:url('~~/images/{image}')"><div class="wrap rv">
  <div class="eyebrow">Complimentary estimates</div>
  <h2>Begin with a <em>conversation</em>.</h2>
  <p>Tell us about your property and what you envision. We'll visit, listen and provide a clear proposal.</p>
  <div class="actions"><a class="btn btn-solid" href="~/contact/">Request an estimate</a><a class="btn" href="{TEL}">{B["phone"]}</a></div>
</div></section>'''


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items) + '</div>'


def zig(services, start=0):
    return ''.join(f'''<a class="zig rv" href="~/services/{s["slug"]}/">
  <div class="zig-img">{img(s["img"] + ".jpg", s["name"])}</div>
  <div><span class="num">{i + start + 1:02d}</span><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="more">Discover →</span></div>
</a>''' for i, s in enumerate(services))


def ph(crumb, h1, lead, image):
    return f'''<section class="ph" style="background-image:url('~~/images/{image}')"><div class="wrap">
  <div class="crumbs"><a href="~/">Home</a> · {crumb}</div><h1>{h1}</h1><p>{lead}</p></div></section>'''


def home():
    towns = ''.join(f'<li>{t["name"]}<small>NC</small></li>' for t in TOWNS)
    body = header() + f'''
<section class="hero" style="background-image:url('~~/images/hero-home.jpg')"><div class="wrap">
  <div class="eyebrow">Apex · Cary · Holly Springs · The Triangle</div>
  <h1>Grounds, kept <em>beautifully</em>.</h1>
  <p>Lawn, landscape, tree and outdoor living services for homes that deserve a little more care.</p>
  <div class="actions"><a class="btn btn-solid" href="~/contact/">Request an estimate</a><a class="btn" href="~/services/">Our services</a></div>
  <span class="scroll">Scroll</span>
</div></section>

<section><div class="wrap statement rv">
  <div class="eyebrow">Carolina Premier Lawn &amp; Tree Services</div>
  <p>We believe the outside of a home should feel as considered as the inside. Every visit, every bed edge and every cut is done with that in mind.</p>
  <div class="rule"></div>
  <div class="metrics"><div><b>5.0</b><span>Google rating</span></div><div><b>{B["review_count"]}</b><span>Five-star reviews</span></div><div><b>100%</b><span>Insured</span></div></div>
</div></section>

<section class="bg2"><div class="wrap">
  <div class="head rv"><div class="eyebrow">Services</div><h2>Seven disciplines, <em>one standard</em>.</h2>
  <p>From the weekly cut to a new terrace, from pruning a heritage oak to lighting the house for the holidays.</p></div>
  {zig(SERVICES)}
</div></section>

<section><div class="wrap">
  <div class="head rv"><div class="eyebrow">Our approach</div><h2>Quietly <em>exceptional</em>.</h2></div>
  <div class="process">
    <div class="rv"><b>i.</b><h3>Listen</h3><p>We walk the property with you and learn how you use it and what you want from it.</p></div>
    <div class="rv"><b>ii.</b><h3>Propose</h3><p>A clear, complimentary estimate, and a design or mockup for larger projects.</p></div>
    <div class="rv"><b>iii.</b><h3>Tend</h3><p>Careful work on a dependable schedule, with the property left immaculate.</p></div>
  </div>
</div></section>

<section class="bg2"><div class="wrap rating rv">
  <div class="eyebrow">Reputation</div><div class="score">5.0</div><div class="stars">★★★★★</div>
  <p>Every one of our {B["review_count"]} Google reviews is five stars.</p>
  <div class="actions" style="justify-content:center"><a class="btn" href="~/reviews/">Read reviews</a></div>
</div></section>

<section><div class="wrap">
  <div class="head rv"><div class="eyebrow">Where we work</div><h2>The <em>Triangle</em>.</h2></div>
  <ul class="towns rv">{towns}</ul>
</div></section>

<section class="bg2"><div class="wrap">
  <div class="head rv" style="margin-left:auto;margin-right:auto;text-align:center"><div class="eyebrow">Questions</div><h2>Before we <em>begin</em>.</h2></div>
  {faq(HOME_FAQS)}
</div></section>
{cta()}''' + footer()
    write(C, '', 'Carolina Premier | Concept C', body, FONTS)


def services_hub():
    body = header('services/') + ph('Services', 'Seven disciplines, <em>one standard</em>.',
                                                  'Everything outside your home or property, cared for by one insured local team.', 'lawn.jpg') + f'''
<section class="bg2"><div class="wrap">{zig(SERVICES)}</div></section>{cta()}''' + footer()
    write(C, 'services/', 'Services | Concept C', body, FONTS)


def service(s):
    items = ''.join(f'<div class="rv"><h3>{e(n)}</h3><p>{e(d)}</p></div>' for n, d in s['items'])
    intro = ''.join(f'<p>{e(p)}</p>' for p in s['intro'])
    local = ''.join(f'<p>{e(p)}</p>' for p in s['local'])
    h1 = s['h1'].replace('<span class="hl">', '<em>').replace('</span>', '</em>')
    others = [o for o in SERVICES if o is not s][:2]
    body = header('services/') + ph(f'<a href="~/services/">Services</a> · {e(s["name"])}', h1, e(s['lead']), s['img'] + '.jpg') + f'''
<section><div class="wrap two">
  <div class="prose rv"><div class="eyebrow">Overview</div>{intro}</div>
  <div class="prose rv"><div class="eyebrow">{e(s["local_title"])}</div>{local}</div>
</div></section>
<section class="bg2"><div class="wrap"><div class="head rv"><div class="eyebrow">Included</div><h2>The <em>details</em>.</h2></div><div class="items">{items}</div></div></section>
<section><div class="wrap"><div class="head rv" style="margin-left:auto;margin-right:auto;text-align:center"><div class="eyebrow">Questions</div><h2>Good to <em>know</em>.</h2></div>{faq(s["faqs"])}</div></section>
<section class="bg2"><div class="wrap"><div class="head rv"><div class="eyebrow">Also offered</div></div>{zig(others)}</div></section>
{cta(s["img"] + ".jpg")}''' + footer()
    write(C, f'services/{s["slug"]}/', f'{s["name"]} | Concept C', body, FONTS)


def areas():
    rows = ''.join(f'<div class="rv"><h3>{t["name"]}, <em>NC</em></h3><p>{e(t["lead"])}</p></div>' for t in TOWNS)
    body = header('service-areas/') + ph('Service Areas', 'Rooted in <em>Apex</em>.', 'Serving homes and communities across southwest Wake County.', 'trees.jpg') + f'''
<section class="bg2"><div class="wrap"><div class="items">{rows}</div></div></section>{cta()}''' + footer()
    write(C, 'service-areas/', 'Service Areas | Concept C', body, FONTS)


def projects():
    body = header('projects/') + ph('Projects', 'Selected <em>work</em>.', 'A portfolio of recent projects across the Triangle.', 'garden-path.jpg') + f'''
<section><div class="wrap soon rv"><div class="eyebrow">Portfolio</div><h2>Arriving <em>soon</em>.</h2>
<p>We're photographing recent projects for this portfolio. In the meantime, photos of our work are on Google.</p>
<div class="actions" style="justify-content:center"><a class="btn" href="{B["google_url"]}" target="_blank" rel="noopener">View on Google</a></div></div></section>{cta()}''' + footer()
    write(C, 'projects/', 'Projects | Concept C', body, FONTS)


def reviews():
    body = header('reviews/') + ph('Reviews', 'In their <em>words</em>.', f'{B["review_count"]} reviews on Google, each one five stars.', 'lawn.jpg') + f'''
<section class="bg2"><div class="wrap rating rv"><div class="score">5.0</div><div class="stars">★★★★★</div>
<div class="actions" style="justify-content:center"><a class="btn btn-solid" href="{B["google_url"]}" target="_blank" rel="noopener">Read on Google</a><a class="btn" href="{B["google_url"]}" target="_blank" rel="noopener">Leave a review</a></div></div></section>{cta()}''' + footer()
    write(C, 'reviews/', 'Reviews | Concept C', body, FONTS)


def about():
    body = header('about/') + ph('About', 'Care you can <em>see</em>.', 'A local, fully insured team based in Apex, North Carolina.', 'garden.jpg') + f'''
<section><div class="wrap two" style="align-items:center">
  {img("planting.jpg", "Planting by hand", cls="rv")}
  <div class="prose rv"><div class="eyebrow">Our philosophy</div><h2 style="font-size:3rem">Show up. Do it right. <em>Leave it immaculate.</em></h2>
  <p>Carolina Premier Lawn &amp; Tree Services cares for lawns, landscapes, trees and outdoor living spaces for homeowners, HOAs and businesses across Apex and the Triangle.</p>
  <p>We're 100% insured, our estimates are complimentary, and every client who has reviewed us on Google has given us five stars.</p></div>
</div></section>{cta()}''' + footer()
    write(C, 'about/', 'About | Concept C', body, FONTS)


def contact():
    opts = ''.join(f'<option>{e(s["name"])}</option>' for s in SERVICES)
    towns = ''.join(f'<option>{t["name"]}</option>' for t in TOWNS)
    body = header() + ph('Inquire', 'Begin with a <em>conversation</em>.', 'Share a few details and your request arrives as a text, or simply call.', 'hero-home.jpg') + f'''
<section><div class="wrap two">
  <form class="form rv" data-sms>
    <label>Name<input name="Name" required></label>
    <label>Property address<input name="Address" required></label>
    <label>Town<select name="Town">{towns}<option>Other</option></select></label>
    <label>Service<select name="Service">{opts}</select></label>
    <label>Tell us more<textarea name="Details" rows="3"></textarea></label>
    <div><button class="btn btn-solid" type="submit">Send inquiry</button></div>
    <p class="note">Opens your texting app with your request filled in.</p>
  </form>
  <div class="prose rv"><div class="eyebrow">Direct</div><h2 style="font-size:3.4rem"><a href="{TEL}" style="text-decoration:none">{B["phone"]}</a></h2>
  <p>Serving Apex, Cary, Holly Springs, Fuquay-Varina, Morrisville and southwest Raleigh. Fully insured. Complimentary estimates.</p></div>
</div></section>''' + footer()
    write(C, 'contact/', 'Inquire | Concept C', body, FONTS)


def build():
    write_static(C, CSS)
    home(); services_hub()
    for s in SERVICES:
        service(s)
    areas(); projects(); reviews(); about(); contact()
    print('built', C)
