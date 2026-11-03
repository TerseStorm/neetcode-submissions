class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        total = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            elif height[l] >= height[r]:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        return total