# -*- coding: utf-8 -*-


"""
Created on Tue Jul 23 19:39:54 2019

@author: PlagueDoctor
"""

import itertools

 
def look_and_say(n):
    #input : integer n 
    #complexity : O(n(2^n))
    def next_number(s):
        i = 0
        result = []
        while i < len(s):
            count = 1
            while (i + 1) < len(s) and s[i] == s[i+1] :
                i+=1
                count += 1
                #count variable counts the number of times a digit appears contiuously
            result.append(str(count)  + s[i])#appending count and the digit counted
            i+=1
        return ''.join(result)
    s = '1'
    for _ in range(1,n):
        s = next_number(s)
    return s

def alt_look_and_say(n):
    #uses itertools
    s = '1'
    for _ in range(1,n):
        s = ''.join(str(len(list(group))) + key for key,group in itertools.groupby(s))
    return s

def main():
    number = int(input())
    result1 = look_and_say(number)
    result2 = alt_look_and_say(number)
    print('result 1 : ' + result1)
    print('result 2 : ' + result2)

if __name__ == '__main__' :
    main()