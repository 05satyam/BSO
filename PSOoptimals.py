#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Simple Particle Swarm Optimization (PSO) with Python
#   July, 2016
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division
import random
import math
from functions import *
import time
#--- MAIN ---------------------------------------------------------------------+

class Particle:
    def __init__(self,x0):
        self.position_i=[]          # particle position
        self.velocity_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.err_best_i=-1          # best error individual
        self.err_i=-1               # error individual

        for i in range(0,num_dimensions):
            self.velocity_i.append(random.uniform(-1,1))
            self.position_i.append(x0[i])

    # evaluate current fitness
    def evaluate(self,costFunc):
        self.err_i=costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i

    # update new particle velocity
    def update_velocity(self,pos_best_g, c1, c2):
        w=0.9       # constant inertia weight (how much to weigh the previous velocity)

        for i in range(0,num_dimensions):
            r1=random.random()
            r2=random.random()

            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0,num_dimensions):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]
                
class PSO():
    def __init__(self,costFunc,x0,bounds,num_particles,maxiter, c1, c2):
        global num_dimensions

        num_dimensions=len(x0)
        err_best_g=-1                   # best error for group
        pos_best_g=[]                   # best position for group

        # establish the swarm
        swarm=[]
        for i in range(0,num_particles):
            swarm.append(Particle(x0))

        # begin optimization loop
        i=0
        while i < maxiter:
            #print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0,num_particles):
                swarm[j].evaluate(costFunc)

                # determine if current particle is the best (globally)
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g=list(swarm[j].position_i)
                    err_best_g=float(swarm[j].err_i)

            # cycle through swarm and update velocities and position
            for j in range(0,num_particles):
                swarm[j].update_velocity(pos_best_g, c1, c2)
                swarm[j].update_position(bounds)
            i+=1

        # print final results
        results.append(err_best_g) #collect accuracy and time results of each algorithm run
#         print('FINAL:')
#         print(pos_best_g)
#         print(err_best_g)

if __name__ == "__PSO__":
    main()
#############################################
def range_with_floats(start, stop, step):
    while stop > start:
        yield start
        start += step
#############################################
#--- RUN ----------------------------------------------------------------------+
# low=-5.12    #rastrigin
# up=5.12      #dropwave
# low=-512  #eggholder
# up=512
low=-500  #schwefel
up=500
# low=-10  #easom#holdertable
# up=10    #shubert
# low=-5  #ackley
# up=5
# low=-2  #sphere
# up=2
# low=0  #langermann
# up=10

np = [10, 30, 50, 100]
mi = [15000, 5000, 4000, 1500]
c1s = [.1, .5, 1, 2]

num_of_iter = 10
DIMENSIONS= 29
#langermann: time: 5.16875 sec, -3.804940502927631  precision, with 30  DIMENSIONS 100 particles, 2 c1, 2.5 c2
#eggholder: time: 9.5078125 sec, -17901.418916967566  precision, with 30  DIMENSIONS 50 particles, 1 c1, 1.5 c2
#schwefel: time: 4.740625 sec, 2257.375752134252  precision, with 30  DIMENSIONS 100 particles, 0.1 c1, 1.1 c2,
optimal_precision = 10000000
for npc in range(len(np)):
    for c_1 in c1s:
        for c_2 in range_with_floats(c_1+.5, 3, .5):
            exp=0
            times=[]
            results=[]
            while exp<num_of_iter:
                initial=[]               # initial starting location [x1,x2...]
                bounds=[]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
                for i in range(0, DIMENSIONS):
                    initial.append(random.uniform(low, up))
                    bounds.append([low, up])
                    
                start_time=time.process_time()
                
                PSO(schwefel,initial,bounds,num_particles=np[npc],maxiter=mi[npc], c1=c_1, c2=c_2)
                
                total_time=time.process_time()-start_time
                times.append(total_time)
                exp+=1

            results_average=sum(results)/len(results) #get an average
            time_average=sum(times)/len(times)
            if optimal_precision>results_average:
                print("time:",time_average,"sec,",results_average, " precision, with",DIMENSIONS+1," DIMENSIONS",np[npc],"particles,",c_1,"c1,",c_2,"c2,")
                optimal_precision=results_average