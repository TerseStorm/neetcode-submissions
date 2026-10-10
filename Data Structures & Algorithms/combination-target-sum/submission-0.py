class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        nnums = nums[::-1]
        def getCombinations(nums, total, target):
            if sum(total) > target:
                return
            if sum(total) == target:
                combinations.append(total)
                return
            i = 0
            while len(nums) > 0:
                num = nums[-1]
                getCombinations(nums.copy(), total + [num] , target)
                nums.pop()

        
        getCombinations(nnums, [], target)
        return combinations