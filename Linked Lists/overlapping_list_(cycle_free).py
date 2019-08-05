def overlapping_list(L1,L2):
    
    def Length(L):
        length = 0
        while L :
            length += 1
            L = L.next
        return length
    
    L1_len , L2_len = Length(L1) , Length(L2)
    if L1_len > L2_len :
        L1 , L2 = L2, L1 #L2 is kept as the longer list
    
    for _ in (abs(L1_len - L2_len)) :
        L2 = L2.next 
    #traversing the extra elements

    while L1 and L2 and L1 is not L2 :
       L1 , L2 = L1.next , L2.next 
    return L1 #If fthe return value is none then there is no overlapping

