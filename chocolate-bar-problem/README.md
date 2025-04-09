# Chocolate Bar Problem

## Problem Statement

Sam loves chocolate. He goes to a store with some money, and he is allowed to buy chocolate bars for a certain price. After eating one chocolate, he can get an additional chocolate bar by returning some wrappers. The task is to determine how many chocolates Sam can eat, given the amount of money he has, the price of a single chocolate, and the number of wrappers needed for a free chocolate bar.

You are given the following:
- A list of integers representing the prices of the chocolate bars.
- An integer `d`, representing the total money Sam has.
- An integer `m`, representing the number of chocolate bars he can buy at once.

Return the total number of chocolates Sam can eat.

---

## Constraints

- 1 ≤ s ≤ 10^5
- 1 ≤ d ≤ 10^5
- 1 ≤ m ≤ 10^5
- The list `s` will contain integers that represent the prices of each chocolate bar.

---

## Solution

### Edge Cases

- If Sam has no money (`d = 0`), the result will be `0`.
- If there are fewer chocolates than `m`, no chocolate can be bought at once.
- If the number of wrappers doesn't suffice for extra chocolates, only a basic chocolate count will be returned.

---

### Approach

1. **Iterate through the list**: Loop through the list of prices and calculate the total chocolates that can be bought given the amount of money (`d`).
2. **Check for Wrappers**: After each chocolate purchase, check if Sam can use wrappers for a free chocolate, and add to the count.
3. **Edge Handling**: Ensure that negative or impossible conditions (like not enough money or wrappers) are handled properly.

## Explanation
Given a list of prices **[1, 2, 1, 3, 2]**, total money 3, and m = 2 (indicating Sam buys 2 chocolates at once), the function calculates how many combinations of the 2 chocolates **sum** up to the available money.

For example:
s = [1, 2, 1, 3, 2] 
d = 3             
m = 2   

result = chocolate(s, d, m)
print(result) # Output: 2

In the case above, there are two possible combinations of two chocolates that sum up to 3:

Chocolates at indices 0 and 1 (prices 1 + 2)

Chocolates at indices 2 and 3 (prices 1 + 2)

## Complexity
- Time Complexity: O(n * m) → We loop through the list and check sums of sublists of size m.

- Space Complexity: O(1) → The function uses a constant amount of extra space.

>*"Life is like a chocolate bar, enjoy every bit of it."*

**javaGhost1**