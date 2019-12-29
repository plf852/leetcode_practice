def minPathSum(grid) -> int:
    import numpy as np
    m,n = np.shape(grid)
    dp = np.zeros((m,n),dtype=np.int)

    for i in range(0,m):
        for j in range(0,n):
            dp[i][j] = grid[i][j]
            if i-1<0 and j-1>=0:
                dp[i][j] += dp[i][j-1]
            elif i-1>=0 and j-1<0:
                dp[i][j] += dp[i-1][j]
            elif i-1>=0 and j-1>=0:
                dp[i][j] += min(dp[i-1][j],dp[i][j-1])

    return dp[m-1][n-1]

#在原始数据上进行操作
def minPathSum(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    if m == 0 or n == 0:
        return 0
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[m - 1][n - 1]

print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))