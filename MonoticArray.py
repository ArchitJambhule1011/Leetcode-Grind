"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.


"""

#Tip = An array is monotic if it is in decreasing order or increasing order, we just created two variabels which are the reverse sorted
# array and the normal sorted array. If the inputs matches one of the two, we say it is monotic

class Solution:
    def isMonotonic(self, nums:list[int]) -> bool:
        rev = sorted(nums, reverse=True)
        so = sorted(nums)

        return nums==rev or nums==so