import numpy as np


def IDCT_Basis(x, y, N):
    """
    Return the IDCT Basis function for x,y and N
    :param x: the horizontal image index of the IDCT output
    :param y: the vertical image index of the IDCT output
    :param N: size of block (N*N)
    :return: DCT Basis function for given x and y
    """
    b = np.zeros((N, N))
    for u in range(N):
        for v in range(N):
            b[u][v] = np.cos((2 * x + 1) * u * np.pi / (2 * N)) * np.cos((2 * y + 1) * v * np.pi / (2 * N))

    return b