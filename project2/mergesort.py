#
# MERGE SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# recursively,
#   cut the array into two halves: left, right
#   sort each half
#   merge both halves
#

#
# Non-destructive sort:
#
# array is unchanged
# returns a sorted copy
#


def merge_rec(a, b):
    """ Merge of two sorted arrays (recursive version)
    
    IN:  sorted arrays a and b
    OUT: merging of a and b into one sorted array
    """
    if not a or not b or a[-1] < b[0]:
        return a + b
    if a[0] < b[0]:
        return [a[0]] + merge_rec(a[1:], b)
    return [b[0]] + merge_rec(a, b[1:])


def merge(a, b):
    """ Merge of two sorted arrays (iterative version)
    
    IN:  sorted arrays a and b
    OUT: merging of a and b into one sorted array
    """
    if not a or not b or a[-1] < b[0]:
        return a + b
    res = [ a[0] for i in range(len(a)+len(b)) ]
    next_a = 0
    last_a = len(a)-1
    last_b = len(b)-1
    for i in range(len(res)):
        next_b = i - next_a
        if (next_a > last_a) or ((next_b <= last_b) and (a[next_a] > b[next_b])):
            res[i] = b[next_b]
        else:
            res[i] = a[next_a]
            next_a += 1
    return res


def sort(array):
    """ Sorting function (merge sort)
    IN: arbitrary array
    OUT: sorted array
    """
    # TODO *MANDATORY* for project 2
    # replace the lines below with your own code
    list.sort(array)
    return array


