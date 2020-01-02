class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 计算时间长
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),self.treeDeep(root.left)+self.treeDeep(root.right))
    def treeDeep(self,root):
        if root is None:
            return 0
        return 1+max(self.treeDeep(root.left),self.treeDeep(root.right))

# 加速后
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max = 0
        self.treeDeep(root)
        return self.max
    def treeDeep(self,root):
        if root is None:
            return 0
        l = self.treeDeep(root.left)
        r = self.treeDeep(root.right)
        self.max = max(self.max,l+r)
        return 1+max(l,r)