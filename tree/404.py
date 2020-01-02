from tree.my_lib import *
root = initTree([3,9,20,None,None,15,7])

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        return self.mySumOfLeftLeaves(root,root)

    def mySumOfLeftLeaves(self,root,parent):
        if root is None:
            return 0
        res = 0
        if root.left is None and root.right is None:
            if root == parent.left:
                return root.val
            else:
                return 0
        if root.left is not None:
            res += self.mySumOfLeftLeaves(root.left,root)

        if root.right is not None:
            res += self.mySumOfLeftLeaves(root.right,root)
        return res

s = Solution()
print(s.sumOfLeftLeaves(root))
