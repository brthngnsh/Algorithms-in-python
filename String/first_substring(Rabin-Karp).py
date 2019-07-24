# -*- coding: utf-8 -*-

"""
Created on Wed Jul 24 12:50:36 2019

@author: PlagueDoctor
"""

import functools

def rabin_karp(s , t) :
    if len(s) > len(t):
        return -1
    base = 26
    t_hash = functools.reduce(lambda h , c : base * h + ord(c) , t[:len(s)] , 0)
    s_hash = functools.reduce(lambda h , c : base * h + ord(c) , s , 0)
    power_of_s = base**max(len(s)-1 , 0)
    
#    print(t_hash)
#    print(s_hash)
    
    for i in range(len(s) , len(t)):
        if t_hash == s_hash and t[i-len(s) : i] == s :
            return i-len(s)
    
        t_hash -= ord(t[i - len(s)])*power_of_s 
        t_hash = t_hash * base +  ord(t[i])
        if t_hash == s_hash and t[-len(s):] == s :
            return len(t) - len(s)
    return -1
    
def main() :
    x = rabin_karp('CGC',"GACGCCA")
    if x > -1 :
        print('sub-string occurs at position :' + str(x))
    else :
        print('sub-string not present ')
        
if __name__ == '__main__' :
    main()
     