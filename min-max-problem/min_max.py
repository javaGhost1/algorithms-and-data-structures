#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()

    # get the total sum
    total_sum = sum(arr)

    # get min element
    min_element = min(arr)
    # get max element
    max_element = max(arr)

    # max sum
    max_sum = total_sum - min_element
    # min sum
    min_sum = total_sum - max_element
    

    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
