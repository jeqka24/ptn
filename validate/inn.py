def validate_inn(value):
    val = str("".join(filter(str.isdigit, str(value))))
    length = len(val)
    if not (length in [10, 12]):
        # raise ValueError("Длина ИНН должна быть 10 или 12 цифр")
        return False
    if len(val) == 10:
        weights = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
        inn = [a for a in map(int, str(val))]
        control = sum(a * b for a, b in zip(inn, weights)) % 11 % 10
        if control != inn[-1]:
            # raise ValueError("Несовпадение контрольной суммы (10)")
            return False
    if len(val) == 12:
        weights1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
        weights2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
        inn = [a for a in map(int, str(val))]
        control1 = sum(a * b for a, b in zip(inn, weights1)) % 11 % 10
        control2 = sum(a * b for a, b in zip(inn, weights2)) % 11 % 10
        if control1 != inn[-2] or control2 != inn[-1]:
            # raise ValueError("Несовпадение контрольной суммы (12)")
            return False
    return True



