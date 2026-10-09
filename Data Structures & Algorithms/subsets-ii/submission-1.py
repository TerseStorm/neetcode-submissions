class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # You had the right idea with adding to what came before. Kind of.
        powerset = [[]]

        def deduplicate(pset):
            for i in range(len(pset)):
                pset[i] = sorted(pset[i])

            fset = []
            for p in pset:
                if p not in fset:
                    fset.append(p)
            return fset


        for num in nums:
            powerset += [curr + [num] for curr in powerset]
        return deduplicate(powerset)
