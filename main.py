from JPEG.Utilities.read_image import read_image
from JPEG.DEFS import CompressionMode,CompressionTechnique
from JPEG.encoder import encoder
import numpy as np
from JPEG.Utilities.calculate_compression_ratio import calculate_comprrssion_ratio
from JPEG.decoder import decoder
from JPEG.Utilities.save_image import save_image
import matplotlib.pyplot as plt
from Conv.communication_link import communication_link


def main():
    # ==================== Read Image =======================
    N = 8
    image_path = "./Asssets/palestine.jpg"
    image_array, vertical_padding, horizontal_padding = read_image(image_path, N)

    # ==================== Encode Image =======================
    compression_mode = CompressionMode.LOW
    compression_technique = CompressionTechnique.ARITHMETIC
    encoded_data, huffman_tree, no_vertical_blocks, no_horizontal_blocks = encoder(image_array, N, compression_mode,compression_technique)

    # ==================== Communication Link =======================
    K = 3
    generator_polynomials = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    fc = 0.1
    Ab = 1
    Tb = 100
    n = 1000
    snr_start = -40
    snr_end = -10
    snr_step = 1
    block_size = 64

    channel_decoded_signal_high_snr, channel_decoded_signal_medium_snr, channel_decoded_signal_low_snr, \
    restored_src_encoded_bit_seq_high_snr, restored_src_encoded_bit_seq_medium_snr, restored_src_encoded_bit_seq_low_snr = \
    communication_link(encoded_data, generator_polynomials, K, fc, Ab, Tb, n, snr_start, snr_end,
                                              snr_step, block_size)

    # ==================== Decode Image =======================
    # With Channel Encoding
    decoded_image_channel_high = decoder(channel_decoded_signal_high_snr, N, compression_mode, vertical_padding, horizontal_padding,
                            huffman_tree, no_vertical_blocks, no_horizontal_blocks,compression_technique)
    decoded_image_channel_medium = decoder(channel_decoded_signal_medium_snr, N, compression_mode, vertical_padding, horizontal_padding,
                            huffman_tree, no_vertical_blocks, no_horizontal_blocks,compression_technique)
    decoded_image_channel_low = decoder(channel_decoded_signal_low_snr, N, compression_mode, vertical_padding, horizontal_padding,
                            huffman_tree, no_vertical_blocks, no_horizontal_blocks,compression_technique)

    # Without Channel Encoding
    decoded_image_src_high = decoder(restored_src_encoded_bit_seq_high_snr, N, compression_mode, vertical_padding, horizontal_padding,
                            huffman_tree, no_vertical_blocks, no_horizontal_blocks,compression_technique)
    decoded_image_src_medium = decoder(restored_src_encoded_bit_seq_medium_snr, N, compression_mode, vertical_padding, horizontal_padding,
                            huffman_tree, no_vertical_blocks, no_horizontal_blocks,compression_technique)
    decoded_image_src_low = decoder(restored_src_encoded_bit_seq_low_snr, N, compression_mode, vertical_padding, horizontal_padding,
                            huffman_tree, no_vertical_blocks, no_horizontal_blocks,compression_technique)

    # ==================== Calculate Compression Ratio =======================
    compression_ratio = calculate_comprrssion_ratio(image_array, encoded_data)
    print(f"Compression ratio: {compression_ratio}:1")

    # ==================== Show and Save Image =======================
    # save the decoded image as jpg

    original_image = image_array[:decoded_image_channel_high.shape[0] - vertical_padding,
                     :decoded_image_channel_high.shape[1] - horizontal_padding]

    # plot the 6 restored images in one plot (4 * 2) and let the original image occupy the whole first row
    fig, ax = plt.subplots(2, 4)

    ax[0, 0].imshow(original_image, cmap='gray')
    ax[0, 0].set_title('Original Image')

    # High SNR
    ax[0, 1].imshow(decoded_image_channel_high, cmap='gray')    
    ax[0, 1].set_title('Decoded Image with Channel Encoding (High SNR)', fontsize=8)
    ax[1, 1].imshow(decoded_image_src_high, cmap='gray')
    ax[1, 1].set_title('Decoded Image without Channel Encoding (High SNR)', fontsize=8)

    # Medium SNR
    ax[0, 2].imshow(decoded_image_channel_medium, cmap='gray')
    ax[0, 2].set_title('Decoded Image with Channel Encoding (Medium SNR)', fontsize=8)
    ax[1, 2].imshow(decoded_image_src_medium, cmap='gray')
    ax[1, 2].set_title('Decoded Image without Channel Encoding (Medium SNR)', fontsize=8)

    # Low SNR
    ax[0, 3].imshow(decoded_image_channel_low, cmap='gray')
    ax[0, 3].set_title('Decoded Image with Channel Encoding (Low SNR)', fontsize=8)
    ax[1, 3].imshow(decoded_image_src_low, cmap='gray')
    ax[1, 3].set_title('Decoded Image without Channel Encoding (Low SNR)', fontsize=8)
    plt.show()

    # save_image(original_image, decoded_image, compression_ratio, compression_mode)


if __name__ == "__main__":
    main()
