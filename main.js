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

// Before/after sliders on the projects page
document.querySelectorAll('.ba input').forEach((input) => {
  input.addEventListener('input', () => {
    input.parentElement.style.setProperty('--pos', input.value + '%');
  });
});

// Quote form: no server, so it opens a pre-filled text message to the business
const form = document.querySelector('#quote-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const d = new FormData(form);
    const body = [
      "Hi! I'd like a free estimate.",
      'Name: ' + d.get('name'),
      'Address: ' + d.get('address') + ', ' + d.get('town'),
      'Service: ' + d.get('service'),
      d.get('details') ? 'Details: ' + d.get('details') : '',
    ].filter(Boolean).join('\n');
    window.location.href = 'sms:+19843818731?&body=' + encodeURIComponent(body);
  });
}
