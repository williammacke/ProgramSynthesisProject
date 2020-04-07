from src.RL.policy import Policy
import numpy as np
from src.evolution.eval import evaluate

def train(policy, env, expert, gamma=0.9, num_rollouts=100):
    reward = float('-inf')
    next_reward = 0
    rollouts = []
    for _ in range(num_rollouts):
        rollout = []
        done = False
        obs = env.reset()
        while not done:
            action, _states = expert.predict(obs)
            nobs, reward, done, _ = obs.step(action)
            rollout.append((obs, action, reward))
            obs = nobs
        rollout.append((obs, None, None))
        rollouts.append(rollout)
    while reward < next_reward:
        next_reward = float('-inf')
        neighborhood = policy.get_neighborhood()
        dists = np.zeros(len(neighborhood))
        for i,p in enumerate(neighborhood):
            p.optimize(rollouts)
            dists[i] = p.distance(rollouts)
        i = np.argmin(dists)
        policy = neighborhood[i]
        reward = next_reward
        next_reward = np.mean(evaluate(policy, env, gamma))
    return policy
