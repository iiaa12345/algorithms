n, W = list(map(int, input().split()))

w = []
p = []
for i in range(n):
    wt, pt = list(map(int, input().split()))
    w.append(wt)
    p.append(pt)

dp = [[0 for i in range(n + 1)] for j in range(W + 1)]

for i in range(1, W + 1):
    for j in range(1, n + 1):
        if i - w[j - 1] >= 0:
            dp[i][j] = max(dp[i][j - 1], dp[i - w[j - 1]][j - 1] + p[j - 1])
        else:
            dp[i][j] = dp[i][j - 1]
            
print(dp)
