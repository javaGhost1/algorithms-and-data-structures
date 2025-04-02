
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
        # update character count
        char_map[s[right]] = 
        # update max_freq






s = "AABABBA"
k = 1
print(character_replacement(s, k))
s = "ABAB"
k = 2
print(character_replacement(s, k))


