from fitness import FitnessFunction
from annealing import Annealer

import scheduler
import successor

fitness_func = FitnessFunction()
ksc_coords = (46.81819372475244, -92.08550938909693)

eagle_mtn = (47.897391, -90.560111)

schedule_func = scheduler.ExponentialScheduler(20, 0.005, 100)
# schedule_func = scheduler.LinearScheduler(250, 0.01)

successor_func = successor.GaussianSuccessorFunction(0.25)

a = Annealer(ksc_coords, fitness_func, schedule_func, successor_func)
sln = a.anneal()

print(f"Found {sln[-1]} at height {fitness_func(sln[-1])}")
print(f"Goal is {eagle_mtn} at height {fitness_func(eagle_mtn)}")

print()
prev = 0
for i in range(0, len(sln)):
    if not sln[i] == prev:
        print(f"{sln[i][0]}, {sln[i][1]}")
        prev = sln[i]
