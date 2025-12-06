import numpy as np
from .get_quantization_table import get_quantization_table


def quantize(block, CompressionMode):
    """
    Quantize a block based on compression mode
    :param block: numpy array of block
    :param CompressionMode: enum class
    :return: quantized block
    """
    return np.round(np.divide(block, get_quantization_table(CompressionMode)))
