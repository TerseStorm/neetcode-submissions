class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxList = [0] * len(nums)
        minList = [float('inf')] * len(nums)
        maxList[0] = nums[0]
        minList[0] = nums[0]

        for i in range(1, len(nums)):
            maxList[i] = max(nums[i], nums[i] * maxList[i-1], nums[i] * minList[i-1])
            minList[i] = min(nums[i], nums[i] * minList[i-1], nums[i] * maxList[i-1])
        return max(maxList)