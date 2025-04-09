# Birthday Cake Candles

## Problem Statement
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.

Example
candles = [4, 4, 1, 3]

The tallest candles are 4 units high. There are 2 candles with this height, so the function should return 2.

Function Description

Complete the function  with the following parameter(s):

: the candle heights
Returns

: the number of candles that are tallest
Input Format

The first line contains a single integer, , the size of .
The second line contains  space-separated integers, where each integer  describes the height of .

Constraints

Sample Input 0

4
3 2 1 3
Sample Output 0

2
Explanation 0

Candle heights are . The tallest candles are  units, and there are  of them.

---

## 💡 Approach
Used a stack to track open brackets.
- When encountering a closing bracket, check if it matches the top of the stack.
- If mismatched or empty at the wrong time → invalid

---

## 🧪 Edge Cases
- All candles are of the same height → return the length of the list.
- Only one candle → return 1.
- Heights in descending or random order → still works, as we check only the max and its frequency.

---

## ⏱️ Complexity
- Time Complexity: O(n)
One pass to find the max, another to count.
- Space Complexity: O(1)
Only a few variables used.

---

## ✨ Learnings
- Use max() to easily find the largest value in a list.
- list.count(value) is a clean way to count occurrences.
- Breaking problems into small steps (find max, count max) simplifies the logic.
