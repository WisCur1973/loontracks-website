---
title: "Election Forecasts"
description: "Probability models for 2026 elections across the upper midwest"
layout: "dashboard"
---

<style>
.elections-container {
  width: 95vw;
  max-width: 95vw;
  margin-left: calc(-47.5vw + 50%);
  padding: 0;
}

.election-section {
  width: 100%;
  margin-bottom: 30px;
}

.congressional-frame {
  width: 100%;
  height: 400vh;
  border: none;
  display: block;
}

.governor-frame {
  width: 100%;
  height: 300vh;
  border: none;
  display: block;
}

.legislature-frame {
  width: 100%;
  height: 900vh;
  border: none;
  display: block;
}

.election-title {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  color: #2d3748;
  margin: 30px 0 10px 0;
  padding: 15px 20px;
  background: #f7fafc;
  border-bottom: 2px solid #e2e8f0;
}

.main-title {
  text-align: center;
  font-size: 32px;
  font-weight: bold;
  color: #2d3748;
  margin: 20px 0 30px 0;
  padding: 0 20px;
}

body {
  margin: 0;
  padding: 0;
}
</style>

<div class="main-title">2026 Election Forecasts</div>

<div class="elections-container">
  <div class="election-section">
    <div class="election-title">Congressional Forecast</div>
    <iframe src="/elections/Congressional_Forecast_2026-02-09.html" class="congressional-frame" scrolling="no"></iframe>
  </div>

  <div class="election-section">
    <div class="election-title">Governor Forecast</div>
    <iframe src="/elections/Governor_Forecast_2026-02-09.html" class="governor-frame" scrolling="no"></iframe>
  </div>

  <div class="election-section">
    <div class="election-title">Michigan Legislature Forecast</div>
    <iframe src="/elections/MI_Legislature_Forecast_2026-02-09.html" class="legislature-frame" scrolling="no"></iframe>
  </div>

  <div class="election-section">
    <div class="election-title">Minnesota Legislature Forecast</div>
    <iframe src="/elections/MN_Legislature_Forecast_2026-02-09.html" class="legislature-frame" scrolling="no"></iframe>
  </div>

  <div class="election-section">
    <div class="election-title">Wisconsin Legislature Forecast</div>
    <iframe src="/elections/WI_Legislature_Forecast_2026-02-09.html" class="legislature-frame" scrolling="no"></iframe>
  </div>
</div>