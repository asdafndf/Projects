# This code tells you the smallest number in an array
arr = [25, 11, 2, 75, 56]
def minimum_number(arr):
    min = arr[0]
    for x in range(0, len(arr)):
        if(arr[x] < min):
            min = arr[x]
    return(f"Smallest element present in given array: {min}"

# Smallest AND biggest and the same time (with 1 iteration)
def maximum_and_minium(numbers):
    min = numbers[0]
    max = numbers[0]
    for x in numbers:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min, max