#  from https://ru.wikipedia.org/wiki/Контрольное_число | https://en.wikipedia.org/wiki/Check_digit add:
#  - ISIN (Международный код ценной бумаги, в том числе и банковских карт)
#       Примеры - https://www.isin.org/isin-database/ :
#    Title 	        isin 	        description (type, isin, wkn, ticker)       country 	type
# Microsoft Corp. 	US5949181045 	Equity, ISIN US5949181045, WKN 870747, MSF 	US 	        Equity
# Google Inc. 	    US38259P5089 	Equity, ISIN US38259P5089, WKN A0B7FY, GGQ1	US 	        Equity
# Apple Inc. 	    US0378331005 	Equity, ISIN US0378331005, WKN 865985, APC 	US 	        Equity
# Invesco Ltd. 	    BMG491BT1088 	Equity Shares, BMG491BT1088 	            Bermuda 	Equity
# Accenture plc 	IE00B4BNMY34 	Equity Shares, ISIN IE00B4BNMY34     	    Ireland 	Equity
# Amazon.com Inc. 	US0231351067 	Equity Shares, ISIN US0231351067 	        United States 	Equity
# Netflix Inc. 	    US64110L1061 	Equity Shares, ISIN US64110L1061 	        United States 	Equity
# Facebook, Inc. 	US30303M1027 	Equity Shares, ISIN 	                    United States 	Equity
# BMW Australia 	CH0031240127 	Bond, ISIN CH0031240127, WKN A0NWXQ 	    Switzerland 	Bond
# Yorbeau Res Inc. 	CA9861913023 	Equity, ISIN CA9861913023, WKN 872300, UAN 	Canada 	    Equity
#

# 4000-0000-0000-6 — 13-значная банковская карта Visa.
# 5610-0000-0000-0001 — 16-значная банковская карта Australian Bankcard.
# RU0007661625 — ISIN акции Газпрома номиналом 5 руб.
# DE0001136927 — пример ISIN с сайта Банка Эстонии.

from functools import reduce


def validate_isin(value):
    # . Uppercase
    # . filter 0..9, A..Z
    # . Check length - 13 or 16 characters for bank cards, 14 for Equities
    # . Replace 'A'..'Z' for '10'..'35'
    # Luhn algorythm implementation is from https://ru.wikipedia.org/wiki/Алгоритм_Луна#Python

    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)

    replacer = lambda x: \
        (ord(x) <= ord('Z') and ord(x) >= ord('A') and str(ord(x) - ord('A') + 10)) or \
        (ord(x) <= ord('9') and ord(x) >= ord('0') and str(x)) or \
        ('')  # skip other characters

    filtered = reduce(str.__add__, map(replacer, value))

    # skipped due to the some equities having several Chars instead of two
    # if len(filtered) not in [13, 14, 16]:
    #    return False

    evens = sum(int(i) for i in filtered[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in filtered[-2::-2])

    checksum = evens + odds

    # Oh, debugging...
    # print(f'code={value}, checksum={checksum}')

    return checksum % 10 == 0
