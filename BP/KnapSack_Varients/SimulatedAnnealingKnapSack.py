'''
In this implementation, we define the knapsack problem with a list of weights, a list of values, and a capacity.
We also define the initial temperature, cooling rate, and stopping temperature for the simulated annealing algorithm.
The objective value function calculates the total value of a given solution, and returns

running for 1 min
'''
import copy
import random
import math

# Define the knapsack problem with weights and values
import time

import KnapSack
#from KnapSack_Varients import visualize_knapsack
#from KnapSack_Varients.visualize_knapsack import animate_visualization_3d

dimensions = 19 #represent dimensions
ITEMS = {} #weights and values
RANGES = []
plot_xvals = []

# Define the initial temperature, cooling rate, and stopping temperature
INTIAL_TEMP = 2500
cooling_rate = 0.0000018 #10d
STOPPING_TEMP = 1e-7
times = []
results = []


generateTrailsCSV=True
fitness = KnapSack.knapsack_objective_fun_without_probablity_1
e = 0
MAX_TRIALS=10
file_name = 'SA_knapsack_16nov_' + str(e) + str(MAX_TRIALS) + '_' + str(fitness.__name__) + '_' + str(dimensions + 1) + '.xls'

# Define the function to make a decision whether to accept the neighbor solution
def accept_neighbor(current_value, neighbor_value, temperature):
    if neighbor_value > current_value:
        return True
    else:
        delta = neighbor_value - current_value
        probability = math.exp(delta / temperature)
        return random.uniform(0, 1) < probability


def create_neighbours(curr_solution):
    neighbour_solution = copy.deepcopy(curr_solution)
    for i in range(0, dimensions):
        if (random.uniform(0, 1) >= 0.5):
            if (random.uniform(0, 1) >= 0.5 and neighbour_solution[i] < RANGES[i]):  # increase
                neighbour_solution[i] += 1
            elif (neighbour_solution[i] > 0):  # decrease
                neighbour_solution[i] -= 1
    return neighbour_solution

# Define the simulated annealing algorithm
def simulated_annealing(CAPACITY, RANGES):
    '''generate a random solution'''
    current_solution = [random.randint(0, RANGES[_]) for _ in range(0, dimensions)]
    #print("current_solution ", current_solution)
    current_value = fitness(current_solution, CAPACITY, ITEMS, dimensions)[1]
    temperature = INTIAL_TEMP

    while temperature > STOPPING_TEMP:
        '''make a neighbor solution'''
        neighbour_solution = create_neighbours(current_solution)
        neighbor_value = fitness(neighbour_solution, CAPACITY, ITEMS, dimensions)[1]
        if accept_neighbor(current_value, neighbor_value, temperature):
            current_solution = neighbour_solution
            current_value = neighbor_value
        temperature *= 1 - cooling_rate
    return current_solution, current_value


start_time = time.process_time()
# Run the simulated annealing algorithm

best_solution_res=[]
while e < MAX_TRIALS:
    start_time_per_trial = time.process_time()
    #ITEMS, RANGES, CAPACITY = KnapSack.generate_random_items_ranges(dimensions)
    ITEMS = KnapSack.item_list_20_1[e]
    RANGES = KnapSack.range_list_20[e]
    CAPACITY = KnapSack.CAPACITY[dimensions]
    best_solution, best_value = simulated_annealing(CAPACITY, RANGES)
    print(" e - ",e,   "best_value: ", best_value)
    #print("best_solution ", best_solution)
    results.append(best_value)
    best_solution_res.append(best_solution)
    plot_xvals.append(best_solution)
    times.append(time.process_time() - start_time_per_trial)
    # if(time.process_time() - start_time >300): #5min break
    #     break;
    e=e+1

success_results_count = 0;
for i in results:
    if(i!=-1):
        success_results_count+=1
accuracy = success_results_count/len(results)
avg_time = sum(times)/len(times)
print("Total number of trials ", len(results), " Accuracy ", accuracy*100, " Avg time per trail ", avg_time )



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

    wb.save(file_name)

    print("All time saved")

#visualize_knapsack.visualize_knapsack_implementaion(ITEMS, CAPACITY, dimensions, best_solution_res, 'SA-knapsack')
#animate_visualization_3d(100,ITEMS, CAPACITY, dimensions, plot_xvals , RANGES, results, "SA-knapsack-animation-1")
