'''
this script is used specifically for plotting the functions and see how the functions graph looks like

'''
import matplotlib.pyplot as plt
import numpy as np

import NonContinuousFunctions

#
import functions

fig = plt.figure(figsize=plt.figaspect(0.5))
# ax = fig.add_subplot(1, 1, 1, projection='3d')

'''
call below method to plot 2d curve
'''

def plot2d_py(func, low, up, nspace, responseLabel):

    ax = fig.gca()
    X = np.linspace(low, up, nspace)
    print(X)
    XY = np.array([X])
    Z = np.apply_along_axis(func, 0, XY)
    #Z = func(XY)
    print("Z  :   ",Z)
    # print("len Z ", len(Z))
    plt.plot(X, Z.T)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    fig.savefig('plotting_img/final_plot_2D/' + func.__name__ + '.svg', format='svg', dpi=1200)
    plt.show()

'''
call below method to plot 3d curve
'''
def plot3d_py(func, low, up, nspace, responseLabel):
    ax = fig.gca(projection='3d')
    vectorizeFunc = np.vectorize(func)

    X = np.linspace(low, up, nspace)
    Y = np.linspace(low,up,nspace)
    X, Y = np.meshgrid(X, Y)
    XY = np.array([X, Y])
    Z = np.apply_along_axis(func, 0, XY)
    my_cmap = plt.get_cmap('inferno')
    ax.plot_surface(X, Y, Z,cmap=my_cmap,
                        alpha = 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax.set_zlabel(responseLabel)
    ax.xaxis.set_tick_params(labelsize=8)
    ax.yaxis.set_tick_params(labelsize=8)
    ax.zaxis.set_tick_params(labelsize=8)


    #plt.savefig('plotting_img/final_plot_3D/' + func.__name__+'.png')
    fig.savefig('plotting_img/final_plot_3D/' + func.__name__+'.svg', format='svg', dpi=1200)
    plt.show()

#func : run this for ploting non continuous rastrigin

#plot3d(NonContinuousFunctions.continous_scaffer_fun, -100, 100, 50, 'non-continus-response')

#plot3d_py(NonContinuousFunctions.ellipsoid, -2,2, 100, 'response')



def convert_svg_pdf():
    import cairosvg

    def svg_to_pdf(input_svg, output_pdf):
        cairosvg.svg2pdf(url=input_svg, write_to=output_pdf)

    # Example usage:
    input_svg_path = 'plotting_img/final_plot_3D/xin_she_yang_n2.svg'
    output_pdf_path = 'plotting_img/final_plot_3D/xin_she_yang_n2.pdf'

    svg_to_pdf(input_svg_path, output_pdf_path)
convert_svg_pdf()
