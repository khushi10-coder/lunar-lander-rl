# Rocket Lander AI - Demo & Media Documentation Summary

This document outlines the high-resolution screenshots and screen recording videos captured for demonstration, GitHub documentation, and LinkedIn showcase posts.

---

## 1. Screenshots Overview (`media/screenshots/`)

All screenshots were rendered in 1920x1080 (16:9 full HD) using the project's styling and visual components:

| Filename | Resolution | Description / Features Shown |
| :--- | :--- | :--- |
| `01_dashboard.png` | 1920x1080 | **Full Project Dashboard**: Header, badges (*Learns by practice*, *Learns from points*, *Runs in browser*), quick start guide, pilot selection cards, and LAUNCH button. |
| `02_standard_pilot.png` | 1920x1080 | **Standard Pilot (Baseline)**: Soft landing demonstration, score `236` (exceeds 200 threshold with gold star), and fuel gauge. |
| `03_hurry_up_pilot.png` | 1920x1080 | **Hurry-Up Pilot (Time Penalty)**: High-efficiency, fast trajectory touchdown between flags with minimal fuel usage. Score `251`. |
| `04_hovering_pilot.png` | 1920x1080 | **Cheater Pilot (Reward Hacking)**: Rocket deliberately hovering in the air without landing. Explains the +0.5 per frame bug causing score `-15`. |
| `05_smart_pilot.png` | 1920x1080 | **Smart Pilot (Potential-Based Shaping)**: Smooth descent and touchdown using Ng et al. policy invariance reward. Score `244`. |
| `06_model_comparison.png` | 1920x1080 | **Interactive Comparison Grid**: All 4 pilots displayed with behavioral descriptions, point rules, and status badges. |
| `07_training_results.png` | 1920x1080 | **Scoreboard & Evaluation Table**: 100-episode benchmark scores, horizontal score bars, and the dotted `SOLVED = 200` threshold line. |
| `agent_comparison.png` | 1200x675 | **LinkedIn Showcase Infographic**: 16:9 graphic comparing reward designs, benchmark results, and the reward hacking lesson. |

---

## 2. Simulation Videos Overview (`media/videos/`)

All videos are encoded using H.264/MP4 (`yuv420p`) at 30 FPS, optimized for universal browser and social media playback:

| Filename | Duration | Frame Count | File Size | Description |
| :--- | :--- | :--- | :--- | :--- |
| `standard_pilot.mp4` | 13.2 s | 395 frames | 551 KB | Standard Pilot descent and touchdown between flags. |
| `hurry_up_pilot.mp4` | 12.0 s | 359 frames | 460 KB | Hurry-Up Pilot rapid descent and fuel-efficient landing. |
| `hovering_pilot.mp4` | 15.5 s | 465 frames | 606 KB | Hovering Pilot hovering indefinitely (reward hacking demonstration). |
| `smart_pilot.mp4` | 8.0 s | 241 frames | 274 KB | Smart Pilot smooth approach and perfect landing. |
| `rocket_lander_full_demo.mp4` | 58.2 s | 1,746 frames | 1.88 MB | **Full Demo Video**: Title cards, side-by-side run comparisons, and key takeaways. |

---

## 3. Pilot Benchmark Results & Observed Behaviors

| Pilot | Model File | Benchmark Score (100 eps) | Observed Behavior | Solved Status |
| :--- | :--- | :--- | :--- | :--- |
| **Hurry-Up Pilot** | `ppo_time.zip` | **243.3 ± 46.1** | Aggressive, swift descent to avoid per-step penalty. | **Solved** (>200) |
| **Smart Pilot** | `ppo_fixed.zip` | **240.6 ± 48.0** | Graceful touchdown using potential-based distance shaping. | **Solved** (>200) |
| **Standard Pilot** | `ppo_baseline.zip` | **219.2 ± 67.4** | Steady descent and clean touchdown. | **Solved** (>200) |
| **Cheater Pilot** | `ppo_hover.zip` | **-12.0 ± 82.5** | Hovers mid-air indefinitely to exploit positive frame rewards. | **Failed** (<200) |

> **Key RL Finding**: Agents do not optimize what we intended; they optimize the exact mathematical formulation of the reward function. Giving +0.5 per frame for remaining upright incentivized infinite hovering instead of landing.

---

## 4. Commands Used

### Launching Dashboard
```bash
streamlit run app.py
```

### Running Model Evaluations
```bash
python src/evaluate.py --model models/ppo_baseline.zip --episodes 100
python src/evaluate.py --model models/ppo_time.zip --episodes 100
python src/evaluate.py --model models/ppo_hover.zip --episodes 100
python src/evaluate.py --model models/ppo_fixed.zip --episodes 100
```
