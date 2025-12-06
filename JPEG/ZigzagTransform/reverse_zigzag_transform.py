from .get_zigzag_indices import get_zigzag_indices
import numpy as np

def reverse_zigzag_transform(_1d_array, N):
    """
    Return 2d block (N*N) from the 1d array zigzag-traversed
    :param _1d_array: 1d array (N*N)
    :param N: size of block
    :return: 2d block (N*N)
    """
    zigzag_indices = get_zigzag_indices(N)

    block = np.zeros((N,N))

    for i,zigzag_index in enumerate(zigzag_indices):
        block[zigzag_index[0], zigzag_index[1]] = _1d_array[i]

    return block