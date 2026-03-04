---
title: "Minnesota Iron Industry Forecast"
description: "Probability models and forecasts for Minnesota taconite mining operations"
layout: "dashboard"
---

<style>
.dashboard-container {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  padding: 0;
  overflow-x: auto;
}

.dashboard-frame {
  width: 100%;
  height: 200vh;
  border: none;
  display: block;
}

.dashboard-title {
  text-align: center;
  font-size: 28px;
  font-weight: bold;
  color: #2d3748;
  margin: 20px 0;
  padding: 0 20px;
}

body {
  margin: 0;
  padding: 0;
}
</style>

<div class="dashboard-title">Minnesota Iron Industry Forecast</div>

<div class="dashboard-container">
  <iframe src="/models/unified_mine_forecast_dashboard.html" class="dashboard-frame" scrolling="no"></iframe>
</div>

<div class="dashboard-container" style="margin-top: 20px;">
  <iframe src="/models/port_forecasts_dashboard.html" class="dashboard-frame" scrolling="no"></iframe>
</div>