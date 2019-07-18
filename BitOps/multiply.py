# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:03:18 2019

@author: PlagueDoctor
"""

#note: add definition must be placed inside mult definition to work[else the output is 1]
def mult(x,y):
    def add(a, b):
        running_sum, carryin, temp_a, temp_b, k = 0, 0, a, b, 1
        while temp_a or temp_b :
            ak, bk = a & k , b & k
            #bit existance
            carryout = ( ak & bk ) | (ak & carryin) | (bk & carryin)
            #new carry exists if: 
            #1.both a and b have 1 or
            #2.there exists a carry and 'a' is 1 or
            #3.there exists a carry and 'b' is 1
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1 , k<<1 , temp_a>>1 , temp_b>>1)
        return running_sum | carryin
    
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum,y)
        x, y = x >> 1, y << 1
    return running_sum

#testcase

x = 23
y = 5
z = mult(x,y)
print(z)