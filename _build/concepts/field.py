"""Concept D: Field Day. Bold and sporty: deep green, lime and yellow, Barlow Condensed headlines,
brush-stroke underlines, outlined chunky buttons and photo cards."""
from common import B, TEL, SMS, SERVICES, TOWNS, HOME_FAQS, NAV, e, img, write, write_static

C = 'field-day'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">'

BRUSH = '<svg class="brush" viewBox="0 0 300 14" preserveAspectRatio="none" aria-hidden="true"><path d="M2 9 C 60 4, 120 6, 180 4 S 270 3, 298 6 L 296 9 C 240 8, 200 10, 140 10 S 40 12, 4 12 Z" fill="currentColor"/><path d="M190 11 L 260 9 L 262 10 L 192 12 Z M 230 4 L 290 3 L 291 4 L 232 5 Z" fill="currentColor" opacity=".6"/></svg>'

CSS = r''':root { --green: #0a4d24; --green-2: #0e5f2d; --green-3: #073a1b; --lime: #8cc63f; --lime-2: #a5d65a; --yellow: #ffc20e; --ink: #0f1f14; --muted: #4c5a50; --off: #f3f7ef; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: #fff; color: var(--ink); font: 400 1.06rem/1.7 Barlow, system-ui, sans-serif; }
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; }
h1, h2, h3 { font-family: "Barlow Condensed", Impact, sans-serif; font-weight: 800; text-transform: uppercase; line-height: 1.02; letter-spacing: .005em; margin: 0 0 .3em; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 20px; }
.brush { display: block; width: 260px; height: 14px; color: var(--lime); margin: 6px auto 26px; }
.left .brush { margin-left: 0; }
.title { text-align: center; font-size: clamp(2.4rem, 5.6vw, 4rem); color: var(--green); }
.on-dark .title, .on-dark h2 { color: #fff; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 18px 34px; border-radius: 16px; font-family: Barlow, sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; font-size: 1.02rem; text-decoration: none; cursor: pointer; transition: transform .15s, background .15s; border: 0; }
.btn:hover { transform: translateY(-2px); }
.btn-green { background: var(--green); color: #fff; box-shadow: 0 0 0 4px var(--lime); }
.btn-green:hover { background: var(--green-2); }
.btn-yellow { background: var(--yellow); color: var(--green); }
.btn-yellow:hover { background: #ffd04a; }
.btn-lime { background: var(--lime); color: var(--green-3); }
.actions { display: flex; flex-wrap: wrap; gap: 18px; margin-top: 30px; }
.actions.center { justify-content: center; }

/* header */
.hdr { position: sticky; top: 0; z-index: 30; background: var(--green); }
.hdr::after { content: ""; display: block; height: 7px; background: linear-gradient(90deg, var(--yellow) 0 22%, var(--lime) 22% 100%); }
.hdr .wrap { display: flex; align-items: center; justify-content: space-between; height: 92px; gap: 20px; }
.hdr .logo { display: block; background: var(--green-3); border: 3px solid var(--lime); border-radius: 14px; padding: 4px 10px; }
.hdr .logo img { width: 112px; }
.nav { display: flex; align-items: center; gap: 26px; }
.nav a { color: #fff; text-decoration: none; font-family: "Barlow Condensed", sans-serif; font-weight: 700; font-size: 1.25rem; text-transform: uppercase; letter-spacing: .04em; }
.nav a:hover, .nav a[aria-current] { color: var(--lime); }
.nav .btn { font-family: Barlow, sans-serif; font-size: .9rem; padding: 12px 20px; color: var(--green); box-shadow: none; }
.nav .btn:hover { color: var(--green); }
.menu { display: none; width: 58px; height: 52px; background: var(--green-3); border: 3px solid var(--lime); border-radius: 12px; color: #fff; cursor: pointer; }

/* hero */
.hero { position: relative; background: var(--green-3) center / cover no-repeat; color: #fff; text-align: center; padding: 90px 0 150px; }
.hero::before { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(7, 58, 27, .88) 0%, rgba(7, 58, 27, .8) 60%, rgba(7, 58, 27, .65) 100%); }
.hero .wrap { position: relative; max-width: 960px; }
.hero h1 { font-size: clamp(2.8rem, 7.4vw, 5.6rem); }
.hero .brush { width: 300px; }
.hero p { font-size: 1.22rem; max-width: 62ch; margin: 0 auto; color: #e6efe4; }
.hero .actions { justify-content: center; }
.hero .btn { min-width: 290px; }

/* trust box */
.trust { position: relative; z-index: 2; margin-top: -86px; }
.trust ul { list-style: none; margin: 0 auto; padding: 30px 26px; max-width: 1000px; background: var(--lime); border: 5px solid #fff; border-radius: 22px; box-shadow: 0 18px 40px rgba(7, 58, 27, .25); display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 14px 30px; font-family: "Barlow Condensed", sans-serif; font-weight: 800; text-transform: uppercase; font-size: clamp(1.4rem, 3vw, 2rem); color: #fff; text-shadow: 0 1px 0 rgba(7, 58, 27, .25); }
.trust li { display: flex; align-items: center; gap: 30px; }
.trust li + li::before { content: ""; width: 14px; height: 14px; background: var(--green); transform: rotate(45deg); border-radius: 3px; }

section { padding: 90px 0; }
.on-dark { background: var(--green); color: #e6efe4; }
.off { background: var(--off); }
.lead-text { max-width: 70ch; margin: 0 auto; text-align: center; font-size: 1.15rem; }
.on-dark .lead-text { color: #e6efe4; }

/* about split */
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
.split h2 { font-size: clamp(2.2rem, 4.6vw, 3.4rem); color: var(--green); }
.on-dark .split h2 { color: #fff; }
.split .photo { border-radius: 26px; border: 6px solid var(--lime); overflow: hidden; }
.split .photo img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
.ticks { list-style: none; padding: 0; margin: 22px 0 0; display: grid; gap: 12px; }
.ticks li { display: flex; gap: 12px; font-weight: 600; }
.ticks li::before { content: "✓"; flex: none; width: 28px; height: 28px; border-radius: 8px; background: var(--lime); color: var(--green-3); display: grid; place-items: center; font-weight: 900; }

/* service cards */
.cards { display: grid; gap: 26px; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); margin-top: 40px; }
.card { position: relative; display: flex; align-items: flex-end; min-height: 360px; border-radius: 26px; overflow: hidden; text-decoration: none; color: #fff; background: var(--green); }
.card img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform .5s; }
.card::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10, 77, 36, 0) 30%, rgba(10, 77, 36, .95) 88%); }
.card:hover img { transform: scale(1.06); }
.card .plus { position: absolute; z-index: 2; top: 20px; right: 20px; width: 58px; height: 58px; border-radius: 14px; background: var(--lime); border: 3px solid var(--green); color: var(--green); display: grid; place-items: center; font-size: 2.2rem; font-weight: 700; line-height: 1; transition: transform .2s; }
.card:hover .plus { transform: rotate(90deg); }
.card div { position: relative; z-index: 1; padding: 28px 30px; }
.card h3 { font-size: 2.1rem; margin: 0; }
.card p { margin: 6px 0 0; color: #d9e8d6; }

/* process */
.process { max-width: 860px; margin: 40px auto 0; border-left: 5px dashed var(--lime); padding-left: 34px; display: grid; gap: 10px; }
.process details { padding: 12px 0; }
.process summary { cursor: pointer; list-style: none; display: flex; align-items: baseline; gap: 22px; }
.process summary::-webkit-details-marker { display: none; }
.process .n { font-family: "Barlow Condensed", sans-serif; font-weight: 800; font-size: 3rem; color: var(--lime); line-height: 1; }
.process h3 { font-size: 1.9rem; color: var(--green); margin: 0; }
.process p { margin: 12px 0 0; font-size: 1.12rem; color: var(--muted); }

/* reviews */
.score { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 24px 50px; text-align: center; }
.score .big { font-family: "Barlow Condensed", sans-serif; font-weight: 800; font-size: clamp(6rem, 14vw, 9rem); line-height: .9; color: var(--yellow); }
.score .stars { color: var(--yellow); font-size: 2rem; letter-spacing: 6px; }
.score p { margin: 6px 0 0; font-size: 1.15rem; }

/* towns */
.towns { display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; margin-top: 34px; }
.towns span { background: #fff; border: 3px solid var(--green); color: var(--green); border-radius: 14px; padding: 10px 22px; font-family: "Barlow Condensed", sans-serif; font-weight: 800; font-size: 1.4rem; text-transform: uppercase; }

/* faq */
.faq { max-width: 900px; margin: 40px auto 0; display: grid; gap: 14px; }
.faq details { border: 3px solid var(--green); border-radius: 16px; padding: 0 22px; background: #fff; }
.faq summary { cursor: pointer; list-style: none; padding: 18px 0; font-weight: 700; font-size: 1.12rem; color: var(--green); display: flex; justify-content: space-between; gap: 16px; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; flex: none; width: 32px; height: 32px; border-radius: 9px; background: var(--lime); color: var(--green); display: grid; place-items: center; font-size: 1.5rem; line-height: 1; transition: transform .2s; }
.faq details[open] summary::after { transform: rotate(45deg); }
.faq p { margin: 0 0 20px; color: var(--muted); }

/* cta */
.cta { background: var(--green) center / cover no-repeat; position: relative; text-align: center; color: #fff; }
.cta::before { content: ""; position: absolute; inset: 0; background: rgba(7, 58, 27, .86); }
.cta .wrap { position: relative; }
.cta h2 { font-size: clamp(2.4rem, 6vw, 4.2rem); }
.cta p { max-width: 54ch; margin: 0 auto; font-size: 1.15rem; color: #e6efe4; }

/* page header */
.ph { position: relative; background: var(--green-3) center / cover no-repeat; color: #fff; text-align: center; padding: 80px 0 70px; }
.ph::before { content: ""; position: absolute; inset: 0; background: rgba(7, 58, 27, .86); }
.ph .wrap { position: relative; }
.crumbs { font-weight: 600; font-size: .95rem; color: var(--lime); margin-bottom: 14px; }
.crumbs a { color: #fff; text-decoration: none; }
.ph h1 { font-size: clamp(2.6rem, 6.4vw, 4.6rem); }
.ph p { max-width: 62ch; margin: 0 auto; font-size: 1.15rem; color: #e6efe4; }

/* service page */
.items { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; margin-top: 40px; }
.item { background: #fff; border: 3px solid var(--green); border-radius: 18px; padding: 24px; box-shadow: 6px 6px 0 var(--lime); }
.item h3 { font-size: 1.6rem; color: var(--green); margin-bottom: 6px; }
.item p { margin: 0; color: var(--muted); }
.prose p { color: var(--muted); }
.on-dark .prose p { color: #d9e8d6; }
.soon { text-align: center; max-width: 680px; margin: 0 auto; border: 4px dashed var(--lime); border-radius: 24px; padding: 50px 30px; }

/* form */
.form { background: #fff; border: 4px solid var(--green); border-radius: 24px; padding: 34px; display: grid; gap: 16px; box-shadow: 10px 10px 0 var(--lime); }
.form h2 { color: var(--green); font-size: 2.4rem; margin: 0; }
.form label { display: grid; gap: 6px; font-weight: 700; color: var(--green); }
.form input, .form select, .form textarea { font: inherit; width: 100%; padding: 14px 16px; border: 2px solid #c9d8c3; border-radius: 12px; background: var(--off); }
.form input:focus, .form select:focus, .form textarea:focus { outline: none; border-color: var(--lime); box-shadow: 0 0 0 3px rgba(140, 198, 63, .35); }
.form .note { font-size: .9rem; color: var(--muted); margin: 0; }

/* footer */
.ftr { background: var(--green-3); color: #c4d7c0; padding: 0 0 100px; }
.ftr::before { content: ""; display: block; height: 7px; background: linear-gradient(90deg, var(--lime) 0 78%, var(--yellow) 78% 100%); margin-bottom: 70px; }
.ftr .grid { display: grid; grid-template-columns: 1.3fr 1fr 1fr 1fr; gap: 40px; }
.ftr .logo img { width: 170px; }
.ftr h4 { font-family: "Barlow Condensed", sans-serif; font-weight: 800; text-transform: uppercase; color: var(--lime); font-size: 1.4rem; margin: 0 0 12px; }
.ftr ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 7px; }
.ftr a { text-decoration: none; }
.ftr a:hover { color: #fff; }
.ftr .tel { font-family: "Barlow Condensed", sans-serif; font-weight: 800; font-size: 2.2rem; color: #fff; }
.ftr .copy { margin-top: 50px; border-top: 1px solid rgba(255, 255, 255, .12); padding-top: 22px; font-size: .88rem; }

/* sticky mobile bar */
.mbar { display: none; position: fixed; left: 0; right: 0; bottom: 0; z-index: 40; grid-template-columns: 1fr 1fr; }
.mbar a { padding: 17px; text-align: center; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; text-decoration: none; }
.mbar a:first-child { background: var(--green); color: #fff; }
.mbar a:last-child { background: var(--yellow); color: var(--green); }

.rv { opacity: 0; transform: translateY(24px); transition: opacity .6s, transform .6s; }
.rv.in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .rv { opacity: 1; transform: none; transition: none; } }

@media (max-width: 1020px) {
  .menu { display: grid; place-items: center; }
  .nav { display: none; position: absolute; top: 99px; left: 0; right: 0; background: var(--green); flex-direction: column; align-items: stretch; gap: 0; padding: 6px 20px 24px; border-bottom: 7px solid var(--lime); }
  .nav.open { display: flex; }
  .nav a { padding: 14px 0; border-bottom: 1px solid rgba(255, 255, 255, .12); font-size: 1.5rem; }
  .nav .btn { margin-top: 16px; }
  .split { grid-template-columns: 1fr; }
  .ftr .grid { grid-template-columns: 1fr 1fr; }
  .mbar { display: grid; }
}
@media (max-width: 620px) {
  section { padding: 70px 0; }
  .hero { padding: 64px 0 130px; }
  .hero .btn, .actions .btn { width: 100%; min-width: 0; }
  .trust ul { flex-direction: column; gap: 12px; }
  .trust li { flex-direction: column; gap: 12px; }
  .cards { grid-template-columns: 1fr; }
  .card { min-height: 300px; }
  .ftr .grid { grid-template-columns: 1fr; }
  .form { padding: 24px; box-shadow: 6px 6px 0 var(--lime); }
  .process { padding-left: 22px; }
  .process .n { font-size: 2.4rem; }
  .process h3 { font-size: 1.6rem; }
}
'''


