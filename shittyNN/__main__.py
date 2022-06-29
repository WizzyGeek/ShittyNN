import numpy as np
from math import exp

class Perceptron_NameSpace_Exp1:
    from . import Perceptron
    fn = "p_wts.npy"

    class Identify:
        unit = np.ones(4)
        z = np.zeros(4)
        l1 = [
            unit, z, z, z
        ]

        l2 = [z, unit, z, z]

        l3 = np.ones((4, 4))

    # @classmethod
    # def initialise_wts(cls):
    #     wts = np.zeros(16)
    #     np.save(cls.fn, wts)
    #     wts = np.load(cls.fn, allow_pickle=True)
    #     print(wts)

    @classmethod
    def run(cls):
        p = cls.Perceptron(np.load(cls.fn, allow_pickle=True))
        I = cls.Identify
        for i in (I.l1, I.l2, I.l3):
            print(p.compute(i)) # F!ck the activation function lmao add it later when this shit works

    @classmethod
    def train(cls): # well a perceptron obviously cant diff between a 4x4 1s
        # and horizontal rows so we will limit our selves to detecting first two rows
        # 1/4 *  [
            # 1, 1, 1, 1
            # 1, 1, 1, 1
            # -1, -1, -1, -1
            # -1, -1, -1, -1
        #] These should be our weights for this trivial nueral network equivalent of hello world
        p = cls.Perceptron(np.zeros(16))
        I = cls.Identify
        inputs = np.array((I.l1, I.l2, I.l3)).reshape((3, 16))
        print(inputs)
        targets = [1, 1, 0]
        weighted_sums = []

        from .perceptron.training import reduction_gradient_vector

        itr = 0
        while True:
            for i in (I.l1, I.l2, I.l3):
                weighted_sums.append(p.compute(i))

            delta = reduction_gradient_vector(targets, weighted_sums, inputs)
            print(delta)
            print(p.wt + delta)
            print("=" * 4, itr)

            p.wt += delta
            weighted_sums = []
            itr += 1
            try:
                input()
            except KeyboardInterrupt:
                break

    # Reduction method worked!!
    # cons: Whole lot of iterations on the same set, took around 10 iterations
    # pros: Extremely accurate result

e1 = Perceptron_NameSpace_Exp1

class Perceptron_Exp2:
    dataset = {
        (1, 0): 1,
        (1, 1): 1,
        (0, 1): 1,
        (0, 0): 0
    }
    from . import Perceptron

    # if I understand correctly
    # Then this should cause the weights to explode
    # or may be it wont and just dally around and never achieve the relation
    # idk what i am doing tbh
    @classmethod
    def main(cls):
        # https://www.desmos.com/calculator/hbegeknhvq
        def activation(x):
            return 1 - (exp(-1 * x) * (1 - x))
        def slope(x):
            return exp(-1 * x) * (2 - x)
        from shittyNN.perceptron.training.gradient import gradient_vector
        P = cls.Perceptron(np.zeros(2))
        results = []
        weighted_sums = []
        r = .1 # rate of learning

        while 1:
            for i in cls.dataset:
                k = P.compute(i)
                weighted_sums.append(k)
                results.append(activation(k))

            v = gradient_vector(cls.dataset.values(), results, weighted_sums, tuple(cls.dataset.keys()), slope)
            print(results)
            print(v)
            results = []
            weighted_sums = []
            P.wt -= v * r # looking at this after writing theory, double checked it
            # code is all correct the activation function is just shit.
            print(P.wt)
            try:
                input()
            except KeyboardInterrupt:
                break
    # Results
    # The perceptron did not achieve the perfect weights due to the nature of the graph of the activation function in which the
    # slope decreases as it approaches 1, which was the target, hence the unattainibility of the perfect weights can be attributed to activation function
    # selection
    # The Perceptron training speed was proportional to the rate of learning
    # In all the cases the perceptron approched the correct results in a forgivable margin for both high and low learning rates
    # The weights did not converge and kept increasing however for large rate of learning the limitations of floating point numbers
    # stopped the the weights from increasing much quicker than for small which can also be attributed to the activation function

    # The selection of an activation function passing through origin led to (0, 0): 0 relation to not be included in the training
    # as bias was not a part and the weightd sum of this input is already the target which remains the same when passed through the activation function

if __name__ == "__main__":
    # e1.initialise_wts()
    # e1.train()
    Perceptron_Exp2.main()