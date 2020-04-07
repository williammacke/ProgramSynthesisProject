from src.grammars import non_terminal
import random
import copy
from src.expressions.expression import Expression
from skopt.space import Real

class Grammar:
    def __init__(self, start, env, non_terminals = []):
        self._start = start
        self._non_terminals = set([start] + list(non_terminals))
        assert len(env.observation_space.shape) == 1
        num_inputs = env.observation_space.shape[0]
        self._inputs = np.array([Input(f"x{i}") for i in range(num_inputs)])
        terminals = list(self._inputs) + [Param(Real(-100,100))]
        self._symbols = set(list(self._non_terminals) + list(terminals))
        self._expressions = {e.id:e for nt in self._non_terminals for e in nt.expressions}

    def add_terminal(self, terminal):
        self._symbols.add(terminal)

    def add_non_terminal(self, non_terminal):
        self._non_terminals.add(non_terminal)
        self._symbols.add(non_terminal)
        self._expressions.update({non_terminal.id:non_terminal})

    def gen_random_program(self):
        return self._start.expand()

    def modify_program(self, program, random_prob=0):
        if random.random() < random_prob:
            return self.get_random_program()
        p = copy.deepcopy(program)
        e = random.choice(p.expressions)
        ep = e.parent
        if ep:
            for i,expr in enumerate(ep._params):
                if expr == e:
                    ep._params[i] = copy.deepcopy(self._expressions[e.id])
        else:
            p = self._expressions(p.id)
        return p.expand()



    @property
    def non_terminals(self):
        return self._non_terminals

    @property
    def inputs(self):
        return self._inputs

    def contains(self, nt):
        return nt in self._non_terminals
