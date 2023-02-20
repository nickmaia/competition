consoantes = "bcdfghjklmnpqrstvwxyz"

risada = input()

for letra in risada:
    if letra in consoantes:
        risada = risada.replace(letra, "")

if risada == risada[::-1]:
    print("S")
else:
    print("N")
