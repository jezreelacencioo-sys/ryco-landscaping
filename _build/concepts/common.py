"""Shared helpers for the design concepts in /concepts/. Each concept module builds a small
multi-page site from the same business content as the main site. Concepts are noindex."""
import pathlib
import sys
from html import escape

from PIL import Image

BUILD = pathlib.Path(__file__).resolve().parent.parent
ROOT = BUILD.parent
sys.path.insert(0, str(BUILD))
from content import BUSINESS, SERVICES, TOWNS, HOME_FAQS  # noqa: E402,F401

B = BUSINESS
TEL = 'tel:' + B['phone_e164']
SMS = 'sms:' + B['phone_e164']


def e(s):
    return escape(s, quote=False)


def img(name, alt='', cls='', lazy=True):
    """name is a path under the repo's images/ folder."""
    with Image.open(ROOT / 'images' / name) as im:
        w, h = im.size
    cls_attr = f' class="{cls}"' if cls else ''
    lazy_attr = ' loading="lazy"' if lazy else ''
    return f'<img src="~~/images/{name}" alt="{escape(alt)}" width="{w}" height="{h}"{cls_attr}{lazy_attr}>'


def write(concept, path, title, body, head_extra=''):
    """Write concepts/<concept>/<path>index.html. In markup, '~/' is the concept root and
    '~~/' is the repo root (shared images and assets)."""
    depth = path.count('/')
    to_concept = '../' * depth or './'
    to_root = '../' * (depth + 2)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<link rel="icon" href="~~/favicon.svg" type="image/svg+xml">
{head_extra}
<link rel="stylesheet" href="~/style.css">
</head>
<body>
{body}
<script src="~/site.js"></script>
</body>
</html>
'''
    for q in ('"', "'", '('):
        html = html.replace(q + '~~/', q + to_root).replace(q + '~/', q + to_concept)
    out = ROOT / 'concepts' / concept / path / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def pages(concept, build_fns):
    for fn in build_fns:
        fn()
    print(f'built concept {concept}')


SITE_JS = '''const btn = document.querySelector('[data-menu]');
const nav = document.querySelector('[data-nav]');
if (btn) btn.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  btn.setAttribute('aria-expanded', open);
});
const io = new IntersectionObserver((es) => es.forEach((x) => {
  if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); }
}), { threshold: 0.12 });
document.querySelectorAll('.rv').forEach((el) => io.observe(el));
document.querySelectorAll('form[data-sms]').forEach((form) => form.addEventListener('submit', (ev) => {
  ev.preventDefault();
  const d = new FormData(form);
  const lines = ["Hi! I'd like a free estimate."];
  for (const [k, v] of d.entries()) if (v) lines.push(k + ': ' + v);
  window.location.href = 'sms:+19843818731?&body=' + encodeURIComponent(lines.join('\\n'));
}));
'''


def write_static(concept, css):
    d = ROOT / 'concepts' / concept
    d.mkdir(parents=True, exist_ok=True)
    (d / 'style.css').write_text(css)
    (d / 'site.js').write_text(SITE_JS)


NAV = [('services/', 'Services'), ('service-areas/', 'Areas'), ('projects/', 'Projects'),
       ('reviews/', 'Reviews'), ('about/', 'About')]

ALL_PAGES = ['', 'services/', *[f'services/{s["slug"]}/' for s in SERVICES], 'service-areas/',
             'projects/', 'reviews/', 'about/', 'contact/']
