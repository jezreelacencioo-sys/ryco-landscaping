"""Builds the static site from content.py. Run from anywhere: python3 _build/build.py"""
import json
import pathlib
import shutil
import sys
from html import escape

from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content import SITE, BUSINESS, SERVICES, COMBOS, TOWNS, GUIDES, HOME_FAQS, REVIEWS, PROJECTS, SOCIAL  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
B = BUSINESS
TEL = 'tel:' + B['phone_e164']
SMS = 'sms:' + B['phone_e164']
MAILTO = 'mailto:' + B['email']
SVC = {s['slug']: s for s in SERVICES}
TOWN = {t['slug']: t for t in TOWNS}
SITEMAP = []


def e(s):
    return escape(s, quote=False)


def img_size(name):
    with Image.open(ROOT / 'images' / name) as im:
        return im.size


def img(name, alt='', cls=''):
    w, h = img_size(name)
    cls_attr = f' class="{cls}"' if cls else ''
    return f'<img src="~/images/{name}" alt="{escape(alt)}" width="{w}" height="{h}"{cls_attr} loading="lazy">'


# ------------------------------------------------------------------ schema

BUSINESS_LD = {
    '@type': 'LandscapingBusiness',
    '@id': SITE + '/#business',
    'name': B['name'],
    'url': SITE + '/',
    'telephone': B['phone_e164'],
    'email': B['email'],
    'openingHoursSpecification': [
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '07:00', 'closes': '19:00'},
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Saturday', 'opens': '07:00', 'closes': '17:00'},
    ],
    'logo': SITE + '/images/logo.png',
    'image': SITE + '/images/og-image.jpg',
    'address': {'@type': 'PostalAddress', 'addressLocality': B['city'], 'addressRegion': B['state'], 'addressCountry': 'US'},
    'areaServed': [{'@type': 'City', 'name': f"{t['name']}, NC"} for t in TOWNS],
}
if any(SOCIAL.values()):
    BUSINESS_LD['sameAs'] = [u for u in SOCIAL.values() if u]


def ld(*items):
    return ('<script type="application/ld+json">'
            + json.dumps({'@context': 'https://schema.org', '@graph': [BUSINESS_LD, *items]}, ensure_ascii=False)
            + '</script>')


def faq_ld(faqs):
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faqs]}


def crumbs_ld(crumbs):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': name, 'item': SITE + '/' + path}
        for i, (name, path) in enumerate(crumbs)]}


def ba_media(p):
    if not p.get('before'):
        return img(p['after'], alt=p['title'])
    return f'''<div class="ba" style="--pos:50%">
  {img(p["after"], alt=p["title"] + " after")}
  <div class="ba-before">{img(p["before"], alt=p["title"] + " before")}</div>
  <span class="ba-handle" aria-hidden="true"><svg viewBox="0 0 24 24" width="26" height="26"><path d="M9 6l-6 6 6 6M15 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
  <input type="range" min="0" max="100" value="50" aria-label="Before and after comparison slider">
  <span class="ba-tag ba-tag-b">Before</span><span class="ba-tag ba-tag-a">After</span>
</div>'''


def has_combo(s, t):
    return (s['slug'], t['slug']) in COMBOS


def combo_path(s, t):
    """The service-in-town page, or the main service page for services without town pages."""
    if not has_combo(s, t):
        return f'services/{s["slug"]}/'
    return f'service-areas/{t["slug"]}/{s["slug"]}/'


def combo_label(s, t):
    return f'{s["name"]} in {t["name"]}' if has_combo(s, t) else s['name']


# ------------------------------------------------------------------ chrome

LOGO = '<img src="~/images/logo.png" alt="Carolina Premier Lawn and Tree Services LLC" width="286" height="150">'

GRASS = ('<div class="grass" aria-hidden="true"><svg viewBox="0 0 1440 60" preserveAspectRatio="none"><path fill="#86cf45" d="M0 60 L0 34 '
         + ' '.join(f'L{x} {y}' for x, y in zip(range(8, 1440, 8), [18, 32, 8, 30, 14, 32, 4, 30, 16, 34, 10, 32, 20, 34, 6, 30, 18, 34, 12, 32, 22, 34] * 9))
         + ' L1440 34 L1440 60 Z"/></svg></div>')


def header(path):
    def cur(prefix):
        return ' aria-current="page"' if path.startswith(prefix) else ''
    svc_links = ''.join(f'<a href="~/services/{s["slug"]}/">{e(s["name"])}</a>' for s in SERVICES)
    town_links = ''.join(f'<a href="~/service-areas/{t["slug"]}/">{t["name"]}, NC</a>' for t in TOWNS)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar">
  <a href="~/contact/">Get a Free Estimate</a>
  <a href="{TEL}">Call<span class="hide-sm"> Now:</span> {B["phone"]}</a>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="~/" aria-label="{e(B["name"])} home">{LOGO}</a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <div class="dd"><a href="~/services/"{cur("services/")}>Services</a><div class="dd-menu">{svc_links}</div></div>
      <div class="dd"><a href="~/service-areas/"{cur("service-areas/")}>Service Areas</a><div class="dd-menu">{town_links}</div></div>
      <a href="~/projects/"{cur("projects/")}>Projects</a>
      <a href="~/reviews/"{cur("reviews/")}>Reviews</a>
      <a href="~/about/"{cur("about/")}>About</a>
      <a class="btn btn-lime" href="~/contact/">Free Estimate</a>
    </nav>
  </div>
