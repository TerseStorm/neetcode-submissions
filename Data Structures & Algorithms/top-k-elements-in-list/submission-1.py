class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for num in nums:
            hash[num] = 1 + hash.get(num, 0)

        ans = list(hash.keys())
        ans.sort(key=lambda x: hash[x], reverse=True)

        return ans[:k]
        