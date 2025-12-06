import numpy as np


def IDCT(C, idct_basis):
    """
    Return the IDCT of a block
    :param C: numpy array of the block
    :param idct_basis: List of IDCT Basis function
    :return: IDCT of C
    """
    N = len(C)
    A = np.zeros((N, N))

    for x in range(N):
        for y in range(N):
            basis = idct_basis[x][y]
            A[x][y] = np.sum(np.multiply(C, basis))

    return A
