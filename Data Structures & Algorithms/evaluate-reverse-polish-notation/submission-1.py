class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(['+','-','*','/'])
        for i in range(len(tokens)):
            if tokens[i] in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == '+':
                    stack.append(int(num2) + int(num1))
                elif tokens[i] == '-':
                    stack.append(int(num2) - int(num1))
                elif tokens[i] == '*':
                    stack.append(int(num2) * int(num1))
                else:
                    stack.append(int(num2) // int(num1))
            else:
                stack.append(tokens[i])
        return int(stack[-1])