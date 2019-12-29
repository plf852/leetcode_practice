# g(n) 表示n个节点对应的二叉搜索树个数,f(i)代表以i为节点的二叉搜索树个数
# g(n) = f(1)+f(2)....+f(n)
# f(i) = g(i-1)*g(n-i) 左边i-1个节点，右边n-i个节点

class Solution:
    def numTrees(self, n: int) -> int:
        g = [0]*(n+1)
        g[0]=1
        g[1]=1

        for i in range(2,n+1):
            for j in range(1,i+1):
                g[i] += g[j-1]*g[i-j]

        return g[n]

s = Solution()
print(s.numTrees(3))