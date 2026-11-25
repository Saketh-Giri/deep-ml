def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return None
    inv = [[0,0],[0,0]]
    inv[0][0] = matrix[1][1]/det
    inv[1][1] = matrix[0][0]/det
    inv[0][1] = -matrix[0][1]/det
    inv[1][0] = -matrix[1][0]/det
    return inv