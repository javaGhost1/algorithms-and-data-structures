# Problem Title: Get Total X

## Problem Statement

Given two lists of integers `a` and `b`, you need to find how many integers `x` exist such that:
- Each element of `a` divides `x`.
- `x` divides each element of `b`.

In other words, you need to find the number of integers `x` that satisfy the conditions:
- `x` is a multiple of the Least Common Multiple (LCM) of all elements in list `a`.
- `x` divides the Greatest Common Divisor (GCD) of all elements in list `b`.

## Constraints
- The number of elements in the lists `a` and `b` will be between 1 and 1000.
- Each integer in the lists `a` and `b` will be between 1 and 1000, inclusive.

## Input Format

- The first line contains two space-separated integers `n` and `m` — the number of elements in list `a` and list `b` respectively.
- The second line contains `n` space-separated integers, the elements of list `a`.
- The third line contains `m` space-separated integers, the elements of list `b`.

## Output Format

Print the total number of integers `x` that satisfy the conditions described above.

## Example

### Sample Input

```
2 3
2 4
16 32 96
```

### Sample Output

```
3
```

### Explanation:
For the input above:
- The LCM of elements in `a = [2, 4]` is 4.
- The GCD of elements in `b = [16, 32, 96]` is 16.
- The numbers that are multiples of 4 and divide 16 are: `4, 8, 12, 16`. There are 3 numbers that satisfy the conditions: `4, 8, 16`.

Thus, the output is `3`.

## Approach

### Step-by-Step Plan:

1. **LCM Calculation**: 
   - First, compute the LCM (Least Common Multiple) of all elements in list `a`. This is done by applying the LCM formula iteratively on all elements of `a`.
   
2. **GCD Calculation**: 
   - Next, compute the GCD (Greatest Common Divisor) of all elements in list `b`.

3. **Counting Valid Multiples**: 
   - Iterate over all multiples of the LCM computed in step 1, up to the GCD calculated in step 2.
   - Check if each multiple divides the GCD. If so, it's a valid value for `x`.
   
4. **Return the Count**: 
   - Return the total count of valid `x` values.

### Edge Cases:
- If the LCM of list `a` exceeds the GCD of list `b`, the output will be 0.
- Lists with minimum length (only 1 element in each).
- Large numbers in `a` or `b` may test the algorithm's efficiency.

## Solution Explanation

1. **LCM and GCD Functions**:
   - We use `reduce` to apply the `lcm` and `gcd` functions across the lists `a` and `b`. This ensures that we calculate the LCM and GCD for multiple elements, not just pairs.

2. **Valid Multiples**:
   - The key observation is that any number `x` that satisfies the conditions must be a multiple of `LCM(a)` and divide `GCD(b)`.

3. **Iterating Efficiently**:
   - We iterate through the multiples of `LCM(a)` starting from `LCM(a)` itself, checking each multiple up to `GCD(b)`. If it divides `GCD(b)`, we increment the count.

### Time Complexity:

- **LCM Calculation**: The time complexity for computing the LCM of two numbers is `O(log(max(a, b)))`. For multiple elements, using `reduce`, it becomes `O(n * log(max(a)))`, where `n` is the length of list `a`.
  
- **GCD Calculation**: Similarly, computing the GCD of multiple elements in list `b` using `reduce` takes `O(m * log(max(b)))`, where `m` is the length of list `b`.

- **Counting Valid Multiples**: The loop runs for `gcd_b / lcm_a` iterations, which is a manageable number in most cases.

Thus, the overall complexity is `O(n * log(max(a))) + O(m * log(max(b))) + O(gcd_b / lcm_a)`.

## Code

```python
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def getTotalX(a, b):
    # Step 1: Find LCM of all elements in a
    lcm_a = reduce(lcm, a)
    
    # Step 2: Find GCD of all elements in b
    gcd_b = reduce(math.gcd, b)
    
    # Step 3: Count how many multiples of lcm_a divide gcd_b
    count = 0
    m = lcm_a
    while m <= gcd_b:
        if gcd_b % m == 0:
            count += 1
        m += lcm_a  # Increment by lcm_a to check the next multiple
    
    return count

# Test the function
a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a, b))  # Output should be 3
```

## Author:
Freeman

---
