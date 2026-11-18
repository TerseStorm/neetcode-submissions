class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        frequenciesT  = {}
        window = {}
        
        # build up the frequencies map
        for c in t:
            frequenciesT[c] = 1 + frequenciesT.get(c, 0)


        have, need = 0, len(frequenciesT)

        res, resLen = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            # easier to keep track of the quota this way?
            if c in frequenciesT and frequenciesT[c] == window[c]:
                have += 1

            while have == need:
                currentSize = right - left + 1
                if currentSize < resLen:
                    res = [left, right]
                    resLen = currentSize

                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in frequenciesT and window[leftChar] < frequenciesT[leftChar]:
                    have -= 1

                left += 1

        best_left, best_right = res
        return s[best_left : best_right + 1] if resLen != float('inf') else "" 

            