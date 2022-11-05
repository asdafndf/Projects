# Convert a decimal number to binary. The first one is my solution

def to_binary1(n):
    list_ = []
    while n > 0:
        list_.append(n % 2)
        n = n//2
    to_string = [str(x) for x in list_]
    return int("".join(to_string[::-1]))

# Better practices:

def to_binary2(n):
    return int(f"{n:b}")

def to_binary3(n):
    return int(bin(n)[2:])