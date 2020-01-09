# 关键是学会转化问题
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        snums = [s.index(i) for i in s]
        tnums = [t.index(i) for i in t]
        print(snums)
        print(tnums)
        return snums == tnums

s = Solution()
print(s.isIsomorphic("egg","add"))