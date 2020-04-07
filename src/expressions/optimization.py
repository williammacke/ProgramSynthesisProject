from collections.abc import Iterable
from src.expressions.expression import Expression
from skopt import gp_minimize
import numpy as np

def optimize_expression(e, x, y, inputs):
    x = np.array(x)
    y = np.array(y)
    def evaluate_expression(*params):
        e.setValue(*params)
        y_ = []
        for p in x:
            if isinstance(p, Iterable):
                for i,val in zip(inputs, p):
                    i.setInput(val)
            else:
                inputs.setInput(p)
            y_.append(e.value)
        y_ = np.array(y_)
        diff = y-y_
        err =  np.dot(diff, diff)
        return err

    results = gp_minimize(evaluate_expression, e.space)
    e.setValue(*results.x)
    return e
