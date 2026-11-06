class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        stack = []

        def backtrack(lB, rB):
            if lB == rB == n:
                # we build the result on the stack
                results.append(''.join(stack))
                return

            if lB < n:
                stack.append("(")
                backtrack(lB+1, rB)
                stack.pop()

            if rB < lB:
                stack.append(")")
                backtrack(lB, rB+1)
                stack.pop()

        backtrack(0, 0)
        return results