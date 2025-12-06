import numpy as np
from JPEG.HuffmanCode.huffman_decode import huffman_decode
from JPEG.ZigzagTransform.reverse_zigzag_transform import reverse_zigzag_transform
from JPEG.RunLength.Run_Length_Decocder import run_length_decoder
from JPEG.Quantizer.dequantize import dequantize
from JPEG.DCT.IDCT import IDCT
from JPEG.DCT.IDCT_Basis import IDCT_Basis
from JPEG.Blockify.deblockify_image import deblockify_image
from JPEG.FinitePercisionArthimiticDecoder.decoder import arithmetic_decode

def decoder(encoded_image, N, CompressionMode, VerticalPadding, HoriziontalPadding, HuffmanTree, no_vertical_blocks,no_horizontal_blocks,CompressionTechnique):
    """
    Decode the encoded image
    :param encoded_image: encoded image
    :param N: block size (N*N)
    :param CompressionMode: Compression mode (HIGH, LOW)
    :param VerticalPadding: Vertical padding length
    :param HoriziontalPadding: Horizontal padding length
    :param HuffmanTree: Huffman tree used for encoding
    :param no_vertical_blocks: Number of vertical blocks
    :param no_horizontal_blocks: Number of horizontal blocks
    :return: decoded image
    """
    # [1] apply Entropy decoding to encoded image
    if CompressionTechnique == CompressionTechnique.ARITHMETIC:
        entropy_decoded_image = np.array(arithmetic_decode(encoded_image, HuffmanTree))
    else:
        entropy_decoded_image = np.array(huffman_decode(encoded_image,HuffmanTree))
    
    # [2] apply run-length decoding
    runlength_decoded_image = run_length_decoder(entropy_decoded_image, no_vertical_blocks, no_horizontal_blocks, N)
    
    # [3] apply reverse zigzag transform (1D to 2D)
    #zigzag_transformed_image = np.zeros((no_vertical_blocks,no_horizontal_blocks,N,N))
    blocks = np.zeros((no_vertical_blocks, no_horizontal_blocks ,N,N))

    # image_total_pixels = no_vertical_blocks*no_horizontal_blocks*N*N

    index = 0
    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            block = reverse_zigzag_transform(runlength_decoded_image[index:index+N*N],N)
            blocks[i][j] = block.reshape((N, N))
            index += N*N

    # [4] apply dequantization to each block

    dequantized_blocks = np.zeros(blocks.shape)

    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            dequantized_blocks[i][j] = dequantize(blocks[i][j], CompressionMode)

    # [5] apply IDCT to each block
    idct_basis = np.zeros((N,N,N,N))

    for x in range(N):
        for y in range(N):
            idct_basis[x][y] = IDCT_Basis(x,y,N)

    idct_blocks = np.zeros(blocks.shape)

    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            idct_blocks[i][j] = IDCT(dequantized_blocks[i][j], idct_basis)

    # [6] deblockify the image
    decoded_image = deblockify_image(idct_blocks)
    return decoded_image[:decoded_image.shape[0] - VerticalPadding, :decoded_image.shape[1] - HoriziontalPadding]
