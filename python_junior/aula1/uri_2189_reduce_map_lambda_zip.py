# encontrar na lista a posição que o número coincide com a posição.
from functools import reduce

n = int(input())
count = 1
while n != 0:
    print("Teste {}".format(count))
    count += 1
    print(
        reduce(
            lambda x, y: x + y,
            map(
                lambda x: x[1] if x[0] == x[1] else 0,
                zip(map(int, input().split()), range(1, n + 1)),
            ),
            0
        )
    )
    print()
    n = int(input())