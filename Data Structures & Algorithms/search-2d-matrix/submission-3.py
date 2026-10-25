class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        inRange = False
        while not inRange:
            mid = (start + end) // 2
            if start > end:
                return False
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                inRange = True
            elif target >= matrix[mid][-1]:
                start = mid + 1
            elif target <= matrix[mid][0]:
                end = mid - 1
        found  = False
        left = 0
        nums = matrix[mid]
        right = len(nums) - 1
        while left <= right:
            midd = (left + right) // 2
            if nums[midd] == target:
                return True
            elif target < nums[midd]:
                right = midd - 1
            elif target > nums[midd]:
                left = midd + 1
        return False

        