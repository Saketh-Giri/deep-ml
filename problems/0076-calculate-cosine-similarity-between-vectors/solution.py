import math
import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    
    total1 = 0
    for j in range(len(v1)):
        total1 += v1[j]**2
    total1 = math.sqrt(total1)

    total2 = 0
    for k in range(len(v2)):
        total2 += v2[k]**2
    total2 = math.sqrt(total2)

    return total/(total1 * total2)