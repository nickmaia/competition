###############################################################
####### By Elder Vicente de Paulo Sobrinho - UFTM #############
###############################################################
#--------------------------------------------------------------------------------
# Trabalhando com listas - forma tradicional
Lista=[]
for data in range(20, 0, -1):
    Lista.append(data)
print(Lista) # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Lista=list(range(20, 0, -1))
print(Lista) # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#--------------------------------------------------------------------------------
# Trabalhando com listas - usando compressão
# general         ==> new_list = [expression for member in iterable]
# to filter       ==> new_list = [expression for member in iterable (if conditional)]
# to change value ==> new_list = [expression (if conditional) for member in iterable]
Lista=[data for data in range(20, 0, -1)]
print(Lista) # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# pegando apenas os numeros pares
Lista=[data for data in range(20, 0, -1) if data%2==0]
print(Lista) # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# criando uma lista diferente baseado nos elementos de outra 
Lista=["par" if data%2==0 else "impar" for data in range(20, 0, -1)]
print(Lista) # ['par', 'impar', 'par', 'impar', 'par', 'impar', 'par', ... , 'impar']

#--------------------------------------------------------------------------------
## Fazendo o fatiamento da lista/elementos
## List Slice => Lista[Inicio:Fim:Passo]
Lista=list(range(20, 0, -1)) # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(Lista[3 : 12 : 2])  # imprime de dois em dois os elementos com indice entre 3 e 12 ==> [17, 15, 13, 11, 9]
print(Lista[  : -1 :  ])  # imprime todos os elementos menos o último   ==> [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
print(Lista[  :    :-1])  # imprime todos os elementos em ordem reversa ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(Lista[ 5:    :  ])  # imprime todos os elementos com indice >= 5  ==> [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(Lista[-5:    :  ])  # imprime os últimos 5 elementos na ordem q aparecem ==> [5, 4, 3, 2, 1]
## OOOUUU
print(Lista[slice(   3,   12,    2)])  # imprime de dois em dois os elementos com indice entre 3 e 12 ==> [17, 15, 13, 11, 9]
print(Lista[slice(None,   -1, None)])  # imprime todos os elementos menos o último   ==> [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
print(Lista[slice(None, None,   -1)])  # imprime todos os elementos em ordem reversa ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(Lista[slice(   5, None, None)])  # imprime todos os elementos com indice >= 5  ==> [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(Lista[slice(  -5, None, None)])  # imprime os últimos 5 elementos na ordem q aparecem ==> [5, 4, 3, 2, 1]

#--------------------------------------------------------------------------------
## Listas nD (2D - Matriz ou Lists of Lists)
## Matriz=[ # 5 Linhas por 5 colunas
##         [5, 4, 3, 2, 1], 
##         [5, 4, 3, 2, 1], 
##         [5, 4, 3, 2, 1], 
##         [5, 4, 3, 2, 1], 
##         [5, 4, 3, 2, 1]
## ]
Matriz=[ [data for data in range(5, 0, -1)] for _ in range(0,5,1) ] # 5 Linhas por 5 colunas
from pprint import pprint
pprint(Matriz) # imprime a matriz formatada (Linha por Colunas)


## Matriz=[ # 5 Linhas por 5 colunas
##         [ 1,  2,  3,  4,  5],
##         [ 6,  7,  8,  9, 10],
##         [11, 12, 13, 14, 15],
##         [16, 17, 18, 19, 20],
##         [21, 22, 23, 24, 25]
## ]
N=5
Matriz=[ [(N*i)+j+1 for j in range(N)] for i in range(N) ] 
pprint(Matriz) # imprime a matriz formatada (Linha por Colunas)

print(Matriz[N-1]) # [21, 22, 23, 24, 25]
print(Matriz[N-1][N-1]) # acessando a última posição ==> 25 (inteiro)

