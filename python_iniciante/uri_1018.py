while True:
    try:
        n = int(input())

        notas_100 = n // 100
        resto_100 = n % 100

        notas_50 = resto_100 // 50
        resto_50 = resto_100 % 50

        notas_20 = resto_50 // 20
        resto_20 = resto_50 % 20

        notas_10 = resto_20 // 10
        resto_10 = resto_20 % 10

        notas_5 = resto_10 // 5
        resto_5 = resto_10 % 5

        notas_2 = resto_5 // 2
        resto_2 = resto_5 % 2

        notas_1 = resto_2 // 1
        resto_1 = resto_2 % 1

        print(n)
        print("{} nota(s) de R$ 100,00".format(notas_100))
        print("{} nota(s) de R$ 50,00".format(notas_50))
        print("{} nota(s) de R$ 20,00".format(notas_20))
        print("{} nota(s) de R$ 10,00".format(notas_10))
        print("{} nota(s) de R$ 5,00".format(notas_5))
        print("{} nota(s) de R$ 2,00".format(notas_2))
        print("{} nota(s) de R$ 1,00".format(notas_1))
    except:
        break
