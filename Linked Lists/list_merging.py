# -*- coding: utf-8 -*-

"""
Created on Thu Jul 26 23:49:38 2019

@author: PlagueDoctor
"""

class listnode :
    def __init__(self,data=0,nextnode = None):
        self.data=data
        self.next = nextnode
    def getdata(self,data):
        self.data = data
    def getnext(self,nextnode):
        self.next = nextnode

class Singlelylinked():
    def __init__(self):
        self.head = None
        
    def printf(self):
            pval = self.head
            while pval != None :
                print(pval.data)
                pval = pval.next
        
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

def main():
    
    L1 = Singlelylinked()
    e1 = listnode(5)
    e2 = listnode(8)
    L1.head = e1
    e1.next = e2
    
    L2 = Singlelylinked()
    e3 = listnode(2)
    e4 = listnode(7)
    L2.head = e3
    e3.next = e4
    print('Printing L1....')
    L1.printf()
    print('printing L2....')
    L2.printf()
    
    L1.head = merging_list(L1.head,L2.head)
    
    print('printing result.....')
    L1.printf()
    
    print('exiting....')
if __name__ == '__main__' :
    main()
    