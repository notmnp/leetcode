class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in range(len(nums)):
            
            # target - current number = number we need
            # check if number we need is in dict, if found get index
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            
            d[nums[i]] = i

        return []