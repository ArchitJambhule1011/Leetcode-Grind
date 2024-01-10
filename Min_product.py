# Heap question 
import heapq
''' 
Given an array of n positive integers. We are required to write a program to print the minimum product of k integers of the given array.
'''

class Solution:
    def min_product(self, arr, k):
        heapq.heapify(arr)
        result = 1
        for _ in range(k):
            min_element = heapq.heappop(arr)
            result *= min_element
        
        return result
