# Turn a binary number to decimal

def binary_to_decimal(n):
    arr = [int(x) for x in str(n)]
    result = 0
    for x in arr:
        result = result * 2 + x
    return result

def binary_to_decimal(n):
    return int(str(n), 2)