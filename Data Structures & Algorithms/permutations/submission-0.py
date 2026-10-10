class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        nnums = nums[::-1]

        def getPermutations(nums, per):
            if len(nums) == 0:
                permutations.append(per)
                return
            for num in nums:
                getPermutations([n for n in nums if n != num], per + [num])

        getPermutations(nnums, [])
        return permutations