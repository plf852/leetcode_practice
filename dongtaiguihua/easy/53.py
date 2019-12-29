# 动态规划算法
def maxSubArray(nums) -> int:
    msum = 0
    history_max = nums[0]
    for num in nums:
        if msum > 0:
            msum += num
        else:
            msum = num
        history_max = history_max if history_max>msum else msum
    return history_max

# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# 暴力法
def bl_maxSubArray(nums) -> int:
    history_max = nums[0]
    # 暴力1
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         sum = 0
    #         for k in range(i,j+1):
    #             sum += nums[k]
    #         if sum>history_max:
    #             history_max = sum

    # 暴力2
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum>history_max:
                history_max = sum
    return history_max

#print(bl_maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# 分治
def fz_maxSubArray(nums):
    if len(nums)==1:
        return nums[0]
    left_max = fz_maxSubArray(nums[0:len(nums)//2])
    right_max = fz_maxSubArray(nums[len(nums)//2:])

    max_l = nums[len(nums) // 2 - 1]
    tmp = 0
    for i in range(len(nums) // 2 - 1, -1, -1):
        tmp += nums[i]
        max_l = max(tmp, max_l)  # 之所以不能提早终止，是因为只有遍历完所有的值，才会找到最大的
    max_r = nums[len(nums) // 2]
    tmp = 0
    for i in range(len(nums) // 2, len(nums)):
        tmp += nums[i]
        max_r = max(tmp, max_r)

    return max(left_max,right_max,max_l+max_r)

print(fz_maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


#print(bl_maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
