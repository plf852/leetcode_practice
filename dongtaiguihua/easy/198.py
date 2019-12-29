# https://leetcode-cn.com/problems/house-robber/


# 时间超限
def rob(nums) -> int:
    if len(nums) == 0:
        return 0
    if len(nums)==1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)

    return max(nums[0] + rob(nums[2:]),rob(nums[1:]))


print(rob([1,2,3,1]))

# 分治
def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums)==1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)

    mid = len(nums)//2
    return max(nums[mid]+rob(nums[0:mid-1])+rob(nums[mid+2:]),rob(nums[0:mid])+rob(nums[mid+1:]))

print(rob([1,2,3,1]))

# 动态规划
def rob(nums):
    # d[n] = max(d[n-1],d[n-2]+num)
    dn_2 = 0
    dn_1 = 0
    for num in nums:
        tmp = dn_1
        dn_1 = max(dn_2 + num,dn_1)
        dn_2 = tmp
    return dn_1

print(rob([1,2,3,1]))