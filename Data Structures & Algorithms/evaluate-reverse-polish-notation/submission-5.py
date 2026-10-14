class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                match token:
                    case '+':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(y + x)
                    case '-':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(y - x)
                    case '*':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(y * x)
                    case '/':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(math.trunc(y / x))
            else:
                stack.append(int(token))
        return stack[0]