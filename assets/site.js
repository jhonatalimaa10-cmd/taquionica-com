document.documentElement.classList.add('js');
(function () {
  var t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  if (t && n) {
    t.addEventListener('click', function () {
      var open = n.classList.toggle('open');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
      t.textContent = open ? 'Close' : 'Menu';
    });
  }
  // Services menu
  var sb = document.querySelector('.nav-svc-btn'), sm = document.getElementById('svc-menu');
  function setMenu(open) { if (!sb) return; sm.classList.toggle('open', open); sb.setAttribute('aria-expanded', open ? 'true' : 'false'); }
  if (sb && sm) {
    sb.addEventListener('click', function (e) { e.stopPropagation(); setMenu(!sm.classList.contains('open')); });
    document.addEventListener('click', function (e) { if (!sm.contains(e.target)) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setMenu(false); sb.focus(); } });
  }
  // Close mobile nav after following an in-page link
  if (n) n.addEventListener('click', function (e) {
    if (e.target.tagName === 'A' && n.classList.contains('open')) { n.classList.remove('open'); t.setAttribute('aria-expanded', 'false'); t.textContent = 'Menu'; }
  });
  // Stack trace, drawn once
  var s = document.querySelector('.stack-list');
  if (s) {
    if (!('IntersectionObserver' in window)) s.classList.add('on');
    else { var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { s.classList.add('on'); io.disconnect(); } }); }, { threshold: 0.35 }); io.observe(s); }
  }
  // WhatsApp form: builds the message and opens WhatsApp
  document.querySelectorAll('.wa-form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true, data = {};
      f.querySelectorAll('input, select, textarea').forEach(function (el) {
        var v = (el.value || '').trim(); data[el.name] = v;
        var bad = !v || (el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
        el.setAttribute('aria-invalid', bad ? 'true' : 'false'); if (bad) ok = false;
      });
      var err = f.querySelector('.f-error');
      if (!ok) { err.hidden = false; var first = f.querySelector('[aria-invalid="true"]'); if (first) first.focus(); return; }
      err.hidden = true;
      var msg = 'Hello Taquionica, I would like to discuss a project.\n\n' +
        'Name: ' + data.name + '\nCompany: ' + data.company + '\nEmail: ' + data.email +
        '\nCountry: ' + data.country + '\nService: ' + data.service + '\n\nProject:\n' + data.message +
        '\n\nPage: ' + location.href.split('#')[0];
      var url = 'https://wa.me/' + f.getAttribute('data-wa') + '?text=' + encodeURIComponent(msg);
      var link = f.querySelector('.f-link'); link.href = url; f.querySelector('.f-fallback').hidden = false;
      var w = null; try { w = window.open(url, '_blank', 'noopener'); } catch (x) {}
      if (!w) { try { window.location.href = url; } catch (x) {} }
    });
  });
})();
