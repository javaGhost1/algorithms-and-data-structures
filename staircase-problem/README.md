# Staircase

## Problem Statement

A staircase of size `n` is built using the `#` symbol and spaces. The staircase is right-aligned, meaning that each line has increasing numbers of `#` symbols aligned to the right.

Write a function that prints a staircase of height `n`.

Each line should consist of spaces followed by `#` symbols, such that the last line contains `n` hashes and the first line contains only one.

---

## Constraints

- 1 ≤ n ≤ 100

---

## Solution

### Edge Cases

- **n = 1**: Should print just one `#` with no leading spaces.
- **n = 0**: Should print nothing.
- **n = 100**: Should efficiently print a staircase without performance degradation or misalignment.

---

### Approach

We iterate from `1` to `n`, and for each level:
- Print `(n - i)` spaces
- Followed by `i` `#` symbols

This ensures the staircase is right-aligned, with the correct amount of spacing and hashes per line.

---

### Explanation

For `n = 6`, the output will be:

Each line `i` contains:
- `n - i` spaces
- `i` hashes

---

### Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1) — aside from print output, no additional space is used.

---

> *"Every step upward is progress — one hash at a time."*

**— javaGhost1**
