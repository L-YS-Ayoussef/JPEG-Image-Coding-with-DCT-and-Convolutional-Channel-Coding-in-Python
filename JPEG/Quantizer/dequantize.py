import numpy as np
from .get_quantization_table import get_quantization_table


def dequantize(block, CompressionMode):
    """
    Dequantize a block based on compression mode
    :param block: numpy array of block
    :param CompressionMode: enum class
    :return: dequantized block
    """
    return np.round(np.multiply(block, get_quantization_table(CompressionMode)))
