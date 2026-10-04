class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for string in strs, if its multiset representation
        groups = dict()
        for string in strs:
            multiset = self.toMultiset(string)
            if multiset in groups.keys():
                groups[multiset].append(string)
            else:
                groups[multiset] = [string]
        return list(groups.values())

    
    def toMultiset(self, Str) -> List[str]:
        seen = []
        multiset = []
        for char in Str:
            if char not in seen:
                seen.append(char)
                multiset.append(char)
            else:
                count = seen.count(char)
                newChar = char + str(count + 1)
                seen.append(char)
                multiset.append(newChar)
        return frozenset(multiset)

    
        