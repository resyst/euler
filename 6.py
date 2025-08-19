def euler_6(n):
    sum_n = n * (n + 1) // 2
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    return sum_n**2 - sum_sq

inputs = [10, 100]
for n in inputs:
    print(f"{n}: {euler_6(n)}")
