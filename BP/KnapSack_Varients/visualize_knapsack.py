
'''
-------------
'''
from matplotlib import animation

import matplotlib.pyplot as plt
import numpy as np
import KnapSack
from mpl_toolkits.mplot3d import Axes3D


def plot3dScatter(solution_points, final_cost):
    # Create a 3D scatter plot of the points and their values
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(solution_points[:, 0], solution_points[:, 1], final_cost[:], c=final_cost, cmap='cool')
    ax.set_xlabel('Item 1')
    ax.set_ylabel('Item 2')
    ax.set_zlabel('cost')
    plt.title('Knapsack Objective Function')
    plt.show()

'''
-------------------------------- plot 3d fitness and display trajectories begin -------------------
'''
def plot3d(solution_points, final_cost, xBestSolution, trajectory_z, algorithmName):
    # Create a 3D plot of the objective function
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(solution_points[:, 0], solution_points[:, 1], final_cost[:], cmap='viridis', alpha=0.7)

    ax.plot(xBestSolution[:,0],xBestSolution[:,1], trajectory_z, 'o-', label='Trajectory')
    # Add labels and title
    ax.legend()
    ax.set_xlabel('Item 1')
    ax.set_ylabel('Item 2')
    ax.set_zlabel('cost')
    plt.title('Knapsack Objective Function')

    plt.savefig(algorithmName + '.png')
    # Show the plot
    plt.show()

# Generate a set of random points in the search space

# Evaluate the knapsack function at each point - called from each alpgorithm
def visualize_knapsack_implementaion(ITEMS, CAPACITY, dimension, xBestSolution, ranges,results, algorithmName):
    best_solution, bst_solun_trajectory_z, plotting_points, plotting_value = plotting_helper_fun(CAPACITY, ITEMS, dimension, xBestSolution, ranges, results)

    #plot3dScatter(solution_points, value)
    plot3d(plotting_points, plotting_value, best_solution, bst_solun_trajectory_z, algorithmName)

'''
-------------------------------- plot 3d fitness and display trajectories ENDS -------------------
'''


'''
------------------------animate the trajectories code : begins----------------
'''
def animate3D_func(i, trajectory_z ,best_solution,ax,plt,X,Y):
    ax.clear()  # Clears the figure to update the line, point,

    my_cmap = plt.get_cmap('jet')
    trajectory_z_1,y_temp = np.meshgrid(trajectory_z, trajectory_z)
    trajectory_z_1=trajectory_z_1.reshape(X.shape)
    ax.plot_surface(X,Y, trajectory_z_1, cmap=my_cmap, alpha=0.1)

    ax.plot3D(best_solution[:i, 0], best_solution[:i, 1], trajectory_z[:i], c='blue')
    # Updating Point Location
    ax.scatter(best_solution[:i,0], best_solution[:i,1], trajectory_z[0:i], c='blue',linewidth=0.2)


    ax.set_xlabel('x - (0-CAPACITY of knapsack)')
    ax.set_ylabel('y - (0-CAPACITY of knapsack)')
    ax.set_zlabel('z - total value')


def animate_visualization_3d(MAX_ITER, ITEMS, CAPACITY, dimension, xBestSolution, ranges,results, algorithmName):

    best_solution,X,Y = plotting_helper_fun(CAPACITY, ITEMS, dimension, xBestSolution, ranges, results)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ani = animation.FuncAnimation(fig, animate3D_func, fargs=(results ,best_solution,ax, plt,X,Y), interval=400, frames=MAX_ITER,
                                  repeat=False)
    plt.show()
    writergif = animation.PillowWriter(fps=MAX_ITER)
    ani.save(algorithmName + '.gif', writer=writergif)



'''
------------------------animate the trajectories code : ENDS----------------
'''


#common method used as helper for both type of plotting
def plotting_helper_fun(CAPACITY, ITEMS, dimension, xBestSolution, ranges, results):
    '''
    ----unused code----
    :param CAPACITY: capacity of knspaack
    :param ITEMS: items of knapsack
    :param dimension: total number of dimensions
    :param xBestSolution: best xvals solution found after running the algorithms
    :param ranges: ranges for knapsack for each dimension
    :param results: final result for each trial as per xBestSolution
    :return:
    '''
    # n_plotting_points = 2000
    # plotting_points = np.random.randint(0, CAPACITY, size=(n_plotting_points, dimension))
    # plotting_value = np.zeros(n_plotting_points)

    # for i in range(n_plotting_points):
    #     plotting_value[i] = KnapSack.select_knapsack_items_unbounded(plotting_points[i], CAPACITY, ITEMS, dimension, copy.copy(ranges))[1]

    # print("len of , ", len(xBestSolution))
    '''
            -------------
    '''
    best_solution = np.random.randint(0, CAPACITY, size=(len(xBestSolution), dimension))
    X=[]
    Y=[]

    for i in range(len(xBestSolution)):
        for j in range(dimension):
            best_solution[i][j]= xBestSolution[i][j]

    for i in range(len(xBestSolution)):
        X.append(xBestSolution[i][0])
        Y.append(xBestSolution[i][1])


    X1,Y1=np.meshgrid(X,Y)

    # bst_solun_trajectory_z = np.zeros(len(xBestSolution))
    # for i in range(len(best_solution)):
    #     bst_solun_trajectory_z[i] = results[i] #KnapSack.select_knapsack_items_unbounded([best_solution[i][0], best_solution[i][1]], CAPACITY, ITEMS, dimension, copy.copy(ranges))[1]

    return best_solution,  X1, Y1




# Define the parameters of the knapsack function
dimension = 2  # Number of items
if __name__ == '__main__':
    ITEMS, RANGES, CAPACITY = KnapSack.generate_random_items_ranges(2)
    xBestSolution = np.random.randint(0, CAPACITY, size=(100, dimension))
    animate_visualization_3d(1000,ITEMS, CAPACITY, dimension, xBestSolution , "test-animation")
