class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        left = 0
        right = 1
        condition = True
        frequencies[s[0]] = 1
        mostFrequentChar = s[0]
        res = 1
        while right < len(s):
            frequencies[s[right]] += 1
            mostFrequentChar = max(frequencies.keys(), key=frequencies.get)
            substringLength = (right - left) + 1
            mostFrequentLength = frequencies[mostFrequentChar] # has to be most frequent length within window!!!
            maxReplacements = substringLength - mostFrequentLength
            if maxReplacements <= k:
                res = max(res, mostFrequentLength + maxReplacements)
                right += 1
            else:
                frequencies[s[left]] -= 1
                mostFrequentChar = max(frequencies.keys(), key=frequencies.get)
                left += 1
                right += 1
        return res
