import os
import math
import sys

def two_sum_brute_force(nums, target):
    """Get the sum of numbers"""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i]+nums[j]
            if sum == target:
                return (i, j)
    return None


if __name__ == "__main__":
    nums = [2,7,10,11,15]
    target = 9

    print(two_sum_brute_force(nums, target))
