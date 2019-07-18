"""
Created on Mon Jun  3 14:32:48 2019

@author: PlagueDoctor
"""
def closestbit(x):
    TOTAL_BITS = 64
    for i in range(TOTAL_BITS - 1):
        if(x >> i) & 1 != (x >> (i+1)) & 1 :
            x ^= (1 << i) | (1 << (i+1))
            #SWAPPING iTH AND (i+1)TH BIT
            return x
    raise ValueError("All bits are 0 or 1")


#TEST CASE
x = 7
y = closestbit(x)
print(y)

#OUTPUT : 11