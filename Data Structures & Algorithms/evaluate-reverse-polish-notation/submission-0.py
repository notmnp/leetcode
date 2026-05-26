class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        output = []
        for i in tokens:
            total = i
            if i == "+": 
                total = int(output.pop()) + int(output.pop())
            elif i == "-": 
                temp = int(output.pop())
                total = int(output.pop()) - temp
            elif i == "*": 
                total = int(output.pop()) * int(output.pop())
            elif i == "-": 
                temp = int(output.pop())
                total = int(output.pop()) / temp
            
            output.append(total)
        return output[0]