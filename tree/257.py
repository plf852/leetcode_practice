from tree.my_lib import *
root = initTree([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        self.res = []
        self.printPath(root, '')
        return self.res

    def printPath(self, root, path):
        if root is None:
            return
        path += str(root.val)
        if root.left is None and root.right is None:
            self.res.append(path)
        path += '->'
        self.printPath(root.left, path)
        self.printPath(root.right, path)

s = Solution()
print(s.binaryTreePaths(root))