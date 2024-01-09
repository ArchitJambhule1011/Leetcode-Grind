''' 
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



'''

from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        output = []
        count = Counter(nums)
        for num, freq in count.items():
            if freq != 2:
                output.append(num)
        return output  