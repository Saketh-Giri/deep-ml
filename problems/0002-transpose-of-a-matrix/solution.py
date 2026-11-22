def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows, cols = len(a), len(a[0])
    t_matrix = [[0] * rows for _ in range(cols)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            t_matrix[j][i] = a[i][j]
    return t_matrix