# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:35:13 2019

@author: PlagueDoctor
"""

def power(x,y):
    #compute x^y
    result, power = 1.0, y
    if y < 0 :
        power, x = -power, 1.0/x
    while power & 1 :
        result*=x
        x,power = x * x, power >> 1
    return result

#testcase
    
x = 5
y = 3
z = power(x,y)
print(z)