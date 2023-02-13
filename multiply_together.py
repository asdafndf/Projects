# Given a number, these function return the product of its digits
def multiply_together_1(number):
    """
    Calculate the product of the digits of a number.
    Input: int
    """
    n = str(number)
    product = 1
    for x in n:
        product *= int(x)
    return product

from math import prod

def multyply_together_2(number):
    """
    Calculate the product of the digits of a number.
    Input: int
    """
    return prod(int(x) for x in str(number))


