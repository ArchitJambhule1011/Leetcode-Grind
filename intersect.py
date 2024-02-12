"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

from collections import Counter 

class Solution:
    def intersect(self, nums1:list[int], nums2:list[int]) -> list[int]:
        count_nums_1 = Counter(nums1)
        result = []

        for num in nums2:
            if num in count_nums_1 and count_nums_1[num] > 0:
                result.append(num)
                count_nums_1[num] -= 1
        
        return result