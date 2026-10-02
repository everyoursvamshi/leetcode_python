class Solution:

    def longestConsecutiveApproach1(self, nums: list[int]) -> int:

        # Store each number as a key.
        # Value = [has_previous, has_next]
        num_map = {}
        for value in nums:
            num_map[value] = [False, False]
        # Identify whether each number has a consecutive
        # previous number and/or next number.
        for value in num_map.keys():
            if value + 1 in num_map:
                num_map[value][1] = True
            if value - 1 in num_map:
                num_map[value][0] = True
        max_len = 0

        print(num_map)

        # Start from every number and expand in both directions.
        for currt in num_map.keys():
            len = 1
            value = currt
            # Count consecutive numbers in the forward direction.
            while num_map[value][1] == True:
                len += 1
                # Mark the forward connection as visited.
                num_map[value][1] = False
                value = value + 1
                # Mark the corresponding backward connection as visited.
                num_map[value][0] = False
            value = currt

            # Count consecutive numbers in the backward direction.
            while num_map[value][0] == True:
                len += 1
                # Mark the backward connection as visited.
                num_map[value][0] = False
                value = value - 1
                # Mark the corresponding forward connection as visited.
                num_map[value][1] = False
            if max_len < len:
                max_len = len
        return max_len


    # Time Complexity:
    # O(N) average
    #
    # Building num_map              -> O(N)
    # Finding consecutive neighbors -> O(N)
    # Traversing consecutive values  -> O(N)
    #
    # Each consecutive connection is visited only once.


    # Space Complexity:
    # O(N)
    #
    # num_map can contain up to N unique numbers.
    # Each number stores two Boolean values.


    def longestConsecutiveApproach2(self, nums: list[int]) -> int:
        # Store each unique number and whether it has been visited.
        visit_map = {}
        for value in nums:
            visit_map[value] = False
        max_len = 0
        # Process each unique number.
        for currt in visit_map.keys():

            # Skip numbers that were already processed
            # as part of another consecutive sequence.
            if visit_map[currt] == True:
                continue
            len = 1
            # Mark the current number as visited.
            visit_map[currt] = True
            value = currt + 1
            # Count consecutive numbers in the forward direction.
            while value in visit_map and visit_map[value] == False:
                len += 1
                # Mark the number as visited so it won't
                # be processed again later.
                visit_map[value] = True
                value += 1
            value = currt - 1

            # Count consecutive numbers in the backward direction.
            while value in visit_map and visit_map[value] == False:
                len += 1
                # Mark the number as visited.
                visit_map[value] = True
                value -= 1

            if max_len < len:
                max_len = len

        return max_len


    # Time Complexity:
    # O(N) average
    #
    # Building visit_map -> O(N)
    # Each number is visited at most once in the while loops.
    #
    # Overall -> O(N) average.


    # Space Complexity:
    # O(N)
    #
    # visit_map stores up to N unique numbers and their visited status.


    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert the input to a set for O(1) average-time lookup.
        nums = set(nums)
        max_len = 0
        # Process each unique number.
        for value in nums:
            # If the previous number exists, this is not the
            # beginning of a consecutive sequence.
            if value - 1 in nums:
                continue
            len = 1
            value_next = value + 1
            # Count consecutive numbers starting from this value.
            while value_next in nums:
                len += 1
                value_next += 1
            # Update the longest sequence found so far.
            max_len = max(max_len, len)
        return max_len


    # Time Complexity:
    # O(N) average
    #
    # Creating the set       -> O(N)
    # Finding sequence starts -> O(N)
    # Traversing sequences    -> O(N) overall
    #
    # Each sequence is traversed only from its starting number,
    # so the same consecutive sequence is not repeatedly scanned.


    # Space Complexity:
    # O(N)
    #
    # The set can contain up to N unique numbers.
