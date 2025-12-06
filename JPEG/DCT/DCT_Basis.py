import numpy as np


def DCT_Basis(u, v, N):
    """
    Return the DCT Basis function for u,v and N
    :param u: the horizontal frequency index of the DCT output
    :param v: the vertical frequency index of the DCT output
    :param N: size of block (N*N)
    :return: DCT Basis function for given u and v
    """
    b = np.zeros((N, N))
    for x in range(N):
        for y in range(N):
            b[x][y] = np.cos((2 * x + 1) * u * np.pi / (2 * N)) * np.cos((2 * y + 1) * v * np.pi / (2 * N))

    return b
