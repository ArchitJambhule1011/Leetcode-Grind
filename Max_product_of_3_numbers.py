""" 
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""
# Max product can be between two combinations
# 1: Between the 3 max numbers 
# 2: Between 2 smallest and 1 largest 

class Solution:
   def maximumProduct(self, nums: list[int]) -> int:
     nums.sort()
     max_product_1 = nums[-1] * nums[-2] * nums[-3]
     max_product_2 = nums[0]  * nums[1]  * nums[-1]

     max_value = max(max_product_1, max_product_2)

     return max_value

      