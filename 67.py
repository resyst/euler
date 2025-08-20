def euler_67(triangle):
    dp = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        dp = [triangle[i][j] + max(dp[j], dp[j + 1]) for j in range(len(triangle[i]))]
    return dp[0]

with open('0067_triangle.txt') as f:
    triangle = [list(map(int, line.split())) for line in f.readlines()]

print(euler_67(triangle))
