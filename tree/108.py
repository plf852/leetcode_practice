
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = (len(nums)-1)//2
        root = TreeNode(nums[mid])
        if mid >0:
            root.left = self.sortedArrayToBST(nums[:mid])
        else:
            root.left = None
        if mid+1<len(nums):
            root.right = self.sortedArrayToBST(nums[mid+1:])
        else:
            root.right = None
        return root

    def levelOrder(self, root: TreeNode):
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
            res.append(tmp)
        return list(res)

s = Solution()
root = s.sortedArrayToBST([-10,-3,0,5,9])
print(s.levelOrder(root))
