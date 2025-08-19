def euler_1(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

inputs = [10, 1000]
for n in inputs:
    print(f"{n}: {euler_1(n)}")
