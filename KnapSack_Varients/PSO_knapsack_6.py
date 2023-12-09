import random
import time


# define the unbounded knapsack problem
import KnapSack
#from KnapSack_Varients import visualize_knapsack
#from KnapSack_Varients.visualize_knapsack import animate_visualization_3d

ITEMS = {} #weights and values
RANGES = []
CAPACITY=0

times = []
results = []
plot_xvals = []



dimensions =19  # number of dimensions
# PSO parameters
n_particles = 200  # number of particles
max_iterations =1500 # maximum number of iterations

e = 60
MAX_TRIALS=70

generateTrailsCSV = True
fitness = KnapSack.knapsack_objective_fun_without_probablity_1
file_name='PSO_knapsack_17nov-' + str(e) + str(MAX_TRIALS)+'_' +str(fitness.__name__) + '_' + str(dimensions + 1) + '.xls'


# main function
def __pso_knapsack__():
    # initialize particles and velocities

    particles = [[random.uniform(0, RANGES[i]) for i in range(dimensions)] for n in range(n_particles)]

    velocities = [[0 for _ in range(dimensions)] for _ in range(n_particles)]

    # Initialize particle best position and fitness
    particle_best_positions = particles.copy()
    particle_best_fitnesses = [fitness(particles[i], CAPACITY, ITEMS, dimensions)[1] for i in range(n_particles)]
    #print("particle_best_fitnesses ", particle_best_fitnesses )
    # Initialize swarm best position and fitness value
    best_fitness_idx = particle_best_fitnesses.index(max(particle_best_fitnesses))
    swarm_best_position = particles[best_fitness_idx].copy()
    swarm_best_fitness = max(particle_best_fitnesses)
    #print(velocities)
    #main loop
    for t in range(max_iterations):
        c1 = 1  #cognitive parameter
        c2 = 2  # social parameter
        w = 0.9  # inertia weight
        # update velocities and positions

        for i in range(n_particles):
            r1 = [random.random() for _ in range(dimensions)]
            r2 = [random.random() for _ in range(dimensions)]
           # print(f"Type of velocities[{i}]: {type(velocities[i])}, value: {velocities[i]}")

            velocities[i] = [
                w * velocities[i][j] +
                c1 * r1[j] * (particle_best_positions[i][j] - particles[i][j]) +
                c2 * r2[j] * (swarm_best_position[j] - particles[i][j])
                for j in range(dimensions)
            ]



            #particles[i] = np.round(1.0 / (1.0 + np.exp(-velocities[i])))  # apply sigmoid activation function to velocities
            for d in range(dimensions):
                # Update the new position for each dimension
                particles[i][d] = max(0, min(round(particles[i][d] + velocities[i][d]), RANGES[d]))

        # evaluate fitnesses

            # Evaluate fitnesses
            for i in range(n_particles):
                current_fitness = fitness(particles[i], CAPACITY, ITEMS, dimensions)[1]
                if current_fitness > particle_best_fitnesses[i]:
                    particle_best_positions[i] = particles[i].copy()
                    particle_best_fitnesses[i] = current_fitness
                if current_fitness > swarm_best_fitness:
                    swarm_best_position = particles[i].copy()
                    swarm_best_fitness = current_fitness

    results.append(swarm_best_fitness)
    plot_xvals.append(swarm_best_position)
    #print("Best solution found: ", swarm_best_position)
    print("Best fitness value found: ", swarm_best_fitness)


'''
--------------------PSO KNAPSACK MAIN Functions ENDS-----------------------
'''

start_time = time.process_time()
# Run the PSO-kanpsack annealing algorithm

while e < MAX_TRIALS:
    start_time_per_trial = time.process_time()
    random.seed()

    # knapsack ITEMS{Weights, Values}, RANGES, CAPACITY
    #ITEMS, RANGES, CAPACITY = KnapSack.generate_random_items_ranges(dimensions)
    ITEMS = KnapSack.item_list_20_1[e]
    RANGES = KnapSack.range_list_20[e]
    CAPACITY = KnapSack.CAPACITY[dimensions]

    #calling pso knapsack
    __pso_knapsack__()
    times.append(time.process_time() - start_time_per_trial)
    print("e- ", e)
    e = e + 1

#KnapSack._visualize_(plot_xvals, results, max_iterations, 'PSO-knaspack-1')
success_results_count = 0;
for i in results:
    if(i!=-1):
        success_results_count+=1
accuracy = success_results_count/len(results)
avg_time = sum(times)/len(times)
print("Total number of trials ", len(results), " Accuracy ", accuracy*100, " Avg time per trail ", avg_time )


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


#visualize_knapsack.visualize_knapsack_implementaion(ITEMS, CAPACITY, dimensions, plot_xvals, 'PSO-knapsack')

#animate_visualization_3d(100,ITEMS, CAPACITY, dimensions, plot_xvals , RANGES, results, "PSO-knapsack-animation-1")
