class Solution:
    def productExceptSelfApproch1(self, nums: list[int]) -> list[int]:
        # Count the number of zeros in the input.
        no_zeros = 0
        # Store the product of all non-zero values.
        product = 1
        # Calculate the product of non-zero values
        # and count the number of zeros.
        for value in nums:
            if value == 0:
                no_zeros += 1
            else:
                product = product * value

        # Initialize the result array with zeros.
        result = [0] * len(nums)

        # If there are more than one zero,
        # every product will contain at least one zero.
        if no_zeros > 1:
            return result
        # If there is exactly one zero,
        # only the position containing zero will have a non-zero result.
        elif no_zeros == 1:
            for i, value in enumerate(nums):
                # The result for the zero position is the product
                # of all the non-zero values.
                if value == 0:
                    result[i] = product
                    return result
        # If there are no zeros, divide the total product
        # by the current value to get product except self.
        else:
            for i, value in enumerate(nums):
                result[i] = int(product / value)
        return result

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Count the number of zeros in the input.
        zero_count = 0
        # Store the product of all non-zero values.
        product = 1
        # Calculate the product of non-zero values
        # and count the number of zeros.
        for value in nums:
            if value == 0:
                zero_count += 1
            else:
                product = product * value
        # Initialize the result array with zeros.
        result = [0] * len(nums)
        # If there are more than one zero,
        # every product will contain at least one zero.
        if zero_count > 1:
            return result
        # If there is exactly one zero,
        # only the zero position gets the product of all non-zero values.
        elif zero_count == 1:
            for i, value in enumerate(nums):
                if value == 0:
                    result[i] = product
                    break
        # If there are no zeros, divide the total product
        # by the current value.
        else:
            for i, value in enumerate(nums):
                result[i] = product // value
        return result
