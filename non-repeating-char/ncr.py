

def check_repeats(chars):
    """check for non repeating characters"""
    checked = {}
    #count occurences of characters
    for char in chars:
        checked[char] = checked.get(char, 0)+1
        #code above is short for
        # if char in checked:
        #     checked[char] += 1
        # else:
        #     checked[char] = 1
    print(checked)
    for i, char in enumerate(chars):
        if checked[char] == 1:
            return char
    return None

if __name__ == "__main__":
    print(check_repeats("leetcode"))     
    print(check_repeats("loveleetcode"))  
    print(check_repeats("aabb"))         
