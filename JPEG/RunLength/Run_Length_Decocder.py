import numpy as np


def run_length_decoder(encoded,no_vertical_blocks,no_horizontal_blocks,N):
    """
    Decode the encoded image
    :param encoded: encoded image
    :param no_vertical_blocks: Number of vertical blocks
    :param no_horizontal_blocks: Number of horizontal blocks
    :param N: block size (N*N)
    :return: decoded image
    """
    total_image_length = N*N*no_horizontal_blocks*no_vertical_blocks

    encoded_len = encoded.shape
    image = np.zeros(total_image_length)
    idx = 0
    for i in range(encoded_len[0]):
        if encoded[i - 1] == 0:
            continue
        if encoded[i] == 0:
            for j in range(int(encoded[i+1])):
                if idx < total_image_length:
                    image[idx] = 0
                    idx += 1
        else:
            if idx < total_image_length:
                image[idx] = encoded[i]
                idx += 1
    return image
