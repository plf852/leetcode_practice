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