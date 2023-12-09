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
import scipy.stats as stats
#from scipy.stats import conover
from itertools import combinations
import statsmodels.api as sm
from statsmodels.formula.api import ols
from bioinfokit.analys import stat

'''

------Below notation used by SM
SM-satyam mittal
nc = non contninuous
cnt = continuous

algorithms = ['Spiderman', 'BP','SA','TA','PSO','WO','GWO']
nc_functions = ['quadric', 'rosenbrock', 'step_fun', 'xin_she_yang_n2', 'rastrigin', 'ellipsoid']
nc_funcs = ['quadric', 'rosenbrock', 'step_fun', 'xin_she_yang_n2', 'rastrigin', 'ellipsoid']
nc_f_minimum =[0 , 0 , 0 , 0,0,0]
nc_convergeLimit =[0.0744 , 1 , 1 , 0.430,1,0.85]

cnt_functions=[ 'rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']
cnt_funcs=[ 'rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']
cnt_f_minimum =[0, 0, 0, -1, -186.7309, 0, -19.2085, -959.6407, -1, -4.15580929184779]
cnt_convergeLimit =[0.99, 2.5, 100, -0.1, -49, 118, -18.1, -936, -0.94, -4.127577]

knapsack_objective_fun_without_probablity_1
'''

algorithms = ['Spiderman', 'BP', 'SA', 'TA', 'PSO', 'WO', 'GWO']
functions = ['knapsack_objective_fun_without_probablity_1']
funcs = ['knapsack_objective_fun_without_probablity_1']
f_minimum = [0]
convergeLimit = [1]
import scikit_posthocs as sp
def convor(df):
    # Perform post hoc analysis with Holm correction
    data = [df['Spiderman'], df['BP'], df['SA'], df['TA'], df['PSO'], df['WO'],df['GWO']]
    labels = ['Spiderman', 'BP', 'SA', 'TA', 'PSO', 'WO', 'GWO']

    posthoc_results = sp.posthoc_conover(data, p_adjust='bonferroni')
    # Convert the results to a pandas DataFrame
    df_results = pd.DataFrame(posthoc_results)

    # Convert the DataFrame to LaTeX format
    latex_table = df_results.to_latex()

    # Print or display the LaTeX table
    print(latex_table)


def kruskal_wallis():
    for k in range(0, len(functions)):
        for d in range(2, 7):  # dimension from 2-6
            dataACC = {'Spiderman': [], 'BP': [], 'SA': [], 'TA': [], 'PSO': [], 'WO': [], 'GWO': []}
            dataPRE = {'Spiderman': [], 'BP': [], 'SA': [], 'TA': [], 'PSO': [], 'WO': [], 'GWO': []}
            weGotSomethin = False
            for a in algorithms:
                print(a)
                #string = "../Server-Results/New_Time/" + a + "/NonContinuous/" + a + "_" + funcs[k] + "_" + str(d) + ".xls"
                string = "../Server-Results/Knapsack_Results/" + a + "_knapsack/29oct/" + a + "_" + funcs[k] + "_" + str(
                    d) + ".xls"

                if (path.exists(string)):
                    xls = pd.ExcelFile(string)
                    weGotSomethin = True
                    sheetX = xls.parse(0)
                    algo = a  # a.replace('\\', '')

                    # if float(sheetX.columns[0]) < convergeLimit[k]:
                    #     dataACC[algo].append(float(sheetX.values[0][0]))
                    #     dataPRE[algo].append(float(sheetX.columns[0]))
                    # else:
                    #     dataACC[algo].append(0)
                    #     dataPRE[algo].append(None)
                    dataACC[algo].append(float(sheetX.values[0][0]))
                    dataPRE[algo].append(float(sheetX.columns[0]))
                    for i in range(0, 99):
                        #if float(sheetX.values[i][0]) < convergeLimit[k]:
                            dataACC[algo].append(float(sheetX.values[i][0]))
                            dataPRE[algo].append(float(sheetX.values[i][0]))
                        # else:
                        #     dataACC[algo].append(0)
                        #     dataPRE[algo].append(None)

            if (weGotSomethin):
                alpha = 0.05  # Significance level
                print("--------------", funcs[k], "function,", d, "dimensions--------------")
                print("THE FOLLOWING RESULT FOR ACCURACY")
                # print(dataACC)
                df = pd.DataFrame(dataACC)
                df_melt = pd.melt(df.reset_index(), id_vars=['index'],
                                  value_vars=['Spiderman', 'BP', 'SA', 'TA', 'PSO', 'WO', 'GWO'])
                df_melt.columns = ['index', 'algorithm', 'value']

                stat, pvalue = stats.kruskal(df['Spiderman'], df['BP'], df['SA'], df['TA'], df['PSO'], df['WO'],
                                                df['GWO'])
                print("P value overall is", pvalue)
                if pvalue > alpha:
                    print("No significant difference between groups (fail to reject H0)")
                else:
                    print("Significant difference between groups (reject H0)")

                #print("KRUSKALs STATS  are:  ", stat)
                #convor(df)

                print("THE FOLLOWING RESULT FOR PRECISION")
                df = pd.DataFrame(dataPRE)
                df_melt = pd.melt(df.reset_index(), id_vars=['index'],
                                  value_vars=['Spiderman', 'BP', 'SA', 'TA', 'PSO', 'WO', 'GWO'])
                df_melt.columns = ['index', 'algorithm', 'value']

                fvalue, pvalue = stats.kruskal(df['Spiderman'], df['BP'], df['SA'], df['TA'], df['PSO'], df['WO'],
                                                df['GWO'])
                print("P value overall is", pvalue)
                if pvalue > alpha:
                    print("No significant difference between groups (fail to reject H0)")
                else:
                    print("Significant difference between groups (reject H0)")

                #print("KRUSKAL STATS  are:  ", stats)
                convor(df)

kruskal_wallis()


