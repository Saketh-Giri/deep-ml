def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    rows, cols = len(a), len(b[0])
    c = [[0] * cols for _ in range(rows)]
    temp = 0
    for i in range(len(b[0])):
        for j in range(len(a)):
            for k in range(len(a[0])):
                temp += a[j][k] * b[k][i]
            c[j][i] = temp
            temp = 0
    return c