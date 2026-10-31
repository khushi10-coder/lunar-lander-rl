import glob, json, os
import numpy as np
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

env = gym.make("LunarLander-v3")   # wrapper OFF
results = {}

for v in ["baseline", "time", "hover", "fixed"]:
    means = []
    for path in sorted(glob.glob(f"models/{v}_seed*.zip")):
        m, s = evaluate_policy(PPO.load(path), env, n_eval_episodes=20)
        means.append(m)
    if means:
        results[v] = {"mean": round(float(np.mean(means)), 1), "runs": len(means)}

os.makedirs("web", exist_ok=True)
with open("web/results.json", "w") as f:
    json.dump(results, f, indent=2)
print(results)