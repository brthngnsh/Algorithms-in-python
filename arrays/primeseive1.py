# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:52:09 2019

@author: PlagueDoctor
"""

def primebyseive1(n):
    #function returns prime numberss from 1 to n
    prime = []
    is_prime = [False,False] + [True] * (n-1)
    #prime stores prime numbers
    #initially all vaues except 0 and 1 are set to True
    for p in range(2,n+1):
        if is_prime[p]:
            prime.append(p)
        #sieving all multiples of p out of calculation
        for i in range(p,n+1,p):
            is_prime[i] = False
    return prime