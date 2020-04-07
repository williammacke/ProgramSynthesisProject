import context
import random
from src.grammars.grammar import Grammar
from src.grammars.non_terminal import NonTerminal
from src.expressions import expression
from src.expressions import param
from src.expressions.optimization import optimize_expression
from skopt.space import Real
import numpy as np

inputs = [param.Input("x", 1)]
param = param.Param(Real(-100, 100), 0)

non_terminals = [NonTerminal([], ident=i) for i in range(1)]

symbols = inputs+non_terminals+[param]
terminals = inputs+[param]
j = 0
for nt in non_terminals:
    for i in range(1):
        fun = random.choice(expression.FUNCTIONS)
        nt.add_expression(expression.Expression(
            random.choices(symbols, k=fun.num_args), 
            fun.function, ident=j, func_string=fun.func_string))
        j += 1
    fun = random.choice(expression.FUNCTIONS)
    nt.add_expression(expression.Expression(random.choices(terminals, k=fun.num_args),
        fun.function, ident=j, func_string=fun.func_string))
    j += 1



grammar = Grammar(non_terminals[0], symbols, non_terminals)

p = grammar.gen_random_program()

print(p.code)

x = np.linspace(-5, 5, 1000)

def f(x):
    return 3*x+5
y = np.array([f(i) for i in x])

optimize_expression(p, x, y, inputs[0])
