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

def list_add(L1 , L2) :
    cur_pointer = dummy_head = ListNode()
    carry = 0
    while L1 or L2 or carry :
        value = (L1.data if L1 else 0) + (L2.data if L2 else 0) + carry
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        cur_pointer.next = ListNode(value % 10)
        carry , cur_pointer = value // 10 , cur_pointer.next 
    return dummy_head.next 

def main() :
    L1 = SingleList()
    n = int(input('Enter no of nodes : '))
    #cur is used to keep track of final element
    #and also for traversal
    cur = L1.head
    print('Enter the nodes in sorted order')
    while cur != None :
        cur = cur.next
    for _ in range(n) :
        if L1.head == None :
            #this runs if linked list contains no elements
            n = ListNode()
            n.data = int(input())
            L1.head = n
            cur = n
        else :
            #A new node n is created
            n = ListNode()
            n.data = int(input())
            cur.next = n
            #n gets added next to current node
            cur = cur.next
    print('user entered input : ')
    L1.print_data()
    print('\n\n')
    L2 = SingleList()
    n = int(input('Enter no of nodes : '))
    #cur is used to keep track of final element
    #and also for traversal
    cur = L2.head
    print('Enter the nodes in sorted order')
    while cur != None :
        cur = cur.next
    for _ in range(n) :
        if L2.head == None :
            #this runs if linked list contains no elements
            n = ListNode()
            n.data = int(input())
            L2.head = n
            cur = n
        else :
            #A new node n is created
            n = ListNode()
            n.data = int(input())
            cur.next = n
            #n gets added next to current node
            cur = cur.next
    print('user entered input : ')
    L2.print_data()
    print('\n\n')
    L1.head = list_add(L1.head,L2.head)
    L1.print_data()

if __name__ == '__main__' :
    main()
    
