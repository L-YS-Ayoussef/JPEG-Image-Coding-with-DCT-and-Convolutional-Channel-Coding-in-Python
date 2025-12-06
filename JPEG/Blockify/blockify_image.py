def blockify_image(image_array, N):
    """
    Divide an image array into blocks of size (N*N).
    :param image_array: numpy array of image
    :param N: size of blocks (N*N)
    :return: list of blocks each of shape (N*N)
    """
    img_lenght, img_width = image_array.shape

    blocks = image_array.reshape(img_lenght // N, N, img_width // N, N)
    blocks = blocks.swapaxes(1, 2)

    return blocks
