import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
import time

###############limits of variables for each function#####################
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
# low=-512  #eggholder
# up=512

NUM_OF_ITERATIONS=10
DIMENSIONS = 29  #without y axis
#define hyper-parameters
START_RESULTANT = -2 # start step size
END_RESULTANT = -.0001   # end step size
START_ANGLE = 40
END_ANGLE = 70
MAX_ITER = 5000
NUM_OF_STEPS = 30
REFINEMENT_PREC = 0.000001
NUM_BALLS = 30
ACC_PER = .8

fitness = rastrigin

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
            break
        
        if (isUnderneath==False and y_space<y_func) or (isUnderneath==True and y_space>y_func) or y_space==y_func:####crossing detected implementation
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
accurate=0
while exp<NUM_OF_ITERATIONS:#number of experiments
    #get random initial point
    pop = []
    for p in range(NUM_BALLS):
        pop.append([])
        pop[p].append([random.uniform(low, up) for i in range(DIMENSIONS)])
        pop[p].append(fitness(pop[p][0]))
#     print("start ", y)
    start_time=time.process_time()

    for i in range(MAX_ITER):
        for p in range(NUM_BALLS):
            pop[p][0], pop[p][1] = BPround(pop[p][0], pop[p][1], i)
        
        if i%1==0:
            pop.sort(key=lambda row: (row[1]), reverse=True)
            for p in range(int(NUM_BALLS*(1-ACC_PER))):
                pop[p][0]=pop[29][0]
                pop[p][1]=pop[29][1]
        
    print("end ",pop[29][1])#,"x:",pop[best_p][0])
    
    total_time=time.process_time()-start_time

#     if y<0.99:
#         accurate+=1
    results.append(pop[29][1]) #collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp+=1
#     print("Time:",total_time,"Precision:",y)
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("time:",time_average,"sec,",results_average, " precision, with",START_RESULTANT,"step and",END_ANGLE," angle end")
# print("accuracy:",accurate)
# print("After",NUM_OF_ITERATIONS,"iterations of variant tr3 it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")
###############store results to xls file##############
import xlwt 
from xlwt import Workbook 

wb = Workbook() 

sheet1 = wb.add_sheet('file')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1

wb.save('..\Results\\variantTR4_'+str(fitness.__name__)+'_'+str(DIMENSIONS+1)+'_secs.xls')
print("All saved")