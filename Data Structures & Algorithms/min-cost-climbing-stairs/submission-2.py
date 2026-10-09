class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nStairs = len(cost) + 1
        minCost = [0] * nStairs
        minCost[0] = 0
        minCost[1] = 0
        if len(minCost) > 2:
            for i in range(2, nStairs):
                minCost[i] = min(cost[i-2] + minCost[i-2], cost[i-1] + minCost[i-1])
        return minCost[nStairs-1]