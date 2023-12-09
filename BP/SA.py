import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time

import NonContinuousFunctions
import visualize_optimization_functions_trajectories_
from functions import * 
times=[]
results=[]
A = 10      # rastrigin factor

final_temp = 0.0001 # final temperature
b =  .99974  # reducing factor of temperature
neighbor_distance = 2 # the distance that a possible neighbor can have in x or y dimension
dimensions=2
fitness = NonContinuousFunctions.rosenbrock
num_of_iter=100  #number of experiment iteration

exp=0
up =1 # non continuous rastrigin
low= -1

# low=-5.12    #rastrigin
# up=5.12      #dropwave
# low=-512  #eggholder
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

plot_xvals = []
plot_xvals_ys = []
start_time1=time.process_time()
while exp<num_of_iter:
    start_time=time.process_time()
    T = 10 # starting temperature
    xvals= []
    for i in range(0, dimensions):
        xvals.append(random.uniform(low, up))

#     z = holdertable(xvals)
#     count=0
    z = fitness(xvals)
    print("start", xvals)
    plot_xvals.append(xvals)
    plot_xvals_ys.append(z)
    while T>final_temp:
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

        DE = z - fitness(neighbors)

        if DE > 0:   # if the neighbor is better, accept it
            for i in range(0, dimensions):
                xvals[i] = neighbors[i]
        else:   # if not, accept it with a probability
            if random.uniform(0, 1) < math.exp(DE / T):
                for i in range(0, dimensions):
                    xvals[i] = neighbors[i]

#         z = holdertable(xvals)
        z = fitness(xvals)
        plot_xvals.append(xvals)
        plot_xvals_ys.append(z)
        T=b*T
#         count+=1
#         print("Iteration ",count,": x =",xvals[0]," y =",xvals[1],"z = ",xvals[2]," w =",z)

    print(exp , " yval - ", xvals)
    total_time=time.process_time()-start_time
#     if (total_time>5):
    results.append(z) #collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp+=1

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Simulated Annealing it is found that it takes ",time_average," seconds and to have an accuracy of ",results_average, " from the global minimum")
#visualize_fun_trajec_move.visualize_3d(num_of_iter, low, up, plot_xvals_ys, plot_xvals, fitness)

import xlwt 
from xlwt import Workbook 
         
wb = Workbook() 
          
sheet1 = wb.add_sheet('file')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1

wb.save('Server-Results/SA_2_'+str(fitness.__name__)+'_'+str(dimensions+1)+'.xls')

print("All saved")

