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

# funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann'] #3D
funcs = ['schwefel', 'eggholder']

xls = pd.ExcelFile("Server-Results/Convergence_Results/3D/1/3D_1_Continuous_Convergence_MAE.xls")
lenOfExcel = 15    #3D
sheetX = xls.parse(0)

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
    BP_res.append(sheetX.values[i][0])
    SA_res.append(sheetX.values[i][1])
    TA_res.append(sheetX.values[i][2])
    PSO_res.append(sheetX.values[i][3])
    GWO_res.append(sheetX.values[i][4])
    WO_res.append(sheetX.values[i][5])
    
xls = pd.ExcelFile("times.xls")
sheetX = xls.parse(0)
times=[0.1, 0.2, 0.5, 1, 2, 5]
BP_times = []
BP_times.append(sheetX.columns[0])
SA_times = []
SA_times.append(sheetX.columns[0])
TA_times = []
TA_times.append(sheetX.columns[0])
PSO_times = []
PSO_times.append(sheetX.columns[0])
for i in range(0,lenOfExcel):
    BP_times.append(sheetX.values[i][0])
    SA_times.append(sheetX.values[i][1])
    TA_times.append(sheetX.values[i][2])
    PSO_times.append(sheetX.values[i][2])
i=0
k=0
while i<=lenOfExcel:
    if BP_res[i] in funcs:
        if i!=0:
            for j in range(0, len(times0)):
                if results0[j]!="null":
                    plt.plot(times[j], results0[j], markerfacecolor='cyan', markeredgecolor='cyan', marker='o', markersize=5)
                if results1[j]!="null":
                    plt.plot(times[j], results1[j], markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)
                if results2[j]!="null":
                    plt.plot(times[j], results2[j], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
                if results3[j]!="null":
                    plt.plot(times[j], results3[j], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
                if results4[j]!="null":
                    plt.plot(times[j], results4[j], markerfacecolor='gray', markeredgecolor='gray', marker='o', markersize=5)
                if results5[j]!="null":
                    plt.plot(times[j], results5[j], markerfacecolor='yellow', markeredgecolor='yellow', marker='o', markersize=5)
            plt.plot(times, results0, 'cyan', label='Buggy Pinball')
            plt.plot(times, results1, 'orange', label='Simulated Annealing')
            plt.plot(times, results2, 'g', label='Threshold Accepting')
            plt.plot(times, results3, 'r', label='Particle Swarm Optimization')
            plt.plot(times, results4, 'gray', label='Grey Wolf Optimization')
            plt.plot(times, results5, 'yellow', label='Whale Optimization')
             
#             plt.legend()
             
#             plt.title(funcs[k]+' function')
            plt.xlabel('time allowances (seconds)')
            plt.ylabel('Mean Absolute Error')
#             plt.ylabel('Root-mean-square deviation')
            k+=1
            plt.show()
        times0 = []
        results0 = []
        times1 = []
        results1 = []
        times2 = []
        results2 = []
        times3 = []
        results3 = []
        results4 = []
        results5 = []
    else:
        if not BP_res[i]=='\\variantTR4':
            times0.append(BP_times[i])
            results0.append(BP_res[i])
            times1.append(SA_times[i])
            results1.append(SA_res[i])
            times2.append(TA_times[i])
            results2.append(TA_res[i])
            times3.append(PSO_times[i])
            results3.append(PSO_res[i])
            results4.append(GWO_res[i])
            results5.append(WO_res[i])
    i+=1
for j in range(0, len(times0)):
    if results0[j]!="null":
        plt.plot(times[j], results0[j], markerfacecolor='cyan', markeredgecolor='cyan', marker='o', markersize=5)
    if results1[j]!="null":
        plt.plot(times[j], results1[j], markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)
    if results2[j]!="null":
        plt.plot(times[j], results2[j], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
    if results3[j]!="null":
        plt.plot(times[j], results3[j], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    if results4[j]!="null":
        plt.plot(times[j], results4[j], markerfacecolor='gray', markeredgecolor='gray', marker='o', markersize=5)
    if results5[j]!="null":
        plt.plot(times[j], results5[j], markerfacecolor='yellow', markeredgecolor='yellow', marker='o', markersize=5)
plt.plot(times, results0, 'cyan', label='Buggy Pinball')
plt.plot(times, results1, 'orange', label='Simulated Annealing')
plt.plot(times, results2, 'g', label='Threshold Accepting')
plt.plot(times, results3, 'r', label='Particle Swarm Optimization')
plt.plot(times, results4, 'gray', label='Grey Wolf Optimization')
plt.plot(times, results5, 'yellow', label='Whale Optimization')
             
# plt.legend()
             
# plt.title(funcs[k]+' function')
plt.xlabel('time allowances (seconds)')
plt.ylabel('Mean Absolute Error')
# plt.ylabel('Root-mean-square deviation')
plt.show()
