# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:24:17 2019

@author: PlagueDoctor
"""

def division(x,y):
    #computing x/y
    result, power = 0, 32
    y_power = y << power
    while x >= y :
        while y_power > x:
                y_power >>= 1
                power -= 1
        result += 1 << power
        x -= y_power
    return result

#testcase
    
x = 24
y = 5
z = division(x,y)
print(z)

