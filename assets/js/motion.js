/* ==========================================================================
   GelaVit — experience layer
   Inertia scroll · preloader · custom cursor · scroll-driven scény ·
   horizontálny rail · reveals · fly-to-cart. Vanilla, bez závislostí.

   Pravidlá: animujeme len transform/opacity, 60 fps, všetko sa vypína pri
   prefers-reduced-motion, kurzorové efekty len na (pointer: fine).
   ========================================================================== */
(function () {
  'use strict';

  var mqReduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var reduce = mqReduce.matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var raf = window.requestAnimationFrame.bind(window);
  var clamp = function (v, a, b) { return v < a ? a : v > b ? b : v; };
  var lerp = function (a, b, t) { return a + (b - a) * t; };

  /* =======================================================================
     1. Inertia scroll — necháme natívny scroll (aby fungoval position:sticky),
        len ho tlmíme lerpom. Na dotyku sa nezapína.
     ======================================================================= */
  var Scroll = {
    y: window.scrollY, target: window.scrollY, active: false,
    listeners: [],
    on: function (fn) { this.listeners.push(fn); },
    to: function (top) {
      var max = document.documentElement.scrollHeight - innerHeight;
      top = clamp(top, 0, max);
      if (this.active) { this.target = top; }
      else { window.scrollTo({ top: top, behavior: 'smooth' }); }
    }
  };

  function inertiaScroll() {
    if (reduce || !fine) return;
    Scroll.active = true;
    Scroll.target = window.scrollY;
    document.documentElement.classList.add('has-inertia');

    var maxY = function () { return document.documentElement.scrollHeight - innerHeight; };

    addEventListener('wheel', function (e) {
      if (e.ctrlKey) return;
      if (e.target.closest('[data-native-scroll]')) return;
      e.preventDefault();
      Scroll.target = clamp(Scroll.target + e.deltaY * (e.deltaMode === 1 ? 22 : 1), 0, maxY());
    }, { passive: false });

    addEventListener('keydown', function (e) {
      var step = { PageDown: innerHeight * .85, PageUp: -innerHeight * .85,
                   ArrowDown: 90, ArrowUp: -90, Home: -1e7, End: 1e7, ' ': innerHeight * .8 }[e.key];
      if (step === undefined || /input|textarea|select/i.test(e.target.tagName)) return;
      Scroll.target = clamp(Scroll.target + step, 0, maxY());
    });

    addEventListener('resize', function () { Scroll.target = clamp(Scroll.target, 0, maxY()); });
  }

  /* Jedna rAF slučka pre celý web */
  function loop() {
    if (Scroll.active) {
      if (Math.abs(Scroll.target - Scroll.y) > 0.4) {
        Scroll.y = lerp(Scroll.y, Scroll.target, 0.105);
        window.scrollTo({ top: Scroll.y, behavior: 'instant' });
      } else {
        Scroll.y = Scroll.target;
      }
    } else {
      Scroll.y = window.scrollY;
    }
    for (var i = 0; i < Scroll.listeners.length; i++) Scroll.listeners[i](Scroll.y);
    raf(loop);
  }

  /* Scrollbar, dotyk, programový scroll, obnova pozície — prevezmi hodnotu */
  addEventListener('scroll', function () {
    if (!Scroll.active) return;
    // ak sa pozícia líši od tej, ktorú sme práve nastavili, scrolloval niekto iný
    if (Math.abs(window.scrollY - Scroll.y) > 3) { Scroll.y = Scroll.target = window.scrollY; }
  }, { passive: true });

  window.GelavitScroll = Scroll;

  /* =======================================================================
     2. Preloader — logo sa nadýchne, počítadlo beží, potom clona odíde hore
     ======================================================================= */
  function preloader() {
    var el = $('.preloader');
    if (!el) { document.body.classList.add('is-ready'); return; }
    var seen = false;
    try { seen = sessionStorage.getItem('gv_intro') === '1'; } catch (e) {}
    if (reduce || seen) {
      el.remove(); document.body.classList.add('is-ready', 'intro-done');
      return;
    }
    try { sessionStorage.setItem('gv_intro', '1'); } catch (e) {}
    var num = $('.preloader-num', el);
    var bar = $('.preloader-bar i', el);
    var start = performance.now();
    var min = 1000;

    (function tick(now) {
      var p = clamp((now - start) / min, 0, 1);
      var eased = 1 - Math.pow(1 - p, 2);
      if (num) num.textContent = Math.round(eased * 100).toString().padStart(2, '0');
      if (bar) bar.style.transform = 'scaleX(' + eased + ')';
      if (p < 1) raf(tick); else finish();
    })(start);

    function finish() {
      el.classList.add('is-out');
      document.body.classList.add('is-ready');
      setTimeout(function () {
        document.body.classList.add('intro-done');
        el.remove();
      }, 900);
    }
  }

  /* =======================================================================
     3. Vlastný kurzor — mäkký krúžok, ktorý sa mení podľa kontextu
     ======================================================================= */
  function cursor() {
    if (!fine || reduce) return;
    var dot = document.createElement('div');
    dot.className = 'cursor';
    dot.innerHTML = '<span class="cursor-label"></span><span class="cursor-coords"></span>';
    document.body.appendChild(dot);
    document.documentElement.classList.add('has-cursor');

    var label = $('.cursor-label', dot);
    var coords = $('.cursor-coords', dot);
    var x = innerWidth / 2, y = innerHeight / 2, cx = x, cy = y;

    addEventListener('pointermove', function (e) { x = e.clientX; y = e.clientY; }, { passive: true });
    addEventListener('pointerdown', function () { dot.classList.add('is-down'); });
    addEventListener('pointerup', function () { dot.classList.remove('is-down'); });
    addEventListener('mouseleave', function () { dot.classList.add('is-gone'); });
    addEventListener('mouseenter', function () { dot.classList.remove('is-gone'); });

    (function tick() {
      cx = lerp(cx, x, .19); cy = lerp(cy, y, .19);
      dot.style.transform = 'translate3d(' + (cx - dot.offsetWidth / 2) + 'px,' + (cy - dot.offsetHeight / 2) + 'px,0)';
      if (coords) coords.textContent = String(Math.round(x)).padStart(4, '0') + ' / ' + String(Math.round(y)).padStart(4, '0');
      raf(tick);
    })();

    document.addEventListener('pointerover', function (e) {
      var t = e.target.closest('[data-cursor], a, button, input, textarea, select, summary');
      if (!t) { dot.className = 'cursor'; label.textContent = ''; return; }
      var txt = t.getAttribute('data-cursor');
      if (txt) { dot.className = 'cursor is-label'; label.textContent = txt; }
      else if (/INPUT|TEXTAREA|SELECT/.test(t.tagName)) { dot.className = 'cursor is-text'; label.textContent = ''; }
      else { dot.className = 'cursor is-link'; label.textContent = ''; }
    });
  }

  /* =======================================================================
     4. Rozdelenie textu na znaky / riadky
     ======================================================================= */
  function splitText() {
    if (reduce) return;
    $$('[data-split]').forEach(function (h) {
      var lines = h.innerHTML.split(/<br\s*\/?>/i);
      h.innerHTML = lines.map(function (line, li) {
        // zachovaj vnorené tagy: rozdeľ len textové uzly
        var tmp = document.createElement('span');
        tmp.innerHTML = line;
        var out = '', i = 0;
        (function walk(node) {
          Array.prototype.forEach.call(node.childNodes, function (n) {
            if (n.nodeType === 3) {
              out += n.textContent.replace(/\S+/g, function (w) {
                return '<span class="w" style="--c:' + (i++) + '">' + w + '</span>';
              });
            } else {
              var open = '<' + n.tagName.toLowerCase() +
                (n.className ? ' class="' + n.className + '"' : '') + '>';
              out += open; walk(n); out += '</' + n.tagName.toLowerCase() + '>';
            }
          });
        })(tmp);
        return '<span class="line" style="--l:' + li + '"><span class="line-in">' + out + '</span></span>';
      }).join('');
    });
  }

  /* =======================================================================
     5. Reveals + počítadlá
     ======================================================================= */
  function reveals() {
    var sel = '.reveal, .reveal-img, [data-split], .steps-line, [data-count]';
    var targets = $$(sel);
    if (!('IntersectionObserver' in window)) {
      targets.forEach(function (el) { el.classList.add('is-in'); }); return;
    }
    $$('.products-grid, .feature-grid, .quote-grid, .post-grid, .stats, .rail-track').forEach(function (g) {
      $$('.reveal', g).forEach(function (el, i) { el.style.setProperty('--i', i); });
    });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        if (e.target.hasAttribute('data-count')) countUp(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -6% 0px' });
    targets.forEach(function (el) { io.observe(el); });
  }

  function countUp(el) {
    if (reduce) return;
    var raw = el.getAttribute('data-count');
    var m = raw.match(/^([^\d]*)([\d.,\s]*\d)(.*)$/);
    if (!m) return;
    var prefix = m[1], suffix = m[3];
    var num = parseFloat(m[2].replace(/\s/g, '').replace(',', '.'));
    if (!isFinite(num)) return;
    var dec = (String(num).split('.')[1] || '').length;
    var group = /\s/.test(m[2]);
    var t0 = performance.now(), dur = 1500;
    (function tick(now) {
      var p = clamp((now - t0) / dur, 0, 1);
      var v = (num * (1 - Math.pow(1 - p, 3))).toFixed(dec);
      var out = String(v).replace('.', ',');
      if (group) out = out.replace(/\B(?=(\d{3})+(?!\d))/g, '\u00a0');
      el.textContent = prefix + out + suffix;
      if (p < 1) raf(tick); else el.textContent = raw;
    })(t0);
  }

  /* =======================================================================
     6. Scroll-driven hero
     ======================================================================= */
  function heroScene() {
    var hero = $('.hero'); if (!hero) return;
    var slides = $$('.hero-slide', hero);
    var dots   = $$('.hero-dot', hero);
    var picks  = $$('.hero-pick-item', hero);
    var fill   = $('.hero-progress i', hero);
    var cue    = $('.scroll-cue', hero);
    var stage  = $('.hero-stage', hero);
    var ring   = $('.hero-ring', hero);
    if (!slides.length) return;

    var cur = -1;

    function setActive(idx) {
      if (idx === cur) return;
      cur = idx;
      slides.forEach(function (s, i) {
        var on = i === idx;
        s.classList.toggle('is-on', on);
        s.setAttribute('aria-hidden', on ? 'false' : 'true');
        s.setAttribute('tabindex', on ? '0' : '-1');
      });
      picks.forEach(function (s, i) {
        var on = i === idx;
        s.classList.toggle('is-on', on);
        var a = s.querySelector('a'); if (a) a.setAttribute('tabindex', on ? '0' : '-1');
      });
      dots.forEach(function (d, i) {
        d.classList.toggle('is-on', i === idx);
        d.setAttribute('aria-selected', i === idx ? 'true' : 'false');
      });
      if (stage) stage.style.setProperty('--stage-hue', slides[idx].dataset.hue || '#F04E4A');
      if (hero) hero.style.setProperty('--stage-hue', slides[idx].dataset.hue || '#F04E4A');
    }
    setActive(0);

    // mobil / reduced motion: klikacie prepínanie, žiadna pripnutá scéna
    var coarse = window.matchMedia('(hover: none)').matches;
    var staticMode = reduce || coarse || innerWidth < 980;
    if (staticMode) { hero.classList.add('is-static'); hero.style.height = 'auto'; }

    dots.forEach(function (d, i) {
      d.addEventListener('click', function () {
        if (staticMode) { setActive(i); return; }
        // pri scroll-driven scéne skoč na správnu výšku
        var total = hero.offsetHeight - innerHeight;
        var top = hero.offsetTop + total * ((i + 0.5) / slides.length);
        if (window.GelavitScroll && window.GelavitScroll.to) window.GelavitScroll.to(top);
        else window.scrollTo({ top: top, behavior: 'smooth' });
      });
    });

    if (staticMode) return;

    Scroll.on(function (y) {
      var total = hero.offsetHeight - innerHeight;
      if (total <= 0) return;
      var p = clamp(y / total, 0, 1);
      var idx = clamp(Math.floor(p * slides.length * 0.999), 0, slides.length - 1);
      setActive(idx);
      if (fill) fill.style.transform = 'scaleX(' + p.toFixed(4) + ')';
      if (ring) ring.style.transform = 'rotate(' + (p * 150).toFixed(2) + 'deg)';
      if (cue) cue.style.opacity = 1 - clamp(p * 3.4, 0, 1);
      var inner = (p * slides.length) % 1;
      slides[idx].style.setProperty('--drift', (inner - 0.5).toFixed(3));
    });
  }

  /* =======================================================================
     7. Signature scéna — pripnutý prehliadač príchutí
     ======================================================================= */
  function showcase() {
    var sec = $('.showcase'); if (!sec) return;
    var slides = $$('.showcase-slide', sec);
    var names = $$('.showcase-name', sec);
    var dots = $$('.showcase-dot', sec);
    var fill = $('.showcase-progress i', sec);
    if (!slides.length) return;

    function setActive(idx, p) {
      slides.forEach(function (s, i) { s.classList.toggle('is-on', i === idx); });
      names.forEach(function (s, i) { s.classList.toggle('is-on', i === idx); });
      dots.forEach(function (d, i) {
        d.classList.toggle('is-on', i === idx);
        d.setAttribute('aria-current', i === idx ? 'true' : 'false');
      });
      sec.style.setProperty('--tint', slides[idx].dataset.tint || '#F1E9DC');
      if (fill) fill.style.transform = 'scaleX(' + p + ')';
    }
    setActive(0, 0);

    // mobil / reduced motion: prepínanie klikom, bez scroll-driven scény
    if (reduce || innerWidth < 980 || window.matchMedia('(hover: none)').matches) {
      sec.classList.add('is-static');
      dots.forEach(function (d, i) {
        d.addEventListener('click', function () { setActive(i, (i + 1) / slides.length); });
      });
      return;
    }

    Scroll.on(function (y) {
      var r = sec.getBoundingClientRect();
      var total = sec.offsetHeight - innerHeight;
      if (total <= 0) return;
      var p = clamp(-r.top / total, 0, 1);
      var idx = clamp(Math.floor(p * slides.length * 0.999), 0, slides.length - 1);
      setActive(idx, p);
      var inner = (p * slides.length) % 1;
      slides[idx].style.setProperty('--drift', (inner - .5).toFixed(3));
    });

    dots.forEach(function (d, i) {
      d.addEventListener('click', function () {
        var total = sec.offsetHeight - innerHeight;
        var y = sec.offsetTop + total * ((i + .5) / slides.length);
        if (Scroll.active) Scroll.target = y; else scrollTo({ top: y, behavior: 'smooth' });
      });
    });

    addEventListener('resize', function () {
      if (innerWidth < 980 && !sec.classList.contains('is-static')) location.reload();
    });
  }

  /* =======================================================================
     8. Horizontálny rail ťahaný vertikálnym scrollom
     ======================================================================= */
  function rail() {
    var wrap = $('.rail'); if (!wrap) return;
    var track = $('.rail-track', wrap);
    if (!track) return;

    function distance() { return Math.max(0, track.scrollWidth - innerWidth + 80); }
    if (reduce || innerWidth < 900 || window.matchMedia('(hover: none)').matches) {
      wrap.classList.add('is-static');
      return;
    }
    function size() { wrap.style.height = (innerHeight + distance()) + 'px'; }
    size(); addEventListener('resize', size);

    Scroll.on(function () {
      var r = wrap.getBoundingClientRect();
      var total = wrap.offsetHeight - innerHeight;
      if (total <= 0) return;
      var p = clamp(-r.top / total, 0, 1);
      track.style.transform = 'translate3d(' + (-p * distance()) + 'px,0,0)';
    });
  }

  /* =======================================================================
     9. Paralax vrstiev s data-speed
     ======================================================================= */
  function parallax() {
    if (reduce) return;
    var items = $$('[data-speed]');
    if (!items.length) return;
    Scroll.on(function () {
      items.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > innerHeight + 200) return;
        var mid = r.top + r.height / 2 - innerHeight / 2;
        el.style.transform = 'translate3d(0,' + (-mid * parseFloat(el.dataset.speed)) + 'px,0)';
      });
    });
  }

  /* =======================================================================
     9b. Bočný index sekcií — 01 / 02 / 03 …
     ======================================================================= */
  function sectionIndex() {
    var secs = $$('[data-index]');
    if (secs.length < 3 || innerWidth < 1560) return;
    var nav = document.createElement('nav');
    nav.className = 'rail-index';
    nav.setAttribute('aria-label', 'Sekcie');
    nav.innerHTML = secs.map(function (s, i) {
      if (!s.id) s.id = 'sec-' + (i + 1);
      return '<a href="#' + s.id + '"><i></i>' + String(i + 1).padStart(2, '0') + '</a>';
    }).join('');
    document.body.appendChild(nav);
    var links = $$('a', nav);
    Scroll.on(function (y) {
      nav.classList.toggle('is-on', y > innerHeight * 0.7);
      var active = 0;
      secs.forEach(function (s, i) {
        if (s.getBoundingClientRect().top <= innerHeight * 0.45) active = i;
      });
      links.forEach(function (a, i) { a.classList.toggle('is-on', i === active); });
    });
  }

  /* =======================================================================
     10. Hlavička, progress, marquee
     ======================================================================= */
  function chrome() {
    var head = $('.site-header');
    var bar = document.createElement('div'); bar.className = 'progress';
    if (!reduce) document.body.appendChild(bar);
    var last = 0;
    Scroll.on(function (y) {
      if (head) {
        head.classList.toggle('is-stuck', y > 8);
        if (!reduce) head.classList.toggle('is-hidden', y > last + 2 && y > 300 && !$('.mobile-menu.is-open'));
      }
      if (!reduce) {
        var max = document.documentElement.scrollHeight - innerHeight;
        bar.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')';
      }
      last = y;
    });

    $$('.marquee-track').forEach(function (t) {
      if (t.children.length === 1) t.appendChild(t.firstElementChild.cloneNode(true));
    });
  }

  /* =======================================================================
     11. Prechod medzi stránkami — clona
     ======================================================================= */
  function transitions() {
    if (reduce) return;
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a');
      if (!a || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
      var href = a.getAttribute('href') || '';
      if (!href || href[0] === '#' || a.target === '_blank' || a.hasAttribute('download')) return;
      if (/^(mailto:|tel:)/.test(href)) return;
      if (a.hostname && a.hostname !== location.hostname) return;
      e.preventDefault();
      document.body.classList.add('is-leaving');
      setTimeout(function () { location.href = a.href; }, 430);
    });
    addEventListener('pageshow', function (ev) {
      if (ev.persisted) document.body.classList.remove('is-leaving');
    });
  }

  /* =======================================================================
     12. Let do košíka (Swiss: bez rotácie, priama dráha)
     ======================================================================= */
  function interactions() {
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-add]'); if (!btn) return;
      var cart = $('.cart-btn');
      if (cart) {
        cart.classList.remove('is-bumped'); void cart.offsetWidth; cart.classList.add('is-bumped');
        var badge = $('.cart-count', cart);
        if (badge) { badge.classList.remove('is-pop'); void badge.offsetWidth; badge.classList.add('is-pop'); }
      }
      if (reduce || !cart) return;
      var scope = btn.closest('.card') || btn.closest('.pdp') || document;
      var img = scope.querySelector('.card-media img, .pdp-media img'); if (!img) return;
      var from = img.getBoundingClientRect(), to = cart.getBoundingClientRect();
      var ghost = document.createElement('img');
      ghost.src = img.currentSrc || img.src; ghost.className = 'fly'; ghost.alt = '';
      ghost.style.left = (from.left + from.width / 2 - 46) + 'px';
      ghost.style.top = (from.top + from.height / 2 - 46) + 'px';
      document.body.appendChild(ghost);
      var dx = to.left + to.width / 2 - (from.left + from.width / 2);
      var dy = to.top + to.height / 2 - (from.top + from.height / 2);
      ghost.animate([
        { transform: 'translate(0,0) scale(1)', opacity: 1 },
        { transform: 'translate(' + dx * .55 + 'px,' + (dy * .4 - 60) + 'px) scale(.55)', opacity: 1, offset: .55 },
        { transform: 'translate(' + dx + 'px,' + dy + 'px) scale(.08)', opacity: 0 }
      ], { duration: 720, easing: 'cubic-bezier(.5,0,.3,1)' }).onfinish = function () { ghost.remove(); };
    });
  }

  /* =======================================================================
     13. FAQ + kotvy
     ======================================================================= */
  function details() {
    $$('.faq details').forEach(function (d) {
      var a = $('.faq-a', d);
      if (!a || a.classList.contains('faq-wrap')) return;
      var inner = document.createElement('div');
      while (a.firstChild) inner.appendChild(a.firstChild);
      a.appendChild(inner); a.classList.add('faq-wrap');
    });
    if (reduce) return;
    $$('.faq summary').forEach(function (s) {
      s.addEventListener('click', function (e) {
        var d = s.parentElement;
        if (!d.open) return;
        e.preventDefault();
        d.classList.add('is-closing');
        setTimeout(function () { d.open = false; d.classList.remove('is-closing'); }, 300);
      });
    });
  }

  function anchors() {
    $$('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href'); if (id.length < 2) return;
        var t = document.getElementById(id.slice(1)); if (!t) return;
        e.preventDefault();
        var y = t.getBoundingClientRect().top + window.scrollY - 88;
        if (Scroll.active) Scroll.target = y;
        else scrollTo({ top: y, behavior: reduce ? 'auto' : 'smooth' });
      });
    });
  }

  /* ---------------------------------------------------------------- boot -- */
  function boot() {
    splitText();
    preloader();
    inertiaScroll();
    cursor();
    chrome();
    reveals();
    heroScene();
    showcase();
    rail();
    sectionIndex();
    parallax();
    transitions();
    interactions();
    details();
    anchors();
    loop();
  }

  mqReduce.addEventListener && mqReduce.addEventListener('change', function () { location.reload(); });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
