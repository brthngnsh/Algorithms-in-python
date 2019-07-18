# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:57:28 2019

@author: PlagueDoctor
"""

def multiply_digits(x,y):
    sign=1
    if (x[0]<0) ^ (y[0]<0):
        sign = (-1) 
    else:
        x[0],y[0] = abs(x[0]),abs(y[0])
    print('sign= '+str(sign))
    result = [0] * (len(x) + len(y))
    for i in reversed(range(len(x))):
        for j in reversed(range(len(y))):
            result[i+j+1] += x[i]*y[j]
            result[i+j] += result[i+j+1]//10
            result[i+j+1] %=10
    result = result[next((i for i,x in enumerate(result) if x!=0),len(result)):] or [0]
    result[0]*=sign
    return result


#testcase
    
A=[-1,4,5]
B=[2,3]
C=multiply_digits(A,B)
print(C)