</header>
'''


SOCIAL_ICONS = {
    'facebook': ('Facebook', '<path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v7h4v-7H16l.6-4h-3.1V9c0-.6.4-1 1-1z"/>'),
    'instagram': ('Instagram', '<path d="M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4zm5 5a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm5.5-1.5a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" fill-rule="evenodd"/>'),
}


def social_links():
    links = ''.join(f'<a href="{url}" target="_blank" rel="noopener" aria-label="{SOCIAL_ICONS[k][0]}"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true">{SOCIAL_ICONS[k][1]}</svg></a>'
                    for k, url in SOCIAL.items() if url)
    return f'<div class="social">{links}</div>' if links else ''


def guarantee_block(cls='off'):
    return f'''<section class="{cls}">
  <div class="wrap guarantee reveal">
    <div class="seal" aria-hidden="true">
      <svg viewBox="0 0 200 200"><defs><path id="seal-circ" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs>
      <text><textPath href="#seal-circ" textLength="486" lengthAdjust="spacing">SATISFACTION GUARANTEED ✦ SATISFACTION GUARANTEED ✦ </textPath></text></svg>
      <span>100%<small>Guaranteed</small></span>
    </div>
    <div>
      <div class="eyebrow">Our promise</div>
      <h2>Not happy? We'll make it <span class="hl">right.</span></h2>
      <p>Your satisfaction is guaranteed. If anything about our work isn't right, just let us know and we'll come back and fix it. No hassle, no runaround.</p>
      <div class="actions"><a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a></div>
    </div>
  </div>
</section>
'''


def footer():
    svc = ''.join(f'<li><a href="~/services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    towns = ''.join(f'<li><a href="~/service-areas/{t["slug"]}/">{t["name"]}, NC</a></li>' for t in TOWNS)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="logo" href="~/">{LOGO}</a>
        <p>Lawn care, tree services and landscaping for homes in Apex, NC and the surrounding Triangle.</p>
        <p><a class="footer-phone" href="{TEL}">{B["phone"]}</a><br><a href="{MAILTO}">{B["email"]}</a><br>Apex, NC<br>{B["hours"]}</p>
        {social_links()}
        <p><span class="stars">★★★★★</span> {B["rating"]} on Google · {B["review_count"]} reviews</p>
      </div>
      <div><h2 class="foot-h">Services</h2><ul>{svc}</ul></div>
      <div><h2 class="foot-h">Service Areas</h2><ul>{towns}</ul></div>
      <div><h2 class="foot-h">Company</h2><ul>
        <li><a href="~/about/">About Us</a></li>
        <li><a href="~/projects/">Projects</a></li>
        <li><a href="~/reviews/">Reviews</a></li>
        <li><a href="~/lawn-care-guides/">Lawn Care Guides</a></li>
        <li><a href="~/contact/">Contact</a></li>
      </ul></div>
    </div>
    <div class="copyright">© 2026 {e(B["name"])}. All rights reserved.</div>
  </div>
</footer>
<div class="mobile-bar">
  <a href="{TEL}">Call Now</a>
  <a href="{SMS}">Text Us</a>
</div>
<script src="~/main.js"></script>
'''


def page(path, title, desc, body, schema=(), og_img='og-image.jpg', preload=None, og_type='website', index=True):
    """path: '' for home, 'services/' etc. Writes path/index.html with relative links."""
    depth = path.count('/')
    prefix = '../' * depth if depth else './'
    url = SITE + '/' + path
    pre = f'<link rel="preload" as="image" href="~/images/{preload}">\n' if preload else ''
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b0f0c">{'' if index else chr(10) + '<meta name="robots" content="noindex">'}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(B["name"])}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="~/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="~/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Lilita+One&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="~/styles.css">
{pre}{ld(*schema)}
</head>
<body>
{header(path)}<main id="main">
{body}</main>
{footer()}</body>
</html>
'''
    html = html.replace('"~/', '"' + prefix).replace("'~/", "'" + prefix).replace('(~/', '(' + prefix)
    out = ROOT / (path + 'index.html' if path.endswith('/') or path == '' else path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    if index:
        SITEMAP.append(url)


# ------------------------------------------------------------------ building blocks

def breadcrumbs(crumbs):
    parts = []
    for i, (name, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<span aria-current="page">{e(name)}</span>')
        else:
            parts.append(f'<a href="~/{p}">{e(name)}</a>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ' <span aria-hidden="true">/</span> '.join(parts) + '</nav>'


def page_hero(image, eyebrow, h1, lead, crumbs=None, buttons=True):
    btns = f'''
    <div class="actions">
      <a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a>
      <a class="btn btn-outline" href="{TEL}">Call {B["phone"]}</a>
    </div>''' if buttons else ''
    return f'''<section class="page-hero" style="background-image:url('~/images/{image}')">
  <div class="wrap">
    {breadcrumbs(crumbs) if crumbs else ''}
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>{btns}
  </div>
</section>
'''


def svc_card(s):
    return f'''<a class="svc reveal" href="~/services/{s["slug"]}/">
  {img(s["img"] + ".jpg")}<span class="plus" aria-hidden="true">+</span>
  <div>
    <h3>{e(s["name"])}</h3>
    <p>{e(s["short"])}</p>
    <span class="more">Learn more →</span>
  </div>
</a>'''


def svc_grid(services, cta=False):
    cards = [svc_card(s) for s in services]
    if cta:
        cards.append('''<a class="svc svc-cta reveal" href="~/contact/">
  <div>
    <h3>Not sure what you need?</h3>
    <p>Tell us about your property and we'll put together a free estimate.</p>
    <span class="more">Get a free estimate →</span>
  </div>
</a>''')
    return '<div class="cards">\n' + '\n'.join(cards) + '\n</div>'


def faq_block(faqs, title='Common questions', eyebrow='FAQ', cls='off'):
    items = '\n'.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)
    return f'''<section class="{cls}">
  <div class="wrap">
    <div class="section-head center reveal"><div class="eyebrow">{eyebrow}</div><h2>{title}</h2></div>
    <div class="faq reveal">
{items}
    </div>
  </div>
