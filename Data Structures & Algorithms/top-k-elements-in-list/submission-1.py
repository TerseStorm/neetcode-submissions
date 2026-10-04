class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for num in nums:
            # creates the hash in-place. No need for an if statement, 
            # if the num is not in hash, then hash.get(num, 0) defaults to 0.
            hash[num] = 1 + hash.get(num, 0)

        # convert keys into a list
        ans = list(hash.keys())
        # sort keys by their values in reverse order (largest first)
        ans.sort(key=lambda x: hash[x], reverse=True)

        # get first k items
        return ans[:k]
        
