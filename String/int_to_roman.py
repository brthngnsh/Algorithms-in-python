# -*- coding: utf-8 -*-

"""
Created on Thu Jul 25 15:58:30 2019

@author: PlagueDoctor
"""

def int_to_roman(s) :
    roman = {'M':1000 , 'CM':900 ,'D':500 ,'CD':400 ,'C':100 ,'XD':90 , 'L':50 , 'XL':40 , 'X':10 , 'IX':9 , 'V':5 ,'IV':4,'I':1}
    i = 0
    key = list(roman.keys())
    val = list(roman.values())
    symbol = ''
    while s>0 :
        for _ in range(s//val[i]):
            symbol+=(key[i])
            s-=val[i]
        i+=1
    
    return symbol

def main():
    inte = int(input())
    sym = int_to_roman(inte)
    print(sym)
    
if __name__ == "__main__" :
    main()