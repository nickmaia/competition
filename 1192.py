from string import ascii_uppercase

N = int(input())

for i in range(N):

    n1, a, n2 = list(input()); n1 = int(n1); n2 = int(n2)
    if n1 == n2:
        print(n1*n2)
    elif a in ascii_uppercase:
        print(n2-n1)
    else:
        print(n1+n2)
