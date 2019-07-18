# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:41:48 2019

@author: PlagueDoctor
"""

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if(A[i]) != 10:
            break
        else:
            A[i] = 0
            A[i-1]+=1
    if(A[0] == 10):
        A[0] = 0
        A.append(0)

#testcase
    
A = [1,4,9]
plus_one(A)
print(A)
    