for i in range(11):
    if (i == 0) or (i == 5) or (i == 10):
        I = i // 5
        for j in range(1, 4):
            print("I={} J={}".format(I, j + I))
    else:
        I = 0.2 * i
        for j in range(1, 4):
            print("I={:.1f} J={:.1f}".format(I, j + I))
