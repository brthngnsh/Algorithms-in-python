# this program locates the ceter of the list and compares nodes
import list_reverse as lr

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


def list_is_palindrome(L,n):
    fast = slow = L
    count = 0
    while fast and fast.next :
        fast , slow = fast.next.next , slow.next
        count += 1 
    
    first_half , second_half = L , lr.reversing(slow,1,count) 
    while first_half and second_half :
        print('comparing : ',second_half.data,first_half.data)
        if first_half.data != second_half.data :
            return False
        second_half , first_half = second_half.next , first_half.next 
    return True

def main():
    L = SingleList()
    n = int(input('Enter no of nodes : '))
    #cur is used to keep track of final element
    #and also for traversal
    cur = L.head
    cou = n
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
    result = list_is_palindrome(L.head,cou)
    print('\n')
    print('Output : ',result)

if __name__ == '__main__' :
    main()