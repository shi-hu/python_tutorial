# Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

phoneBook = {}

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        key, value = input().rstrip().split(' ')
        phoneBook[key] = value
    while True:
        try:
            query = input()
            if (query in  phoneBook) == False:
                print("Not found")
            elif (query in phoneBook) == True:
                print('{}={}'.format(query, phoneBook[query]))
        except EOFError as e:
            print(end="")
            break
        
