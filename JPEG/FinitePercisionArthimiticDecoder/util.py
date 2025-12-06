import numpy as np
from collections import Counter


def calculate_frequencies(input_stream):
    element_counts = Counter(input_stream.tolist())  # Convert NumPy array to list
    return dict(element_counts)


def calculate_cumulative_frequency(symbol, frequency_dictionary):
    cumulative_frequency = 0
    for s in frequency_dictionary:
        cumulative_frequency += frequency_dictionary[s]
        if s == symbol:
            break
    return cumulative_frequency
