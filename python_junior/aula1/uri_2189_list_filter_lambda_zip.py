# encontrar na lista a posição que o número coincide com a posição.

n = int(input())
count = 1
while n != 0:
    print("Teste {}".format(count))
    count += 1
    print(
        list(filter(
            lambda x: x[0] == x[1],
            zip(map(int, input().split()), range(1, n + 1)),
        ))[0][0]
    )
    print()
    n = int(input())