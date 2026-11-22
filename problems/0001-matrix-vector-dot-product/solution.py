def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if (len(a[0]) != len(b)):
        return -1
    temp = 0
    result = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            temp += a[i][j] * b[j]
        result.append(temp)
        temp = 0
    return result