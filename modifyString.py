"""
Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
"""

import string
import random

class Solution:
    def modifyString(self, s:str) -> str:
        letters = list(string.ascii_lowercase)
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                new_letter = random.choice(letters)

                while (i > 0 and s[i - 1] == new_letter) or (i < len(s) - 1 and s[i + 1] == new_letter):
                    new_letter = random.choice(letters)

                s[i] = new_letter

        return ''.join(s)