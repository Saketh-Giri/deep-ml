def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    if len(matrix) == 2 or len(matrix[0]) == 2:
        return ((matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]), matrix[0][0]+matrix[1][1])
    else:
        a = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        b = matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
        c = matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
        return (a - b + c, matrix[0][0] + matrix[1][1] + matrix[2][2])