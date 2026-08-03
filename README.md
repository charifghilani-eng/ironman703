# 🏊🚴🏃 IronPredict — Ironman 70.3 Performance Analysis

A full-stack data analysis of my **Ironman 70.3 Agadir 2025** race, built to answer three questions: where am I weak, where should I invest training, and how ready will I be for my next race (Portugal 70.3, April 2027).

---

## 📊 Overview

IronPredict is an end-to-end sports analytics project combining race results, personal training data, and physiological modelling to produce a diagnostic and forward-looking readiness analysis. It was built as both a personal performance tool and a demonstration of applied data analysis.

**Race:** Ironman 70.3 Agadir 2025 — Swim 1.9km / Bike 90km / Run 21.1km
**Athlete:** M18-24 division, finish time 7:06:54 (corrected), age-group rank 24/26

---

## 🎯 Key Findings

- **The swim is the true limiting factor** (z-score +1.63 vs age group). It was the least-developed discipline, not a lack of talent — training was minimal and inconsistent.
- **The run was NOT the real weakness**, despite being the worst discipline on race day. The result was confounded by an IT-band injury (physio-linked to weak glutes) and off-the-bike fatigue. Two healthy pre-race long runs (~6:52/km) proved underlying run fitness was sound.
- **The bike is a relative strength held back by equipment.** Ridden on a standard road bike; ~2–4 km/h of speed is available through aero equipment alone, with zero fitness gain or injury risk — the best risk-adjusted improvement.
- **T1 is ~2 minutes of free time**, the cheapest gain in the entire race, lost to first-timer inefficiency.
- **A documented data correction**: the official run split was inflated (course re-entry after finishing); photographic evidence confirms a true finish of 7:06:54.
- **Readiness plan**: a 35-week periodized build projects race-day fitness (CTL) ~5× the Agadir baseline, arriving well-tapered.

---

## 🛠️ Methodology

1. **Diagnosis** — Z-scores per discipline vs the M18-24 age group, converting incomparable split times into a single comparable "distance from the field" scale.
2. **Confounder analysis** — Separating genuine weaknesses from circumstantial factors (injury, equipment, fatigue) using training data to isolate true fitness.
3. **Training load modelling** — CTL / ATL / TSB (fitness / fatigue / form) from activity data.
4. **ROI analysis** — Estimating where training time buys the most improvement, risk-adjusted for injury.
5. **Readiness simulation** — Forward-projecting a periodized training plan toward the next race.

---

## 💻 Tech Stack

- **Python** (pandas, NumPy) — data cleaning, analysis, modelling
- **Jupyter Notebooks** — exploratory analysis
- **SQLite** — structured storage of results and metrics
- **Power BI** — interactive dashboard (race overview, per-discipline deep-dives, readiness)

---

## 📊 Dashboard

An interactive Power BI dashboard presenting the full analysis across seven pages, styled with official Ironman 70.3 Agadir branding.

### Overview Analysis
Field-wide view of all 522 finishers — average splits, age-group breakdown, athlete map, and an interactive race-pace profile.
![Overview Analysis](Capture%20d'écran%202026-08-03%20013546.png)

### My Race Diagnosis
My race in detail — splits, official race-pace curve, and the z-score analysis identifying my limiting factor.
![My Race Diagnosis](Capture%20d'écran%202026-08-03%20013615.png)

### Swim Deep-Dive
Why the swim is my primary trainable weakness — training volume, sessions, and performance vs the field.
![Swim Deep-Dive](Capture%20d'écran%202026-08-03%20013642.png)

### Bike Deep-Dive
My relative strength — speed analysis and the equipment vs fitness decomposition.
![Bike Deep-Dive](Capture%20d'écran%202026-08-03%20013714.png)

### Run Deep-Dive
The injury story — how IT-band injury and fatigue confounded my run, and the evidence of my true run fitness.
![Run Deep-Dive](Capture%20d'écran%202026-08-03%20013738.png)

### Transitions (T1 & T2)
The free time — T1 was ~2 minutes slower than average, the cheapest gain in the whole race.
![Transitions](Capture%20d'écran%202026-08-03%20013813.png)

### Conclusion & Readiness
Where I stand now and a 35-week readiness plan projecting my fitness toward Ironman 70.3 Portugal (April 2027).
![Conclusion](Capture%20d'écran%202026-08-03%20013936.png)

## ⚠️ Notes & Limitations

- Training data (especially pool swims) is under-recorded, as pool sessions don't auto-log via GPS. Self-reported training is clearly labelled and separated from recorded data.
- Training-load values use a duration-based proxy (not power/HR-based TSS), so they are interpreted as trend and self-comparison rather than absolute values.
- The run-split correction rests on athlete account plus photographic evidence, not an official timing amendment. Both recorded and corrected values are reported.

---

## 📄 License

© 2026 Charif Ghilani. All rights reserved.
This project is shared publicly for portfolio and demonstration purposes only.
No part may be copied, reused, modified, or redistributed without explicit written permission.
