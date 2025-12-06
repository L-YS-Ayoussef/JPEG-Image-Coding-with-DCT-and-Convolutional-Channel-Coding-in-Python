import numpy as np

def calculate_comprrssion_ratio(original_image_array, entropy_encoder_output):
    """
    Calculate the compression ratio of the image
    :param original_image_array: the original image array
    :param entropy_encoder_output: the output of the entropy encoder
    :return: the compression ratio
    """
    # count the number of bits for the binary representation of the image
    original_size = 0       # in bits
    for i in range(0, len(original_image_array)):
        for j in range(0, len(original_image_array[0])):
            original_size += len(bin(int(original_image_array[i][j]))[2:])     # [2:] to remove the '0b' prefix
    
    # count the number of bits for the entropy encoder output
    compressed_size = len(entropy_encoder_output)     # in bits
    
    return int(np.ceil(original_size / compressed_size))