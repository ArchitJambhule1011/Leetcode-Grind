"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

"""
import string

class Solution:
    def toLowercase(self, s: str) -> str:
        capital = list(string.ascii_uppercase)
        small = list(string.ascii_lowercase)

        hash = {}
        for i in range(len(capital)):
            hash[capital[i]] = small[i]

        output = []
        s_str = list(s)
        for i in s_str:
            if i.isupper():
                output.append(hash[i])
            else:
                output.append(i)
        
        return ''.join(i for i in output)