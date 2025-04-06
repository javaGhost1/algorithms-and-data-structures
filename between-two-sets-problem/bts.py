import math
from functools import reduce
def lcm(a, b):
    return abs(a*b)//math.gcd(a, b)

def getTotalX(a, b):
    # step1: find lcm of all elments in a
    lcm_a = reduce(math.lcm, a)
    # step2: find the gcd of all the elements in b
    gcd_b = reduce(math.gcd, b)
    # step 3: count how many multiples of lcm_a divided by gcd_b are there
    count = 0
    m = lcm_a
    while m <= gcd_b:
        if gcd_b % m == 0:
            count += 1
        m += lcm_a

    return(count)

a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a, b)) 