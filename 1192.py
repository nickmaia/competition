N = int(input())
dados = []
for i in range(N):
    dados = list(input())
    
    if dados[0] == dados[2]:
        print(int(dados[0])*int(dados[2]))
        
    elif dados[1].isupper() is True:
        print(int(dados[2])-int(dados[0]))
        
    else:
        print(int(dados[0])+int(dados[2]))