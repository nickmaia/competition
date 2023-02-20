a, b, c = map(int, input().split())

maior_a_b = (a + b + abs(a - b)) // 2

maior_geral = (maior_a_b + c + abs(maior_a_b - c)) // 2

print("{} eh o maior".format(maior_geral))
