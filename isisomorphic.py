"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

"""

class Solution:
    def isisomorphic(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping_s = {}
        mapping_t = {}

        for char_s , char_t in zip(s,t):
            if char_s not in mapping_s:
                mapping_s[char_s] = char_t
            else:
                if mapping_s[char_s] != char_t:
                    return False
                
            if char_t not in mapping_t:
                mapping_t[char_t] = char_s
            else:
                if mapping_t[char_t] != char_s:
                    return False
                
        return True