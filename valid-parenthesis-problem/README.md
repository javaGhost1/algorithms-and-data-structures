# Valid Parentheses

## Problem Statement
# Valid Parentheses
Given a string s containing just the
characters '(' , ')' , '{' , '}' , '[' and ']' ,
determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same
type of brackets.
2. Open brackets must be closed in the correct
order.
Example 1:
Input: s = "()"
Output: valid
Example 2:
Input: s = "()[]{}"
Output: valid

Example 3:
Input: s = "(]"
Output: invalid
Example 4:
Input: s = "([)]"
Output: invalid

---

## Approach
Used a stack to track open brackets.
- When encountering a closing bracket, check if it matches the top of the stack.
- If mismatched or empty at the wrong time → invalid

---

## Edge Cases
- Empty string → Valid
- Only closing bracket → Invalid
- Nested incorrectly → Invalid

---

## Complexity
- Time: O(n)
- Space: O(n)

---

## Learnings
- Stack is perfect for “nested” or “reverse order” problems
