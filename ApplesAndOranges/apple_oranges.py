

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    for d in apples:
        # check if it flls on house
        if s<=a+d<=t:
            apple_count += 1
    
    oranges_count = 0
    for d in oranges:
        # check if orange lands on house
        if s<=b+d<=t:
            oranges_count += 1

    print(apple_count)
    print(oranges_count)


s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)