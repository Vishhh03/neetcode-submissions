class Solution:
    def isValid(self, s: str) -> bool:
        start = {'(':')', '{':'}', '[':']'} # {} for set literal
        stack = []

        for char in s:
            if char in start:
                stack.append(char)
            else:
                if not stack:
                    return False
                item = stack.pop()
                if start[item] != char:
                    return False
        if stack:
            return False
        return True
        


