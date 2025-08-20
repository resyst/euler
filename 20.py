from math import factorial

def euler_20(n):
    return sum(map(int, str(factorial(n))))

inputs = [10, 100]
for n in inputs:
    print(f"{n}: {euler_20(n)}")
