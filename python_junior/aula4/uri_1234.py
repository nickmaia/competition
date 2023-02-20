import re

pattern = re.compile("(\w{1})(\s*)(\w{1})|(\w{1})")


def danca(er):  # er: expressão regular
    try:
        resultado = er.group(1).upper() + er.group(2) + er.group(3).lower()
    except AttributeError:
        resultado = er.group(4).upper()
    return resultado


while True:
    try:
        texto = input()
        novo_texto = re.sub(pattern, danca, texto)
        print(novo_texto)
    except EOFError:
        break
