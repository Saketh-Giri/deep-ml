import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    # By convention, an empty set of vectors is independent.
    if len(vectors) == 0:
        return True

    matrix = np.array(vectors, dtype=float)

    # Nonempty sets of zero-dimensional vectors are dependent.
    if matrix.shape[1] == 0:
        return False

    rank = np.linalg.matrix_rank(matrix)
    return rank == len(vectors)