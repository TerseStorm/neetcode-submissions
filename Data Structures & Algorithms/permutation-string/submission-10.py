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
        frequencies2 = getFrequencies(s2[0:windowSize])
        left = 0


        def isPermutation():
            if all([key in frequencies2.keys() for key in frequencies1.keys()]):
                return all([frequencies2[k] == frequencies1[k] for k in frequencies1.keys()])
            return False

        while left + windowSize <= len(s2):
            if s2[left] in frequencies1.keys() and isPermutation():
                return True
            frequencies2[s2[left]] -= 1
            if frequencies2[s2[left]] == 0:
                frequencies2.pop(s2[left])
            left += 1
            if left + windowSize - 1 < len(s2):
                frequencies2[s2[left+windowSize-1]] += 1
            
        return False