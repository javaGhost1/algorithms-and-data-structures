# 🎂 Birthday Chocolate (Subarray Division)

## Problem Description

Given a list of integers representing pieces of chocolate, and two integers `d` and `m` representing Ron's birth day and birth month respectively, determine how many ways the chocolate can be divided into `m` contiguous pieces such that the sum of those pieces is equal to `d`.

This is a classic problem known as **Subarray Division**.

---

## 🧠 Problem Statement

You are given an array of integers `s`, and two integers:
- `d`: the day of the month (target sum)
- `m`: the month (number of elements in subarray)

You must count how many contiguous subarrays of length `m` sum up to `d`.

---

## 🧪 Example

### Input:
```python
s = [1, 2, 1, 3, 2]
d = 3
m = 2
