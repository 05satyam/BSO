'''

-This script is used to generate MAE graph comparison between different algorithms.
-It is implemented to work for multiple dimensions
-Give path to the convergence file and run the script to make comparison
- As of now it works for BP, FSmO{foggy-spiderman}, SA, TA, PSO, GWO, WO

'''

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
import matplotlib.patches as mpatches

'''
funcs is an array which can have multiple functions at a time 
But it is suggested to run for one function at a time
'''
funcs = ['ellipsoid'] #multi-D

#put path of convergence excel sheet
# excel_path = "Server-Results/Convergence_Results/3D/Continuous/"+funcs[0]\
#          +"_3d_Continuous_Convergence_MAE.xls"

excel_path = ""
xls = pd.ExcelFile(excel_path)
lenOfExcel = 6 #number of lines in converge excel sheet
sheetX = xls.parse(0)

'''
Below are the arrays for each algorithm to compare results
if you add a new algorithm add array for that new algorithm
'''
BSO_res = []
BSO_res.append(sheetX.columns[0])
BP_res = []
BP_res.append(sheetX.columns[0])
SA_res = []
SA_res.append(sheetX.columns[0])
TA_res = []
TA_res.append(sheetX.columns[0])
PSO_res = []
PSO_res.append(sheetX.columns[0])
GWO_res = []
GWO_res.append(sheetX.columns[0])
WO_res = []
WO_res.append(sheetX.columns[0])

for i in range(0,lenOfExcel):
    BSO_res.append(sheetX.values[i][0])
    BP_res.append(sheetX.values[i][1])
    SA_res.append(sheetX.values[i][2])
    TA_res.append(sheetX.values[i][3])
    PSO_res.append(sheetX.values[i][4])
    GWO_res.append(sheetX.values[i][5])
    WO_res.append(sheetX.values[i][6])
print(BSO_res)
X = np.arange(5)
for f in funcs:
    '''
          hold data for plotting for each algorithm so if again you add new algorithm make another result array 
        '''
    results0=[]
    results1=[]
    results2=[]
    results3=[]
    results4=[]
    results5=[]
    results6=[]
    i=0
    while i<=lenOfExcel:
        if not BP_res[i] in funcs:
            if isinstance(BP_res[i], float) or isinstance(BP_res[i], int):
                results0.append(BSO_res[i])
                results1.append(BP_res[i])
                results2.append(SA_res[i])
                results3.append(TA_res[i])
                results4.append(PSO_res[i])
                results5.append(GWO_res[i])
                results6.append(WO_res[i])
        else:
            if f!=BSO_res[i]:
                i+=2
        i+=1
    # for j in range(0, len(results0)):
    #     plt.plot(X[j], results0[j], linestyle="-", markerfacecolor='b', markeredgecolor='b', marker='h', markersize=5, alpha=0.5, label='BSO')
        #
        # plt.plot(X[j], results1[j], linestyle="-", markerfacecolor='c', markeredgecolor='c', marker='s', markersize=7,alpha=0.5, label='BP')
        #
        # plt.plot(X[j], results2[j],linestyle="-", markerfacecolor='g', markeredgecolor='g', marker='o', markersize=6,alpha=0.5, label='SA')
        #
        # plt.plot(X[j], results3[j],linestyle="-", markerfacecolor='r', markeredgecolor='r', marker='x', markersize=5,alpha=0.5, label='TA')
        #
        # plt.plot(X[j], results4[j], linestyle="-",markerfacecolor='y', markeredgecolor='y', marker='*', markersize=5,alpha=0.5, label='PSO')
        #
        # plt.plot(X[j], results5[j],linestyle="-", markerfacecolor='purple', markeredgecolor='purple', marker='+', markersize=3,alpha=0.5, label='GWO')
        #
        # plt.plot(X[j], results6[j],linestyle="-", markerfacecolor='darkorange', markeredgecolor='darkorange', marker='o', markersize=2,alpha=0.5, label='WO')

    plt.plot(X, results0, linestyle="-", color="b", marker='o', markersize=5,
             alpha=0.5, label='BSO')
    plt.plot(X, results1, linestyle="-", color="c", marker='o', markersize=7,alpha=0.5, label='BP')

    plt.plot(X, results2,linestyle="-", color="g", marker='o', markersize=6,alpha=0.5, label='SA')

    plt.plot(X, results3,linestyle="-", color="r", marker='o', markersize=5,alpha=0.5, label='TA')

    plt.plot(X, results4, linestyle="-",color="y", marker='o', markersize=5,alpha=0.5, label='PSO')

    plt.plot(X, results5,linestyle="-", color="purple", marker='o', markersize=3,alpha=0.5, label='GWO')

    plt.plot(X, results6,linestyle="-", color="darkorange", marker='o', markersize=2,alpha=0.5, label='WO')

    plt.xticks(X, ['2D(1 s)', '3D(5 s)', '4D(1 min) ', '5D(5 min)', '6D(20 min)'])

    '''
           if again you add new algorithm make another entry below for each algorithms representing
           different color 
    '''
    blue_patch = mpatches.Patch(color='b', label='Blindfolded Spiderman(BSO)')
    cyan_patch = mpatches.Patch(color='c', label='BuggyPinball(BP)')
    green_patch = mpatches.Patch(color='g', label='Simulated Annealing(SA)')
    red_patch = mpatches.Patch(color='r', label='Threshold Accepting(TA)')
    yellow_patch = mpatches.Patch(color='y', label='Particle Swarm (PSO)')
    purple_patch = mpatches.Patch(color='purple', label='Grey Wolf (GWO)')
    black_patch = mpatches.Patch(color='darkorange', label= 'Whale Optimization(WO)')
    #
    plt.legend(loc=0, fontsize='small', handles=[blue_patch, cyan_patch, green_patch, red_patch, yellow_patch, purple_patch, black_patch])

    plt.xlim([-.5, 5.5])
    plt.ylim([-.1, 1])
    plt.title(f+' function')
    plt.ylabel('Mean Absolute Error')
    plt.savefig('plotting_img/res_graphs/'+ funcs[0]+'_MAE_NonContinuous_New_Time.png', dpi=300)
    plt.show()
