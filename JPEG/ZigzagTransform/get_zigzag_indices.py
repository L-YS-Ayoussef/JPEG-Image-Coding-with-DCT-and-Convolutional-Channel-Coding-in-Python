import numpy as np

def get_zigzag_indices(N):
    """
    Return the zigzag transform for a block of size N*N
    :param N: size of block (N*N)
    :return: 1D array zigzag transform for a 2D block of size (N*N)
    """

    zigzag_indices = [(i,j) for i in range(N) for j in range(N)]
    zigzag_indices.sort(key = lambda x: (x[0]+ x[1], x[1]) if (x[0]+x[1])%2 == 0 else (x[0]+x[1], x[0]))

    return zigzag_indices