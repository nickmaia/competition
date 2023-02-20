n = int(input())
while n!=0:
    
    # create empty matrix
    Array = [n*[0] for i in range(n)]
    
    t = len(str(2 ** (2 * (n-1))))
    
    # fullfill matrix
    for j in range(n):
        for i in range(j,n):
            for k in range(n*2):
                if i+j == k:
                    Array[i][j] = 2 ** k
                    Array[j][i] = 2 ** k
    # print matrix
    for i in range(n):
        line = "{number:>{fill}s}".format(number=str(Array[0][i]),fill=t)
        for j in range(1,n):
            line += " {number:>{fill}s}".format(number=str(Array[j][i]),fill=t)
        print(line)
    print()
    
    # another case
    n = int(input())