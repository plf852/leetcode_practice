# -*- coding: UTF-8 -*-
# 第一次自己用暴力统计1的办法也可以ac
# 第二种动态规划思路
# 当i为奇数，结果等于i-1偶数中1的数量加上最后那个1 result[i] = result[i-1] + 1
# 当i为偶数，结果等于i/2偶数中1的数量  result[i] = result[i//2]
def countBits( num: int):
    result=[0]*(num+1)
    for i in range(1,num+1):
        if i%2==1:
            result[i] = result[i-1] + 1
        else:
            result[i] = result[i//2]
    return result

print(countBits(5))
