# return the number of divisors a number has
def number_of_divisors(n):
    sqrt = n**0.5
    count = 0
    for x in range(1,int(sqrt)+1):
        if n%x == 0:
            count += 2
    if sqrt%1 == 0:
        return count - 1
    return count


