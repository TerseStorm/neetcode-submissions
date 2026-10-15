class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers) - 1
        while i1 < i2:
            numSum = numbers[i1] + numbers[i2]

            if numSum > target:
                i2 -= 1
            elif numSum < target:
                i1 +=1
            else:
                return [i1+1, i2+1]
        return []