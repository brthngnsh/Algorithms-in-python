def cycletest(head):
    def cycle_len(end):
        start , step = end , 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    
    slow = fast = head
    #fast and slow are list pointer moving at different pace
    #if slow anf fast point to the same node after the first jump then there exists a cycle
    while fast and fast.next and fast.next.next :
        slow , fast = slow.next , fast.next.next 
        if slow is fast :
            #cycle_len_iter is used to find the start of the cycle
            cycle_len_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_iter = cycle_len_iter.next 
            
            it = head
            # iter check for cycle
            while it is not cycle_len_iter :
                it = it.next 
                cycle_len_iter = cycle_len_iter.next 
            return it #it points to the cycle
    return None   # None is returned if the fast node does not have any nodes ahead of it (ie) linked list has an end point