def header(cur=''):
    links = ''.join(f'<a href="~/{p}"{" aria-current=page" if cur == p else ""}>{n}</a>' for p, n in NAV)
    return f'''<header class="hdr"><div class="wrap">
  <a class="logo" href="~/"><img src="~~/images/logo.png" alt="Carolina Premier Lawn and Tree Services" width="286" height="150"></a>
  <button class="menu" data-menu aria-expanded="false" aria-label="Menu"><svg width="26" height="22" viewBox="0 0 26 22" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round"><path d="M2 3h22M2 11h22M2 19h22"/></svg></button>
  <nav class="nav" data-nav>{links}<a class="btn btn-yellow" href="~/contact/">Free Quote</a></nav>
</div></header>
<main>'''


def footer():
    svc = ''.join(f'<li><a href="~/services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    towns = ''.join(f'<li>{t["name"]}, NC</li>' for t in TOWNS)
    return f'''</main>
<footer class="ftr"><div class="wrap">
  <div class="grid">
    <div><a class="logo" href="~/"><img src="~~/images/logo.png" alt="Carolina Premier" width="286" height="150"></a>
      <p>Lawn care, landscaping, tree work, hardscaping and fencing across Apex and the Triangle. 100% insured.</p><a class="tel" href="{TEL}">{B["phone"]}</a></div>
    <div><h4>Services</h4><ul>{svc}</ul></div>
    <div><h4>Service Areas</h4><ul>{towns}</ul></div>
    <div><h4>Company</h4><ul><li><a href="~/about/">About</a></li><li><a href="~/projects/">Projects</a></li><li><a href="~/reviews/">Reviews</a></li><li><a href="~/contact/">Contact</a></li></ul></div>
  </div>
  <div class="copy">© 2026 {e(B["name"])} · Design concept D: Field Day</div>
</div></footer>
<div class="mbar"><a href="{TEL}">Call Now</a><a href="{SMS}">Text Us</a></div>'''


def title(text):
    return f'<h2 class="title">{text}</h2>{BRUSH}'


def cards(services):
    return '<div class="cards">' + ''.join(f'''<a class="card rv" href="~/services/{s["slug"]}/">
  {img(s["img"] + ".jpg", s["name"])}<span class="plus" aria-hidden="true">+</span>
  <div><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p></div></a>''' for s in services) + '</div>'


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items) + '</div>'


