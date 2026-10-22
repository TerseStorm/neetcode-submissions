class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][1]:
                j, top = stack.pop()
                res[j] = i - j
            if len(stack) == 0 or temperatures[i] <= stack[-1][1]:
                stack.append([i, temperatures[i]])
        return res