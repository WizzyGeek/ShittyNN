import numpy as np

class Perceptron:
    def __init__(self, weights, bias=0):
        if weights is not None and isinstance(weights, (tuple, list, np.ndarray)):
            self.wt = np.array(weights).flatten()
        elif isinstance(weights, int):
            self.wt = np.ones(weights)
        else:
            raise Exception("Bad weights value provided")

        self.bias = bias # place holder dont actually plan on training this lol

    def compute(self, inp: list | tuple | np.ndarray) -> int:
        return np.vdot(self.wt, inp) + self.bias # type: ignore

