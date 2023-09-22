# Simulated Annealing
# current = make_node(initial_state(problem))
# for t = 1 to inf
#   T = schedule(t)
#   if T == 0:
#     return current
#   next = randomly selected successor of current
#   deltaE = value(next) - value(current)
#   if deltaE > 0:
#     current = next
#   else current = next only with probability exp(deltaE / T)

# TODO Add adaptive annealing schedulers

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

    def anneal(self):
        coords = []
        current = self.initial_state

        for t in range(0, sys.maxsize):
            coords.append(current)
            T = self.schedule(t)

            if T == 0:
                if DEBUG:
                    print(f"Finished after {t} iterations")
                return coords

            next_neighbor = self.successor(current)

            delta_e = self.value(next_neighbor) - self.value(current)

            if delta_e > 0 or (exp(delta_e/T) > uniform(0, 1)):
                current = next_neighbor
