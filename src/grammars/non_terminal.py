import random
import copy
class NonTerminal:
    def __init__(self, expressions, ident=None):
        self._expressions = expressions
        self._id = ident
        self._enabled = True
        self._valid_expressions = [e for e in expressions if e.enabled]

    def disable(self):
        self._enabled = False

    def enable(self):
        self._enabled = True


    @property
    def id(self):
        return self._id


    def expand(self):
        return random.choice(self._valid_expressions).expand()

    def add_expression(self, expression):
        self._expressions.append(expression)
        if expression.enabled:
            self._valid_expressions.append(expression)
    
        
    @property
    def expressions(self):
        return self._expressions

    @property
    def code(self):
        return str(self._id)

    def __deepcopy__(self, memo):
        return NonTerminal([copy.deepcopy(e) for e in self._expressions], self._id)

    @property
    def enabled(self):
        return self._enabled
