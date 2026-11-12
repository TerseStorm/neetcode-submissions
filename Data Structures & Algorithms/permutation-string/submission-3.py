class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        if len(s2) < windowSize:
            return False
        
        def getFrequencies(sN):
            frequencies = defaultdict(int)
            for s in sN:
                frequencies[s] += 1
            return frequencies

        frequencies1 = getFrequencies(s1)
        left = 0


        def isPermutation(sN):
            frequencies = getFrequencies(sN)
            if frequencies.keys() == frequencies1.keys():
                return all([frequencies[k] == frequencies1[k] for k in frequencies.keys()])
            return False

        while left + windowSize <= len(s2):
            if s2[left] in frequencies1.keys() and isPermutation(s2[left:left+windowSize]):
                return True
            left += 1
        return False