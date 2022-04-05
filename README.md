# Iban Checker API
This project is designed to recieve REST API calls from a web-host to validate IBAN numbers and check them against there country codes and requirements returning either True or False for validation.

## Goal
 to Read IBAN numbers and check there validation according to the "Validating the IBAN" segment of [Wikipedia-IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) 
  the goals followed are referenced by the wikipedia page.
   - Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
   - Move the four initial characters to the end of the string
   - Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11, ..., Z = 35
   - Interpret the string as a decimal integer and compute the remainder of that number on division by 97

