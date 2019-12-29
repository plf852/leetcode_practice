class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(' ')
        res = []
        for i in t:
            res.append(''.join([i for i in reversed(i)]))
        return ' '.join(res)

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))