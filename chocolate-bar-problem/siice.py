import math

def chocolate(s, d, m):
    # initialise count
    count = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count
s = [1, 2, 1, 3, 2] 
d = 3             
m = 2   

result = chocolate(s, d, m)
print(result)