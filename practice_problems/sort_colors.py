"""
Sorting colors
"""


def sorting_colors(input):
    """
    >>> sorting_colors([2, 0, 1, 2, 1, 0])
    [0, 0, 1, 1, 2, 2]
    >>> sorting_colors([1, 2, 2, 0])
    [0, 1, 2, 2]
    >>> sorting_colors([1, 0, 2, 1, 1])
    [0, 1, 1, 1, 2]
    """

    # time complexity: O(N)
    # space complexity: O(1)

    colors = {}

    for color in input:
        colors[color] = colors.setdefault(color, 0) + 1

    for i in range(colors[0]):
        input[i] = 0

    for i in range(colors[0], colors[0] + colors[1]):
        input[i] = 1

    for i in range(colors[0] + colors[1], colors[0] + colors[1] + colors[2]):
        input[i] = 2



    return input


