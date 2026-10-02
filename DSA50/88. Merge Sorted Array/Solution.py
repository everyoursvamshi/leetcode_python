class Solution:

    def mergeApproach1(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        # Remove the extra empty positions from nums1.
        # nums1 initially has m valid elements + n empty positions.
        while len(nums1) > m:
            nums1.pop()

        # nums1_len points to the number of valid elements remaining in nums1.
        nums1_len = m

        # nums2_len represents the number of elements remaining in nums2.
        nums2_len = n

        # Continue until all elements from nums2 are inserted into nums1.
        while nums2_len > 0:

            # If nums1 still has elements to compare and the current
            # nums1 element is smaller than the current nums2 element,
            # insert the nums2 element after the nums1 element.
            if nums1_len > 0 and nums1[nums1_len-1] < nums2[nums2_len-1]:

                # Insert nums2's current largest remaining element
                # at the current position in nums1.
                nums1.insert(nums1_len, nums2[nums2_len-1])

                # Move to the next element in nums2.
                nums2_len -= 1

            # If nums1_len becomes -1, insert the remaining nums2
            # element at the beginning of nums1.
            elif nums1_len == -1:

                nums1.insert(0, nums2[nums2_len-1])

                # Move to the next element in nums2.
                nums2_len -= 1

            # Otherwise, move backwards through nums1 to find the
            # correct position for the current nums2 element.
            else:
                nums1_len -= 1


    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        # i points to the last valid element in nums1.
        i = m - 1

        # j points to the last element in nums2.
        j = n - 1

        # k points to the last available position in nums1.
        # nums1 already has enough space for all elements from nums2.
        k = m + n - 1

        # Compare elements from the end of both arrays.
        # The larger element is placed at position k.
        while i >= 0 and j >= 0:

            # If the current nums1 element is smaller,
            # place the larger nums2 element at position k.
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1

            # Otherwise, place the current nums1 element at position k.
            else:
                nums1[k] = nums1[i]
                i -= 1

            # Move the destination position backwards.
            k -= 1

        # If nums2 still has elements remaining,
        # copy them into nums1.
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
