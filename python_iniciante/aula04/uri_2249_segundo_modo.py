consoantes = "bcdfghjklmnpqrstvwxyz"

risada = input()

risada_sem_consoantes = ""

for letra in risada:
    if letra not in consoantes:
        risada_sem_consoantes += letra

if risada_sem_consoantes == risada_sem_consoantes[::-1]:
    print("S")
else:
    print("N")
