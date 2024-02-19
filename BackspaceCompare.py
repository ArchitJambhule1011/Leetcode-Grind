"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    def backspaceCompare(self, s:str, t:str) -> bool:
        def build_string(string):
            stack = []
            for i in string:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return build_string(s) == build_string(t)