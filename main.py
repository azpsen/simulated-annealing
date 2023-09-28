from fitness import FitnessFunction
from annealing import Annealer
from vizualizer import visualize

import scheduler
import successor

fitness_func = FitnessFunction()
ksc_coords = (46.81819372475244, -92.08550938909693)

eagle_mtn = (47.897391, -90.560111)

# schedule_func = scheduler.ExponentialScheduler(20, 0.005, 100)
schedule_func = scheduler.LinearScheduler(40, 0.005, 100)

successor_func = successor.GaussianSuccessorFunction(0.25)

a = Annealer(ksc_coords, fitness_func, schedule_func, successor_func)
sln = a.anneal(get_list=True)

print(f"Found {sln[-1]} at height {fitness_func(sln[-1])}")
print(f"Goal is {eagle_mtn} at height {fitness_func(eagle_mtn)}")

visualize(sln, eagle_mtn)