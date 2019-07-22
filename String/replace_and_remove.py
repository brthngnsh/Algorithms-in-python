# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:34:34 2019

@author: PlagueDoctor
"""

#input : string , size 
#relace 'a' with 'dd'
#remove 'b'

def replace_and_remove(string,s):
    #forward traverse : remove all 'b'
    write_index , a_count = 0, 0
    for i in range(s):
        if string[i] == 'a':
            a_count += 1
        if string[i] != 'b':
            string[write_index] = string[i]
            write_index+=1
    #Backward traverse : converting 'a' to 'dd'
    cur_index = write_index - 1
    write_index+=a_count - 1
    final_size = write_index + 1
    while cur_index >= 0 :
        if string[cur_index] == 'a' :
            string[write_index-1:write_index+1] = 'dd'
            write_index-=2
        else :
            string[write_index] = string[cur_index]
            write_index-=1
        cur_index-=1
    return string,final_size

def main():
    string = input()
    #enter string as list elements
    s=int(input())
    string = string.split()
    string,s = replace_and_remove(string,s)
    print(string,s)
        
    
if __name__ == '__main__' :
    main()
    