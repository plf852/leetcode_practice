from tree.my_lib import *
root = initTree([1,2,3,None,4])


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.res = []
        self.dx = -1
        self.dy = -1
        self.xi = None
        self.yi = None
        self.deepOrder(root, x, y, 0, None)
        print(self.xi,self.yi)
        print(self.dx,self.dy)
        if self.xi and self.yi:
            return self.xi != self.yi and self.dx == self.dy
        return False

    def deepOrder(self, root, x, y, deep, parent):
        if not root:
            return
        self.res.append(root.val)
        if root.val == x:
            self.dx = deep
            self.xi = parent
        if root.val == y:
            self.dy = deep
            self.yi = parent
        self.deepOrder(root.left, x, y, deep + 1, root)
        self.deepOrder(root.right, x, y, deep + 1, root)

s = Solution()
print(s.isCousins(root,2,3))