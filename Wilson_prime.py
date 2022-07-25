# This code determines whether a number is Wilson prime or not. 

from math import *
def am_i_wilson(n):
    for x in range(2,ceil(sqrt(n))):
        if n % x == 0:
            return False
    if (n-1) <= 0:
        return False
    else:
        return (factorial(n-1)+1) % (n*n) == 0