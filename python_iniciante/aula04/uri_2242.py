# in, not in
# replace para strings
# atributos de bibliotecas

consoantes = "bcdfghjklmnpqrstvwxyz"

risada = input()

risada_sem_consoantes = ""
# tirar consoantes
for letter in risada:
    if letter not in consoantes:
        risada_sem_consoantes += letter

# verificar se a risada resultante é anagrama
if risada_sem_consoantes[::-1] == risada_sem_consoantes:
    print("S")
else:
    print("N")