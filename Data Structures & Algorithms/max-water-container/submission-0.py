class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            volume = min(heights[l], heights[r]) * (r - l)
            maxVolume = max(maxVolume, volume)
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return maxVolume