</section>
'''


STEPS = [
    ('Free Estimate', 'Call, text or request a quote online. We look at your property, talk through what you want and give you a clear, upfront price.'),
    ('Scheduling', 'Pick a date for your project, or set up weekly or bi-weekly service for ongoing care.'),
    ('The Work', 'Our crew handles it start to finish, done right for Triangle clay and weather.'),
    ('Clean Up & Enjoy', 'We clean up, haul away the debris and leave the property looking sharp.'),
]


def steps_block():
    steps = ''.join(f'<details class="reveal"{" open" if i == 0 else ""}><summary><span class="n">{i + 1:02d}</span><h3>{t}</h3></summary><p>{e(d)}</p></details>'
                    for i, (t, d) in enumerate(STEPS))
    return f'''<section class="dark">
  <div class="wrap">
    <div class="section-head center reveal"><div class="eyebrow">How it works</div><h2>Getting started is <span class="hl">easy</span></h2></div>
    <div class="process">{steps}</div>
  </div>
</section>
'''


def review_cards(limit=None):
    if not REVIEWS:
        return ''
    cards = '\n'.join(f'''<figure class="review reveal">
  <div class="stars">★★★★★</div>
  <blockquote>{e(r["text"])}</blockquote>
  <figcaption><b>{e(r["name"])}</b>{" · " + e(r["service"]) if r.get("service") else ""}</figcaption>
</figure>''' for r in REVIEWS[:limit])
    return f'<div class="reviews-grid">\n{cards}\n</div>'


def reviews_band():
    cards = review_cards(limit=3)
    return f'''<section class="dark">
  <div class="wrap">
    <div class="reviews-card reveal">
      <div class="big-num"><span class="n">{B["review_count"]}</span><span class="l">5-Star<br>Google Reviews</span></div>
      <div>
        <div class="stars big">★★★★★</div>
        <h2>Top-rated by our <span class="hl">neighbors</span></h2>
        <p>Every one of our Google reviews is five stars. See what Triangle homeowners say about working with us.</p>
        <div class="actions"><a class="btn btn-lime" href="~/reviews/">See Reviews</a></div>
      </div>
    </div>
    {cards}
  </div>
</section>
'''


def cta_band(title='Ready for a better-looking yard?'):
    return f'''<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>{title}</h2>
      <p>Free estimates across Apex and the Triangle. Call or text today.</p>
    </div>
    <div class="actions">
      <a class="btn btn-dark" href="{TEL}">Call {B["phone"]}</a>
      <a class="btn btn-dark" href="~/contact/">Get a Free Estimate</a>
    </div>
  </div>
</section>
'''


def town_chips(link_suffix=''):
    return '<ul class="towns">' + ''.join(
        f'<li><a href="~/service-areas/{t["slug"]}/">{t["name"]}{link_suffix}</a></li>' for t in TOWNS) + '</ul>'


def map_embed(q, zoom=11):
    return (f'<iframe class="map reveal" title="Map of {e(q)}" src="https://www.google.com/maps?q={q.replace(" ", "+")}'
            f'&amp;z={zoom}&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>')


def guide_card(g):
    return f'''<a class="guide reveal" href="~/lawn-care-guides/{g["slug"]}/">
  {img(g["img"] + ".jpg")}
  <div><h3>{e(g["title"])}</h3><p>{e(g["summary"])}</p><span class="more">Read the guide →</span></div>
</a>'''


def ticker():
    items = ''.join(f'<span>{e(s["name"])}</span>' for s in SERVICES)
    return f'<div class="ticker" aria-hidden="true"><div class="ticker-track">{items}{items}</div></div>'


BADGE = '''<div class="badge" aria-hidden="true">
  <svg viewBox="0 0 200 200"><defs><path id="circ" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs>
  <text><textPath href="#circ" textLength="486" lengthAdjust="spacing">5-STAR RATED ✦ 100% INSURED ✦ APEX, NC ✦ </textPath></text></svg>
  <span>5.0<small>★★★★★</small></span>
</div>'''


def before_after_home():
    featured = [p for p in PROJECTS if p.get('featured') and p.get('before')][:2]
    if not featured:
        return ''
    items = '\n'.join(f'''<figure class="project reveal">
  {ba_media(p)}
  <figcaption><h3>{e(p["title"])}</h3><p class="meta">{e(SVC[p["service"]]["name"]) if p.get("service") in SVC else ""}</p></figcaption>
</figure>''' for p in featured)
    return f'''<section class="off">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Before &amp; after</div>
      <h2>See the <span class="hl">difference</span></h2>
      <p>Drag the slider to compare. These are real jobs from our crew.</p>
    </div>
    <div class="projects home-ba">
{items}
    </div>
    <div class="actions"><a class="btn btn-dark" href="~/projects/">See More Projects</a></div>
  </div>
</section>
'''


# ------------------------------------------------------------------ pages

def build_home():
    services_cards = svc_grid(SERVICES, cta=True)
    guides = '\n'.join(guide_card(g) for g in GUIDES)
    body = f'''<section class="hero" style="background-image:url('~/images/work/hero.jpg')">
  <div class="wrap">
    <div class="hero-copy">
      <div class="eyebrow">Landscaping · Hardscaping · Tree Services</div>
      <h1>Lawn &amp; Tree Care in <span class="hl">Apex, NC</span></h1>
      <p class="lead">Lawn care, landscaping, tree work and hardscaping for a healthier, better-looking property all year long. 100% insured.</p>
      <div class="actions">
        <a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a>
        <a class="btn btn-outline" href="~/services/">View Services</a>
      </div>
    </div>
    {BADGE}
  </div>
