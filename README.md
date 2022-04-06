# Iban Checker API
This project is designed to recieve REST API calls from a web-host to validate IBAN numbers and check them against there country codes and requirements returning either True or False for validation.

## Goal
 to Read IBAN numbers and check there validation according to the "Validating the IBAN" segment of [Wikipedia-IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) 
  the goals followed are referenced by the wikipedia page.
   - Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
   - Move the four initial characters to the end of the string
   - Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11, ..., Z = 35
   - Interpret the string as a decimal integer and compute the remainder of that number on division by 97

## Future Development

For future development with this project I would like to create further validation according to Countries BBAN numbers where some countries use internal check digit algorithms to validate domestic BBANS as stated in [IBAN_CHECKER](https://www.iban.com/iban-checker).

I would also like to create a simple frontend for submitting IBANS and user interface for validation.


## Errors or issues in development

Due to lack of knowledge I could'nt create a makefile in the time frame as I have never been tasked to make one before and with the time frame available I would prefer to hand in what I have available for review.
Tried to build a Dockerfile for the first time and hopefully understood the layout and design of what was required for it.

### Resources used

- [IBAN-CHECKER](https://www.iban.com/iban-checker)
- [Wikipedia-IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [FLASK-TESTING](https://flask.palletsprojects.com/en/2.1.x/testing/)
- [FLASK-FACTORIES](https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/)
- [DOCKER-FILE](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)