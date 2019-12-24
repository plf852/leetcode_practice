class Solution:
    def defangIPaddr(self, address: str) -> str:
        strs = address.split('.')
        #return strs[0]+'[.]'+strs[1]+'[.]'+strs[2]+'[.]'+strs[3]
        return "[.]".join(strs) # 函数高级用法

s = Solution()
print(s.defangIPaddr("1.1.1.1"))
