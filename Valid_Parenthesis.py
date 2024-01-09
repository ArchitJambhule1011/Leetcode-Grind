class Solution:
    def isValidParenthesis(self, s : str) -> bool:
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            elif i in brackets.values():
                if not stack or brackets[stack.pop()] != i:
                    return False
            else:
                continue
        
        return not stack