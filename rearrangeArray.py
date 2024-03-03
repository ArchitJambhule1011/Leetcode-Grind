"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        output = []
        for i , j in zip(pos,neg):
            output.append(i)
            output.append(j)

        return output