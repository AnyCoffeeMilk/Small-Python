n = 5
w = 15

goods = [[12, 4], [1, 2], [4, 10], [2, 1], [2, 2]]

dp = [[0 for i in range(w + 1)] for j in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, w+1):
        dp[i][j] = dp[i-1][j]
        if j >= goods[i-1][0]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-goods[i-1][0]] + goods[i-1][1])

print(dp[-1][-1])