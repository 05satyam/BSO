import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from datetime import datetime

import NonContinuousFunctions
import visualize_optimization_functions_trajectories_
from functions import *
import time
from NonContinuousFunctions import *
#from NonContinuousRotatedHybridCompositeFunc import *
from datetime import date
###############limits of variables for each function#####################
'''
low=-5.12    #rastrigin
up=5.12     #dropwave
# low=-500  #schwefel
# up=500
# low=-5  #ackley
# up=5
# low=-2  #sphere
# up=2
# low=0  #langermann
# up=10
# low=-10  #easom
# up=10
#low=-512  #eggholder
#up=512
'''

'''
Non COntinuous functons starts 
'''

NUM_OF_ITERATIONS = 1
generateTrailsCSV = True
DIMENSIONS = 9  # without y axis
# define hyper-parameters
###4d working
START_RESULTANT = 10  # start step size
END_RESULTANT = .000001  # end step size
START_ANGLE = 0.5
END_ANGLE = 89
MAX_ITER = 19000
NUM_OF_STEPS = 50000
fitness = rastrigin2
REFINEMENT_PREC = 0.0000001
low = -5.12
up = 5.12
outside_trajectoroies_count = 0

# print([[random.randint(1,10) for _ in range(49)] for _ in range(5)])
#############################################
def iterative_refinement(isUnderneath, y_func, x_space, y_space, xsteps, yStep, cur_round):
    #jump in the middle of the step until crossing point is detected
    while abs(y_space-y_func)>REFINEMENT_PREC and yStep!=0:
        for j in range(0, DIMENSIONS):
            xsteps[j] = xsteps[j]/2
        yStep = yStep/2

        if (isUnderneath==False and y_space>y_func) or (isUnderneath==True and y_space<y_func):
            for j in range(0, DIMENSIONS):
                x_space[j] += xsteps[j]
            y_space += yStep
        else:
            for j in range(0, DIMENSIONS):
                x_space[j] -= xsteps[j]
            y_space -= yStep
         
        y_func = fitness(x_space)
        #if step gets too small, exit because we have a satisfactorily accurate solution
        if abs(yStep)<REFINEMENT_PREC:
            y_space = y_func
            
    return x_space, y_func
#############################################
def BPround(xvalues, y, i):
    #define cooling schedules for resultant and angle
    resultant = START_RESULTANT - i*(START_RESULTANT-END_RESULTANT)/MAX_ITER
    a = START_ANGLE - i*(START_ANGLE-END_ANGLE)/MAX_ITER

    #setting direction randomly #find resultant
    xsteps=[]
    numerator=0
    resultant_step = 0
    for j in range(DIMENSIONS):
        xsteps.append(random.uniform(-1, 1))
        numerator += -(xsteps[j]**2)*(math.sin(math.radians(a))**2)
        resultant_step+=xsteps[j]**2
        
    yStep = -math.sqrt(numerator/((math.sin(math.radians(a))**2) - 1))
    resultant_step = math.sqrt(resultant_step + yStep**2)
    #find factor
    f=resultant/resultant_step
    
    #calculate steps of the vector for the given direction #start current vector
    x_space = []
    for j in range(0, DIMENSIONS):
        xsteps[j] = xsteps[j]*abs(f)
        x_space.append(xvalues[j] + xsteps[j])
    yStep = yStep*abs(f)
    y_space = y + yStep
    
    y_func = fitness(x_space)
    
    if y_space < y_func:
        isUnderneath = True
    else:
        isUnderneath = False
        
    for countSteps in range(NUM_OF_STEPS):#steps begin here
        if min(x_space)<low or max(x_space)>up:
            global outside_trajectoroies_count
            outside_trajectoroies_count += 1
            break
        
        if (isUnderneath==False and y_space < y_func) or (isUnderneath==True and y_space > y_func) or y_space==y_func:####crossing detected implementation
            xvalues, y = iterative_refinement(isUnderneath, y_func, x_space, y_space, xsteps, yStep, i)
            break
        
        for j in range(0, DIMENSIONS):
            x_space[j] += xsteps[j]
        y_space += yStep
        y_func = fitness(x_space)
        
    return xvalues, y
#############################################
# for START_RESULTANT in sr:
#     for END_ANGLE in ea:
times=[]
results=[]
exp=0
start_time1=time.process_time()

plot_xvals = []
plot_xvals_ys = []
count=0
while exp<NUM_OF_ITERATIONS:#number of experiments or number of trials
    #get random initial point
    xvals=[]    
    xvals = [random.uniform(low, up) for i in range(DIMENSIONS)]
    #print("xvals ", xvals)
    y = fitness(xvals)
    print("start ", y)
    start_time=time.process_time()
    plot_xvals.append(xvals)
    plot_xvals_ys.append(y)
    for i in range(MAX_ITER): # number of rounds
        xvals, y = BPround(xvals, y, i)
        plot_xvals.append(xvals)
        plot_xvals_ys.append(y)
        #if(i>MAX_ITER-5):
         #   print('in main method xvals' , xvals)
    if(y< 1):
            
            count +=1
    print(exp , " - end ",y, '  count ', count )
    total_time=time.process_time()-start_time

    results.append(y) #collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp+=1
#visualize_fun_trajec_move.visualize_3d(MAX_ITER, low, up, plot_xvals_ys, plot_xvals, fitness)
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)

now = datetime.now()

end_tym = now.strftime("%H:%M:%S")

#print("time:",time_average,"sec,",results_average, " precision, with",START_RESULTANT,"step and",END_ANGLE," angle end")
print("After",NUM_OF_ITERATIONS,"iterations of variant tr3 it is found that it takes ",time_average," seconds per iteration and has a average distance of ",results_average, " from the global minimum" , " end tym ", end_tym)
#visualize_fun_trajec_move.visualize_3d(MAX_ITER, low, up, plot_xvals_ys, plot_xvals, fitness)
###############store results to xls file##############
import xlwt
from xlwt import Workbook

wb = Workbook()

if(generateTrailsCSV):
    sheet1 = wb.add_sheet('file')
    i=0
    for wr in results:
        sheet1.write(i, 0, wr)
        sheet1.write(i, 1, times[i])
        i+=1

    wb.save('Server-Results/BP_0_1_'  +str(fitness.__name__)+'_'+str(DIMENSIONS+1)+'_2.xls')
    print("All time saved")


