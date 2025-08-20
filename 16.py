def euler_16(n):
    return sum(map(int, str(2**n)))

inputs = [15, 1000]
for n in inputs:
    print(f"{n}: {euler_16(n)}")
