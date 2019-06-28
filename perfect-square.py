def numSquares(self, n):
    dp = [n for _ in range(n+1)]
    for i in range(n+1):
        if i**2 <= n:
            dp[i**2] = 1
        j = 1
        while j**2 < i:
            dp[i] = min(dp[i], dp[i-j**2] + 1)
            j +=1
    return dp[n]