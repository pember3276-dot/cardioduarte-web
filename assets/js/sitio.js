/* CARDIODUARTE · comportamiento común a las tres propuestas
   - Menú móvil accesible
   - Sombra del encabezado al desplazarse
   - Aparición suave de bloques (respeta "reducir movimiento")
   - Formulario de cita: validación y paso a WhatsApp
   - Botones que preseleccionan un servicio en el formulario */
(function () {
  var doc = document.documentElement;

  /* Menú móvil */
  var b = document.querySelector('.menu-btn'), m = document.getElementById('mnav');
  if (b && m) {
    var set = function (o) {
      m.hidden = !o;
      b.setAttribute('aria-expanded', o);
      b.setAttribute('aria-label', o ? 'Cerrar menú' : 'Abrir menú');
    };
    b.addEventListener('click', function () { set(m.hidden); });
    m.addEventListener('click', function (e) { if (e.target.tagName === 'A') set(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  }

  /* Encabezado */
  var top = document.querySelector('header.top');
  var onScroll = function () { if (top) top.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Aparición suave */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    doc.classList.add('anim');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 60 + 'ms';
      io.observe(el);
    });
  }


  /* Contadores (cifras que suben al aparecer) */
  var nums = document.querySelectorAll('[data-count]');
  if (!reduce && 'IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target, to = +el.getAttribute('data-count'), suf = el.getAttribute('data-suffix') || '', t0 = null;
        co.unobserve(el);
        (function step(t) { t0 = t0 || t; var k = Math.min(1, (t - t0) / 1100); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))) + suf; if (k < 1) requestAnimationFrame(step); })(performance.now());
      });
    }, { threshold: 0.4 });
    nums.forEach(function (n) { co.observe(n); });
  }

  /* Acordeones de un solo elemento abierto */
  document.querySelectorAll('details[data-acc]').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      document.querySelectorAll('details[data-acc="' + d.getAttribute('data-acc') + '"]').forEach(function (o) { if (o !== d) o.open = false; });
    });
  });

  /* Preseleccionar servicio */
  document.querySelectorAll('[data-servicio]').forEach(function (a) {
    a.addEventListener('click', function () {
      var s = document.getElementById('f-servicio');
      if (s) s.value = a.getAttribute('data-servicio');
    });
  });

  /* Formulario de cita */
  var f = document.getElementById('form-cita');
  if (!f) return;
  function v(id) { return document.getElementById(id).value.trim(); }
  function err(id, msg) { document.getElementById('e-' + id).textContent = msg; }
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = true, first = null;
    err('nombre', ''); err('tel', ''); err('ok', '');
    if (v('f-nombre').length < 3) { err('nombre', 'Escriba su nombre para poder llamarle.'); ok = false; first = first || 'f-nombre'; }
    if (v('f-tel').replace(/\D/g, '').length < 7) { err('tel', 'Escriba un número de celular válido, por ejemplo 300 123 4567.'); ok = false; first = first || 'f-tel'; }
    if (!document.getElementById('f-ok').checked) { err('ok', 'Para enviar la solicitud, marque la autorización de tratamiento de datos.'); ok = false; first = first || 'f-ok'; }
    if (!ok) { document.getElementById(first).focus(); return; }
    var txt = 'Hola, soy ' + v('f-nombre') + '. Quisiera una cita de ' + v('f-servicio') + ' (' + v('f-cobertura') + '), preferiblemente en la ' + v('f-franja').toLowerCase() + '.' + (v('f-msg') ? ' ' + v('f-msg') : '');
    document.getElementById('ok-name').textContent = v('f-nombre').split(' ')[0];
    document.getElementById('ok-wa').href = 'https://wa.me/573187984545?text=' + encodeURIComponent(txt);
    var box = document.getElementById('ok');
    box.hidden = false;
    box.scrollIntoView({ block: 'nearest', behavior: reduce ? 'auto' : 'smooth' });
    box.focus({ preventScroll: true });
  });
})();
