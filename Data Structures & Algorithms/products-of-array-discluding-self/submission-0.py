import functools

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # To the left, to the left
        prefixProd = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixProd[i] = prefixProd[i-1] * nums[i-1]
        # BAZZARAGHT
        suffixProd = [1] * len(nums)
        for i in reversed(range(0, len(nums)-1)):
            suffixProd[i] = suffixProd[i+1] * nums[i+1]
        return [prefixProd[i] * suffixProd[i] for i in range(len(nums))]
        