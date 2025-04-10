Here's `breakingRecords` problem:

---

# Problem Title: Breaking Records

## Problem Statement

Maria plays a game where she tracks her scores in a series of games. After each game, she compares her current score to her highest and lowest scores ever. She keeps a record of how many times she breaks her highest and lowest scores during the series.

Your task is to write a function that receives a list of Maria’s scores and returns the number of times she breaks her highest and lowest scores. The function should return the total number of times she breaks the highest and the lowest records.

## Input Format

- The first line contains a single integer `n`, denoting the number of games.
- The second line contains `n` space-separated integers, where each integer represents the score for a particular game.

## Output Format

- The function should return two space-separated integers on a single line:
  - The first integer is the number of times she broke her highest score.
  - The second integer is the number of times she broke her lowest score.

## Constraints

- The number of games `n` will be between 1 and 1000.
- The scores will be positive integers.

## Sample Input

```
9
10 5 20 20 4 5 2 25 1
```

## Sample Output

```
2 4
```

### Explanation

For the input above, the series of scores is:
`[10, 5, 20, 20, 4, 5, 2, 25, 1]`.

- Maria starts with a score of 10.
- Her first score of 5 does not break any records.
- Her score of 20 breaks the highest record (10), so the best count increases to 1.
- The score of 20 doesn't break any records.
- Her score of 4 breaks the lowest record (5), so the worst count increases to 1.
- The score of 5 doesn't break any records.
- The score of 2 breaks the lowest record (4), so the worst count increases to 2.
- The score of 25 breaks the highest record (20), so the best count increases to 2.
- The score of 1 breaks the lowest record (2), so the worst count increases to 3.

Thus, the final output is `2 4` because Maria broke her highest score 2 times and her lowest score 4 times.

## Approach

### Step-by-Step Plan:

1. **Initial Setup**:
   - Start by initializing `high` and `low` to the first score in the series.
   - Initialize counters `best` and `worst` to 0, which will keep track of how many times Maria breaks her highest and lowest scores.

2. **Iterate through Scores**:
   - For each subsequent score in the list:
     - If the score is greater than `high`, update `high` and increment the `best` counter.
     - If the score is less than `low`, update `low` and increment the `worst` counter.

3. **Return the Results**:
   - After processing all scores, return the `best` and `worst` counters as a space-separated string.

### Edge Cases:
- A list with only one score (no record-breaking possible).
- All scores are the same (no record-breaking).
- The scores increase or decrease monotonically.

## Solution Explanation

The function first initializes `high` and `low` to the first score. Then, it loops through the rest of the scores and checks if each score either breaks the high record or the low record. If it does, it updates the `high` or `low` values and increments the respective counters.

### Time Complexity:
- **O(n)**: The function iterates through the list of scores once, where `n` is the number of scores. The time complexity is linear because the operation inside the loop is constant time.

### Space Complexity:
- **O(1)**: The function uses a constant amount of extra space regardless of the input size.


## Author:
Freeman

---

