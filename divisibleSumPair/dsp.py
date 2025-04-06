import math

def divisibleSumPairs(n, ar, k):
    # initialize a count
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i]+ar[j]) % k == 0:
                count += 1
    
    return count

n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
result = divisibleSumPairs(n, ar, k)
print(result)