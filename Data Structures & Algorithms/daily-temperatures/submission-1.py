class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)): 

            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                temp = stack.pop()
                output[temp[1]] = i - temp[1]
            
            stack.append((temperatures[i], i))

        return output