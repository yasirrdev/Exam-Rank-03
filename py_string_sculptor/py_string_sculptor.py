def sculptor(text: str) -> str:

    lower = True
    s = ""

    for i in text:
        if i.isalpha():
            if lower:
                s += i.lower()
            else:
                s += i.upper()
            lower = not lower
        else:
            s += i
    return s
