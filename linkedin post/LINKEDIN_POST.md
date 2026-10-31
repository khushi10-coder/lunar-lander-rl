# Ready-to-Post LinkedIn Caption

Copy and paste the text below directly into your LinkedIn post, and attach `media/screenshots/agent_comparison.png` or `media/videos/rocket_lander_full_demo.mp4`!

---

### LinkedIn Post Draft:

What happens when you reward an AI pilot for floating? It learns how to cheat. 🚀

For my latest reinforcement learning project, I trained AI agents with Proximal Policy Optimization (PPO) to land a lunar rocket in OpenAI Gymnasium's `LunarLander-v3`.

Instead of just training a single model, I tested what happens when you modify how the agent receives points (Reward Shaping):

🎮 **1. Standard Pilot (Baseline):**
Trained on standard environmental rewards. Takes its time, balances attitude, and lands softly (Average Score: 219.2).

⚡ **2. Hurry-Up Pilot (Time Penalty):**
Penalized each second it spent in the air. Result: It became our most efficient pilot, cutting descent time and saving fuel (Average Score: 243.3).

🛸 **3. Cheater Pilot (The Hover Hack):**
I added a simple rule: +0.5 points for every frame the rocket stays upright. 
Instead of landing, the AI discovered a loophole: it hovered mid-air forever farming infinite points without ever touching down (Score: -12.0). A textbook example of **Reward Hacking**!

🧠 **4. Smart Pilot (Potential-Based Shaping):**
Using potential-based reward shaping ($\Phi(s') - \Phi(s)$), we rewarded only progress toward the landing pad. It fixed the loophole completely and achieved clean, graceful touchdowns (Average Score: 240.6).

---

### 🛠️ Built With:
- **PyTorch** & **Stable-Baselines3** (PPO)
- **OpenAI Gymnasium** & **Box2D physics**
- **Streamlit** for an interactive, beginner-friendly web dashboard

Check out the code, models, and interactive dashboard on GitHub:
👉 https://github.com/khushi10-coder/lunar-lander-rl

#ReinforcementLearning #MachineLearning #AI #Python #PPO #DataScience #DeepLearning #Gymnasium #Streamlit
