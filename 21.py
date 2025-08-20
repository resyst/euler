from math import isqrt

def sum_proper_divisors(n):
    return 1 + sum(i + (n // i if n // i != i else 0) for i in range(2, isqrt(n) + 1) if n % i == 0)

def euler_21(n):
    div_sums = [0] * n
    for i in range(1, n):
        for j in range(i, n, i):
            div_sums[j] += i
    amicables = set()
    for a in range(1, n):
        b = div_sums[a] - a
        if b != a:
            db = div_sums[b] - b if b < n else sum_proper_divisors(b)
            if db == a:
                amicables |= {a, b} if b < n else {a}
    return sum(amicables)

inputs = [220, 284]
for n in inputs:
    print(f"{n}: {sum_proper_divisors(n)}")

print(euler_21(10000))
