# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LeverOrder:
    def levelOrderBottom(self, root: TreeNode):
        from collections import deque
        res = deque()
        if root is None:
            return
        deq = deque()
        deq.append(root)

        while deq:
            t = len(deq)
            tmp = []
            for i in range(t):
                first = deq.popleft()
                tmp.append(first.val)
                if first.left is not None:
                    deq.append(first.left)
                if first.right is not None:
                    deq.append(first.right)
            res.appendleft(tmp)
        return list(res)

def initTree(data):
    root = TreeNode(data[0])
    parent = root
    for i in range(1,len(data)):
        if i%2 == 1:
            parent.left = TreeNode(data[i])
            parent = parent.left
        elif i%2 == 0:
            parent.right = TreeNode(data[i])
            parent = parent.right
    return root
root = initTree([1,2,3,4,5])
s = LeverOrder()
print(s.levelOrderBottom(root))