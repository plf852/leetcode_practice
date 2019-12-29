class Solution:
    def divisorGame(self, N) -> bool:
        if N==1:
            return False
        if N%2 == 0:
            return True
        else:
            return self.divisorGame(N-2)

s = Solution()
print(s.divisorGame(5))