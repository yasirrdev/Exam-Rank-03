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


if __name__ == "__main__":
    print((sculptor("Hello world")))    # → "hElLo WoRlD"
    print(sculptor("Hello, world!"))  # → "hElLo, WoRlD!"
    print(sculptor("123abcDEF"))      # → "123aBcDeF"
    print(sculptor("a-bC-dEf-ghIj"))  # → "a-Bc-DeF-gHiJ"
    print(sculptor(""))               # → ""
    print(sculptor("12345"))          # → "12345"
    print(sculptor("A"))              # → "a"
    print(sculptor("ab"))             # → "aB"
