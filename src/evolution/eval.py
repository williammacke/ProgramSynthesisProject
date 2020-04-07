
def evaluate(policy, env, gamma=0.9, num_rollouts=1):
    returns = []
    for _ in range(num_rollouts):
        obs = env.reset()
        done = False
        rewards = []
        while not done:
            obs, reward, done, _ env.step(policy(obs))
            reward.append(reward)
        G = 0
        for r in reversed(rewards):
            G = r + gamma*G
        returns.append(G)
    return returns
