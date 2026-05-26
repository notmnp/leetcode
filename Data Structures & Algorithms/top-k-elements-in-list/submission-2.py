class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        count = [[] for i in range(len(nums)+1)]
        output = []

        for i in range(len(nums)):
            if freq.get(nums[i]):
                freq[nums[i]] += 1
            else: 
                freq[nums[i]] = 1
    
        for n, c in freq.items():
            count[c].append(n)
        
        for i in range(len(count)-1, 0, -1):
            for j in range(len(count[i])):
                output.append(count[i][j])
                if len(output) >= k:
                    return output
        
        return output
        
