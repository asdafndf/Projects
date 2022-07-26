# %%
from math import *
def is_prime(n):
    if n == 1:
        return "%s is not a prime" % (n)
    for x in range(2,int(sqrt(n))+1):
        if (n % x) == 0:
            return "%s is not a prime" % (n)
        else:
            return "%s is a prime" % (n)
is_prime(2)

# %%
from math import *

def is_prime2(n):
    for i in range(2,int(sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True
is_prime2(2)


