# 🧩 Valid Parentheses

## 🧠 Problem Statement
Given a string containing just the characters `()[]{}`, check if the string is valid.
A string is valid if:
- Every open bracket is closed by the same type
- They are closed in the correct order

### ✅ Example
Input: `"()[]{}"`  
Output: `"Valid"`

---

## 💡 Approach
Used a stack to track open brackets.
- When encountering a closing bracket, check if it matches the top of the stack.
- If mismatched or empty at the wrong time → invalid

---

## 🧪 Edge Cases
- Empty string → Valid
- Only closing bracket → Invalid
- Nested incorrectly → Invalid

---

## ⏱️ Complexity
- Time: O(n)
- Space: O(n)

---

## ✨ Learnings
- Stack is perfect for “nested” or “reverse order” problems
