# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:13:34 2019

@author: PlagueDoctor
"""

def pascal_triangle(n):
    result = [[1] * (i+1) for i in range(n)]
    #forms the pattern [1],[1,1],[1,1,1],[1,1,1,1],...n times
    for i in range(n):
        for j in range(1,i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
            #sums up imediate upper left and right elements of the current elements
            #eg:
            #         1
            #       1   1
            #      1  2  1
            #here 2 is got by adding upper left(i-1,j-1) and its upper right(i-1,j) elements
            
    return result
def main():
    n = int(input())
    result = pascal_triangle(n)
    print(result)

if __name__ == '__main__' :
    main()