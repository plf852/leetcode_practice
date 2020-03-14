class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def initTree(data):
    root = TreeNode(data[0])
    tmp = [root]
    for i in range(1,len(data)):
        if data[i] is not None:
            d = TreeNode(data[i])
            if i % 2 == 1:
                tmp[(i - 1) // 2].left = d
            else:
                tmp[(i - 2) // 2].right = d
        else:
            d = None
        tmp.append(d)
    return root

def levelOrder(root: TreeNode):
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

def buildTree(preorder, inorder) -> TreeNode:
    if preorder==[] or inorder==[]:
        return None
    def findNum(target):
        for i in range(len(inorder)):
            if inorder[i] == target:
                return i
        return -1
    root = TreeNode(preorder[0])
    index = findNum(preorder[0])
    root.left = buildTree(preorder[1:index+1],inorder[:index])
    root.right = buildTree(preorder[index+1:len(preorder)],inorder[index+1:len(inorder)])
    return root