# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:54:16 2019

@author: PlagueDoctor
"""
#random selection - offline data
import random
def offline_dats_sampling(k,A):
    for i in range(k):
        r = random.randint(i,len(A) - 1)
        A[i],A[r] = A[r],A[i]
    