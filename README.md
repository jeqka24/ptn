## PTN - Personal tax number validation
Russian version - see below

This python package is a collection of simple validators to be used in Russia.
The codes to be validated are:
 * INN (persinal Tax Number) - Russia specific
 * SNILS (social security number)  - Russia specific
 * ISBN (length 8 и 10) / EAN-13 (length 13) - paper-printed books, magazines and newspapers
 * ISIN - credit card or other equities

## PTN - валидация ИНН, СНИЛС, EAN-13, ISBN, ISIN (банк. карты)
Этот пакет содержит набор валидаторов для разнообразных кодов:
 * ИНН (индивидуальный номер налогоплательщика)
 * СНИЛС (страховой номер индивидуального лицевого счета)
 * ISBN (длиной 8 и 10) / EAN-13 (13 символов) - код печатных изданий
 * ISIN (код банковских карт, акций, облигаций)

В каталоге contrib.django.fields содержатся поля для каждого из вида кода, основаны на Charfield