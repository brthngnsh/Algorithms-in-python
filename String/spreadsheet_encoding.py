# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:44:34 2019

@author: PlagueDoctor
"""

import functools
def spreadsheet_col_decode(col):
    #col is the spreadsheet column in upper case
    return functools.reduce(lambda result, c : result * 26 + ord(c) - ord('A') + 1,col,0)

def main():
    column = input()
    column = column.upper()
    num = spreadsheet_col_decode(column)
    print(num)
    
if __name__ == "__main__" :
    main()
    