class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # You had the right idea with adding to what came before. Kind of.
        powerset = [[]]
        for num in nums:
            powerset += [curr + [num] for curr in powerset]
        return powerset