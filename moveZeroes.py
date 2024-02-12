"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""

class Solution:
    def moveZeroes(self, nums:list[int]) -> None:
        non_zero_index = 0
        for current_index in range(len(nums)):
            if nums[current_index] != 0:
                nums[current_index] , nums[non_zero_index] = nums[non_zero_index] , nums[current_index]
                non_zero_index += 1