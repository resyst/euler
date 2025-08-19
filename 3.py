def prime_factors(n):
    while n % 2 == 0:
        yield 2
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            yield i
            n //= i
        i += 2
    if n > 1:
        yield n

def euler_3(n):
    return max(prime_factors(n))

print(euler_3(600851475143))
