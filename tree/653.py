from tree.my_lib import *
# 先构建再查询
class Solution:
    def __init__(self):
        self.table = {}

    def build_table(self, root):
        if not root:
            return
        self.table[root.val] = 1
        self.build_table(root.left)
        self.build_table(root.right)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        if not self.table:
            self.build_table(root)
        tmp = k - root.val
        if tmp != root.val and tmp in self.table:
            return True
        left = self.findTarget(root.left, k)
        right = self.findTarget(root.right, k)
        return left or right

# 边构建边查询，效率更高
class Solution:
    def __init__(self):
        self.table = {}

    def build_table(self, root, k):
        if not root:
            return False
        self.table[root.val] = 1
        tmp = k - root.val
        if tmp != root.val and tmp in self.table: # 即使当前没有查到，如果真的存在，遍历其他节点也会查到，所以不会返回错误答案
            return True
        return self.build_table(root.left, k) or self.build_table(root.right, k)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        return self.build_table(root, k)