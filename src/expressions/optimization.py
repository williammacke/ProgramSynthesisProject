from expression import Expression
from skopt import gp_minimize

def optimize_expression(e, inputs, outputs):
    inputs = np.array(inputs)
    outputs = np.array(outputs)
    def evaluate_expression(*params):
        e.setValue(*params)
        y_ = []
        for i in inputs:
            e.setInput(*i)
            y_.append(e.value)
        y_ = np.array(y_)
        diff = outputs-y_
        return np.dot(diff, diff)

    results = gp_minimize(evaluate_expression, e.space)
    e.setValue(*results.x)
    return e
