# Is x an integer? This code will tell.

def is_it_int(x):
    return x % 1 == 0

def is_it_int2(x):
    return int(x) == x

# Only works with integers if a 0 is given after the decimal point
def is_it_int3(x):
    return x.is_integer()