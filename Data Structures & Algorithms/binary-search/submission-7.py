class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ub = len(nums) - 1
        lb = 0
        guess = (ub+lb)//2
        
        for i in range(len(nums)):

            if nums[guess] < target: 
                lb = guess + 1
            elif nums[guess] > target:
                ub = guess - 1        
            else: 
                return guess
            guess = (ub+lb)//2
        
        return -1