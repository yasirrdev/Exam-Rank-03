def bracket_validator(s: str) -> bool:
    stack = []  # pila donde guardamos los brackets abiertos

    for i in s:
        # Si es un bracket de apertura → lo guardamos
        if i in "([{":
            stack.append(i)

        # Si es un bracket de cierre → comprobamos
        elif i in ")]}":
            # Si no hay nada en la pila → no hay apertura previa → inválido
            if not stack:
                return False

            # Sacamos el último bracket abierto
            last = stack.pop()

            # Comprobamos que coincidan
            if (i == ')' and last != '(') or \
               (i == '}' and last != '{') or \
               (i == ']' and last != '['):
                return False

        # Si no es bracket → lo ignoramos

    # Si la pila está vacía → todo cerrado correctamente
    return not stack


if __name__ == "__main__":

    print(bracket_validator("()"))                              # → True
    print(bracket_validator("()[]{}"))                          # → True
    print(bracket_validator("{[()]}"))                          # → True
    print(bracket_validator(""))                                # → True
    print(bracket_validator("hello(hhhh)world{ho}w are"))       # → True
    print(bracket_validator("(]"))                              # → False
    print(bracket_validator("([)]"))                            # → False
    print(bracket_validator("((("))                             # → False
    print(bracket_validator("())"))                             # → False
