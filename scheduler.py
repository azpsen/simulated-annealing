from math import exp

class LinearScheduler:
    def __init__(self, temperature, rate, limit):
        self.temperature = temperature
        self.rate = rate
        self.limit = limit

    def __call__(self, t):
        val = self.temperature - (t * self.rate)
        return val if val < self.limit else 0


class ExponentialScheduler:
    def __init__(self, temperature, rate, limit):
        self.temperature = temperature
        self.rate = rate
        self.limit = limit

    def __call__(self, t):
        val = self.temperature * exp(-self.rate * t)
        return val if val < self.limit else 0
