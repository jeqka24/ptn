# EAN codes of length 13 (12 digits + 1 control digit) is supported
# Algo taken from:
#  https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-13_check_digit_calculation

def validate_ean(value):
    L = (1, 3)

    checksum = 0
    filtered = [int(s) for s in filter(str.isdigit, value)]
    for digit in range(len(filtered)-1):
        checksum += filtered[digit] * L[digit % 2]

    return (10 - checksum % 10) == filtered[-1]

