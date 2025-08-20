from functools import lru_cache

@lru_cache(maxsize=None)
def collatz(n):
    return 1 if n == 1 else 1 + collatz(n // 2 if n % 2 == 0 else 3 * n + 1)

print(collatz(13))
print(max(range(1, 1000000), key=collatz))
