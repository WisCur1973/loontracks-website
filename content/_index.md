---
title: "Loon Tracks"
description: "Data analysis and probability models for the upper midwest"
---

<style>
.homepage-grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 8px;
  max-width: 100vw;
  margin: 0;
  height: 500px;
  padding: 5px;
}

.grid-box {
  border-radius: 12px;
  padding: 30px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  font-size: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.grid-box:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.iron-industry {
  background: linear-gradient(135deg, #4a5568, #2d3748);
}

.hunting {
  background: linear-gradient(135deg, #38a169, #2f855a);
}

.blog {
  grid-column: 2;
  grid-row: 1 / 3;
  background: linear-gradient(135deg, #3182ce, #2c5282);
  font-size: 24px;
  flex-direction: column;
  gap: 15px;
}

.elections {
  background: linear-gradient(135deg, #d69e2e, #b7791f);
}

.disease {
  background: linear-gradient(135deg, #e53e3e, #c53030);
}

.site-title {
  text-align: center;
  font-size: 48px;
  font-weight: bold;
  color: #2d3748;
  margin-bottom: 40px;
  margin-top: 20px;
}

.blog-subtitle {
  font-size: 16px;
  opacity: 0.9;
  font-weight: normal;
}
</style>

<div class="homepage-grid">
  <a href="/iron-industry/" class="grid-box iron-industry">
    MN Iron Industry
  </a>

  <a href="https://wiscur.substack.com" class="grid-box blog">
    <div>News & Opinion</div>
    <div class="blog-subtitle">Latest analysis and insights</div>
  </a>

  <a href="/hunting/" class="grid-box hunting">
    Hunting
  </a>

  <a href="/elections/" class="grid-box elections">
    Elections
  </a>

  <a href="/disease/" class="grid-box disease">
    Measles & Disease
  </a>
</div>