class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):

            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))
                print(stack)
            
            else: 
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+': 
                    temp = a + b
                elif tokens[i] == '-': 
                    temp = b - a
                elif tokens[i] == '*': 
                    temp = a * b
                elif tokens[i] == '/': 
                    temp = b / a
                stack.append(int(temp))

 
        return stack[0]