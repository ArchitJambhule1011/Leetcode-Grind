'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".


'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ''
        for i in address :
            if i == '.':
                new_address += '[.]'
            else:
                new_address += i

        return new_address