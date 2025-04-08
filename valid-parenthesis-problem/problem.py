
def isValid(s: str) -> bool:
    """Check for valid parenthesis"""
    stack = []
    # set matches
    matching = {")":"(","}":"{","]":"["}

    for char in s:
        # check if char is valid
        if char in matching.values():
            stack.append(char) #add the char to stack
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                # check if stack is empty and if it's a match
                return False
            stack.pop() # remove the pair
        else:
            # other characters don't apply
            return False

    return not stack #stack should not be empty

print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("{[]}"))      # True