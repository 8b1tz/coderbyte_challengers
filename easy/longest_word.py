import re


def LongestWord(sen):
    sen = re.sub(r'[^\w\s]', '', sen)
    lista = sen.split(' ')
    return max(lista, key=lambda x: len(x))
