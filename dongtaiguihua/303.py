# 解答错误
class NumArray:

    def __init__(self, nums):
        self.nums = nums
        length = (1 + len(nums))*len(nums) //2
        self.table = [None]*length

    def sumRange(self, i: int, j: int) -> int:
        if i>j:
            return 0
        if i == j:
            return self.nums[i]
        if i + 1 ==j:
            return self.nums[i] + self.nums[j]

        index = (len(self.nums)+len(self.nums)-i+1)*i // 2 + j-i
        if self.table[index] is None:
            mid = (i+j)//2
            self.table[index] = self.sumRange(i,mid-1) + self.sumRange(mid,j)  # 这里用中分就没有意义了

        return self.table[index]

na = NumArray([-8261,2300,-1429,6274,9650,-3267,1414,-8102,6251,-5979,-5291,-4616,-4703])
print(na.sumRange(2,11))
print(na.sumRange(2,2))
print(na.sumRange(3,3))
print(na.sumRange(4,5))
print(na.sumRange(6,7))
print(na.sumRange(8,8))
print(na.sumRange(9,9))
print(na.sumRange(10,11))
print('------------------')

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.table = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                self.table[i]=nums[i]
            else:
                self.table[i]=self.table[i-1]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.table[j]
        return self.table[j] - self.table[i-1]

na = NumArray([-8261,2300,-1429,6274,9650,-3267,1414,-8102,6251,-5979,-5291,-4616,-4703])
print(na.sumRange(2,11))
print(na.sumRange(2,2))
print(na.sumRange(3,3))
print(na.sumRange(4,5))
print(na.sumRange(6,7))
print(na.sumRange(8,8))
print(na.sumRange(9,9))
print(na.sumRange(10,11))