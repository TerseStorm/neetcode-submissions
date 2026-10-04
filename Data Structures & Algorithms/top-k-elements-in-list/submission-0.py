class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topNums = []
        counts = self.toCounts(nums)
        for _ in range(k):
            topNum = 0
            topCount = 0
            for num in counts.keys():
                if counts[num] > topCount:
                    topCount = counts[num]
                    topNum = num
            topNums.append(topNum)
            counts.pop(topNum)
        return topNums

    def toCounts(self, nums: List[int]):
        seen = dict()
        for num in nums:
            if num in seen.keys():
                seen[num] += 1
            else:
                seen[num] = 1
        return seen