</section>
{GRASS}
<div class="trust">
  <ul>
    <li>5 Stars on Google</li>
    <li>100% Insured</li>
    <li>Free Estimates</li>
  </ul>
</div>
{ticker()}
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">What we do</div>
      <h2>Everything your yard needs, <span class="hl">one call</span></h2>
      <p>From weekly mowing to new patios, tree removal and even Christmas lights, we take care of the whole property so you don't have to juggle different companies.</p>
    </div>
    {services_cards}
  </div>
</section>
{before_after_home()}{reviews_band()}
<section>
  <div class="wrap split">
    {img("work/mulch-walkway.jpg", cls="reveal rounded")}
    <div class="reveal">
      <div class="eyebrow">Why Carolina Premier</div>
      <h2>Local crew. <span class="hl">Pro results.</span></h2>
      <p>We're based right here in Apex, so we know Triangle yards: the red clay, the summer heat and the fescue that needs extra care every fall.</p>
      <ul class="checks">
        <li>100% insured on every job</li>
        <li>Lawn, landscape, tree and hardscape work from one company</li>
        <li>Free, no-pressure estimates</li>
        <li>Rated 5 stars on Google</li>
        <li>Satisfaction guaranteed</li>
      </ul>
      <a class="btn btn-lime" href="~/about/">About Us</a>
    </div>
  </div>
</section>
{guarantee_block(cls='')}{steps_block()}
<section class="off">
  <div class="wrap split">
    <div class="reveal">
      <div class="eyebrow">Service areas</div>
      <h2>Proudly serving <span class="hl">Apex</span> &amp; the Triangle</h2>
      <p>Based in Apex, we work throughout southwest Wake County. Pick your town to see how we help homeowners there.</p>
      {town_chips(", NC")}
    </div>
    {map_embed("Apex, NC")}
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Lawn care guides</div>
      <h2>Tips for <span class="hl">Triangle</span> yards</h2>
      <p>Straightforward advice for lawns, beds and trees in our part of North Carolina.</p>
    </div>
    <div class="guides">{guides}</div>
  </div>
</section>
{faq_block(HOME_FAQS)}{cta_band()}'''
    website = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': B['name'],
               'publisher': {'@id': SITE + '/#business'}}
    page('', 'Carolina Premier Lawn & Tree | Lawn Care in Apex, NC',
         'Lawn care, landscaping, tree removal, patios, fencing and Christmas lights in Apex, Cary, Holly Springs and the Triangle. 5-star rated, 100% insured.',
         body, schema=[website, faq_ld(HOME_FAQS)], preload='work/hero.jpg')


def build_services_hub():
    crumbs = [('Home', ''), ('Services', 'services/')]
    body = page_hero('work/backyard-walkway.jpg', 'Our services', 'Lawn, Tree &amp; <span class="hl">Landscape</span> Services',
                     'Everything outside your home or property, handled by one local, 5-star rated and 100% insured crew.', crumbs) + f'''<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Pick a service</div><h2>What can we <span class="hl">help with?</span></h2></div>
    {svc_grid(SERVICES, cta=True)}
  </div>
</section>
{steps_block()}{reviews_band()}{cta_band()}'''
    page('services/', 'Lawn, Tree & Landscaping Services in Apex, NC | Carolina Premier',
         'Lawn care, landscaping, tree services, hardscaping and fencing, Christmas lighting and commercial and HOA maintenance in Apex, NC and the Triangle.',
         body, schema=[crumbs_ld(crumbs)], preload='work/backyard-walkway.jpg')


def build_service(s):
    path = f'services/{s["slug"]}/'
    crumbs = [('Home', ''), ('Services', 'services/'), (s['name'], path)]
    intro = ''.join(f'<p>{e(p)}</p>' for p in s['intro'])
    local = ''.join(f'<p>{e(p)}</p>' for p in s['local'])
    items = '\n'.join(f'<div class="item reveal"><h3>{e(n)}</h3><p>{e(d)}</p></div>' for n, d in s['items'])
    related = svc_grid([o for o in SERVICES if o is not s][:3])
    area_links = '<ul class="towns">' + ''.join(
        f'<li><a href="~/{combo_path(s, t)}">{e(s["name"])} in {t["name"]}</a></li>' if has_combo(s, t)
        else f'<li><a href="~/service-areas/{t["slug"]}/">{t["name"]}, NC</a></li>' for t in TOWNS) + '</ul>'
    guides = [g for g in GUIDES if s['slug'] in g['related_services']]
    guide_html = ''
    if guides:
        guide_html = f'''<section class="off">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Learn more</div><h2>Helpful <span class="hl">guides</span></h2></div>
    <div class="guides">{''.join(guide_card(g) for g in guides)}</div>
  </div>
</section>
'''
    body = page_hero(s['img'] + '.jpg', 'Apex &amp; the Triangle', s['h1'], e(s['lead']), crumbs) + f'''<section>
  <div class="wrap split top">
    <div class="reveal prose">
      <div class="eyebrow">{e(s["name"])}</div>
      <h2>Done right, <span class="hl">every time</span></h2>
      {intro}
    </div>
    <aside class="include-card reveal">
      <h3>Why us</h3>
      <ul class="checks"><li>100% insured</li><li>Satisfaction guaranteed</li><li>5.0 stars on Google</li><li>Free estimates</li></ul>
      <a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a>
    </aside>
  </div>
</section>
<section class="off">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">What we offer</div><h2>{e(s["name"])} <span class="hl">services</span></h2></div>
    <div class="items">
{items}
    </div>
  </div>
</section>
<section class="dark">
  <div class="wrap split">
    <div class="reveal prose">
      <div class="eyebrow">Local know-how</div>
      <h2>{e(s["local_title"])}</h2>
      {local}
    </div>
    {img(s["img"] + ".jpg", cls="reveal rounded")}
  </div>
