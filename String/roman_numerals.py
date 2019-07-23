# -*- coding: utf-8 -*-

"""
Created on Tue Jul 23 22:00:18 2019

@author: PlagueDoctor
"""
import functools
def Roman_to_decimal(s):
    #input should be a correct roman numeral or it must be check for the 6 exceptions
    t = {'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000}
    return functools.reduce(lambda val , i : val + (-t[s[i]] if t[s[i]] < t[s[i+1]] else t[s[i]]), reversed(range(len(s)-1)) , t[s[-1]])
    
def main():
    roman = input()
    result = Roman_to_decimal(roman)
    print(result)
    
if __name__ == '__main__' :
    main()
    