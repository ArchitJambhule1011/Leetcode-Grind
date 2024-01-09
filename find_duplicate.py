''' 
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number
'''


from collections import Counter

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq >= 2:
                return num