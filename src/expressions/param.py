class Value:
    def __init__(self, value):
        self._value = value

    def setValue(self, value):
        pass

    @property 
    def value(self):
        return self._value

    @property
    def space(self):
        return []


class Param:
    def __init__(self, space, value=None):
        self._space = space
        self._value = value

    def setValue(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def space(self):
        return [self._space]



