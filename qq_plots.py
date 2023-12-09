
from scipy import stats
from os import path
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import probplot

'''
'Spiderman', 'BP', 'SA', 'TA', 'PSO', 'WO', 'GWO'

'''

algorithms = ['Spiderman', 'BP', 'SA', 'TA', 'PSO', 'WO', 'GWO']

#functions = ['quadric', 'rosenbrock', 'step_fun', 'xin_she_yang_n2', 'rastrigin', 'ellipsoid']
functions = ['knapsack_objective_fun_without_probablity_1']
f_minimum = [0, 0, 0, 0, 0, 0]
convergeLimit = [0.0744, 1, 1, 0.430, 1, 0.85]
#
# functions = ['ackley', 'sphere', 'schwefel', 'rastrigin']
# f_minimum = [0, 0, 0, 0]
# convergeLimit = [2.5, 100, 118.43835, 0.9949591]

#
# functions = ['dropwave', 'easom', 'eggholder', 'holdertable', 'langermann', 'shubert']
# f_minimum = [ -1, -1, -959.6407, -19.2085, -4.15580929184779, -186.7309]
# convergeLimit = [ -0.94, -0.1, -936, -18.1, -4.1275, -49]
#


time='Old_Time'
fun_type='NonContinuous'
d=[2,3,4,5,6]
d1=['2','3','4','5', '6']


def qq_plots_for_datasets():

    for a in algorithms:
        for function in functions:
            k = 0
            for i in d:
                name_param = "_" + fun_type + "_" + time + "_" + str(i) + ".png"
                #string = "Server-Results/"+time+"/" + a + "/"+ fun_type+"/" + a  + "_" + function + "_" + str(i) + ".xls"
                string = 'Server-Results/Knapsack_Results/'+a+'_knapsack/random_item/'+a+'_'+function+'_'+str(i)+'.xls'
                if (path.exists(string)):
                    print(string)
                    xls = pd.ExcelFile(string)

                    sheetX = xls.parse(0)
                    data_acc = []
                    data_prec = []

                    #if float(sheetX.columns[0]) < convergeLimit[0]:
                    data_acc.append(1)
                    data_prec.append(float(sheetX.columns[0]))
                    #else:
                     #   data_acc.append(0)
                        #data_prec.append(None)


                    for i in range(0, 99):
                        #if float(sheetX.values[i][0]) < convergeLimit[0]:
                            data_acc.append(1)
                            data_prec.append(float(sheetX.values[i][0]))
                        #else:
                         #   data_acc.append(0)
                            #data_prec.append(None)

                    probplot_data = probplot(data_prec, plot=plt)

                    # Add a reference line for normal distribution
                    a1=a
                    if(a == 'Spiderman'):
                        a1 = 'BSO'

                    # plt.title('Q-Q Plot - '+ a1 + ' - ' + function + ' - ' + d1[k] +'Dimension')
                    plt.title('Q-Q Plot - ' + a1 +  '-kanpsack- ' + d1[k] + 'Dimension')
                    plt.xlabel('Theoretical Quantiles')
                    plt.ylabel('Sample Quantiles')
                    plt.grid(True)

                    #Show the plot

                    #plt.savefig('plotting_img/qq_plots/' + a +'_' + function + name_param, dpi=300)
                    plt.savefig('plotting_img/qq_plots/' + a +'_knapsack_' + d1[k], dpi=300)
                    #plt.close()
                    plt.show()
                    k+=1
                else:
                     print("path does not exists : ", string)


qq_plots_for_datasets()
plt.close()