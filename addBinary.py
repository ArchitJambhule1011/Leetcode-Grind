'Given two binary strings a and b, return their sum as a binary string.'

class Solution:
    def isbinary(self, a:str, b:str) -> str:
        a_dec = int(a,2)
        b_dec = int(b,2)
        res = a_dec + b_dec
        return bin(res).replace('0b','')