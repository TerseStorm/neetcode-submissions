class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i, point in enumerate(nums):
            if point > 0:
                break
            
            # because the list is sorted, all duplicates are next to each other, so we just skip dealing with them.
            if i > 0 and point == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R :
                threeSum = point + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    triplets.append([point, nums[L], nums[R]])
                    R -= 1
                    L += 1

                    # Same thing here. Because all duplicates are next to each other, we skip dealing with them.
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return triplets
