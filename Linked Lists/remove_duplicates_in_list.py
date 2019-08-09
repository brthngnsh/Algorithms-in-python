def remove_dups_in_list(L):
    it = L
    while it:
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = it.next
    return L