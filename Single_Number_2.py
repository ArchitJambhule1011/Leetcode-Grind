
""" 
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space


"""


from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq != 3:
                return num