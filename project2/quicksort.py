#
# QUICKSORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# recursively,
#   take one value from the array as pivot
#   split the remainder of the array into two arrays:
#      left array with values smaller than pivot
#      right array with values larger than pivot
#   sort left and right independently
#   combine left, pivot, right into a sorted array
#
# NB: in practice, the way to chose the pivot is very
# significant to ensure good performance. However, in
# this lecture, we make a naive choice in order to keep
# the discussion simple and focus instead on the core
# idea of the algorithm.

#
# Non-destructive sort:
#
# array is unchanged
# returns a sorted copy
#

def sort(array):
    """ Sorting function (quicksort)
    IN: arbitrary array
    OUT: sorted array
    """
    if len(array)  < 2: return array
    if len(array) == 2: return [min(array), max(array)]

    pivot = array[0]
    tail  = array[1:]
    left  = [ v for v in tail if v < pivot ]
    right = [ v for v in tail if v >= pivot ]
    return sort(left) + [ pivot ] + sort(right)

