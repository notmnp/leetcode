class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        return (piles[-1]//(h//len(piles)))