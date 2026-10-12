class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        succ = dict()
        for num in nums:
            succ[num] = "end"
            if succ.get(num-1):
                succ[num-1] = num
            if succ.get(num+1):
                succ[num] = num+1
        
        seenNums = set()
        maxCount = 0
        
        def traverse(num):
            curCount = 1
            while succ[num] != "end":
                num = succ[num]
                seenNums.add(num) 
                curCount += 1
            return curCount

        for num in nums:
            if num not in seenNums:
                seenNums.add(num)
                count = traverse(num)
                maxCount = max(maxCount, count)
        return maxCount