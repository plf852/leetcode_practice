class Solution:
    def removeElement(self, nums, val: int) -> int:
        real = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[real]=nums[i]
                real+=1
        return real
s = Solution()
print(s.removeElement([4,2,3,4],4))
class Solution:  #当val比较少时，相比第一种，可以减少复制次数
    def removeElement(self, nums, val: int) -> int:
        i = 0
        n = len(nums)
        while i<n:
            if nums[i]==val:
                nums[i]=nums[n-1]
                n-=1
            else:
                i+=1
        return n