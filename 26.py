from math import isqrt

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, isqrt(n) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors

def euler_phi(n):
    if n == 1: return 1
    factors = prime_factors(n)
    phi = n
    for p in factors:
        phi = phi // p * (p - 1)
    return phi

def get_divisors(n):
    return sorted({1, n} | {j for i in range(2, isqrt(n) + 1) if n % i == 0 for j in (i, n // i)})

def multiplicative_order(a, n):
    if n == 1: return 0
    phi = euler_phi(n)
    for d in get_divisors(phi):
        if pow(a, d, n) == 1:
            return d

def optimized_cycle_length(d):
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    if d == 1:
        return 0
    return multiplicative_order(10, d)

def euler_26(max_d):
    max_length = max_denominator = 0
    for d in range(2, max_d):
        cycle = optimized_cycle_length(d)
        if cycle > max_length:
            max_length, max_denominator = cycle, d
    return max_denominator

inputs = [10, 1000]
for n in inputs:
    print(f"{n}: {euler_26(n)}")
