###############################################################
####### By Elder Vicente de Paulo Sobrinho - UFTM #############
###############################################################

n, m = map(int, input().split() )
Matriz=[ list(map(int,input().split() )) for _ in range(n) ]

## ----------------- Usando Numpy

import numpy as np
Matriz=np.array(Matriz)

def Rule1(Matriz, n): # True = Rule1 ok; False = Rule1 not ok
    ZeroIndex=np.where(Matriz.sum(axis=1) == 0) 
    if len(ZeroIndex[0]): ## Tem linha com apenas ZEROS
        ListBase=range(min(ZeroIndex[0]), n) # vamos gerar uma lista sem lacunas e de um em um
        #são de tamanhos <>, então tem linhas não zero depois de uma com apenas zero
        if len(ListBase)!=len(ZeroIndex[0]): 
            return False
        # Uma validação exatra, compara a lista gerada com a extraida dos dados fornecidos
        Val=sum(map(lambda x: x[0]-x[1], zip(ListBase, ZeroIndex[0])))
        if Val!=0: # Tem linha q não é zero, então tem lacuna
            return False
    return True

def Rule2(Matriz, m, n): # True = Rule2 ok; False = Rule2 not ok
    # Gera uma lista dos indices onde o primeiro num é <> de zero
    IndexList=[min( np.where( Matriz[ii, ] !=0 )[0] , default=None) for ii in range(n)]
    #for i,item in enumerate(IndexList): # vamos filtrar e ver se é tudo zero ou não
    #    if item is None: continue
    #    if i+1>=n or item+1>=m: continue
    #    data=Matriz[i+1::, 0:item+1: ]
    #    print( np.amax(data) )
    # outra forma de fazer o código acima
    MAX=max(map(lambda x: 0 if x[1] is None or x[0]+1>=n or x[1]+1>m else np.amax(Matriz[x[0]+1::, 0:x[1]+1: ] ), enumerate(IndexList)), default=0)
    return True if MAX==0 else False

if Rule1(Matriz, n) and Rule2(Matriz, m, n):
    print("S")
else:
    print("N")

