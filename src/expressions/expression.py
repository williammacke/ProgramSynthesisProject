class Expression:
    def __init__(self, params, function):
        self._params = params
        self._function = function

    def expand(self):
        return Expression([p.expand() for p in self._params], self.function)


    @property
    def value(self):
        values = [p.value for p in self._params]
        return self._function(*values)

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
