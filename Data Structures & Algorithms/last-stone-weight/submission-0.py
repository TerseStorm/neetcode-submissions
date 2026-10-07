class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []
        for stone in stones:
            heapq.heappush_max(self.heap, stone)
        while len(self.heap) > 1:
            stone1 = heapq.heappop_max(self.heap)
            stone2 = heapq.heappop_max(self.heap)
            if stone1 < stone2:
                heapq.heappush_max(self.heap, stone2 - stone1)
            elif stone2 < stone1:
                heapq.heappush_max(self.heap, stone1 - stone2)
        if len(self.heap) == 0:
            return 0
        else:
            return self.heap[0]
        