from random import uniform
from math import exp

import sys

DEBUG = True


class Annealer:
    def __init__(self, initial_state, fitness_func, schedule_func, successor_func):
        self.initial_state = initial_state
        self.value = fitness_func
        self.schedule = schedule_func
        self.successor = successor_func

    def anneal(self, get_list=False):
        coords = []
        current = self.initial_state
        best = current

        for t in range(0, sys.maxsize):
            if get_list:
                if len(coords) == 0 or not coords[-1] == current:
                    coords.append(current)
            T = self.schedule(t)

            if T == 0:
                if DEBUG:
                    print(f"Finished after {t} iterations")
                if get_list:
                    coords.append(best)
                    return coords
                else:
                    return best

            next_neighbor = self.successor(current)

            delta_e = self.value(next_neighbor) - self.value(current)

            if delta_e > 0 or (exp(delta_e / T) > uniform(0, 1)):
                current = next_neighbor
                if self.value(current) > self.value(best):
                    best = current
