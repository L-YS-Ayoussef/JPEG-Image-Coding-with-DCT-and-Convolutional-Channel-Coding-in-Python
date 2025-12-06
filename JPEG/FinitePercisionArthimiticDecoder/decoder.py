# Importing necessary utility function
from .util import calculate_cumulative_frequency


# Main function for arithmetic decoding
def arithmetic_decode(encoded_code, frequency_dictionary, precision=32):
    """
    Decode an arithmetic encoded message.

    Parameters:
    - encoded_code (str): The binary-encoded message to be decoded.
    - frequency_dictionary (dict): A dictionary containing symbol frequencies.
    - precision (int): The precision of the arithmetic coding (default is 32).

    Returns:
    - decoded_message (list): The decoded message as a list of integers.
    """

    # Initialization
    code_size = len(encoded_code)
    encoded_code = [int(c) for c in encoded_code]
    stream_size = sum(frequency_dictionary.values())
    full = 2 ** precision
    half = full // 2
    quarter = half // 2
    low_range = 0
    high_range = full
    decoded_value = 0
    index = 1
    decoded_message = []

    # Decode initial value
    while index <= precision and index <= code_size:
        if encoded_code[index - 1] == 1:
            decoded_value = decoded_value + 2 ** (precision - index)
        index += 1

    flag = 1

    # Main decoding loop
    while flag:
        # Iterate through symbols in the frequency dictionary
        for symbol in frequency_dictionary:
            frequency_symbol = frequency_dictionary[symbol]
            cumulative_frequency_high = calculate_cumulative_frequency(symbol, frequency_dictionary)
            cumulative_frequency_low = cumulative_frequency_high - frequency_symbol
            range_size = high_range - low_range
            high_range_new = low_range + range_size * cumulative_frequency_high // stream_size
            low_range_new = low_range + range_size * cumulative_frequency_low // stream_size

            # Check if the decoded value falls within the current symbol's range
            if low_range_new <= decoded_value < high_range_new:
                decoded_message.extend([symbol])
                low_range = low_range_new
                high_range = high_range_new

                # Check for the termination symbol '!'
                if symbol == '!':
                    flag = 0
                break

        # Binary scaling and updating decoded value
        while True:
            if high_range < half:
                # Update ranges and decoded value for low range
                low_range *= 2
                high_range *= 2
                decoded_value *= 2
                if index <= code_size:
                    decoded_value += encoded_code[index - 1]
                    index += 1
            elif low_range >= half:
                # Update ranges and decoded value for high range
                low_range = 2 * (low_range - half)
                high_range = 2 * (high_range - half)
                decoded_value = 2 * (decoded_value - half)
                if index <= code_size:
                    decoded_value += encoded_code[index - 1]
                    index += 1
            elif low_range >= quarter and high_range < 3 * quarter:
                # Additional scaling for certain ranges
                low_range = 2 * (low_range - quarter)
                high_range = 2 * (high_range - quarter)
                decoded_value = 2 * (decoded_value - quarter)
                if index <= code_size:
                    decoded_value += encoded_code[index - 1]
                    index += 1
            else:
                break

    # Remove the termination symbol and convert symbols to integers
    decoded_message.pop()
    decoded_message = [int(float(c)) for c in decoded_message]

    # Return the decoded message
    return decoded_message
