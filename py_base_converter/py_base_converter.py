def convert_base(num: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        if not 2 <= from_base <= 36 or not 2 <= to_base <= 36:
            return "ERROR"

        n = int(num, from_base)

        if n == 0:
            return "0"

        res = ""
        while n:
            res += digits[n % to_base]
            n //= to_base

        return res[::-1]

    except Exception:
        return "ERROR"
