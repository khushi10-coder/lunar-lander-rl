import argparse
import gymnasium as gym
from gymnasium.wrappers import RecordVideo
from stable_baselines3 import PPO

parser = argparse.ArgumentParser()
parser.add_argument("--variant", default="baseline")
parser.add_argument("--seed", type=int, default=0)
parser.add_argument("--episodes", type=int, default=3)
args = parser.parse_args()

env = gym.make("LunarLander-v3", render_mode="rgb_array")
env = RecordVideo(env, video_folder=f"videos/{args.variant}",
                  name_prefix=f"{args.variant}_seed{args.seed}",
                  episode_trigger=lambda ep: True)
model = PPO.load(f"models/{args.variant}_seed{args.seed}")

for _ in range(args.episodes):
    obs, _ = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, r, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
env.close()