import numpy as np


def DCT(A, dct_basis):
    """
    Return the DCT of a block
    :param A: numpy array of the block
    :param dct_basis: List of DCT Basis function
    :return: DCT of A
    """
    N = len(A)
    C = np.zeros((N, N))

    for u in range(N):
        for v in range(N):
            C[u][v] = np.sum(np.multiply(A, dct_basis[u][v]))

    # Normalization
    C = C / 16
    C[0, :] = C[0, :] / 2
    C[:, 0] = C[:, 0] / 2
    # C = np.round(C)

    return C