</section>
{steps_block().replace('class="dark"', 'class=""', 1)}{reviews_band()}{faq_block(s["faqs"], title=e(s["name"]) + " FAQ")}<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Service areas</div><h2>{e(s["name"])} <span class="hl">near you</span></h2>
    <p>Pick your town to see our {e(s["name"])} services there.</p></div>
    {area_links}
  </div>
</section>
<section class="off">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">More services</div><h2>Other ways we can <span class="hl">help</span></h2></div>
    {related}
  </div>
</section>
{guide_html}{cta_band()}'''
    service_ld = {'@type': 'Service', 'name': s['name'], 'serviceType': s['name'], 'description': s['short'],
                  'url': SITE + '/' + path, 'provider': {'@id': SITE + '/#business'},
                  'areaServed': [{'@type': 'City', 'name': f"{t['name']}, NC"} for t in TOWNS],
                  'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': s['name'], 'itemListElement': [
                      {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': n, 'description': d}} for n, d in s['items']]}}
    page(path, s['title'] + ' | Carolina Premier', s['desc'], body,
         schema=[service_ld, faq_ld(s['faqs']), crumbs_ld(crumbs)], preload=s['img'] + '.jpg')


def build_combo(s, t):
    path = combo_path(s, t)
    c = COMBOS[(s['slug'], t['slug'])]
    name = t['name']
    crumbs = [('Home', ''), ('Service Areas', 'service-areas/'), (f'{name}, NC', f'service-areas/{t["slug"]}/'), (s['name'], path)]
    body_html = ''.join(f'<p>{e(p)}</p>' for p in c['body'])
    includes = ''.join(f'<li>{e(n)}</li>' for n, _ in s['items'])
    others = '\n'.join(f'''<a class="svc-link reveal" href="~/{combo_path(o, t)}"><b>{e(combo_label(o, t))}</b><span>{e(o["short"])}</span></a>'''
                       for o in SERVICES if o is not s)
    nearby = '<ul class="towns">' + ''.join(
        f'<li><a href="~/{combo_path(s, TOWN[n])}">{e(s["name"])} in {TOWN[n]["name"]}</a></li>' for n in t['nearby']) \
        + f'<li><a href="~/services/{s["slug"]}/">All {e(s["name"])}</a></li></ul>'
    who = 'properties' if s['slug'] == 'commercial-hoa' else 'homes'
    body = page_hero(s['img'] + '.jpg', f'{name}, NC', f'{e(s["name"])} in <span class="hl">{name}, NC</span>',
                     e(c['lead']), crumbs) + f'''<section>
  <div class="wrap split top">
    <div class="reveal prose">
      <div class="eyebrow">{e(s["name"])} in {name}</div>
      <h2>Serving {name} <span class="hl">{who}</span></h2>
      {body_html}
      <a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a>
    </div>
    <aside class="include-card reveal">
      <h3>What we offer</h3>
      <ul class="checks">{includes}</ul>
      <p>100% insured · 5.0 stars on Google</p>
    </aside>
  </div>
</section>
{faq_block(c["faqs"], title=f"{e(s['name'])} in {name}: FAQ")}{reviews_band()}<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">More in {name}</div><h2>Other services in <span class="hl">{name}</span></h2></div>
    <div class="svc-links">
{others}
    </div>
  </div>
</section>
<section class="off">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Nearby</div><h2>{e(s["name"])} in <span class="hl">nearby towns</span></h2></div>
    {nearby}
  </div>
</section>
{cta_band(f"Get a free estimate in {name}")}'''
    service_ld = {'@type': 'Service', 'name': f'{s["name"]} in {name}, NC', 'serviceType': s['name'],
                  'description': c['lead'], 'url': SITE + '/' + path, 'provider': {'@id': SITE + '/#business'},
                  'areaServed': {'@type': 'City', 'name': f'{name}, NC'}}
    title = f'{s["name"]} in {name}, NC | Carolina Premier'
    if len(title) > 65:
        title = f'{s["name"]} in {name}, NC'
    page(path, title, f'{c["lead"]} Free estimates: {B["phone"]}.', body,
         schema=[service_ld, faq_ld(c['faqs']), crumbs_ld(crumbs)], preload=s['img'] + '.jpg')


def build_areas_hub():
    crumbs = [('Home', ''), ('Service Areas', 'service-areas/')]
    cards = '\n'.join(f'''<a class="town-card reveal" href="~/service-areas/{t["slug"]}/">
  <h3>{t["name"]}, NC</h3><p>{e(t["lead"])}</p><span class="more">Services in {t["name"]} →</span>
</a>''' for t in TOWNS)
    body = page_hero('work/tree-service.jpg', 'Where we work', 'Serving Apex &amp; the <span class="hl">Triangle</span>',
                     'Based in Apex, we serve homeowners throughout southwest Wake County.', crumbs) + f'''<section class="dark">
  <div class="wrap">
    <div class="town-grid">
{cards}
    </div>
  </div>
</section>
<section class="off">
  <div class="wrap">
    <div class="section-head reveal"><h2>Don't see your <span class="hl">town?</span></h2>
    <p>Give us a call or text. If you're nearby, there's a good chance we can still help.</p></div>
    {map_embed("Apex, NC", 10)}
  </div>
