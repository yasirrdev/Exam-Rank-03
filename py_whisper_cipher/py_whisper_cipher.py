def py_whisper_cipher(s: str, n: int) -> str:

    result = ""
    for i in range(0, len(s)):
        if s[i].isalpha():
            if s[i].islower():
                result += chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
            else:
                result += chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        else:
            result += s[i]

    return result
