class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search:
        # we need a start and end pointer to keep track of the beginning and end of our search window.
        # We also need a middle pointer too.
        start, end = 0, len(nums) - 1
        found = False
        while not found:
            middle  = (end + start) // 2
            if nums[middle] == target:
                return middle
            if end <= start:
                return -1
            elif target > nums[middle]:
                start = middle + 1
            elif target < nums[middle]:
                end = middle - 1

