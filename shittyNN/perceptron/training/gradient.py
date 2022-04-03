import numpy as np

# functions for reference
def calculate_error(targets, results):
    if len(targets) != len(results):
        raise Exception("differing target-result pair provided")

    n = len(targets)
    return (sum((i - j) ** 2 for i, j in zip(targets, results)) / (2 * n))

def gradient_for_wt(targets, results, weighted_sums, inputs, activator_slope_fn, wt_index):
    n = len(targets)

    if n != len(results) or n != len(inputs) or n != len(weighted_sums):
            raise Exception("differing target-result-input-sums pair provided")

    inputs = [np.array(i).flatten() for i in inputs]

    return (sum((t - a) * activator_slope_fn(s) * (-1 * x) for t, a, s, x in zip(targets, results, weighted_sums, map(lambda x: x[wt_index], inputs))) / n)

def correction_gradient_for_wt(targets, results, weighted_sums,  inputs, activator_slope_fn, wt_index):
    return -1 / gradient_for_wt(targets, results, weighted_sums, inputs, activator_slope_fn, wt_index)


# actually useful functions
def intermediate_gradient_vector(targets, results, weighted_sums, activator_slope_fn):
    return np.array(tuple((a - t) * activator_slope_fn(s) for t, a, s in zip(targets, results, weighted_sums)))

def gradient_vector(targets, results, weighted_sums, inputs, activator_slope_fn): # dw = -n * v
    n = len(targets)

    if n != len(results) or n != len(inputs) or n != len(weighted_sums):
        raise Exception("differing target-result-input-sums pair provided")

    inter = intermediate_gradient_vector(targets, results, weighted_sums, activator_slope_fn)
    inputs = np.array(inputs).reshape((n, len(inputs[0])))
    return np.array(tuple(np.dot(inter, inputs[:, i]) for i in range(inputs.shape[1])))

# experiments
# dw = -n * n(D) * v
def mean_gradient_vector(targets, results, weighted_sums, inputs, activator_slope_fn): # this is my own experiment thingy
    return gradient_vector(targets, results, weighted_sums, inputs, activator_slope_fn) / len(targets)

# dw = V * r
def correction_gradient_vector(targets, results, weighted_sums, inputs, activator_slope_fn): # another experiment thingy
    return np.array(-1 / i for i in gradient_vector(targets, results, weighted_sums, inputs, activator_slope_fn))
