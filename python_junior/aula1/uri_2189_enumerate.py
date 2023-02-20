# encontrar na lista a posição que o número coincide com a posição.

n = int(input())
count = 1
while n != 0:
    print("Teste {}".format(count))
    count += 1
    ingressos = map(int, input().split())
    for i, ingresso in enumerate(ingressos, start=1):
        if i != ingresso: 
            continue        
        print(i)
        break
    print()
    n = int(input())