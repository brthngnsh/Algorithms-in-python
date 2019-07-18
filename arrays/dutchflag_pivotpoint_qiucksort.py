# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:41:43 2019

@author: PlagueDoctor
"""
import copy
def pivot_split1(x,A):
    #x is the index of pivot
    #A is the list of elements
    pivot = A[x]
    #swapping all smaller elements
    for i in range(len(A)):
        for j in range(len(A)):
            if A[j] < pivot:
                A[i],A[j] = A[j],A[i]
    #swapping all larger elements
    for i in reversed(range(len(A))):
        for j in reversed(range(len(A))):
            if A[j] > pivot:
                A[i],A[j] = A[j],A[i]
                #printing on swap

def pivot_split2(x,A):
    #x is the index of pivot
    #A is the list of elements
    pivot = A[x]
    small , equal , large = 0 , 0 , len(A)
    while equal < large :
        if A[equal] < pivot :
            A[small] , A[equal] = A[equal] , A[small]
            small , equal = small+1 , equal+1
        elif A[equal] == pivot :
            equal += 1
        else:
            large = large-1
            A[large],A[equal]=A[equal],A[large]
            

#testcase
                
A = [1, 8, 2, 9, 9, 0, 3]
B=copy.deepcopy(A)
pivot_split1(2,A)
pivot_split2(2,B)
print(A)
print('..............................')
print(B)