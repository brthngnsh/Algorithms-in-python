"""
Created on Fri Aug 02 16:35:38 2019

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


def delete_duplicate(L):
    #this function takes advantage of the fact that the linked list is sorted 
    it = L
    # 'it' acts as write variable
    while it:
        distinct = it.next 
        #'distinct' is the traversal variable
        while distinct and distinct.data == it.data :
            distinct = distinct.next 
        it.next = distinct
        it = distinct
    return L

def main() :
    L = SingleList()
    n = int(input('Enter no of nodes : '))
    #cur is used to keep track of final element
    #and also for traversal
    cur = L.head
    print('Enter the nodes in sorted order')
    while cur != None :
        cur = cur.next
    for _ in range(n) :
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
    L.head = delete_duplicate(L.head)
    print('Output : ')
    L.print_data()

if __name__ == '__main__' :
    main()
