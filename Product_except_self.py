""" 
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

class Solution:
    def productexceptself(self, nums : list[int]) -> list[int]:
        n = len(nums)
        leftProduct = [1] * n
        rightProduct = [1] * n

        left_product = 1
        for i in range(1, n):
            leftProduct[i] = left_product * nums[i - 1]
            left_product *= nums[i - 1]

        right_product = 1 
        for i in range(n - 2, -1, -1):
            rightProduct[i] = right_product * nums[i + 1]
            right_product *= nums[i + 1]

        result = [leftProduct[i] * rightProduct[i] for i in range(n)]

        return result