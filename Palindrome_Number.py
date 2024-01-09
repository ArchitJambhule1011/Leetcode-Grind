class isPalindrome:
    def Palindrome_check(self, x : int) -> bool: 
        x_str = str(x)
        return x_str == x_str[::-1]