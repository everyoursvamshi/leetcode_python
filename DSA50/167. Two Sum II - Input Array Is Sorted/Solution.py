class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i=0;
        j=len(numbers)-1
        while i<j:
            total = numbers[i]+numbers[j]
            if target == total:
                return [i+1,j+1]
            elif target < total:
                j=j-1
            else:
                i=i+1
        return []
