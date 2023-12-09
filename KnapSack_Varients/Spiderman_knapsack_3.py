import copy
import math
import random

import time
#from NonContinuousFunctions import *
# from NonContinuousRotatedHybridCompositeFunc import *
import KnapSack

###############limits of variables for each function#####################
exp = 30
NUM_OF_ITERATIONS = 40
generateTrailsCSV = True
DIMENSIONS =5 # withozut y axis
# define hyper-parameters

START_RESULTANT = 5  # start step size
END_RESULTANT = 0.00001  # end step size
START_ANGLE =1
END_ANGLE = 89
MAX_ITER = 1410000
NUM_OF_STEPS = 150


fitness = KnapSack.knapsack_objective_fun_without_probablity_1



ITEMS = {}  # weights and values
RANGES = []
CAPACITY = 0  # Knapsack capacity


# create new neighbour from previous xvals and xsteps
def _create_neighbour_(xspace, xsteps, RANGES, low, up):
    xspace_neighbour = copy.copy(xspace)
    for j in range(0, DIMENSIONS):
        if (xspace_neighbour[j]<=RANGES[j]):  # increase
            xspace_neighbour[j] = round(xspace[j] + xsteps[j])
        elif (xspace_neighbour[j] > 0):  # decrease
            xspace_neighbour[j] = round(xspace[j] - xsteps[j])
    #print("calculated xspace_neighbour : ", xspace_neighbour)
    return xspace_neighbour


#############################################

def memoized_refining(low, up, x_space, x_space_old, y_func, y_func_old):
    '''
    Below code is used for the case: when number of steps are over and we are outside the stepping loop
    and the final xspace is either otuside the function space or not

    case1: if outside the function space return old values

    case2.1: if inside the function space but the final y_fun value is greater than the old value return new calculated values

    case2.2: if inside the function space but the final y_fun value is less than the old value return old y_fun
    '''
    if ((min(x_space) < low or max(x_space) > up)):  # spiderman case1
        x_space = x_space_old
        y_func = y_func_old
    if (min(x_space) >= low and max(x_space) <= up):  # spiderman case2.1 and 2.2
        if (y_func > y_func_old):
            x_space = x_space_old
            y_func = y_func_old
    return x_space, y_func



def __spiderman_knapsack__(xvalues, y, i, low, up):
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
    x_space_old = copy.copy(xvalues)
    y_func_old = copy.copy(y)

    for j in range(0, DIMENSIONS):
        xsteps[j] = xsteps[j] * abs(f)

    #create neighbour as per knapsack
    x_space = _create_neighbour_(xvalues, xsteps, RANGES, low, up)
    yStep = yStep * abs(f)

    #should i round this?
    y_space = y + yStep

    y_func = fitness(x_space, CAPACITY, ITEMS, DIMENSIONS)[1]

    if y_space < y_func:
        isUnderneath = True
    else:
        isUnderneath = False

    for countSteps in range(NUM_OF_STEPS):  # steps begin here
        if min(x_space) < low or max(x_space) > up:
            '''case: outside function space break, no need to explore'''
            break

        '''
        case: check if new y_func is above the function space or not
        '''
        if (isUnderneath == True and y_space >= y_func):
            isUnderneath = False

        '''
        case: if above function and new values greater then old one, return old one and break;
               y_func < y_func_old = as per knapsack : if new values are smaller then return the memoized values
        '''
        if  (isUnderneath == False and y_func < y_func_old):
            x_space = copy.copy(x_space_old)
            # y_space = y_space_old
            y_func = y_func_old
            break

        '''
        case : if new y_func is less then the old one, copy the new values to old 
               y_func > y_func_old = as per knapsack: if new y-func greater then update the memoized values 
        '''
        if (y_func > y_func_old):
            x_space_old = copy.copy(x_space)
            # y_space_old = y_space
            y_func_old = copy.copy(y_func)

        '''
        case: calculate new  steps           
        '''
        x_space = _create_neighbour_(x_space,xsteps,RANGES, low, up) #create neighbour as per knapsack
        y_space += yStep
        y_func = fitness(x_space, CAPACITY, ITEMS, DIMENSIONS)[1]

    x_space, y_func = memoized_refining(low, up, x_space, x_space_old, y_func, y_func_old)

    return x_space, y_func



#############################################
# for START_RESULTANT in sr:
# for END_ANGLE in ea:
times = []
results = []

start_time1 = time.process_time()
plot_xvals = []

summ=0
while exp < NUM_OF_ITERATIONS:  # number of experiments or number of trials
    # knapsack ITEMS{Weights, Values}, RANGES, CAPACITY
    #ITEMS, RANGES, CAPACITY = KnapSack.generate_random_items_ranges(DIMENSIONS)
    ITEMS = KnapSack.item_list_6[exp]
    RANGES = KnapSack.range_list_6[exp]
    CAPACITY = KnapSack.CAPACITY[DIMENSIONS]
    #print(CAPACITY)
    # get random initial point
    xvals = []
    xvals = [random.uniform(0, RANGES[i]) for i in range(DIMENSIONS)]
    # print("xvals ", xvals)
    y = fitness(xvals, CAPACITY, ITEMS, DIMENSIONS)[1]
    # print("start xvals ", xvals)
    print("start ", y)
    start_time = time.process_time()

    low = 0
    up = CAPACITY

    for i in range(MAX_ITER):  # 10000000
        xvals, y = __spiderman_knapsack__(xvals, y, i, low, up)
    summ +=y
    print(exp, " - end ", y, "   , xvals : ", xvals)

    total_time = time.process_time() - start_time
    plot_xvals.append(xvals)
    results.append(y)  # collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp += 1

results_average = sum(results) / len(results)  # get an average
time_average = sum(times) / len(times)

print("avg ", (summ/100))
#-----------------remove below code while final submission
success_results_count = 0
for i in results:
    if(i!=-1):
        success_results_count+=1
accuracy = success_results_count/len(results)
avg_time = sum(times)/len(times)
print("Total number of trials ", len(results), " Accuracy ", accuracy*100, " Avg time per trail ", avg_time )

#------------------below code is just to visualze
# visualize_knapsack.visualize_knapsack_implementaion(ITEMS, CAPACITY, DIMENSIONS, plot_xvals, 'Spiderman-knapsack')

#------------------below code is to animate
# animate_visualization_3d(100,ITEMS, CAPACITY, DIMENSIONS, plot_xvals , RANGES, results, "Spiderman-knapsack-animation-4")



###############store results to xls file##############
from xlwt import Workbook

wb = Workbook()

if (generateTrailsCSV):
    sheet1 = wb.add_sheet('file')
    i = 0
    for wr in results:
        sheet1.write(i, 0, wr)
        sheet1.write(i, 1, times[i])
        i += 1

    wb.save('Spiderman_knapsack_6nov_'+str(exp) + '-'+str(MAX_ITER)+'_'+ str(fitness.__name__) + '_' + str(DIMENSIONS + 1) + '.xls')
    print("All time saved")
