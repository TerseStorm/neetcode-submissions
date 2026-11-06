class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        stack = []

        def backtrack(lB, rB):
            if lB == rB == n:
                # we build the result on the stack
                results.append(''.join(stack))
                return

            # start by adding an open bracket
            if lB < n:
                stack.append("(")
                backtrack(lB+1, rB)
                stack.pop()

            # balance an open bracket by closing it, but we do this in a LIFO fashion
            # This means that the first correct string is always the deepest-stacked bracket
            # "((...()...))"
            # And the last is the bracket string with the most breadth
            # "()()...()"
            if rB < lB:
                stack.append(")")
                backtrack(lB, rB+1)
                stack.pop()

        backtrack(0, 0)
        return results