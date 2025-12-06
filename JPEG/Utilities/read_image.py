from PIL import Image
from JPEG.Utilities import save_image
import numpy as np

def read_image(image_path, N):
    """
    Read image and convert it to a numpy array in grayscale
    :param image_path: path to the image
    :param N: block size (N*N)
    :return: image array, and padding length and width
    """

    # Load the image
    image = Image.open(image_path)

    #image to gray scale
    image = image.convert('L')

    image_array = np.array(image)

    img_lenght, img_width = image_array.shape

    padding_length = 0
    padding_width = 0

    # check if the image is divisible by N and zero pad if necessary
    if img_lenght % N != 0:
        padding_length = N - img_lenght % N
        image_array = np.concatenate((image_array, np.zeros((padding_length, img_width))), axis=0)

    if img_width % N != 0:
        padding_width = N - img_width % N
        image_array = np.concatenate((image_array, np.zeros((img_lenght, padding_width))), axis=1)
    
    return image_array, padding_length, padding_width