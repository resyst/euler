from itertools import accumulate, count
from math import isqrt

def num_divisors(n):
    return sum(1 if i * i == n else 2 for i in range(1, isqrt(n) + 1) if n % i == 0)

def triangular_numbers():
    return accumulate(count(1))

def euler_12(n):
    for k in triangular_numbers():
        if num_divisors(k) > n:
            return k

inputs = [5, 500]
for n in inputs:
    print(f"{n}: {euler_12(n)}")
