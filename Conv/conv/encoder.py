from Conv.util.util import encode_sequence_with_polynomial, divide_into_blocks


def convert_sequence_to_string(sequence):
    """
    Convert a list of sequences into a single string.

    Parameters:
    - sequence (list): List of sequences.

    Returns:
    - S (list): List of characters representing the converted sequence.
    """
    S = []
    for i in range(len(sequence[0])):
        for j in range(len(sequence)):
            S.append(sequence[j][i])
    return S


def encode(A, generator_polynomials, k):
    """
    Encode a binary sequence using a set of generator polynomials and a given block size.

    Parameters:
    - A (str): Binary sequence to be encoded.
    - generator_polynomials (list): List of generator polynomials for encoding.
    - k (int): Block size for encoding.

    Returns:
    - encoded_sequence_string (list): List of characters representing the encoded sequence.
    """
    A = '0' * (k - 1) + A
    encoded_sequences = []

    # Iterate through each generator polynomial for encoding.
    for polynomial in generator_polynomials:
        C = ''

        # Iterate through each block of the binary sequence.
        for i in range(len(A) - k + 1):
            curr_list = A[i:i + k]
            curr_list = curr_list[::-1]

            # Encode the current block using the specified polynomial.
            C += encode_sequence_with_polynomial(curr_list, polynomial)

        # Append the encoded sequence for the current polynomial.
        encoded_sequences.append(C)

    # Convert the list of encoded sequences into a single string.
    encoded_sequence_string = convert_sequence_to_string(encoded_sequences)

    return encoded_sequence_string


def encode_all_blocks(blocks, generator_polynomials, k):
    """
    Encode a list of blocks using a set of generator polynomials and a given block size.

    Parameters:
    - blocks (list): List of binary blocks to be encoded.
    - generator_polynomials (list): List of generator polynomials for encoding.
    - k (int): Block size for encoding.

    Returns:
    - encoded_sequences (list): List of integers representing the encoded sequences.
    """
    encoded_sequences = []  # Initialize an empty list to store the encoded sequences.
    # Iterate through each block in the input list of blocks.
    for block in blocks:
        # Encode the current block using the encode function.
        sequence = encode(block, generator_polynomials, k)
        # Extend the list of encoded sequences with the current encoded block sequence.
        encoded_sequences.extend(sequence)
    # Flatten the list of strings and convert each character to an integer.
    encoded_sequences = [int(char) for string in encoded_sequences for char in string]
    return encoded_sequences


def channel_encoder(A, generator, k, block_size):
    """
    Encode a message using a channel encoder with a given generator polynomial, block size, and message.

    Parameters:
    - A (str): Binary message to be encoded.
    - generator (list): List of generator polynomials for encoding.
    - k (int): Block size for encoding.
    - block_size (int): Size of each block for encoding.

    Returns:
    - encoded_message (list): List of integers representing the encoded message.
    """
    # Divide the message into blocks using the divide_into_blocks function.
    blocks = divide_into_blocks(A, block_size)

    # Use the encode_all_blocks function to encode each block with the given generator polynomial and block size.
    encoded_message = encode_all_blocks(blocks, generator, k)

    return encoded_message
