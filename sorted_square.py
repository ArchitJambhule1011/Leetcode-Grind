"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedsquare(self, nums:list[int]) -> list[int]:
        output = sorted([i**2 for i in nums])
        return output