
def migratoryBirds(arr):
    # setup hash map
    count_birds = {}
    # initialise max fcount
    max_freq = 0

    for bird in range(len(arr)):
        # update bird count
        count_birds[arr[bird]] = count_birds.get(arr[bird], 0)+1
        # find most repeated
        max_freq = max(max_freq, count_birds[arr[bird]])

        # find smallest repeats
    result = min(count for count in count_birds if count_birds[count] == max_freq)
    return result

arr = [1, 4, 4, 4, 5, 3]
arr2 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
print(migratoryBirds(arr2))