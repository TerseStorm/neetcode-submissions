class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        for num in nums:
            heapq.heappush_max(queue, num)
        res = 0
        for _ in range(k):
           res = heapq.heappop_max(queue)
        return res