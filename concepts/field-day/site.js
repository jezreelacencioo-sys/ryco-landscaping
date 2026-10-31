const btn = document.querySelector('[data-menu]');
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
  window.location.href = 'sms:+19843818731?&body=' + encodeURIComponent(lines.join('\n'));
}));