# Vamos imprimir a matriz e formatar os valoes com 3 dígitos (colocando zeros a esquerda)
# 001; 002; 003; 004; 005;
# 006; 007; 008; 009; 010;
# 011; 012; 013; 014; 015;
# 016; 017; 018; 019; 020;
# 021; 022; 023; 024; 025;
for linha in Matriz: # passando por cada linha da matriz
    for elemento in linha: # pegando cada elemento da matriz
        print(f"{elemento:03}; ",end="") # imprime cada elemento na mesma linha e formata eles
    print("") # vamos passar p/ a próxima linha

# Slice da Matriz 2D (lists of Lists)
print(Matriz[  : -1 :  ])     # imprime as linhas da matriz menos a última     ==> [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
print(Matriz[  :    :-1])     # imprime as linhas da matriz em ordem reversa   ==> [[21, 22, 23, 24, 25], [16, 17, 18, 19, 20], [11, 12, 13, 14, 15], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]]
print(Matriz[ 2:    :  ])     # imprime as linhas da matriz com indice >= 2    ==> [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
print(Matriz[-2:    :  ])     # imprime as últimas 2 linhas da matriz na ordem ==> [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
# lists of Lists => Slice não funciona na vertical, não nativamente (ex. pegar todos os elementos da primeira coluna). 


#--------------------------------------------------------------------------------
## Numpy -- Permite fazer slices avançados, ex. pegar os elementos da primeira coluna
## python -m pip install numpy
import numpy as np

L1=list(range(0,25)) # <class 'list'>
print(L1) # Imprime os elementos da lista ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
L1=np.array(L1) # converte a lista para usar o numpy ==> <class 'numpy.ndarray'>
print(L1) # Imprime os elementos da lista ==> [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]

# [
#   [ 0  1  2  3  4]
#   [ 5  6  7  8  9]
#   [10 11 12 13 14]
#   [15 16 17 18 19]
#   [20 21 22 23 24]
# ]
L1=L1.reshape((5,5)) # Criando uma matriz 2D (5 x 5) ==> Veja acima
print(L1) # Imprime a matriz 2D (5 x 5)
print(L1.shape) # imprime a qtde de linhas e colunas da matriz ==> tupla (5, 5) 

