import functools
import copy
import random
class Function:
    def __init__(self, function, num_args, func_string=""):
        self._function = function
        self._num_args = num_args
        self._func_string = ""

    @property
    def function(self):
        return self._function

    @property
    def num_args(self):
        return self._num_args

    @property
    def func_string(self):
        return self._func_string

    def __deepcopy__(self):
        return Function(self._function, self._num_args)

class VarArgsFunction(Function):
    def __init__(self, function, min_args, max_args, func_string=""):
        super().__init__(function, max_args, func_string)
        assert self._min_args < self._max_args
        self._min_args = min_args
        self._max_args = max_args

    @property
    def num_args(self):
        return int(random.random()*(self._max_args-self._min_args))+self._min_args

class Expression:
    def __init__(self, params, function, ident=None):
        self._params = params
        for p in self._params:
            p.parent = self
        self._function = function
        self._id = ident
        self._parent = None

    def expand(self):
        return Expression([p.expand() for p in self._params], self.function)


    @property
    def value(self):
        values = [p.value for p in self._params]
        return self._function(*values)

    @property
    def id(self):
        return self._id

    @property
    def parent(self):
        return self._parent

    def setValue(self, values):
        for value,param in zip(values, self.params):
            param.setValue(value)

    def setInput(self, values):
        for value,param in zip(values, self.inputs):
            param.setInput(value)

    @property
    def space(self):
        return [item for param in self._params for item in param.space]

    @property
    def params(self):
        return [p for param in self._params for p in param.params]

    @property
    def inputs(self):
        return [p for param in self._params for p in param.inputs]

    def __deepcopy__(self):
        return Expression([copy.deepcopy(p) for p in self._params], self._function, self._id)

def PLUS(*args):
    return functools.reduce(lambda a,b:a+b, args)

def MINUS(a, b):
    return a-b

def MULT(*args):
    return functools.reduce(lambda a,b:a*b, args)

def DIV(a, b):
    return a/b

def IF(a, b, c):
    if a:
        return b
    else:
        return c

FUNCTIONS = [
        VarArgsFunction(PLUS, 2, 10, "(+ {})"),
        Function(MINUS, 2, "(- {})"),
        VarArgsFunction(MULT, 2, 10, "(* {})"),
        Function(DIV, 2, "(/ {})"),
        Function(IF, 3, "(if {})")
        ]
