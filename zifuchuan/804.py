class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        res = set()
        for i in words:
            res.add(self.trans(i))
        return len(res)

    def trans(self,word):
        table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = []
        ai = ord('a')
        for i in word:
            res.append(table[ord(i)-ai])
        return ''.join(res)

s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))