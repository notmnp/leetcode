class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        m = 10000000
        maxProfit = 0
        
        for i in range(len(prices)):

            m = min(prices[i], m)
            maxProfit = max((prices[i]-m), maxProfit)

        return maxProfit