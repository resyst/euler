def euler_9(s: int):
    for a in range(1, s // 3 + 1):
        for b in range(a + 1, (s - a) // 2 + 1):
            c = s - a - b
            if c > b and a**2 + b**2 == c**2:
                yield a * b * c

print(next(euler_9(1000)))
