# Simulated Annealing
An implementation of the simulated annealing algorithm used to approximate the global optimum; in this case used to estimate the highest point in Minnesota.

### Best Solution
This image shows the path taken in finding the best solution. This run took 149027 iterations and used the following parameters for the scheduler and successor function:

| Parameter | Value |
| :--- | ---: |
| Scheduler | Exponential |
| Initial Temperature | 20 |
| Decay Rate | 0.005 |
| Successor Variance | 0.25 |

![Path taken by algorithm](img/best_sln.png)