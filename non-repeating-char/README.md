# Check First Non-Repeating Character

## Problem Statement

Given a string `chars`, return the first character that does **not** repeat. If every character repeats or the string is empty, return `None`.

---

## Constraints

- The input is a lowercase string consisting of only alphabetic characters.
- 1 ≤ |chars| ≤ 10⁵
- Return the **first** non-repeating character, not all.

---

## Solution

### Edge Cases

- `"aabb"` → All characters repeat, so output should be `None`.
- `"leetcode"` → Output should be `'l'` because it's the first unique character.
- `"loveleetcode"` → Output should be `'v'`.
- Empty string `""` → Should return `None`.

---

### Approach

1. **Count Occurrences**:
   - Traverse the string once to build a dictionary `checked` that stores the count of each character.

2. **Identify the First Unique**:
   - Traverse the string again using `enumerate` to find the first character whose count in the dictionary is `1`.

3. Return that character. If none is found, return `None`.

---

### Explanation

- The code uses a dictionary to efficiently store character frequencies.
- Then it checks, in order, which character has a frequency of `1`.

Example:

```python
Input: "loveleetcode"
Checked Dictionary: {'l': 1, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}
Output: 'v'

## Complexity
- Time Complexity: O(n), where n is the length of the input string.

- Space Complexity: O(1), assuming the character set is limited to lowercase English letters (max 26 entries in the dictionary).

> *"In a noisy world, uniqueness speaks the loudest."*

**— javaGhost1**
