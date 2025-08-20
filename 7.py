from itertools import count, islice
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def euler_7(n):
    primes = (num for num in count(2) if is_prime(num))
    return next(islice(primes, n - 1, n))

inputs = [6, 10001]
for n in inputs:
    print(f"{n}: {euler_7(n)}")
