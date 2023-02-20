N, M = map(int, input().split())

pivos = []
pivo_before = 0
condition = True
for i in range(N):
    row = map(int, input().split())
    index_col = 0
    for num in row:
        index_col += 1
        if (num != 0):
            pivos.append(index_col)
            break
        if index_col == M:
            pivos.append(M+1)
    if pivos[-1]!= M+1:
        try:
            if pivos[-1] <= pivos[-2]:
                condition = False
        except:
            continue
if not condition:
    print('N')
else:
    print('S')