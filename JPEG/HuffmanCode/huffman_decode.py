# Function to decode Huffman-encoded data
def huffman_decode(encoded_data, root):
    """
    Decode the Huffman-encoded data
    :param encoded_data: Huffman-encoded data
    :param root: Huffman tree root
    :return: decoded data
    """
    decoded_data = []
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left  # Traverse left with '0'
        else:
            current_node = current_node.right  # Traverse right with '1'

        if current_node.symbol is not None:
            decoded_data.append(current_node.symbol)  # Append the symbol when a leaf node is reached
            current_node = root  # Reset to the root for the next symbol

    return decoded_data  # Return the decoded data
