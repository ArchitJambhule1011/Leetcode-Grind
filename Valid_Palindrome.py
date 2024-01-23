"""
Given a string s, return true if it is a palindrome, or false otherwise
"""

class Solution:
    def isPlaindrome(self, s:str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            if not s[low].isalnum():
                low += 1
            elif not s[high].isalnum():
                high -= 1
            elif s[low].lower() == s[high].lower():
                low += 1
                high -= 1
            else:
                return False
            
        return True