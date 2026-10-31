// Mobile menu
const menuBtn = document.querySelector('.menu-btn');
const nav = document.querySelector('.nav');
menuBtn.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', open);
});

// Fade sections in as they scroll into view
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// Before/after sliders: drag or tap anywhere on the photo; arrow keys via the hidden range input
document.querySelectorAll('.ba').forEach((ba) => {
  const input = ba.querySelector('input');
  const set = (pct) => {
    pct = Math.max(0, Math.min(100, pct));
    ba.style.setProperty('--pos', pct + '%');
    input.value = pct;
  };
  const fromEvent = (e) => {
    const r = ba.getBoundingClientRect();
    set(((e.clientX - r.left) / r.width) * 100);
  };
  ba.addEventListener('pointerdown', (e) => {
    ba.classList.add('dragging');
    ba.setPointerCapture(e.pointerId);
    fromEvent(e);
  });
  ba.addEventListener('pointermove', (e) => {
    if (ba.classList.contains('dragging')) fromEvent(e);
  });
  const stop = () => ba.classList.remove('dragging');
  ba.addEventListener('pointerup', stop);
  ba.addEventListener('pointercancel', stop);
  input.addEventListener('input', () => set(+input.value));
  ba.tabIndex = -1;
  ba.addEventListener('click', () => input.focus({ preventScroll: true }));
  // Nudge the handle once when it first scrolls into view so people know it moves
  const hint = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      ba.classList.add('hint');
      hint.disconnect();
    }
  }, { threshold: 0.6 });
  hint.observe(ba);
});
