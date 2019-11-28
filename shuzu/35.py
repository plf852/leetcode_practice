def searchInsert(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = int((left+right)*1.0/2)
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # 这个算是二分法的改进版，相比原来的二分法（只能返回存在或不存在），如果不存在这个元素，可以返回插入位置
    return left

print(searchInsert([1,3,5,6],7))