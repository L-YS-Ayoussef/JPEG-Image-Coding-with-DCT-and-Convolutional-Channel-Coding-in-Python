import numpy as np


def run_length_encoder(image):
    """
    Encode the image using run length encoding
    :param image: image to be encoded
    :return: encoded image
    """
    zeros_count = 0
    length = image.shape
    encoded = np.array([])
    for i in range(length[0]):
        if image[i] == 0:
            if zeros_count == 0:
                encoded = np.append(encoded, 0)
            zeros_count += 1
        else:
            if zeros_count != 0:
                encoded = np.append(encoded, zeros_count)
                zeros_count = 0
            encoded = np.append(encoded, image[i])
    if zeros_count != 0:
        encoded = np.append(encoded,zeros_count)
    return encoded