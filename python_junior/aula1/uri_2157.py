n = int(input())

for _ in range(n):
  a, b = map(int, input().split())
  first_part = "".join(map(str, range(a, b + 1)))
  second_part = first_part[::-1]
  print(first_part + second_part)