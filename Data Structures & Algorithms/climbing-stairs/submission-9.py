class Solution:
    def climbStairs(self, n: int) -> int:
        nWays = [0] * n
        nWays[0] = 1
        if n > 1:
            nWays[1] = 2
            for i in range(2, n):
                # You should've had more trust in your recurrence!
                # nWays[i-2]: How many ways could I have taken 2 steps?
                # nWays[i-1]: How many ways could I have taken 1 step?
                nWays[i] = nWays[i-2] + nWays[i-1] 
        return nWays[n-1]