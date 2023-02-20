NDIM = 12 # mude para 12 antes de submeter

op = input()
Array = []
for i in range(NDIM):
    line = []
    for i in range(NDIM):
        line.append(float(input()))
    Array.append(line)
    
soma = 0
count = 0
for i in range(NDIM):
    for j in range(NDIM):
        if (i < j) and (i + j <= NDIM-2):
            soma += Array[i][j]
            count += 1

if op == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/count))