# Slice com numpy L1[ Linha, Coluna ] onde:
#                     Linha  = Inicio : Fim : Passo
#                     Colune = Inicio : Fim : Passo
print(L1[0:1:, :: ])    # imprime os elementos da primeira linha ==> [[0 1 2 3 4]]
print(L1[1:2:, :: ])    # imprime os elementos da segunda linha  ==> [[5 6 7 8 9]]
print(L1[0:2:, :: ])    # imprime os elementos da primeira e segunda linha ==> [[0 1 2 3 4] [5 6 7 8 9]]
print(L1[::, 0:1: ])    # imprime os elementos da primeira coluna ==> [[ 0] [ 5] [10] [15] [20]]
print(L1[::, 1:2: ])    # imprime os elementos da segunda coluna  ==> [[ 1] [ 6] [11] [16] [21]]
print(L1[::, 0:2: ])    # imprime os elementos da primeira e segunda coluna ==> [[ 0  1] [ 5  6] [10 11] [15 16] [20 21]] 
print(L1[0:1:, ::-1 ])  # imprime os elementos da primeira linha em ordem reversa ==> [[4 3 2 1 0]]
print(L1[1:2:, ::-1 ])  # imprime os elementos da segunda linha em ordem reversa  ==> [[9 8 7 6 5]]
print(L1[0:2:, ::-1 ])  # imprime os elementos da primeira e segunda em ordem reversa ==> [[4 3 2 1 0] [9 8 7 6 5]]
print(L1[::-1, 0:1: ])  # imprime os elementos da primeira coluna em ordem reversa ==> [[20] [15] [10] [ 5] [ 0]]
print(L1[::-1, 1:2: ])  # imprime os elementos da segunda coluna em ordem reversa  ==> [[21] [16] [11] [ 6] [ 1]]
print(L1[::-1, 0:2: ])  # imprime os elementos da primeira e segunda coluna em ordem reversa ==> [[20 21] [15 16] [10 11] [ 5  6] [ 0  1]]
print(L1[0:1:, ::-2 ])  # imprime os elementos da primeira linha em ordem reversa e de dois em dois ==> [[4 2 0]]
print(L1[1:2:, ::-2 ])  # imprime os elementos da segunda linha em ordem reversa e de dois em dois  ==> [[9 7 5]]
print(L1[0:2:, ::-2 ])  # imprime os elementos da primeira e segunda em ordem reversa e de dois em dois ==> [[4 2 0] [9 7 5]]
print(L1[::-2, 0:1: ])  # imprime os elementos da primeira coluna em ordem reversa e de dois em dois ==> [[20] [10] [ 0]]
print(L1[::-2, 1:2: ])  # imprime os elementos da segunda coluna em ordem reversa e de dois em dois ==> [[21] [11] [ 1]]
print(L1[::-2, 0:2: ])  # imprime os elementos da primeira e segunda coluna em ordem reversa e de dois em dois ==> [[20 21] [10 11] [ 0  1]]
print(L1[0:1:, ::2 ])   # imprime os elementos da primeira linha de dois em dois ==> [[0 2 4]]
print(L1[1:2:, ::2 ])   # imprime os elementos da segunda linha de dois em dois  ==> [[5 7 9]]
print(L1[0:2:, ::2 ])   # imprime os elementos da primeira e segunda de dois em dois ==> [[0 2 4] [5 7 9]]
print(L1[::2, 0:1: ])   # imprime os elementos da primeira coluna de dois em dois ==> [[ 0] [10] [20]]
print(L1[::2, 1:2: ])   # imprime os elementos da segunda coluna de dois em dois  ==> [[ 1] [11] [21]]
print(L1[::2, 0:2: ])   # imprime os elementos da primeira e segunda coluna de dois em dois ==> [[ 0  1] [10 11] [20 21]]
print(L1[1:4:, 1:4: ])  # imprime os elementos internos (descarta a primera e a última linha, a primera e a última coluna) ==> [[ 6  7  8] [11 12 13] [16 17 18]]
print(L1[0:1:, :: ].sum())    # imprime a soma dos elementos da primeira linha ==> 10
print(L1[0:2:, :: ].sum())    # imprime a soma dos elementos da primeira e segunda linha ==> 45

# mais algumas operações com numpy
Mat1=np.array([ [1,2,3], [4,5,6], [5,4,7] ])
Mat2=np.array([ [9,8,7], [6,5,5], [2,3,5] ])
print(Mat1 * Mat2) # multiplica os elementos das matrizes       ==> [[ 9 16 21] [24 25 30] [10 12 35]]
print(np.dot(Mat2,Mat1)) # realiza a multiplicação de matrizes  ==> [[ 76  86 124] [ 51  57  83] [ 39  39  59]]

#Alterando valores da matriz usando Slice
# [ 
#  [ 0  1  2  3  4]
#  [ 5  0  0  0  9]
#  [10  0  0  0 14]
#  [15  0  0  0 19]
#  [20 21 22 23 24]
# ]
L1[1:4:, 1:4: ]=0  # coloca ZERO nos elementos internos 
print(L1)

#--------------------------------------------------------------------------------
## IMPORTANTE:
## Na maratona o comando "import numpy as np" não é permitido (gera erro)
## Isso porque numpy é um biblioteca externa ao python, por isso instalamos ela com "python -m pip install numpy"
## Para usar essa estrutura do numpy na maratona, temos que embarcar essa lib no código
## Assim,vamos usar o arquivo "TinyNumpyBase.py" como base para embarcar (https://github.com/eldereng/MaratonaProgramacao2020-Matriz/)
## Então use o arquivo "TinyNumpyBase.py" e inclua seu código dentro de "def mainCode():", teste e envie o arquivo
## Veja o arquivo "TinyNumpyExample.py", nele mostramos as operações acima sem usar a biblioteca numpy.
##    python TinyNumpyExample.py
## PS.: Algumas funcionalidades do numpy não estão disponíveis na "TinyNumpy". 
##      Além disso, esse procedimento de "embarcar" faz seu programa ficar + lento. Então seu uso tem que ser analisado  
