# This code tells you the sum of the first n numbers
def summation(n):
    sum = 0
    for x in range(1, n + 1):
        sum = sum + x
    print("Sum of first %d numbers is: %d" % (n, sum))