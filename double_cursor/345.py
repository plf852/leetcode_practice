
class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        table = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        head = 0
        tail = len(res)-1
        while head<tail:
            while res[head] not in table and head<tail:head+=1 #head<tail 防止不存在元音字母导致的数组越界
            while res[tail] not in table and head<tail:tail-=1
            if head<tail: # 防止数组越界
                tmp = res[head]
                res[head]= res[tail]
                res[tail]=tmp
                head += 1
                tail -= 1
        return ''.join(res)