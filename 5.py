from math import lcm

def euler_5(n):
    return lcm(*range(1, n + 1))

print(euler_5(20))
