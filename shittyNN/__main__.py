import numpy as np

from shittyNN.perceptron.training import gradient

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

    @classmethod
    def initialise_wts(cls):
        wts = np.zeros(16)
        np.save(cls.fn, wts)
        wts = np.load(cls.fn, allow_pickle=True)
        print(wts)

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
        p = cls.Perceptron(np.load(cls.fn, allow_pickle=True))
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

if __name__ == "__main__":
    e1.initialise_wts()
    e1.train()