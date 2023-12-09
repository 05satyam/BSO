import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
import time

###############limits of variables for each function#####################
# low=-5.12    #rastrigin
# up=5.12      #dropwave
# low=-500  #schwefel
# up=500
low=-5  #ackley
up=5    #styblinskiTang
# low=-2   #sphere
# up=2
# low=0  #langermann
# up=10
# low=-10  #easom
# up=10
# low=-512  #eggholder
# up=512
# low=-100   #griewank
# up=100     #sineEnvelope

NUM_OF_ITERATIONS=10
dims = [29]  #without y axis
#define hyper-parameters
sr = [-1, -5, -10, -20, -50] # start step size
END_RESULTANT = -.0001   # end step size
# sa = [.1, 1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 89]#78
# sa = [.01, .1, 1, 5, 20, 50, 70, 89]
sa = [.01, .05, .1, 1, 2, 5]
MAX_ITER = 500
ns = [15, 25]
fitness = styblinskiTang
REFINEMENT_PREC = 0.000001

############## 30D #########################
#rastrigin: time: 5.9078125 sec, 71.28865056559243  precision, with -2 step, 5 angle start and 40  angle end
#ackley: time: 4.803125 sec, 0.021923881220898257  precision, with -0.75 step, 1 angle start and 2  angle end
#schwefel: time: 5.6625 sec, 3507.533953155471  precision, with -75 step, 0.1 angle start and 2  angle end
#sphere: 
#langermann time: 6.7640625 sec, -4.895038278024835  precision, with -0.5 step, 1 angle start and 2.0  angle end
#griewank: time: 3.2015625 sec, 0.2948670376918241  precision, with -3 step, 0.05 angle start,  0.1  angle end and 100 steps
#sineEnvelope: time: 4.028125 sec, 14.015646281788111  precision, with -0.5 step, 0.01 angle start,  0.1  angle end and 50 steps
#eggholder: time: 2.4171875 sec, -13223.805969224486  precision, with 30  dimensions -50 step, 0.1 angle start,  50  angle end, 80 steps
#styblinskiTang:
#############################################
def iterative_refinement(isUnderneath, y_func, x_space, y_space, xsteps, yStep, cur_round, DIMENSIONS):
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
def BPround(xvalues, y, i, START_RESULTANT, START_ANGLE, END_ANGLE, NUM_OF_STEPS, DIMENSIONS):
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
            break
        
        if (isUnderneath==False and y_space<y_func) or (isUnderneath==True and y_space>y_func) or y_space==y_func:####crossing detected implementation
            xvalues, y = iterative_refinement(isUnderneath, y_func, x_space, y_space, xsteps, yStep, i, DIMENSIONS)
            break
        
        for j in range(0, DIMENSIONS):
            x_space[j] += xsteps[j]
        y_space += yStep
        y_func = fitness(x_space)
        
    return xvalues, y
#############################################
def range_with_floats(start, stop, step):
    while stop > start:
        yield start
        start += step
#############################################
optimal_precision = 10000000
for DIMENSIONS in dims:
    for NUM_OF_STEPS in ns:
        for START_RESULTANT in sr:
            for sac in range(len(sa)-1):
                START_ANGLE=sa[sac]
                for eac in range(sac+1, len(sa)):
                    END_ANGLE=sa[eac]
                    times=[]
                    results=[]
                    exp=0
                    while exp<NUM_OF_ITERATIONS:#number of experiments
                        #get random initial point
                        xvals=[]    
                        xvals = [random.uniform(low, up) for i in range(DIMENSIONS)]
                        y = fitness(xvals)
                        
                        start_time=time.process_time()
                    
                        for i in range(MAX_ITER):
                            xvals, y = BPround(xvals, y, i, START_RESULTANT, START_ANGLE, END_ANGLE, NUM_OF_STEPS, DIMENSIONS)
                    
                        
                        total_time=time.process_time()-start_time
                        
                        results.append(y) #collect accuracy and time results of each algorithm run
                        times.append(total_time)
                        exp+=1
        
                    results_average=sum(results)/len(results) #get an average
                    time_average=sum(times)/len(times)
                    if optimal_precision>results_average:
                        print("time:",time_average,"sec,",results_average, " precision, with",DIMENSIONS+1," dimensions",START_RESULTANT,"step,",START_ANGLE,"angle start, ",END_ANGLE," angle end,",NUM_OF_STEPS,"steps")
                        optimal_precision=results_average