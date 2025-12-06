import matplotlib.pyplot as plt

def save_image(original_image, decoded_image, compression_ratio, compression_mode):
    """
    Save the decoded image as jpg
    :param original_image: original image
    :param decoded_image: decoded image
    :return: None
    """
    # save decoded image as jpg file
    plt.imsave(f'compressed_image_({compression_mode.name}).jpg', decoded_image, cmap='gray')

    # show original image and decoded image in one figure and save it with titles
    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')
    fig.add_subplot(1, 2, 2)
    plt.imshow(decoded_image, cmap='gray')
    plt.title(f'Compressed Image ({compression_ratio}:1)')
    plt.show()