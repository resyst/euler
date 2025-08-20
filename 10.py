from math import isqrt

def euler_10(n):
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    return sum(i for i in range(n) if sieve[i])

inputs = [10, 2000000]
for n in inputs:
    print(f"{n}: {euler_10(n)}")