</section>
{cta_band()}'''
    page('service-areas/', 'Areas We Serve: Apex, Cary & Holly Springs | Carolina Premier',
         'Carolina Premier Lawn & Tree Services serves Apex, Cary, Holly Springs, Fuquay-Varina, Morrisville and southwest Raleigh, NC.',
         body, schema=[crumbs_ld(crumbs)], preload='work/tree-service.jpg')


def build_town(t):
    path = f'service-areas/{t["slug"]}/'
    name = t['name']
    crumbs = [('Home', ''), ('Service Areas', 'service-areas/'), (f'{name}, NC', path)]
    intro = ''.join(f'<p>{e(p)}</p>' for p in t['intro'])
    challenges = '\n'.join(f'<div class="step reveal no-num"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t['challenges'])
    svc_links = '\n'.join(f'''<a class="svc-link reveal" href="~/{combo_path(s, t)}"><b>{e(s["name"])}</b><span>{e(s["short"])}</span></a>''' for s in SERVICES)
    nearby = '<ul class="towns">' + ''.join(
        f'<li><a href="~/service-areas/{n}/">{TOWN[n]["name"]}, NC</a></li>' for n in t['nearby']) + '</ul>'
    body = page_hero(t['img'] + '.jpg', f'Serving {name}, NC', f'Lawn Care &amp; Tree Services in <span class="hl">{name}, NC</span>',
                     e(t['lead']), crumbs) + f'''<section>
  <div class="wrap split">
    <div class="reveal prose">
      <div class="eyebrow">{name} homeowners</div>
      <h2>Your {name} <span class="hl">lawn &amp; tree</span> team</h2>
      {intro}
      <a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a>
    </div>
    {map_embed(f"{name}, NC", 12)}
  </div>
</section>
<section class="dark">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Local challenges</div><h2>What {name} yards <span class="hl">deal with</span></h2></div>
    <div class="steps">
{challenges}
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Services in {name}</div><h2>How we help in <span class="hl">{name}</span></h2></div>
    <div class="svc-links">
{svc_links}
    </div>
  </div>
</section>
{reviews_band()}{faq_block(t["faqs"], title=f"{name} FAQ")}<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Nearby</div><h2>We also <span class="hl">serve</span></h2></div>
    {nearby}
  </div>
</section>
{cta_band(f"Need help with your {name} yard?")}'''
    page(path, f'Lawn Care & Tree Services in {name}, NC | Carolina Premier',
         f'Lawn care, landscaping, tree services, patios, fencing and Christmas lights in {name}, NC. 5-star rated and 100% insured. Free estimates: (984) 381-8731.',
         body, schema=[faq_ld(t['faqs']), crumbs_ld(crumbs)], preload=t['img'] + '.jpg')


def build_projects():
    crumbs = [('Home', ''), ('Projects', 'projects/')]
    if PROJECTS:
        items = []
        for p in PROJECTS:
            media = ba_media(p)
            svc = SVC.get(p.get('service'))
            svc_link = f'<a href="~/services/{svc["slug"]}/">{e(svc["name"])}</a>' if svc else ''
            items.append(f'''<figure class="project reveal">
  {media}
  <figcaption><h3>{e(p["title"])}</h3><p class="meta">{" · ".join(x for x in (e(p.get("town", "")), svc_link) if x)}</p><p>{e(p.get("text", ""))}</p></figcaption>
</figure>''')
        gallery = '<div class="projects">\n' + '\n'.join(items) + '\n</div>'
    else:
        gallery = f'''<div class="coming-soon reveal">
  <h2>Project photos <span class="hl">coming soon</span></h2>
  <p>We're putting together before-and-after photos of our recent lawn, tree and landscape work. In the meantime, you can see photos of our work on our Google profile.</p>
  <div class="actions" style="justify-content:center">
    <a class="btn btn-lime" href="{B["google_url"]}" target="_blank" rel="noopener">See Photos on Google</a>
    <a class="btn btn-dark" href="~/contact/">Get a Free Estimate</a>
  </div>
</div>'''
    body = page_hero('work/front-yard.jpg', 'Our work', 'Recent <span class="hl">Projects</span>',
                     'Lawns, trees and landscapes we have transformed across Apex and the Triangle.', crumbs, buttons=False) + f'''<section class="off">
  <div class="wrap">
    {gallery}
  </div>
</section>
{cta_band("Want results like these?")}'''
    page('projects/', 'Our Projects: Lawn & Tree Work in Apex, NC | Carolina Premier',
         'See recent lawn care, tree trimming and landscaping projects by Carolina Premier Lawn & Tree Services in Apex and the Triangle.',
         body, schema=[crumbs_ld(crumbs)], preload='work/front-yard.jpg')


def build_reviews():
    crumbs = [('Home', ''), ('Reviews', 'reviews/')]
    cards = review_cards()
    if not cards:
        cards = f'''<div class="coming-soon reveal">
  <h2>Read our reviews <span class="hl">on Google</span></h2>
  <p>Our customers have left {B["review_count"]} reviews on Google, and every one of them is five stars. Click below to read them all.</p>
</div>'''
    body = page_hero('work/backyard-walkway.jpg', 'Customer reviews', f'<span class="hl">{B["rating"]}</span> Stars on Google',
                     f'{B["review_count"]} five-star reviews from homeowners across Apex and the Triangle.', crumbs, buttons=False) + f'''<section class="off">
  <div class="wrap">
    <div class="rating-hero reveal">
      <div class="rating-num">{B["rating"]}</div>
      <div>
        <div class="stars big">★★★★★</div>
        <p><b>{B["review_count"]} Google reviews</b>, all five stars</p>
        <div class="actions">
          <a class="btn btn-lime" href="{B["google_url"]}" target="_blank" rel="noopener">Read All Reviews on Google</a>
          <a class="btn btn-dark" href="{B["google_url"]}" target="_blank" rel="noopener">Leave Us a Review</a>
        </div>
      </div>
    </div>
    {cards}
  </div>
