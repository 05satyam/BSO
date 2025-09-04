import copy
import math
import random
from random import randint

import numpy as np

import NonContinuousFunctions
import functions
import visualize_optimization_functions_trajectories_
from functions import *
import time
from NonContinuousFunctions import *
# from NonContinuousRotatedHybridCompositeFunc import *
from datetime import date

###############limits of variables for each function#####################
DIMENSIONS = 2 # without y axis
NUM_OF_ITERATIONS= 1
generateTrailsCSV =False
# define hyper-parameters
START_RESULTANT = -0.5 # start step size
END_RESULTANT = 0.00001  # end step size
START_ANGLE = 1
END_ANGLE = 89
MAX_ITER = 50
NUM_OF_STEPS = 5000
fitness = functions.ackley
REFINEMENT_PREC = 0.0001
low = -5
up = 5
total_trials_outside_trjectory_count = []
total_trials_trajectories_outside_steps_count = []
total_outside_trjectory_count = 0
trajectories_outside_steps_count = 0


# print([[random.randint(1,10) for _ in range(49)] for _ in range(5)])

#############################################
def memoized_refining(x_prime, xvalues, y_func, y):
    '''
    Below code is used for the case: when number of steps are over and we are outside the stepping loop
    and the final xspace is either otuside the function space or not

    case1: if outside the function space return old values

    case2.1: if inside the function space but the final y_fun value is greater than the old value return old

    case2.2: if inside the function space but the final y_fun value is less than the old value return new y_fun
    '''
    if ((min(x_prime) < low or max(x_prime) > up) or y_func > y):  # spiderman case1
        #print("case1 ", x_space, "  yfun ", y_func)
        x_prime = copy.copy(xvalues)
        y_func = y

    #remove below commented code
    # if (min(x_space) >= low and max(x_space) <= up):  # spiderman case2.1 and 2.2
    #     #print("case2.1 ", x_space, "  yfun ", y_func)
    #     if (y_func > y_func_old):
    #         #print("case2.2 ", x_space_old, "  yfun ", y_func_old)
    #         x_space = copy.copy(x_space_old)
    #         y_func = y_func_old

    return x_prime, y_func



def SpiderManTrajectory(xvalues, y, i):
    # define cooling schedules for resultant and angle
    resultant = START_RESULTANT - i * (START_RESULTANT - END_RESULTANT) / MAX_ITER
    a = START_ANGLE - i * (START_ANGLE - END_ANGLE) / MAX_ITER
    # setting direction randomly #find resultant
    xsteps = []
    numerator = 0
    resultant_step = 0

    for j in range(DIMENSIONS):
        #if(random.uniform(low, up)<xvalues[j]):
        # if ((low + up) / 2 < xvalues[j]):
          #  xsteps.append(random.uniform(-1, 0))
        #else:
         #   xsteps.append(random.uniform(0, 1))

        xsteps.append(random.uniform(-1, 1))
        numerator += -(xsteps[j] ** 2) * (math.sin(math.radians(a)) ** 2)
        resultant_step += xsteps[j] ** 2

    yStep = -math.sqrt(numerator / ((math.sin(math.radians(a)) ** 2) - 1))
    resultant_step = math.sqrt(resultant_step + yStep ** 2)
    # find factor
    f = resultant / resultant_step
    # calculate steps of the vector for the given direction #start current vector
    x_prime = []
    #x_space_old = copy.copy(xvalues)
    #y_func_old = copy.copy(y)

    for j in range(0, DIMENSIONS):
        xsteps[j] = xsteps[j] * abs(f)
        x_prime.append(xvalues[j] + xsteps[j])
    yStep = yStep * abs(f)
    y_t = y + yStep        #hypothetical - y traj

    y_func = fitness(x_prime)

    if y_t < y_func:
        isUnderneath = True
    else:
        isUnderneath = False

    '''
    below variable is used for counting the number of steps after which we are outside function space
    '''
    outside_steps_count = 0
    for countSteps in range(NUM_OF_STEPS):  # steps begin here
        if min(x_prime) < low or max(x_prime) > up:
            '''case: outside function space break, no need to explore'''
            break

        '''
        case: check if new y_func is above the function space or not
        '''
        if (isUnderneath == True and y_t >= y_func):
            isUnderneath = False

        '''
        case: if above function and new values greater then old one, return old one and break;
        '''
        if (isUnderneath == False and y_func >= y):
            x_prime = copy.copy(xvalues)
            #y_space = y_space_old
            y_func = y
            break

        '''
        case : if new y_func is less then the old one, copy the new values to old 
        '''
        if (y_func < y):
            xvalues = copy.copy(x_prime)
            #y_space_old = y_space
            y = copy.copy(y_func)

        '''
        case: calculate new  steps
        '''
        for j in range(0, DIMENSIONS):
            x_prime[j] += xsteps[j]
        y_t += yStep
        y_func = fitness(x_prime)
        outside_steps_count += 1

    x_space, y_func = memoized_refining(x_prime, xvalues, y_func, y)

    return x_space, y_func




