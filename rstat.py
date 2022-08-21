from numpy import median


def mmm(arr):
    """Write to STDOUT minimum, median and maximum of array.

    In future let's check, if it's possible in python to make it like .toString in Java - so it would return arr of
    ints, but we could make nice output like this with right method.


    :param arr: array with type that can be ordered
    """
    print("minimum: {}".format(min(arr)))
    print("median: {}".format(median(arr)))
    print("maximum: {}".format(max(arr)))
