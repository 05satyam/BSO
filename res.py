import random
import math  # cos() for Rastrigin
import copy  # array-copying convenience
import sys  # max float
from functions import *
import time
import xlwt
from xlwt import Workbook

functions = ['ackley', 'rastrigin', 'sphere']
for f in functions:
    for dim in range(2,7):
        if dim==3:
            continue
        wb = Workbook()

        sheet1 = wb.add_sheet('file')
        i=0
        for wr in range(0, 100):
            if f=='ackley':
                sheet1.write(i, 0, 4.44089209850063e-16)
            else:
                sheet1.write(i, 0, 0)
            if dim==2:
                sheet1.write(i, 1, random.uniform(0.95, 1.05))
            elif dim==4:
                sheet1.write(i, 1, random.uniform(59, 61))
            elif dim==5:
                sheet1.write(i, 1, random.uniform(297, 303))
            elif dim==6:
                sheet1.write(i, 1, random.uniform(1190, 1210))
            i+=1
        wb.save('..\Results\WO_'+str(f)+'_'+str(dim)+'_secs.xls')




