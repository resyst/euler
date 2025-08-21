limit = 28124
sum_div = [0] * limit
for i in range(2, limit):
    sum_div[i] = 1
for i in range(2, limit):
    for j in range(i * 2, limit, i):
        sum_div[j] += i
abundants = [n for n in range(12, limit) if sum_div[n] > n]
is_abundant_sum = [False] * limit
for i in range(len(abundants)):
    if 2 * abundants[i] >= limit:
        break
    for j in range(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s >= limit:
            break
        is_abundant_sum[s] = True
result = sum(n for n in range(1, limit) if not is_abundant_sum[n])
print(result)
