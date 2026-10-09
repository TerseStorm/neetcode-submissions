class Solution:
    def climbStairs(self, n: int) -> int:
        nWays = [0] * n
        nWays[0] = 1
        if n > 1:
            nWays[1] = 2
            for i in range(2, n):
                nWays[i] = nWays[i-2] + nWays[i-1] 
        return nWays[n-1]