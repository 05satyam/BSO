'''

-This script is used to generate bar graph comparison between different algorithms.
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


def autolabel(rects, xpos='center'):
    """

    :param rects:  represents the bars
    :param xpos:  position of the legend on each bar
    """
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height+1.8),
                    xytext=(offset[xpos]*1, 1),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom', rotation=90)

'''
funcs is an array which can have multiple functions at a time 
But it is suggested to run for one function at a time
'''
#funcs = ['rastrigin', 'ackley', 'sphere', 'schwefel'] #multi-D
funcs = ['xin_she_yang_n2'] #multi-D

#put path of convergence excel sheet
xls = pd.ExcelFile("/Users/satyammittal/PycharmProjects/BP/Server-Results/Convergence_Results/3D/NonContinuous/xin_she_yang_n2_3d_NonContinuous_Convergence.xls")
lenOfExcel = 7 #number of lines in converge excel sheet
sheetX = xls.parse(0)
img_name = 'plotting_img/res_graphs/accuracy/casestudy4/' + funcs[0] + '_NonContinuous_oldTime_6dec.png'
'''
Below are the arrays for each algorithm to compare results
if you add a new algorithm add array for that new algorithm
'''
BP_res = []
BP_res.append(sheetX.columns[0])
SPM_res = []
SPM_res.append(sheetX.columns[0])
SA_res = []
SA_res.append(sheetX.columns[0])
TA_res = []
TA_res.append(sheetX.columns[0])
PSO_res = []
PSO_res.append(sheetX.columns[0])
WO_res = []
WO_res.append(sheetX.columns[0])
GWO_res = []
GWO_res.append(sheetX.columns[0])

for i in range(0,lenOfExcel):
    SPM_res.append(sheetX.values[i][0])
    BP_res.append(sheetX.values[i][1])

    SA_res.append(sheetX.values[i][2])
    TA_res.append(sheetX.values[i][3])
    PSO_res.append(sheetX.values[i][4])

    GWO_res.append(sheetX.values[i][5])
    WO_res.append(sheetX.values[i][6])

X = np.arange(6)
for f in funcs:
    '''
      hold data for plotting for each algorithm so if again you add new algorithm make another result array 
    '''
    results0=[]
    results1=[]
    results2=[]
    results3=[]
    results4 = []
    results5 = []
    results6 = []
    i=0
    while i<=lenOfExcel:
        if not BP_res[i] in funcs:
            if isinstance(BP_res[i], int):
                results0.append(BP_res[i])
                results1.append(SPM_res[i])
                results2.append(SA_res[i])
                results3.append(TA_res[i])
                results4.append(PSO_res[i])
                results5.append(WO_res[i])
                results6.append(GWO_res[i])
        else:
            if f!=BP_res[i]:
                i+=2
        i+=1
    fig, ax = plt.subplots()
    '''
        below array used for plotting 
        so if again you add new algorithm make another result array
    '''
    bp_ci = []
    spm_ci = []
    sa_ci = []
    ta_ci = []
    pso_ci = []
    wo_ci = []
    gwo_ci = []
    print(results0)
    print(results1)
    for j in range(0, len(results0)):
        bp_ci.append(196*math.sqrt((results0[j]/100)*(1-results0[j]/100)/100))
        spm_ci.append(196 * math.sqrt((results1[j] / 100) * (1 - results1[j] / 100) / 100))
        sa_ci.append(196*math.sqrt((results2[j]/100)*(1-results2[j]/100)/100))
        ta_ci.append(196*math.sqrt((results3[j]/100)*(1-results3[j]/100)/100))
        pso_ci.append(196*math.sqrt((results4[j]/100)*(1-results4[j]/100)/100))
        wo_ci.append(196 * math.sqrt((results5[j] / 100) * (1 - results5[j] / 100) / 100))
        gwo_ci.append(196 * math.sqrt((results6[j] / 100) * (1 - results6[j] / 100) / 100))

    rects1=ax.bar(X - 0.3, results0, color = 'b', width = 0.1, yerr=bp_ci, capsize=4, label='BPO')
    rects2 = ax.bar(X - 0.18, results1, color='c', width=0.1, yerr=spm_ci, capsize=4, label='BSO')
    rects3=ax.bar(X - 0.06, results2, color = 'r', width = 0.1, yerr=sa_ci, capsize=4, label='SA')
    rects4=ax.bar(X +0.06, results3, color = 'g', width = 0.1, yerr=ta_ci, capsize=4, label='TA')
    rects5=ax.bar(X + 0.18, results4, color = 'y', width = 0.1, yerr=pso_ci, capsize=4, label='PSO')
    rects6 = ax.bar(X + 0.3, results5, color='purple', width=0.1, yerr=wo_ci, capsize=4,
                    label='WO')
    rects7 = ax.bar(X + 0.42, results6, color='black', width=0.1, yerr=gwo_ci, capsize=4,
                    label='GWO')
    ax.set_xticklabels([' ', '.1s', '.2s', '.5s', '1s', '2s', '5s'])
    autolabel(rects1, "center")
    autolabel(rects2, "center")
    autolabel(rects3, "center")
    autolabel(rects4, "center")
    autolabel(rects5, "center")
    autolabel(rects6, "center")
    autolabel(rects7, "center")

    plt.legend(loc=7)
    plt.ylim([0, 120])
    plt.title(f+' function')
    plt.ylabel('Accuracy(%)')
    #             plt.ylabel('Mean Absolute Error')
                
    fig.tight_layout()

    plt.savefig(img_name, dpi=300)
    plt.show()
