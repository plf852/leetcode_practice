from tree.my_lib import *

class Solution:
    def averageOfLevels(self, root: TreeNode):
        from collections import deque
        import numpy as np
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while len(queue):
            mlen = len(queue)
            tmp = []
            for i in range(mlen):
                q = queue.popleft()
                tmp.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            res.append(np.mean(tmp))
        return res

# 使用list操作比deque 更节约时间
class Solution:
    def averageOfLevels(self, root: TreeNode):
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            tmp_queue = []
            tmp = 0
            for q in queue:
                tmp += q.val
                if q.left:
                    tmp_queue.append(q.left)
                if q.right:
                    tmp_queue.append(q.right)
            res.append(tmp*1.0/len(queue))
            queue = tmp_queue
        return res

s = Solution()
root = initTree([3,9,20,None,None,15,7])
print(s.averageOfLevels(root))