# Uso do range - Criando uma lista de números, iniciando em 5 e terminando em 20 (de um em um)
Lista=[]
i=5
while (i<=20):
    Lista.append(i)
    i=i+1
print(Lista)
# ou
Lista=list(range(5, 20+1, 1))
print(Lista)

## ------------------------------------------------------------------------------------------------
# Uso do map - convertendo uma lista de caracteres numéricos para uma lista de inteiros
Lista=["1", "5", "6", "7", "8", "0"]
Lista2=[]
for data in Lista:
    Lista2.append( int(data) )
print(Lista2)
# ou
Lista2=list( map(int, Lista) )
print(Lista2)


## ------------------------------------------------------------------------------------------------
# Uso do enumerate - descobrindo em qual posição da lista se encontra cada item
Lista=["1", "5", "6", "7", "8", "0"]
i=0
while i < len(Lista):
    print(f"item {Lista[i]} na posicão {i+1}")
    i = i + 1
# ou
for i,data in enumerate(Lista, start=1):
    print(f"item {data} na posicão {i}")


## ------------------------------------------------------------------------------------------------
# Uso do zip - percorrendo pares de itens em duas listas independentes
# CUIDADO: O tamanho das listas devem ser iguais ou você deve fazer algum tipo de tratamento p/ evitar erros
Lista1=["A", "B", "C", "D", "E", "F"]
Lista2=["5", "4", "3", "2", "1", "0"]
i=0
while i<len(Lista1):
    print(f"item {i+1} da lista1 {Lista1[i]} e item {i+1} da lista2 {Lista2[i]}")
    i = i + 1
# ou
for i, data in enumerate(zip( Lista1, Lista2 ), start=0):
    print(f"item {i+1} da lista1 {data[0]} e item {i+1} da lista2 {data[1]}")


## ------------------------------------------------------------------------------------------------
# Uso do sum - percorrendo uma lista de números e gerando a soma
Lista=[5, 4, 3, 2, 1, 0]
soma=0
for data in Lista:
    soma= soma + data
print(soma)
# ou 
soma= sum( Lista )
print(soma)


## ------------------------------------------------------------------------------------------------
# Uso do lambda (rotina anônima) - percorrendo uma lista de números descobrindo os > q 3
def sum(x): #X é > que 3?
    if x>3: 
        return True
    return False
Lista=[5, 4, 3, 2, 1, 0]
result=list( map(sum, Lista ) )
print(result)
# ou
Lambda=lambda x: True if x > 3 else False
result=list( map(Lambda, Lista ) )
print(result)
# ou
result=list( map( lambda x: True if x > 3 else False , Lista ) )
print(result)


## ------------------------------------------------------------------------------------------------
# Uso do reduce - percorrendo uma lista de números descobrindo quantos são > q 3
from functools import reduce
Lista=[5, 4, 3, 2, 1, 0]
count=0
for data in Lista:
    if data>3:
        count = count + 1
print(count)
# ou 
Map=map( lambda x: True if x > 3 else False , Lista )
result=reduce( lambda x, y: x + y, Map, 0 )
print(result)


## ------------------------------------------------------------------------------------------------
# Uso do filter - percorrendo uma lista de números e gerando uma nova apenas com o números > q 3
Lista=[5, 4, 3, 2, 1, 0]
ListaNew=[]
for data in Lista:
    if data>3:
        ListaNew.append( data )
print( ListaNew )
# ou 
ListaNew=list( filter( lambda x: True if x > 3 else False , Lista ))
print( ListaNew )
