def py_palindrom_string(s: str) -> bool:
    p = ""

    for i in s:
        if i.isalnum():
            p += i.lower()
    return p == p[::-1]
