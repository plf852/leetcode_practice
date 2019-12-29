#　主要在题目理解上．学会将问题进行转换，实际上是个偶数位排序和奇数位拼接的和
class Solution:
    def numSpecialEquivGroups(self, A) -> int:
        res = set()
        for i in A:
            res.add(''.join(sorted(i[::2])+sorted(i[1::2])))
        return len(res)