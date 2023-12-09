import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import math
from functions import *
import pandas as pd
import xlrd
from os import path
import xlwt
from xlwt import Workbook

wb = Workbook()
wb2 = Workbook()
sheet1 = wb.add_sheet('times')
sheet2 = wb2.add_sheet('results_MAE')

algorithms = ['Spiderman','BP', 'SA',  'TA', 'PSO', 'GWO','WO']

# algorithms = ['Spiderman']

#-----------------NC-------------------------------
functions = ['step_fun', 'rastrigin', 'ellipsoid', 'rosenbrock', 'quadric', 'xin_she_yang_n2']
funcs = ['step_fun', 'rastrigin', 'ellipsoid', 'rosenbrock', 'quadric', 'xin_she_yang_n2']

f_minimum = [0,0,0,0,0,0]
convergeLimit = [1,1,0.85, 1,0.0744,0.430]


#------------------Conti------------------------------
# #
# functions = ['dropwave', 'easom', 'eggholder', 'holdertable', 'langermann', 'shubert']
# funcs = ['dropwave', 'easom', 'eggholder', 'holdertable', 'langermann', 'shubert']
# f_minimum = [ -1, -1, -959.6407, -19.2085, -4.15580929184779, -186.7309]
# convergeLimit = [ -0.94, -0.1, -936, -18.1, -4.1275, -49]

# functions = ['ackley', 'sphere', 'schwefel', 'rastrigin']
# funcs = ['ackley',  'sphere', 'schwefel', 'rastrigin']
# f_minimum = [0, 0, 0, 0]
# convergeLimit = [2.5, 100, 118.43835, 0.9949591]

# functions = ['xin_she_yang_n2']
# funcs = ['xin_she_yang_n2']
# f_minimum = [0]
# convergeLimit = [0.430]

#---------          for 3d multiple times           -----
# functions = ['ackley', 'sphere', 'schwefel', 'rastrigin', 'dropwave', 'easom', 'eggholder', 'holdertable', 'langermann', 'shubert']
# funcs = ['ackley', 'sphere', 'schwefel', 'rastrigin', 'dropwave', 'easom', 'eggholder', 'holdertable', 'langermann', 'shubert']
# f_minimum = [ 0, 0, 0, 0, -1, -1, -959.6407, -19.2085, -4.15580929184779, -186.7309]
# convergeLimit = [2.5, 100, 118.43835, 0.9949591,  -0.94, -0.1, -936, -18.1, -4.1275, -49]
#
# functions = ['step_fun', 'rastrigin', 'ellipsoid', 'rosenbrock', 'quadric', 'xin_she_yang_n2']
# funcs = ['step_fun', 'rastrigin', 'ellipsoid', 'rosenbrock', 'quadric', 'xin_she_yang_n2']
#
# f_minimum = [0,0,0,0,0,0]
# convergeLimit = [1,1,0.85, 1,0.0744,0.430]
#
'''
Server-Results/Old_Time/
Server-Results/3D/
Server-Results/3D_1plot/
'''
base_path="Server-Results/Old_Time/"
fun_type="NonContinuous"

