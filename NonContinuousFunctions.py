import math
import random

import numpy as np

import functions

'''
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
-----------------------------------USED DISCONTINOUS FUNCTIONS-------------------------------------------------
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
'''
'''
1.
[-100,100]
f(0)=0
sncd min y=1
'''
def step_fun(xvals1):
    fun_val=0;
    for i in xvals1:
        fun_val += (np.floor(abs(i)))
    return fun_val

'''
#2
CEC2005
Non-Continuous Expanded Scaffer’s F6 Function
0, 0.0441
'''
def expanded_scaffer_fun(xvals):

        def scaffer_fun(x1, x2):
            return 0.5 + (np.sin(np.sqrt(x1 ** 2 + x2 ** 2)) ** 2 - 0.5) / (
                    1 + 0.001 * (x1 ** 2 + x2 ** 2)) ** 2

        #rounding xvals as per the function requirement
        for i in range(0, len(xvals)):
            if abs(xvals[i]) >= 0.5:
                xvals[i] = round(2 * xvals[i]) / 2

        '''
         below line is calculating scaffer_fun(xvals[d] and xvals[1]) d is the dimension
        '''
        result = scaffer_fun(xvals[-1], xvals[0])
        for i in range(0, len(xvals) - 1):
            result += scaffer_fun(xvals[i], xvals[i+1])
        return result

'''
CONTINUOUS SCAFFER FUN
'''
def continous_scaffer_fun(xvals):  # Defines the function
    return 0.5+( ((np.sin((xvals[0] ** 2 + xvals[1] ** 2) ** 2) ** 2) - 0.5)
                 / ((1 + 0.001 * (xvals[0] ** 2 + xvals[1] ** 2)) ** 2))




'''
#3
non continous rastrigin function
min=0
[-5.12, 5.12]
https://www.researchgate.net/publication/347268116_Weighted_Fuzzy_Production_Rule_Extraction_Using_Modified_Harmony_Search_Algorithm_and_BP_Neural_Network_Framework
'''

def rastrigin(xvals):
    fun_val=len(xvals)*10
    for i in xvals:
        yi=i
        if(np.abs(i)>=0.5):
            yi= round(2*i)/2
        fun_val += yi**2 - 10*(np.cos(2*np.pi*yi))
    return fun_val

'''
4
https://towardsdatascience.com/optimization-eye-pleasure-78-benchmark-test-functions-for-single-objective-optimization-92e7ed1d1f12

xi [-2pi,2pi]
i [1,d]
f(0…..0) = 0
2nd min = 0.430
'''
def xin_she_yang_n2(xvals):
    fst_val=0
    scnd_val=0
    for i in range(0,len(xvals)):
        fst_val +=  np.abs(xvals[i])

    for i in range(0, len(xvals)):
        scnd_val += np.sin(xvals[i]**2)

    return fst_val*(np.exp(-scnd_val))

'''
5
rosenbrock non continuoys function
https://repository.up.ac.za/bitstream/handle/2263/39764/Wilke_Gradient_2013.pdf;sequence=1
y-min=0
y-2nd min=1
-1<=x<=1
'''
def rosenbrock(xvals):
    res=0
    #print(len(xvals))
    n = len(xvals)//2
    #print("len xvals ",len(xvals))
    for i in range(0,n):

        if(0 <= np.sin(2*(np.abs(xvals[i]))) and  np.sin(2*(np.abs(xvals[i]))) < (2/3)):
            val1 = (xvals[i] * (2 * i) - (xvals[i] ** 2 * (2 * i - 1))) ** 2
            val2 = (1 - xvals[i] * (2 * i - 1)) ** 2
            res += (1/1.2)*(100*val1 + val2)

        if((-2/3) <= np.sin(2*(np.abs(xvals[i]))) and np.sin(2*(np.abs(xvals[i]))) < 0):
            val1 = (xvals[i] * (2 * i) - (xvals[i] ** 2 * (2 * i - 1))) ** 2
            val2 = (1 - xvals[i] * (2 * i - 1)) ** 2
            res += 1.2*(100*val1 + val2)

        if((-2/3) > np.sin(2*(np.abs(xvals[i]))) and np.sin(2*(np.abs(xvals[i])))>=(2/3)):
            val1 = (xvals[i] * (2 * i) - (xvals[i] ** 2 * (2 * i - 1))) ** 2
            val2 = (1 - xvals[i] * (2 * i - 1)) ** 2
            res += (100*val1 + val2)

    return res

