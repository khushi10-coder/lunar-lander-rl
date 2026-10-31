import glob, os
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

env = gym.make("LunarLander-v3")   # wrapper OFF
print(f"{'model':28} {'mean':>8} {'std':>8}")

for path in sorted(glob.glob("models/*.zip")):
    model = PPO.load(path)
    mean, std = evaluate_policy(model, env, n_eval_episodes=20)
    print(f"{os.path.basename(path):28} {mean:8.1f} {std:8.1f}")