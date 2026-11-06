class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            # There should only be n brackets
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # start by adding an open bracket
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            # balance an open bracket by closing it, but we do this in a LIFO fashion
            # This means that the first correct string is always the deepest-stacked bracket
            # "((...()...))"
            # And the last is the bracket string with the most breadth
            # "()()...()"
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res