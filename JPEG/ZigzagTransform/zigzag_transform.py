# Different implementation of the 2d block into 1d array
from .get_zigzag_indices import get_zigzag_indices
import numpy as np

def zigzag_transform(block):
    """
    Return 1d array zigzag-traversed from the 2d block (N*N)
    :param block: 2d block (N*N)
    :return: 1d array (N*N)
    """
    N = block.shape[0]

    zigzag_indices = get_zigzag_indices(N)

    _1d_array = np.zeros(N*N)

    for i,zigzag_index in enumerate(zigzag_indices):
        _1d_array[i] = block[zigzag_index[0], zigzag_index[1]]

    return _1d_array