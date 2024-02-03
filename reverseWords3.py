"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""

class Solution:
    def reverseWords(self, s:str) -> str:
        s = list(s.split(' '))
        output = []
        for i in s:
            output.append(i[::-1])

        return ' '.join(i for i in output)