# 不仅可以对数组元素进行hash，对矩阵元素也可以
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        import math
        distance = [[-1]*len(points) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i,len(points)):
                d = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
                distance[i][j] = d
                distance[j][i] = d
        res = 0
        for i in range(len(points)):
            table = {}
            for j in range(len(points)):
                if i!=j:
                    if distance[i][j] not in table:
                        table[distance[i][j]] = 1
                    else:
                        table[distance[i][j]] += 1
            for j in table:
                if table[j]>=2:
                    res += table[j]*(table[j]-1)
        return res