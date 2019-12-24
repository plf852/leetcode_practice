# -*- coding: UTF-8 -*-
# 本地测试通过，但是提交后超时
class Solution:
    def stoneGame(self, piles) -> bool:
        a = self.shou(piles)
        b = sum(piles) - a
        if a>b:
            return True
        else:
            return False

    def shou(self,piles):
        if len(piles)==0:
            return 0
        if piles[0]>piles[-1]:
            return piles[0] + max(self.shou(piles[2:]),self.shou(piles[1:-1]))
        else:
            return piles[-1] + max(self.shou(piles[0:-2]),self.shou(piles[1:-1]))

s = Solution()
print(s.stoneGame([4,5,6,7]))

# 动态规划解法
class Solution:
    def stoneGame(self, piles) -> bool:
        import numpy as np
        dp = np.zeros((len(piles),len(piles),2),dtype = np.int)
        for i in range(len(piles)):
            dp[i][i][0] = piles[i]

        for l in range(1, len(piles)):
            for i in range(len(piles)-1):
                j = i+l
                if j==len(piles):
                    break
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left>right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]

        return (dp[0][len(piles)-1][0]-dp[0][len(piles)-1][1])>0


s = Solution()
print(s.stoneGame([2,3,5,6]))
# 通过归纳法得知，alex总是赢，所以直接返回True