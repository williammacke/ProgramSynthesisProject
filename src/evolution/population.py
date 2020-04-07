from src.RL.policy import Policy
from src.RL.train import train


class Member:
    def __init__(self, grammar, env):
        self._grammar = grammar
        self._policy = Policy(env.action_space, grammar)
        self._fit = float('-inf')

    def train(self, env, expert, gamma=0.9, num_rollouts=100):
        self._policy = train(self._policy, env, expert, gamma, num_rollouts)

