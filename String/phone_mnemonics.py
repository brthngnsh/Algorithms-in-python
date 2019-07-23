# -*- coding: utf-8 -*-

"""
Created on Mon Jul 23 19:08:45 2019

@author: PlagueDoctor
"""

MAPPING = ['0' , '1' , 'ABC' , 'DEF' , 'GHI' , 'JKL' , 'MNO' , 'PQRS' , 'TUV' , 'WXYZ']
#MAPPING is a hash table 

def phone_mnemonics(phone_no):
    #this program generates all possible mnemonics for the given number
    def phone_mnemonics_helper(digit):
        if digit == len(phone_no):
            mnemonics.append(''.join(partial_mnemonics))
            #if digit == len(phone_no) the 'digit' is the last number in the phone_no
        else :
            for c in MAPPING[int(phone_no[digit])]:
                #c tries for all combos in MAPPING for 'digit'
                partial_mnemonics[digit] = c
                phone_mnemonics_helper(digit+1)
                #recursion follow-up
    mnemonics , partial_mnemonics = [] , [0] * len(phone_no)
    phone_mnemonics_helper(0)
    #first recursion loop starts here
    return mnemonics

def main():
    phone_no = input()
    print(phone_mnemonics(phone_no))
    
if __name__ == '__main__' :
    main()

