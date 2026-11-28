import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a real-valued matrix using row reduction.

    Args:
        A: Input matrix of shape (m, n).
        tol: Absolute tolerance for treating a value as zero.

    Returns:
        The rank of the matrix.
    """
    A = np.asarray(A)

    if A.ndim != 2:
        raise ValueError("A must be a two-dimensional matrix.")

    # Make a floating-point copy so division works and A isn't modified.
    A = A.astype(float, copy=True)

    m, n = A.shape
    rank = 0

    for col in range(n):
        # All rows have pivots, so there can't be any more.
        if rank == m:
            break

        # Find the largest possible pivot in this column, starting
        # at the row where we want to place the next pivot.
        pivot_row = rank + np.argmax(np.abs(A[rank:, col]))

        # If the whole remaining column is close to zero, skip it.
        if abs(A[pivot_row, col]) <= tol:
            continue

        # Move the pivot into position.
        A[[rank, pivot_row]] = A[[pivot_row, rank]]

        # Eliminate entries below the pivot.
        for row in range(rank + 1, m):
            factor = A[row, col] / A[rank, col]
            A[row] = A[row] - factor * A[rank]

        rank += 1

    return rank