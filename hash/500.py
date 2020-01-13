
class Solution:
    def findWords(self, words):
        table = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        res = []
        for i in words:
            last = None
            flag = True
            for j in i:
                if ord('A')<=ord(j)<=ord('Z'):
                    j = chr(ord(j)-ord('A')+ord('a'))
                if last is None:
                    for k in range(len(table)):
                        if j in table[k]:
                            last = k
                            break
                else:
                    for k in range(len(table)):
                        if j in table[k]:
                            now = k
                            break
                    if last != now:
                        flag = False
                        break
            if flag:
                res.append(i)
        return res

s = Solution()
print(s.findWords(["abdfs","cccd","a","qwwewm"]))