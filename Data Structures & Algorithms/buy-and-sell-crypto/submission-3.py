class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If the list is monotonically decreasing, you make no profit.
        smallestIndex = 0
        smallestValue = float('inf')
        largestProfit = 0
        for i in range(len(prices)):
            # iterate through the list.
            # Moving to the first item, we find that buying and selling
            # same day gives a profit of 0, way better than infinity.
            # Then we move to the second day, and we see that buying on this day
            # would burn less of a hole in your pocket. So our smallest index becomes 
            # this one.
            # Furthermore, since the largest index must never be less 
            # than the smallest index, it "snaps forward" to the largest index.
            # If we have a good profit going, and we see a small number equal or less than the smallestValue, that doesn't guarantee we get a better profit. But maybe it could. Consider
            # [10,2,5,6,7,1,9]
            # [10,2,5,6,7,1]
            if prices[i] < smallestValue:
                smallestValue = prices[i]
                smallestIndex = i
            if prices[i] - prices[smallestIndex] >= largestProfit:
                largestProfit = prices[i] - prices[smallestIndex]
        return largestProfit
                