# How to raise a number to a power

def raise_to_power(base, power):
    result = 1
    count = 0
    while count < power:
        result = result * base
        count += 1
    return result

def raise_to_power2(base, power):
    result = 1
    for x in range(power):
        result = result * base
    return result

def raise_to_power3(base, power):
    return pow(base, power)