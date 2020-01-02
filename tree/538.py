from tree.my_lib import *
root = initTree([5,2,13,1,4,8,15])
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.dic = {}
        self.build_table(root)
        last = None
        for i in reversed(list(self.dic)):
            if last == None:
                last = self.dic[i]
            else:
                self.dic[i] += last
                last = self.dic[i]

        return self.updateTree(root)

    def build_table(self, root):
        if root is None:
            return

        if root.val not in self.dic.keys():
            self.dic[root.val] = root.val
        self.build_table(root.left)
        self.build_table(root.right)

    def updateTree(self, root):
        if root is None:
            return None
        root.val = self.dic[root.val]
        self.updateTree(root.left)
        self.updateTree(root.right)
        return root
s = Solution()
print(levelOrder(s.convertBST(root)))
root = initTree([5,2,13,1,4,8,15])
class Solution:
    def __init__(self):
        self.last = None
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.convertBST(root.right)
        if self.last is None:
            self.last = root.val
        else:
            root.val += self.last
            self.last = root.val
        self.convertBST(root.left)
        return root

s = Solution()
print(levelOrder(s.convertBST(root)))