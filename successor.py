from fitness import FitnessFunction
from random import normalvariate


class GaussianSuccessorFunction:
    def __init__(self, variance):
        self.f = FitnessFunction()
        self.mean = 0
        self.variance = variance

    def __call__(self, node):
        neighbor = node
        elevation = None
        while elevation is None or neighbor == node:
            shift = (normalvariate(self.mean, self.variance), normalvariate(self.mean, self.variance))
            neighbor = (node[0] + shift[0], node[1] + shift[1])
            elevation = self.f(neighbor)
        return neighbor
