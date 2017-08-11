
def ascending_binary(array):
    """
    >>> ascending_binary([1, 2, 3])
    [1, 2, 3]

    >>> ascending_binary([5, 3, 7, 10, 14])
    [3, 5, 10, 7, 14]
    """
    # initialize a hash
    binaries = {}
    # convert each int in array into binary

    binary_sorted_list = []

    for integer in array:
        bit_string_integer = list("{0:b}".format(integer))
        count = 0
        for char in bit_string_integer:
            if char == "1":
                count += 1
        if count not in binaries:
            binaries[count] = [integer]
        else:
            binaries[count].append(integer)

    for key, value in sorted(binaries.items()):
        sorted_values = sorted(value)
        for value in sorted_values:
            binary_sorted_list.append(value)




    return binary_sorted_list

