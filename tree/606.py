from tree.my_lib import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:
            return str(t.val)+'('+self.tree2str(t.left)+')'  # left
        # elif not t.left and t.right:
        #     return str(t.val)+'('+self.tree2str(t.right)+')'  # right
        return t.val + '(' + self.tree2str(t.left) + ')('+self.tree2str(t.right)+')'  #left right
