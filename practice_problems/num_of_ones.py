"""
Count and return the number of ones in an array
"""



def num_of_ones(arr):
    """
     >>> num_of_ones([0, 0, 0, 1, 1])
     2
     >>> num_of_ones([0, 0, 0, 0, 1, 1, 1, 1])
     4
     >>> num_of_ones([0])
     0
     >>> num_of_ones([0, 1, 1, 1, 1, 1, 1, 1, 1])
     8
     >>> num_of_ones([1, 1, 1, 1, 1, 1, 1, 1, 1])
     9
     >>> num_of_ones([0, 0, 0, 0, 0])
     0
     >>> num_of_ones([0, 0, 0, 0, 1])
     1
    """

    # calculate the midpoint
    # initialize start, and end pointers

    start = 0
    end = len(arr) - 1

    if arr[0] == 1:
        return len(arr)

    # calculate the midpoint
    midpoint = (end - start) // 2

    while start < end:
        # if on one, check if previous number is zero, so you know it's the first one. Else, check lower end of array.
        if arr[midpoint] == 1:
            if arr[midpoint - 1] == 0:
                return len(arr) - midpoint
            else:
                end = midpoint
        else:
            # if on zero, check if next number is 1. If not, check higher end of array.
            if arr[midpoint + 1] == 1:
                return len(arr) - (midpoint + 1)
            else:
                start = midpoint

        # calculate new midpoint
        midpoint = start + (end - start) // 2

        # if start is equal to midpoint. Checking two elements.
        if start == midpoint:
            return 0


    return 0
