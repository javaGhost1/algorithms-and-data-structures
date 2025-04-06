

def breakingRecords(scores):
    # initialise the scores
    high = low = scores[0]
    best = worst = 0

    for score in scores[1:]:
        # check for high score
        if score > high:
            high = score
            best += 1
        if score < low:
            low = score
            worst += 1
    return f"{best} {worst}"

# Sample input
n = 9
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

# Output
result = breakingRecords(scores)
print(result)  # Output: [2, 4]
