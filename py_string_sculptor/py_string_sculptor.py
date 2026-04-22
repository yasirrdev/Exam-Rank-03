def py_string_sculptor(text: str) -> str:

    newtext = ""
    lower = True

    for i in range(0, len(text)):
        if text[i].isalpha():
            if lower:
                newtext += text[i].lower()
            else:
                newtext += text[i].upper()
            lower = not lower
        else:
            newtext += text[i]
    return newtext
