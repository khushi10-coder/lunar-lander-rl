# Rocket Lander AI

I trained AI pilots with reinforcement learning to land a simulated rocket, and showed how changing the point rules makes the AI either land properly or learn to cheat.

Live demo: coming soon

---

## What It Is

This project teaches a computer to pilot a rocket to a safe lunar touchdown. No human programmer wrote rules on how to fire the engines or balance against gravity. Instead, the AI practiced over a million times in a physics simulator, discovering how to fly entirely on its own by collecting points. An interactive space-themed web dashboard lets you launch the pilots, test different landing spots, and compare their behaviors side by side.

---

## The Four Pilots

Each pilot was trained with a different scoring rule to explore how point systems shape AI behavior:

| Pilot | Original Name | How It Earns Points |
| :--- | :--- | :--- |
| **🎯 Standard Pilot** | `baseline` | Learns with the game's normal points: rewarded for landing softly between the flags, penalized for crashing. |
| **⚡ Hurry-Up Pilot** | `time` | Loses a tiny fraction of a point every second, learning that wasting time costs fuel. |
| **⚠️ Cheater Pilot** | `hover` | Receives +1 point every second it stays upright and slow in mid-air, learning to float instead of land. |
| **🚀 Smart Pilot** | `fixed` | Only receives points for getting closer to the pad, so hovering stops paying and safe landing is restored. |

---

## Tournament Results

These scores are the average points earned over 20 test landings with custom bonuses switched off:

| Pilot | Original Name | Average Score | Flight Outcome |
| :--- | :--- | :---: | :--- |
| **⚡ Hurry-Up Pilot** | `time` | **243.3** | Clean, fast touchdown |
| **🚀 Smart Pilot** | `fixed` | **240.6** | Gentle, highly stable landing |
| **🎯 Standard Pilot** | `baseline` | **219.2** | Reliable touchdown |
| **⚠️ Cheater Pilot** | `hover` | **-12.0** | Floats in mid-air until time runs out |

> **Note:** Each pilot was trained once (one seed), so small differences between pilots may be luck. The Cheater Pilot's low score clearly shows it never lands. 200 or more counts as a good landing.

---

## Key Idea: Reward Hacking

When we gave the Cheater Pilot bonus points for floating upright and slow, it discovered that landing ended the round and stopped the payments. Floating in mid-air earned endless safe points without any danger of crashing into the ground, so the AI chose to cheat rather than land. We fixed this by rewarding improvement toward the pad rather than static hovering, forcing the AI to make a prompt, gentle landing.

---

## How to Run It

Python 3.10 to 3.12 works best on Windows, macOS, and Linux.

### 1. Clone the repository and navigate into the folder
```bash
git clone https://github.com/khushi10-coder/lunar-lander-rl.git
cd lunar-lander-rl
```

### 2. Create and activate a virtual environment
* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the web dashboard
```bash
python -m streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser to launch rockets and test the pilots.

---

## How I Trained It

If you want to train your own pilots or run benchmarks from the terminal:

* **Train a pilot:**
  ```bash
  python src/train.py --variant fixed --steps 1000000 --seed 0
  ```
  *(Options for `--variant`: `baseline`, `time`, `hover`, `fixed`)*

* **Evaluate saved models across 20 flights:**
  ```bash
  python src/evaluate.py
  ```

* **Export evaluation scores to `web/results.json`:**
  ```bash
  python src/export_results.py
  ```

* **Record video clips of a trained pilot:**
  ```bash
  python src/record.py --model models/fixed_seed0.zip --out videos/fixed
  ```

---

## Project Structure

```text
lunar-lander-rl/
├── .streamlit/
│   └── config.toml          # Cosmic dark purple theme configuration
├── assets/
│   ├── style.css            # Custom CSS for the arcade space theme
│   └── svgs.py              # Inline SVG artwork (rocket, planets, gold star)
├── models/
│   ├── baseline_seed0.zip   # Trained model: Standard Pilot
│   ├── fixed_seed0.zip      # Trained model: Smart Pilot
│   ├── hover_seed0.zip      # Trained model: Cheater Pilot
│   └── time_seed0.zip       # Trained model: Hurry-Up Pilot
├── src/
│   ├── evaluate.py          # Benchmark all saved models on 20 episodes
│   ├── export_results.py    # Compute and save mean scores to web/results.json
│   ├── record.py            # Record episode replay MP4 videos
│   ├── train.py             # Train PPO agent on any reward variant
│   ├── watch_random.py      # Watch an untrained agent for comparison
│   └── wrappers.py          # Gymnasium reward shaping environment wrappers
├── web/
│   └── results.json         # Benchmark tournament results loaded by the app
├── .gitignore               # Ignores virtual envs, videos, and cache files
├── app.py                   # Main Streamlit web application
├── packages.txt             # Linux system dependencies (swig) for cloud deploy
├── README.md                # Project documentation and guide
└── requirements.txt         # Pinned Python package dependencies
```

---

## Tech Used

* **Python** — Core language
* **Gymnasium & Box2D** — Physics simulation environment (`LunarLander-v3`)
* **Stable-Baselines3 (PPO)** — Proximal Policy Optimization reinforcement learning algorithm
* **PyTorch** — Deep learning framework backing the policy network
* **Streamlit** — Interactive frontend dashboard

---

## Author

* **khushi10-coder** — [GitHub Profile](https://github.com/khushi10-coder)
