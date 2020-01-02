from tree.my_lib import *
root = initTree([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
class Solution:
    def pathSum(self, root: TreeNode, tmp: int):
        self.all_path = []
        self.path = []
        if root is None:
            return 0
        self.printPath(root, tmp)
        return self.all_path

    def printPath(self, root, cur_sum):
        if root is None:
            return
        self.path.append(root.val)
        cur_sum -= root.val
        if root.left is None and root.right is None:
            if cur_sum == 0:
                self.all_path.append(self.path)
        self.printPath(root.left, cur_sum)
        self.printPath(root.right, cur_sum)
        self.path = self.path[:-1]

s = Solution()
print(s.pathSum(root,22))
