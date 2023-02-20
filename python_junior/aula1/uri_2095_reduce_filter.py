# https://www.urionlinejudge.com.br/judge/pt/problems/view/2095
from functools import reduce

S  = int(input())
Qi = map(int, input().split(" "))
Ni = map(int, input().split(" "))
Qi = sorted(Qi)
Ni = sorted(Ni)
ganha = 0

def Filter(soldado):
    global ganha # permite modificar variável fora do escopo da função
    if Ni[soldado] > Qi[ganha]: 
        ganha += 1 # modificando variável fora do escopo da função
        return 1
    return 0

#Result=len(list( filter(Filter, range(S)) )) 
# OR
Result=reduce(lambda x, y: x + 1,  filter(Filter, range(S))  , 0)

print( Result )
