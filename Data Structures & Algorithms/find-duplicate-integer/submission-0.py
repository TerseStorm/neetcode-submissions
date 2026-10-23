class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nSet = set()
        for num in nums:
            if num in nSet:
                return num
            else:
                nSet.add(num)