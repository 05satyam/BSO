import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time

import NonContinuousFunctions
from functions import *
times=[]
results=[]
A = 10      # rastrigin factor

init_T =  1  #initial threshold
rounds = 68000     # number of parts that the threshold sequence will contain
neighbor_distance = 900 # the distance that a possible neighbor can have in x or y dimension
T = np.linspace(init_T, 0, rounds)  #all threshold values for the TA
dimensions= 2  #only the variables of the objective function
fitness = eggholder
low=-512
up=512

num_of_iter= 100 #number of experiment iterations

# low=-5.12    #rastrigin
# up=5.12      #dropwave
# low=1-512  #eggholder
# up=512
# low=-500  #schwefel
# up=500
# low=-10  #easom#holdertable
# up=10    #shubert
# low=-5  #ackley
# up=5
# low=-2  #sphere
# up=2
# low=0  #langermann
# up=10




exp=0
count=0
while exp<num_of_iter:
    start_single = time.process_time()
    xvals=[]
    for i in range(0, dimensions):
        xvals.append(random.uniform(low, up))

    z=fitness(xvals)
    
    start_time=time.process_time()
    
    for t in T:
        neighbors=[]
        for i in xvals:
            if i - neighbor_distance > low: #setting lower limits
                lower = i - neighbor_distance
            else:
                lower = low
            
            if i + neighbor_distance < up: #setting upper limits
                upper = i + neighbor_distance
            else:
                upper = up
            neighbors.append(random.uniform(lower, upper))
             
        DE = z-fitness(neighbors)
        
        if DE > -t:    # if the new solution is better, accept it
            for i in range(0, dimensions):
                xvals[i] = neighbors[i]

        z=fitness(xvals)
    if(z< -936):#-4.12757):
            count +=1
    print(exp , "  yvals- ", z, ' count : ', count)
    total_time=time.process_time()-start_time
#     if (total_time<5):
    results.append(z) #collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp+=1
#     print("Time:",total_time,"Precision:",z)

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Threshold Accepting it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")

import xlwt 
from xlwt import Workbook 
    
wb = Workbook() 
     
sheet1 = wb.add_sheet('file')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1

#<<<<<<< HEAD
wb.save('Server-Results/TA_0_5_'+str(fitness.__name__)+'_'+str(dimensions+1)+'2.xls')
#=======
#wb.save('Server-Results/TA_0_1_'+str(fitness.__name__)+'_'+str(dimensions+1)+'.xls')
#>>>>>>> e251f3d7ec982c4ef6bf3147911e5873ffe9e92a

print("All saved")
