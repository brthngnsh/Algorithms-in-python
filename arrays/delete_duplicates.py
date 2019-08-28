# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:35:02 2019

@author: PlagueDoctor
"""

def delete_duplicate(A):
    if not A:
        return 0
    write_index = 0
    for i in range(1,len(A)):
        if A[i] != A[write_index]:
            write_index+=1
            A[write_index]=A[i]
    del A[write_index+1:]
    return A
x=delete_duplicate([1,1,2,2,3])
print(x)