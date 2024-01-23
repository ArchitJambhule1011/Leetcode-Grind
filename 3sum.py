"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue 

            left = i + 1
            right = len(nums) - 1
            while left < right:
                threesum = a + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res