#below method is used for 2d plot only
def rosenbrock1(xvals):
    res=0
    n = len(xvals)
    print(n)
    #for i in range(0,n):

    if (0 <= np.sin(2 * (np.abs(xvals))) and np.sin(2 * (np.abs(xvals))) < (2 / 3)):
        val1 = (xvals * (2 * 1) - (xvals ** 2 * (2 * 1 - 1))) ** 2
        val2 = (1 - xvals * (2 * 1 - 1)) ** 2
        res += (1 / 1.2) * (100 * val1 + val2)

    if ((-2 / 3) <= np.sin(2 * (np.abs(xvals))) and np.sin(2 * (np.abs(xvals))) < 0):
        val1 = (xvals * (2 * 1) - (xvals ** 2 * (2 * 1 - 1))) ** 2
        val2 = (1 - xvals * (2 * 1 - 1)) ** 2
        res += 1.2 * (100 * val1 + val2)

    if ((-2 / 3) > np.sin(2 * (np.abs(xvals))) and np.sin(2 * (np.abs(xvals))) >= (2 / 3)):
        val1 = (xvals * (2 * 1) - (xvals ** 2 * (2 * 1 - 1))) ** 2
        val2 = (1 - xvals * (2 * 1 - 1)) ** 2
        res += (100 * val1 + val2)
    return res


'''
6
main function
y min = 0
y 2ndminx = 0.0744
-1<=x<=1

https://repository.up.ac.za/bitstream/handle/2263/39764/Wilke_Gradient_2013.pdf;sequence=1
https://link.springer.com/article/10.1007/s11081-011-9178-7
'''
def quadric(xvals):
    res = 0
    n = len(xvals)
    for i in range(0,n):
        for j in range(0,i):
            if(np.sin(8*np.abs(xvals[i])) > 0.5):
                res += xvals[j]
            if(np.sin(8*np.abs(xvals[i])) < -0.5):
                res += 1.2*(xvals[j])
            if (np.sin(8 * np.abs(xvals[i])) >= -0.5 and np.sin(8*np.abs(xvals[i])) <= 0.5):
                res += (1/1.2) * (xvals[j])

        res = res **2

    return res


'''
below function used for 2d plot only
'''
def quadric1(xvals):
    res = 0
    n = len(xvals)
    print(n)
    if (np.sin(8 * np.abs(xvals)) > 0.5):
        res += xvals
    if (np.sin(8 * np.abs(xvals)) < -0.5):
        res += 1.2 * (xvals)
    if (np.sin(8 * np.abs(xvals)) >= -0.5 and np.sin(8 * np.abs(xvals)) <= 0.5):
        res += (1 / 1.2) * (xvals)

    res = res ** 2

    return res

'''
ymin=0
2nd ymin=0.85
-2 <= xval <= 2

https://repository.up.ac.za/bitstream/handle/2263/39764/Wilke_Gradient_2013.pdf;sequence=1
https://link.springer.com/article/10.1007/s11081-011-9178-7
'''
def ellipsoid(xvals):
    res=0
    n = len(xvals)
    # for i in range(0,n):
    limit_sum=0
    for j in range(n):
        limit_sum += xvals[j]

    if(np.sin(2*limit_sum)>0.5):
        for i in range(0, n):
            res +=  (1/1.1)*(2 ** (i-1))*(xvals[i] ** 2)
        res += 1/n
    elif(np.sin(2*limit_sum)<-0.5):
        for i in range(0, n):
            res += (1.1) * (2 ** (i - 1)) * (xvals[i] ** 2)
        res += 1 / n
    else:
        for i in range(0, n):
            res += (2 ** (i - 1)) * (xvals[i] ** 2)

    return  res