STEPS = [
    ('Free Estimate', 'Request a quote online or give us a call. We\'ll come out, look at your property, talk through what you want and give you a clear, upfront price.'),
    ('Scheduling', 'Once you\'re ready, we put your job on the calendar, or set up a recurring weekly or bi-weekly schedule for ongoing service.'),
    ('The Work', 'Our crew handles the job from start to finish, done right for Triangle soil and weather.'),
    ('Clean Up & Enjoy', 'We clean up, haul away the debris and leave your property looking its best.'),
]


def process():
    return '<div class="process">' + ''.join(f'''<details{" open" if i == 0 else ""} class="rv"><summary><span class="n">{i + 1:02d}.</span><h3>{t}</h3></summary><p>{e(d)}</p></details>'''
                                             for i, (t, d) in enumerate(STEPS)) + '</div>'


def cta(image='lawn.jpg'):
    return f'''<section class="cta" style="background-image:url('~~/images/{image}')"><div class="wrap rv">
  <h2>Ready for a better-looking yard?</h2>{BRUSH}
  <p>Free estimates across Apex and the Triangle. Call, text or request a quote online.</p>
  <div class="actions center"><a class="btn btn-green" href="~/contact/">Get a Free Quote</a><a class="btn btn-yellow" href="{TEL}">Call {B["phone"]}</a></div>
</div></section>'''


