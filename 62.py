from collections import defaultdict

def digit_signature(n):
    return tuple(sorted(str(n)))

def euler_62(n):
    cubes = defaultdict(list)
    k = 1
    while True:
        cube = k ** 3
        sig = digit_signature(cube)
        cubes[sig].append(cube)
        if len(cubes[sig]) == n:
            return min(cubes[sig])
        k += 1

inputs = [3, 5]
for n in inputs:
    print(f"{n}: {euler_62(n)}")
