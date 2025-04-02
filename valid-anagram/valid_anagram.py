

def v_anagram(s, t):
    """anagram logic"""
    if len(s) != len(t):
        return False # Check if the number of char is the same
    # store values of each and check
    chars = {}
    # check if each char is in the other string
    for char in s:
        chars[char] = chars.get(char, 0)+1
    for char in t:
        chars[char] = chars.get(char, 0)-1
    for value in chars.values():
        if value != 0:
            return False
    return True
     

if __name__ == "__main__":
    s = "listen"
    t = "silent" 
    print(v_anagram(s, t))
    s = "rat" 
    t = "car"  
    print(v_anagram(s, t))
    s = "hello" 
    t = "ollhe" 
    print(v_anagram(s, t))
