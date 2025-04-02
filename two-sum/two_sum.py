

def two_sum(nums, target):
    """We implement hashmaps"""

    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return(seen[complement], i)
        seen[num] = i
    return None

# Test
nums = [2, 7, 10, 11, 15]
target = 9
print(two_sum(nums, target)) 