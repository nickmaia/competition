###############################################################
####### By Elder Vicente de Paulo Sobrinho - UFTM #############
###############################################################
n, m = map(int, input().split() )
Matriz=[ list(map(int,input().split() )) for _ in range(n) ]

#----------------------------------------------------------------------------
# PARTE I
# Armazena qual a posição do primeiro número > 0, se não tiver coloca -1
#   Exemplo de matriz
#   0 5 1 0 3 2 2 0
#   0 0 0 0 4 0 1 2
#   0 0 0 0 0 0 0 0
#   0 0 0 0 0 0 0 0
#   0 0 0 0 0 0 0 0
Lin=[]
for ii in range(n): # percorre cada linha da matriz
    ## identifica quais num são != de 0, e aramazena em lista o par (index, num)
    ffilter=filter(lambda x: x[1]!=0, enumerate(Matriz[ii])) 
    #   p/ ii=0  => [(1, 5), (2, 1), (4, 3), (5, 2), (6, 2)]
    #   p/ ii=1  => [(4, 4), (6, 1), (7, 2)]
    #   p/ ii>=2 => []
    ## pega apenas o primeiro par onde num é != de 0. Se lista vazia, então retorna o par (-1, 0)
    nnext=next(ffilter, (-1,0) )
    #   p/ ii=0  => [1, 5]
    #   p/ ii=1  => [4, 4]
    #   p/ ii>=2 => [-1, 0]
    ## cria a lista final apenas com o index do primeiro num != de 0
    Lin.append( nnext[0] )
    #  Qdo terminar o loop temos: [1, 4, -1, -1, -1]
# OOOOOUUUUU pode-se fazer tudo junto (de uma só vez):
#Lin=[ next( filter(lambda x: x[1]!=0, enumerate(Matriz[ii])), (-1,0) )[0] for ii in range(n) ]
#----------------------------------------------------------------------------

# Pega a posição do primeiro elemento -1, se não tiver coloca n
Fim = Lin.index(-1) if -1 in Lin else n
# Vamos fazer slice da lista Lin
# Lin => [1, 4, -1, -1, -1]; Zeros => [-1, -1, -1]; NonZero => [1, 4]
Zeros, NonZero=Lin[Fim:], Lin[:Fim]

#----------------------------------------------------------------------------
# PARTE II
# Tem elemento >= 0 depois que achou 1 sequencia de zero? (Rule I)
CheckAllZeros=next(filter(lambda x: x!=-1, Zeros), None) 
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# PARTE III
# checa se os indices non-zeros são crescentes... (Rule II)
# NonZero ==> [1, 4]; então: NonZero[1:] ==> [4] e NonZero[:-1] ==> [1]
# map(   lambda a, b: a - b,  ==> 4 - 1  ==> [3]
# filter(lambda x   : x <=0,  ==> []
# next(                       ==> None
CheckCrescentElements=next(filter(lambda x: x<=0, map(lambda a, b: a-b, NonZero[1:], NonZero[:-1])), None)
#----------------------------------------------------------------------------

# Fim...
if CheckAllZeros is None and CheckCrescentElements is None:
    print("S")
else:
    print("N")
