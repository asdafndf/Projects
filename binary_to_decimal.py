# Turn a binary number to decimal

def method1(n):
    arr = [int(x) for x in str(n)]
    result = 0
    for x in arr:
        result = result * 2 + x
    return result

def method2(n):
    return int(str(n), 2)