# 🚀 Rocket Lander AI

> **An AI-powered lunar landing simulator where four reinforcement learning agents compete to master the perfect touchdown — or discover how to cheat the scoring system!**

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![RL](https://img.shields.io/badge/AI-Reinforcement%20Learning-orange)
![PPO](https://img.shields.io/badge/Algorithm-PPO-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)

**🎮 Live Demo:** Coming Soon!

---

## 🎯 Project Objective

Train AI pilots to land a simulated rocket safely using **Reinforcement Learning (PPO)**.

Instead of programming flight instructions, the AI learns through trial and error, receiving rewards and penalties for its actions.

The interesting experiment? Changing the reward rules changes how the AI behaves — sometimes it even learns to cheat!

---

## 👨‍🚀 Meet the Four Pilots

| Pilot | Personality | Learning Strategy |
|---|---|---|
| 🎯 Standard Pilot | The Responsible One | Learns using the game's original rewards. |
| ⚡ Hurry-Up Pilot | The Speedrunner | Learns to land quickly by receiving time penalties. |
| 😈 Cheater Pilot | The Rule Exploiter | Learns to hover instead of landing to collect bonus points. |
| 🚀 Smart Pilot | The Problem Solver | Learns to move closer to the landing pad instead of hovering. |

---

## 🏆 Tournament Results

Average scores across 20 test flights:

| Pilot | Average Score | Outcome |
|---|---:|---|
| ⚡ Hurry-Up | **243.3** | Fast touchdown |
| 🚀 Smart | **240.6** | Stable landing |
| 🎯 Standard | **219.2** | Successful landing |
| 😈 Cheater | **-12.0** | Never lands! |

> Scores of 200+ count as a good landing. Each pilot was trained using one random seed, so results are experimental rather than statistically conclusive.

---

## 🧠 The Interesting Part: Reward Hacking

I gave one AI bonus points for hovering upright and slowly in the air.

Instead of landing, it discovered that hovering continuously earned more rewards!

This is called **Reward Hacking** — when an AI exploits the reward system instead of achieving the intended goal.

I redesigned the reward function to encourage progress towards the landing pad, creating the Smart Pilot.

**Lesson learned:** AI learns what you reward, not necessarily what you intend.

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Gymnasium & Box2D | Lunar physics simulation |
| Stable-Baselines3 (PPO) | Reinforcement Learning |
| PyTorch | Neural network framework |
| Streamlit | Interactive web dashboard |

---

## 💻 How to Run

**1. Clone the repository**

```bash
git clone https://github.com/khushi10-coder/lunar-lander-rl.git
cd lunar-lander-rl
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate it**

Windows:
```powershell
.\.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Launch the dashboard**

```bash
python -m streamlit run app.py
```

Open `http://localhost:8501` and start your lunar mission! 🌙

---

## 🧪 Train Your Own Pilot

```bash
python src/train.py --variant fixed --steps 1000000 --seed 0
```

Available variants: `baseline`, `time`, `hover`, `fixed`.

**Evaluate all pilots:**

```bash
python src/evaluate.py
```

---

## 💡 What I Learned

- Reinforcement Learning and PPO.
- Reward shaping and policy optimization.
- AI behavior through trial and error.
- Reward hacking and unintended AI behavior.
- Model evaluation and performance comparison.
- Building interactive AI dashboards.

---

## 👩‍🚀 Author

**Khushi Nanekar** — [GitHub Profile](https://github.com/khushi10-coder)

---

<p align="center">
  <b>🚀 Four pilots. One moon. One unexpected cheater.</b>
  <br/>
  <i>Sometimes AI doesn't break the rules. It finds loopholes in them.</i>
</p>
