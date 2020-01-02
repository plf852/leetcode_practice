from tree.my_lib import *

root = initTree([1,1,2,3,3,2,None])
class Solution:
    def findMode(self, root: TreeNode):
        self.dic = {}
        self.build_table(root)
        t = sorted(self.dic.values(),reverse=True)
        print(t)
        res = []
        for k in self.dic:
            if self.dic[k] == t[0]:
                res.append(k)
        return res

    def build_table(self, root):
        if root is None:
            return
        if root.val in self.dic.keys():
            self.dic[root.val] += 1
        else:
            self.dic[root.val] = 1

        self.build_table(root.left)
        self.build_table(root.right)

s = Solution()
print(s.findMode(root))
