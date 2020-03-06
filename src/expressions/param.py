import copy
class Value:
    def __init__(self, value):
        self._value = value

    def setValue(self, value):
        pass

    @property 
    def value(self):
        return self._value

    def expand(self):
        return copy.deepcopy(self)

    @property
    def space(self):
        return []

    @propery
    def params(self):
        return []

    @propery
    def inputs(self):
        return []

    def __deepcopy__(self):
        return Value(self.value)


class Param:
    def __init__(self, space, value=None):
        self._space = space
        self._value = value

    def setValue(self, value):
        self._value = value

    def setInput(self, value):
        pass

    def expand(self):
        return copy.deepcopy(self)

    @property
    def value(self):
        return self._value

    @property
    def space(self):
        return [self._space]

    @property
    def params(self):
        return [self]

    @property
    def inputs(self):
        return []

    def __deepcopy__(self):
        return Param(self._space, self._value)


class Input:
    def __init__(self, name, value=None):
        self._name = name
        self._value = value

    def setValue(self, value):
        pass
    
    def setInput(self, value):
        self._value = value

    def expand(self):
        return copy.deepcopy(self)

    @property
    def value(self):
        return self._value

    @property
    def params(self):
        return []

    @property
    def inputs(self):
        return [self]

    def __deepcopy__(self):
        return Input(self._name, self._value)
