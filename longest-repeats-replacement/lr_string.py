
def character_replacement(s: str, k: int):
    """find longest string with replacements"""
    # hashmap
    char_map={}
    # setup pointers
    left = 0
    max_freq=0
    # setup a max
    max_len=0
    # track using right
    for right in range(len(s)):
        # update character count use get
        char_map[s[right]] = char_map.get[s[right], 0]+1
        # update max_freq
        max_freq = max(max_freq, char_map[s[right]])
        # Check if we need more than k replacements
        if (right-left+1) - max_freq > k:
            # Remove the leftmost character from the window
            char_map[s[left]] -= 1
            left += 1 # Shrink the window
        # update mx length
        max_len = max(max_len, right-left+1)
    return max_len


s = "AABABBA"
k = 1
print(character_replacement(s, k))
s = "ABAB"
k = 2
print(character_replacement(s, k))