def ph(crumb, h1, lead, image):
    return f'''<section class="ph" style="background-image:url('~~/images/{image}')"><div class="wrap">
  <div class="crumbs"><a href="~/">Home</a> / {crumb}</div><h1>{h1}</h1>{BRUSH}<p>{lead}</p></div></section>'''


def trust():
    return '<div class="trust"><div class="wrap"><ul><li>100% Insured</li><li>5 Stars on Google</li><li>Homes, HOAs &amp; Businesses</li></ul></div></div>'


def home():
    towns = ''.join(f'<span>{t["name"]}</span>' for t in TOWNS)
    body = header() + f'''
<section class="hero" style="background-image:url('~~/images/hero-home.jpg')"><div class="wrap">
  <h1>Lawn, Landscape &amp; Tree Company in Apex, NC</h1>{BRUSH}
  <p>Carolina Premier keeps Triangle properties looking their best with lawn care, landscaping, tree services, hardscaping, fencing and even Christmas lights.</p>
  <div class="actions"><a class="btn btn-green" href="~/contact/">Get a Free Quote</a><a class="btn btn-yellow" href="~/services/">View Services</a></div>
</div></section>
{trust()}

<section><div class="wrap split">
  <div class="rv left"><h2>Apex's all-in-one outdoor crew</h2>{BRUSH}
    <p class="prose" style="color:var(--muted)">Most homeowners juggle a mowing company, a tree guy and a landscaper. With Carolina Premier, it's one call. We take care of the lawn every week, keep beds and shrubs sharp, take down problem trees, build patios and fences, and light up your house for the holidays.</p>
    <ul class="ticks"><li>100% insured on every job</li><li>Rated 5.0 by every Google reviewer</li><li>Free, upfront estimates</li><li>Local to Apex</li></ul></div>
  <div class="photo rv">{img("garden-path.jpg", "Landscaped garden path")}</div>
</div></section>

<section class="off"><div class="wrap">
  {title("Our Services")}
  <div class="actions center" style="margin-top:0"><a class="btn btn-green" href="~/contact/">Get a Free Quote</a></div>
  {cards(SERVICES)}
</div></section>

<section><div class="wrap">
  {title("Our Process")}
  <div class="actions center" style="margin-top:0"><a class="btn btn-green" href="~/contact/">Get a Free Quote</a></div>
  {process()}
</div></section>

<section class="on-dark"><div class="wrap">
  <div class="score rv"><div class="big">5.0</div><div><div class="stars">★★★★★</div><h2 style="font-size:2.6rem;margin:6px 0 0">{B["review_count"]} Five-Star Google Reviews</h2>
  <p>Every customer who reviewed us gave us five stars.</p><div class="actions"><a class="btn btn-yellow" href="~/reviews/">Read Reviews</a></div></div></div>
</div></section>

<section><div class="wrap">
  {title("Areas We Serve")}
  <p class="lead-text">Based in Apex, we serve homes, HOAs and businesses throughout southwest Wake County.</p>
  <div class="towns">{towns}</div>
</div></section>

<section class="off"><div class="wrap">{title("Common Questions")}{faq(HOME_FAQS)}</div></section>
{cta()}''' + footer()
    write(C, '', 'Carolina Premier Lawn & Tree | Concept D', body, FONTS)


