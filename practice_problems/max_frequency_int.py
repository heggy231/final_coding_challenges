"""
Maximum frequency integer
"""


def max_frequency_int(input):
    """
    >>> max_frequency_int([-2, -2, -2, -2, 4, 5])
    -2
    >>> max_frequency_int([])
    """

    if len(input) == 0:
        return

    int_frequencies = {}

    most_occurring_int = input[0]
    max_count = 0

    for integer in input:
        int_frequencies[integer] = int_frequencies.get(integer, 0) + 1
        if int_frequencies[integer] > max_count:
            max_count = int_frequencies[integer]
            most_occurring_int = integer

    return most_occurring_int





