"""
Subarray sort
"""



import math
def subarray_sort(array):
    """
    >>> subarray_sort([3, 4, 8, 7, 10, 6, 17])
    [2, 5]
    >>> subarray_sort([3, 4, 8, 7, 20, 6 , 17])
    [2, 6]
    >>> subarray_sort([3, 4, 8, 7, 20, 6 , 17, 22, 14, 26])
    [2, 8]
    """

    # iterate through the array
    # when value at index is less than value at next index, set start pointer
    # keep track of the max at that stage. When you hit a value greater than maximum, set end pointer.
    # return start and end

    start = 0
    end = len(array)
    minimum = math.inf
    maximum = -math.inf

    first_start= 0
    final_start = 0
    final_end = 0

    # iterating through the array, and setting start pointer.
    for i in range(len(array) - 1):
        # if one element is greater than the next element --> unsorted.
        if array[i] > array[i + 1]:
            first_start += 1
            if first_start == 1:
                start = i

    # grab the maximum and minimum of the subarray.
    for i in range(start, end):
        if array[i] > maximum:
            maximum = array[i]
        if array[i] < minimum:
            minimum = array[i]


    for i in range(len(array)):
        if array[i] > minimum:
            final_start += 1
            if final_start == 1:
                start = i

    for j in range(len(array) - 1, -1, -1):
        if array[j] < maximum:
            final_end += 1
            if final_end == 1:
                end = j

    return [start, end]




