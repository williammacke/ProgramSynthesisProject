import random
import copy
class NonTerminal:
    def __init__(self, expressions, ident=None):
        self._expressions = expressions
        self._id = ident


    @property
    def id(self):
        return self._id


    def expand(self):
        return random.choice(self._expressions).expand()

    def add_expression(self, expression):
        self._expressions.append(expression)
        
    @property
    def expressions(self):
        return self._expressions

    def __deepcopy__(self):
        return NonTerminal([copy.deepcopy(e) for e in self._expressions], self._id_)

