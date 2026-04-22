def py_bracket_validator(s: str) -> bool:
    stack = []

    for i in range(0, len(s)):
        if s[i] in "([{":
            stack.append(s[i])
        elif s[i] in ")]}":
            if not stack:
                return False
            top = stack.pop()
            if s[i] == ')' and top != '(':
                return False
            elif s[i] == ']' and top != '[':
                return False
            elif s[i] == '}' and top != '{':
                return False

    return len(stack) == 0
