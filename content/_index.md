---
title: "Loon Tracks"
description: "Data analysis and probability models for the upper midwest"
markup: html
---

<div class="homepage-container">
  <!-- Left Column -->
  <div class="left-column">
    <!-- MN Iron Industry Category Card -->
    <div class="category-card">
      <div class="category-header">MN Iron Industry</div>
      <div class="category-grid">
        <a href="/iron-mine/" class="category-tile iron-mine">
          Mine Activity
        </a>
        <a href="/iron-port/" class="category-tile iron-port">
          Port Activity
        </a>
      </div>
    </div>

    <!-- Elections Category Card -->
    <div class="category-card">
      <div class="category-header">Elections</div>
      <div class="category-grid elections-grid">
        <a href="/congress/" class="category-tile congress">
          Congress
        </a>
        <a href="/governor/" class="category-tile governor">
          Governor
        </a>
        <a href="/mi-legislature/" class="category-tile mi-leg">
          MI Legislature
        </a>
        <a href="/mn-legislature/" class="category-tile mn-leg">
          MN Legislature
        </a>
        <a href="/wi-legislature/" class="category-tile wi-leg">
          WI Legislature
        </a>
      </div>
    </div>
  </div>

  <!-- Center Column -->
  <div class="center-column">
    <div class="preview-carousel" role="region" aria-label="Forecast previews" aria-roledescription="carousel">
      <div class="carousel-track">
        <a class="carousel-slide" href="/congress/" aria-label="Wisconsin Congressional Forecast">
          <img src="/previews/congressional_wi.png" alt="Wisconsin congressional district forecast map" loading="lazy">
          <div class="carousel-caption">Wisconsin Congressional Forecast</div>
        </a>
        <a class="carousel-slide" href="/congress/" aria-label="Michigan Congressional Forecast">
          <img src="/previews/congressional_mi.png" alt="Michigan congressional district forecast map" loading="lazy">
          <div class="carousel-caption">Michigan Congressional Forecast</div>
        </a>
        <a class="carousel-slide" href="/congress/" aria-label="Minnesota Congressional Forecast">
          <img src="/previews/congressional_mn.png" alt="Minnesota congressional district forecast map" loading="lazy">
          <div class="carousel-caption">Minnesota Congressional Forecast</div>
        </a>
        <a class="carousel-slide" href="/governor/" aria-label="Governor races forecast">
          <img src="/previews/governor.png" alt="Governor race win-probability forecast for Michigan, Minnesota, and Wisconsin" loading="lazy">
          <div class="carousel-caption">Governor Races — MI · MN · WI</div>
        </a>
        <a class="carousel-slide" href="/wi-legislature/" aria-label="Wisconsin Legislature Forecast">
          <img src="/previews/wi_legislature.png" alt="Wisconsin state legislature seat forecast" loading="lazy">
          <div class="carousel-caption">Wisconsin Legislature Forecast</div>
        </a>
        <a class="carousel-slide" href="/mi-legislature/" aria-label="Michigan Legislature Forecast">
          <img src="/previews/mi_legislature.png" alt="Michigan state legislature seat forecast" loading="lazy">
          <div class="carousel-caption">Michigan Legislature Forecast</div>
        </a>
        <a class="carousel-slide" href="/mn-legislature/" aria-label="Minnesota Legislature Forecast">
          <img src="/previews/mn_legislature.png" alt="Minnesota state legislature seat forecast" loading="lazy">
          <div class="carousel-caption">Minnesota Legislature Forecast</div>
        </a>
        <a class="carousel-slide" href="/iron-port/" aria-label="Minnesota Port Shipping Forecast">
          <img src="/previews/iron_port.png" alt="Minnesota iron ore port shipping-season forecast gauges" loading="lazy">
          <div class="carousel-caption">Minnesota Port Shipping Forecast</div>
        </a>
      </div>
      <div class="carousel-dots" role="tablist" aria-label="Choose preview"></div>
    </div>
  </div>

  <script>
  (function () {
    var root = document.querySelector('.preview-carousel');
    if (!root) return;
    var slides = [].slice.call(root.querySelectorAll('.carousel-slide'));
    var dotsWrap = root.querySelector('.carousel-dots');
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var DELAY = 6000, i = 0, timer = null;

    var dots = slides.map(function (s, idx) {
      var d = document.createElement('button');
      d.className = 'carousel-dot';
      d.type = 'button';
      d.setAttribute('role', 'tab');
      d.setAttribute('aria-label', 'Show ' + (s.getAttribute('aria-label') || ('slide ' + (idx + 1))));
      d.addEventListener('click', function (e) { e.preventDefault(); show(idx); if (!reduce) start(); });
      dotsWrap.appendChild(d);
      return d;
    });

    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, idx) { s.classList.toggle('active', idx === i); });
      dots.forEach(function (d, idx) {
        var on = idx === i;
        d.classList.toggle('active', on);
        d.setAttribute('aria-selected', on ? 'true' : 'false');
      });
    }
    function start() { stop(); timer = setInterval(function () { show(i + 1); }, DELAY); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }

    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', function () { if (!reduce) start(); });

    show(0);
    if (!reduce) start();
  })();
  </script>

  <!-- Right Column -->
  <div class="right-column">
    <div class="category-card">
      <div class="category-header">Public Health</div>
      <div class="category-grid">
        <a href="/measles/" class="category-tile measles">
          Measles
        </a>
        <a href="/flu-season/" class="category-tile flu-season">
          Flu Season
        </a>
      </div>
    </div>
    <div class="coming-soon-tile">
      Coming Soon
    </div>
  </div>
</div>