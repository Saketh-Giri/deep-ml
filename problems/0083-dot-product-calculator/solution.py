import numpy as np

def calculate_dot_product(vec1, vec2):
    x=0
    for i in range(len(vec1)):
        x += vec1[i] * vec2[i]
    return x