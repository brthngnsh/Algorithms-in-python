# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:00:38 2019

@author: PlagueDoctor
"""

def swap ( x, i, j ):
    if (x >> i) & 1 != (x >> j) & 1:
        # CONDITION TO CHECK IF I AND J ARE EQUAL
        bit_mask = (1 << i) | (1 << j)
        #BITMASK IS A NEW BINARY VALUE CONTAINING ONLY THE BITS TO BE SWAPPED (IE.) X[i] AND X[j] 
        x ^= bit_mask
        #THE VALUES TO BE SWAPPED IN X ARE XORed WITH BIT_MASK 
    return x

#TESTCASE
x = 25
x = swap(x,0,1)
print(x)
