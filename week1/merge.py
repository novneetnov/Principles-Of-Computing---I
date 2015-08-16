# url : http://www.codeskulptor.org/#user39_MMUT83KjKI_8.py

"""
Merge function for 2048 game.
"""

import test_merge


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    return_line = [0]
    merge_flag = False

    for elem in line:
        if elem != 0:
            if return_line[-1] == elem and merge_flag is False:
                return_line[-1] = 2 * elem
                merge_flag = True
                continue
            else:
                return_line.append(elem)
            merge_flag = False

    return_line.pop(0)
    zeros_lst = [0] * (len(line) - len(return_line))
    return_line.extend(zeros_lst)

    return return_line

test_merge.run_suite(merge)