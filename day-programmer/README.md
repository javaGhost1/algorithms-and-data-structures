# Day of the Programmer - Solution

## Problem Statement

In the year 1700, Russia used the Julian calendar, but in 1918, they switched to the Gregorian calendar. The **Day of the Programmer** refers to the 256th day of the year, which falls on **12th September** for leap years and **13th September** for non-leap years. However, the year **1918** was an exceptional case where the switch from the Julian to the Gregorian calendar caused the 256th day to fall on **26th September**.

Given a year `Y`, the task is to determine the **Day of the Programmer** for that year, considering the different calendar systems and leap year rules.

### Input Format

- A single integer `year` representing the year for which we need to determine the **Day of the Programmer**.

### Output Format

- Print the date of the **Day of the Programmer** in the format `DD.MM.YYYY`.

### Constraints

- 1700 ≤ `year` ≤ 2700

### Example Input

```python
2017
```

### Example Output

```python
13.09.2017
```

### Explanation

In the year **2017**, the 256th day of the year falls on **13th September**, as it is not a leap year.

---

## Solution

### Approach

To calculate the **Day of the Programmer**:
1. For **year 1918**, the day is fixed as **26.09.1918** due to the change in the calendar system.
2. For **years before 1918** (Julian calendar), the year is a leap year if it is divisible by 4.
3. For **years after 1918** (Gregorian calendar), the year is a leap year if:
   - It is divisible by 400, or
   - It is divisible by 4 but not divisible by 100.
4. If the year is a leap year, the 256th day is **12th September**. Otherwise, it is **13th September**.

    
# Test cases
print(dayOfProgrammer(2017))  # Output: 13.09.2017
print(dayOfProgrammer(2020))  # Output: 12.09.2020
print(dayOfProgrammer(1900))  # Output: 13.09.1900 (not a leap year, divisible by 100 but not 400)
print(dayOfProgrammer(1918))  # Output: 26.09.1918 (special case)
```

### Edge Cases

1. **Year 1918**: This year has a special rule due to the transition between the Julian and Gregorian calendars, and the 256th day falls on **26th September**.
2. **Leap years**: The function correctly identifies leap years based on both the Julian and Gregorian calendars.
   - **Julian leap year**: A year divisible by 4 before 1918.
   - **Gregorian leap year**: A year divisible by 400, or divisible by 4 but not 100, after 1918.
3. **Non-leap years**: For non-leap years, the 256th day falls on **13th September**.

### Time Complexity

- The time complexity is **O(1)** as the solution only involves basic arithmetic checks, making it a constant-time operation.

---

## Quote

_"Programming is like solving a puzzle, each problem presenting new opportunities for creativity."_  
**— javaGhost1**

---
