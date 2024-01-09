# use sorting to sort the tow strings, if they are same they are anagrams

class Solution:
    def isValidAnagram(s : str, t : str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t 
