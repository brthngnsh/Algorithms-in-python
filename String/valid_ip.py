# -*- coding: utf-8 -*-

"""
Created on Thu Jul 25 15:07:30 2019

@author: PlagueDoctor
"""

def valid_ip(s):
    #VALID_IP  is a function that can generate all valid ip addresses a given number 
    #eg :
    #input : 1234235120
    #output : ['1.23.4.235120', '1.234.235.120', '12.3.4.235120', '123.4.235.120']
    def is_valid_part(s):
        return len(s)==1 or (s != '0' and s<='255')
    #returns True if s is a single number or (
    #the value of s is <= 255 and
    #s does not have more than 1 zero (ie): s can be '0' but not '00' or '000')
    result , part = [] , [None]*4
    #part can only have 4 parts like 192.168.1.1
    for i in range(1,min(4,len(s))):
        #'i' can take values of 1 - 3 digits only
        part[0] = s[:i]
        if is_valid_part(part[0]):
            for j in range(1,min(len(s)-i,4)):
                #j takes upto 3 digits succeeding the max digit 'i' can take
                #ie j takes values from digit 4 to digit 6
                part[1] = s[i:i+j]
                if is_valid_part(part[1]):
                    for k in range(1,min(len(s)-i-j,4)):
                        part[2] , part[3] = s[i+j:i+j+k] , s[i+j+k:]
                        if is_valid_part(part[2]) and is_valid_part(part[3]):
                            result.append('.'.join(part))
                            # appending  when all parts are valid
    return result

def main():
    ip_addr = input()
    result = valid_ip(ip_addr)
    print(result)
    
if __name__ == '__main__' :
    main()