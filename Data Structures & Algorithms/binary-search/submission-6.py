class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ub = len(nums)
        lb = 0
        guess = (ub+lb)//2
        
        for i in range(len(nums)):

            if nums[guess] < target: 
                lb = guess
            elif nums[guess] > target:
                ub = guess            
            else: 
                return guess
            guess = (ub+lb)//2
        
        return -1