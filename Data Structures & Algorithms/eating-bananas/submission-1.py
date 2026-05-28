class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        guess = max(piles)//2

        print(guess)


        while l < r: 
            th = 0
            for i in range(len(piles)):
                # hours per stack
                th += (piles[i] + guess - 1) // guess # rounds up
            if th <= h:
                r = guess            
            else: 
                l = guess + 1
            guess = (l+r)//2 

        return l


