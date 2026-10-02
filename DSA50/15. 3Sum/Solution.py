class Solution:
    def threeSumApproach1(self, nums: list[int]) -> list[list[int]]:
        # Sort the input array
        # Time: O(n log n)
        nums.sort()

        result = []
        nums_len = len(nums)

        # Iterate through every element and consider it as the middle value
        for i, value in enumerate(nums):

            # Left pointer starts before the current element
            left = i - 1

            # Right pointer starts after the current element
            right = i + 1

            # Continue while both pointers are within the array
            while left >= 0 and right < nums_len:

                # Found a triplet whose sum is zero
                if nums[left] + nums[right] + value == 0:
                    result.append([nums[left], value, nums[right]])

                    # Move both pointers to search for another combination
                    right += 1
                    left -= 1

                # Sum is less than zero
                # Since array is sorted, increase right to get a larger value
                elif nums[left] + nums[right] + value < 0:
                    right += 1

                # Sum is greater than zero
                # Since array is sorted, decrease left to get a smaller value
                else:
                    left -= 1

        # Convert each inner list to tuple because lists are unhashable
        # set() removes duplicate triplets
        # Convert the tuples back to lists
        return [list(x) for x in set(map(tuple, result))]

        # Time Complexity: O(n²)
        #   Sorting: O(n log n)
        #   Outer loop: O(n)
        #   Two-pointer traversal: O(n) for each iteration
        #
        # Space Complexity: O(n²)
        #   result can contain O(n²) triplets in the worst case
        #   Auxiliary space excluding output: O(1)


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the input array
        # Sorting is required for the two-pointer technique
        nums.sort()

        result = []
        nums_len = len(nums)

        # Iterate through the array
        # We need at least two elements after i for left and right
        for i in range(nums_len - 2):

            # Current element
            value = nums[i]

            # Skip duplicate values for the first element
            # This prevents duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Left pointer starts immediately after i
            left = i + 1

            # Right pointer starts at the end of the array
            right = nums_len - 1

            # Continue until the two pointers meet
            while left < right:

                # Calculate the sum of the three values
                total = nums[left] + nums[right] + value

                # Found a valid triplet
                if total == 0:
                    result.append([nums[left], value, nums[right]])

                    # Skip duplicate values on the left
                    # This prevents duplicate triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate values on the right
                    # This prevents duplicate triplets
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                # Sum is less than zero
                # Because the array is sorted, increase left
                # to get a larger value
                elif total < 0:
                    left += 1

                # Sum is greater than zero
                # Because the array is sorted, decrease right
                # to get a smaller value
                else:
                    right -= 1

        # Return all unique triplets
        return result

        # Time Complexity: O(n²)
        #   Sorting: O(n log n)
        #   Outer loop: O(n)
        #   Two-pointer traversal: O(n) for each i
        #
        # Space Complexity: O(n²)
        #   result can contain O(n²) triplets in the worst case
        #   Auxiliary space excluding output: O(1)
