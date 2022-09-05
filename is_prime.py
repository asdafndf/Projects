# This code determines whether n is prime or not

from math import *
def is_prime(n):
    if n == 1:
        return f"{n} is not a prime"
    for x in range(2,int(sqrt(n))+1):
        if (n % x) == 0:
            return f"{n} is not a prime"
    return f"{n} is a prime"