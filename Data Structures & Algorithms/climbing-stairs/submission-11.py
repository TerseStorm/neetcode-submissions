class Solution:
    def climbStairs(self, n: int) -> int:
        nWays = [0] * n
        nWays[0] = 1
        if n > 1:
            nWays[1] = 2
            for i in range(2, n):
                # You should've had more trust in your recurrence!
                # nWays[i-2]: How many unique ways could I have taken 2 steps?
                #   - Add two steps to each way and you get to i.
                # nWays[i-1]: How many unique ways could I have taken 1 step?
                #   - Add one step to each way and you get to i.
                # Those 1's and twos you were adding were actions, 
                # but here, we're counting *ways* of getting from i-1 or i-2 to i.
                nWays[i] = nWays[i-2] + nWays[i-1]  
        return nWays[n-1]