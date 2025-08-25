def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def euler_25(digits):
    for index, fib in enumerate(fibonacci(), start=1):
        if len(str(fib)) >= digits:
            return index


inputs = [3, 1000]
for n in inputs:
    print(f"{n}: {euler_25(n)}")
