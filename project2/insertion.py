from sort_core import swap

#
# INSERTION SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   sorted   = []
#   unsorted = array
# take element elt from unsorted one by one
#   insert elt into sorted and move it down
#   until it reaches its correct position
#
# NB: in the code below, index i represents the "border"
# between sorted and unsorted.


def sort(array):
    """ Non-destructive insertion sort:

    array is unchanged
    returns a sorted copy
    """
    res = array.copy()
    sort_inline(res)
    return res


def sort_inline(array):
    """ Inline insertion sort:
    modifies the input array directly
    """
    for i in range(len(array)):
        for j in range(i-1, -1, -1):
             if array[j] > array[j+1]:
                swap(array, j, j+1)
    return array


def sort_optimized(array):
    """ Inline insertion sort (slightly optimized):
    modifies the input array directly
    """
    for i in range(len(array)):
        j = i-1
        while (j >= 0) and array[j] > array[j+1]:
            swap(array, j, j+1)
            j -= 1
    return array
