import random
class NonTerminal:
    def __init__(self, expressions):
        self._expressions = expressions

    def expand(self):
        return random.choice(self._expressions).expand()

    def add_expression(self, expression):
        self._expressions.append(expression)
        

    @property
    def expressions(self):
        return self._expressions
