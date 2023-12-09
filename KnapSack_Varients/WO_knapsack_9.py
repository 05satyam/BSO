import builtins
import copy
import math
import random
import sys
import time

import numpy as np
import KnapSack
#from KnapSack_Varients import visualize_knapsack
#from KnapSack_Varients.visualize_knapsack import animate_visualization_3d

ITEMS = {} #weights and values
RANGES = []
CAPACITY=0 # Knapsack capacity

times = []
results = []
plot_xvals = []
# Define problem parameters

n_whales = 300  #Number of whales
dimensions = 9  # Dimensionality of the search space
max_iter = 70000  # Maximum number of iterations

MAX_TRIALS=100
e = 90
generateTrailsCSV=True
fitness=KnapSack.knapsack_objective_fun_without_probablity_1


# whale class
class whale:
    def __init__(self, fitness, dim, minx, maxx, seed):
        self.position = [random.uniform(minx, RANGES[i]) for i in range(dim)]
        self.fitness = fitness(self.position, CAPACITY, ITEMS, dim)[1]  # curr fitness


def __wo_knapsack__(fitness, max_iter, n, dimensions, minx, maxx):
    rnd = random.Random(0)

    # create n random whales
    whales_positions = [whale(fitness, dimensions, minx, maxx, i) for i in range(n)]
    # compute the value of best_position and best_fitness in the whale Population
    best_solution = [0.0 for i in range(dimensions)]
    best_fitness = sys.float_info.max

    for i in range(n):  # check each whale
        if whales_positions[i].fitness < best_fitness:
            best_fitness = whales_positions[i].fitness
            best_solution = copy.copy(whales_positions[i].position)

    # main loop of woa
    itr = 0

    # Main loop
    while itr < max_iter:
        a = 2 * (1 - itr / max_iter)
        a2 = -1 + itr * ((-1) / max_iter)
        # Update positions of whales
        for i in range(n_whales):
            A = 2 * a * random.random() - a  # parameter A controls search radius
            C = 2 * random.random()  # parameter C controls spiral motion
            b = 1
            l = (a2 - 1) * rnd.random() + 1  # index of a random whale


            D = [0.0 for i in range(dimensions)]
            D1 = [0.0 for i in range(dimensions)]
            Xnew = [0.0 for i in range(dimensions)]
            Xrand = [0.0 for i in range(dimensions)]

            if random.random() < 0.5:
                if abs(A) > 1:
                    for j in range(dimensions):
                        D[j] = abs(C * best_solution[j] - whales_positions[i].position[j])
                        Xnew[j] = best_solution[j] - A * D[j]
                else:
                    p = random.randint(0, n_whales - 1)
                    while (p == i):
                        p = random.randint(0, n_whales - 1)

                    Xrand = whales_positions[p].position

                    for j in range(dimensions):
                        D[j] = abs(C * Xrand[j] - whales_positions[i].position[j])
                        Xnew[j] = Xrand[j] - A * D[j]
            else:
                for j in range(dimensions):
                    D1[j] = abs(best_solution[j] - whales_positions[i].position[j])
                    Xnew[j] = D1[j] * math.exp(b * l) * math.cos(2 * math.pi * l) + best_solution[j]

            #updating new position for ith whale
            for j in range(dimensions):
                '''
                    update the new position between 0 to max range for each dimention                    
                '''
                Xnew[j] = builtins.max(round(Xnew[j]), 0)
                Xnew[j] = min(round(Xnew[j]), RANGES[j])

            # Evaluate fitness of new position
            new_fitness = fitness(Xnew, CAPACITY, ITEMS, dimensions)[1]

            # Update best solution
            if new_fitness < best_fitness:
                best_solution = Xnew
                best_fitness = new_fitness
        itr+=1

    print("best_solution : ", best_solution)
    print("best_fitness  : ", best_fitness)
    # Return best solution value
    return best_fitness, best_solution



start_time = time.process_time()


best_solution_res=[]
summ=0
while e < MAX_TRIALS:
    start_time_per_trial = time.process_time()
    random.seed(1)
    # knapsack ITEMS{Weights, Values}, RANGES, CAPACITY
    #ITEMS, RANGES, CAPACITY = KnapSack.generate_random_items_ranges(dimensions)
    ITEMS = KnapSack.item_list_10[e]
    RANGES = KnapSack.range_list_10[e]
    CAPACITY = KnapSack.CAPACITY[dimensions]
    #calling wo knapsack
    best_fitness_val, best_solution = __wo_knapsack__(fitness, max_iter, n_whales, dimensions, 0, CAPACITY)
    print("e - ",e, "  fitness val-  ", best_fitness_val)
    results.append(best_fitness_val)
    best_solution_res.append(best_solution)
    times.append(time.process_time() - start_time_per_trial)
    summ += best_fitness_val
    e = e + 1


success_results_count = 0
for i in results:
    if(i!=-1):
        success_results_count+=1
accuracy = success_results_count/len(results)
avg_time = sum(times)/len(times)
print("Total number of trials ", len(results), " Accuracy ", accuracy*100, " Avg time per trail ", avg_time )
print("avg : ", (summ/100))
###############store results to xls file##############
import xlwt
from xlwt import Workbook

wb = Workbook()

if (generateTrailsCSV):
    sheet1 = wb.add_sheet('file')
    i = 0
    for wr in results:
        sheet1.write(i, 0, wr)
        sheet1.write(i, 1, times[i])
        i += 1

    wb.save('WO_knapsack_16nov_'+str(e) + '-'+str(MAX_TRIALS)+'_'+ str(fitness.__name__) + '_' + str(dimensions + 1) + '.xls')
    print("All time saved")



# visualize_knapsack.visualize_knapsack_implementaion(ITEMS, CAPACITY, dimensions, best_solution_res, 'WO-knapsack')

#animate_visualization_3d(100,ITEMS, CAPACITY, dimensions, best_solution_res , RANGES, results, "WO-knapsack-animation-2")
