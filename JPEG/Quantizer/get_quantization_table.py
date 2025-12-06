import numpy as np


def get_quantization_table(CompressionMode):
    """
    Get quantization table based on compression mode
    :param CompressionMode: enum class
    :return: quantization table
    """
    if CompressionMode == CompressionMode.LOW:
        return np.array([[1, 1, 1, 1, 1, 2, 2, 4],
                         [1, 1, 1, 1, 1, 2, 2, 4],
                         [1, 1, 1, 1, 2, 2, 2, 4],
                         [1, 1, 1, 1, 2, 2, 4, 8],
                         [1, 1, 2, 2, 2, 2, 4, 8],
                         [2, 2, 2, 2, 2, 4, 8, 8],
                         [2, 2, 2, 4, 4, 8, 8, 16],
                         [4, 4, 4, 4, 8, 8, 16, 16]])
    elif CompressionMode == CompressionMode.HIGH:
        return np.array([[1, 2, 4, 8, 16, 32, 64, 128],
                         [2, 4, 4, 8, 16, 32, 64, 128],
                         [4, 4, 8, 16, 32, 64, 128, 128],
                         [8, 8, 16, 32, 64, 128, 128, 256],
                         [16, 16, 32, 64, 128, 128, 256, 256],
                         [32, 32, 64, 128, 128, 256, 256, 256],
                         [64, 64, 128, 128, 256, 256, 256, 256],
                         [128, 128, 128, 256, 256, 256, 256, 256]])
    else:
        raise ValueError('Invalid compression mode. Valid modes are: low, high')
