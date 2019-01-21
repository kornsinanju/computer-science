from sort_core import swap

#
# BUBBLE SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   unsorted = array
#   sorted   = []
# repeatedly
#   scan through the unsorted array, moving larger elements up
#   until no swap occurs during a scan
#
# NB: in the code below, index n represents the "border"
# between unsorted and sorted.


def sort(array):
    """ Non-destructive bubblesort sort.    
    array is unchanged; returns a sorted copy
    """
    res = array.copy()
    sort_inline(res)
    return res


def sort_inline(array):
    """ Inline bubblesort sort.
    modifies the input array directly
    """
    # TODO (OPTIONAL): implement bubblesort sort
    # replace the lines below with your own code
    list.sort(array)
    return array

