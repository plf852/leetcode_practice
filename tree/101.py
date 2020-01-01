class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    def isMirror(self,t1,t2):
        if t1 is None and t2 is None: # 不能写成t1==t2
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.isMirror(t1.left,t2.right) and self.isMirror(t1.right,t2.left)