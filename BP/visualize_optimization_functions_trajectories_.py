'''
This code helps in ploting functions plots along with their trjectories in 2d and 3d for any algorithm and any functions

'''

from matplotlib import animation

import numpy as np
import matplotlib.pyplot as plt

'''
2d trajectory plot- animation code
'''
def animate2D_func(i, data, yvals ,ax, up, low, plt, func):
    ax.clear()  # Clears the figure to update the line, point,

    X = np.linspace(low,up, 1000)
    XY = np.array([X])
    #Z = func(XY) #when function created using numpy lib

    Z = np.apply_along_axis(func, 0, XY) #when function created using math library

    plt.plot(X, Z)
    # Updating Trajectory Line
    plt.plot(data[0,:i],yvals[:i], c='blue')

    # Updating Point Location
    plt.scatter(data[0,:i],  yvals[0:i],  c='blue',linewidth=0.01)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    print(" frame num: ", i)


'''
2d:

main method which will be used in algorithm to plot the trajectory 
'''
def visualize_2d(MAX_ITER, low, up, plot_xvals_ys, plot_xvals, func):
    # Create a plot of the function
    fig = plt.figure()
    ax = fig.gca()


    data = np.array(list(plot_xvals)).T
    yvals1=np.array([plot_xvals_ys]).T

    print(data.shape)
    print(yvals1.shape)
    ani = animation.FuncAnimation(fig, animate2D_func, fargs=(data, yvals1, ax, up, low, plt, func), interval=200,
                                  frames=MAX_ITER,repeat=False)


    writergif = animation.PillowWriter(fps=MAX_ITER)
    ani.save('plotting_img/Spiderman_3_' + func.__name__ + '.gif', writer=writergif)
    #plt.show()

    # Display the plot



'''
---------------------------------animation 3d--------------------------------------
3d trajectory plot- animation code
'''

def animate3D_func(i, data, yvals ,ax, up, low,plt, func):
    ax.clear()  # Clears the figure to update the line, point,
    xvals = np.linspace(low, up, 100)
    X, Y = np.meshgrid(xvals, xvals)
    #Z = func(np.array([X, Y]))
    Z = np.apply_along_axis(func, 0, np.array([X, Y]))
    my_cmap = plt.get_cmap('inferno')
    ax.plot_surface(X, Y, Z, cmap=my_cmap,
                    alpha=.3)

    # # Updating Trajectory Line
    print(yvals[0,:i])
    ax.plot3D(data[0,:i], data[1,:i], yvals[0,:i], c='blue')
    # Updating Point Location
    ax.scatter(data[0,:i], data[1,:i], yvals[0,0:i], c='red',linewidth=0.5)
    # Adding Constant Origin
    # ax.plot3D(data[0, 0:1], data[0, 1:2], yvals[0,0:1],
    #            c='black', marker='o')

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('y')
    print(" frame num: ", i)


'''
3d:
main method which will be used in algorithm to plot the trajectory 
'''
def visualize_3d(MAX_ITER, low, up, plot_xvals_ys, plot_xvals,func):

    data = np.array(list(plot_xvals)).T
    yvals1 = np.array([plot_xvals_ys])
    print(data.shape)
    print(yvals1.shape)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # X = np.linspace(low, up, 1000)
    # Y = np.linspace((-1) * up, up, 1000)
    # XY = np.array([X, Y])

    # Z = np.array([np.apply_along_axis(func, 0, XY)])


    ani = animation.FuncAnimation(fig, animate3D_func, fargs=(data, yvals1, ax, up, low, plt,func), interval=200, frames=MAX_ITER,
                                  repeat=False)
    plt.show()
    writergif = animation.PillowWriter(fps=50)
    ani.save('plotting_img/Spiderman_c1_' + func.__name__ + '_01.gif', writer=writergif)

