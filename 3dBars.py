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

def autolabel(rects, xpos='center'):
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

# funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann'] #3D
funcs = ['step_fun'] #3D

xls = pd.ExcelFile("BP_Spiderman_convergence.xls")
lenOfExcel = 3    #3D
sheetX = xls.parse(0)
print(sheetX)
BP_res = []
BP_res.append(sheetX.columns[0])
SPM_res = []
SPM_res.append(sheetX.columns[0])
#
# SA_res = []
# SA_res.append(sheetX.columns[0])
# TA_res = []
# TA_res.append(sheetX.columns[0])
# PSO_res = []
# PSO_res.append(sheetX.columns[0])
# GWO_res = []
# GWO_res.append(sheetX.columns[0])
# WO_res = []
# WO_res.append(sheetX.columns[0])
for i in range(0,lenOfExcel):
    BP_res.append(sheetX.values[i][0])
    SPM_res.append(sheetX.values[i][1])
    # SA_res.append(sheetX.values[i][1])
    # TA_res.append(sheetX.values[i][2])
    # PSO_res.append(sheetX.values[i][3])
    # GWO_res.append(sheetX.values[i][4])
    # WO_res.append(sheetX.values[i][5])

i=0
k=0
X = np.arange(1)
while i<=lenOfExcel:
    #print("i : ", i)
    if BP_res[i] in funcs:
        if i!=0:
            fig, ax = plt.subplots()
            bp_ci = []
            spm_ci = []
            # sa_ci = []
            # ta_ci = []
            # pso_ci = []
            # gwo_ci = []
            # wo_ci = []
            for j in range(0, len(results0)):
                bp_ci.append(196*math.sqrt((results0[j]/100)*(1-results0[j]/100)/100))
                spm_ci.append(196 * math.sqrt((results1[j] / 100) * (1 - results1[j] / 100) / 100))
                # sa_ci.append(196*math.sqrt((results1[j]/100)*(1-results1[j]/100)/100))
                # ta_ci.append(196*math.sqrt((results2[j]/100)*(1-results2[j]/100)/100))
                # pso_ci.append(196*math.sqrt((results3[j]/100)*(1-results3[j]/100)/100))
                # gwo_ci.append(196*math.sqrt((results4[j]/100)*(1-results4[j]/100)/100))
                # wo_ci.append(196*math.sqrt((results5[j]/100)*(1-results5[j]/100)/100))
            
            rects1=ax.bar(X - 0.375, results0, color = 'cyan', width = 0.15, yerr=bp_ci, capsize=2, label='Buggy Pinball')
            rects2 = ax.bar(X - 0.225, results1, color='orange', width=0.15, yerr=spm_ci, capsize=2,
                            label='Spiderman')
            # rects2=ax.bar(X - 0.225, results1, color = 'orange', width = 0.15, yerr=sa_ci, capsize=2, label='Simulated Annealing')
            # rects3=ax.bar(X - 0.075, results2, color = 'g', width = 0.15, yerr=ta_ci, capsize=2, label='Threshold Accepting')
            # rects4=ax.bar(X + 0.075, results3, color = 'r', width = 0.15, yerr=pso_ci, capsize=2, label='Particle Swarm Optimization')
            # rects5=ax.bar(X + 0.225, results4, color = 'gray', width = 0.15, yerr=gwo_ci, capsize=2, label='Grey Wolf Optimization')
            # rects6=ax.bar(X + 0.375, results5, color = 'yellow', width = 0.15, yerr=wo_ci, capsize=2, label='Whale Optimization')
                        
            ax.set_xticklabels(['', '0.1', '0.2', '0.5', '1', '2', '5'])
            autolabel(rects1, "left")
            autolabel(rects2, "left")
            # autolabel(rects2, "left")
            # autolabel(rects3, "left")
            # autolabel(rects4, "left")
            # autolabel(rects5, "left")
            # autolabel(rects6, "left")
#             plt.legend(loc=4)
            plt.ylim([0, 115])
#             plt.xlim([0.5, 8])
#             plt.title(funcs[k]+' function')
            plt.xlabel('time allowances (seconds)')
            plt.ylabel('Accuracy (%)')
#             plt.ylabel('Mean Absolute Error')
            k+=1
            
            fig.tight_layout()
            plt.show()
        results0 = []
        results1 = []
        results2 = []
        results3 = []
        results4 = []
        results5 = []
    else:
        if not BP_res[i]=='\\variantTR4'and i!=1:
            print("i : ",i, " , " ,BP_res[i], " , ",SPM_res[i])
            results0.append(BP_res[i])
            results1.append(SPM_res[i])
            # results1.append(SA_res[i])
            # results2.append(TA_res[i])
            # results3.append(PSO_res[i])
            # results4.append(GWO_res[i])
            # results5.append(WO_res[i])
    i+=1
fig, ax = plt.subplots()
bp_ci = []
spm_ci = []
sa_ci = []
ta_ci = []
pso_ci = []
gwo_ci = []
wo_ci = []
print(results0)
print(results1)
for j in range(0, len(results0)):
    bp_ci.append(196*math.sqrt((results0[j]/100)*(1-results0[j]/100)/100))
    spm_ci.append(196 * math.sqrt((results1[j] / 100) * (1 - results1[j] / 100) / 100))
    # sa_ci.append(196*math.sqrt((results1[j]/100)*(1-results1[j]/100)/100))
    # ta_ci.append(196*math.sqrt((results2[j]/100)*(1-results2[j]/100)/100))
    # pso_ci.append(196*math.sqrt((results3[j]/100)*(1-results3[j]/100)/100))
    # gwo_ci.append(196*math.sqrt((results4[j]/100)*(1-results4[j]/100)/100))
    # wo_ci.append(196*math.sqrt((results5[j]/100)*(1-results5[j]/100)/100))

rects1=ax.bar(X - 0.375, results0, color = 'cyan', width = 0.15, yerr=bp_ci, capsize=2, label='Buggy Pinball')
rects2=ax.bar(X - 0.225, results1, color = 'orange', width = 0.15, yerr=spm_ci, capsize=2, label='Simulated Annealing')

# rects2=ax.bar(X - 0.225, results1, color = 'orange', width = 0.15, yerr=sa_ci, capsize=2, label='Simulated Annealing')
# rects3=ax.bar(X - 0.075, results2, color = 'g', width = 0.15, yerr=ta_ci, capsize=2, label='Threshold Accepting')
# rects4=ax.bar(X + 0.075, results3, color = 'r', width = 0.15, yerr=pso_ci, capsize=2, label='Particle Swarm Optimization')
# rects5=ax.bar(X + 0.225, results4, color = 'gray', width = 0.15, yerr=gwo_ci, capsize=2, label='Grey Wolf Optimization')
# rects6=ax.bar(X + 0.375, results5, color = 'yellow', width = 0.15, yerr=wo_ci, capsize=2, label='Whale Optimization')
            
ax.set_xticklabels(['','1'])
autolabel(rects1, "left")
autolabel(rects2, "left")
# autolabel(rects2, "left")
# autolabel(rects3, "left")
# autolabel(rects4, "left")
# autolabel(rects5, "left")
# autolabel(rects6, "left")
#             plt.legend(loc=4)
plt.ylim([0, 115])
#             plt.xlim([0.5, 8])
#             plt.title(funcs[k]+' function')
plt.xlabel('time allowances (seconds)')
plt.ylabel('Accuracy (%)')
#             plt.ylabel('Mean Absolute Error')
k+=1

fig.tight_layout()
plt.show()