def services_hub():
    body = header('services/') + ph('Services', 'Our Services', 'Seven services from one insured, 5-star rated local crew.', 'lawn.jpg') + f'''
<section class="off"><div class="wrap">{cards(SERVICES)}</div></section>
<section><div class="wrap">{title("Our Process")}{process()}</div></section>{cta()}''' + footer()
    write(C, 'services/', 'Services | Concept D', body, FONTS)


def service(s):
    items = ''.join(f'<div class="item rv"><h3>{e(n)}</h3><p>{e(d)}</p></div>' for n, d in s['items'])
    intro = ''.join(f'<p>{e(p)}</p>' for p in s['intro'])
    local = ''.join(f'<p>{e(p)}</p>' for p in s['local'])
    body = header('services/') + ph(f'<a href="~/services/">Services</a> / {e(s["name"])}', e(s['name']), e(s['lead']), s['img'] + '.jpg') + trust() + f'''
<section><div class="wrap split">
  <div class="rv left prose"><h2>{e(s["name"])} done right</h2>{BRUSH}{intro}
    <div class="actions"><a class="btn btn-green" href="~/contact/">Get a Free Quote</a></div></div>
  <div class="photo rv">{img(s["img"] + ".jpg", s["name"])}</div>
</div></section>
<section class="off"><div class="wrap">{title("What's Included")}<div class="items">{items}</div></div></section>
<section class="on-dark"><div class="wrap split">
  <div class="rv left prose"><h2>{e(s["local_title"])}</h2>{BRUSH}{local}</div>
  <div class="rv">{process()}</div>
</div></section>
<section class="off"><div class="wrap">{title("Common Questions")}{faq(s["faqs"])}</div></section>
<section><div class="wrap">{title("More Services")}{cards([o for o in SERVICES if o is not s][:3])}</div></section>
{cta(s["img"] + ".jpg")}''' + footer()
    write(C, f'services/{s["slug"]}/', f'{s["name"]} | Concept D', body, FONTS)


