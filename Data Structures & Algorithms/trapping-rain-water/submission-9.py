class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        leftMax = height[0]
        rightMax = height[-1]
        l = 0
        r = len(height) - 1

        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        
        return total

