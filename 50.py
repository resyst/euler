from math import isqrt

def euler_50(limit):
    sieve = [True] * limit
    sieve[0] = False
    sieve[1] = False
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    prefix = [0]
    for i, p in enumerate(sieve):
        if p:
            prefix.append(prefix[-1] + i)

    n = len(prefix) - 1
    max_len = 0
    max_prime = 0

    for start in range(n):
        for length in range(1, n - start + 1):
            s = prefix[start + length] - prefix[start]
            if s >= limit:
                break
            if length > max_len and sieve[s]:
                max_len = length
                max_prime = s

    return max_prime

inputs = [100, 1000, 1_000_000]
for limit in inputs:
    print(f"{limit}: {euler_50(limit)}")
