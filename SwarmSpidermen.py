import builtins
import copy
import math
import random
import sys
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

NUM_OF_ITERATIONS = 1
generateTrailsCSV = False
DIMENSIONS = 9  # without y axis
# define hyper-parameters
START_RESULTANT = -10  # start step size
END_RESULTANT = 0.000001  # end step size
START_ANGLE = 7
END_ANGLE = 0
MAX_ITER = 3000
NUM_OF_STEPS = 30
fitness = NonContinuousFunctions.rastrigin
low = -5.12
up = 5.12
c_nc = "nc_"

times = []
results = []
exp = 0
start_time1 = time.process_time()
num_spiderman = 1000



class spiderman:
     def __init__(self, fitness, dimension, low, up, seed):
         self.position = [random.uniform(low, up) for i in range(dimension)]
         self.fitness = fitness(self.position)


#############################################
def spiderMan(spidermanPopulation, Xbest, Fbest, i):

    for spiderman_i in range(num_spiderman): # iterating on all spidermans
        xsteps = []
        numerator = 0
        resultant_step = 0
        # define cooling schedules for resultant and angle
        resultant = START_RESULTANT - i * (START_RESULTANT - END_RESULTANT) / MAX_ITER
        a = START_ANGLE - i * (START_ANGLE - END_ANGLE) / MAX_ITER
        for j in range(DIMENSIONS):
            if ((low + up) / 2 < spidermanPopulation[spiderman_i].position[j]):
                xsteps.append(random.uniform(-1, 0))
            else:
                xsteps.append(random.uniform(0, 1))

            numerator += -(xsteps[j] ** 2) * (math.sin(math.radians(a)) ** 2)
            resultant_step += xsteps[j] ** 2

        yStep = -math.sqrt(numerator / ((math.sin(math.radians(a)) ** 2) - 1))
        resultant_step = math.sqrt(resultant_step + yStep ** 2)
        # find factor
        f = resultant / resultant_step
        # calculate steps of the vector for the given direction #start current vector
        x_space = []
        x_space_old = copy.copy(Xbest)
        y_func_old = copy.copy(Fbest)

        for j in range(0, DIMENSIONS):
            xsteps[j] = xsteps[j] * abs(f)
            x_space.append(spidermanPopulation[spiderman_i].position[j] + xsteps[j])
        yStep = yStep * abs(f)
        y_space = Fbest + yStep

        y_func = fitness(x_space)

        if y_space < y_func:
            isUnderneath = True
        else:
            isUnderneath = False

        '''
        below variable is used for counting the number of steps after which we are outside function space
        '''
        outside_steps_count = 0
        for countSteps in range(NUM_OF_STEPS):  # steps begin here
            if min(x_space) < low or max(x_space) > up:
                '''case: outside function space break, no need to explore'''
                break

            '''
            case: check if new y_func is above the function space or not
            '''
            if countSteps > 0 and (isUnderneath == True and y_space >= y_func):
                isUnderneath = False

            '''
            case: if above function and new values greater then old one, return old one and break;
            '''
            if countSteps > 0 and (isUnderneath == False and y_func > y_func_old):
                x_space = copy.copy(x_space_old)
                # y_space = y_space_old
                y_func = y_func_old
                break

            '''
            case : if new y_func is less then the old one, copy the new values to old 
            '''
            if (y_func < y_func_old):
                x_space_old = copy.copy(x_space)
                # y_space_old = y_space
                y_func_old = copy.copy(y_func)

            '''
            case: calculate new  steps
            '''
            for j in range(0, DIMENSIONS):
                x_space[j] += xsteps[j]
            y_space += yStep
            y_func = fitness(x_space)
            outside_steps_count += 1

        '''
        Below code is used for the case: when number of steps are over and we are outside the stepping loop 
        and the final xspace is either otuside the function space or not 
    
        case1: if outside the function space return old values
    
        case2.1: if inside the function space but the final y_fun value is greater than the old value return old
    
        case2.2: if inside the function space but the final y_fun value is less than the old value return new y_fun
        '''
        if ((min(x_space) < low or max(x_space) > up)):  # spiderman case1
            x_space = x_space_old
            y_func = y_func_old

        if (min(x_space) >= low and max(x_space) <= up):  # spiderman case2.1 and 2.2
            if (y_func > y_func_old):
                x_space = x_space_old
                y_func = y_func_old

        for dim in range(DIMENSIONS):
            spidermanPopulation[spiderman_i].position[dim] = x_space[dim]

    for i in range(num_spiderman):
        for dim in range(DIMENSIONS):
            spidermanPopulation[i].position[dim] = builtins.max(spidermanPopulation[i].position[dim], low)
            spidermanPopulation[i].position[j] = min(spidermanPopulation[i].position[dim], up)

        spidermanPopulation[i].fitness = fitness(spidermanPopulation[i].position)

        if(spidermanPopulation[i].fitness < Fbest):
            Xbest = copy.copy(spidermanPopulation[i].position)
            Fbest = spidermanPopulation[i].fitness

    return Xbest, Fbest



while exp < NUM_OF_ITERATIONS:  # number of experiments or number of trials
    # get random initial point

    spidermanPopulation = [spiderman(fitness, DIMENSIONS, low, up, i) for i in range(num_spiderman)]
    Xbest = [0.0 for i in range(DIMENSIONS)]
    Fbest = sys.float_info.max
    for i in range(num_spiderman):
        if spidermanPopulation[i].fitness < Fbest:
            Fbest = spidermanPopulation[i].fitness
            Xbest = copy.copy(spidermanPopulation[i].position)

    start_time = time.process_time()

    for i in range(MAX_ITER):  # trajectories
        Xbest, Fbest = spiderMan(spidermanPopulation, Xbest, Fbest, i)

    print(exp, " - end ", Fbest)
    err = fitness(Xbest)
    print("err - ", err)
    total_time = time.process_time() - start_time

    results.append(Fbest)  # collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp += 1

results_average = sum(results) / len(results)  # get an average
time_average = sum(times) / len(times)

print("After", NUM_OF_ITERATIONS, "iterations of variant tr3 it is found that it takes ", time_average,
      " seconds per iteration and has a average distance of ", results_average, " from the global minimum")
