# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:52:08 2019

@author: PlagueDoctor
"""

def alternation(A):
    #input : list of integers --> 'A'
    #output : List 'B'
    #B--> B[0]<=B[1]>=B[2]<=B[3]
    #finding median gives O(n)
    #regular sorting gives O(nlogn)
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2],reverse=i%2)
    #the above algorithm has O(n) time complexity
    #but it does not require space for more than 2 elements
        