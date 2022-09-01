from functools import reduce

# Checks both ISBN (10 digits) and ISSN (8 digits). For ISBN with 13 digits see EAN-13

# При нанесении ISBN на книгу в виде штрих-кода собственная контрольная цифра удаляется,
#   слева приписывается префикс 978 (или 979, этот префикс пока не используется).
# При нанесении ISSN на журнал в виде штрих-кода собственная контрольная цифра удаляется,
#   слева приписывается префикс 977, а справа — 2 цифры, несущие некую дополнительную информацию, не содержащуюся непосредственно в ISSN (обычно 00 для платных изданий).
# Далее в обоих случаях справа приписывается контрольная цифра, вычисленная по 13-значному алгоритму для штрих-кода.
DEBUG = False


def validate_isbn(value):
    LOOKUP = {
        '0': 0, "1": 1, "2": 2, '3': 3,
        '4': 4, "5": 5, "6": 6, '7': 7,
        '8': 8, "9": 9, 'X': 10,
        }
    filtered = [LOOKUP[s] for s in filter(lambda x: x in "0123456789X", value)]
    if DEBUG:
        print(f"Checksum for {value}:")
        for a, b in zip(range(len(filtered)+1, 1), filtered):
            print(f'{a} * {b} = {a * b}')
        print(' is: ', sum([a * b for a, b in zip(range(len(filtered)+1, 1), filtered)]) % 11)

    checksum = sum([a * b for a, b in zip(range(len(filtered)+1, 1), filtered)]) % 11

    return checksum == 0

