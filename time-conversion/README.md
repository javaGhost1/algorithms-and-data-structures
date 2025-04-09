# Time Conversion

## Problem Statement

Given a time in 12-hour AM/PM format, convert it to 24-hour military time.

- The input string is in the format `hh:mm:ssAM` or `hh:mm:ssPM`.
- Your function should return the string in 24-hour format: `HH:MM:SS`.

---

## Constraints

- The input will always be a valid time in the 12-hour format.
- 01 ≤ hh ≤ 12
- 00 ≤ mm, ss ≤ 59
- The input string will always end with `AM` or `PM`.
- Leading zeroes will be present for single-digit hours, minutes, or seconds.

---

## Solution

### Edge Cases

- `"12:00:00AM"` → Midnight → Should return `"00:00:00"`
- `"12:00:00PM"` → Noon → Should return `"12:00:00"`
- `"01:00:00PM"` → Afternoon → Should return `"13:00:00"`
- `"01:00:00AM"` → Early Morning → Should return `"01:00:00"`

---

### Approach

1. **Extract Time Parts**:
   - Use slicing and `split(':')` to separate hours, minutes, and seconds with the period (`AM`/`PM`).

2. **Convert Hour Component**:
   - If the time is `"AM"` and the hour is `12`, convert it to `"00"`.
   - If the time is `"PM"` and the hour is not `12`, add 12 to the hour.

3. **Format and Return**:
   - Return the converted string in `HH:MM:SS` 24-hour format using Python's formatted string feature.

---

### Explanation

Given `"07:05:45PM"`:
- The hour is `7`, and since it's `PM`, add 12 → `19`.
- Final result: `"19:05:45"`

```python
Input: "12:01:00AM"
Output: "00:01:00"

Input: "07:05:45PM"
Output: "19:05:45"

## Complexity
- Time Complexity: O(1) → Fixed-length input string.

- Space Complexity: O(1)

> *"Precision in time is the first sign of discipline."*

— javaGhost1