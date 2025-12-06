import heapq  # Import the heapq module for the priority queue implementation


class HuffmanNode:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


# Function to build the Huffman tree from symbol frequencies
def build_huffman_tree(frequencies):
    heap = [HuffmanNode(symbol=s, frequency=f) for s, f in frequencies.items()]  # Create a heap with HuffmanNodes
    heapq.heapify(
        heap)  # Convert the list into a min-heap data structure, the min-heap -> follows the property of a complete binary tree in which the value of the internal node is smaller than or equal to the value of the children of that node

    while len(heap) > 1:
        left = heapq.heappop(heap)  # Pop the smallest node from the heap, note -> left is a HuffmanNode
        right = heapq.heappop(heap)  # Pop the second smallest node from the heap

        internal_node = HuffmanNode(frequency=left.frequency + right.frequency)  # Create a new internal node
        internal_node.left = left  # Assign the left child
        internal_node.right = right  # Assign the right child

        heapq.heappush(heap, internal_node)  # Push the new internal node back into the heap

    return heap[0]  # Return the root of the Huffman tree


# Function to generate Huffman codes from the Huffman tree
def generate_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}

    if node.symbol is not None:
        codes[node.symbol] = current_code
    else:
        generate_huffman_codes(node.left, current_code + "0", codes)  # Recursively traverse left with '0'
        generate_huffman_codes(node.right, current_code + "1", codes)  # Recursively traverse right with '1'

    return codes
