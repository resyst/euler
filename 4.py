def euler_4(n):
    min_factor = 10 ** (n - 1)
    max_factor = 10 ** n - 1
    max_palindrome = 0
    for i in range(max_factor, min_factor - 1, -1):
        if i * i <= max_palindrome:
            break
        products = (i * j for j in range(i, min_factor - 1, -1) if i * j > max_palindrome)
        for prod in products:
            if str(prod) == str(prod)[::-1]:
                max_palindrome = max(max_palindrome, prod)
    return max_palindrome

inputs = [2, 3]
for n in inputs:
    print(f"{n}: {euler_4(n)}")
