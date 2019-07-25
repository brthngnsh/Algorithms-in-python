# -*- coding: utf-8 -*-

"""
Created on Thu Jul 25 15:29:30 2019

@author: PlagueDoctor
"""

def string_in_sinewave(s) :
    #this function prints the string in a sinewave form
    #ist line has 1,5,9,...
    #2nd line has 0,2,4,....
    #3rd line has 3,7,11,...
    #eg : 
    #input : taskmaster
    #output : aartsmsekt
    
    #Waveform :
    #
    #    a                  a                r
    # t      s         m        s        e
    #             k                 t
    #
    return s[1::4] + s[::2] + s[3::4]

def main():
    string = input()
    result = string_in_sinewave(string)
    print(result)
    
if __name__ == '__main__' :
    main()
    