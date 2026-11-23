import math
import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if (norm_type == "frobenius" and arr.ndim != 2):
        raise ValueError("Frobenius norm requires a 2D array.")
    
    if norm_type == "l1":
        total = 0
        if (arr.ndim == 1):
            for i in range(len(arr)):
                total += abs(arr[i])
        else:
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    total += abs(arr[i][j])

    if norm_type == "l2" or norm_type == "frobenius":
        total = 0
        if (arr.ndim == 1):
            for i in range(len(arr)):
                total += arr[i]**2
            total = math.sqrt(total)
        else:
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    total += arr[i][j]**2
            total = math.sqrt(total)
    
    if norm_type == "linf":
        total = -1
        if (arr.ndim == 1):
            for i in range(len(arr)):
                if (abs(arr[i]) > total):
                    total = abs(arr[i])
        else:
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if (abs(arr[i][j]) > total):
                        total = abs(arr[i][j])
    return total