from itertools import takewhile

def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

def euler_2(n):
    return sum(f for f in takewhile(lambda x: x <= n, fibonacci()) if f % 2 == 0)

print(euler_2(4000000))
