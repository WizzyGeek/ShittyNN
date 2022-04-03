class Runner:
    def __init__(self, dt: dict) -> None:
        self.dataset = dt

    def train(self, model):
        ...

    def compute_each(self, model):
        for i in self.dataset:
            yield model.compute(i)