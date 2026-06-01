from itertools import permutations

products = set()
for p in permutations('123456789'):
    s = ''.join(p)
    for i in range(1, 8):
        for j in range(i + 1, 9):
            a, b, c = int(s[:i]), int(s[i:j]), int(s[j:])
            if a * b == c:
                products.add(c)

print(sum(products))
