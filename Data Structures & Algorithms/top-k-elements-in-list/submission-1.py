class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = {}
        o = [[] for x in range(len(nums)+1)]
        a = []

        for i in range(len(nums)):
            
            if nums[i] in n:
                n[nums[i]] += 1                    
            else: 
                n[nums[i]] = 1

        for j in n.keys():

            o[n[j]].append(j)
        
        for q in range (len(o) - 1, 0, -1):
            for num in o[q]: 
                a.append(num)
                if len(a) == k:
                    return a                