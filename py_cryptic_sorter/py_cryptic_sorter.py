def py_cryptic_sorter(tlist: list[str]) -> list[str]:
    def count_vowels(s: str):
        count = 0
        for i in s:
            if i in "aeiouAEIOU":
                count += 1
        return count

    return sorted(tlist, key=lambda s: (
        count_vowels(s),
        len(s),
        s.lower()
    ))
