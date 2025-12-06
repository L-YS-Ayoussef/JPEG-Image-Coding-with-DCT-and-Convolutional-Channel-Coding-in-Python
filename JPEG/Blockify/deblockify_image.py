import numpy as np


def deblockify_image(blocks):
    """
    Reconstruct an image from its blocks
    :param blocks: list of blocks
    :return: image array
    """
    N = len(blocks[0][0])  # block size
    image_length = len(blocks) * N  # number of vertical blocks * block size
    image_width = len(blocks[0]) * N  # number of horizontal blocks * block size

    image_array = blocks.reshape(image_length // N, image_width // N, N, N)
    image_array = image_array.swapaxes(1, 2).reshape(-1, image_length, image_width).squeeze()

    return image_array
