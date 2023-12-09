import copy
import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from datetime import datetime

import KnapSack
# from KnapSack_Varients.visualize_knapsack import animate_visualization_3d
import time

# from NonContinuousFunctions import *
# from KnapSack_Varients import visualize_knapsack
# from KnapSack_Varients.visualize_knapsack import animate_visualization_3d


generateTrailsCSV = True
DIMENSIONS = 19  # without y axis
# define hyper-parameters
###4d working
START_RESULTANT = 9  # start step size
END_RESULTANT = .000001  # end step size
START_ANGLE = 0.5
END_ANGLE = 89
MAX_ITER = 1600
NUM_OF_STEPS = 18000
ii = 0
fitness = KnapSack.knapsack_objective_fun_without_probablity_1
REFINEMENT_PREC = 0.0000000000001
low = 0
up = 0
ITEMS = {}  # weights and values
RANGES = []
CAPACITY = 0  # Knapsack capacity

outside_trajectoroies_count = 0
exp = 90
NUM_OF_ITERATIONS = 100
file_name='BP_knapsack_17nov90-100_' + str(fitness.__name__) + '_' + str(DIMENSIONS + 1) + '.xls'

#############################################
def iterative_refinement(isUnderneath, y_func, x_space, y_space, xsteps, yStep, cur_round):
    # jump in the middle of the step until crossing point is detected
    while abs(y_space - y_func) > REFINEMENT_PREC and yStep != 0:
        for j in range(0, DIMENSIONS):
            xsteps[j] = xsteps[j] / 2
        yStep = yStep / 2

        if (isUnderneath==False and y_space>y_func) or (isUnderneath==True and y_space<y_func) or y_space==y_func:
            for j in range(0, DIMENSIONS):
                x_space[j] = min(RANGES[j], round(x_space[j] + xsteps[j]))

            y_space += yStep
        else:
            for j in range(0, DIMENSIONS):
                x_space[j] = max(round(x_space[j] - xsteps[j]),0) # code for knapsack by SM
            y_space -= yStep

        y_func = fitness(x_space, CAPACITY, ITEMS, DIMENSIONS)[1]
        # if step gets too small, exit because we have a satisfactorily accurate solution
        if abs(yStep) < REFINEMENT_PREC:
            y_space = y_func

    return x_space, y_func


#############################################
def BPround(xvalues, y, i):
    # define cooling schedules for resultant and angle
    resultant = START_RESULTANT - i * (START_RESULTANT - END_RESULTANT) / MAX_ITER
    a = START_ANGLE - i * (START_ANGLE - END_ANGLE) / MAX_ITER

    # setting direction randomly #find resultant
    xsteps = []
    numerator = 0
    resultant_step = 0
    for j in range(DIMENSIONS):
        xsteps.append(random.uniform(0, 1))
        numerator += -(xsteps[j] ** 2) * (math.sin(math.radians(a)) ** 2)
        resultant_step += xsteps[j] ** 2

    yStep = -math.sqrt(numerator / ((math.sin(math.radians(a)) ** 2) - 1))
    resultant_step = math.sqrt(resultant_step + yStep ** 2)
    # find factor
    f = resultant / resultant_step

    # calculate steps of the vector for the given direction #start current vector
    x_space = []
    for j in range(0, DIMENSIONS):
        xsteps[j] = (xsteps[j] * abs(f))
        x_space.append(round(xvalues[j] + xsteps[j]))

    yStep = yStep * abs(f)
    y_space = y + yStep

    y_func = fitness(x_space, CAPACITY, ITEMS, DIMENSIONS)[1]

    if y_space < y_func:
        isUnderneath = True
    else:
        isUnderneath = False
    #print("x_space : ", x_space , " xsteps : ", xsteps)
    for countSteps in range(NUM_OF_STEPS):  # steps begin here
        if min(x_space) < low or max(x_space) > up:
            global outside_trajectoroies_count
            outside_trajectoroies_count += 1
            break

        if (isUnderneath == False and y_space < y_func) or (
                isUnderneath == True and y_space > y_func) or y_space == y_func:  ####crossing detected implementation

            xvalues, y = iterative_refinement(isUnderneath, y_func, x_space, y_space, xsteps, yStep, i)
            #print("isUnderneath ", isUnderneath, "  xsteps  ", xsteps ,  "  xvalues ", xvalues, "  y ", y)
            break

        for j in range(0, DIMENSIONS):
            x_space[j] = min(RANGES[j], round(x_space[j] + xsteps[j]))
        y_space += yStep
        y_func = fitness(x_space, CAPACITY, ITEMS, DIMENSIONS)[1]
        # print("steps  y_func ", y_func)

    return xvalues, y


#############################################

times = []
results = []

start_time1 = time.process_time()

plot_xvals = []
plot_xvals_ys = []

summ = 0
while exp < NUM_OF_ITERATIONS:  # number of experiments or number of trials
    # get random initial point
    # ITEMS, RANGES, CAPACITY = KnapSack.generate_random_items_ranges(DIMENSIONS) # code for knasack
    ITEMS = KnapSack.item_list_20[exp]
    RANGES = KnapSack.range_list_20[exp]
    CAPACITY = KnapSack.CAPACITY[DIMENSIONS]
    xvals = []
    low = 0
    up = CAPACITY

    # xvals = [round(random.uniform(low, up)) for i in range(DIMENSIONS)]
    xvals = [random.randint(0, RANGES[i]) for i in range(DIMENSIONS)]
    y = fitness(xvals, CAPACITY, ITEMS, DIMENSIONS)[1]
    print("start ", y, " xvals ", xvals)
    start_time = time.process_time()

    for i in range(MAX_ITER):  # number of rounds
        xvals, y = BPround(xvals, y, i)

    print(exp, " - end ", y, " xvals ", xvals)
    summ = summ + y
    total_time = time.process_time() - start_time
    plot_xvals.append(xvals)
    results.append(y)  # collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp += 1
# visualize_fun_trajec_move.visualize_3d(MAX_ITER, low, up, plot_xvals_ys, plot_xvals, fitness)
results_average = sum(results) / len(results)  # get an average
time_average = sum(times) / len(times)

now = datetime.now()

end_tym = now.strftime("%H:%M:%S")
print("avg: ", (summ / 100))
# -----------------remove below code while final submission
success_results_count = 0
for i in results:
    if (i != -1):
        success_results_count += 1
accuracy = success_results_count / len(results)
avg_time = sum(times) / len(times)
print("Total number of trials ", len(results), " Accuracy ", accuracy * 100, " Avg time per trail ", avg_time)

# ------------------below code is just to visualze
#visualize_knapsack.visualize_knapsack_implementaion(ITEMS, CAPACITY, DIMENSIONS, plot_xvals, RANGES, results, 'BP-knapsack-4')

# ------------------below code is to animate
#animate_visualization_3d(100,ITEMS, CAPACITY, DIMENSIONS, plot_xvals , RANGES, results, "BP-knapsack-animation-2")


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


