import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = heapq.nlargest(k, nums)[::-1]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        if len(self.pool) < self.k:
            return None
        return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)