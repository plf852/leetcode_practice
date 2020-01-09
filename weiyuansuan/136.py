# 利用异或的性质
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = 0
        for i in nums:
            d ^= i
        return d