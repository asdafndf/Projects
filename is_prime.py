# In theory this code determines whether n is prime or not, however it has to be checked
from math import *
def is_prime(n):
    if n == 1:
        return False
    for x in range(2,int(sqrt(n))+1):
        if n % x == 0:
            return "%s is not a prime" % (n)
        else:
            return "%s is a prime" % (n)