class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1 #Since the array is 0 indexed 

        while low <= high:
            mid = (low + high) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1 

        return -1 