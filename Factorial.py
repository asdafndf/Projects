# This code gives you n!. For negative numbers it doesn't work

def factor(n):
    product = 1
    if n < 0:
        return f"{n} is negative, sorry"
    else:
        for x in range(1,n+1):
            product *= x
    return f"{n}! equals {product}"

# You can also import:
from math import *
def factor2(n):
    return factorial(n)
factor2(4)