</section>
{cta_band("Join our happy customers")}'''
    page('reviews/', '5-Star Reviews | Carolina Premier Lawn & Tree, Apex NC',
         f'Carolina Premier Lawn & Tree Services is rated {B["rating"]} stars from {B["review_count"]} Google reviews. See what Apex and Triangle homeowners say.',
         body, schema=[crumbs_ld(crumbs)], preload='work/backyard-walkway.jpg')


def build_about():
    crumbs = [('Home', ''), ('About', 'about/')]
    body = page_hero('work/front-yard.jpg', 'About us', 'Your Local <span class="hl">Lawn &amp; Tree</span> Team',
                     'Based in Apex, NC and rated five stars by our customers.', crumbs) + f'''<section>
  <div class="wrap split">
    {img("work/planting.jpg", cls="reveal rounded")}
    <div class="reveal prose">
      <div class="eyebrow">Our story</div>
      <h2>Care you can <span class="hl">see</span></h2>
      <p>Carolina Premier Lawn &amp; Tree Services LLC takes care of lawns, trees and landscapes for homeowners across Apex and the Triangle. We show up, do the job right and leave your property looking its best.</p>
      <p>Our customers have given us a perfect five-star rating on Google, and we work hard to keep it that way on every job.</p>
      <a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a>
    </div>
  </div>
</section>
<section class="dark">
  <div class="wrap">
    <div class="section-head center reveal"><div class="eyebrow">What we stand for</div><h2>How we <span class="hl">work</span></h2></div>
    <div class="steps">
      <div class="step reveal no-num"><h3>Show up</h3><p>Reliable service on a schedule you can count on.</p></div>
      <div class="step reveal no-num"><h3>Do it right</h3><p>The right height, the right timing and the right technique for Triangle yards.</p></div>
      <div class="step reveal no-num"><h3>Leave it clean</h3><p>Every visit ends with a cleanup, so all you see is the result.</p></div>
    </div>
  </div>
</section>
{guarantee_block(cls='')}<section class="off">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Service areas</div><h2>Where we <span class="hl">work</span></h2></div>
    {town_chips(", NC")}
  </div>
</section>
{cta_band()}'''
    page('about/', 'About Us | Carolina Premier Lawn & Tree Services, Apex NC',
         'Carolina Premier Lawn & Tree Services LLC is a 5-star rated lawn care and tree service company based in Apex, NC, serving the Triangle.',
         body, schema=[crumbs_ld(crumbs)], preload='work/front-yard.jpg')


def build_contact():
    crumbs = [('Home', ''), ('Contact', 'contact/')]
    options = ''.join(f'<option>{e(s["name"])}</option>' for s in SERVICES)
    towns = ''.join(f'<option>{t["name"]}</option>' for t in TOWNS)
    body = page_hero('work/backyard-walkway.jpg', 'Contact us', 'Get Your <span class="hl">Free Estimate</span>',
                     "Fill out the form and we'll get back to you with a price. You'll get a confirmation email right away.", crumbs, buttons=False) + f'''<section class="off">
  <div class="wrap contact-grid">
    <form class="form reveal" action="https://formsubmit.co/{B["email"]}" method="POST">
      <h2>Book a free estimate</h2>
      <input type="hidden" name="_subject" value="New estimate request from your website">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="{SITE}/thank-you/">
      <input type="hidden" name="_autoresponse" value="Thanks for reaching out to Carolina Premier Lawn &amp; Tree Services! We got your estimate request and will get back to you soon with a price. Need us sooner? Call or text {B["phone"]}.">
      <input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off" aria-hidden="true">
      <label>Your name <input name="name" required autocomplete="name"></label>
      <div class="row">
        <label>Email <input name="email" type="email" required autocomplete="email"></label>
        <label>Phone <input name="phone" type="tel" required autocomplete="tel"></label>
      </div>
      <label>Property address <input name="address" required autocomplete="street-address"></label>
      <div class="row">
        <label>Town <select name="town">{towns}<option>Other</option></select></label>
        <label>Service needed <select name="service">{options}<option>Something else</option></select></label>
      </div>
      <div class="row">
        <label>Preferred date (optional) <input name="preferred_date" type="date"></label>
        <label>Preferred time (optional) <select name="preferred_time"><option>No preference</option><option>Morning (8–11)</option><option>Midday (11–2)</option><option>Afternoon (2–5)</option></select></label>
      </div>
      <label>Details (optional) <textarea name="details" rows="4" placeholder="Yard size, timing, anything we should know"></textarea></label>
      <button class="btn btn-lime" type="submit">Send My Request</button>
      <p class="form-note">You'll get a confirmation email as soon as you send this. Prefer to talk? Call or text <a href="{TEL}">{B["phone"]}</a>.</p>
    </form>
    <div class="info-card reveal">
      <div><h3>Call us</h3><a href="{TEL}">{B["phone"]}</a></div>
      <div><h3>Text us</h3><a href="{SMS}">{B["phone"]}</a></div>
      <div><h3>Email us</h3><a class="email" href="{MAILTO}">{B["email"]}</a></div>
      <div><h3>Hours</h3><p>Mon–Fri 7 AM – 7 PM<br>Saturday 7 AM – 5 PM</p></div>
      <div><h3>Fully covered</h3><p>100% insured, and satisfaction guaranteed</p></div>
      <div><h3>Service area</h3><p>Apex, Cary, Holly Springs, Fuquay-Varina, Morrisville and southwest Raleigh, NC</p></div>
      <div><h3>Reviews</h3><p><span class="stars">★★★★★</span> {B["rating"]} on Google from {B["review_count"]} reviews</p></div>
    </div>
  </div>
