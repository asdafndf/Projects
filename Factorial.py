# This code gives you n!. For negative numbers it doesn't work

def factor(n):
    product = 1
    if n < 0:
        return "%s is negative, sorry" % (n)
    else:
        for x in range(1,n+1):
            product = product * x
    return "%s! equals %s" % (n,product)

# You can also import:
from math import *
def factor2(n):
    return factorial(n)
factor2(4)