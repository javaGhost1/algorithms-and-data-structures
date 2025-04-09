# Grading Students

## Problem Description

HackerLand University has a grading policy where:

- Every student receives a grade between **0** and **100**.
- Any grade **less than 38** is considered **failing**.
- If the grade is **38 or more**:
  - Round it **up to the next multiple of 5** **only if** the difference is **less than 3**.
  - Otherwise, **leave it as is**.

## Objective

Write a function that takes in a list of student grades and applies the rounding rules above. Return the new list of grades.

---

## Sample Input
4 73 67 38 33


## Sample Output
75 67 40 33


## Explanation

- **73** → next multiple of 5 is **75** → difference = 2 → round → **75**
- **67** → next multiple of 5 is **70** → difference = 3 → don’t round → **67**
- **38** → next multiple of 5 is **40** → difference = 2 → round → **40**
- **33** → less than 38 → don’t round → **33**

---
## Time and Space Complexity
- Time Complexity: O(n) — loop through all grades once

- Space Complexity: O(n) — store adjusted results in a new list


## Edge Cases

- Grades **exactly on a multiple of 5** → no rounding (e.g., 80 → 80)
- Grades **within 2 of a multiple of 5** and **≥ 38** → round up (e.g., 39 → 40)
- Grades **< 38** → never round
- Grade is **already a multiple of 5** (e.g., 85 → 85)
- All grades are **failing** → no rounding should occur

---

## Function Signature

```python
def gradingStudents(grades: List[int]) -> List[int]:
    ...


code by javaGhost1 | @havaGhost1