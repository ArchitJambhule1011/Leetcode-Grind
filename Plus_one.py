""" 
ou are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digit_str = ''.join([str(i) for i in digits])
        digit_int = int(digit_str) + 1
        output = list(str(digit_int))
        output_1 = [int(i) for i in output]

        return output_1