/* ==========================================================================
   GelaVit — front-end shop (vanilla JS, no dependencies)
   Cart lives in localStorage. Order is submitted to a form endpoint that
   emails you the order (see CONFIG.orderEndpoint in config.js).
   ========================================================================== */
(function () {
  'use strict';

  var CFG = window.GELAVIT_CONFIG || {};
  var CATALOG = window.GELAVIT_CATALOG || {};
  var T = window.GELAVIT_I18N || {};
  var LANG = document.documentElement.lang || 'sk';
  var KEY = 'gelavit_cart_v1';
  var BASE = document.body.getAttribute('data-base') || '';

  /* ---------- helpers ---------- */
  function money(n) {
    return new Intl.NumberFormat(LANG === 'sk' ? 'sk-SK' : LANG === 'de' ? 'de-DE' : 'en-IE',
      { style: 'currency', currency: 'EUR' }).format(n);
  }
  function t(k) { return (T[k] !== undefined) ? T[k] : k; }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }

  /* ---------- cart store ---------- */
  function read() {
    try { var v = JSON.parse(localStorage.getItem(KEY)); return Array.isArray(v) ? v : []; }
    catch (e) { return []; }
  }
  function write(items) {
    try { localStorage.setItem(KEY, JSON.stringify(items)); } catch (e) {}
    paintCount();
    document.dispatchEvent(new CustomEvent('cart:change'));
  }
  var Cart = {
    items: function () {
      return read().filter(function (i) { return CATALOG[i.slug]; });
    },
    add: function (slug, qty) {
      if (!CATALOG[slug]) return;
      var items = read(), found = null;
      items.forEach(function (i) { if (i.slug === slug) found = i; });
      if (found) found.qty = Math.min(99, found.qty + (qty || 1));
      else items.push({ slug: slug, qty: qty || 1 });
      write(items);
    },
    set: function (slug, qty) {
      var items = read().filter(function (i) { return i.slug !== slug || qty > 0; });
      items.forEach(function (i) { if (i.slug === slug) i.qty = Math.max(1, Math.min(99, qty)); });
      write(items);
    },
    remove: function (slug) {
      write(read().filter(function (i) { return i.slug !== slug; }));
    },
    clear: function () { write([]); },
    count: function () {
      return Cart.items().reduce(function (s, i) { return s + i.qty; }, 0);
    },
    subtotal: function () {
      return Cart.items().reduce(function (s, i) { return s + CATALOG[i.slug].price * i.qty; }, 0);
    }
  };
  window.GelavitCart = Cart;

  /* ---------- header count ---------- */
  function paintCount() {
    var n = Cart.count();
    $$('.cart-count').forEach(function (el) {
      el.textContent = n;
      el.classList.toggle('is-on', n > 0);
    });
  }

  /* ---------- toast ---------- */
  var toastEl, toastTimer;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      toastEl.setAttribute('role', 'status');
      document.body.appendChild(toastEl);
    }
    toastEl.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8.5l3.2 3L13 5"/></svg>' + msg;
    requestAnimationFrame(function () { toastEl.classList.add('is-on'); });
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('is-on'); }, 2600);
  }

  /* ---------- add to cart buttons ---------- */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-add]');
    if (btn) {
      e.preventDefault();
      var slug = btn.getAttribute('data-add');
      var qtyIn = $('#qty');
      var q = (btn.hasAttribute('data-use-qty') && qtyIn) ? parseInt(qtyIn.value, 10) || 1 : 1;
      Cart.add(slug, q);
      toast(t('added'));
      return;
    }
    var rm = e.target.closest('[data-remove]');
    if (rm) { e.preventDefault(); Cart.remove(rm.getAttribute('data-remove')); }
  });

  /* ---------- qty stepper on PDP ---------- */
  $$('[data-qty]').forEach(function (b) {
    b.addEventListener('click', function () {
      var input = $('#qty'); if (!input) return;
      var v = parseInt(input.value, 10) || 1;
      input.value = Math.max(1, Math.min(99, v + parseInt(b.getAttribute('data-qty'), 10)));
    });
  });

  /* ---------- cart page ---------- */
  function renderCart() {
    var host = $('#cart-lines'); if (!host) return;
    var items = Cart.items();
    var empty = $('#cart-empty'), body = $('#cart-body');
    if (!items.length) {
      if (empty) empty.hidden = false;
      if (body) body.hidden = true;
      return;
    }
    if (empty) empty.hidden = true;
    if (body) body.hidden = false;

    host.innerHTML = items.map(function (i) {
      var p = CATALOG[i.slug];
      return '<div class="cart-line">' +
        '<img src="' + BASE + 'assets/img/products/' + p.img + '-400.webp" alt="" width="92" height="92" loading="lazy">' +
        '<div><h4>' + p.name + '</h4><div class="muted" style="font-size:.8125rem">' + p.pack + ' · ' + money(p.price) + '</div>' +
        '<button class="remove" data-remove="' + i.slug + '" type="button">' + t('remove') + '</button></div>' +
        '<div style="text-align:right"><div class="qty" style="height:40px">' +
          '<button type="button" data-line="' + i.slug + '" data-delta="-1" aria-label="-">−</button>' +
          '<input type="number" min="1" max="99" value="' + i.qty + '" data-line-input="' + i.slug + '" aria-label="' + t('qty') + '">' +
          '<button type="button" data-line="' + i.slug + '" data-delta="1" aria-label="+">+</button>' +
        '</div><div style="margin-top:.5rem;font-weight:600">' + money(p.price * i.qty) + '</div></div>' +
      '</div>';
    }).join('');

    $$('[data-line]', host).forEach(function (b) {
      b.addEventListener('click', function () {
        var slug = b.getAttribute('data-line');
        var cur = Cart.items().filter(function (i) { return i.slug === slug; })[0];
        Cart.set(slug, cur.qty + parseInt(b.getAttribute('data-delta'), 10));
      });
    });
    $$('[data-line-input]', host).forEach(function (inp) {
      inp.addEventListener('change', function () {
        Cart.set(inp.getAttribute('data-line-input'), parseInt(inp.value, 10) || 1);
      });
    });
    paintTotals();
  }

  /* ---------- totals (cart + checkout) ---------- */
  function shippingPrice() {
    var sel = $('input[name="shipping"]:checked');
    if (!sel) return null;
    var base = parseFloat(sel.getAttribute('data-price')) || 0;
    if (CFG.freeFrom && Cart.subtotal() >= CFG.freeFrom && sel.value !== 'pickup') return 0;
    return base;
  }
  function paymentFee() {
    var sel = $('input[name="payment"]:checked');
    return sel ? (parseFloat(sel.getAttribute('data-price')) || 0) : 0;
  }
  function paintTotals() {
    var sub = Cart.subtotal();
    var ship = shippingPrice();
    var fee = paymentFee();
    var total = sub + (ship || 0) + fee;

    var s = $('#sum-sub'); if (s) s.textContent = money(sub);
    var sh = $('#sum-ship');
    if (sh) sh.textContent = ship === null ? '—' : (ship === 0 ? t('free') : money(ship));
    var pf = $('#sum-fee-row');
    if (pf) { pf.hidden = fee <= 0; var pfv = $('#sum-fee'); if (pfv) pfv.textContent = money(fee); }
    var tt = $('#sum-total'); if (tt) tt.textContent = money(total);

    var prog = $('#free-ship');
    if (prog && CFG.freeFrom) {
      var left = CFG.freeFrom - sub;
      prog.textContent = left > 0 ? t('freeLeft').replace('{x}', money(left)) : t('freeGot');
      prog.hidden = sub <= 0;
    }
    var mini = $('#sum-items');
    if (mini) {
      mini.innerHTML = Cart.items().map(function (i) {
        var p = CATALOG[i.slug];
        return '<div class="summary-row"><span>' + i.qty + '× ' + p.name + '</span><span>' + money(p.price * i.qty) + '</span></div>';
      }).join('');
    }
  }

  $$('input[name="shipping"], input[name="payment"]').forEach(function (r) {
    r.addEventListener('change', paintTotals);
  });

  /* ---------- checkout ---------- */
  function initCheckout() {
    var form = $('#order-form'); if (!form) return;
    if (!Cart.items().length) { location.href = CFG.cartUrl; return; }

    form.addEventListener('submit', function (e) {
      var lines = Cart.items().map(function (i) {
        var p = CATALOG[i.slug];
        return i.qty + '× ' + p.name + ' (' + p.sku + ') — ' + money(p.price * i.qty);
      }).join('\n');
      var ship = shippingPrice(), fee = paymentFee();
      var shipLabel = ($('input[name="shipping"]:checked') || {}).getAttribute
        ? $('input[name="shipping"]:checked').getAttribute('data-label') : '';
      var payLabel = $('input[name="payment"]:checked')
        ? $('input[name="payment"]:checked').getAttribute('data-label') : '';

      $('#f-order').value = lines;
      $('#f-subtotal').value = money(Cart.subtotal());
      $('#f-shipping').value = shipLabel + ' — ' + (ship === 0 ? t('free') : money(ship || 0));
      $('#f-payment').value = payLabel + (fee ? ' (+' + money(fee) + ')' : '');
      $('#f-total').value = money(Cart.subtotal() + (ship || 0) + fee);

      if (!CFG.orderEndpoint) {
        // No endpoint configured yet → open the customer's mail client instead.
        e.preventDefault();
        var body = t('mailIntro') + '\n\n' + lines + '\n\n' +
          t('subtotal') + ': ' + money(Cart.subtotal()) + '\n' +
          t('shipping') + ': ' + $('#f-shipping').value + '\n' +
          t('payment') + ': ' + $('#f-payment').value + '\n' +
          t('total') + ': ' + $('#f-total').value + '\n\n' +
          '—\n' + $('#name').value + '\n' + $('#email').value + '\n' + $('#phone').value + '\n' +
          $('#street').value + ', ' + $('#zip').value + ' ' + $('#city').value + '\n' +
          ($('#note').value || '');
        location.href = 'mailto:' + (CFG.orderEmail || 'info@gelavit.sk') +
          '?subject=' + encodeURIComponent(t('orderSubject')) + '&body=' + encodeURIComponent(body);
        setTimeout(function () { Cart.clear(); location.href = CFG.thanksUrl; }, 700);
        return;
      }
      // Real endpoint (Formspree / FormSubmit / Netlify Forms) — let it submit,
      // clear the cart on the way out.
      try { localStorage.setItem(KEY, '[]'); } catch (err) {}
    });
  }

  /* ---------- header / menu / reveal ---------- */
  function initChrome() {
    var header = $('.site-header');
    if (header) {
      var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 8); };
      onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
    }
    var burger = $('.burger'), menu = $('.mobile-menu');
    if (burger && menu) {
      burger.addEventListener('click', function () {
        menu.classList.add('is-open');
        document.body.style.overflow = 'hidden';
        $$('.mm-links a', menu).forEach(function (a, i) { a.style.animationDelay = (i * 55 + 120) + 'ms'; });
      });
      $('.mm-close', menu).addEventListener('click', function () {
        menu.classList.remove('is-open'); document.body.style.overflow = '';
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { menu.classList.remove('is-open'); document.body.style.overflow = ''; }
      });
    }
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
      $$('.reveal').forEach(function (el) { io.observe(el); });
    } else {
      $$('.reveal').forEach(function (el) { el.classList.add('is-in'); });
    }
  }

  /* ---------- boot ---------- */
  document.addEventListener('cart:change', function () { renderCart(); paintTotals(); });
  paintCount();
  initChrome();
  renderCart();
  paintTotals();
  initCheckout();
})();