def areas():
    rows = ''.join(f'<div class="item rv"><h3>{t["name"]}, NC</h3><p>{e(t["lead"])}</p></div>' for t in TOWNS)
    body = header('service-areas/') + ph('Service Areas', 'Areas We Serve', 'Based in Apex and serving southwest Wake County.', 'trees.jpg') + f'''
<section class="off"><div class="wrap"><div class="items" style="margin-top:0">{rows}</div></div></section>{cta()}''' + footer()
    write(C, 'service-areas/', 'Service Areas | Concept D', body, FONTS)


def projects():
    body = header('projects/') + ph('Projects', 'Our Projects', 'Before-and-after photos from jobs across the Triangle.', 'garden.jpg') + f'''
<section><div class="wrap"><div class="soon rv"><h2 style="color:var(--green);font-size:2.6rem">Photos Coming Soon</h2>
<p style="color:var(--muted)">We're putting together before-and-after photos. Until then, see photos of our work on Google.</p>
<div class="actions center"><a class="btn btn-green" href="{B["google_url"]}" target="_blank" rel="noopener">See Photos on Google</a></div></div></div></section>{cta()}''' + footer()
    write(C, 'projects/', 'Projects | Concept D', body, FONTS)


def reviews():
    body = header('reviews/') + ph('Reviews', '5 Stars on Google', f'{B["review_count"]} reviews, every one of them five stars.', 'lawn.jpg') + f'''
<section class="on-dark"><div class="wrap"><div class="score rv"><div class="big">5.0</div><div><div class="stars">★★★★★</div>
<div class="actions"><a class="btn btn-yellow" href="{B["google_url"]}" target="_blank" rel="noopener">Read on Google</a><a class="btn btn-green" href="{B["google_url"]}" target="_blank" rel="noopener">Leave a Review</a></div></div></div></div></section>{cta()}''' + footer()
    write(C, 'reviews/', 'Reviews | Concept D', body, FONTS)


