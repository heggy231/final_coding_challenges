


def common_substrings(string1, string2):
    """
    >>>sorted(common_substrings("AAABBBCDC", "CDCAAABBB"))
    ['AAA', 'AAB', 'ABB', 'CDC']

    """
    # find all 3 letter combinations of string1 -- > set
    # find all 3 letter combinations of string2 -- > set
    # set math --> remove differences
    # convert to list, return

    start = 0
    end = 0
    counter = 0
    three_letter_combo_1 = ""
    three_letter_combo_2 = ""
    string1_set = set()
    string2_set = set()
    while start < len(string1) and end < len(string1):
        three_letter_combo_1 += string1[end]
        three_letter_combo_2 += string2[end]
        counter += 1
        end += 1

        if counter == 3:
            string1_set.add(three_letter_combo_1)
            string2_set.add(three_letter_combo_2)
            counter = 0
            start += 1
            end = start
            three_letter_combo_1 = ""
            three_letter_combo_2 = ""

    return list(string1_set & string2_set)