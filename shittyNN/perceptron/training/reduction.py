import numpy as np

def reduction_gradient_vector(targets, weighted_sums, inputs):
    n = len(targets)
    inputs = np.array(inputs).reshape((n, np.array(inputs[0]).size))
    return sum((i / sum(i)) * (t * max(0, t - a) + (t - 1) * max(0, a)) for i, t, a in zip(inputs, targets, weighted_sums))