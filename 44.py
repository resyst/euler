from math import isqrt

def is_pentagonal(n):
    x = 24 * n + 1
    y = isqrt(x)
    if x != y * y:
        return False
    return (y + 1) % 6 == 0

def euler_44():
    best = float('inf')
    k = 1
    pp = 0
    while True:
        pk = k * (3 * k - 1) // 2
        if pp and pk - pp >= best:
            break
        for j in range(k - 1, 0, -1):
            pj = j * (3 * j - 1) // 2
            d = pk - pj
            if d >= best:
                break
            if is_pentagonal(pk + pj) and is_pentagonal(d):
                best = d
        pp = pk 
        k += 1 
    return best 

print(euler_44())
