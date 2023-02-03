# Determine if a given array is ascending or descending
def is_ascending(arr):
    """Determines if a given array is ascending"""
    for i in range(len(arr)-1):
        if arr[i] < arr[i + 1]:
            return True
        else:
            return False

def is_descending(arr):
    """Determines if a given array is descending"""
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            return True
        else:
            return False


