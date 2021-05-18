import re

# This function takes in a string whch contains diffrent types of parenthesis
# It returns true if:
#                   1. Open brackets must be closed by the same type of brackets.
#                   2.Open brackets must be closed in the correct order.
# Otherwise returns false

def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in ["(", "{", "["]:
            #Push into stack if it an opening parenthesis
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True



if __name__ == '__main__':
    print(isValid("(]"))
    print(isValid("()[]{}"))
