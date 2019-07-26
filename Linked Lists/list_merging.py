# -*- coding: utf-8 -*-

"""
Created on Thu Jul 26 23:49:38 2019

@author: PlagueDoctor
"""

class listnode :
    def __init__(self,data=0,nextnode = None):
        self.data=data
        self.next = nextnode
        
def merging_list(L1,L2) :
    dummy_head = tail = listnode()
    #creating dummy nodes
    
    while L1 and L2 :
        if L1.data < L2.data :
            tail.next , L1 = L1, L1.next 
        else:
            tail.next , L2 = L2 , L2.next
        tail = tail.next
    
    tail.next = L1 or L2
    #appending remaining elements of L1 and L2
    return dummy_head.next


    