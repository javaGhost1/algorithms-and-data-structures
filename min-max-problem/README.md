#  Mini-Max Sum

## Problem Description

Given **five positive integers**, find the **minimum** and **maximum** values that can be calculated by summing exactly **four of the five integers**. Then, print the respective **minimum** and **maximum** values as a single line of **two space-separated integers**.

---

## Problem Statement

You are given an array of 5 integers. Your task is to:

- Calculate the **minimum sum** of 4 out of the 5 integers.
- Calculate the **maximum sum** of 4 out of the 5 integers.
- Print both values on a single line, separated by a space.

> **Important**: Since the input values can be large, be sure to use a data type that supports **64-bit integers** (e.g., `long` in Java/C++, or `int` in Python).

---

## Example

### Sample Input
1 2 3 4 5

### Sample output
10 14

### Explanation:
From the input `[1, 2, 3, 4, 5]`, the following 4-element sums are possible:
- Exclude 5 → 1 + 2 + 3 + 4 = **10**
- Exclude 4 → 1 + 2 + 3 + 5 = **11**
- Exclude 3 → 1 + 2 + 4 + 5 = **12**
- Exclude 2 → 1 + 3 + 4 + 5 = **13**
- Exclude 1 → 2 + 3 + 4 + 5 = **14**

The **minimum sum** is `10`, and the **maximum sum** is `14`.

---
## Time Complexity
Time: O(n) 
— one pass to compute sum, and one to get min and max

Space: O(1)

javaGhost1 | @javaGhost1