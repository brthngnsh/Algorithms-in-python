# -*- coding: utf-8 -*-

"""
Created on Mon Jul 29 18:21:06 2019

@author: PlagueDoctor
"""

class ListNode:
    def __init__(self,data=0,nextnode=None) :
        self.data = data
        self.next = nextnode

class SingleList :
    def __init__(self) :
        self.head = None
        
    def print_data(self):
        cur = self.head
        while cur != None :
            print(cur.data)
            cur = cur.next

def reversing (L, start , finish) :
    dummyhead = sublist_head = ListNode(0,L)
    for _ in range(1,start):
        sublist_head = sublist_head.next
    
    #reversing
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next , temp.next , sublist_head.next = temp.next , sublist_head.next , temp
        
        #Explaination :
        #  sublist_head.next points to the start position
        #  sublist_iter is initially at start and it traverses through the list pushing the element next to it to start position
        #  so that it reachs the finish position first
        #  temp is used to hold the node being pushed by sublist_iter when sublist_iter.next takes the value of temp.next
        #  fianlly sublist_head.next is attached to temp and temp.next takes the value of sublist_head.next(ie temp becomes node at start position)
    
    return dummyhead.next

def main() :
    L = SingleList()
    cou = int(input('Enter no of nodes : '))
    #cur is used to keep track of final element
    #and also for traversal
    cur = L.head
    while cur != None :
        cur = cur.next
    for _ in range(cou) :
        if L.head == None :
            #this runs if linked list contains no elements
            n = ListNode()
            n.data = int(input())
            L.head = n
            cur = n
        else :
            #A new node n is created
            n = ListNode()
            n.data = int(input())
            cur.next = n
            #n gets added next to current node
            cur = cur.next
        print('user entered input : ')
    L.print_data()
    print('\n\n')
    L.head = reversing(L.head,1,4)
    L.print_data()
    
    
if __name__ == '__main__' :
    main()