# python implementation of Grey wolf optimization (GWO)
import random
import math  # cos() for Rastrigin
import copy  # array-copying convenience
import sys  # max float

import KnapSack
import time
import xlwt
from xlwt import Workbook


# wolf class
class wolf:
    def __init__(self, fitness, dim, minx, maxx, seed):
        #     self.rnd = random.Random(seed)
        self.position = [random.uniform(minx, RANGES[i]) for i in range(dim)]
        self.fitness = fitness(self.position, CAPACITY, ITEMS, dim)[1]  # curr fitness


# grey wolf optimization (GWO)
def __gwo_knapack__(fitness, max_iter, n, dim, minx, maxx):
    # create n random wolves
    population = [wolf(fitness, dim, minx, maxx, i) for i in range(n)]
    # On the basis of fitness values of wolves
    # sort the population in asc order
    population = sorted(population, key=lambda temp: temp.fitness)
    # best 3 solutions will be called as
    # alpha, beta and gama
    alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])
    # main loop of gwo
    Iter = 0
    while Iter < max_iter:
        # if Iter % 10 == 0 and Iter > 1:
        #     print(str(population[0].position)+"-"+str(population[1].position))
        #     print("Iter = " + str(Iter) + " best fitness = %.3f" % alpha_wolf.fitness)
        # linearly decreased from 2 to 0
        a = 2 * (1 - Iter / max_iter)
        # updating each population member with the help of best three members
        for i in range(n):
            X1 = [0.0 for i in range(dim)]
            X2 = [0.0 for i in range(dim)]
            X3 = [0.0 for i in range(dim)]
            Xnew = [0.0 for i in range(dim)]
            j = 0
            while j < dim:
                A1, A2, A3 = a * (2 * random.uniform(0, 1) - 1), a * (2 * random.uniform(0, 1) - 1), a * (
                            2 * random.uniform(0, 1) - 1)
                C1, C2, C3 = 2 * random.uniform(0, 1), 2 * random.uniform(0, 1), 2 * random.uniform(0, 1)
                X1[j] = alpha_wolf.position[j] - A1 * abs(C1 * alpha_wolf.position[j] - population[i].position[j])
                X2[j] = beta_wolf.position[j] - A2 * abs(C2 * beta_wolf.position[j] - population[i].position[j])
                X3[j] = gamma_wolf.position[j] - A3 * abs(C3 * gamma_wolf.position[j] - population[i].position[j])
                Xnew[j] = round((X1[j] + X2[j] + X3[j]) / 3)
                if (Xnew[j] >= 0 and Xnew[j] <= RANGES[j]):
                    # print(Xnew)
                    j += 1

            fnew = fitness(Xnew, CAPACITY, ITEMS, dim)[1]

            # greedy selection
            if fnew > population[i].fitness:
                population[i].position = Xnew
                population[i].fitness = fnew

        # On the basis of fitness values of wolves
        # sort the population in asc order
        population = sorted(population, key=lambda temp: temp.fitness)

        # best 3 solutions will be called as
        # alpha, beta and gama
        alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])

        Iter += 1
    # end-while

    # returning the best solution
    return alpha_wolf.position


# ----------------------------

ITEMS = {}  # weights and values
RANGES = []
CAPACITY = 0  # Knapsack capacity

exp = 40
num_of_iter = 50
dim = 19
num_particles = 200
rounds = 25000

fitness = KnapSack.knapsack_objective_fun_without_probablity_1
file_name = 'GWO_17nov_' + str(exp) + '_' + str(fitness.__name__) + '_' + str(dim + 1) + '.xls'
times = []
results = []
while exp < num_of_iter:
    # ITEMS, RANGES, CAPACITY = KnapSack.generate_random_items_ranges(dim)
    ITEMS = KnapSack.item_list_20_1[exp]
    RANGES = KnapSack.range_list_20[exp]
    CAPACITY = KnapSack.CAPACITY[dim]
    start_time = time.process_time()

    best_position = __gwo_knapack__(fitness, rounds, num_particles, dim, 0, CAPACITY)
    err = fitness(best_position, CAPACITY, ITEMS, dim)[1]

    results.append(err)
    print(exp, ' - ', err, '   position-  ', best_position)
    total_time = time.process_time() - start_time
    times.append(total_time)
    exp += 1

results_average = sum(results) / len(results)  # get an average
time_average = sum(times) / len(times)

success_results_count = 0
for i in results:
    if (i != -1):
        success_results_count += 1
accuracy = success_results_count / len(results)
avg_time = sum(times) / len(times)
print("Total number of trials ", len(results), " Accuracy ", accuracy * 100, " Avg time per trail ", avg_time)

wb = Workbook()

sheet1 = wb.add_sheet('file')
i = 0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i += 1

    wb.save(file_name)
    #     wb.close()
print("All saved")
