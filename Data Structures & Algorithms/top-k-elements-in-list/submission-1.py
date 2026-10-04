class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for num in nums:
            # creates the hash in-place. No need for an if statement, 
            # if the num is not in hash, then hash.get(num, 0) defaults to 0.
            hash[num] = 1 + hash.get(num, 0)

        ans = list(hash.keys())
        ans.sort(key=lambda x: hash[x], reverse=True)

        return ans[:k]
        
