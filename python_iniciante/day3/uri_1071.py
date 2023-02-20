m = int(input())
n = int(input())

menor, maior = sorted([m, n])

soma_impares = 0

for i in range(menor + 1, maior):
    if i % 2 == 1:
        soma_impares += i

print(soma_impares)
