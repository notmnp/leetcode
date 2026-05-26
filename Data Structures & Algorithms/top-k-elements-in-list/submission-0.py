class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = {}
        o = []

        for i in range(len(nums)):
            
            if nums[i] in n:
                n[nums[i]] += 1                    
            else: 
                n[nums[i]] = 1
            
            if n[nums[i]] == k:
                o.append(nums[i])
        
        return o