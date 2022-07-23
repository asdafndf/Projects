# This code tells you the smallest number in an array
arr = [25, 11, 2, 75, 56]
def minimum_number(arr):
    min = arr[0]
    for x in range(0, len(arr)):
        if(arr[x] < min):
            min = arr[x]
    return("Smallest element present in given array: %s" % (min))
minimum_number(arr)