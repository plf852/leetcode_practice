from tree.my_lib import *
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        sum -= root.val
        if root.left is None and root.right is None:
            return sum==0
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)

root = initTree([5,4,8,11,None,13,4,7,2,None,None,None,1])
s = Solution()

print(s.hasPathSum(root,22))