#############################################
# for START_RESULTANT in sr:
# for END_ANGLE in ea:
times = []
results = []
exp = 0
start_time1 = time.process_time()
plot_xvals = []
plot_xvals_ys = []
while exp < NUM_OF_ITERATIONS:  # number of experiments or number of trials
    # get random initial point
    xvals = []
    xvals = [random.uniform(low, up) for i in range(DIMENSIONS)]
    y = fitness(xvals)
    # print("start xvals ", xvals)
    print("start ", y)
    start_time = time.process_time()
    plot_xvals.append(xvals)
    plot_xvals_ys.append(y)
    for i in range(MAX_ITER):  # 10000000
        xvals, y = SpiderManTrajectory(xvals, y, i)
        #if(i>MAX_ITER-5):
          #  print("START_RESULTANT : ", START_RESULTANT, ' , END_RESULTANT: ', END_RESULTANT, ' , START_ANGLE: ', START_ANGLE, ' , END_ANGLE: ', END_ANGLE)
        plot_xvals.append(xvals)
        plot_xvals_ys.append(y)
        total_trials_outside_trjectory_count.append(i)
        total_trials_trajectories_outside_steps_count.append(trajectories_outside_steps_count)
    # print("total_outside_trjectory_count ", total_outside_trjectory_count)
    # print("err ", fitness(xvals))
    # print(" - end ", xvals)
    print(exp, " - end ", y)
    # print("size of total_outside_trjectory_count ", len(total_trials_outside_trjectory_count))
    # print("total_outside_trjectory_count ", total_outside_trjectory_count)
    # print("size of trajectories_outside_steps_count ", len(trajectories_outside_steps_count))
    # print("trajectories_outside_steps_count ", trajectories_outside_steps_count)

    total_time = time.process_time() - start_time

    results.append(y)  # collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp += 1

visualize_optimization_functions_trajectories_.visualize_3d(MAX_ITER, low, up, plot_xvals_ys, plot_xvals, fitness)
results_average = sum(results) / len(results)  # get an average
time_average = sum(times) / len(times)

# print("time:",time_average,"sec,",results_average, " precision, with",START_RESULTANT,"step and",END_ANGLE," angle end")
print("After", NUM_OF_ITERATIONS, "iterations of variant tr3 it is found that it takes ", time_average,
      " seconds per iteration and has a average distance of ", results_average, " from the global minimum")
###############store results to xls file##############
import xlwt
# from xlwt import Workbook
#
# wb = Workbook()
#
# if (generateTrailsCSV):
#     sheet1 = wb.add_sheet('file')
#     i = 0
#     for wr in results:
#         sheet1.write(i, 0, wr)
#         sheet1.write(i, 1, times[i])
#         i += 1
#
#     wb.save('Server-Results/Spiderman_5_'+ str(fitness.__name__) + '_' + str(DIMENSIONS + 1) + '.xls')
#     print("All time saved")
