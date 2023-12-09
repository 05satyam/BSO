'''

script to calculate variance, mean and average from excel sheets for the result obtained

df[0] : it will read the result value from excel sheet and assume that results are in 0th column of sheet
'''
import pandas as pd
from os import path

algorithms = ['PSO_knapsack', 'SA_knapsack', 'Spiderman_knapsack', 'WO_knapsack']
functions = 'knapsack_objective_fun_without_probablity_1'

for a in algorithms:
    print("\n")
    print("Algorithm: ", a ," ->" )
    for dim in range(2, 11):
        string = "Server-Results/Knapsack_Results/" + a + "/random_item/"+a+ "_" + functions + "_"+str(dim) + "_randomItem.xls"
        if(path.exists(string) == False and a == 'Spiderman_knapsack' and dim==3):
            string = "Server-Results/Knapsack_Results/" + a + "/random_item/" + a + "_" + functions + "_" + str(
                10) + "_randomItem_1.xls"

        if (path.exists(string) == False):
            # print("path ", string)
            continue
        # Read in Excel sheet
        df = pd.read_excel(string, header=None)

        # Calculate variance, mean and avg
        variance = df[0].var()
        mean = df[0].mean()
        average = df[0].sum() / len(df)

        print("Dimension: ", str(dim) ," Mean: ",mean ," Average: ",average , " Variance: ", variance)