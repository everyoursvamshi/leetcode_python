class Solution:

    # Approach 1: Using Dictionary
    def containsDuplicateMap(self, nums: list[int]) -> bool:
        seen = {}
        for value in nums:
            if value in seen:
                return True
            seen[value] = True
        return False

    # Approach 2: Using Set (Recommended)
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for value in nums:
            if value in seen:
                return True
            seen.add(value)
        return False

