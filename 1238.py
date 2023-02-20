N = int(input())

for i in range(N):
    s1, s2 = input().split()
    
    resposta = ""
    try:
        for l1, l2 in zip(s1,s2):
            resposta += l1 + l2
            
        if len(s1) == len(s2):
            print(resposta)
    
        elif len(s2) > len(s1):
            tam = len(s1) - len(s2)
            ultima_letra = s2[tam:]
            print(resposta+ultima_letra)
        else:
            tam = len(s2) - len(s1)
            ultima_letra = s1[tam:]
            print(resposta+ultima_letra)
            
    except:
        break
    
    
