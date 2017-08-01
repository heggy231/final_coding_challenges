"""
Plus one problem
"""


def plus_one(arr):
    """
    Given an array of positive integers, return an array that just adds one to the number.

    Time complexity: O(N)
    Space complexity: O(1)

    >>> plus_one([1,2,3])
    [1, 2, 4]
    >>> plus_one([1, 9])
    [2, 0]
    >>> plus_one([1, 9, 9])
    [2, 0, 0]
    """

    pointer = len(arr) - 1

    if arr[pointer] <= 8:
        arr[pointer] += 1
    else:
        while arr[pointer] > 8:
         arr[pointer] = 0
         pointer -= 1
        arr[pointer] += 1




    return arr





