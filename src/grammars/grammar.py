import non_terminal
import random
from ..expressions.expression import Expression

class Grammar:
    def __init__(self, symbols, functions):
        self._symbols = symbols
        self._functions = functions

    def addSymbol(self, symbol):
        self._symbols.append(symbol)

    def gen_random_program(self):
        function = random.choice(self._functions)
        symbols = [random.choice(self._symbols) for _ in range(function.num_args)]
        return Expression(symbols, function.function).expand()
