# my solutions to the "Perfect Number Verifier" kata at codewars.com

# This is O(n)
def is_perfect(n):
    half_plus_one = int(n/2)+1
    divisors = [x for x in range(1, half_plus_one) if n % x == 0]
    return sum(divisors) == n

# This is O(sqrt(n))
def is_perfect(n):
    if n == 1:
        return False
    sqrt = int(n**0.5)
    divisors_1 = [x for x in range(2, sqrt+1) if n % x == 0]
    divisors_all = divisors_1.copy()
    for x in divisors_1:
        divisors_all.append(n/x)
    return 1 + sum(divisors_all) == n



