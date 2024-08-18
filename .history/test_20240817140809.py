def isValid(s: str) -> bool:
    stack = []

    # every time we enconuter a closing bracket,
    # we want to check if stack.pop() has the corresponding opening
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            opener = stack.pop()
            print("Current", char, "Opener", opener)
            if (char == ')' and opener != '(') or (char == ']' and opener != ']') \
            or (char == '}' and opener != '{'):
                return False
    
    return True


s = "([{}])"
print(isValid(s))