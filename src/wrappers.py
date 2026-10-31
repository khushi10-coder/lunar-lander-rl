import gymnasium as gym


class TimePenaltyWrapper(gym.Wrapper):
    """Small charge every frame so waiting costs something."""
    def __init__(self, env, fee=0.01):
        super().__init__(env)
        self.fee = fee

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        return obs, reward - self.fee, terminated, truncated, info


class HoverBonusWrapper(gym.Wrapper):
    """Deliberately flawed: +1 per frame when upright and slow."""
    def __init__(self, env, bonus=1.0):
        super().__init__(env)
        self.bonus = bonus

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        upright = abs(obs[4]) < 0.1                        # tilt
        slow = abs(obs[2]) < 0.1 and abs(obs[3]) < 0.1     # x and y speed
        if upright and slow:
            reward += self.bonus
        return obs, reward, terminated, truncated, info


class FixedWrapper(gym.Wrapper):
    """Pays for improvement (change between frames) plus a per-frame fee."""
    def __init__(self, env, fee=0.05, scale=1.0):
        super().__init__(env)
        self.fee, self.scale, self.prev = fee, scale, 0.0

    @staticmethod
    def _quality(obs):
        # higher = better: low speed, upright
        return -(abs(obs[2]) + abs(obs[3]) + abs(obs[4]))

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        self.prev = self._quality(obs)
        return obs, info

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        q = self._quality(obs)
        reward += self.scale * (q - self.prev) - self.fee
        self.prev = q
        return obs, reward, terminated, truncated, info


def make_env(variant="baseline", render_mode=None):
    env = gym.make("LunarLander-v3", render_mode=render_mode)
    if variant == "time":
        env = TimePenaltyWrapper(env)
    elif variant == "hover":
        env = HoverBonusWrapper(env)
    elif variant == "fixed":
        env = FixedWrapper(env)
    elif variant != "baseline":
        raise ValueError(f"unknown variant: {variant}")
    return env