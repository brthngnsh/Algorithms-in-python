# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:59:27 2019

@author: PlagueDoctor
"""

def primebyseive2(n):
    if n<2:
        return []
    prime = [2]
    #prime stores prime numbers
    size = (n - 3) // 2 + 1
    #reducing the size of calculation since sieve for prime 
    #is completed halfway through the array
    is_prime = [True] * size
    for i in range(size):
        p = 2*i + 3
        #prime pattern
        prime.append(p)
        for j in range(2*i**2 + 6*i + 3,size,p):
            is_prime[j] = False
            #seiving by p^2
            #hence the 2*i**2 + 6*i + 3 as start value for range