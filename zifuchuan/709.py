class Solution:
    def toLowerCase(self, t: str) -> str:
        Ai = ord('A')
        Zi = ord('Z')
        ai = ord('a')
        t = []
        for i in range(len(s)):
            index = ord(s[i])
            if index>=Ai and index<=Zi:
                t.append(chr(index-Ai+ai))
            else:
                t.append(s[i])


s = Solution()
print(s.toLowerCase("qwe"))