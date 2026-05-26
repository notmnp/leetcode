class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = []
        stack = []
        fleet = 1

        for i in range(len(position)):
            time.append((target-position[i])/speed[i])
        
        for j in range(len(position)):
            stack.append((position[j], time[j]))

        stack.sort()
        print(stack)
        a = stack.pop()

        while len(stack) > 0:
            print(stack)
            b = stack.pop()
            while len(stack) > 0 and (a[0]>=b[0] and a[1]>=b[1] and a[1]>=target):
                b = stack.pop()
            if not (a[0]>=b[0] and a[1]>=b[1]):
                fleet += 1
            a = b
            print(a)
        
        return fleet

       

        return fleet