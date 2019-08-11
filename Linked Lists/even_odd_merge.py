# This program reorders the nodes by placing the 
# even indexed nodes at the beginning fo;;owed
# by the odd indexed nodes

class ListNode:
    def __init__(self,data=0) :
        self.data = data
        self.next = None

class SingleList :
    def __init__(self) :
        self.head = None
        
    def print_data(self):
        cur = self.head
        while cur != None :
            print(cur.data)
            cur = cur.next


def even_odd_merge(L) :
    if not L :
        return L
    
    even_dummy , odd_dummy = ListNode(0) , ListNode(0)
    tails , turn = [even_dummy , odd_dummy] , 0
    while L :
        tails[turn].next = L
        L = L.next
        turn ^= 1
        tails[turn] = tails[turn].next
    tails[1].next = None
    tails[0].next = odd_dummy
    return even_dummy.next

def main():
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
    L.head = even_odd_merge(L.head)
    print('Output : ')
    L.print_data()

if __name__ == '__main__' :
    main()