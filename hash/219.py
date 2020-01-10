# 转化思路
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table:
                return True
            table[nums[i]] = 1
            if len(table) > k:
                table.pop(nums[i-k])
        return False