"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
"""

class Solution:
    def findLucky(self, arr:list[int]) -> int:
        from collections import Counter
        stack = []
        count = Counter(arr)
        for key, value in count.items():
            if key == value:
                stack.append(key)
        if stack:
            return max(stack)
        else:
            return -1