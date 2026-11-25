def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix:
        return []
    ans = []

    if mode.lower() == "column":
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        for c in range(n_cols):
            total = 0.0
            for r in range(n_rows):
                total += matrix[r][c]
            ans.append(total / n_rows)
    else:  # row mode
        for row in matrix:
            if not row:
                ans.append(0.0)
            else:
                total = 0.0
                for v in row:
                    total += v
                ans.append(total / len(row))
    return ans