"""
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
"""

class Solution:
    def maxFrequencyElements(self, nums : list[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        max_counts = []
        for key, value in count.items():
            if value == max(count.values()):
                max_counts.append(value)

        return sum(i for i in max_counts)