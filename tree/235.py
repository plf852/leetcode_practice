
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
# 迭代
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root is not None:
            if root.val > p.val and root.val>q.val:
                root = root.left
            elif root.val < p.val and root.val<q.val:
                root = root.right
            else:
                return root
        return None