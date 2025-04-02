

def longest_substring(s):
    """check for longest substring"""
    # hasmap
    char_map = {}
    # set up the window pointers
    left = 0
    right = 0
    # track longest substring
    max_len = 0

    for right in range(len(s)):
        # check for duplicates
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1 # move left
        char_map[s[right]] = right #update right
        # update max length
        max_len = max(max_len, right-left+1)
    
    return max_len

# Example usage:
print(longest_substring("abcabcbb"))  # Output: 3 (substring "abc")
print(longest_substring("bbbbb"))  # Output: 1 (substring "b")
print(longest_substring("pwwkew"))  # Output: 3 (substring "wke")