for a in algorithms:
    k = 0
    l = 0
    for f_name in functions:
        d=1
        for j in range(2,7):
            string = base_path + a+"/"+fun_type+"/" + a + "_" + f_name + "_" + str(j) + ".xls"
            # string = "Server-Results/3D/" + a + "/NonContinuous/" + a  + "_0_1_" + f_name + "_" + str(3) + ".xls"
            # string = "Server-Results/New_Time/" + a + "/NonContinuous/" + a+"_" + f_name + "_" + str(j) + "_" + str(d)+ ".xls"

            if (path.exists(string)):
                    print(string)
                    xls = pd.ExcelFile(string)
            else:
                string = base_path + a+"/"+fun_type+"/" + a + "_" + f_name + "_" + str(j) + ".xls"
                # string = "Server-Results/3D/"+ a+"/NonContinuous/" + a + "_0_1_" + f_name + "_" + str(3) + ".xls"
                # string = "Server-Results/3D_1plot/" + a + "/NonContinuous/" + a + f_name + "_" + str(3) + "_" + str(d) + ".xls"
                if (path.exists(string)):
                    # print(string)
                    xls = pd.ExcelFile(string)
                else:
                    continue

            sheetX = xls.parse(0)

            data = []
            data.append(float(sheetX.columns[0]))
            for i in range(0, 99):
                data.append(float(sheetX.values[i][0]))

            percentage = 0
            resss = 0
            for i in data:
                if ((i < convergeLimit[k])):
                    percentage += 1

                if ((i < convergeLimit[k])):
                    resss += abs(f_minimum[k] - i)  # MAE

            if percentage == 0:
                results_average = "null"
            else:
                results_average = resss / 100
            if j == 2:
                if a == algorithms[0]:
                    sheet1.write(l, 0, funcs[k])

                    sheet2.write(l, 0, funcs[k])
                    l += 1

                    sheet1.write(l, 0, algorithms[0])
                    sheet1.write(l, 1, algorithms[1])
                    sheet1.write(l, 2, algorithms[2])
                    sheet1.write(l, 3, algorithms[3])
                    sheet1.write(l, 4, algorithms[4])
                    sheet1.write(l, 5, algorithms[5])
                    sheet1.write(l, 6, algorithms[6])

                    sheet2.write(l, 0, algorithms[0])
                    sheet2.write(l, 1, algorithms[1])
                    sheet2.write(l, 2, algorithms[2])
                    sheet2.write(l, 3, algorithms[3])
                    sheet2.write(l, 4, algorithms[4])
                    sheet2.write(l, 5, algorithms[5])
                    sheet2.write(l, 6, algorithms[6])

                    l += 1
                else:
                    l += 2

            if a == algorithms[0]:
                sheet1.write(l, 0, percentage)

                sheet2.write(l, 0, results_average,xlwt.easyxf(num_format_str='0.0'))
            elif a == algorithms[1]:
                sheet1.write(l, 1, percentage)

                sheet2.write(l, 1, results_average,xlwt.easyxf(num_format_str='0.0'))
            elif a == algorithms[2]:
                sheet1.write(l, 2, percentage)

                sheet2.write(l, 2, results_average,xlwt.easyxf(num_format_str='0.0'))
            elif a == algorithms[3]:
                sheet1.write(l, 3, percentage)

                sheet2.write(l, 3, results_average,xlwt.easyxf(num_format_str='0.0'))
            elif a == algorithms[4]:
                sheet1.write(l, 4, percentage)

                sheet2.write(l, 4, results_average,xlwt.easyxf(num_format_str='0.0'))
            elif a == algorithms[5]:
                sheet1.write(l, 5, percentage)

                sheet2.write(l, 5, results_average,xlwt.easyxf(num_format_str='0.0'))
            else:
                sheet1.write(l, 6, percentage)

                sheet2.write(l, 6, results_average,xlwt.easyxf(num_format_str='0.0'))

            wb.save('Server-Results/Convergence_Results/functions/Old_Time/' + 'NonContinuous_Convergence.xls')
            wb2.save('Server-Results/Convergence_Results/functions/Old_Time/' + 'NonContinuous_Convergence_MAE.xls')

            # wb.save('Server-Results/Convergence_Results/functions/New_Time/' +functions[k]+ 'NonContinuous_Convergence.xls')
            # wb2.save('Server-Results/Convergence_Results/functions/New_Time/' +functions[k]+ 'NonContinuous_Convergence_MAE.xls')

            # wb.save( 'Server-Results/Convergence_Results/3D/NonContinuous/' + functions[k] + '_3d_NonContinuous_Convergence.xls')
            # wb2.save('Server-Results/Convergence_Results/3D/NonContinuous/' + functions[k] + '_3d_NonContinuous_Convergence_MAE.xls')

            print("Algorithm " + a + " Function " + funcs[k] + " for " + str(j) + " has " + str(percentage) + "%")
            l += 1
            d += 1
        k += 1




'''
for functions which have only 3d results
'Server-Results/Convergence_Results/functions/New_Time/' + 'Continuous3d_Convergence.xls'
'Server-Results/Convergence_Results/functions/New_Time/' + 'Continuous3d_Convergence_MAE.xls'


for 3d results multiple times
'Server-Results/Convergence_Results/3D/1/' + '3d_1_Continuous_Convergence_MAE.xls'
'''
