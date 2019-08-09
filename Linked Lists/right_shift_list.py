def list_right_shift(L,k):
    # k is the integer that shows how many rotations take place
    tail , n = L , 1
    if not L:
        return L
    while tail:
        tail = tail.next
        n += 1
    
    k %= n
    tail.next = L # joinng the tail to the head
    step_to_head , new_tail  =  n-k , tail
    # the final head is k steps behind the current tail
    # which n-k steps in forward direction
    while step_to_head:
        step_to_head -= 1
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.ext = None
    L = new_head
    return L

    