class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = self.build_dict(s)
        tDict = self.build_dict(t)
        # they are an anagram of each other if:
            # they have the same length
            # they have the same dict keys
            # these keys have the same values
            # they are not the same string
        return sDict.keys() == tDict.keys() and self.same_values(sDict, tDict)

    def same_values(self, dict1, dict2):
        for key in dict1.keys():
            if dict1[key] != dict2[key]:
                return False
        return True

    def build_dict(self, string):
        d = dict()
        for s in string:
            if s in d.keys():
                d[s] += 1
            else:
                d[s] = 1
        return d