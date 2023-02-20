n = int(input())

lista = []

def reduzir(n1,d1, menor):
    if n1%menor == 0 and d1%menor==0:
        return menor
    else:
        return reduzir(n1, d1, menor-1)

for i in range(n):
    lista = input().split()
    N1 = int(lista[0])
    N2 = int(lista[4])
    D1 = int(lista[2])
    D2 = int(lista[6])

    if lista[3] == "+":
        n1 = (N1*D2 + N2*D1) 
        d1 = (D1*D2)
        
    if lista[3] == "-":
        n1 = (N1*D2 - N2*D1) 
        d1 = (D1*D2)
    
    if lista[3] == "*":
        n1 = (N1*N2)
        d1 = (D1*D2)
    
    if lista[3] == "/":
        n1 = (N1*D2)
        d1 = (N2*D1)
        
    menor = reduzir(n1,d1,abs(min(n1,d1)))
        
    print(f"{n1}/{d1} = {int(n1/menor)}/{int(d1/menor)}")
    
    