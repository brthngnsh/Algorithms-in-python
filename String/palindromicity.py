# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:22:45 2019

@author: PlagueDoctor
"""

def ispalindrome(string):
    i, j = 0, len(string) - 1
    while i<j:
        while not string[i].isalnum() and i<j:
            i+=1
        while not string[j].isalnum() and i<j:
            j-=1
        if string[i] != string[j]:
            return False
        i, j = i+1 , j-1
        
    return True

def main():
    string = input()
    result = ispalindrome(string)
    print(result)

if __name__ == '__main__' :
    main()