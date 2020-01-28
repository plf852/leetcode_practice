class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)):
            costs[i].append(abs(costs[i][0]-costs[i][1]))
        costs = sorted(costs,key=lambda x:-x[2])
        a = 0
        b = 0
        count = len(costs)//2
        cur = None
        msum = 0
        for i in range(len(costs)):
            cur = i
            if costs[i][0]<costs[i][1]:
                a+=1
                msum += costs[i][0]
            else:
                b+=1
                msum += costs[i][1]
            if a==count or b==count:
                break
        if a!=count:
            for i in range(cur+1,len(costs)):
                msum +=costs[i][0]
        else:
            for i in range(cur+1,len(costs)):
                msum += costs[i][1]
        return msum

