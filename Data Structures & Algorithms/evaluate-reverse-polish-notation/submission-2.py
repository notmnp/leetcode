class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        output = []
        operators = ['+', '-', '*', '/']

        for i in tokens:
            
            total = i
            
            if i in operators: 
                
                a = output.pop()
                b = output.pop()

                if i == "+": 
                    total = a + b
                elif i == "-": 
                    total = b - a
                elif i == "*": 
                    total = a * b
                elif i == "/": 
                    total = b / a
            
            output.append(int(total))

        return output[0]