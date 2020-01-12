# 找到结果和1个数的关系
# grid不一定是方阵
# 减少一半计算量的算法
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = 0
                    if i-1>=0 and grid[i-1][j] == 1:
                        num += 1
                    if j+1<len(grid[0]) and grid[i][j+1] ==1:
                        num += 1
                    if i+1<len(grid) and grid[i+1][j] == 1:
                        num+=1
                    if j-1>=0 and grid[i][j-1] == 1:
                        num+=1
                    res += 4-num
        return res

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = 0
                    if i-1>=0 and grid[i-1][j] == 1:
                        num += 1
                    if j+1<len(grid[0]) and grid[i][j+1] ==1:
                        num += 1
                    if i+1<len(grid) and grid[i+1][j] == 1:
                        num+=1
                    if j-1>=0 and grid[i][j-1] == 1:
                        num+=1
                    res += 4-num
        return res

