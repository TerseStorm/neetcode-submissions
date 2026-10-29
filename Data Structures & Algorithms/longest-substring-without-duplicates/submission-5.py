class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startPointer = 0
        longest = 0
        charSet = set()
        endPointer = startPointer
        while startPointer < len(s):
            while endPointer < len(s) and s[endPointer] not in charSet:
                charSet.add(s[endPointer])
                longest = max(longest, (endPointer - startPointer) + 1)
                endPointer += 1
            if endPointer >= len(s):
                return longest
            toRemove = s[endPointer]
            removed = s[startPointer]
            charSet.remove(s[startPointer])
            startPointer += 1
            while toRemove != removed:
                removed = s[startPointer]
                charSet.remove(s[startPointer])
                startPointer += 1
            charSet.add(s[endPointer])
            endPointer += 1
        return longest