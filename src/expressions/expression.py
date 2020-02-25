class Expression:
    def __init__(self, params, function):
        self._params = params
        self._function = function


    @property
    def value(self):
        values = [p.value for p in self._params]
        return self._function(*values)

    def setValue(self, values):
        for param,value in zip(self._params,values):
            param.setValue(values)

    @property
    def space(self):
        return [item for param in self._params for item in param.space]

