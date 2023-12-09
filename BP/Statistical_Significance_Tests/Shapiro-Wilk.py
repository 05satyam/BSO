from scipy import stats
from os import path
import pandas as pd

'''
statistical significance tests names to be used: shapiro, 

algorithms name to be used = 
        ['BP', 'Spiderman', 'TA', 'SA', 'PSO','WO', 'GWO']
functions_cnt names to be used = 
        [ 'ackley','rastrigin,  'schwefel','sphere', 'dropwave','easom', 'eggholder', 'holdertable','langermann', 'shubert']
functions_nc names to be used = 
        [ 'ellipsoid', 'quadric','rastrigin', 'rosenbrock', 'step_fun', 'xin_she_yang_n2']
'''
algorithms = ['BP', 'Spiderman', 'TA', 'SA', 'PSO','WO', 'GWO']
functions = ['quadric', 'rosenbrock', 'step_fun', 'xin_she_yang_n2', 'rastrigin', 'ellipsoid']
funcs = ['quadric', 'rosenbrock', 'step_fun', 'xin_she_yang_n2', 'rastrigin', 'ellipsoid']
f_minimum = [0, 0, 0, 0, 0, 0]
convergeLimit = [0.0744, 1, 1, 0.430, 1, 0.85]

import matplotlib.pyplot as plt
from scipy.stats import probplot
def statistical_sig_test():
    for a in algorithms:
        print('-------------------Shapiro-Wilk TEST STARTS for algorithm  - '+ a + '----------------------' )
        for k in range(0, len(functions)):
            for d in range(2, 7): #dimension from 2-6
                #string = "../Server-Results/New_Time/" + a + "/NonContinuous/" + a  + "_" + functions[k] + "_" + str(d) + ".xls"
                string = "../Server-Results/Knapsack_Results/" + a + "_knapsack/29oct/" + a + "_" + funcs[
                    k] + "_" + str(
                    d) + ".xls"

                if (path.exists(string)):
                    print(string)
                    xls = pd.ExcelFile(string)

                    sheetX = xls.parse(0)
                    data_acc = []
                    data_prec = []

                    if float(sheetX.columns[0]) < convergeLimit[k]:
                        data_acc.append(1)
                        data_prec.append(float(sheetX.columns[0]))
                    else:
                        data_acc.append(0)
                        data_prec.append(None)


                    for i in range(0, 99):
                        if float(sheetX.values[i][0]) < convergeLimit[k]:
                            data_acc.append(1)
                            data_prec.append(float(sheetX.values[i][0]))
                        else:
                            data_acc.append(0)
                            data_prec.append(None)

                    # plt.hist(data_prec, bins=10, edgecolor='black')
                    # # Add labels and title
                    # plt.xlabel('Value')
                    # plt.ylabel('Frequency')
                    # plt.title('Histogram of Sample Data')

                    # probplot_data = probplot(data_prec, plot=plt)
                    #
                    # # Add a reference line for normal distribution
                    # plt.title('Q-Q Plot')
                    # plt.xlabel('Theoretical Quantiles')
                    # plt.ylabel('Sample Quantiles')
                    # plt.grid(True)

                    # Show the plot
                    # plt.show()
                    # Perform Shapiro-Wilk test
                    #statistic_acc, p_value_acc = stats.shapiro(data_acc)
                    statistic_prec, p_value_prec = stats.shapiro(data_prec)
                    # print('Shapiro-Wilk test results for ACCURACY')
                    # print("p-value:", p_value_acc)
                    # print(d, "-D and "+ f"Test Statistic: {statistic_acc:.4f}")

                    print('Shapiro-Wilk test results for PRECISION')
                    print("p-value:", p_value_prec)
                    print(d, "-D and "+ f"Test Statistic: {statistic_prec:.4f}")


                else:
                    print("path does not exists : ", string)

            print('         --------Shapiro-Wilk test ENDS for function  : '+ functions[k] + '--------')

        print('--------------------------ENDS -  Algorithm  - '+ a + '-----------------------')

statistical_sig_test()