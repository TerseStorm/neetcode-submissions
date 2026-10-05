class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lParen = ['(', '{', '[']
        rParen = [')', '}', ']']
        for paren in s:
            if paren in lParen:
                stack.insert(0, paren)
            # consider your test cases, mate!
            elif paren in rParen and len(stack) > 0 and self.cuteCouple(stack[0]+paren):
                stack.pop(0)
            else:
                return False
        return len(stack) == 0

    def cuteCouple(self, s):
        return s in ['()', '{}', '[]']