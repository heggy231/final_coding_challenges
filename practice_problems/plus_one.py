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
    >>> plus_one([9, 9])
    [1, 0, 0]
    """

    pointer = len(arr) - 1

    if arr[pointer] <= 8:
        arr[pointer] += 1
    else:
        while arr[pointer] > 8 and pointer >= 0:
            # checking on the first element, returning right then and there. 
            if pointer == 0:
                arr[pointer] = 0
                arr.insert(0, 1)
                return arr
            arr[pointer] = 0
            pointer -= 1
        arr[pointer] += 1






    return arr





