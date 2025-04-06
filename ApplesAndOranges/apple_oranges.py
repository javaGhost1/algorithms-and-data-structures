

def CountApplesAndOranges(s, t, a, b, apples, oranges):
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


first_multiple_input = input().rstrip().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))