def about():
    body = header('about/') + ph('About', 'About Carolina Premier', 'Local to Apex. 100% insured. Rated five stars on Google.', 'garden.jpg') + trust() + f'''
<section><div class="wrap split">
  <div class="photo rv">{img("planting.jpg", "Planting by hand")}</div>
  <div class="rv left prose"><h2>Show up. Do it right. Leave it clean.</h2>{BRUSH}
  <p>Carolina Premier Lawn &amp; Tree Services LLC takes care of lawns, landscapes, trees, hardscapes and fences for homeowners, HOAs and businesses across Apex and the Triangle.</p>
  <p>Every job gets the same attention, from a weekly mow to a new patio: the right technique for Triangle clay and weather, and a clean property when we leave.</p>
  <ul class="ticks"><li>100% insured</li><li>5.0 stars on Google</li><li>Free estimates</li></ul></div>
</div></section>{cta()}''' + footer()
    write(C, 'about/', 'About | Concept D', body, FONTS)


def contact():
    opts = ''.join(f'<option>{e(s["name"])}</option>' for s in SERVICES)
    towns = ''.join(f'<option>{t["name"]}</option>' for t in TOWNS)
    body = header() + ph('Contact', 'Get a Free Quote', 'Send your request by text or give us a call.', 'lawn.jpg') + f'''
<section class="off"><div class="wrap split" style="align-items:start">
  <form class="form rv" data-sms><h2>Request a Quote</h2>
    <label>Name<input name="Name" required autocomplete="name"></label>
    <label>Property Address<input name="Address" required autocomplete="street-address"></label>
    <label>Town<select name="Town">{towns}<option>Other</option></select></label>
    <label>Service<select name="Service">{opts}</select></label>
    <label>Details<textarea name="Details" rows="4"></textarea></label>
    <button class="btn btn-green" type="submit">Send My Request</button>
    <p class="note">Opens your texting app with your request filled in.</p></form>
  <div class="rv left"><h2 style="color:var(--green);font-size:3rem">Call or Text</h2>{BRUSH}
    <a class="btn btn-yellow" href="{TEL}" style="font-size:1.4rem">{B["phone"]}</a>
    <ul class="ticks"><li>Free estimates</li><li>100% insured</li><li>5.0 stars on Google</li><li>Apex, Cary, Holly Springs, Fuquay-Varina, Morrisville &amp; SW Raleigh</li></ul></div>
</div></section>''' + footer()
    write(C, 'contact/', 'Contact | Concept D', body, FONTS)


def build():
    write_static(C, CSS)
    home(); services_hub()
    for s in SERVICES:
        service(s)
    areas(); projects(); reviews(); about(); contact()
    print('built', C)
