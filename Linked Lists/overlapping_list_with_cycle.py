"""
Created on Wed Aug 07 21:17:38 2019

@author: PlagueDoctor
"""

import cycle_test as ct
import overlapping_list_cycle_free as cf

def overlapping_with_cycle_test(L1,L2):
    root1 , root2 = ct.cycletest(L1) , ct.cycletest(L2)

    if not root1 and not root2 :
        #no cycle exists
        return cf.overlapping_list(L1,L2)

    elif (root1 and not root2) or (root2 and not root1) :
        return None
    # None is return because there is a list with a cycle while one doesn't have one
    # It implies that the two Lists do not overlap
    # If it ad been so then both would have a cycle
    temp = root2
    while(True) :
        temp = temp.next
        if temp == root1 or temp == root2 :
            break
        if temp != root1 :
            return None
    def distance(a,b):
        dist = 0
        while a!=b:
            a = a.next
            dist += 1
        return dist
    dist_1 , dist_2 = distance(L1,root1) , distance(L2,root2)
    # Locating first overlapping
    if dist_1 > dist_2 :
        dist_1 , dist_2 = dist_2 , dist_1
        root1 , root2 = root2 , root1
    for _ in range(abs(dist_1 - dist_2)):
        L2 = L2.next 
    while L1 is not L2 and L1 is not root1 and L2 is not root2 :
        L1,L2 = L1.next,L2.next
    # If L1 = L2 before reaching root1 then the meet occcurs before cycle
    # else the itersection takes place within the cycle in which case any node within the cycle can be returned
    return L1 if L1 is L2 else root1
    
