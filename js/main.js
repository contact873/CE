/* Consolidated Engineers - site behaviour. Vanilla JS, no dependencies. */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------- mobile menu ---------------- */
  var toggle = document.querySelector('[data-menu-toggle]');
  var menu = document.querySelector('[data-menu]');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) {
        menu.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------------- scroll reveal ---------------- */
  var revealEls = [].slice.call(document.querySelectorAll('.js-reveal'));
  if (revealEls.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      revealEls.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var reveal = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-visible');
          reveal.unobserve(e.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealEls.forEach(function (el) { reveal.observe(el); });
    }
  }

  /* ---------------- count-up stats ---------------- */
  function countUp(el) {
    var end = parseFloat(el.getAttribute('data-count')) || 0;
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    var duration = 2500;
    var start = null;
    function step(now) {
      if (start === null) start = now;
      var t = Math.min(1, (now - start) / duration);
      var eased = 1 - Math.pow(1 - t, 3);
      el.textContent = prefix + Math.round(end * eased).toLocaleString() + suffix;
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  var counters = [].slice.call(document.querySelectorAll('[data-count]'));
  if (counters.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      /* final values are already in the markup */
    } else {
      var counter = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          countUp(e.target);
          counter.unobserve(e.target);
        });
      }, { threshold: 0.5 });
      counters.forEach(function (el) { counter.observe(el); });
    }
  }

  /* ---------------- scroll-spy dot rail ---------------- */
  var railLinks = [].slice.call(document.querySelectorAll('.nav-aside a[href^="#"]'));
  if (railLinks.length && 'IntersectionObserver' in window) {
    var byId = {};
    railLinks.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      if (document.getElementById(id)) {
        byId[id] = byId[id] || [];
        byId[id].push(a);
      }
    });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        railLinks.forEach(function (a) { a.classList.remove('is-active'); });
        (byId[e.target.id] || []).forEach(function (a) { a.classList.add('is-active'); });
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    Object.keys(byId).forEach(function (id) { spy.observe(document.getElementById(id)); });
  }

  /* ---------------- hero parallax (subtle) ---------------- */
  var heroImg = document.querySelector('.hero__media img');
  if (heroImg && !reduceMotion) {
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var y = Math.min(window.scrollY, window.innerHeight);
        heroImg.style.transform = 'translateY(' + (y * 0.12).toFixed(1) + 'px) scale(1.04)';
        ticking = false;
      });
    }, { passive: true });
  }

  /* ---------------- enquiry form ---------------- */
  function showStatus(form, ok, message) {
    var status = form.querySelector('[data-form-status]');
    if (!status) return;
    status.textContent = message;
    status.classList.add('is-visible', ok ? 'is-ok' : 'is-error');
    status.classList.remove(ok ? 'is-error' : 'is-ok');
    status.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'nearest' });
  }

  [].slice.call(document.querySelectorAll('[data-enquiry-form]')).forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      /* honeypot: bots only */
      if ((form.company_website && form.company_website.value) !== '') return;

      var data = new FormData(form);
      fetch(form.getAttribute('action'), { method: 'POST', body: data })
        .then(function (res) { return res.json(); })
        .then(function (json) {
          showStatus(form, !!json.ok, json.message || 'Thank you.');
          if (json.ok) form.reset();
        })
        .catch(function () {
          var subject = 'Website enquiry: ' + (data.get('product') || 'General');
          var body = 'Name: ' + (data.get('name') || '') + '\n' +
                     'Organisation: ' + (data.get('organisation') || '') + '\n' +
                     'Telephone: ' + (data.get('phone') || '') + '\n\n' +
                     (data.get('message') || '');
          var mailto = 'mailto:info@cedefense.com?subject=' +
            encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
          showStatus(form, false,
            'This preview host cannot process forms. ');
          var status = form.querySelector('[data-form-status]');
          if (status) {
            var link = document.createElement('a');
            link.href = mailto;
            link.textContent = 'Send this enquiry by email instead';
            link.style.textDecoration = 'underline';
            status.appendChild(document.createTextNode(' '));
            status.appendChild(link);
            status.appendChild(document.createTextNode(' or call +92 42 3576 4907-08.'));
          }
        });
    });
  });

  /* ---------------- contact: preselect category from ?product= ---------------- */
  var productSelect = document.getElementById('product');
  if (productSelect) {
    var wanted = new URLSearchParams(window.location.search).get('product');
    if (wanted) {
      var wantedLower = wanted.toLowerCase();
      for (var i = 0; i < productSelect.options.length; i++) {
        var text = productSelect.options[i].text.toLowerCase();
        if (text === wantedLower || text.indexOf(wantedLower) !== -1) {
          productSelect.selectedIndex = i;
          break;
        }
      }
    }
  }

  /* ---------------- footer year ---------------- */
  [].slice.call(document.querySelectorAll('[data-year]')).forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
