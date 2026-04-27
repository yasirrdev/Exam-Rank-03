def Shift_alphabet(s: str, n: int) -> str:
    new_str = ""

    for i in s:
        if i.isalpha():
            if i.islower():
                new_str += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            elif i.upper():
                new_str += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else:
            new_str += i
    return new_str


if __name__ == "__main__":
    print(Shift_alphabet("abz", 1))            # → "bca"
    print(Shift_alphabet("AbZ", 1))            # → "BcA"
    print(Shift_alphabet("Hello World!", 3))   # → "Khoor Zruog!"
    print(Shift_alphabet("bca", -1))           # → "abz"
    print(Shift_alphabet("abc", 26))           # → "abc"
    print(Shift_alphabet("xyz", 3))            # → "abc"
    print(Shift_alphabet("", 10))              # → ""
    print(Shift_alphabet("12345", 4))          # → "12345"
