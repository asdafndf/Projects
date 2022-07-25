# In theory this code determines whether n is a Wilson prime or not, but it has to be tested.

from math import *
def am_i_wilson(n):
    return (factorial(n-1)+1) % pow(n,2) == 0 

def am_i_wilson(n):    
    def factorial(n):
        product = 1
        for x in range(1,n+1):
            product = product * x
        return product
    return (factorial(n-1)+1) % n*n == 0