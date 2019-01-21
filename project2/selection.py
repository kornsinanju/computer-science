from sort_core import swap

#
# SELECTION SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   sorted   = []
#   unsorted = array
# iteratively,
#   remove the smallest element of unsorted
#   add it at the end of sorted
#
# NB: in the code below, index i represents the "border"
# between sorted and unsorted.
#

def sort(array):
    """ Non-destructive bubblesort sort.    
    array is unchanged; returns a sorted copy
    """
    res = array.copy()
    sort_inline(res)
    return res


def sort_inline(array):
    """ Inline selection sort.
    modifies the input array directly
    """
    # TODO (OPTIONAL): implement selection sort
    # replace the lines below with your own code
    list.sort(array)
    return array

