from time import sleep, time

inicio = time()
from functools import reduce
from operator import __mul__
from sys import stdin

n = 100000
print(reduce(__mul__, range(1, n + 1), 1) % 1000)
final = time()
print(final - inicio)

inicio = time()
from functools import reduce
from operator import __mul__

n = 100000
result = 1
for i in range(1, n + 1):
    result *= i
print(result % 1000)
final = time()
print(final - inicio)