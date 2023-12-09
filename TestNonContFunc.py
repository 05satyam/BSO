'''

Delete this file
'''
import time
from random import random

from numpy.random import randint

import NonContinuousFunctions

start_time1=time.process_time()

while(True):
   xvals = randint(-5.12, 5.12, 50)
   y = NonContinuousFunctions.non_continous_rastrigin(xvals)
   if(y<0):
      print("negative ", y)
      break
   else:
      print("positive")

   if (time.process_time() + start_time1 > 300): #in seconds
      print("5 minutes done, no negative value found")
      break;

