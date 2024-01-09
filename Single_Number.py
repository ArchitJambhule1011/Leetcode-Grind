'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq == 1:
                return num
        