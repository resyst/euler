from math import comb

def euler_15(n):
    return comb(n + n, n)

inputs = [2, 20]
for n in inputs:
    print(f"{n}: {euler_15(n)}")
