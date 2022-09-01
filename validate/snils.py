__all__ = ["validate_snils"]


# Todo: move everything from simple Bool type to (Result: Bool, Error: object)

def validate_snils(value):
    val = str("".join(filter(str.isdigit, str(value))))
    length = len(val)
    if not (length in [11, ]):
        # raise ValueError("Длина СНИЛС должна быть 11 цифр")
        return False
    if len(val) == 11:
        weights = list(range(9, 0, -1))
        snils = [a for a in map(int, str(val))]
        control = sum(a * b for a, b in zip(snils, weights))
        if control > 101:
            control %= 101
        if (control == 100) or (control == 101):
            control = 0
        if not (control == int("".join(map(str, snils[-2:])))):
            # raise ValueError("Несовпадение контрольной суммы (%d), присутствует %d" % (control, int("".join(map(str, snils[-2:])))))
            return False
    return True
