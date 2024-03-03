"""
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.
"""

class Solution:
    def max_sum_subarray(self, nums:list[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum