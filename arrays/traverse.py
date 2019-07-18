# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:05:39 2019

@author: PlagueDoctor
"""

def traverse(A):
    #A is a list which contains a list of 
    #numbers which repersents the the max move that can be taken 
    #from that position
    furthest_reached , last_index = 0 , len(A)-1
    i = 0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached , A[i]+i)
        #A[i] is the maximum index it can move from index i 
        i+=1
    return furthest_reached >= last_index
#returns true if the last position can be reached