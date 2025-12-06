# This file contains all the definitions for the project

from enum import Enum

class CompressionMode(Enum):
    """
    Compression mode enum class
    """
    LOW = 1
    HIGH = 2


class CompressionTechnique(Enum):
    HUFFMAN = 1
    ARITHMETIC = 2