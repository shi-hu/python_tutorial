#!/bin/python3

import math
import os
import random
import re
import sys

def decimalToBinary(n):
    return bin(n).replace('0b','')
    

def countOnes(n):
    binary = []
    count = 0
    for i in range(len(n)):
        if int(n[i]) == 1:
            count+=1
        elif int(n[i]) == 0:
            binary.append(count)
            count = 0
        
    binary.append(count)
    return max(binary)
             

if __name__ == '__main__':
    n = int(input())
    bin_n = decimalToBinary(n)
    max_count = countOnes(bin_n)
    print(max_count)

    
    
