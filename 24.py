from math import factorial

d = list(range(10))
n = 1000000 - 1
p = []

while d:
    f = factorial(len(d) - 1)
    p.append(d.pop(n // f))
    n %= f

result = ''.join(map(str, p))
print(result)
