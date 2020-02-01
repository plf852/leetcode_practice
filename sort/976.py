class Solution:
    def largestPerimeter(self, A) -> int:
        if len(A)<3:
            return 0
        for i in range(len(A)):
            mmax = 0
            mindex = -1
            for j in range(i,len(A)):
                if A[j]>mmax:
                    mmax = A[j]
                    mindex = j
            tmp = A[i]
            A[i] = A[mindex]
            A[mindex] = tmp
            if i>=2 and A[i]+A[i-1]>A[i-2]:  # 利用冒泡排序的特点，减少计算量
                return A[i]+A[i-1]+A[i-2]
        return 0