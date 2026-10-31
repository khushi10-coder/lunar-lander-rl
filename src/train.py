import argparse
from stable_baselines3 import PPO
from wrappers import make_env

parser = argparse.ArgumentParser()
parser.add_argument("--variant", default="baseline",
                    choices=["baseline", "time", "hover", "fixed"])
parser.add_argument("--steps", type=int, default=1_000_000)
parser.add_argument("--seed", type=int, default=0)
args = parser.parse_args()

env = make_env(args.variant)
model = PPO("MlpPolicy", env, seed=args.seed, verbose=1)
model.learn(total_timesteps=args.steps)

path = f"models/{args.variant}_seed{args.seed}"
model.save(path)
print("saved", path)