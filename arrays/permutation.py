# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:08:10 2019

@author: PlagueDoctor
"""

def permutation1(perm,A):
    for i in range(len(perm)):
        next = i
        while perm[next] >= 0 :
            #if perm[next] is -ve then it has already completed a swapping
            A[i],A[perm[next]] = A[perm[next]],A[i]
            #swapping permutation value to position in array
            temp = perm[next]
            #storing value in temp to use as next
            perm[next] -= len(perm)
            #adding -ve sign in perm to indicate that the permutation at 
            #the given position is completed
            next = temp
            #temp assigned to next to for a cycle
            #i increments when cycle is completed
            #ie when next gets -ve value
    #removing -ve sign
    perm[:] = [a + len(perm) for a in perm]
    
def permutation2(perm,A):
    def cyclic_permutation(start,perm,A):
        i , temp = start , A[start]
        while True:
            next_i = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i , temp = next_i , next_temp
            if i == start :
                break
    for i in range(len(A)):
        j=perm[i]
        while j!=i:
            if j < i :
                break
            j=perm[j]
        else:
            cyclic_permutation(i,perm,A)