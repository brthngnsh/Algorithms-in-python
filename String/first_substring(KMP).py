# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:18:36 2019

@author: PlagueDoctor
"""
def KMP( pat , text ) :
    M = len(pat)
    N = len(text)
    
    lps = [0] * M
    j = 0
    computeLPS(pat,M,lps)
    i = 0
    while i < N :
        if text[i] == pat[j] :
            j+=1
            i+=1
        if j == M :
            return i-j
            j = lps[j-1]
        elif i < N and pat[j] != text[i] :
            if j != 0 :
                j = lps[j-1]
            else :
                i += 1
def computeLPS(pat,M,lps) :
    len = 0
    lps[0]
    i = 1
    while i < M :
        if pat[i] == pat[len] :
            len+=1
            lps[i] = len
            i += 1
        else :
            if len != 0 :
                len = lps[len-1]
            else :
                lps[i] = 0
                i += 1

def main(): 
    x = KMP('CGC',"GGACGCCA")
    print('substring present at : ' + str(x))
    
if __name__ == "__main__" :
    main()