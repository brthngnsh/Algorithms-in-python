# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:14:35 2019

@author: PlagueDoctor
"""

import random
def uniform_random_numbers(lowerbound,upperbound):
    
    number_of_outcomes = upperbound - lowerbound + 1
    while  True :
      result,i = 0,0
      while (i<<1) < number_of_outcomes:
          result = result<<1 | int(random.random())
          i+=1
          if result < number_of_outcomes :
              break
    return result + lowerbound