</section>
{faq_block(HOME_FAQS[:2], title="Before you reach out", cls="")}'''
    page('contact/', 'Free Estimate | Contact Carolina Premier Lawn & Tree, Apex NC',
         'Get a free estimate for lawn care, tree services or landscaping in Apex, NC and the Triangle. Call or text (984) 381-8731 or send a request online.',
         body, schema=[crumbs_ld(crumbs)], preload='work/backyard-walkway.jpg')


def build_thanks():
    body = page_hero('work/backyard-walkway.jpg', 'Request received', 'Thanks! We got <span class="hl">your request</span>',
                     "We'll get back to you soon with a price. Check your inbox for a confirmation email (and your spam folder, just in case).", buttons=False) + f'''<section class="off">
  <div class="wrap"><div class="coming-soon reveal">
    <h2>Need us <span class="hl">sooner?</span></h2>
    <p>Call or text {B["phone"]} and we'll take it from there.</p>
    <div class="actions" style="justify-content:center"><a class="btn btn-lime" href="{TEL}">Call {B["phone"]}</a><a class="btn btn-outline" href="~/">Back to Home</a></div>
  </div></div>
</section>
'''
    page('thank-you/', 'Thank You | Carolina Premier Lawn & Tree', 'Thanks for your estimate request.', body, index=False)


def build_guides():
    crumbs = [('Home', ''), ('Lawn Care Guides', 'lawn-care-guides/')]
    body = page_hero('work/mulch-walkway.jpg', 'Lawn care guides', 'Tips for <span class="hl">Triangle</span> Yards',
                     'Straightforward advice for lawns, beds and trees in our part of North Carolina.', crumbs, buttons=False) + f'''<section class="off">
  <div class="wrap"><div class="guides">{''.join(guide_card(g) for g in GUIDES)}</div></div>
</section>
{cta_band("Rather leave it to the pros?")}'''
    page('lawn-care-guides/', 'Lawn Care Guides for Apex & the Triangle | Carolina Premier',
         'Lawn, landscape and tree care advice for homeowners in Apex, Cary and the Triangle from Carolina Premier Lawn & Tree Services.',
         body, schema=[crumbs_ld(crumbs)], preload='work/mulch-walkway.jpg')

    for g in GUIDES:
        path = f'lawn-care-guides/{g["slug"]}/'
        gc = crumbs + [(g['title'], path)]
        related = svc_grid([SVC[r] for r in g['related_services']])
        others = [o for o in GUIDES if o is not g]
        body = page_hero(g['img'] + '.jpg', 'Lawn care guide', g['h1'], e(g['summary']), gc, buttons=False) + f'''<section>
  <div class="wrap article-grid">
    <article class="prose article">
      {g["body"]}
    </article>
    <aside class="article-side">
      <div class="include-card">
        <h3>Need a hand?</h3>
        <p>We take care of lawns, trees and beds across Apex and the Triangle.</p>
        <a class="btn btn-lime" href="~/contact/">Get a Free Estimate</a>
        <a class="side-phone" href="{TEL}">{B["phone"]}</a>
      </div>
      <div class="side-links"><h3>More guides</h3>{''.join(f'<a href="~/lawn-care-guides/{o["slug"]}/">{e(o["title"])}</a>' for o in others)}</div>
    </aside>
  </div>
</section>
<section class="off">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">Related services</div><h2>Let us <span class="hl">handle it</span></h2></div>
    {related}
  </div>
</section>
{cta_band()}'''
        article = {'@type': 'Article', 'headline': g['title'], 'description': g['desc'],
                   'image': SITE + f'/images/{g["img"]}.jpg', 'datePublished': '2026-10-31', 'dateModified': '2026-10-31',
                   'author': {'@id': SITE + '/#business'}, 'publisher': {'@id': SITE + '/#business'},
                   'mainEntityOfPage': SITE + '/' + path}
        page(path, g['title'] + ' | Carolina Premier', g['desc'], body,
             schema=[article, crumbs_ld(gc)], preload=g['img'] + '.jpg', og_type='article')


def build_404():
    body = f'''<section class="page-hero" style="background-image:url('~/images/work/backyard-walkway.jpg')">
  <div class="wrap">
    <div class="eyebrow">Error 404</div>
    <h1>This page got <span class="hl">mowed over</span></h1>
    <p class="lead">We couldn't find the page you were looking for.</p>
    <div class="actions"><a class="btn btn-lime" href="~/">Back to Home</a><a class="btn btn-outline" href="~/services/">View Services</a></div>
  </div>
</section>
'''
    page('404.html', 'Page Not Found | Carolina Premier Lawn & Tree', 'This page could not be found.', body, index=False)
    # 404 is served from any URL, so it needs absolute links
    p = ROOT / '404.html'
    p.write_text(p.read_text().replace('"./', '"' + SITE + '/').replace("'./", "'" + SITE + '/').replace('(./', '(' + SITE + '/'))


def build_sitemap():
    urls = '\n'.join(f'  <url><loc>{u}</loc><lastmod>2026-10-31</lastmod></url>' for u in SITEMAP)
    (ROOT / 'sitemap.xml').write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')


GENERATED = ['services', 'service-areas', 'projects', 'reviews', 'about', 'contact', 'lawn-care-guides', 'thank-you']

if __name__ == '__main__':
    for d in GENERATED:
        shutil.rmtree(ROOT / d, ignore_errors=True)
    build_home()
    build_services_hub()
    for s in SERVICES:
        build_service(s)
    build_areas_hub()
    for t in TOWNS:
        build_town(t)
        for s in SERVICES:
            if has_combo(s, t):
                build_combo(s, t)
    build_projects()
    build_reviews()
    build_about()
    build_contact()
    build_thanks()
    build_guides()
    build_404()
    build_sitemap()
    print(f'Built {len(SITEMAP)} pages + 404, sitemap.xml, robots.txt')
