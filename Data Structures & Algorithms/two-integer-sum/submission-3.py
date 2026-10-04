class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        ans[nums[0]] = 0
        for i in range(1, len(nums)):
            if target - nums[i] in ans.keys():
                return [ans[target - nums[i]], i]
            else:
                ans[nums[i]] = i
