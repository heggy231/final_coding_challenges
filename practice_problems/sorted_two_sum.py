"""
Sorted two sum problem
"""

def sorted_two_sum(array, target):
    """
    >>> sorted_two_sum([-5, 1, 3, 6, 7], -2)
    [0, 2]

    >>> sorted_two_sum([1, 9, 10], 8)
    [-1, -1]
    >>> sorted_two_sum([-1, -2], 5)
    [-1, -1]

    """

    # have two pointers --> one from the start and one from the end.
    # add up integers at pointers. If too large, decrement end.
    # If too small, add from beginning

    start = 0
    end = len(array) - 1

    while start < end:
        potential_sum = array[start] + array[end]
        if potential_sum < target:
            start += 1
        elif potential_sum > target:
            end -= 1
        else:
            return [start, end]

    return [-1, -1]

