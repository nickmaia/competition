numero_palavras = int(input())

while numero_palavras != 0:

    palavras = []
    tamanho_maximo = 0

    for _ in range(numero_palavras):
        palavra = input()
        n = len(palavra)
        if n > tamanho_maximo:
            tamanho_maximo = n
        palavras.append(palavra)

    for palavra in palavras:
        print(palavra.rjust(tamanho_maximo))

    numero_palavras = int(input())

    if numero_palavras != 0:
        print()
