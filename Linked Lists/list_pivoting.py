# This program pivots the list nodes
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


def list_pivot(L,k):
    if not L :
        return L
    less_head = less_node = ListNode()
    equal_head = equal_node = ListNode()
    greater_head = greater_node = ListNode()
    
    while L :
        if L.data < k :
            less_node.next = L
            less_node = less_node.next
        elif L.data == k :
            equal_node.next = L
            equal_node = equal_node.next
        else :
            greater_node.next = L
            greater_node = greater_node.next
        L = L.next
    
    greater_node.next = None
    equal_node.next = greater_head.next
    less_node.next = equal_head.next 
    return less_head.next

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
    k=int(input('Enter the pivot value : '))
    print('user entered input : ')
    L.print_data()
    print('\n\n')
    L.head = list_pivot(L.head,k)
    print('Output : ')
    L.print_data()

if __name__ == '__main__' :
    main()