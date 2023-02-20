# built-in functions de listas e strings

frutas = ["uva", "pera", "laranja"]  # list
palavra = "abacate"  # str
d = {"a": 1, "b": 2}

print(len(frutas))
print(len(palavra))
print(len(d))

for fruta in frutas:
    print(fruta)

for letra in palavra:
    print(letra)

for i in range(len(frutas)):
    print(frutas[i])

for i in range(len(palavra)):
    print(palavra[i])

print(sum([1, 2, 5, 2]))
# print(sum(['1', '2'])) # error

print(sorted([1, 5, 6, 2]))
print(sorted("dacfbe"))

# métodos de listas e strings

frutas = ["uva", "pera", "laranja"]  # list
palavra = "abacate"  # str

frutas.append("jaboticaba")  # mutáveis
print(frutas)

palavra = palavra.upper()  # imutáveis
print(palavra)

palavra = palavra.replace("BA", "LI")
print(palavra)

print("ok".rjust(5, "*"))
print("ok".rjust(5))
print("ok".ljust(5, "*"))

print("jaboticaba".count("a"))
print([1, 21, 1, 1, 3, 1, 5].count(1))

print("Meu imc é {:.{casas}f}".format(23.5786, casas=3))

print("Minha idade é {} e meu imc é {:.{casas}f}".format(35, 23.5789, casas=3))

numeros = [1, 5, 6, 2]
numeros.sort()
print(numeros)

print("bdaefc".index('f'))

frutas.pop()
print(frutas)

# operadores de pertinência

frutas = ["uva", "pera", "laranja"]  # list
palavra = "abacate"  # str

print("pera" in frutas)
print("r" in palavra)
print("jaboticaba" not in frutas)
print("c" not in palavra)

# inversão de listas ou strings

frutas = ["uva", "pera", "laranja"]  # list
palavra = "abacate"  # str

print(frutas[::-1])
print(palavra[::-1])

palavra = "ovo"

print(palavra == palavra[::-1])
