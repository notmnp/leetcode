class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        tup = []
        stack = []

        for i in range(len(position)):
            cycles = (target-position[i])/speed[i]
            tup.append((cycles, position[i]))
        st = sorted(tup)

        for i in range(len(tup)):
            
            while (len(stack) > 0) and (stack[-1][0] <= st[i][0]) and (stack[-1][1] <= st[i][1]):
                stack.pop()
            stack.append(st[i])

        return len(stack)