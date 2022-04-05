# Dictionary - Refer to ISO 7064 mod 97-10

LETTERS = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16,
           "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23,
           "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30,
           "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35,"0": 0, "1": 1,
           "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

# ISO 3166-1 alpha-2 country code
COUNTRIES = {"AL": [28, "Albania"],
             "AD": [24, "Andorra"],
             "AT": [20, "Austria"],
             "BE": [16, "Belgium"],
             "BA": [20, "Bosnia"],
             "BG": [22, "Bulgaria"],
             "HR": [21, "Croatia"],
             "CY": [28, "Cyprus"],
             "CZ": [24, "Czech Republic"],
             "DK": [18, "Denmark"],
             "EE": [20, "Estonia"],
             "FO": [18, "Faroe Islands"],
             "FI": [18, "Finland"],
             "FR": [27, "France"],
             "DE": [22, "Germany"],
             "GI": [23, "Gibraltar"],
             "GR": [27, "Greece"],
             "GL": [18, "Greenland"],
             "HU": [28, "Hungary"],
             "IS": [26, "Iceland"],
             "IE": [22, "Ireland"],
             "IL": [23, "Israel"],
             "IT": [27, "Italy"],
             "LV": [21, "Latvia"],
             "LI": [21, "Liechtenstein"],
             "LT": [20, "Lithuania"],
             "LU": [20, "Luxembourg"],
             "MK": [19, "Macedonia"],
             "MT": [31, "Malta"],
             "MU": [30, "Mauritius"],
             "MC": [27, "Monaco"],
             "ME": [22, "Montenegro"],
             "NL": [18, "Netherlands"],
             "NO": [15, "Northern Ireland"],
             "PO": [28, "Poland"],
             "PT": [25, "Portugal"],
             "RO": [24, "Romania"],
             "SM": [27, "San Marino"],
             "SA": [24, "Saudi Arabia"],
             "RS": [22, "Serbia"],
             "SK": [24, "Slovakia"],
             "SI": [19, "Slovenia"],
             "ES": [24, "Spain"],
             "SE": [24, "Sweden"],
             "CH": [21, "Switzerland"],
             "TR": [26, "Turkey"],
             "TN": [24, "Tunisia"],
             "GB": [22, "United Kingdom"]}

def iban_is_valid(iban):
    IBAN_LIST = list(iban)
    COUNTRY = IBAN_LIST[:2]
    LENGTH = len(IBAN_LIST)
    COUNTRY_STRING = ''.join(COUNTRY)
    if COUNTRY_STRING in COUNTRIES:
        ACTIVE_COUNTRY = COUNTRIES[COUNTRY_STRING]
        if LENGTH == ACTIVE_COUNTRY[0]:
            HEADER = IBAN_LIST[:4]
            BODY = IBAN_LIST[4:]
            IBAN_LIST = BODY+HEADER
            for i, s in enumerate(IBAN_LIST):
                if s in LETTERS:
                    IBAN_LIST[i] = LETTERS[s]
            IBAN_STRING = ''.join(str(i) for i in IBAN_LIST)
            IBAN_INT = int(IBAN_STRING)
            if IBAN_INT % 97 == 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
