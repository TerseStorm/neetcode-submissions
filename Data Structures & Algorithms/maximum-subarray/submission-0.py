class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = [0] * len(nums)
        maxSum[0] = nums[0]
        for i in range(1, len(nums)):
            maxSum[i] = max(nums[i], maxSum[i-1] + nums[i])
        return max(maxSum)
        