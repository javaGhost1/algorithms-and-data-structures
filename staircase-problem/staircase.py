import math
import os
import random
import re
import sys

def staircase(n):
    """ Draw the staircase using #"""
    
    for i in range(1, n+1):
        #add spaces and #
        print(' '*(n-i)+'#'*i)



if __name__ == '__main__':
    print("Choose the number of stairs you want: ")
    n = int(input().strip())
    staircase(n)
