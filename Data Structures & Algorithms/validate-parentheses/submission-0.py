class Solution:
    def isValid(self, s: str) -> bool:
        start = {'(':')', '{':'}', '[':']'} # {} for set literal
        stack = []

        for char in s:
            if char in start:
                stack.append(char)
            else:
                item = stack.pop()
                if char != item:
                    return False
            return True
        


