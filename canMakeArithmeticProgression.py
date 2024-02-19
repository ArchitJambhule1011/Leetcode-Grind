"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


"""

class Solution:
    def canMakeArithmeticProgression(self, arr : list[int]) -> bool:
        arr.sort()
        output = set()
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            output.add(diff)

        if len(output) == 1:
            return True
        else:
            return False