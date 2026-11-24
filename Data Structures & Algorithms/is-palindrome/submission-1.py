class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True 
        formattedStr = self.formatString(s)
        start = 0
        end = len(formattedStr) - 1
        while start <= end:
            if formattedStr[start].lower() != formattedStr[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def formatString(self, s):
        trimmedStr = s.strip()
        lowerStr = trimmedStr.lower()
        formattedStr = re.sub(r'[^a-zA-Z0-9]', '', lowerStr)
        return formattedStr
