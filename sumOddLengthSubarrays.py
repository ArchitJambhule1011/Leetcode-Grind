"""
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

"""

class Solution:
    def sumoddlengthsubarray(self, arr:list[int]) -> int:
        total_sum = 0
        n = len(arr)

        for length in range(1, n + 1, 2):
            for i in range(n - length + 1):
                total_sum += sum(arr[i:i+length])

        return total_sum