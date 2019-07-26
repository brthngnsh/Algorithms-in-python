# -*- coding: utf-8 -*-

"""
Created on Thu Jul 26 23:19:38 2019

@author: PlagueDoctor
"""

def run_length_decoding(s) :
    #this function is used to decode the compressed string form from run_length_encoding()
    count , result = 0 , []
    for c in s :
        if c.isdigit() :
            count = count * 10 + int(c)
        else :
            result.append(count*c)
            count = 0
        
    return ''.join(result)

def run_length_encoding(s):
    #string compression takes places in this function
    #eg:
    #string = aaaabbca
    #encoded value = 4a2b1c1a
    result , count = [] , 1
    for i in range(1,len(s) + 1) :
        if i==len(s) or s[i] != s[i-1] :
            #i==len(s) => final caharacter is reached
            #s[i] ! s[i-1] => change of character
            result.append(str(count)+s[i-1])
            count = 1 # count is refreshed for next character
        else : # Both elements are the same
            count+=1
    return ''.join(result)

def main():
    string = input()
    print('Encoding....')
    string = run_length_encoding(string)
    print('string : ' + string)
    print('decoding...')
    string = run_length_decoding(string)
    print('string : '+ string)
    
if __name__ == '__main__' :
    main()
    