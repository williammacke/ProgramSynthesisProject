import numpy as np
from src.expressions.optimization import optimize_expression

class Policy:
    def __init__(self, action_space, grammar, programs=None):
        self._grammar = grammar
        self._action_space = action_space
        if programs:
            self._programs = programs
        else:
            self._programs = np.array([grammar.gen_random_program() 
                for _ in range(action_space)])

    def __call__(self, obs):
        for prog in self._programs:
            prog.setInput(obs)
        return np.array([prog.value for prog in self._programs])

    def modify(self):
        return Policy(self._action_space, self._grammar, 
                np.array([self._grammar.modify(prog) for prog in self._programs]))

    def get_neighborhood(self, size=5):
        return np.array([self.modify() for _ in range(size)])

    def optimize(rollouts):
        obss = []
        actions = [[] for _ in range(self._action_space)]
        for rollout in rollouts:
            for obs, action, reward in rollout:
                obss.append(obs)
                for al,a in zip(actions, action):
                    al.append(a)
        for i,p in enumerate(self._programs):
            optimize_expression(p, obss, actions[i], self._grammar.inputs)
