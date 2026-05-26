class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = []
        final = {}

        for i in range(len(position)):
            time.append((target-position[i])/speed[i])
        
        for j in range(len(position)):
            final[(speed[j]*min(time)+position[j])] = 1

        return len(final)