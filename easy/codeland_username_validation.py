import re


def CodelandUsernameValidation(strParam):
    regex = '^[a-zA-Z][a-zA-Z0-9_]{2,23}[a-zA-Z0-9]$'
    response = bool(re.match(regex, strParam))
    return response
