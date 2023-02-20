from functools import reduce
from operator import __mul__

print(__mul__(3, 5))


def fatorial(n):

    if n == 0:
        return 1

    return reduce(__mul__, range(1, n + 1), 1)


print(fatorial(5))
