import numpy as np
from .util import calculate_cumulative_frequency, calculate_frequencies


def arithmetic_encode(input_stream, precision=32):
    """
    Encode a message using arithmetic coding.

    Parameters:
    - input_stream (numpy.ndarray): The input message to be encoded.
    - precision (int): The precision of the arithmetic coding (default is 32).

    Returns:
    - encoded_code (str): The binary-encoded message.
    - frequency_dict (dict): A dictionary containing symbol frequencies.
    """

    # Append termination symbol '!'
    input_stream = np.append(input_stream, np.array('!'))
    stream_size = len(input_stream)

    # Calculate symbol frequencies
    frequency_dict = calculate_frequencies(input_stream)

    # Initialization
    full_range = 2 ** precision
    half_range = full_range // 2
    quarter_range = half_range // 2
    lower_limit = 0
    upper_limit = full_range
    trails = 0
    encoded_code = []

    # Loop through symbols in the input stream
    for symbol in input_stream:
        frequency_symbol = frequency_dict[symbol]
        cumulative_frequency_high = calculate_cumulative_frequency(symbol, frequency_dict)
        cumulative_frequency_low = cumulative_frequency_high - frequency_symbol
        range_size = upper_limit - lower_limit

        # Update upper and lower limits based on cumulative frequencies
        upper_limit = lower_limit + range_size * cumulative_frequency_high // stream_size
        lower_limit = lower_limit + range_size * cumulative_frequency_low // stream_size

        # Binary scaling
        while True:
            if upper_limit < half_range:
                encoded_code.append('0')
                encoded_code.append('1' * trails)
                trails = 0
                lower_limit *= 2
                upper_limit *= 2
            elif lower_limit >= half_range:
                encoded_code.append('1')
                encoded_code.append('0' * trails)
                trails = 0
                lower_limit = 2 * (lower_limit - half_range)
                upper_limit = 2 * (upper_limit - half_range)
            elif lower_limit >= quarter_range and upper_limit < 3 * quarter_range:
                trails += 1
                lower_limit = 2 * (lower_limit - quarter_range)
                upper_limit = 2 * (upper_limit - quarter_range)
            else:
                break

    # Finalize encoding
    trails += 1
    if lower_limit <= quarter_range:
        encoded_code.append('0')
        encoded_code.append('1' * trails)
    else:
        encoded_code.append('1')
        encoded_code.append('0' * trails)

    # Convert the encoded code to a string
    encoded_code = ''.join(encoded_code)

    # Return the encoded code and symbol frequencies
    return encoded_code, frequency_dict
