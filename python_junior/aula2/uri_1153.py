"""
# 0.085s
from functools import reduce
from operator import __mul__

n = int(input())
print(reduce(__mul__, range(1, n + 1), 1))
"""
"""
0.057s
n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i
print(result)
"""
"""
0.037s
from math import factorial

n = int(input())
print(factorial(n))
"""
"""
# 0.170s
from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**7)


@lru_cache(maxsize=256)  # kbites
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


n = int(input())
print(fatorial(n))
"""
"""
# 0.012s
fats = [
    1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600
]
n = int(input())
print(fats[n - 1])
"""
