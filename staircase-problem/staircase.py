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

def leftStaircase(n):
    """Start from right"""

    for i in range(1, n+1):
        print('#'*i+' '*(n-i))

def doubleStaircase(n):
    """Print double staircase"""

    for i in range(1, n+1):
        print(' '*(n-i)+'#'*i+'#'*i+' '*(n-i))

if __name__ == '__main__':
    print("Choose the number of stairs you want: ")
    n = int(input().strip())
    leftStaircase(n)
    staircase(n)
    doubleStaircase(n)
