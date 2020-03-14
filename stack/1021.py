
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        l = 0
        for i in S:
            if i==')': l-=1
            if l>0:
                res.append(i)
            if i=='(':
                l+=1
        return ''.join(res)